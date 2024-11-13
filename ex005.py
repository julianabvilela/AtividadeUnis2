# -*- coding: latin1 -*-

frase = input('Digite uma frase: ')
print('A frase digitada foi: {}' .format(frase))
invertida = ' '.join(palavra[::-1] for palavra in frase.split())
print('A frase de modo inevertida fica: {}'.format(invertida))
