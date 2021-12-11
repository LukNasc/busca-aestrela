from busca import AEstrela
from grafo import Grafo

grafo = Grafo()

a_estrela = AEstrela(grafo.bucharest)
a_estrela.busca(grafo.arad)