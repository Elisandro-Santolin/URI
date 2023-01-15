## 12 - Mostrar a soma dos números pares múltiplos de 4 entre 1 e 500.

print("### Soma números pares ###")

contador = 0

for num in range(1, 501):
    if num % 2 == 0:
        if num % 4 == 0:
            contador = contador + num
print(f'A soma é: {contador}')

