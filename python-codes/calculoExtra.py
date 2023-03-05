## 7 - Escreva um programa que recebe o número de horas trabalhadas de um funcionário e o valor pago por cada hora.
## 8 - Calcule quanto ele deverá receber, considerando que se ele trabalhou mais que 40 horas devemos pagá-lo 1.5 vezes o valor da taxa horária.##

print("### Cálculo de Horas Trabalhadas ###")

horas = int(input("Digite horas trabalhadas : "))
valor = int(input("Digite valor pago por hora: "))

if(horas > 40):
    valor = valor / 1.5
    calculo = (horas * valor)
    print(f'Valor a receber: {calculo:.2f}')
else:
    calculo =(horas * valor)
    print(f'Valor a receber: {calculo:.2f}') 