from datetime import date
import pandas as pd
from enviar_email import enviaremail


def salvarecxel(df):
    salvarexcel = df
    excel = pd.ExcelWriter(f'MonitoramentoClientesCred{date.today()}.xlsx')
    salvarexcel.to_excel(excel, sheet_name="UltimasPropostas")
    excel.save()
    enviaremail()
