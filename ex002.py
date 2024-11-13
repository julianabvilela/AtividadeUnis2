# -*- coding: latin1 -*-

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

if (a>b+c) and (b>a+c) and (c>a+b):
    print("Não formam um triângulo")
elif (a==b) and (b==c):
    area = ((a ^ 2) * (3 ^ (1/2))) / 4
    print(f"formam um triângulo Equilatero e sua area e igual a: {area}")
elif (a==b) or (a==c) or (b==c):
    area = (a*(a^2-(a/2)^2)^(1/2))/2
    print(f"formam um triângulo Isosceles e sua area e igual a: {area}")
elif (a!=b) and (a!=c) and (b!=c):
    p = a+b+c/2
    area = (p ^ 2 (p-a)(p-b)(p-c))
    print("formam um triângulo Escaleno")