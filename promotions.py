"""Resolve task cost at a supplied UTC time without mutating source evidence."""
from datetime import datetime,timezone

def effective_cost(row,promotions,at=None):
 cost=row.get('cost')
 promo=next((p for p in promotions if p['id']==row.get('promotion_id')),None)
 if cost is None or promo is None:return cost
 at=at or datetime.now(timezone.utc)
 parse=lambda s:datetime.fromisoformat(s.replace('Z','+00:00'))
 active=(not promo.get('starts_at') or at>=parse(promo['starts_at'])) and at<parse(promo['ends_at'])
 factor=promo['promotional_multiplier'] if active else 1
 return round(cost*factor/row['reported_cost_multiplier'],6)

def validate_promotions(data):
 seen=set()
 for promo in data.get('promotions',[]):
  if promo['id'] in seen:raise ValueError('Duplicate promotion ID')
  seen.add(promo['id'])
  end=datetime.fromisoformat(promo['ends_at'].replace('Z','+00:00'))
  if end.tzinfo is None:raise ValueError('Expiry requires timezone')
  if not 0<promo['promotional_multiplier']<1:raise ValueError('Invalid discount')
  if not promo['source'].startswith('https://'):raise ValueError('Promotion requires official HTTPS source')
  for kind,standard in promo['standard_rates'].items():
   if standard<=0 or abs(promo['promotional_rates'][kind]/standard-promo['promotional_multiplier'])>1e-9:raise ValueError('Nonuniform token discount needs a token-weighted calculation')
 for row in data['aa']:
  if row.get('promotion_id'):
   if row['promotion_id'] not in seen or row.get('reported_cost_multiplier',0)<=0:raise ValueError('Missing cost pricing basis')
