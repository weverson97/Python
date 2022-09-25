"""
Autor: Weverson Jose da Silva

2 - Observando o mercado de educação infantil, você e sua equipe decidem criar um
aplicativo por meio do qual as crianças aprendam a controlar os seus gastos.
Como forma de validar um protótipo, foi solicitado que você crie um script simples,
em que o usuário deve informar QUANTAS TRANSAÇÕES financeiras realizou ao longo de um
dia e, na sequência, deve informar o VALOR DE CADA UMA das transições que realizou.
Seu programa deverá exibir, ao final, o valor total gasto pelo usuário, bem como a
média do valor de cada transação.

"""
qtd_transações = int(input("Informe a quantidade de transações realizadas no dia: "))
total_transações = 0

for i in range(1, qtd_transações+1):
    transações = float(input(f"Informe o valor da transição {i}°: "))
    total_transações = total_transações + transações

print(f"Total dos gastos: R${total_transações} ")
print(f"Media dos gastos: R${total_transações/transações} ")




