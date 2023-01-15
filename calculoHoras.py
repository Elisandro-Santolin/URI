## 2 - Escreva um programa que solicite ao usuário as horas trabalhadas e o valor pago por cada hora para calcular o valor a ser pago por suas horas de serviço.

print("### Cálculo de Horas Trabalhadas ###")

horas = int(input("Digite horas trabalhadas : "))
valor = int(input("Digite valor pago por hora: "))

calculo = (valor * horas)

print(f'O valor total é: {calculo:.2f}')

