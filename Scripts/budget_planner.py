import yaml
import pandas as pd
from recurrent import RecurringEvent
from dateutil import rrule
from matplotlib import pyplot as plt
import time

import sys
sys.path.insert(0, r'C:/Users/adm-mlung/Desktop/Projekte/MFP/Scripts')
import load_data

def get_dates(freq, Start, End):
    try:
        return [pd.Timestamp(freq).normalize()]
    except ValueError:
        pass
    try: 
        return pd.date_range(start=Start, end=End, freq=freq)
    except ValueError:
        pass
    try:
        r = RecurringEvent()
        r.parse(freq)
        rr = rrule.rrulestr(r.get_RFC_rrule())
        return [
            pd.to_datetime(date).normalize()
            for date in rr.between(Start, End)
        ]
    except ValueError as e:
        raise ValueError('Invalid frequency')

def build_calendar(budget, Start, End):
    
    calendar = pd.DataFrame(index=pd.date_range(start=Start, end = End))

    for key, value in budget.items():
        frequency = value.get('frequency')
        amount = value.get('amount')
        dates = get_dates(frequency,Start, End)
        cashflows = pd.DataFrame(
            data={key:amount},
            index=pd.DatetimeIndex(pd.Series(dates))
        )
        calendar = pd.concat([calendar, cashflows], axis = 1).fillna(0)
    
    calendar['total'] = calendar.sum(axis=1)
    calendar['cum_total'] = calendar['total'].cumsum()

    return calendar


def plot_budget(calendar, Auto):
    plt.figure(figsize=(10, 5))
    plt.plot(calendar.index, calendar.total, label='Daily Total')
    plt.plot(calendar.index, calendar.cum_total, label='Cumulative Total')
    plt.legend()
    if Auto:
        plt.savefig('C:/Users/adm-mlung/Desktop/Projekte/Secrets/plots/Budgets/Auto/Budget_auto_'+ str(time.strftime("%d%m%Y")))
    else:
        plt.savefig('C:/Users/adm-mlung/Desktop/Projekte/Secrets/plots/Budgets/Manuell/Budget_manu_'+ str(time.strftime("%d%m%Y")))
    
def get_monthly_mean(dg, Category):
    ds = dg[dg['Category']==Category]
    ds = ds[['Valutadatum','Betrag']]
    ds['Valutadatum'] = pd.to_datetime(ds['Valutadatum'])
    ds.index = ds['Valutadatum']
    ds = ds.resample('M').sum()
    average = sum(ds['Betrag']/len(ds))
       
    return average  

def create_budget_yaml_auto():

    baseline_path = load_data.get_newest_download('C:/Users/adm-mlung/Desktop/Projekte/Secrets/data/Umsatz_complete')
    df = pd.read_csv(baseline_path)

    Ausgaben = df[df['Betrag']<0].copy()
    categories = set(Ausgaben.Category)
    yaml_dict = {}
    for cat in categories:
        content = {'frequency': 'MS',
            'amount': get_monthly_mean(Ausgaben, cat)}
        yaml_dict[cat] = content 

    

    Einnahmen = df[df['Betrag']>0].copy()
    categories = set(Einnahmen.Category)
    for cat in categories:
        content = {'frequency': 'MS',
        'amount': get_monthly_mean(Einnahmen, cat)}
        yaml_dict[cat] = content

    with open('C:/Users/adm-mlung/Desktop/Projekte/Secrets/data/Budgets/Budget_2019_auto/Budget_2019_auto.yml', 'w') as outfile:
        yaml.dump(yaml_dict, outfile, default_flow_style=False,  allow_unicode=True) 

def main():
    Start = pd.Timestamp(2019, 1, 1).normalize()
    End = pd.Timestamp(2019, 8, 1).normalize()

    create_budget_yaml_auto()

    with open('C:/Users/adm-mlung/Desktop/Projekte/Secrets/data/Budgets/Budget_2019_manu/Budget_2019_manu.yaml','r') as f_manu:
        budget_manu = yaml.load(f_manu)

    with open('C:/Users/adm-mlung/Desktop/Projekte/Secrets/data/Budgets/Budget_2019_auto/Budget_2019_auto.yml','r') as f_auto:
         budget_auto = yaml.load(f_auto)

    calendar_manu = build_calendar(budget_manu, Start, End)
    calendar_auto = build_calendar(budget_auto, Start, End)

    calendar_manu.to_csv('C:/Users/adm-mlung/Desktop/Projekte/Secrets/data/CashFlowCalendars/CFC_MANU_'+ str(time.strftime("%d%m%Y"))+ '.csv' )
    calendar_auto.to_csv('C:/Users/adm-mlung/Desktop/Projekte/Secrets/data/CashFlowCalendars/CFC_AUTO_'+ str(time.strftime("%d%m%Y"))+ '.csv' )

    plot_budget(calendar_manu, Auto=False)
    plot_budget(calendar_auto, Auto=True)


if __name__ == "__main__":
    main()
