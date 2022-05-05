import networkx as nx
import matplotlib.pyplot as plt
import esqueleto_tokeniza as tk

class Grafo:
    
    def __init__(self, lista_tokens) -> None:
        self.lista_tokens = lista_tokens
        self.grafo = nx.Graph()

    def construir_grafo(self):
        # constroi vertices
        for token in self.lista_tokens:
            item = token[0]
            self.grafo.add_node(item)

        # constroi arestas
        for indice in range(len(self.lista_tokens)):
            item, tipo = self.lista_tokens[indice]

            if tipo == tk.OPERADOR:
                item_passado = self.lista_tokens[indice-1][0]
                self.grafo.add_edge(item_passado, item)

            if tipo == tk.NUMERO:
                item_passado = self.lista_tokens[indice-1][0]
                self.grafo.add_edge(item_passado, item)

            if tipo == tk.PARENTESES:
                item_passado = self.lista_tokens[indice-1][0]
                self.grafo.add_edge(item_passado, item)

            if tipo == tk.VARIAVEL and not indice == 0:
                item_passado = self.lista_tokens[indice-1][0]
                self.grafo.add_edge(item_passado, item)


    def mostrar_vertices(self):
        print(self.grafo.nodes())

    def mostrar_arestas(self):
        print(self.grafo.adges())

    def plotar_grafo(self):
        plt.figure(2)
        nx.draw_networkx(self.grafo, with_labels=True)
        plt.savefig('grafo.png')