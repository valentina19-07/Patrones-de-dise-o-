'''
PATRÓN: STRATEGY (Estrategia)
TIPO: Comportamiento
AUTOR: Valentina

¿QUÉ HACE EL PATRÓN?
    Define una familia de algoritmos, encapsula cada uno en su propia clase
    y los hace intercambiables. El cliente puede cambiar de algoritmo en
    tiempo de ejecución.

PROBLEMA QUE RESUELVE
    Un carrito de compras debe calcular el total aplicando distintos
    descuentos (porcentaje, valor fijo, Black Friday). Con if/elif dentro del
    carrito, cada descuento nuevo obliga a modificar esa clase y el código se
    vuelve largo y frágil.

¿POR QUÉ STRATEGY ES ADECUADO?
    - Cada descuento vive en su propia clase, fácil de probar.
    - El carrito delega el cálculo y no sabe cuál descuento se usa.
    - Se puede cambiar el descuento mientras el programa corre.
    - Un descuento nuevo es una clase nueva, sin tocar el carrito.

CÓMO EJECUTAR:  python comportamiento/08_strategy.py
'''

from abc import ABC, abstractmethod


# ---------------------------------------------------------------
# ESTRATEGIA (interfaz común)
# ---------------------------------------------------------------
class EstrategiaDescuento(ABC):
    @abstractmethod
    def aplicar(self, subtotal):
        pass

    @abstractmethod
    def nombre(self):
        pass


# ---------------------------------------------------------------
# ESTRATEGIAS CONCRETAS
# ---------------------------------------------------------------
class SinDescuento(EstrategiaDescuento):
    def aplicar(self, subtotal):
        return subtotal

    def nombre(self):
        return 'Sin descuento'


class DescuentoPorcentaje(EstrategiaDescuento):
    def __init__(self, porcentaje):
        self._porcentaje = porcentaje

    def aplicar(self, subtotal):
        return subtotal * (1 - self._porcentaje / 100)

    def nombre(self):
        return f'Descuento del {self._porcentaje}%'


class DescuentoFijo(EstrategiaDescuento):
    def __init__(self, valor):
        self._valor = valor

    def aplicar(self, subtotal):
        return max(subtotal - self._valor, 0)  # el total nunca es negativo

    def nombre(self):
        return f'Descuento fijo de ${self._valor:,.0f}'


class DescuentoBlackFriday(EstrategiaDescuento):
    def aplicar(self, subtotal):
        return subtotal * 0.70

    def nombre(self):
        return 'Black Friday (30%)'


# ---------------------------------------------------------------
# CONTEXTO: usa una estrategia sin conocer su implementación
# ---------------------------------------------------------------
class CarritoCompras:
    def __init__(self, estrategia=None):
        self._productos = []
        self._estrategia = estrategia or SinDescuento()

    def agregar(self, nombre, precio):
        self._productos.append((nombre, precio))

    def cambiar_estrategia(self, estrategia):
        self._estrategia = estrategia

    def subtotal(self):
        return sum(precio for _, precio in self._productos)

    def total(self):
        return self._estrategia.aplicar(self.subtotal())

    def resumen(self):
        print(f'Subtotal: ${self.subtotal():,.0f} | {self._estrategia.nombre()} | '
              f'Total a pagar: ${self.total():,.0f}')


# ---------------------------------------------------------------
# PRUEBA DEL PATRÓN
# ---------------------------------------------------------------
if __name__ == '__main__':
    carrito = CarritoCompras()
    carrito.agregar('Camiseta', 50000)
    carrito.agregar('Zapatos', 180000)
    carrito.agregar('Gorra', 30000)

    carrito.resumen()

    carrito.cambiar_estrategia(DescuentoPorcentaje(10))
    carrito.resumen()

    carrito.cambiar_estrategia(DescuentoFijo(20000))
    carrito.resumen()

    carrito.cambiar_estrategia(DescuentoBlackFriday())
    carrito.resumen()
