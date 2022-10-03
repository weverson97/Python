"""
	Instruções
Projeto Validador de CNPJ
------------------------------------

Este projeto destina-se à fixação dos conceitos aprendidos até aqui (vetores, strings e, especialmente, funções e
procedimentos). Como a lógica de validação do CNPJ é muito similar à do CPF, você poderá reforçar suas habilidades
de programação.
O algoritmo é explicado no link:

http://www.macoratti.net/alg_cnpj.htm


1) No link acima você encontra a explicação do algoritmo usado pela Receita Federal para validação de um CNPJ.
Estude-o e monte uma planilha em Excel ou Calc para implementar a ideia.

2) Crie um código "base" em C que valida o primeiro dígito verificador. Faça um CTRL+C e CTRL+V com atenção, visto que
o algoritmo para o segundo dígito é muito parecido com o do primeiro.

3) Agora vamos melhorar o código anterior com o uso de uma função para validação de um dígito, que você escreverá uma
vez e usará duas vezes.

4) Vamos melhorar mais ainda o código anterior trabalhando na nova entrada dos dígitos do CNPJ. Vamos lê-los com uma
string e processá-la adequadamente.
    CNPJ -> vetor com os dígitos do CNPJ
    mult -> vetor com os multiplicadores, de tamanho N
    N -> Tamanho do vetor mult e também a quantidade de operações (9 ou 10)
"""
soma = 0
def calculaDigito(N, cnpj = [], mult = []):
    for i in range(N):
        soma = soma + cnpj[i] * mult[i]

    return ((soma * 10) % 14) % 10


def imprimeCNPJ(CNPJ = []):
    for i in range(17):
        if i == 1:
            CNPJ.insert(2, ".")

        elif i == 5:
            CNPJ.insert(6, ".")

        elif i == 9:
            CNPJ.insert(10, "/")

        elif i == 15:
            CNPJ.insert(15, "-")

        print("%4d" % CNPJ[i][i], end='')
        print()
    print(CNPJ)




modulo1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
modulo2 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

CNPJ = [4, 1, 9, 5, 9, 8, 8, 0, 0, 0, 0, 1, 0, 5]

teste = calculaDigito(13, CNPJ, modulo1)

imprimeCNPJ(CNPJ)