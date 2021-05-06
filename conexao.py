import pyodbc
from banco import dados_de_conexao
from script import select
def extracao():
    cnxn = pyodbc.connect(f"DRIVER={dados_de_conexao()['driver']};SERVER={dados_de_conexao()['server']};DATABASE={dados_de_conexao()['database']};UID={dados_de_conexao()['username']};PWD={dados_de_conexao()['password']}")
    cursor = cnxn.cursor()
    cursor.execute(select())
    row = cursor.fetchone()
    extracao = []
   # extracao.append(cursor.fetchall())
    while row:
        extracao.append(row)
        row = cursor.fetchone()
    return extracao