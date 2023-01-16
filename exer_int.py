"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

numero = input('Digite um número inteiro. ')

if numero.isdigit():
    if (int(numero) % 2) == 0:
        print('Seu numero é par')
    else:
        print('Seu numero é impar')
else:
    print('Voce não digitou um numero válido')             