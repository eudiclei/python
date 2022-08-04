###################################################################################
# Projeto:  Voz fala texto escrito 
# Objetivo: Com esta biblioteca é posssível falar texto escrito dentro do código.
# Ideal para chamada de senha em gerenciadores de filas
###################################################################################

import pyttsx3

def voiceChange():
    eng = pyttsx3.init()
    voice = eng.getProperty('voices')
    eng.setProperty('voice', voice[0].id)
    eng.say("Olá! seja bem-vindo!")
    eng.runAndWait()
if __name__ == "__main__":
    voiceChange()