import sys
sys.path.insert(0, r'C:/Users/adm-mlung/Desktop/Projekte/MFP/Scripts')
import load_data
import clean_data

df = load_data.collect_data_spkr('full', True)
print("Success load")
dc = clean_data.clean_data(df)
print("Succes clean")
dd = clean_data.tag_data(dc)
print('Succsess tagging')
de = clean_data.categorize_data(dd)
print('Succes categorizing')

de.to_csv("C:/Users/adm-mlung/Desktop/Projekte/MFP/data/Umsatz_clean.csv")
