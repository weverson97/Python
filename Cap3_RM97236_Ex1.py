"""
Autor: Weverson Jose da Silva

1 – Você foi procurado por um aluno do curso de Produção Multimídia do FIAP ON
para desenvolver um trabalho em parceria: um serviço em que as pessoas possam usar
um estúdio profissional para gravar seus vídeos para o YouTube com máxima qualidade.
O serviço ganha dinheiro por meio de um sistema de assinaturas e de um bônus
calculado por uma porcentagem sobre o faturamento que o canal do cliente
obteve ao longo do ano.

Sua tarefa é criar um algoritmo que receba o tipo de assinatura do cliente,
o faturamento anual dele e que calcule e exiba qual o valor do bônus que
o cliente deve pagar a vocês. A tabela abaixo mostra a porcentagem de acordo
com cada nível de assinatura:

Nível               Porcentagem sobre o faturamento

Basic               30%

Silver              20%

Gold                10%

Platinum            5%
"""
faturamento = float(input(" Informe o faturamento anual: "))
tipo_assinatura = int(input(" Informe o tipo de assinatura: 1 - Basic / 2  - Silver / 3 - Gold / 4 - Platinum: "))
bonus = 0

if tipo_assinatura < 0 or tipo_assinatura > 5:
    print(f" Opção inválida")

else:
    if tipo_assinatura == 1:
        bonus = faturamento * 0.30

    elif tipo_assinatura == 2:
        bonus = faturamento * 0.20

    elif tipo_assinatura == 3:
        bonus = faturamento * 0.10

    else:
        bonus = faturamento * 0.05
    print(f" Terá que pagar R${bonus} do valor de R${faturamento}")











