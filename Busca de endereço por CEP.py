###################################################################################
# Projeto:  Busca Endereço 
# Objetivo: Encontra endereço através de um cep informado 
###################################################################################

import requests
import tkinter as tk

def buscar_cep():
    cep = entrada_cep.get()
    url = f'https://viacep.com.br/ws/{cep}/json/'
    resposta = requests.get(url)
    if resposta.status_code == 200:
        dados = resposta.json()
        lbl_cep['text'] = f'CEP: {dados["cep"]}'
        lbl_logradouro['text'] = f'Logradouro: {dados["logradouro"]}'
        lbl_bairro['text'] = f'Bairro: {dados["bairro"]}'
        lbl_cidade['text'] = f'Cidade: {dados["localidade"]} - {dados["uf"]}'
    else:
        lbl_cep['text'] = 'CEP não encontrado'
        lbl_logradouro['text'] = ''
        lbl_bairro['text'] = ''
        lbl_cidade['text'] = ''

janela = tk.Tk()
janela.geometry('400x200')
janela.title('Busca de Endereço')

lbl_instrucao = tk.Label(janela, text='Digite o CEP:')
lbl_instrucao.pack(padx=5, pady=5)

entrada_cep = tk.Entry(janela)
entrada_cep.pack()

btn_buscar = tk.Button(janela, text='Buscar', command=buscar_cep)
btn_buscar.pack(padx=10, pady=10)

lbl_cep = tk.Label(janela)
lbl_cep.pack()

lbl_logradouro = tk.Label(janela)
lbl_logradouro.pack()

lbl_bairro = tk.Label(janela)
lbl_bairro.pack()

lbl_cidade = tk.Label(janela)
lbl_cidade.pack()

janela.mainloop()
