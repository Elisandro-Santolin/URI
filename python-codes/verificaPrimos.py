## 14 - Mostrar os números primos de 2 até o número digitado pelo usuário. 

entradaNumeros = int(input("Verificar numeros primos ate: "))
multiplicador =0

for contador in range(2,entradaNumeros):
    if (entradaNumeros % contador == 0):
        print("Múltiplo de: ", contador)
        multiplicador += 1

    if(multiplicador==0):
        print("É primo")
else:
    print("Tem",multiplicador," múltiplos acima de 2 e abaixo de",entradaNumeros)