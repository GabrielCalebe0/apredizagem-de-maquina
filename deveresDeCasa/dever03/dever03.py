import csv

dados = [
    ["Nome", "Idade"],
    ["Ana", 25],
    ["Bruno", 30],
    ["Carla", 22],
    ["Daniel", 28],
    ["Eduardo", 35]
]

with open("dados.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(dados)

dados_lista = []
with open("dados.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    next(reader)  
    for linha in reader:
        nome, idade = linha[0], int(linha[1])
        dados_lista.append((nome, idade))

idade_maxima = max(dados_lista, key=lambda x: x[1])[1]

nome_digitado = input("Digite um nome para procurar na lista: ")

encontrado = False
for nome, idade in dados_lista:
    if nome_digitado.strip().lower() == nome.lower():
        encontrado = True
        if idade == idade_maxima:
            print(f"{nome} tem {idade} anos e é a pessoa mais velha da lista.")
        else:
            print(f"{nome} tem {idade} anos e não é a pessoa mais velha da lista.")
        break

if not encontrado:
    print(f"O nome '{nome_digitado}' não foi encontrado na lista. Talvez tenha digitado errado?")
