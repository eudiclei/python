###################################################################################
# Projeto:  Gerador de QR Code 
# Objetivo: Gerar códigos qrcode atraves de uma texto pré-definido
###################################################################################

import qrcode

meu_qrcode = qrcode.make('https://cartilha.cert.br/livro/cartilha-seguranca-internet.pdf')

meu_qrcode.save('qrcode.png')
meu_qrcode.show()