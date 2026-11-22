# MÓDULOS E PACOTES
# um módulo é um arquivo Python que pode ser importado.
# math e datetime são módulos prontos da biblioteca do Python

import math
from datetime import date

# Esta função será chamada pelo main.py.
def mostrar_exemplo():

    # math.sqrt() calcula a raiz quadrada de um número.
    numero = float(input("Escolha um número: "))
    raiz_quadrada = math.sqrt(numero)

    print(f"A raiz quadrada de {numero} é {raiz_quadrada}.")

    hoje = date.today()

    print(f"Data de Hoje: {hoje}")

# Permite testar este arquivo sozinho.
if __name__ == "__main__":
    mostrar_exemplo()