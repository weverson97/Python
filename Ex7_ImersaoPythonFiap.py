"""
7. Faça um programa que peça o nome de um produto, o valor unitário, a quantidade de itens
comprados, e mostre o valor total a pagar.

"""
name_product = input ("Inform the name from product? ")
value_unit = float(input("Inform the unit value from product? "))
how_much = int(input("Inform the how much product you will buy? "))

value_pay = value_unit * how_much

print (f"You will pay {value_pay} dollars ")