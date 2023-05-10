###################################################################################
# Projeto:  Desliga PC 
# Objetivo: Desliga pc com um tempo de espera de 10 segundos
###################################################################################

import os 
  
shutdown = input("Do you wish to shutdown your computer ? (yes / no): ") 
  
if shutdown == 'no': 
    exit() 
else: 
    os.system("shutdown /s /t 10") 