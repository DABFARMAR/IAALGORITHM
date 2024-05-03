from Pila import Pila
from Cola import Cola


class Nodo:
    def __init__(self, posicion, padre=None):
        self.posicion = posicion
        self.padre = padre

    def getPos(self):
        return self.posicion

    def getPadre(self):
        return self.padre


class Busqueda:
    def __init__(self, laberinto, tipo):
        self.laberinto = laberinto
        self.frontera = Pila(laberinto.getSize()) if tipo == 0 else Cola(
            laberinto.getSize())
        self.explorados = Pila(laberinto.getSize())
        self.estado_inicial = laberinto.getInicio()
        self.estado_objetivo = laberinto.getObjetivo()

    def buscarSolucion(self):
        self.frontera.agregar(Nodo(self.estado_inicial))

        while not self.frontera.vacia():
            nodo = self.frontera.remover()
            posicion = nodo.getPos()

            self.laberinto.mostrar(posicion)

            if posicion == self.estado_objetivo:
                self.laberinto.mostrar_solucion(nodo)

                print("Objetivo encontrado en la posición:", posicion)
                print(f"Nodos explorados:", len(self.explorados))
                return nodo

            self.explorados.agregar(nodo)
            vecinos = self.laberinto.getVecinos(posicion)

            for vecino in vecinos:
                if not self.frontera.contiene(vecino) and not self.explorados.contiene(vecino):
                    padre = Nodo(posicion, nodo.getPadre())
                    nodo_vecino = Nodo(vecino, padre)
                    self.frontera.agregar(nodo_vecino)

        print("No existe solución.")
        return
