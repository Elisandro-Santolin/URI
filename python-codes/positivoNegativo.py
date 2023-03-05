## 6 - Escrever um algoritmo que receba um número e diga se ele é positivo, negativo ou nulo. ##

entrada = int(input("Digite um número: "))

if(entrada > 0):
    print("O número digitado é maior que zero, é positivo!")
elif(entrada < 0):
    print("O número digitado é menor que zero, é negativo!")
else:
    print("O número é igual a zero, número nulo")
