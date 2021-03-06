"""This module loads my personal banking data off Sparkasse Krefeld."""
import os
import time

import pandas as pd
from dotenv import load_dotenv
from webbot import Browser

#import gspread
#from oauth2client.service_account import ServiceAccountCredentials

load_dotenv(dotenv_path="C:/Users/adm-mlung/Desktop/Projekte/Secrets/secrets.env", verbose=True)
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
        web.click('CSV-MT940-Format')
        time.sleep(5)
        web.click('Abmelden')

    data_csv_path = get_newest_download(PATH_DOWNLOADS)
    df = pd.read_csv(data_csv_path, error_bad_lines=False,
                     encoding='latin1', delimiter=';',  decimal=',')
    df.set_index(['Valutadatum', 'Verwendungszweck'])
    df.to_csv("C:/Users/adm-mlung/Desktop/Projekte/Secrets/data/Umsatz_raw.csv")
    return df
