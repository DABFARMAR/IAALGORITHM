import os
from time import sleep


class Laberinto:

    def __init__(self, archivo):
        self.inicio = None
        self.objetivo = None

        with open(archivo) as contenido:
            contenido = contenido.readlines()

        self.altura = len(contenido)
        self.ancho = len(contenido[0]) - 1
        self.laberinto = [None]*self.altura

        for idx, line in enumerate(contenido):
            if "A" in line:
                self.inicio = (idx, line.index("A"))

            if "B" in line:
                self.objetivo = (idx, line.index("B"))

            self.laberinto[idx] = list(line.replace("\n", ""))

        # print(self.inicio, self.objetivo)

    def getInicio(self):
        return self.inicio

    def getObjetivo(self):
        return self.objetivo

    def getSize(self):
        return self.altura * self.ancho

    def getVecinos(self, posicion):
        rtn = [(posicion[0], posicion[1]-1),
               (posicion[0], posicion[1]+1),
               (posicion[0]+1, posicion[1]),
               (posicion[0]-1, posicion[1])]

        return list(
            filter(lambda e: -1 not in e and
                   self.altura != e[0] and
                   self.ancho != e[1] and
                   self.laberinto[e[0]][e[1]] != "#", rtn))

    def mostrar(self, posicion=None):
        os.system('cls' if os.name == 'nt' else 'clear')

        if posicion != None:
            caracter = "😀" if posicion == self.objetivo else "█"
            self.laberinto[posicion[0]][posicion[1]] = caracter

        for line in self.laberinto:
            print("".join(line), end="\n")

        sleep(0.1)
