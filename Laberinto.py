import os
from time import sleep
import sys


class Laberinto:
    def __init__(self, archivo):
        self.inicio = None
        self.objetivo = None

        with open(archivo) as contenido:
            contenido = contenido.readlines()

        self.alto = len(contenido)
        self.ancho = len(contenido[0]) - 1
        self.laberinto = [None]*self.alto

        for idx, line in enumerate(contenido):
            if "A" in line:
                self.inicio = (idx, line.index("A"))

            if "B" in line:
                self.objetivo = (idx, line.index("B"))

            self.laberinto[idx] = list(line.replace("\n", ""))

        if not self.inicio or not self.objetivo:
            print("El laberinto no tiene un punto de partida o un objetivo.")
            sys.exit(0)

    def getInicio(self):
        return self.inicio

    def getObjetivo(self):
        return self.objetivo

    def getSize(self):
        return self.alto * self.ancho

    def getVecinos(self, posicion):
        rtn = [(posicion[0]-1, posicion[1]),
               (posicion[0]+1, posicion[1]),
               (posicion[0], posicion[1]-1),
               (posicion[0], posicion[1]+1)]

        return list(
            filter(lambda e: -1 not in e and
                   e[0] < self.alto and
                   e[1] < self.ancho and
                   self.laberinto[e[0]][e[1]] != "#", rtn))

    def mostrarLaberinto(self):
        os.system('cls' if os.name == 'nt' else 'clear')

        for line in self.laberinto:
            print("".join(line).replace("#", "█"), end="\n")

    def mostrarPosicion(self, posicion=None):
        if posicion != None and posicion != self.inicio:
            caracter = "\033[32;1mB\033[0m" if posicion == self.objetivo else "\033[38;5;208m█\033[0m"
            self.laberinto[posicion[0]][posicion[1]] = caracter

        self.mostrarLaberinto()
        sleep(0.05)

    def mostrarSolucion(self, nodo):
        padre = nodo.getPadre()
        posicion = nodo.getPos()

        if padre == None:
            self.mostrarLaberinto()
            return

        if nodo.getPos() != self.objetivo:
            self.laberinto[posicion[0]][posicion[1]] = "\033[32;1m█\033[0m"

        self.mostrarSolucion(padre)
