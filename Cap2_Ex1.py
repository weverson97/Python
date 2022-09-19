"""
Autor: Weverson Jose da Silva

1 - Verificar se os batimentos cardíacos por minuto se encontram na fixa adequada. Para isso, você deve
solicitar ao usuário que informe o seu número de batimentos por minuto (BPM) e a idade. A partir disso,
o script deve verificar e exibir uma mensagem informando se os batimentos do usuário encontram-se
dentro da faixa adequada. Acima da faixa adequada ou abaixo da faixa adequada, de acordo com o
site: https://www.tuasaude.com/frequencia-cardiaca/#:~:text=At%C3%A9%202%20anos%20de%20idade,idosos%3A%2050%20a%2060%20bpm

Até 2 anos de idade: 120 a 140 bpm,
Entre 8 anos até 17 anos: 80 a 100 bpm,
Adulto sedentário: 70 a 80 bpm,
Idosos: 50 a 60 bpm. - 60 anos
"""

idade = int(input(" Informe sua idade: "))
batimentos = int(input(" Informe os batimentos por minuto: "))

if idade <= 2:
    if batimentos >= 120 and batimentos <= 140:
        print(" Seus batimentos encontram-se DENTRO da faixa etária")

    elif batimentos < 120:
        print(" Seus batimentos encontram-se ABAIXO da faixa etária")

    else:
        print(" Seus batimentos encontram-se ACIMA da faixa etária")

elif idade >= 7 and idade <= 17:
    if batimentos >= 80 and batimentos <= 100:
        print(" Seus batimentos encontram-se DENTRO da faixa etária")

    elif batimentos < 80:
        print(" Seus batimentos encontram-se ABAIXO da faixa etária")

    else:
        print(" Seus batimentos encontram-se ACIMA da faixa etária")

elif idade >= 18 and idade <= 60:
    if batimentos >= 70 and batimentos <= 80:
        print(" Seus batimentos encontram-se DENTRO da faixa etária")

    elif batimentos < 70:
        print(" Seus batimentos encontram-se ABAIXO da faixa etária")

    else:
        print(" Seus batimentos encontram-se ACIMA da faixa etária")

else:
    if batimentos >= 50 and batimentos <= 60:
        print(" Seus batimentos encontram-se DENTRO da faixa etária")

    elif batimentos < 50:
        print(" Seus batimentos encontram-se ABAIXO da faixa etária")

    else:
        print(" Seus batimentos encontram-se ACIMA da faixa etária")



