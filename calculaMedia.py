## 3 - Escreva um script que leia 4 notas de um aluno e imprima a média dele.

print("### Calculadora de Média ###")

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))

media = (nota1 + nota2 + nota3 + nota4) / 4

print(f'Sua média é: {media:.2f}')