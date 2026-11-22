from funcoes import mostrar_exemplo as mostrar_funcoes
from colecoes import mostrar_exemplo as mostrar_colecoes
from estruturas_fluxo import mostrar_exemplo as mostrar_estruturas_fluxo
from classes import mostrar_exemplo as mostrar_classes
from palindromo import mostrar_desafio as mostrar_desafio_palindromo
from heranca_polimorfismo import mostrar_exemplo as mostrar_heranca_polimorfismo
from modulos_pacotes import mostrar_exemplo as mostrar_modulos_pacotes

#While True cria um loop que continua para sempre.
# Ele só será interrompido qunado encontrarmos o break.
while True:

    print("\n === Guia Python para Iniciantes ===")
    print("1 - Funções")
    print("2 - Listas e dicionários")
    print("3 - Condições e laços")
    print("4 - Classes")
    print("5 - Desafio Palídromo")
    print("6 - Herança e Polimorfismo")
    print("7 - Módulos e pacotes")
    print("0 - Sair")

    # input() sempre recebe o que foi digitado como texto.
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("\n--- Funções ---")
        mostrar_funcoes()

    elif opcao == "2":
        print("\n--- Listas e dicionários ---")
        mostrar_colecoes()

    elif opcao == "3":
        print("\n--- Condições e laços ---")
        mostrar_estruturas_fluxo()

    elif opcao == "4":
        print("\n--- Classes e objetos ---")
        mostrar_classes()

    elif opcao == "5":
        print("\n--- Desafio Palíndromo ---")
        mostrar_desafio_palindromo()

    elif opcao == "6":
        print("\n--- Herança e Polimorfismo ---")
        mostrar_heranca_polimorfismo()

    elif opcao == "7":
        print("\n--- Módulos e pacotes ---")
        mostrar_modulos_pacotes()

    elif opcao == "0":
        print("Até mais!")

        # break encerra o while True e finaliza o programa.
        break

    else:
        print("Opção inválida. Tente novamente.")