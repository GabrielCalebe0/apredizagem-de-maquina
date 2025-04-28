from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier

iris = load_iris()
X = iris.data   
y = iris.target 
nomes_especies = iris.target_names 

modelo = KNeighborsClassifier(n_neighbors=3)

modelo.fit(X, y)

print("Informe as características da flor para prever a espécie:")

comprimento_sepala = float(input("Comprimento da sépala (cm): "))
largura_sepala = float(input("Largura da sépala (cm): "))
comprimento_petala = float(input("Comprimento da pétala (cm): "))
largura_petala = float(input("Largura da pétala (cm): "))

amostra = [[comprimento_sepala, largura_sepala, comprimento_petala, largura_petala]]

predicao = modelo.predict(amostra)

print("A espécie da flor é:", nomes_especies[predicao[0]])