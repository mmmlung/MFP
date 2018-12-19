import os
import time
import pandas as pd


def tag_data(df):

    df['Category'] = df['Category'].fillna(' ')

    counter_tag = 0
    complete = True

    for index, row in df[df['Tags'].str.isspace()].iterrows():
        counter_tag+=1
        print("Der zu taggende Umsatz hat folgende Werte im Verwendungszweck, Zahlungsempfänger/Begünstiger,Datum und Betrag:")
        print(row['Verwendungszweck'])
        print(row['Beguenstigter/Zahlungspflichtiger'])
        print(row['Buchungstag'])
        print(row['Betrag'])
        print('Bitte gibt das passende Tag ein !')
        tag = input()
        df.at[index,'Tags'] = tag

        if counter_tag % 5 == 0:
            print('Du hast noch ' + str(len(df[df['Tags'].str.isspace()])) + ' zu taggende Umsätze vor dir.')
            print('Hast du genug ? Falls ja, gib "ja" ein')
            aufhören = input()
            if aufhören == 'ja':
                complete = False
                break

    return (df,complete)