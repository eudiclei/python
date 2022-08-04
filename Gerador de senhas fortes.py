###################################################################################
# Projeto:  Gerando senhas fortes 
# Objetivo: Gerar senhas aleatórias com maiúsculas, minúsculas, números 
# e/ou caracteres especiais
###################################################################################

import string
from random import random, choice

valores = ''

# Descomente as linhas a seguir de acordo com o tipo de senha desejada 
# Incluir todas as letras minúsculas e maiúsculas do alfabeto na geração da senha
#valores += string.ascii_letters

# Incluir letras minúsculas
valores += string.ascii_lowercase

# Incluir letras MAIÚSCULAS
#valores += string.ascii_uppercase

# Incluir números de 0 a 9
valores += string.digits 

# Inclui caracteres especiais
#valores += string.punctuation

tamanho = 10
senha =''

for i in range(tamanho):
    senha += choice(valores)

print(senha)
