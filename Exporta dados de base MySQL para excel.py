########################################################################
# Projeto:  Exporta dados MySQL para uma arquivo xls (Excel) 
# Objetivo: Exporta dados de uma base de dados MySQL e exporta para 
# um arquivo.xls
########################################################################

from pymysql import *
import xlwt
import pandas.io.sql as sql
# Conectando a base mysql com o python
con = connect(user="USUARIO",password="PASSWORD",host="SEUSITE",database="NOME_BANCO_DE_DADOS")
# ler os dados
df = sql.read_sql('select * from NOME_TABELA',con)
# Imprimi os dados lidos
print(df)
# Exporta os dados para um arquivo.xls
df.to_excel('arquivoGerado.xls')