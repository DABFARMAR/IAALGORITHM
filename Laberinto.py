
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

    def getVecinos(self, posicion):
        rtn = [(posicion[0], posicion[1]-1),
               (posicion[0], posicion[1]+1),
               (posicion[0]+1, posicion[1]),
               (posicion[0]-1, posicion[1])]

        return list(
            filter(lambda e: -1 not in e and
                   self.altura not in e and
                   self.ancho not in e and
                   self.laberinto[e[0]][e[1]] != "#", rtn))
