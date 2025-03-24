import pandas as pd
import random


frutas = [
    "maçã",
    "banana",
    "laranja",
    "uva",
    "maçã",
    "melão",
    "mamão",
    "banana"
]

with open("frutas.txt", "w") as file:
    for fruta in lisFrutas:
        quantidade = random.randint(0, 100)
        file.write(f"{fruta},{quantidade}\n")

frutas_dict = {}
with open("frutas.txt", "r") as file:
    for line in file:
        fruta, quantidade = line.strip().split(",")
        quantidade = int(quantidade)
        if fruta in frutas_dict:
            frutas_dict[fruta] += quantidade
        else:
            frutas_dict[fruta] = quantidade

df = pd.DataFrame(list(frutas_dict.items()), columns=["Fruta", "Quantidade"])

print(df)