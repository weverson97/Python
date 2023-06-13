"""
5. Faça um programa que peça cinco números e mostre qual o maior e qual o menor.
"""


biggest = float("-inf")
smaller = float(" inf")

for i in range(5):
    number_current = float(input("Inform the number: "))
    
    if number_current > biggest:
        biggest = number_current

    if number_current < smaller:
        smaller = number_current    


print("The biggest number is:", biggest)
print("The smaller number is:", smaller)


