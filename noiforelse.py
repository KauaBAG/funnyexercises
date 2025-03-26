def tratamentoporerro(idade):
    try:
        1/int((idade/18)) 
        #Caso a variavel idade seja menor que 18, idade/18 < 1, 
        #assim o método int() transformará esse decimal em 0,
        #induzindo esse programa a erro quando 1/0, após isso,
        #o erro para a execução de try e começa a de except.
        print("Maior de idade")
    except:
        print("Menor de idade")

def tratamentoporlista(idade):
    idade = int(idade/18)
    lista = ["Menor de idade","Maior de idade","Maior de idade","Maior de idade","Maior de idade","Maior de idade","Maior de idade"]
    print(lista[idade])

if __name__ == '__main__':
    idade = int(input("Qual a idade da pessoa? \nR: "))
    tratamentoporerro(idade)
    tratamentoporlista(idade)
