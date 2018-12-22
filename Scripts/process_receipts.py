import pandas as pd
import time
import sys
sys.path.insert(0, r'C:/Users/adm-mlung/Desktop/Projekte/MFP/Scripts')
import load_data

def insert_bar_belege_sum_bar():

    df_belege = pd.read_excel('C:/Users/adm-mlung/Desktop/Projekte/Secrets/data/Bargeld_Belege/Belege.xlsx').fillna(' ')
    path_umsatze = 'C:/Users/adm-mlung/Desktop/Projekte/Secrets/data/Umsatz_complete/'
    path_newest_umsatz = load_data.get_newest_download(path_umsatze)
    df_umsatze = pd.read_csv(path_newest_umsatz)

    df_umsatze_ohne_bar = df_umsatze[df_umsatze['Category'] != 'Bargeldauszahlung']
    df_umsatze_bar = df_umsatze[df_umsatze['Category'] == 'Bargeldauszahlung']
    df_umsatz_ohne_bar_mit_belege = df_umsatze_ohne_bar.append(df_belege, sort = False)

    sum_Bar_ohne_Beleg = sum(df_umsatze_bar['Betrag']) - sum(df_belege['Betrag'])

    Umsatz_Bar_ohne_Beleg = {
    'Valutadatum' : [str(time.strftime("%d%m%Y"))],
    'Betrag': [sum_Bar_ohne_Beleg],
    'Buchungstext': ['Verrechnung Bargeld'],
    'Category': ['Bargeldauszahlung'],
    'Tag':['Verrechnung Bargeld']
    }

    df_umsatz_bar_ohne_Belege = pd.DataFrame.from_dict(Umsatz_Bar_ohne_Beleg)

    df_cleaned = df_umsatz_ohne_bar_mit_belege.append(df_umsatz_bar_ohne_Belege,sort=False).fillna(' ')

    df_cleaned.to_csv('C:/Users/adm-mlung/Desktop/Projekte/Secrets/data/Umsatz mit Belegen/Umsatz_mit_Belegen_'+str(time.strftime("%d%m%Y"))+'.csv')

    return df_cleaned

def main():
    insert_bar_belege_sum_bar()

if __name__ == "__main__":
    main()