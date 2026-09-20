# Esta função reúne o exemplo que será chamado pelo menu principal.
def mostrar_exemplo():

    #LISTA:
    #Uma lista guarda vários valores em uma ordem.
    # Os itens ficam entre colchetes: []
    frutas = ["maçã", "banana", "Laranja"] 

    # append() adiciona um novo item ao fim da lista.
    frutas.append("uva")

    #print() mostra uma mensagem no terminal.
    print("Frutas disponíeis:")

    #FOR:
    # for cria uma repetição.
    #
    #fruta é uma variável criada a cada repetição.
    # Ela recebe uma fruta por vez da lista.
    #
    # IN significa "dentro de":
    # "para cada fruta dentro de frutas, faça o código abaixo".
    for fruta in frutas:

        # Esta linha está identada (com espaços no começo).
        # Isso indica que ela pertence ao for e será repetida.
        print(f"- {fruta}")

    # print() vazio cria uma linha em branco, só para organizar a saída.
    print()

    #DICIONÁRIO: 
    # Um dicionário guarda pares de chave e valor.
    #Neste caso, o nome é a chave e a nota é o valor.
    # Dicionários usam chaves: {}
    notas = {
        "Ana": 9.5,
        "João": 8.0, 
        "Maria": 7.5
    }

    print("Notas dos alunos:") 

    # items() entrega a chave e o valor de cada item do dicionário.
    #
    # for aluno, nota:
    # aluno recebe o nome, e nota recebe o valor correspondente.
    #
    #in notas.items() significa:
    # "para cada nome e nota dentro do dicionário notas".
    for aluno, nota in notas.items():

        #f antes das aspas permite xolocar variáveis entre {} no texto.
        print(f"{aluno}: {nota}")

# Esta condição é verdadeira apenas se colecoes.py for executado diretamente:
# py colecoes.py
#
# Se ele for importado pelo main.py, o exemplo não roda automaticamente.
if __name__ == "__main__":
    mostrar_exemplo()