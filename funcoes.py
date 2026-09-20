def dobrar(numero): # def dobrar(numero): cria uma função chamada dobrar.
    return numero * 2 # numero é a informação que a função recebe.
# return devolve o resultado.
def mostrar_exemplo():
    numero = 5
    resultado = dobrar(numero) # Chama a função

    print(f"O dobro de {numero} é {resultado}.")

if __name__ == "__main__":
    mostrar_exemplo()