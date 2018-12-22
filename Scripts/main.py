import time
import sys
sys.path.insert(0, r'C:/Users/adm-mlung/Desktop/Projekte/MFP/Scripts')
import load_data
import clean_data
import update_data
import visualize_data
import create_reports

import pandas as pd

def update():
    df = update_data.append_data()
    df = update_data.tag_updated_data_rules(df)
    df = update_data.categorize_updated_data_rules(df)
    df = update_data.tag_updated_data_ui(df)
    df = update_data.categorize_updated_data_ui(df)

    df.to_csv('C:/Users/adm-mlung/Desktop/Projekte/Secrets/data/Umsatz_complete/Umsatz_complete_'+str(time.strftime("%d%m%Y")) +".csv")

    return df


def init():
    df = load_data.collect_data_spkr('full', True)
    print("Success load")
    dc = clean_data.clean_data(df)
    print("Succes clean")
    dd = clean_data.tag_data(dc)
    print('Succsess tagging')
    de = clean_data.categorize_data(dd)
    print('Succes categorizing')
    de = update_data.tag_updated_data_ui(de)
    de = update_data.categorize_updated_data_ui(de)

    de.to_csv('C:/Users/adm-mlung/Desktop/Projekte/Secrets/data/Umsatz_complete/Umsatz_init'+str(time.strftime("%d%m%Y")) +".csv")

    return de

def visualize(df):
    visualize_data.visualize_categories_einnahmen(df)
    visualize_data.visualize_categories_ausgaben(df)

    visualize_data.visualize_einnahmen_weekly(df)
    visualize_data.visualize_ausgaben_weekly(df)


def main():

    initialization = False

    if initialization:
        df = init()
    else:
        df = update()
    
    visualize(df)
    




    # visualize_data.visualize_tags(df)
    # visualize_data.visualize_fixed_variable(df)
    # visualize_data.visualize_miete(df)
    # visualize_data.visualize_versicherungen(df)
    # visualize_data.visualize_zinsen_tilgung(df)
    # visualize_data.visualize_auto(df)


    # create_reports.create_monthly_report(df, week = week)
    # create_reports.create_weekly_report(df, month=month)

    # pfm_dashboard.update_dashboard()

if __name__ == "__main__":
    main()