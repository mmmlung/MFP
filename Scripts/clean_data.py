"""This module cleans my personal banking data off Sparkasse Krefeld."""
import load_data
import rules_tags
import rules_categories
import pandas as pd


def clean_data(dc, date_from = '2018-03-29'):
    dc['Verwendungszweck'] = dc['Verwendungszweck'].fillna(' ')
    dc['Beguenstigter/Zahlungspflichtiger'] = dc['Beguenstigter/Zahlungspflichtiger'].fillna(
        ' ')
    dc['Kontonummer'] = dc['Kontonummer'].fillna(' ')
    dc['BLZ'] = dc['BLZ'].fillna(' ')
    dc = dc.drop(dc[abs(dc['Betrag']) <= 1].index)
    dc['Betrag'] = pd.to_numeric(dc['Betrag'])
    dc['Buchungstag'] = pd.to_datetime(dc['Buchungstag'],dayfirst=True)
    dc['Valutadatum'] = pd.to_datetime(dc['Valutadatum'],dayfirst=True)
    dc = dc[dc['Buchungstag']>date_from]
    return dc


def tag_data(dc):
    dc.insert(8, 'Tags', '')
    dc['Tags'] = dc.apply(rules_tags.rule_based_tagging, axis=1)
    return dc


def categorize_data(dc):
    dc.insert(9, 'Category', '')
    dc['Category'] = dc.apply(rules_categories.rule_based_categorizing, axis=1)
    return dc
