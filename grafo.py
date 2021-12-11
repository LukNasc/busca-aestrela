from vertice import Vertice
from adjacentes import Adjacente

class Grafo:
  arad = Vertice("Arad", 366)
  zerind = Vertice("Zerind", 374)
  oradea = Vertice("Oradea", 380)
  sibiu = Vertice("Sibiu", 253)
  timisoara = Vertice("Timisoara", 329)
  lugoj = Vertice("Lugoj", 244)
  mehadia = Vertice("Mehadia", 241)
  dobreta = Vertice("Dobreta", 242)
  craiova = Vertice("Craiova", 160)
  rimnicu = Vertice("Rimnicu", 193)
  fagaras = Vertice("Fagaras", 178)
  pitesti = Vertice("Pitesti", 98)
  bucharest = Vertice("Bucharest", 0)
  giurgiu = Vertice("Giurgiu", 77)

  arad.add_adjacente(Adjacente(zerind, 75))
  arad.add_adjacente(Adjacente(sibiu, 140))
  arad.add_adjacente(Adjacente(timisoara, 118))

  zerind.add_adjacente(Adjacente(arad, 75))
  zerind.add_adjacente(Adjacente(oradea, 71))

  oradea.add_adjacente(Adjacente(zerind, 71))
  oradea.add_adjacente(Adjacente(sibiu, 151))

  sibiu.add_adjacente(Adjacente(oradea, 151))
  sibiu.add_adjacente(Adjacente(arad, 140))
  sibiu.add_adjacente(Adjacente(fagaras, 99))
  sibiu.add_adjacente(Adjacente(rimnicu, 80))

  timisoara.add_adjacente(Adjacente(arad, 118))
  timisoara.add_adjacente(Adjacente(lugoj, 111))

  lugoj.add_adjacente(Adjacente(timisoara, 111))
  lugoj.add_adjacente(Adjacente(mehadia, 70))

  mehadia.add_adjacente(Adjacente(lugoj, 70))
  mehadia.add_adjacente(Adjacente(dobreta, 75))

  dobreta.add_adjacente(Adjacente(mehadia, 75))
  dobreta.add_adjacente(Adjacente(craiova, 120))

  craiova.add_adjacente(Adjacente(dobreta, 120))
  craiova.add_adjacente(Adjacente(pitesti, 138))
  craiova.add_adjacente(Adjacente(rimnicu, 146))

  rimnicu.add_adjacente(Adjacente(craiova, 146))
  rimnicu.add_adjacente(Adjacente(sibiu, 80))
  rimnicu.add_adjacente(Adjacente(pitesti, 97))

  fagaras.add_adjacente(Adjacente(sibiu, 99))
  fagaras.add_adjacente(Adjacente(bucharest, 211))

  pitesti.add_adjacente(Adjacente(rimnicu, 97))
  pitesti.add_adjacente(Adjacente(craiova, 138))
  pitesti.add_adjacente(Adjacente(bucharest, 101))

  bucharest.add_adjacente(Adjacente(fagaras, 211))
  bucharest.add_adjacente(Adjacente(pitesti, 101))
  bucharest.add_adjacente(Adjacente(giurgiu, 90))