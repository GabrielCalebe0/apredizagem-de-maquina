import pandas as pd
import matplotlib.pyplot as plt

dados = {
    "IMC": [18, 20, 22, 25, 27, 30, 32, 35, 37, 40],
    "Obeso": [False, False, False, False, True, True, True, True, True, True]
}

dataFrame = pd.DataFrame(dados)
dataFrame.to_csv("dados.csv", index=False)

df = pd.read_csv("dados.csv")

plt.scatter(df["IMC"], df["Obeso"], color='blue', label='Dados Originais')
plt.xlabel("IMC")
plt.ylabel("Obeso (True/False)")
plt.title("Relação entre IMC e Obesidade")
plt.legend()
plt.grid()
plt.show()

novo_imc = 28
obeso_estimado = df[df["IMC"] <= novo_imc]["Obeso"].values[-1] if not df[df["IMC"] <= novo_imc].empty else False
print(f"IMC {novo_imc} é obeso? {obeso_estimado}")