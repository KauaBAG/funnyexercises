p = int(input("Qual a sua idade: "))
p = int(p/18)
lista = ["Menor de idade","Maior de idade","Maior de idade","Maior de idade","Maior de idade","Maior de idade","Maior de idade"]
print(lista[p])

try:
    1/int((18/p))
    print("Maior de idade")
except:
    print("Menor de idade")
finally:
    print("a")

