"""
Em que dia da semana caiu o dia 10 de julho de 1926? Foi num sábado. Como?
Explicação: Procure na Tabela A o ano de 1926 e siga na mesma linha à direita,
parando no mês de julho na Tabela B. Ao número encontrado (neste caso 4),
adicione o número do dia em questão (10) e terá o resultado de 14, verificando na
Tabela C que dará sábado.

"""
L = 0
C = 0
def procurarLinha(max_linha, max_coluna, valor_desejado,line, mat = [C][L]):
    for linha in range(max_linha):
        for coluna in range(max_coluna):
            if mat[coluna][linha] == valor_desejado:
                if line:
                 return linha
                else:
                 return coluna

linhaA = 0
conteudoB = 0
DiaSemana = 0


# tabela dos dias do ano
meses= [[4, 0, 0, 3, 5, 1, 3, 6, 2, 4, 0, 2],
        [5, 1, 1, 4, 6, 2, 4, 0, 3, 5, 1, 3],
        [6, 2, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4],
        [0, 3, 4, 0, 2, 5, 0, 3, 6, 1, 4, 6],
        [2, 5, 5, 1, 3, 6, 1, 4, 0, 2, 5, 0],
        [3, 6, 6, 2, 4, 0, 2, 5, 1, 3, 6, 1],
        [4, 0, 0, 3, 5, 1, 3, 6, 2, 4, 0, 2],
        [5, 1, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4],
        [0, 3, 3, 6, 1, 4, 6, 2, 5, 0, 3, 5],
        [1, 4, 4, 0, 2, 5, 0, 3, 6, 1, 4, 6],
        [2, 5, 5, 1, 3, 6, 1, 4, 0, 2, 5, 0],
        [3, 6, 0, 3, 5, 1, 3, 6, 2, 4, 0, 2],
        [5, 1, 1, 4, 6, 2, 4, 0, 3, 5, 1, 3],
        [6, 2, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4],
        [0, 3, 3, 6, 1, 4, 6, 2, 5, 0, 3, 5],
        [1, 4, 5, 1, 3, 6, 1, 4, 0, 2, 5, 0],
        [3, 6, 6, 2, 4, 0, 2, 5, 1, 3, 6, 1],
        [4, 0, 0, 3, 5, 1, 3, 6, 2, 4, 0, 2],
        [5, 1, 1, 4, 6, 2, 4, 0, 3, 5, 1, 3],
        [6, 2, 3, 6, 1, 4, 6, 2, 5, 0, 3, 5],
        [1, 4, 4, 0, 2, 5, 0, 3, 6, 1, 4, 6],
        [2, 5, 5, 1, 3, 6, 1, 4, 0, 2, 5, 0],
        [3, 6, 6, 2, 4, 0, 2, 5, 1, 3, 6, 1],
        [4, 0, 1, 4, 6, 2, 4, 0, 3, 5, 1, 3],
        [6, 2, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4],
        [0, 3, 3, 6, 1, 4, 6, 2, 5, 0, 3, 5],
        [1, 4, 4, 0, 2, 5, 0, 3, 6, 1, 4, 6],
        [2, 5, 6, 2, 4, 0, 2, 5, 1, 3, 6, 1]]


A1 = [[0 for linha in range(28)] for coluna in range(4)]
"""
print("---- MATRIZ A1 ----")
for linha in range(28):
    for coluna in range(4):
        print("%4d" % A1[coluna][linha], end='')
    print("")
"""

A2 = [[0 for linha in range(28)] for coluna in range(4)]
"""
print("---- MATRIZ A2 ----")
for linha in range(28):
    for coluna in range(4):
        print("%4d" % A2[coluna][linha], end='')
    print()
"""

C = [[0 for linha in range(6)] for coluna in range(7)]
"""
print("---- MATRIZ C ----")
for linha in range(6):
    for coluna in range(7):
        print("%4d" % C[coluna][linha], end='')
    print()
"""
##################### MATRIZ A1 (1901 - 2000) #####################
x = -3
for coluna in range(4):
    for linha in range(28):
        if x < 1:
            A1[coluna][linha] = -1
        elif x < 100:
            A1[coluna][linha] = x
        else:
            A1[coluna][linha] = -1
        x = x + 1

print("---- MATRIZ A1(1901-2000)")
for linha in range(28):
    for coluna in range(4):
        print("%4d" % A1[coluna][linha], end='')
    print("")

##################### MATRIZ A2 (2001 - 2092) #####################
x = -19
for coluna in range(4):
    for linha in range(28):
        if x < 1:
            A2[coluna][linha] = -1
        else:
            A2[coluna][linha] = x
        x = x + 1
print("---- MATRIZ A2 (2001-2092) ----")
for linha in range(28):
    for coluna in range(4):
        print("%4d" % A2[coluna][linha], end='')
    print()

##################### MATRIZ DIA DAS SEMANAS #####################
x = 1
for linha in range(6):
    for coluna in range(7):
        if x < 1:
            C[coluna][linha] = -1
        else:
            C[coluna][linha] = x
        x = x + 1

print("---- MATRIZ C (Dias da Semana) ----")
for linha in range(6):
    for coluna in range(7):
        print("%4d" % C[coluna][linha], end='')
    print()
"""
for linha in range(6):
    for coluna in range(7):
        if C[coluna][linha] == 11:
            liner = linha
            colum = coluna
            break
print(f" linha {liner} coluna {colum}")
"""

dia = int(input(f" \nInforme o dia do nascimento: "))
mes = int(input(f" Informe o mês do nascimento: "))
ano = int(input(f" Informe o ano do nascimento: "))

if ano < 1901 or ano > 2092:
     print("Erro! O Ano deve ser entre 1901 a 2092 \n")

else:
     if ano > 1900 and ano < 2001:
          if ano < 2000:
               ano = ano - 1900
          else:
               ano = ano - 2000
          linhaA = procurarLinha(28, 4, ano, 1, A1)
     else:
          ano = ano - 2000
          linhaA = procurarLinha(28, 4, ano, 1, A2)

conteudoB = meses[linhaA][mes-1]
enviaC = conteudoB + dia
DiaSemana = procurarLinha(6, 7, enviaC, 0, C)

if DiaSemana == 0:
    print("Você nasceu na domingo")

elif DiaSemana == 1:
    print("Você nasceu na segunda")

elif DiaSemana == 2:
    print("Você nasceu na terça")

elif DiaSemana == 3:
    print("Você nasceu na quarta")

elif DiaSemana == 4:
    print("Você nasceu na quinta")

elif DiaSemana == 5:
    print("Você nasceu no sexta")

else:
    print("Você nasceu no sábado")

