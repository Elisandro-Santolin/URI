##4 - Escreva um programa que solicite ao usuário uma temperatura Celsius, converta para Fahrenheit, e mostre a temperatura convertida.##

print("### Conversor de Celsius para Fahrenheit")

celsius = float(input("Digite a temperatura em Celsius: "))

fahrenheint = (celsius * 1.8) + 32

print(f'A temperatura em Fahrenheit é: {fahrenheint:.1f}')
