# Verifica se um texto é igual quando lido de trás para frente.
def eh_palindromo(texto):

    # deixa tudo minúsculo e remove os espaços.
    texto_normalizado = texto.lower().replace(" ", "")

    # [::-1] inverte o texto.
    texto_invertido = texto_normalizado[::-1]

    # Retorna True se os dois textos forem iguais.
    return texto_normalizado == texto_invertido

def mostrar_desafio():
    print("--- Desafio: Palíndromo ---")

    # Recebe uma palavra ou frase digitada.
    texto = input("Digite uma palavra ou frase: ")

    # Guarda o resultado da verificação. 
    resultado = eh_palindromo(texto)

    if resultado: 
        print(f'"{texto}" é um palíndromo.')
    else:
        print(f'"{texto}" não é um palíndromo.')

# Permite testar apenas este arquivo. py palindromo.py
if __name__ == "__main__":
    mostrar_desafio()