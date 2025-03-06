def obter_frase():

    while True:
        frase = input("Digite uma frase: ").strip()
        if frase:
            return frase
        print("A entrada está vazia. Tente novamente.")

def analisar_frase(frase):

    num_caracteres = len(frase)
    palavras = frase.split()
    num_palavras = len(palavras)
    maior_palavra = max(palavras, key=len) if palavras else ""
    
    return num_caracteres, num_palavras, maior_palavra, palavras

def manipular_frase(frase, palavras):

    frase_invertida_chars = frase[::-1]
    frase_invertida_palavras = " ".join(reversed(palavras))
    frase_maiusculas = frase.upper()
    frase_minusculas = frase.lower()
    tupla_palavras = tuple(palavras)
    
    return (frase_invertida_chars, frase_invertida_palavras, 
            frase_maiusculas, frase_minusculas, tupla_palavras)

def exibir_resultados(num_caracteres, num_palavras, maior_palavra, 
                      frase_invertida_chars, frase_invertida_palavras, 
                      frase_maiusculas, frase_minusculas, tupla_palavras):

    print("\nResultados da análise:")
    print(f"Número total de caracteres: {num_caracteres}")
    print(f"Número total de palavras: {num_palavras}")
    print(f"Palavra mais longa: {maior_palavra}")
    print(f"Frase invertida (por caracteres): {frase_invertida_chars}")
    print(f"Frase invertida (por palavras): {frase_invertida_palavras}")
    print(f"Frase em maiúsculas: {frase_maiusculas}")
    print(f"Frase em minúsculas: {frase_minusculas}")
    print(f"Tupla de palavras: {tupla_palavras}")

frase_usuario = obter_frase()
num_caracteres, num_palavras, maior_palavra, palavras = analisar_frase(frase_usuario)
(frase_invertida_chars, frase_invertida_palavras, 
 frase_maiusculas, frase_minusculas, tupla_palavras) = manipular_frase(frase_usuario, palavras)

exibir_resultados(num_caracteres, num_palavras, maior_palavra, 
                  frase_invertida_chars, frase_invertida_palavras, 
                  frase_maiusculas, frase_minusculas, tupla_palavras)
