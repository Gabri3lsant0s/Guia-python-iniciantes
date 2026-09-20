# Esta função será chamada pelo menu principal.
def mostrar_exemplo():

    #IF verifica se uma condição é verdadeira.
    # Neste caso: "a idade é maior ou igual a 18?"
    idade = 18 
    print("Verificação de maioridade")
    
    if idade >= 18: 
        print("Você é maior de idade.")
    else:
        # else é executado qunado a condição dp if é falsa.
        print("Você é menor de idade.")

    print()

    # FOR repete um bloco de código.
    # range(1, 6) cria os números de 1 até 5.
    # O número 6 não parece, pois o fim do range não é incluído.
    print("contagem com for:")
    for numero in range(1, 6):
        print(numero)

    print()

    #While também cria uma repetição.
    # Ele continua enquanto a condição for verdadeira.
    contador = 1

    print("Contagem com while:")
    while contador <= 3:
        print(contador)

        #Esta linha aumenta o contador em 1.
        #Sem ela, o contador ficaria sempre em 1:
        #isso criaria um loop infinito.
        contador = contador + 1

# Permite testar este arquivo sozinho com:
# py estruturas_fluxos.py
if __name__ == "__main__":
    mostrar_exemplo()