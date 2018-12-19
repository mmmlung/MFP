import pandas as pd
import time
import sys
sys.path.insert(0, r'C:/Users/adm-mlung/Desktop/Projekte/MFP/Scripts')
import load_data
import clean_data
import rules_categories
import rules_tags
import tagger_ui
import categorize_ui


def append_data():
    #df = load_data.collect_data_spkr('full', online=True)
    df = pd.read_csv('C:/Users/adm-mlung/Downloads/20181219-48503171-umsatz (1).csv',error_bad_lines=False,
                     encoding='latin1', delimiter=';',  decimal=',')
    de = pd.read_csv("C:/Users/adm-mlung/Desktop/Projekte/Secrets/data/Umsatz_complete/Umsatz_tagged_categorized_09122018.csv")
 
    df = clean_data.clean_data(df)
    de = clean_data.clean_data(de) 

    df.set_index(['Valutadatum', 'Verwendungszweck'], verify_integrity = True, inplace=True)
    de.set_index(['Valutadatum', 'Verwendungszweck'], verify_integrity = True, inplace=True)

    dc = de.combine_first(df)
    dc['Tags'] = dc['Tags'].fillna(' ')
    dc['Category'] = dc['Category'].fillna(' ')

    dc = dc.reset_index()

    dc.to_csv("C:/Users/adm-mlung/Desktop/Projekte/Secrets/data/Updated_Umsatz_"+ str(time.strftime("%d%m%Y")) +".csv")

    return dc

def tag_updated_data_rules(df):
    df.loc[(df.Tags.str.isspace()), 'Tags'] = df.loc[(df.Tags.str.isspace())].apply(rules_tags.rule_based_tagging, axis = 1)
    return df

def categorize_updated_data_rules(df):
    df.loc[(df.Category.str.isspace()), 'Category'] = df.loc[(df.Category.str.isspace())].apply(rules_categories.rule_based_categorizing, axis = 1)
    return df

def tag_updated_data_ui(df):
    (dc, complete) = tagger_ui.tag_data(df)
    return dc

def categorize_updated_data_ui(df):
    (dc, complete) = categorize_ui.categorize_data(df)
    return dc