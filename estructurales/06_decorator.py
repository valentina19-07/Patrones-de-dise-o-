'''
PATRÓN: DECORATOR (Decorador)
TIPO: Estructural
AUTOR: Valentina

¿QUÉ HACE EL PATRÓN?
    Añade responsabilidades a un objeto de forma dinámica, envolviéndolo en
    otros objetos que comparten su misma interfaz. Es una alternativa flexible
    a la herencia.

PROBLEMA QUE RESUELVE
    Una cafetería vende bebidas con extras opcionales (leche, chocolate,
    crema). Con herencia habría que crear una subclase por cada combinación
    (EspressoConLeche, EspressoConLecheYChocolate...), lo que genera una
    explosión de clases imposible de mantener.

¿POR QUÉ DECORATOR ES ADECUADO?
    - Cada extra es una clase pequeña que envuelve a la bebida.
    - Las combinaciones se arman en tiempo de ejecución, en cualquier orden y
      cantidad (incluso doble chocolate).
    - Agregar un extra nuevo no obliga a tocar las clases existentes.

CÓMO EJECUTAR:  python estructurales/06_decorator.py
'''

from abc import ABC, abstractmethod


# ---------------------------------------------------------------
# COMPONENTE: interfaz común para bebidas y decoradores
# ---------------------------------------------------------------
class Bebida(ABC):
    @abstractmethod
    def descripcion(self):
        pass

    @abstractmethod
    def costo(self):
        pass


# ---------------------------------------------------------------
# COMPONENTE CONCRETO: la bebida base
# ---------------------------------------------------------------
class Espresso(Bebida):
    def descripcion(self):
        return 'Espresso'

    def costo(self):
        return 4000


# ---------------------------------------------------------------
# DECORADOR BASE: envuelve una bebida y delega en ella
# ---------------------------------------------------------------
class DecoradorBebida(Bebida):
    def __init__(self, bebida):
        self._bebida = bebida

    def descripcion(self):
        return self._bebida.descripcion()

    def costo(self):
        return self._bebida.costo()


# ---------------------------------------------------------------
# DECORADORES CONCRETOS: cada uno añade descripción y costo
# ---------------------------------------------------------------
class Leche(DecoradorBebida):
    def descripcion(self):
        return f'{self._bebida.descripcion()} + Leche'

    def costo(self):
        return self._bebida.costo() + 1500


class Chocolate(DecoradorBebida):
    def descripcion(self):
        return f'{self._bebida.descripcion()} + Chocolate'

    def costo(self):
        return self._bebida.costo() + 2000


class Crema(DecoradorBebida):
    def descripcion(self):
        return f'{self._bebida.descripcion()} + Crema'

    def costo(self):
        return self._bebida.costo() + 1000


# ---------------------------------------------------------------
# PRUEBA DEL PATRÓN
# ---------------------------------------------------------------
def mostrar(bebida):
    print(f'{bebida.descripcion()} -> ${bebida.costo():,.0f}')


if __name__ == '__main__':
    pedido_1 = Espresso()
    pedido_2 = Chocolate(Leche(Espresso()))
    pedido_3 = Crema(Chocolate(Chocolate(Espresso())))  # doble chocolate

    mostrar(pedido_1)
    mostrar(pedido_2)
    mostrar(pedido_3)
