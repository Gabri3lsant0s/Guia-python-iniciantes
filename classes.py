# Class cria um modelo para criar objetos.
# Aqui, TV será o modelo de uma televisão.
class TV: 

    # __init__ é chamado automaticamente quando criamos um objeto.
    # self representa a TV que está sendo criada.
    def __init__(self, marca, tamanho,preco): 

        # Atributos são características do objeto.
        self.marca = marca
        self.tamanho = tamanho
        self.preco = preco

        #Toda TV nova começa desligada.
        self.ligada = False

    # Método é uma função que pertence à classe.
    def ligar(self):
        self.ligada = True
        print("A TV foi ligada.")

    def mostrar_descricao(self):
        # if em uma linha: escolhe o texto conforme o estado da TV.
        estado = "ligada" if self.ligada else "desligada"

        print(f"Marca: {self.marca}")
        print(f"Tamanho: {self.tamanho} polegadas")
        print(f"Preço: R$ {self.preco:.2f}")
        print(f"Estado: {estado}")

# Esta função será chamada pelo main.py.
def mostrar_exemplo():

    # Criamos um objeto chamado tv_sala a partir do modelo TV.
    tv_sala = TV("Samsung", 43, 2400.00)

    print("Antes de ligar:")
    tv_sala.mostrar_descricao()

    print()

    # Chamamos o método ligar() do objeto.
    tv_sala.ligar()

    print()

    print("Depois de ligar:")
    tv_sala.mostrar_descricao()

#Permite testar somente este arquivo com: py classes.py
if __name__ == "__main__":
    mostrar_exemplo()