"""
6. Faça um programa que peça o nome da pessoa e a idade e diga se a pessoa já pode votar, se a
pessoa já pode obter a carta de motorista.

"""

name = input("What's your name? ")
age = int(input("How old are you? "))

if age >=16:
    print(f" The {name} can vote")

if age >=18:
    print(f" The {name} can have drive's license")    