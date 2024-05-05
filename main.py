from Laberinto import Laberinto
from Busqueda import Busqueda


laberinto = Laberinto("maze2.txt")

# 0 - Pila
# 1 - Cola
b = Busqueda(laberinto, tipo=1)
b.buscarSolucion()
