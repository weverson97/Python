"""
4. Faça um programa que peça uma frase para a pessoa e mostre a quantidade de letras que temresultado das 4 operacoes entre os dois aprendendo
na frase.

"""
phrase = input(" Inform any phrase: ")

phrase_complete = len(phrase)
phrase_without_space_aux = phrase.replace(" " ,"")
phrase_without_space = len(phrase_without_space_aux)

print(f" The phrase complete have {phrase_complete}")

print(f" The phrase without sapce have {phrase_without_space}")

