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

    #Cachorro herda de mamifero, como mamifero já herda de animal, cachorro também herda de animal.
class Cachorro(Mamifero):

    def __init__(self, nome, raca):

        #super() chama o __init__ da classe mãe.
        #Assim, não precisamos escrever self.nome = nome novamente.
        super().__init__(nome)

        # raca é juma característica especifíca de cachorro.
        self.raca = raca
            
            # Cachorro substitui o som que viria de Mamifero.
    def emitir_som(self):
        return "Latido"

# Zoologico não herda de Animal, ele apeas guarda vários objetos Animal.
class Zoologico:

    def __init__(self, nome):
        self.nome = nome

        # Começamos com uma lista vazia de animais.
        self.animais = []

    def adicionar_animal(self, animal):

        # append() adiciona o objeto Animal à lista de.
        self.animais.append(animal)

    def apresentar_animais(self):
        print(f"\n--- Animais do {self.nome} ---")

        # Percorre todos os anumais que o zoolómgico possui.
        for animal in self.animais:
            print(f"{animal.nome} emite o som: {animal.emitir_som()}")

            # Mostra a raça apenas se o animal for um cachorro.
            if isinstance(animal, Cachorro):
                print(f"Raça: {animal.raca}")

# Ave também herda da classe Animal.
class Ave(Animal):

    # A ave possui sua própria versão de método emitir_som().
    def emitir_som(self):
        return "Canto"

# Esta função será chamada pelo main.py.
def mostrar_exemplo():

#Criamos um objeto da classe Mamífero.
    leao = Mamifero("Leão")
    canario = Ave("Canário")
    cachorro = Cachorro("Rex", "Labrador")

# Criamos um zoológico
    zoologico = Zoologico("Zoológico da Central")

# Adicionamos objetos de classes diferentes.
    zoologico.adicionar_animal(leao)
    zoologico.adicionar_animal(canario)
    zoologico.adicionar_animal(cachorro)

# Pedimos ao zoológico para apresentar seus animais.
    zoologico.apresentar_animais()

# permite executar este arquivo sozinho para testar.
if __name__ == "__main__":
    mostrar_exemplo()
