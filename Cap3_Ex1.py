"""
Autor: Weverson Jose da Silva

1 - Você deve elaborar um algoritmo implementado em phyton em que o usuário informe
quantos alimentos consumiu naquele dia e depois possa informar o número de calorias de
cada um dos alimentos. Como não estudamos listas neste capítulo, você não deve se
preocupar em armazenar todas as calorias digitadas, mas deve exibir o total de
calorias no final.
"""

qtd_alimentos = int(input("Informe a quantidade de alimentos consumidas no dia: "))
total_calorias = 0

for i in range(1, qtd_alimentos+1):
    calorias_alimentos = float(input(f"Informe a quantidade de calorias do {i}° alimento:"))
    total_calorias = total_calorias + calorias_alimentos

print(f"O valor total das colorias foram {total_calorias } ")