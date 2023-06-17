###################################################################################
# Projeto:  Gerador de QR Code 
# Objetivo: Gerar códigos qrcode atraves de uma texto pré-definido
###################################################################################

import qrcode

meu_qrcode = qrcode.make('https://github.com/eudiclei')

meu_qrcode.save('qrcode.png')
meu_qrcode.show()