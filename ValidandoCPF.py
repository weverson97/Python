"""
	Instruções
Projeto Validador de CNPJ
------------------------------------

Este projeto destina-se à fixação dos conceitos aprendidos até aqui (vetores, strings e, especialmente, funções e
procedimentos). Como a lógica de validação do CNPJ é muito similar à do CPF, você poderá reforçar suas habilidades
de programação.
O algoritmo é explicado no link:

https://www.macoratti.net/alg_cpf.htm


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

def calculaDigito(N, cnpj = [], mult = []):
    soma = 0
    for i in range(N):
        soma = soma + cnpj[i] * mult[i]
    resto = soma % 11

    if resto < 2:
        return 0
    else:
        return 11 - resto



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




modulo1 = [10, 9, 8, 7, 6, 5, 4, 3, 2]
modulo2 = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]

#CPF_Informado = [4, 3, 1, 8, 6, 4, 4, 6, 8, 5, 6]
#CPF_Validado = [4, 3, 1, 8, 6, 4, 4, 6, 8]

CPF_Informado = [4, 0, 2, 5, 5, 4, 3, 8, 8, 5, 0]
CPF_Validado = [4, 0, 2, 5, 5, 4, 3, 8, 8]

first_digito = calculaDigito(9, CPF_Validado, modulo1) # 4,3,1,8,6,4,4,6,8
print(first_digito)
print(CPF_Validado)
CPF_Validado.insert(9, first_digito) ## Acrescenta o primeiro digito na ultima posição
print(CPF_Validado)

second_digito = calculaDigito(10, CPF_Validado, modulo2)
print(second_digito)
CPF_Validado.insert(10, second_digito)

print(CPF_Validado)
#print(CPF)

if CPF_Informado == CPF_Validado:
    print("Your CPF is valid")
else:
    print("Your CPF isn't valid")

#imprimeCNPJ(teste)