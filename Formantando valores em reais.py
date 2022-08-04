##############################################################################
# Projeto:  Formatando valores em Reais 
# Objetivo: Formatar valores monetário americano em Reais
##############################################################################

# Faremos aqui um pequeno calculo da venda de um determinado produto
custo = 500
faturamento = 1500
lucro = faturamento - custo
# Valor americano com 2 casas decimais
print(f'O lucro foi de R${lucro:,.2f}')

# Aqui é mostrado a porcentagem do lucro obtido
margem = lucro / faturamento
print(f'A margem foi de {margem:.1%}')

# Agora formantando o valor em Reais
texto_lucro = f"R${lucro:_.2f}"
texto_lucro = texto_lucro.replace(".", ",").replace("_", ".")
print(f'O lucro em Reais foi de {texto_lucro}')