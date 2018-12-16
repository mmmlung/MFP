"""This module loads my personal banking data off Sparkasse Krefeld."""
import os
import time

import pandas as pd
from dotenv import load_dotenv
from webbot import Browser

#import gspread
#from oauth2client.service_account import ServiceAccountCredentials

load_dotenv(
    dotenv_path="C:/Users/adm-mlung/Desktop/Projekte/MFP/Secrets/secrets.env", verbose=True)
Anmeldename = os.environ.get('Anmeldename')
PIN = os.environ.get('Pin')
PATH_DOWNLOADS = "C:/Users/adm-mlung/Downloads"


def get_newest_download(path):
    files = os.listdir(path)
    paths = [os.path.join(path, basename) for basename in files]
    return max(paths, key=os.path.getctime)




def collect_data_spkr(date_mode, online):

    if date_mode == 'full' and online:
        web = Browser(showWindow=True)
        web.go_to('https://www.sparkasse-krefeld.de/de/home.html')
        web.type(Anmeldename, into='Anmeldename')
        web.type(PIN, into='PIN')
        web.click('Anmelden')
        web.click('Kontostand/Umsatzanzeige')
        web.type('01.01.2018', into='Zeitraum', clear=True)
        web.click('Export')
        web.click('CSV-MT940 Format')
        time.sleep(10)
        web.click('Abmelden')

    data_csv_path = get_newest_download(PATH_DOWNLOADS)
    df = pd.read_csv(data_csv_path, error_bad_lines=False,
                     encoding='latin1', delimiter=';',  decimal=',')
    df.set_index(['Valutadatum', 'Verwendungszweck'])
    df.to_csv("C:/Users/adm-mlung/Desktop/Projekte/MFP/data/Umsatz_raw.csv")
    return df

def append_data():
    df = collect_data_spkr('full', online=True)
    de = pd.read_csv("C:/Users/adm-mlung/Desktop/Projekte/MFP/data/Umsatz_tagged_categorized_09122018.csv")
 
    df.set_index(['Valutadatum', 'Verwendungszweck'], verify_integrity = True)
    de.set_index(['Valutadatum', 'Verwendungszweck'], verify_integrity = True)

    df.append(de, verify_integrity = True, ignore_index = True)

    return de



#df = collect_data_spkr('full', True)
# print(df.head())

#     Code-Schnipsel zum schreiben in Google Drive
#     scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
#     credentials = ServiceAccountCredentials.from_json_keyfile_name("C:/Users/adm-mlung/Desktop/Projekte/Python-204bbd31dbcc.json", scope)

#     gc = gspread.authorize(credentials)
#     content = open("C:/Users/adm-mlung/Desktop/Umsatz.csv",'r').read()

#     sheet = gc.create(title="Umsatz")
#     gc.import_csv(sheet.id,data=content)

#     sheet.share('mattlung05@googlemail.com', perm_type='user', role='writer')


# Workflow/Features
#    1. Analyse der Umsätze des letzten Jahres
#    2. Wöchentlicher Report über Umsätze. Möglichst per Mail an mich
#    3. Integration mit Budget-Tool
#    4. Integration mit anderen Finanzportalen (KFW, Schwäbisch Hall)
