from datetime import date
import time
import pandas as pd
import numpy as np
from salvarExcel import salvarecxel


def formatartabela():
    hoje = str(date.today())
    df = pd.read_csv('MonitoramentoClientesCred'+hoje+'.csv', decimal=',')

    df['Ultima proposta'] = pd.to_datetime(df['Ultima proposta'], dayfirst=True, format="%Y/%m/%d %H:%M:%S")

    matriz = []
    matriz.append(df['Ultima proposta'])

    dhoje = (time.strftime('%Y/%m/%d %H:%M:%S', time.localtime()))
    dhoje = pd.to_datetime(dhoje, dayfirst=True, format="%Y/%m/%d %H:%M:%S")

    nv_matriz = []

    for m in matriz:
        data = dhoje - m
        nv_matriz.append(data)

    for n in nv_matriz:
        df['Tempo S/ Proposta'] = np.r_[n]

    df['Tempo S/ Proposta'] = df["Tempo S/ Proposta"].astype(str)

    salvarecxel(df)
