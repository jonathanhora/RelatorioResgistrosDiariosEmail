from conexao import extracao
import csv
from datetime import date
from main import formatartabela
import time

f = open(f'MonitoramentoClientesCred{date.today()}.csv', 'w', newline='', encoding='utf-8')
w = csv.writer(f)


valores = []
w.writerow(["Instituicao", "Ultima proposta"])
for n in extracao():
    valores.append(list(n))
time.sleep(10)

for m in valores:
    w.writerow(m)

f.close()
time.sleep(10)

formatartabela()



