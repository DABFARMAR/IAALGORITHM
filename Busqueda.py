from Pila import Pila
from Cola import Cola
from Laberinto import Laberinto


class Busqueda:
    def __init__(self, laberinto):
        self.laberinto = laberinto
        self.frontera = Cola(laberinto.getSize())
        self.explorados = Pila(laberinto.getSize())
        self.estado_inicial = laberinto.getInicio()
        self.estado_objetivo = laberinto.getObjetivo()

    def buscarSolucion(self):
        self.frontera.agregar(self.estado_inicial)

        while not self.frontera.vacia():
            nodo = self.frontera.remover()
            self.laberinto.mostrar(nodo)

            if nodo == self.estado_objetivo:
                print("Objetivo encontrado en la posicion:", nodo)
                return nodo

            self.explorados.agregar(nodo)
            vecinos = self.laberinto.getVecinos(nodo)

            for vecino in vecinos:
                if not self.frontera.contiene(vecino) and not self.explorados.contiene(vecino):
                    self.frontera.agregar(vecino)

        print("No existe solución.")
        return


laberinto = Laberinto("maze4.txt")
b = Busqueda(laberinto)
b.buscarSolucion()
