# -*- coding: latin1 -*-

dias = int(input("Digite sua idade em dias: "))
anos = dias / 365
dias %= 365
meses = dias / 30
dias %= 30

print(f"Anos: {anos}")
print(f"Meses: {meses}")
print(f"Dias: {dias}")
