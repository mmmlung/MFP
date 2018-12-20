def rule_based_categorizing(row):
    category = 'Andere'

    if 'Einzahlung' in row['Tags']:
        category = 'Einzahlung'
    if 'Aldi' in row['Tags']:
        category = 'Einkäufe(Haushalt)'
    if 'Netto' in row['Tags']:
        category = 'Einkäufe(Haushalt)'
    if 'Bargeldauszahlung' in row['Tags'] and not 'umbuchung' in row['Verwendungszweck'].lower():
        category = 'Bargeldauszahlung'
    if 'umbuchung' in row['Verwendungszweck'].lower():
        category='Sparen'
    if 'Audible' in row['Tags']:
        category = 'Medien (Bücher, Zeitungen, Streaming)'
    if 'SWK' in row['Tags']:
        category = 'Wohnnebenkosten'
    if 'Radversicherung' in row['Tags']:
        category = 'Versicherungen'
    if 'Miete' in row['Tags']:
        category = 'Miete'
    if 'Getränke' in row['Tags']:
        category = 'Einkäufe(Haushalt)'
    if 'Reinigung' in row['Tags']:
        category = 'Einkäufe(Haushalt)'
    if 'Bausparen' in row['Tags']:
            category = 'Sparen'
    if 'Autohaus' in row['Tags']:
        category = 'Auto'
    if 'Tanken' in row['Tags']:
        category = 'Auto'
    if 'PayPal' in row['Tags']:
        category = 'PayPal'
    if 'UniKid' in row['Tags']:
        category = 'Gesundheit/Ärzte/Kliniken'
    if 'VodafoneZahlung' in row['Tags']:
            category = 'Telefon+Internet'  
    if 'AutokreditLilly' in row['Tags']:
        category = 'Tilgung&Zinsen'
    if 'Altervorsorge' in row['Tags']:
        category = 'Altervorsorge'
    if 'GebührenParken' in row['Tags']:
        category = 'Transport(ÖPNV,Parken)'
    if 'Telefonica' in row['Tags']:
        category = 'Telefon+Internet'
    if 'Ausgehen' in row['Tags']:
            category = 'Ausgehen'
    if 'Kreditkarte' in row['Tags']:
        category = 'Kreditkarte'
    if 'Ikea' in row['Tags']:
        category = 'Einkäufe(Sonstiges)'
    if 'GehaltLilly' in row['Tags']:
        category = 'Gehalt Lilly'
    if 'GebührenStandesamt' in row['Tags']:
        category = 'Anderes'
    if 'Tanken' in row['Tags']:
            category = 'Auto'
    if 'DeutscheBahn' in row['Tags']:
        category = 'Transport(ÖPNV,Parken)'
    if 'REWE' in row['Tags']:
        category = 'Einkäufe(Haushalt)'
    if 'BücherZeitungen' in row['Tags']:
        category = 'Medien (Bücher, Zeitungen, Streaming)'
    if 'Kaufhof' in row['Tags']:
        category = 'Einkäufe(Klamotten)'
    if 'Möbel' in row['Tags']:
        category = 'Einkäufe(Sonstiges)'
    if 'Sparbuch' in row['Tags']:
        category = 'Sparen'
    if 'Fitnessstudio' in row['Tags']:
        category = 'Gesundheit/Ärzte/Kliniken'
    if 'Schwimmen' in row['Tags']:
        category = 'Gesundheit/Ärzte/Kliniken'
    if 'Apotheke' in row['Tags']:
        category = 'Gesundheit/Ärzte/Kliniken'
    if 'TilgungBafög' in row['Tags']:
        category = 'Tilgung&Zinsen'
    if 'LeasingMatthias' in row['Tags']:
        category = 'Tilgung&Zinsen'
    if 'TilgungKFW' in row['Tags']:
        category = 'Tilgung&Zinsen'
    if 'ReiseDelft' in row['Tags']:
        category = 'Reisen'
    if 'Amazon' in row['Tags']:
        category = 'Einkäufe(Sonstiges)'
    if 'GehaltMatthias' in row['Tags']:
        category = 'Gehalt Matthias'
    if 'Sport' in row['Tags']:
        category = 'Transport(ÖPNV,Parken)'
    if 'ÖPNV' in row['Tags']:
        category = 'Gesundheit/Ärzte/Kliniken'
    if 'DMMarkt' in row['Tags']:
        category = 'Einkäufe(Haushalt)'
    if 'Taxi' in row['Tags']:
        category = 'Transport(ÖPNV,Parken)'
    if 'Baumarkt' in row['Tags']:
        category = 'Einkäufe(Sonstiges)' 
    if 'Edeka' in row['Tags']:
        category = 'Einkäufe(Haushalt)'
    if 'KaisersMarkt' in row['Tags']:
        category = 'Einkäufe(Haushalt)' 
    if 'AbrechnungStadtMeerbusch' in row['Tags']:
        category = 'Gehalt Lilly'
    if 'Friseur' in row['Tags']:
        category = 'Einkäufe(Sonstiges)' 
    if 'Getränke' in row['Tags']:
        category = 'Einkäufe(Haushalt)'
    if 'RealMarkt' in row['Tags']:
        category = 'Einkäufe(Haushalt)'
    if 'GEZ' in row['Tags']:
        category = 'Medien (Bücher, Zeitungen, Streaming)'
    if 'TKMAXX' in row['Tags']:
        category = 'Einkäufe(Klamotten)'
    if 'IdeeMarkt' in row['Tags']:
        category = 'Einkäufe(Sonstiges)'
    if 'Esprit' in row['Tags']:
        category = 'Einkäufe(Klamotten)'
    if 'LondonAIConf' in row['Tags']:
        category = 'Reisen'
    if 'SuitSupply' in row['Tags']:
        category = 'Einkäufe(Klamotten)'
    if 'ReiseEgmond' in row['Tags']:
        category = 'Reisen'
    if 'Bäcker' in row['Tags']:
        category = 'Einkäufe(Haushalt)'
    if 'ReiseLondon' in row['Tags']:
        category = 'Reisen'
    if 'ShoppingRoermond' in row['Tags']:
        category = 'Einkäufe(Klamotten)'
    if 'Lasertag' in row['Tags']:
        category = 'Ausgehen'
    if 'ReiseDenHaag' in row['Tags']:
        category = 'Reisen'
    if 'Primark' in row['Tags']:
        category = 'Einkäufe(Klamotten)'
    if 'Kosmetik' in row['Tags']:
        category = 'Einkäufe(Sonstiges)'
    if 'Venlo' in row['Tags']:
        category = 'Reisen'
    if 'AugsburgMarkt' in row['Tags']:
        category = 'Einkäufe(Sonstiges)'
    if 'MediaMarkt' in row['Tags']:
        category = 'Einkäufe(Sonstiges)'
    if 'RossmannMarkt' in row['Tags']:
        category = 'Einkäufe(Haushalt)'
    if 'ActionMarkt' in row['Tags']:
        category = ' Einkäufe(Sonstiges)'
    if 'ÜbertragKontoZusammenlegung' in row['Tags']:
        category = 'Sonstige'
    if 'TicketSWK' in row['Tags']:
        category = 'Transport(ÖPNV,Parken)'
    if 'VersicherungAuto' in row['Tags']:
        category = 'Versicherungen'
    if 'SchuheMatthias' in row['Tags']:
        category = 'Einkäufe(Klamotten)'
    if 'VersicherungAllianz' in row['Tags']:
        category = 'Versicherungen'
    if 'BafögMatthias' in row['Tags']:
        category = 'Tilgung&Zinsen'
    if 'KostenKryoBonn' in row['Tags']:
        category = 'Gesundheit/Ärzte/Kliniken'
    if 'SonderTilgungBafögLilly' in row['Tags']:
        category = 'Tilgung&Zinsen'
    if 'MedikamenteKinderwunsch' in row['Tags']:
        category = 'Gesundheit/Ärzte/Kliniken'
    if 'FahrradLilly' in row['Tags']:
        category = 'Einkäufe(Sonstiges)'
    if 'WellnessKraehennest' in row['Tags']:
        category = 'Reisen'
    if 'PachtHütte' in row['Tags']:
        category = 'Einkäufe(Sonstiges)'
    if 'HotelLondon' in row['Tags']:
        category = 'Reisen'
    if 'HotelHochzeitMaike' in row['Tags']:
        category = 'Reisen'
    if 'KfzSteuerLilly' in row['Tags']:
        category = 'Auto'
    if 'RestaurantStadtwald' in row['Tags']:
        category = 'Ausgehen'
    if 'KlamottenLilly' in row['Tags']:
        category = 'Klamotten'
    if 'ÜberraschungLilly' in row['Tags']:
        category = 'Einkäufe(Sonstiges)'
    if 'GeschenkBrauns' in row['Tags']:
        category = 'Einkäufe(Sonstiges)'
    if 'Klamotten' in row['Tags']:
        category = 'Einkäufe(Klamotten)'
    if 'RestaurantNordbahnhof' in row['Tags']:
        category = 'Ausgehen'
    if 'GeschenkMaikeHochzeit' in row['Tags']:
        category = 'Einkäufe(Sonstiges)'
    if 'Metro' in row['Tags']:
        category = 'Einkäufe(Haushalt)'
    return category

# - Einnahmen: (4)
#             - Gehalt Lilly
#             - Gehalt Keksi
#             - Einzahlung
#             - Sonstige
# - Ausgaben:(20)
#             - Miete
#             - Versicherungen
#             - Einkäufe(Haushalt)
#             - Einkäufe(Klamotten)
#             - Einkäufe(Sonstiges)
#             - Bargeldauszahlungen
#             - Tilgung&Zinsen
#             - Altervorsorge
#             - Telefon+Internet
#             - Sparen
#             - Reisen
#             - Ausgehen
#             - Medien (Bücher, Zeitungen, Streaming)
#             - Wohnnebenkosten
#             - PayPal
#             - Transport(ÖPNV,Parken)
#             - Gesundheit/Ärzte/Kliniken
#             - Kreditkarte
#             - Anderes
#             - Auto