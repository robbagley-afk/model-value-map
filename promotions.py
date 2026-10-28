"""Resolve task cost at a supplied UTC time without mutating source evidence."""
from datetime import datetime,timezone,timedelta
import copy

def visible_offers(offers,at=None,grace_days=7):
 at=at or datetime.now(timezone.utc)
 if at.tzinfo is None or at.utcoffset() is None:raise ValueError('Offer cleanup requires timezone-aware clock')
 out=[]
 for offer in offers:
  end=datetime.fromisoformat(offer['ends_at'].replace('Z','+00:00'))
  if end.tzinfo is None:raise ValueError('Offer expiry requires timezone')
  if at<end+timedelta(days=grace_days):out.append(offer)
 return out

def public_model_data(data,at=None):
 out=copy.deepcopy(data)
 # Fresh public snapshots omit expired recommendations immediately. Private history stays intact.
 out['subscription_promotions']=visible_offers(out.get('subscription_promotions',[]),at,grace_days=0)
 return out

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
 for b in data.get('api_credit_benefits',[]):
  if not b['source'].startswith('https://') or not b.get('expiry') or not b.get('eligibility'):raise ValueError('API credits require source and cycle/eligibility terms')
  if not b.get('amounts_usd') or any(not isinstance(v,(float,int)) or isinstance(v,bool) or v<=0 for v in b['amounts_usd'].values()):raise ValueError('API credit amounts must be positive')
  if b.get('team_pool_cap_usd',0)<=0:raise ValueError('API credit pool cap must be positive')
 for offer in data.get('subscription_promotions',[]):
  if offer.get('api_applies') is not False:raise ValueError('Non-API offers require explicit API exclusion')
  if not offer['source'].startswith('https://'):raise ValueError('Usage offer requires HTTPS source')
  for key in ['starts_at','ends_at']:
   if datetime.fromisoformat(offer[key].replace('Z','+00:00')).tzinfo is None:raise ValueError('Usage offer requires timezone')
  if offer['ends_at']<=offer['starts_at']:raise ValueError('Invalid usage offer range')
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
