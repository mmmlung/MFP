import pandas as pd 
import datetime
from matplotlib import pyplot as plt


Start = pd.Timestamp(2019,1,1).normalize()
End = Start + datetime.timedelta(weeks= 32)

def init_anfangssaldo(df, Anfangssaldo=0):

    anfangssaldo = pd.DataFrame(
        data= {'Anfangssaldo': Anfangssaldo},
        index=pd.date_range(start=Start, end= Start)
    )
    df = pd.concat([df,anfangssaldo],axis=1).fillna(0)
    return df


def init_fixe_einkommen(df):

    März = pd.Timestamp(2019,3,1).normalize()
    
    gehalt_lilly_bis_März = pd.DataFrame(
        data={'Gehalt_Lilly_bis':  2126},
        index= pd.date_range(start=Start, end=März, freq='BM')
    )
    gehalt_lilly_ab_März = pd.DataFrame(
        data={'Gehalt_Lilly_ab':  2297 },
        index= pd.date_range(start=März, end=End, freq='BM')
    )

    gehalt_keksi = pd.DataFrame(
        data={'Gehalt_Keksi': 2742 },
        index = pd.date_range(start=Start, end=End, freq='BM')                        
    )

    df = pd.concat([df, gehalt_keksi, gehalt_lilly_ab_März, gehalt_lilly_bis_März], axis= 1).fillna(0)
    df['Gehalt_Keksi'] = pd.to_numeric(df['Gehalt_Keksi'])
    df['Gehalt_Lilly_bis'] = pd.to_numeric(df['Gehalt_Lilly_bis'])
    df['Gehalt_Lilly_ab'] = pd.to_numeric(df['Gehalt_Lilly_ab'])

    RückerstattungUniKid_Datum = März

    RückerstattungUniKid = pd.DataFrame(
        data={'RückerstattungUniKid': 1570 },
        index = pd.date_range(start=RückerstattungUniKid_Datum, end=RückerstattungUniKid_Datum)                        
    )
    df = pd.concat([df, RückerstattungUniKid], axis= 1).fillna(0)

    SteuerRück = pd.DataFrame(
        data={'SteuerRück': 2000 },
        index = pd.date_range(start=März, end=März)                        
    )
    df = pd.concat([df, SteuerRück], axis= 1).fillna(0)

    return df

def init_fixe_ausgaben(df):
    Miete = pd.DataFrame(
        data= {'Miete':-770},
        index=pd.date_range(start=Start, end=End, freq='MS')
    )
    df = pd.concat([df, Miete], axis= 1).fillna(0)

    BafögM = pd.DataFrame(
        data= {'BafögM':-315},
        index=pd.date_range(start=Start, end=End, freq='Q')
    )
    df = pd.concat([df, BafögM], axis= 1).fillna(0)

    Sparen = pd.DataFrame(
        data= {'Sparen':-1000},
        index=pd.date_range(start=Start, end=End, freq='MS')
    )
    df = pd.concat([df, Sparen], axis= 1).fillna(0)

    AutoKreditLilly = pd.DataFrame(
        data= {'AutoKreditLilly':-218.00},
        index=pd.date_range(start=Start, end=End, freq='MS')
    )
    df = pd.concat([df, AutoKreditLilly], axis= 1).fillna(0)

    Hütte = pd.DataFrame(
        data= {'Hütte':-1500.00},
        index=pd.date_range(start=Start, end=Start)
    )
    df = pd.concat([df, Hütte], axis= 1).fillna(0)

    RadV = pd.DataFrame(
        data= {'RadV':-27.00},
        index=pd.date_range(start=Start, end=End, freq='MS')
    )
    df = pd.concat([df, RadV], axis= 1).fillna(0)

    Altervors = pd.DataFrame(
        data= {'Altersvors':-150.00},
        index=pd.date_range(start=Start, end=End, freq='MS')
    )
    df = pd.concat([df, Altervors], axis= 1).fillna(0)

    InspektionAuto = pd.DataFrame(
        data= {'InspektionAuto':-200.00},
        index=pd.date_range(start=Start, end=Start)
    )
    df = pd.concat([df, InspektionAuto], axis= 1).fillna(0)

    HausratV = pd.DataFrame(
        data= {'HausratV':-220.00},
        index=pd.date_range(start=Start, end=Start)
    )
    df = pd.concat([df, HausratV], axis= 1).fillna(0)

    HausNebenk = pd.DataFrame(
        data= {'HausNebenk':-400.00},
        index=pd.date_range(start=Start, end=Start)
    )
    df = pd.concat([df, HausNebenk], axis= 1).fillna(0)

    LillyBafög = pd.DataFrame(
        data= {'LillyBafög':-115.00},
        index=pd.date_range(start=Start, end=End, freq='MS')
    )
    df = pd.concat([df, LillyBafög], axis= 1).fillna(0)

    BeFit = pd.DataFrame(
        data= {'BeFit':-30.00},
        index=pd.date_range(start=Start, end=End, freq='MS')
    )
    df = pd.concat([df, BeFit], axis= 1).fillna(0)   

    StromSWK = pd.DataFrame(
        data= {'StromSWK':-53.00},
        index=pd.date_range(start=Start, end=End, freq='MS')
    )
    df = pd.concat([df, StromSWK], axis= 1).fillna(0)   

    HandyInternet = pd.DataFrame(
        data= {'HandyInternet':-65.00},
        index=pd.date_range(start=Start, end=End, freq='MS')
    )
    df = pd.concat([df, HandyInternet], axis= 1).fillna(0)

    AutoKreditMatthias = pd.DataFrame(
        data= {'AutoKreditMatthias':-51},
        index=pd.date_range(start=Start, end=End, freq='MS')
    )
    df = pd.concat([df, AutoKreditMatthias], axis= 1).fillna(0)

    return df

def init_salden(df):

    df['Tagessaldo'] = df.sum(axis=1)
    df['Tagesaldo_kumuliert'] = df['Tagessaldo'].cumsum()
    return df

def write_budget(df):

    df.to_csv("C:/Users/adm-mlung/Desktop/Projekte/MFP/data/Budget.csv")
    print('Write to file successfull')

def visualize_budget(df):
    
    plt.figure(figsize=(10, 5))
    plt.plot(df.index, df.Tagessaldo, label='Tagessaldo')
    plt.plot(df.index, df.Tagesaldo_kumuliert, label='Tagesaldo_kumuliert')
    plt.legend()
    plt.savefig('C:/Users/adm-mlung/Desktop/Projekte/MFP/data/Budget')