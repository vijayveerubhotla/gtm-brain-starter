"""Deterministic illustrative scoring. Local files only; no activation or network calls."""
import argparse,json,math
from datetime import date

def number(value,minimum=0,maximum=None):
    if isinstance(value,bool) or not isinstance(value,(int,float)) or not math.isfinite(value):return None
    if value<minimum or (maximum is not None and value>maximum):return None
    return value

def signal_value(signal,model,as_of):
    if not signal.get('source') or not signal.get('name'):return 0,'Missing signal evidence'
    points=number(signal.get('points'),0,model['signal_max']);confidence=number(signal.get('confidence'),0,1)
    if points is None or confidence is None:return 0,'Invalid signal points or confidence'
    try:age=(as_of-date.fromisoformat(signal['event_date'])).days
    except (ValueError,KeyError,TypeError):return 0,'Invalid event date'
    if age<0:return 0,'Future event date'
    if age>model['signal_expiry_days']:return 0,'Expired signal'
    if confidence<0.5:return 0,'Low-confidence signal needs review'
    return points*confidence*math.pow(0.5,age/model['signal_half_life_days']),f'Age {age} days; confidence {confidence:g}'

def evaluate(account,model,as_of):
    assert sum(model['criteria'].values())==model['fit_max']==70,'Example fit ceiling must match the criterion sum.'
    assert model['signal_max']==30 and model['signal_half_life_days']>0 and model['signal_expiry_days']>=0
    receipt={'domain':account['domain'],'evidence':model['evidence'],'fit':0,'timing':0,'total':0,'reasons':[],'missing':[],'state':'Research','action':'Owner review only; no automatic outreach or CRM write'}
    if account.get('excluded') is True:receipt.update(state='Exclude',reasons=['Explicit company exclusion overrides score']);return receipt
    if account.get('excluded') is not False:receipt['missing'].append('Exclusion state not confirmed')
    features=account.get('features',{})
    for key,points in model['criteria'].items():
        fact=features.get(key,{})
        try:age=(as_of-date.fromisoformat(fact['observed_at'])).days
        except (KeyError,ValueError,TypeError):age=-1
        if type(fact.get('match')) is not bool or not fact.get('source') or age<0 or age>model['feature_max_age_days']:
            receipt['missing'].append(key);continue
        if fact['match']:receipt['fit']+=points
        receipt['reasons'].append(f'{key}: {points if fact["match"] else 0} points, {fact["source"]}, observed {fact["observed_at"]}')
    seen=set();timing=0
    for signal in account.get('signals',[]):
        key=(signal.get('name'),signal.get('event_date'),signal.get('source'))
        if key in seen:continue
        seen.add(key);value,reason=signal_value(signal,model,as_of);timing+=value
        receipt['reasons'].append(f'{signal.get("name","Unknown signal")}: {value:.2f} effective points; {reason}')
        if reason.startswith(('Missing','Invalid','Future','Low-confidence')):receipt['missing'].append(reason)
    receipt['timing']=round(min(model['signal_max'],timing),2);receipt['total']=round(receipt['fit']+receipt['timing'],2)
    if not receipt['missing']:
        for tier in sorted(model['tiers'],key=lambda t:t['minimum'],reverse=True):
            if receipt['total']>=tier['minimum']:receipt['state']=tier['label'];break
    if account.get('contradiction'):receipt['state']='Hold';receipt['reasons'].append('Contradictory evidence requires a person')
    return receipt

def main():
    p=argparse.ArgumentParser();p.add_argument('--input',required=True);p.add_argument('--config',required=True);p.add_argument('--as-of',required=True,type=date.fromisoformat);args=p.parse_args()
    with open(args.input) as f:accounts=json.load(f)
    with open(args.config) as f:model=json.load(f)
    print(json.dumps([evaluate(a,model,args.as_of) for a in accounts],indent=2))

if __name__=='__main__':main()
