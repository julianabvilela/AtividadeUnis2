# -*- coding: latin1 -*-

n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))
n3 = int(input("Digite o terceiro numero: "))

if(n1>n2) and (n1>n3):
    print(f'O numero: {n1} � maior')
elif (n2>n1) and (n2>n3):
    print(f'O numero: {n2} � maior')
elif (n3>n1) and (n3>n2):
    print(f'O numero: {n3} � maior')
else:
    print('Os numeros digitados sao iguais!')
