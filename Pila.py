# arreglo: array
# largo: int
# longitud: int
class Pila:
    def __init__(self, largo):
        self.arreglo = [None] * largo
        self.largo = largo
        self.longitud = 0

    # __len__: None -> int
    # Al aplicar el método len() de python a un objeto Pila
    # se ejecuta este método
    def __len__(self):
        return self.longitud

    # vacia: None -> boolean
    # Retorna True si la cola esta vacía
    # si no esta vacía retorna False
    def vacia(self):
        return True if self.longitud == 0 else False

    # agregar: valor -> None
    # Agrega 'valor' a la pila
    # Si la pila esta llena retorna False
    def agregar(self, valor):
        if self.longitud < self.largo:
            self.arreglo[self.longitud] = valor
            self.longitud += 1
        else:
            print("Pila llena")
            return False

    # remover: None -> valor
    # Quita un elemento de la pila y lo retorna
    # Si la pila esta vacía retorna False
    def remover(self):
        if not self.vacia():
            rm = self.arreglo[self.longitud - 1]
            self.arreglo[self.longitud - 1] = None
            self.longitud -= 1
            return rm
        else:
            print("Pila vacía")
            return False

    # __str__: None -> str
    # Cuando se aplica la función print() de python a un objeto de tipo Pila
    # este método devuelve un string con todos los valores guardados en la pila
    def __str__(self):
        rtn = ""
        for elem in self.arreglo:
            rtn += f"[{elem}]"

        return rtn

    def contiene(self, elemento):
        for elem in self.arreglo:
            if elem != None and elem.getPos() == elemento:
                return True

        return False
