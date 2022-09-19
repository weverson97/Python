"""
Weverson José da Silva

Ex2 - Os alunos da sua turma fizeram uma votação para escolher qual dia da semana é o melhor para realização daslives.
Desenvolva um programa em que o usuário informe a quantidade de votos que cada um dos  dia da semana:
(Segunda-feira, terça-feira, quarta-feira, quinta-feira, sexta-feira) obtiveram, verifique e exiba qual dia foi
escolhido
"""

voto1 = input("Informe o voto do primeiro candidato (segunda, terça, quarta, quinta, sexta: ")
voto2 = input("Informe o voto do segundo candidato (segunda, terça, quarta, quinta, sexta: ")
voto3 = input("Informe o voto do terceiro candidato (segunda, terça, quarta, quinta, sexta: ")
voto4 = input("Informe o voto do quarto candidato (segunda, terça, quarta, quinta, sexta: ")
voto5 = input("Informe o voto do quinto candidato (segunda, terça, quarta, quinta, sexta: ")

votos_segunda = 0
votos_terça= 0
votos_quarta = 0
votos_quinta = 0
votos_sexta = 0


# Analisa votos do primeiro candidato
if voto1.upper() == "SEGUNDA":
    votos_segunda = votos_segunda + 1

elif voto1.upper() == "TERÇA":
    votos_terça = votos_terça + 1

elif voto1.upper() == "QUARTA":
    votos_quarta = votos_quarta + 1

elif voto1.upper() == "QUINTA":
    votos_quinta = votos_quinta + 1

elif voto1.upper() == "SEXTA":
    votos_sexta = votos_sexta + 1

else:
    print("O primeiro candidato escolheu um dia da semana incorreto. Por isso seu voto será ignorado")

# Analisa votos do segundo candidato
if voto2.upper() == "SEGUNDA":
    votos_segunda = votos_segunda + 1

elif voto2.upper() == "TERÇA":
    votos_terça = votos_terça + 1

elif voto2.upper() == "QUARTA":
    votos_quarta = votos_quarta + 1

elif voto2.upper() == "QUINTA":
    votos_quinta = votos_quinta + 1

elif voto2.upper() == "SEXTA":
    votos_sexta = votos_sexta + 1

else:
    print("O segundo candidato escolheu um dia da semana incorreto. Por isso seu voto será ignorado")

# Analisa votos do terceiro candidato
if voto3.upper() == "SEGUNDA":
    votos_segunda = votos_segunda + 1

elif voto3.upper() == "TERÇA":
    votos_terça = votos_terça + 1

elif voto3.upper() == "QUARTA":
    votos_quarta = votos_quarta + 1

elif voto3.upper() == "QUINTA":
    votos_quinta = votos_quinta + 1

elif voto3.upper() == "SEXTA":
    votos_sexta = votos_sexta + 1

else:
    print("O terceiro candidato escolheu um dia da semana incorreto. Por isso seu voto será ignorado")

# Analisa votos do quarto candidato
if voto4.upper() == "SEGUNDA":
    votos_segunda = votos_segunda + 1

elif voto4.upper() == "TERÇA":
    votos_terça = votos_terça + 1

elif voto4.upper() == "QUARTA":
    votos_quarta = votos_quarta + 1

elif voto4.upper() == "QUINTA":
    votos_quinta = votos_quinta + 1

elif voto4.upper() == "SEXTA":
    votos_sexta = votos_sexta + 1

else:
    print("O quarto candidato escolheu um dia da semana incorreto. Por isso seu voto será ignorado")

# Analisa votos do quinto candidato
if voto5.upper() == "SEGUNDA":
    votos_segunda = votos_segunda + 1

elif voto5.upper() == "TERÇA":
    votos_terça = votos_terça + 1

elif voto5.upper() == "QUARTA":
    votos_quarta = votos_quarta + 1

elif voto5.upper() == "QUINTA":
    votos_quinta = votos_quinta + 1

elif voto5.upper() == "SEXTA":
    votos_sexta = votos_sexta + 1

else:
    print("O quarto candidato escolheu um dia da semana incorreto. Por isso seu voto será ignorado")

# Analisa qual dia da semana ganhou
if votos_segunda > votos_terça and votos_segunda > votos_quarta and votos_segunda > votos_quinta and votos_segunda> votos_sexta:
    print(f"A segunda feira teve a maior pontuação: {votos_segunda} votos")

elif votos_terça> votos_segunda and votos_terça > votos_quarta and votos_terça > votos_quinta and votos_segunda > votos_sexta:
    print(f"A terça feira teve a maior pontuação: {votos_terça} votos")

elif votos_quarta > votos_segunda and votos_quarta > votos_terça and votos_quarta > votos_quinta and votos_segunda > votos_sexta:
    print(f"A quarta feira teve a maior pontuação: {votos_quarta} votos")

elif votos_quinta > votos_segunda and votos_quinta> votos_terça and votos_quinta > votos_quarta and votos_quinta > votos_sexta:
    print(f"A quinta feira teve a maior pontuação: {votos_quinta} votos")

elif votos_sexta > votos_segunda and votos_sexta > votos_terça and votos_sexta > votos_quarta and votos_sexta > votos_quinta:
    print(f"A sexta feira teve a maior pontuação: {votos_sexta} votos")

else:
    print(" Houve empate")