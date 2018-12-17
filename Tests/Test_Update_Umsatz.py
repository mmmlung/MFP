import sys
sys.path.insert(0, r'C:/Users/adm-mlung/Desktop/Projekte/MFP/Scripts')
import load_data
import clean_data
import update_data
import time

df = update_data.append_data()

df = update_data.tag_updated_data_rules(df)

df = update_data.categorize_updated_data_rules(df)

df = update_data.tag_updated_data_ui(df)

#df = update_data.categorize_updated_data_ui(df)

df.to_csv("C:/Users/adm-mlung/Desktop/Projekte/Secrets/data/Rules_Updated_Umsatz_"+ str(time.strftime("%d%m%Y")) +".csv")