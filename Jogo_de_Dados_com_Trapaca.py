###################################################################################
# Projeto:  Jogo de Dados com Trapaça 
# Objetivo: Estudos e Informativo
# Demonstrar que os jogos digitais podem ser suscetíveis a trapaças 
###################################################################################

# SIMULADOR DE JOGADA DE DADOS (COM TRAPAÇA)

# Este código foi desenvolvido com o propósito de estudo, visando demonstrar que os jogos digitais podem ser suscetíveis a trapaças.
# Neste algoritmo, o jogador só começará a ganhar quando alcançar o valor total_creditado_pretendido.
# O jogador realiza um depósito inicial, sendo que cada lançamento do dado tem um custo de R$ 10. 
# Enquanto o montante depositado não atingir ou ultrapassar R$ 200, que é o valor de ganho almejado,
# o jogador não receberá nenhum prêmio, a menos que o criador do código permita explicitamente.

# O valor digitado (valor do crédito) deve ser sem virgulas (,)  ou pontos (.) .
# Para jogar o dado deve ser digitado um número de 1 (um) a 6 (seis) .

import random

seu_saldo = 0
conta_aposta = 0
credito = 0
total_creditado = 0
total_creditado_pretendido = 200 # valor mínimo para liberar premiação

def simular_lancamento_dado(numero_usuario):
    global seu_saldo,  total_creditado, total_creditado_pretendido, conta_aposta
    # verifica se o apostador tem saldo
    while (seu_saldo >= 10): 
        # Enquanto o valor creditado pelo apostador for inferior ao total_creditado_pretendido
        while total_creditado < total_creditado_pretendido:  
            
            # A trapaça está aqui !!!      
            resultado_dado = random.randint(1, 6)        
            while ((resultado_dado == numero_usuario)):
                resultado_dado = random.randint(1, 6)               
            else:
                seu_saldo = seu_saldo - 10
                conta_aposta = conta_aposta + 1
                print(f"Aposta: {conta_aposta}")
                print(f"Seu saldo é: {seu_saldo}")
                print(f"Apostou no: {numero_usuario} e o Dado deu: {resultado_dado} \n")
                if seu_saldo < 10: # quando o saldo inferior a R$ 10 encaminha para recarregar_saldo
                    print(f"Seu Saldo acabou !!!")
                    recarregar_saldo()    
                                    
            numero_usuario = int(input("Digite novamente de 1 a 6: "))
            simular_lancamento_dado(numero_usuario)                 
            
        else:                          
                      
            # se sim, jogar dado com regra normal 
            resultado_dado = random.randint(1, 6) 
            while ((resultado_dado != numero_usuario)):
                seu_saldo = seu_saldo - 10
                conta_aposta = conta_aposta + 1
                print(f"Aposta: {conta_aposta}")
                print(f"Seu saldo é: {seu_saldo}")
                print(f"Apostou no: {numero_usuario} e o Dado deu: {resultado_dado} \n")
                if seu_saldo < 10:
                    print(f"Seu Saldo acabou !!!")
                    recarregar_saldo()
                numero_usuario = int(input("Digite novamente de 1 a 6: "))               
                resultado_dado = random.randint(1, 6)                               
            else:
                print("\n!!! PARABÉNS !!!\n!!! VOCÊ ACERTOU !!!")
                print(f"Apostou no: {numero_usuario} e o Dado deu: {resultado_dado} \n")
                return      
               
# Recarrega saldo
def recarregar_saldo():
    global seu_saldo, credito, total_creditado
    if seu_saldo < 10:
        print("Seu saldo é insuficiente para fazer uma aposta.")
        credito = int(input("Faça um deposito mínimo de R$ 10: "))
        seu_saldo = seu_saldo + credito
        total_creditado = total_creditado + credito
        print(f"\nSeu saldo é: {seu_saldo}")
        print(f"Total creditado é: {total_creditado}")
        if seu_saldo < 10:
            recarregar_saldo()
        else:
            numero_usuario = int(input("Digite um número de 1 a 6: "))
            simular_lancamento_dado(numero_usuario)

# Se Saldo for inferior a R$ 10, encaminha para Recarregar Saldo
if seu_saldo < 10:
    recarregar_saldo()     