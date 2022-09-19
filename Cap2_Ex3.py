"""
Autor: Weverson Jose da Silva

3 - Hora de decidir! Os colaboradores de sua equipe foram sorteados para ganhar um console de última
geração, cada um, em razão do bom desempenho que tiveram nos últimos projetos. Por uma questão de
logística, porém, a empresa pede que todos os cinco membros da equipe recebam o mesmo aparelhos.

Crie um algoritmo onde o usuário possa digitar o voto de cada um dos 5 membros da equipe e,
ao final, exiba qual foi o console escolhido e com quantos votos.

"""

voto1 = input(" Informe qual o prêmio deseja: PLAYSTATION, XBOX OU NINTENDO: ")
voto2 = input(" Informe qual o prêmio deseja: PLAYSTATION, XBOX OU NINTENDO: ")
voto3 = input(" Informe qual o prêmio deseja: PLAYSTATION, XBOX OU NINTENDO: ")
voto4 = input(" Informe qual o prêmio deseja: PLAYSTATION, XBOX OU NINTENDO: ")
voto5 = input(" Informe qual o prêmio deseja: PLAYSTATION, XBOX OU NINTENDO: ")

pontos_playstation = 0
pontos_xbox = 0
pontos_nintendo = 0

# Verifica o primeiro voto
if voto1.upper() == "PLAYSTATION":
    pontos_playstation = pontos_playstation + 1

elif voto1.upper() == "XBOX":
    pontos_xbox = pontos_xbox + 1

elif voto1.upper() == "NINTENDO":
    pontos_nintendo = pontos_nintendo + 1

else:
    print("O colaborador 1 digitou um console inexistente e seu voto será desconsiderado")

# Verifica o segundo voto
if voto2.upper() == "PLAYSTATION":
    pontos_playstation = pontos_playstation + 1

elif voto2.upper() == "XBOX":
    pontos_xbox = pontos_xbox + 1

elif voto2.upper() == "NINTENDO":
    pontos_nintendo = pontos_nintendo + 1

else:
    print("O colaborador 2 digitou um console inexistente e seu voto será desconsiderado")

# Verifica o terceiro voto
if voto3.upper() == "PLAYSTATION":
    pontos_playstation = pontos_playstation + 1

elif voto3.upper() == "XBOX":
    pontos_xbox = pontos_xbox + 1

elif voto3.upper() == "NINTENDO":
    pontos_nintendo = pontos_nintendo + 1

else:
    print("O colaborador 3 digitou um console inexistente e seu voto será desconsiderado")

# Verifica o quarto voto
if voto4.upper() == "PLAYSTATION":
    pontos_playstation = pontos_playstation + 1

elif voto4.upper() == "XBOX":
    pontos_xbox = pontos_xbox + 1

elif voto4.upper() == "NINTENDO":
    pontos_nintendo = pontos_nintendo + 1

else:
    print("O colaborador 4 digitou um console inexistente e seu voto será desconsiderado")

# Verifica o quinto voto
if voto5.upper() == "PLAYSTATION":
    pontos_playstation = pontos_playstation + 1

elif voto5.upper() == "XBOX":
    pontos_xbox = pontos_xbox + 1

elif voto5.upper() == "NINTENDO":
    pontos_nintendo = pontos_nintendo + 1

else:
    print("O colaborador 5 digitou um console inexistente e seu voto será desconsiderado")


# Verifica resultado geral
if pontos_playstation > pontos_xbox and pontos_playstation > pontos_nintendo:
    print("O console Playstation foi escolhido")

elif pontos_xbox > pontos_playstation and pontos_xbox > pontos_nintendo:
    print("O console XBOX foi escolhido")

elif pontos_nintendo > pontos_playstation and pontos_nintendo > pontos_xbox:
    print("O console Nintendo foi escolhido")

else:
    print("Houve empate")