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

# A lista pode guardar objetos de classes diferente, desde que todos sejam animais.
    animais =[leao, canario, cachorro]

# Para cada animal dentro da lista: 
    for animal in animais:

    # A mesma chamada de método gera resultados diferentes.
    # Isso é polimorfismo.
        print(f"{animal.nome} emite o som: {animal.emitir_som()}")

    if isinstance(animal, Cachorro):
            print(f"Raça: {animal.raca}")

# permite executar este arquivo sozinho para testar.
if __name__ == "__main__":
    mostrar_exemplo()
