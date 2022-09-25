"""
Weverson José da Silva
Ex2 - Os alunos da sua turma fizeram uma votação para escolher qual dia da semana é o melhor para realização das lives.
Desenvolva um programa em que o usuário informe a quantidade de votos que cada um dos dias da semana:
(Segunda-feira, terça-feira, quarta-feira, quinta-feira, sexta-feira) obtiveram, verifique e exiba qual dia foi
escolhido
"""

segunda = int(input("Informe os votos da segunda-feira: "))
terça = int(input("Informe os pontos da terça-feira: "))
quarta = int(input("Informe os pontos da quarta-feira: "))
quinta = int(input("Informe os pontos da quinta-feira: "))
sexta = int(input("Informe os pontos da sexta-feira: "))

# Analisa qual dia da semana ganhou
if segunda > terça and segunda > quarta and segunda > quinta and segunda > sexta:
    print(f"A segunda-feira teve a maior quantidade de votos: {segunda} ")

elif terça > segunda and terça > quarta and terça > quinta and terça > sexta:
    print(f"A terça-feira teve a maior quantidade de votos: {terça} ")

elif quarta > segunda and quarta > terça and quarta > quinta and quarta > sexta:
    print(f"A quarta-feira teve a maior quantidade de votos: {quarta} ")

elif quinta > segunda and quinta > terça and quinta > quarta and quinta > sexta:
    print(f"A quinta-feira teve a maior quantidade de votos: {quinta} ")

elif sexta > segunda and sexta > terça and sexta > quarta and sexta > quinta:
    print(f"A sexta-feira teve a maior quantidade de votos: {sexta} ")

else:
    print(" Houve empate")