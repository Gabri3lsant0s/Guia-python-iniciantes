# HERANÇA E POLIFORMISMO
#
# Herança permite criar uma classe mais específica a partir de uma classe mais genérica.

# Animal é a classe-base.
# Ela guarda o que todos os animais têm em comum.

class Animal:

    #__Init__ é chamado quando um objeto é criado.
    def __init__(self, nome):

        #self.nome guarda o nome de cada animal.
        self.nome = nome
    # Este método representa o som de um animal genérico.
    def emitir_som(self):
        return "Som desconhecido"
    
    # Mamifero é uma classe filha de Animal.
    # O texto entre parênteses informa que Mamifero herda de Animal.
class Mamifero(Animal):


    # Este método tem o mesmo nome do método da classe Animal.
    #Porém, ele possui um comportamento diferente.
    def emitir_som(self):
        return "Rugido"

# Esta função será chamada pelo main.py.
def mostrar_exemplo():

# criamos um objeto da classe Animal.
    animal_generico = Animal("Animal genérico")

#Criamos um objeto da classe Mamífero.
    leao = Mamifero("Leão")

#cada objeto chama o método emitir_som().
    print(f"{animal_generico.nome} emite: {animal_generico.emitir_som()}")
    print(f"{leao.nome} emite: {leao.emitir_som()}")

# permite executar este arquivo sozinho para testar.
if __name__ == "__main__":
    mostrar_exemplo()
