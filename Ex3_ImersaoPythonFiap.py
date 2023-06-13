"""
3. Faça um programa que peça 2 números e mostre o resultado das 4 operacoes entre os dois aprendendo
numeros: soma, subtração, divisão e multiplicação.

"""
first_number = float(input(" Inform the first number: "))
second_number = float(input(" Inform the second number: "))


soma = first_number + second_number
subtracao = first_number - second_number
divisao = first_number / second_number
multiplicao = first_number * second_number

print(f"{first_number} + {second_number} = {soma} ")
print(f"{first_number} - {second_number} = {subtracao} ")
print(f"{first_number} / {second_number} = {divisao} ")
print(f"{first_number} * {second_number} = {divisao} ")