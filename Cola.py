
# largo: int
# arreglo: array
# cabeza: int
# contador: int
# longitud: int
class Cola:

    def __init__(self, largo):
        self.largo = largo
        self.arreglo = [None] * largo
        self.cabeza = 0
        self.contador = 0
        self.longitud = 0

    # __len__: None -> int
    # Al aplicar el método len() de python a un objeto Cola
    # se ejecuta este método
    def __len__(self):
        return self.longitud

    # vacía: None -> boolean
    # Retorna True si la cola esta vacía
    # si no esta vacía retorna False
    def vacia(self):
        return True if self.longitud == 0 else False

    # agregar: valor -> None
    # Agrega 'valor' a la cola, la cola funciona de forma circular
    # Si la cola esta llena retorna False
    def agregar(self, valor):
        if self.longitud < self.largo:
            if self.contador == self.largo:
                self.contador *= 0

            self.arreglo[self.contador] = valor
            self.contador += 1
            self.longitud += 1
        else:
            print("Cola llena")
            return

    # remover: None -> valor
    # Quita un elemento de la cola y lo retorna
    # Si la cola esta vacía retorna False
    def remover(self):
        if not self.vacia():
            rm = self.arreglo[self.cabeza]
            self.arreglo[self.cabeza] = None
            self.cabeza += 1
            self.longitud -= 1
            return rm
        else:
            print("Cola vacía")
            return

    # __str__: None -> str
    # Cuando se aplica la función print() de python a un objeto de tipo Cola
    # este método devuelve un string con todos los valores guardados en la cola
    def __str__(self):
        rtn = ""
        for elem in self.arreglo:
            rtn += f"[{elem}]"

        return rtn

    # contiene: elemento -> boolean
    def contiene(self, elemento):
        for elem in self.arreglo:
            if elem != None and elem.getPos() == elemento:
                return True

        return False
