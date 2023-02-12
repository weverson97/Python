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

CNPJ_Informado = [ ]
CNPJ_Validado = [ ]

modulo1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
modulo2 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

cnpj = input("Informe o CNPJ:")
size = len(cnpj) #Verifica o tamanho do CNPJ

print (size)

#if size < 14 or size > 14: #Avalia quantidades de digitos
if size > 30: #Avalia quantidades de digitos
    print("O CNPJ não contém 14 dígitos")

else: # Se o cpf tiver 14 digitos, converte em array com valores inteiro
    
    for i in range(20):  
        CNPJ_Informado.insert(i, cnpj[i])  
        if (CNPJ_Informado[i] == ".") or (CNPJ_Informado[i] == "/") or (CNPJ_Informado[i] == "-"):
            #CNPJ_Informado[i] = "x"
            #CNPJ_Informado.pop(i)
            #size = len(cnpj) #Verifica o tamanho do CNPJ
            print (i)
    
    print(CNPJ_Informado)  
    try:
         CNPJ_Informado.remove(".")
         CNPJ_Informado.remove(".")

    except ValueError:
        print("Item não existe")
   
    print(CNPJ_Informado)      
    
    """        
    print(CNPJ_Informado)        
    del CNPJ_Informado["."]
    print(CNPJ_Informado)
    
    CNPJ_Informado.remove("x")
    print(CNPJ_Informado)


          
    for i in range(size):  
         if   (cnpj[i] == ".") or (cnpj[i] == "/") or (cnpj[i] == "-"):
                print(i)
                cnpj[i] = " x "
                #print (cnpj[i])
    print (cnpj)

    for i in range(size):
        CNPJ_Informado.insert(i, int (cnpj [i]))
        CNPJ_Validado.insert(i, int (cnpj [i]))

    

    # ------------------- Deleta posição 13 e 12 do array -------------------
    CNPJ_Validado.pop(13) #Apaga a posição 13
    CNPJ_Validado.pop(12) #Apaga a posição 12

    # ------------------- Procura primeiro digito  -------------------
    first_digito = calculaDigito(12, CNPJ_Validado, modulo1) 
    #print(first_digito)
    CNPJ_Validado.insert(12, first_digito) ## Acrescenta o primeiro digito na ultima posição

    # ------------------- Procura segundo digito  -------------------
    second_digito = calculaDigito(13, CNPJ_Validado, modulo2)
    #print(second_digito)
    CNPJ_Validado.insert(13, second_digito)

    # ------------------- Avalia se o CNJP é válido  -------------------
    if CNPJ_Informado == CNPJ_Validado :
        print("CNPJ válido :)")
    else:
        print("CNPJ inválido :(")


"""