## 13 - Solicitar um número para o usuário e mostrar a tabuada desse número. ##

print("### Tabuada ###")

tabuada = int(input("Tabuada do número: "))

for contador in range(10):
    print("%d x %d = %d" % (tabuada, contador+1, tabuada*(contador+1)) )