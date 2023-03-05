## 11 - Mostrar os números pares de 0 a 50 utilizando o comando if

print("### Números pares ###")

contador = 0

while(contador <= 50 ):
    if(contador % 2 == 0):
        print(f'Números Pares:   {contador}')
        contador += 1
    else:
        print(f'Números Ímpares: {contador}')
        contador += 1