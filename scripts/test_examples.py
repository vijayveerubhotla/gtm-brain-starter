"""Exercise meaningful boundaries of the illustrative model, not its wording."""
from evaluate_example import evaluate,signal_value
from pathlib import Path
from datetime import date
import copy,json

root=Path(__file__).resolve().parents[1];model=json.loads((root/'examples/model.json').read_text());accounts=json.loads((root/'examples/accounts.json').read_text());today=date(2026,10,8)
strong=evaluate(accounts[0],model,today);assert strong['fit']==70 and strong['timing']==20 and strong['state']=='Priority review'
assert evaluate(accounts[1],model,today)['state']=='Research'
assert evaluate(accounts[2],model,today)['state']=='Exclude'
signal=accounts[0]['signals'][0]
old=copy.deepcopy(signal);old['event_date']='2026-09-08';assert signal_value(old,model,today)[0]==10
old['event_date']='2025-10-08';assert signal_value(old,model,today)[1]=='Expired signal'
future=copy.deepcopy(signal);future['event_date']='2026-10-09';assert signal_value(future,model,today)[0]==0
invalid=copy.deepcopy(signal);invalid['event_date']='bad-date';assert signal_value(invalid,model,today)[0]==0
invalid['event_date']='2026-10-08';invalid['confidence']=1.5;assert signal_value(invalid,model,today)[0]==0
invalid['confidence']=0.2;assert signal_value(invalid,model,today)[0]==0
invalid['confidence']=1;invalid['points']=-1;assert signal_value(invalid,model,today)[0]==0
duplicate=copy.deepcopy(accounts[0]);duplicate['signals']*=2;assert evaluate(duplicate,model,today)['timing']==20
cap=copy.deepcopy(accounts[0]);cap['signals'] += [dict(signal,name='Different synthetic event')];assert evaluate(cap,model,today)['timing']==30
fake=copy.deepcopy(accounts[0]);fake['features']['size']['match']='false';assert evaluate(fake,model,today)['state']=='Research'
fake=copy.deepcopy(accounts[0]);fake['features']['size']['source']='';assert evaluate(fake,model,today)['state']=='Research'
fake=copy.deepcopy(accounts[0]);fake['contradiction']=True;assert evaluate(fake,model,today)['state']=='Hold'
stale=copy.deepcopy(accounts[0]);stale['features']['size']['observed_at']='2026-01-01';assert evaluate(stale,model,today)['state']=='Research'
print('PASS: 16 fit, evidence, decay, expiry, duplicate, cap, exclusion and contradiction checks. No live-system action.')
