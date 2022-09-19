"""
Autor: Weverson Jose da Silva

2 - Viajar é bom demais! Uma agência de viagens está propondo uma estratégia para alavancar as vendas
após os impactos da pandemia do coronavírus
    A empresa ofertará descontos progressivos na compra de pacotes, dependendo do número de viajantes
que estão no mesmo grupo e moram na mesma residência
    Para ajudar a tornar esse projeto real, voce deve criar um algoritmo que receba o VALOR BRUTO
do pacote, a CATEGORIA DOS ASSENTOS no voo e a QUANTIDADE DE VIAJANTES que moram em uma mesma
casa e calcule os descontos de acordo com a tabela abaixo:

Econômica
2 viajantes 3%
3 viajantes 4%
4 viajantes ou mais 5%

Executiva
2 viajantes 5%
3 viajantes 7%
4 viajantes ou mais 8%

Primeira classe
2 viajantes 10%
3 viajantes 15%
4 viajantes ou mais 20%

O programa deverá exibir o valo BRUTO DA VIAGEM (o mesmo que foi digitado), o VALOR DO DESCONTO,
o VALOR LÍQUIDO DA VIAGEM (Valor bruto menos os descontos) e o VALOR MÉDIO POR VIAJANTE

"""
desconto = 0
valor = int(input(" Informe o valor do pacote: "))
pessoas_qtd = int(input(" Informe q quantidade de viajantes que moram na mesma casa: "))
categoria = int(input(" Informe a categoria: 1-Econômica / 2-Executiva / 3-Primeira Classe "))

if categoria < 1 or categoria > 3:
    print(" Opção inválida")

else:
    # Calculo dos descontos da categoria econômica
    if categoria == 1:
        if pessoas_qtd == 2:
            desconto = valor * 0.03

        elif pessoas_qtd == 3:
            desconto = valor * 0.04

        elif pessoas_qtd >= 4:
            desconto = valor * 0.05

    # Calculo dos descontos da categoria executiva
    if categoria == 2:
        if pessoas_qtd == 2:
            desconto = valor * 0.05

        elif pessoas_qtd == 3:
            desconto = valor * 0.07

        elif pessoas_qtd >= 4:
            desconto = valor * 0.08

    # Calculo dos descontos da categoria primeira classe
    if categoria == 3:
        if pessoas_qtd == 2:
            desconto = valor * 0.10

        elif pessoas_qtd == 3:
            desconto = valor * 0.15

        elif pessoas_qtd >= 4:
            desconto = valor * 0.20

    valor_liquido = valor - desconto
    valor_viajante = valor_liquido / pessoas_qtd

    print("-----------------------------------------")
    print(f" O valor bruto da viagem é {valor}")
    print(f" O valor de desconto será de {desconto} reais")
    print(f" O valor liquido será de {valor_liquido}")
    print(f" O valor a ser pago por cada viajante é de {valor_viajante}")
