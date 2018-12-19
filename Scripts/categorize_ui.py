import os
import time
import pandas as pd


def categorize_data(df):

    df['Category'] = df['Category'].fillna('Andere')
    counter_tag = 0
    complete = True

    for index, row in df[df['Category'].str.contains('Andere')].iterrows():
        counter_tag+=1
        print("Der zu kategorisierende Umsatz hat folgende Werte in Tag, Verwendungszweck, Zahlungsempfänger/Begünstiger,Datum und Betrag:")
        print(row['Tags'])
        print(row['Verwendungszweck'])
        print(row['Beguenstigter/Zahlungspflichtiger'])
        print(row['Buchungstag'])
        print(row['Betrag'])
        print('Bitte die passende Kategorie ein ein !')
        category = input()
        if category not in ['Gehalt Lilly'
                ,'Gehalt Keksi'
                ,'Einzahlung'
                ,'Sonstige'
                ,'Miete'
                ,'Versicherungen'
                ,'Einkäufe(Haushalt)'
                ,'Einkäufe(Klamotten)'
                ,'Einkäufe(Sonstiges)'
                ,'Bargeldauszahlungen'
                ,'Tilgung&Zinsen'
                ,'Altervorsorge'
                ,'Telefon+Internet'
                ,'Sparen'
                ,'Reisen'
                ,'Ausgehen'
                ,'Medien (Bücher, Zeitungen, Streaming)'
                ,'Wohnnebenkosten'
                ,'PayPal'
                ,'Transport(ÖPNV,Parken)'
                ,'Gesundheit/Ärzte/Kliniken'
                ,'Kreditkarte'
                ,'And.'
                ,'Auto'
        ]:
            print('Diese Kategorisierung hast du verbockt. Komm nochmal wieder um es richtig zu machen !')
            complete = False
            continue
        df.at[index,'Category'] = category

        if counter_tag % 5 == 0:
            print('Du hast noch '+ str(len(df[df['Category'].str.contains('Andere')])) + ' Umsätze vor dir.')
            print('Hast du genug ? Falls ja, gib "ja" ein')
            aufhören = input()
            if aufhören == 'ja':
                complete = False
                break

    return (df,complete)
#
#
##Lade durch Rules kategorisierte Umsätze:
#df = pd.read_csv('C:/Users/adm-mlung/Desktop/Projekte/Secrets/data/Umsatz_clean.csv')
#df = df.drop(['Unnamed: 0'], axis=1)
#df['Category'] = df['Category'].fillna('Andere')
#
## Berechne zu taggende Umsätze
#
#counter_tag = 0
#
##Beginne User-Interaction zum Taggen der Umsätze
#for index, row in df[df['Category'].str.contains('Andere')].iterrows():
#    counter_tag+=1
#    print("Der zu kategorisierende Umsatz hat folgende Werte in Tag, Verwendungszweck, Zahlungsempfänger/Begünstiger,Datum und Betrag:")
#    print(row['Tags'])
#    print(row['Verwendungszweck'])
#    print(row['Beguenstigter/Zahlungspflichtiger'])
#    print(row['Buchungstag'])
#    print(row['Betrag'])
#    print('Bitte die passende Kategorie ein ein !')
#    category = input()
#    if category not in ['Gehalt Lilly'
#             ,'Gehalt Keksi'
#             ,'Einzahlung'
#             ,'Sonstige'
#             ,'Miete'
#             ,'Versicherungen'
#             ,'Einkäufe(Haushalt)'
#             ,'Einkäufe(Klamotten)'
#             ,'Einkäufe(Sonstiges)'
#             ,'Bargeldauszahlungen'
#             ,'Tilgung&Zinsen'
#             ,'Altervorsorge'
#             ,'Telefon+Internet'
#             ,'Sparen'
#             ,'Reisen'
#             ,'Ausgehen'
#             ,'Medien (Bücher, Zeitungen, Streaming)'
#             ,'Wohnnebenkosten'
#             ,'PayPal'
#             ,'Transport(ÖPNV,Parken)'
#             ,'Gesundheit/Ärzte/Kliniken'
#             ,'Kreditkarte'
#             ,'And.'
#             ,'Auto'
#    ]:
#        print('Diese Kategorisierung hast du verbockt. Komm nochmal wieder um es richtig zu machen !')
#        continue
#    df.at[index,'Category'] = category
#
#    if counter_tag % 5 == 0:
#        print('Du hast noch '+ str(len(df[df['Category'].str.contains('Andere')])) + ' Umsätze vor dir.')
#        print('Hast du genug ? Falls ja, gib "ja" ein')
#        aufhören = input()
#        if aufhören == 'ja':
#            break
#df.to_csv('C:/Users/adm-mlung/Desktop/Projekte/Secrets/data/Update_Category' + str(time.time())+ '.csv')
#
#print('Sehr fleißig ! Du hast alle Umsätze kategorisiert')