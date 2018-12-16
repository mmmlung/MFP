import os
import time
import pandas as pd

#Lade durch Rules getaggte Umsätze:
df = pd.read_csv('C:/Users/adm-mlung/Desktop/Projekte/MFP/data/Umsatz_clean.csv')
df = df.drop(['Unnamed: 0'], axis=1)
df['Category'] = df['Category'].fillna(' ')

# Berechne zu taggende Umsätze

counter_tag = 0

#Beginne User-Interaction zum Taggen der Umsätze
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
            break
df.to_csv('C:/Users/adm-mlung/Desktop/Projekte/MFP/data/Update_Tag' + str(time.time())+ '.csv')

print('Sehr fleißig ! Du hast alle Umsätze getaggt')