def rule_based_tagging(row):
    tags_collection = " "
    if 'EINZAHLUNG' in row['Buchungstext']:
        tags_collection += ' Einzahlung'
    if 'ALDI' in row['Beguenstigter/Zahlungspflichtiger']:
        tags_collection += ' Aldi'
    if 'NETTO' in row['Beguenstigter/Zahlungspflichtiger']:
        tags_collection += ' Netto'
    if 'BARGELDAUSZAHLUNG' in row['Buchungstext']:
        tags_collection += ' Bargeldauszahlung'
    if 'AUDIBLE' in row['Beguenstigter/Zahlungspflichtiger']:
        tags_collection += ' Audible'
    if 'SWK' in row['Beguenstigter/Zahlungspflichtiger']:
        tags_collection += ' SWK'
    if 'WERTGARANTIE' in row['Beguenstigter/Zahlungspflichtiger']:
        tags_collection += ' Radversicherung'
    if 'Miete' in row['Verwendungszweck']:
        tags_collection += ' Miete'
    if 'TRINK' in row['Beguenstigter/Zahlungspflichtiger']:
        tags_collection += ' Getränke'
    if 'REINIGUNG' in row['Verwendungszweck']:
        tags_collection += ' Reinigung'
    if 'Bausparkasse' in row['Beguenstigter/Zahlungspflichtiger']:
        tags_collection += ' Bausparen'
    if 'AUTOHAUS' in row['Beguenstigter/Zahlungspflichtiger']:
        tags_collection += ' Autohaus'
    if 'Orlen' in row['Beguenstigter/Zahlungspflichtiger']:
        tags_collection += ' Tanken'
    if 'PayPal' in row['Beguenstigter/Zahlungspflichtiger']:
        tags_collection += ' PayPal'
    if 'Unikid' in row['Beguenstigter/Zahlungspflichtiger']:
        tags_collection += ' UniKid'
    if 'vodafone' in row['Beguenstigter/Zahlungspflichtiger'].lower():
        tags_collection += ' VodafoneZahlung'
    if 'SANTANDER' in row['Beguenstigter/Zahlungspflichtiger']:
        tags_collection += ' AutokreditLilly'
    if 'Provinzial' in row['Beguenstigter/Zahlungspflichtiger']:
        tags_collection += ' Altervorsorge'
    if 'PARKEN' in row['Beguenstigter/Zahlungspflichtiger']:
        tags_collection += ' GebührenParken'
    if 'Telefonica' in row['Beguenstigter/Zahlungspflichtiger']:
        tags_collection += ' Telefonica'
    if 'Kornblume' in row['Beguenstigter/Zahlungspflichtiger']:
        tags_collection += ' Ausgehen'
    if 'KREDITKARTENABRECHNUNG' in row['Beguenstigter/Zahlungspflichtiger']:
        tags_collection += ' Kreditkarte'
    if 'IKEA' in row['Beguenstigter/Zahlungspflichtiger']:
        tags_collection += ' Ikea'
    if 'Hildegundis' in row['Beguenstigter/Zahlungspflichtiger']:
        tags_collection += ' GehaltLilly'
    if 'STANDESAMT' in row['Beguenstigter/Zahlungspflichtiger']:
        tags_collection += ' GebührenStandesamt'
    if 'Shell' in row['Beguenstigter/Zahlungspflichtiger']:
        tags_collection += ' Tanken'
    if 'DB Vertrieb' in row['Beguenstigter/Zahlungspflichtiger']:
        tags_collection += ' DeutscheBahn'
    if 'REWE' in row['Beguenstigter/Zahlungspflichtiger']:
        tags_collection += ' REWE'
    if 'CEM OZD' in row['Beguenstigter/Zahlungspflichtiger']:
        tags_collection += ' BücherZeitungen'
    if 'KAUFHOF' in row['Beguenstigter/Zahlungspflichtiger']:
        tags_collection += ' Kaufhof'
    if 'ROLLER' in row['Beguenstigter/Zahlungspflichtiger']:
        tags_collection += ' Möbel'
    if 'JULIA' in row['Beguenstigter/Zahlungspflichtiger']:
        tags_collection += ' Sparbuch'
    if 'BE FIT' in row['Beguenstigter/Zahlungspflichtiger']:
        tags_collection += ' Fitnessstudio'
    if 'RBZV GmbH' in row['Beguenstigter/Zahlungspflichtiger']:
        tags_collection += ' BücherZeitungen'
    if 'ESSO' in row['Beguenstigter/Zahlungspflichtiger']:
        tags_collection += ' Tanken'
    if 'THALIA' in row['Beguenstigter/Zahlungspflichtiger']:
        tags_collection += ' BücherZeitungen'
    if 'DEUTSCHE BANK' in row['Beguenstigter/Zahlungspflichtiger']:
        tags_collection += ' Bargeldauszahlung'
    if 'REBSTOCK' in row['Beguenstigter/Zahlungspflichtiger']:
        tags_collection += ' Schwimmen'
    if 'APOTHEKE' in row['Beguenstigter/Zahlungspflichtiger']:
        tags_collection += ' Apotheke'
    if 'EXTRABLATT' in row['Beguenstigter/Zahlungspflichtiger']:
        tags_collection += ' Ausgehen'
    if 'Julia' in row['Beguenstigter/Zahlungspflichtiger'] and 'Tilgung' in row['Verwendungszweck']:
        tags_collection += ' TilgungBafög'
    if 'ALD Auto' in row['Beguenstigter/Zahlungspflichtiger']:
        tags_collection += ' LeasingMatthias'
    if 'KFW' in row['Beguenstigter/Zahlungspflichtiger']:
        tags_collection += ' TilgungKFW'
    if 'restaurant' in row['Beguenstigter/Zahlungspflichtiger'].lower():
        tags_collection += ' Ausgehen'
    if 'delft' in row['Verwendungszweck'].lower():
        tags_collection += ' ReiseDelft'
    if 'AMAZON' in row['Beguenstigter/Zahlungspflichtiger']:
        tags_collection += ' Amazon'
    if 'ALTRAN' in row['Beguenstigter/Zahlungspflichtiger']:
        tags_collection += ' GehaltMatthias'
    if 'REAL SPORT' in row['Beguenstigter/Zahlungspflichtiger']:
        tags_collection += ' Sport'
    if 'DM DROGERIEMARKT' in row['Beguenstigter/Zahlungspflichtiger']:
        tags_collection += ' DMMarkt'
    if 'Transdev' in row['Beguenstigter/Zahlungspflichtiger']:
        tags_collection += ' ÖPNV'
    if 'TOTAL' in row['Beguenstigter/Zahlungspflichtiger']:
        tags_collection += ' Tanken'
    if 'KENAN' in row['Verwendungszweck']:
        tags_collection += ' Taxi'
    if 'BUCHHANDLUNG' in row['Beguenstigter/Zahlungspflichtiger']:
        tags_collection += ' BücherZeitungen'
    if 'HORNBACH' in row['Beguenstigter/Zahlungspflichtiger']:
        tags_collection += ' Baumarkt'
    if 'EDEKA' in row['Beguenstigter/Zahlungspflichtiger']:
        tags_collection += ' Edeka'
    if 'KAISERS' in row['Beguenstigter/Zahlungspflichtiger']:
        tags_collection += ' KaisersMarkt'
    if 'Stadt Meerbusch' in row['Beguenstigter/Zahlungspflichtiger']:
        tags_collection += ' AbrechnungStadtMeerbusch'
    if 'HAIR ATTACK' in row['Beguenstigter/Zahlungspflichtiger']:
        tags_collection += ' Friseur'
    if 'DURSTY' in row['Beguenstigter/Zahlungspflichtiger']:
        tags_collection += ' Getränke'
    if 'REAL TEAM' in row['Beguenstigter/Zahlungspflichtiger']:
        tags_collection += ' RealMarkt'
    if 'Rundfunk' in row['Beguenstigter/Zahlungspflichtiger']:
        tags_collection += ' GEZ'
    if 'MAXX' in row['Beguenstigter/Zahlungspflichtiger']:
        tags_collection += ' TKMAXX'
    if 'idee' in row['Beguenstigter/Zahlungspflichtiger']:
        tags_collection += ' IdeeMarkt'
    if 'CAFE DEL SOL' in row['Beguenstigter/Zahlungspflichtiger']:
        tags_collection += ' Ausgehen'
    if 'BAUHAUS' in row['Beguenstigter/Zahlungspflichtiger']:
        tags_collection += ' Baumarkt'
    if 'ESPRIT ' in row['Beguenstigter/Zahlungspflichtiger']:
        tags_collection += ' Esprit'
    if '/GB/' in row['Verwendungszweck'] and (row['Buchungstag'] == '15.10.18' or row['Buchungstag'] == '12.10.18'or row['Buchungstag'] == '11.10.18'):
        tags_collection += ' LondonAIConf'
    if 'SuitSupply' in row['Verwendungszweck']:
        tags_collection += ' SuitSupply'
    if 'EGMOND' in row['Verwendungszweck']:
        tags_collection += ' ReiseEgmond'
    if 'KAMPS' in row['Verwendungszweck']:
        tags_collection += ' Bäcker'
    if '/GB/' in row['Verwendungszweck'] and (row['Buchungstag'] == '25.06.18' or row['Buchungstag'] == '26.06.18') and row['Buchungstext'] != 'BARGELDAUSZAHLUNG':
        tags_collection += ' ReiseLondon'
    if 'ROERMON' in row['Verwendungszweck']:
        tags_collection += ' ShoppingRoermond'
    if 'Taxi' in row['Verwendungszweck']:
        tags_collection += ' Taxi'
    if 'LASER' in row['Verwendungszweck']:
        tags_collection += ' Lasertag'
    if 'DEN HAAG' in row['Verwendungszweck'] and row['Buchungstext'] != 'BARGELDAUSZAHLUNG':
        tags_collection += ' ReiseDenHaag'
    if 'GRAVEHAGE' in row['Verwendungszweck']:
        tags_collection += ' ReiseDenHaag'
    if 'PRIMARK' in row['Verwendungszweck']:
        tags_collection += ' Primark'
    if 'Gulf Mertert' in row['Verwendungszweck']:
        tags_collection += ' Tanken'
    if 'SYLTER' in row['Verwendungszweck']:
        tags_collection += ' Ausgehen'
    if 'KOSMETIK' in row['Verwendungszweck']:
        tags_collection += ' Kosmetik'
    if 'VENLO' in row['Verwendungszweck']:
        tags_collection += ' Venlo'
    if 'augsburg' in row['Beguenstigter/Zahlungspflichtiger'].lower():
        tags_collection += ' AugsburgMarkt'
    if 'MEDIA MARKT' in row['Beguenstigter/Zahlungspflichtiger']:
        tags_collection += ' MediaMarkt'
    if 'ROSSMANN' in row['Beguenstigter/Zahlungspflichtiger']:
        tags_collection += ' RossmannMarkt'
    if 'ACTION' in row['Beguenstigter/Zahlungspflichtiger']:
        tags_collection += ' ActionMarkt'
    if 'KONTOUEBERTRAG HABEN' in row['Buchungstext']:
        tags_collection += ' ÜbertragKontoZusammenlegung'
    if 'OnlineTicket' in row['Verwendungszweck'] and 'SWK' in row['Verwendungszweck']:
        tags_collection += ' TicketSWK'
    if 'VHV' in row['Beguenstigter/Zahlungspflichtiger']:
        tags_collection += ' VersicherungAuto'
    if 'CONCEPT STORE KR' in row['Beguenstigter/Zahlungspflichtiger']:
        tags_collection += ' SchuheMatthias'
    if 'Allianz' in row['Beguenstigter/Zahlungspflichtiger']:
        tags_collection += ' VersicherungAllianz'
    if 'BOCKUMER BUCHHDL' in row['Beguenstigter/Zahlungspflichtiger']:
        tags_collection += ' BücherZeitungen'
    if 'BUNDESKASSE IN HALLE/SAALE' in row['Beguenstigter/Zahlungspflichtiger'] or 'BUNDESKASSE IN HALLE' in row['Beguenstigter/Zahlungspflichtiger'] or 'Bundeskasse in Halle' in row['Beguenstigter/Zahlungspflichtiger']:
        tags_collection += ' BafögMatthias'
    if 'Universitätslinikum ' in row['Beguenstigter/Zahlungspflichtiger']:
        tags_collection += ' KostenKryoBonn'
    if 'Sondertilgung' in row['Verwendungszweck']:
        tags_collection += ' SonderTilgungBafögLilly'
    if 'APOTH. AM MARKT	' in row['Beguenstigter/Zahlungspflichtiger']:
        tags_collection += ' MedikamenteKinderwunsch'
    if 'THOMAS UND TIM WEYERS' in row['Beguenstigter/Zahlungspflichtiger']:
        tags_collection += ' FahrradLilly'
    if 'KRAEHENNEST' in row['Verwendungszweck']:
        tags_collection += ' WellnessKraehennest'
    if 'Fuer die Huette' in row['Verwendungszweck']:
        tags_collection += ' PachtHütte'
    if 'ASTOR HYDE PARK' in row['Verwendungszweck']:
        tags_collection += ' HotelLondon'
    if 'HOTEL HAUS HILCKMANN' in row['Beguenstigter/Zahlungspflichtiger']:
        tags_collection += ' HotelHochzeitMaike'
    if 'Kfz-Steuer' in row['Verwendungszweck']:
        tags_collection += ' KfzSteuerLilly'
    if 'STADTW. KREFELD' in row['Verwendungszweck']:
        tags_collection += ' RestaurantStadtwald'
    if 'P+C SAGT DANKE' in row['Beguenstigter/Zahlungspflichtiger']:
        tags_collection += ' KlamottenLilly'
    if 'CTS Eventim' in row['Beguenstigter/Zahlungspflichtiger']:
        tags_collection += ' ÜberraschungLilly'
    if 'Sandra Rademacher' in row['Beguenstigter/Zahlungspflichtiger']:
        tags_collection += ' GeschenkBrauns'
    if 'Zalando' in row['Beguenstigter/Zahlungspflichtiger']:
        tags_collection += ' Klamotten'
    if 'NORDBAHNHOF' in row['Beguenstigter/Zahlungspflichtiger']:
        tags_collection += ' RestaurantNordbahnhof'
    if 'SPORT VOSWINKEL' in row['Beguenstigter/Zahlungspflichtiger']:
        tags_collection += ' KlamottenLilly'
    if 'Fuer die Note' in row['Verwendungszweck']:
        tags_collection += ' GeschenkMaikeHochzeit'
    if 'TAMARIS STORE' in row['Beguenstigter/Zahlungspflichtiger']:
        tags_collection += ' KlamottenLilly'
    if 'GAA Reisebank' in row['Beguenstigter/Zahlungspflichtiger']:
        tags_collection += ' Bargeldauszahlung'
    if 'METRO C+C' in row['Beguenstigter/Zahlungspflichtiger']:
        tags_collection += ' Metro'
    if 'GIROSOLUTION FUER PAYPAL' in row['Beguenstigter/Zahlungspflichtiger']:
        tags_collection += ' PayPal'
    if 'TK-Unimed - Uniklinik Düsseldorf' in row['Beguenstigter/Zahlungspflichtiger']:
        tags_collection += ' Kryokonservierung'
    if '02.12.2018,20.01 UHR' in row['Verwendungszweck']:
        tags_collection += ' AnzahlungMalleRadtour'
    if 'SVWZ+2018-11-30T16.54' in row['Verwendungszweck']:
        tags_collection += ' HotelStuttgart'
    if 'KKH' in row['Beguenstigter/Zahlungspflichtiger']:
        tags_collection += ' VersicherungKKH'
    if 'KUNSTVERLAG MARIA LAACH' in row['Beguenstigter/Zahlungspflichtiger']:
        tags_collection += ' EinkaufMariaLaach'
    if 'Infoscore Forderungsmanagement GmbH' in row['Beguenstigter/Zahlungspflichtiger']:
        tags_collection += ' InkassoKosten'
    if 'GREEN CHILI' in row['Beguenstigter/Zahlungspflichtiger']:
        tags_collection += ' GreenChiliResto'
    if 'SANITAETSHAUS LETTERMANN' in row['Beguenstigter/Zahlungspflichtiger']:
        tags_collection += ' Sanitätshaus'
    if 'Tankstelle ' in row['Beguenstigter/Zahlungspflichtiger']:
        tags_collection += ' Tanken'
    if 'EURABWA+HEATHROW RAIL LINK' in row['Verwendungszweck']:
        tags_collection += ' ÖpnvLondonBells'
    if 'RAMERSHOVEN GMBH MAYEN' in row['Beguenstigter/Zahlungspflichtiger']:
        tags_collection += ' EinkaufenRamershovenMayen'
    if 'Planet Sports GmbH' in row['Beguenstigter/Zahlungspflichtiger']:
        tags_collection += ' EinkaufenPlanetSports'
    if 'BUHL-DATA-SERVICE GMBH' in row['Beguenstigter/Zahlungspflichtiger']:
        tags_collection += ' EinkaufSteuerSoftware'
    if 'HEATHROW' in row['Verwendungszweck']:
        tags_collection += ' ÖpnvAiConf'
    if 'HEINER KEMPKEN' in row['Beguenstigter/Zahlungspflichtiger']:
        tags_collection += ' EinkaufenEdeka'
    if 'DISNEY STORE' in row['Verwendungszweck']:
        tags_collection += ' EinkaufenDisneyStore'
    if 'FOTOSERVICE' in row['Beguenstigter/Zahlungspflichtiger']:
        tags_collection += ' FotoService'
    if 'NANU-NANA' in row['Beguenstigter/Zahlungspflichtiger']:
        tags_collection += ' EinkaufenNanuNana'

    return tags_collection