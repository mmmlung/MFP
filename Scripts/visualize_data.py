import pandas as pd
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import plotly.graph_objs as go
import plotly.io as pio
import time

def visualize_categories_einnahmen(df):

    Einnahmen = df[df['Betrag']>0].copy()
    labels_Einnahmen = list(set(Einnahmen.Category))
    values_Einnahmen = [sum(Einnahmen[Einnahmen['Category']==labels_Einnahmen[i]].Betrag) for i in range(len(labels_Einnahmen))]

    fig1 = go.Figure()
    fig1.add_pie(labels=labels_Einnahmen, values=values_Einnahmen, textposition='auto')

    pio.write_image(fig1,'C:/Users/adm-mlung/Desktop/Projekte/Secrets/plots/Einnahmen/Pie/Einnahmen_'+str(time.strftime("%d%m%Y"))+'.svg',scale=2.5)

    fig2=go.Figure()
    fig2.add_bar(x=labels_Einnahmen,y=values_Einnahmen,text=values_Einnahmen,textposition = 'auto',marker=dict(color='rgb(158,202,225)',line=dict(color='rgb(8,48,107)',width=1.5)),opacity=0.6)
    pio.write_image(fig2,'C:/Users/adm-mlung/Desktop/Projekte/Secrets/plots/Einnahmen/Bar/Einnahmen_'+str(time.strftime("%d%m%Y"))+'.svg',scale=2.5)

def visualize_categories_ausgaben(df):

    Ausgaben = df[df['Betrag']<0].copy()
    labels_Ausgaben = list(set(Ausgaben.Category))
    values_Ausgaben = [round(-1*sum(Ausgaben[Ausgaben['Category']==labels_Ausgaben[i]].Betrag)) for i in range(len(labels_Ausgaben))]

    fig1 = go.Figure()
    fig1.add_pie(labels=labels_Ausgaben, values=values_Ausgaben, textposition='auto')

    pio.write_image(fig1,'C:/Users/adm-mlung/Desktop/Projekte/Secrets/plots/Ausgaben/Pie/Ausgaben_'+str(time.strftime("%d%m%Y"))+'.svg',scale=2.5)

    fig2=go.Figure()
    fig2.add_bar(x=labels_Ausgaben,y=values_Ausgaben,text=values_Ausgaben,textposition = 'auto',marker=dict(color='rgb(158,202,225)',line=dict(color='rgb(8,48,107)',width=1.5)),opacity=0.6)
    pio.write_image(fig2,'C:/Users/adm-mlung/Desktop/Projekte/Secrets/plots/Ausgaben/Bar/Ausgaben_'+str(time.strftime("%d%m%Y"))+'.svg',scale=2.5)

def visualize_einnahmen_weekly(df):
    Einnahmen = df[df['Betrag']>0]
    ds = Einnahmen[['Valutadatum','Betrag']].copy()
    ds['Valutadatum'] = pd.to_datetime(ds['Valutadatum'])
    ds.index= ds['Valutadatum']
    dy = ds.resample('W').sum()
    dy = dy.reset_index()

    values = [round(betrag) for betrag in dy['Betrag']]

    fig = go.Figure()
    fig.add_bar(x=dy.Valutadatum,y=values,text=values,textposition = 'auto',marker=dict(color='rgb(158,202,225)',line=dict(color='rgb(8,48,107)',width=1.5)),opacity=0.6)
    pio.write_image(fig,'C:/Users/adm-mlung/Desktop/Projekte/Secrets/plots/Einnahmen/Bar weekly/Bar weekly'+str(time.strftime("%d%m%Y"))+'.svg',scale=2.75)


def visualize_ausgaben_weekly(df):
    Ausgaben = df[df['Betrag']<0]
    ds = Ausgaben[['Valutadatum','Betrag']].copy()
    ds['Valutadatum'] = pd.to_datetime(ds['Valutadatum'])
    ds.index= ds['Valutadatum']
    dy = ds.resample('W').sum()
    dy = dy.reset_index()

    values = [-1*round(betrag) for betrag in dy['Betrag']]

    fig = go.Figure()
    fig.add_bar(x=dy.Valutadatum,y=values,text=values,textposition = 'auto',marker=dict(color='rgb(158,202,225)',line=dict(color='rgb(8,48,107)',width=1.5)),opacity=0.6)
    pio.write_image(fig,'C:/Users/adm-mlung/Desktop/Projekte/Secrets/plots/Ausgaben/Bar weekly/Bar weekly'+str(time.strftime("%d%m%Y"))+'.svg',scale=2.75)
