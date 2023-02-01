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

def calculaDigito(N, cpf = [], mult = []):
    soma = 0
    for i in range(N):
        soma = soma + cpf[i] * mult[i]
    resto = soma % 11

    if resto < 2:
        return 0
    else:
        return 11 - resto

CPF_Informado = [ ]
CPF_Validado = [ ]
CPF_Aux = [ ]
modulo1 = [10, 9, 8, 7, 6, 5, 4, 3, 2]

modulo2 = modulo1
modulo2.insert(0, 11) # Acrescenta o valor 11 na primeira posição do array modulo2 = [11,10,9,8,7,6,5,4,3,2]

cpf = input("Informe seu CPF:")
size = len(cpf) #Verifica o tamanho do cpf

if size < 11 or size > 11: #Avalia quantidades de digitos
    print("Seu CPF não contém 11 dígitos")

else: # Se o cpf tiver 11 digitos, converte em array com valores inteiro
    for i in range(size):
        CPF_Informado.insert(i, int (cpf[i]))

print(f" CPF validado é {CPF_Validado}")
print(f" CPF informado é {CPF_Informado}")
  
  
CPF_Validado = CPF_Informado
# CPF_Validado = [4,3,1,8,6,4,4,6,8,8,8]


print(f" CPF validado é {CPF_Validado}")
print(f" CPF informado é {CPF_Informado}")

# ------------------- Deleta posição 09 e 10 do array -------------------
CPF_Validado.pop(10) #Apaga a posição 10
CPF_Validado.pop(9) #Apaga a posição 09

print(f" CPF validado é {CPF_Validado}")
print(f" CPF informado é {CPF_Informado}")
# ------------------- Procura primeiro digito  -------------------
first_digito = calculaDigito(9, CPF_Validado, modulo1) 
print(first_digito)
CPF_Validado.insert(9, first_digito) ## Acrescenta o primeiro digito na ultima posição

print(f" CPF validado é {CPF_Validado}")
print(f" CPF informado é {CPF_Informado}")
# ------------------- Procura segundo digito  -------------------
second_digito = calculaDigito(10, CPF_Validado, modulo2)
print(second_digito)
CPF_Validado.insert(10, second_digito)

print(f" CPF validado é {CPF_Validado}")
print(f" CPF informado é {CPF_Informado}")
# ------------------- Avalia se o CPF é válido  -------------------

print(f" CPF validado é {CPF_Validado}")
print(f" CPF informado é {CPF_Informado}")

if CPF_Informado == CPF_Validado :
    print("Seu CPF é válido :)")
else:
    print("Seu CPF  não está válido :(")


