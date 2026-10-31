'''
PATRÓN: STATE (Estado)
TIPO: Comportamiento
AUTOR: Valentina

¿QUÉ HACE EL PATRÓN?
    Permite que un objeto cambie su comportamiento cuando cambia su estado
    interno. Parece que el objeto cambiara de clase.

PROBLEMA QUE RESUELVE
    Un pedido de una tienda en línea pasa por varios estados (Pendiente,
    Pagado, Enviado, Entregado, Cancelado) y cada acción (pagar, enviar,
    entregar, cancelar) solo es válida en ciertos estados. Con if/elif sobre
    una variable de texto, la clase Pedido se llena de condiciones repetidas
    y es fácil permitir transiciones inválidas.

¿POR QUÉ STATE ES ADECUADO?
    - Cada estado es una clase que define qué acciones permite y a qué
      estado se pasa.
    - Las transiciones inválidas se rechazan en un solo lugar (clase base).
    - Agregar un estado nuevo no obliga a modificar los existentes.

CÓMO EJECUTAR:  python comportamiento/10_state.py
'''

from abc import ABC


# ---------------------------------------------------------------
# ESTADO (clase base): por defecto toda acción es inválida
# ---------------------------------------------------------------
class EstadoPedido(ABC):
    nombre = ''

    def pagar(self, pedido):
        self._invalida('pagar')

    def enviar(self, pedido):
        self._invalida('enviar')

    def entregar(self, pedido):
        self._invalida('entregar')

    def cancelar(self, pedido):
        self._invalida('cancelar')

    def _invalida(self, accion):
        print(f'  [X] No se puede {accion} un pedido en estado {self.nombre}.')


# ---------------------------------------------------------------
# ESTADOS CONCRETOS: solo sobrescriben las acciones que sí permiten
# ---------------------------------------------------------------
class Pendiente(EstadoPedido):
    nombre = 'Pendiente'

    def pagar(self, pedido):
        pedido.cambiar_estado(Pagado())

    def cancelar(self, pedido):
        pedido.cambiar_estado(Cancelado())


class Pagado(EstadoPedido):
    nombre = 'Pagado'

    def enviar(self, pedido):
        pedido.cambiar_estado(Enviado())

    def cancelar(self, pedido):
        pedido.cambiar_estado(Cancelado())


class Enviado(EstadoPedido):
    nombre = 'Enviado'

    def entregar(self, pedido):
        pedido.cambiar_estado(Entregado())


class Entregado(EstadoPedido):
    nombre = 'Entregado'  # estado final: ninguna acción permitida


class Cancelado(EstadoPedido):
    nombre = 'Cancelado'  # estado final: ninguna acción permitida


# ---------------------------------------------------------------
# CONTEXTO: delega cada acción en su estado actual
# ---------------------------------------------------------------
class Pedido:
    def __init__(self, numero):
        self.numero = numero
        self._estado = Pendiente()

    def cambiar_estado(self, nuevo_estado):
        print(f'  [OK] Pedido {self.numero}: {self._estado.nombre} -> {nuevo_estado.nombre}')
        self._estado = nuevo_estado

    def pagar(self):
        self._estado.pagar(self)

    def enviar(self):
        self._estado.enviar(self)

    def entregar(self):
        self._estado.entregar(self)

    def cancelar(self):
        self._estado.cancelar(self)


# ---------------------------------------------------------------
# PRUEBA DEL PATRÓN
# ---------------------------------------------------------------
if __name__ == '__main__':
    print('--- Pedido 1: flujo normal ---')
    pedido_1 = Pedido(1001)
    pedido_1.enviar()      # inválido: aún no está pagado
    pedido_1.pagar()
    pedido_1.enviar()
    pedido_1.entregar()
    pedido_1.cancelar()    # inválido: ya fue entregado

    print('--- Pedido 2: cancelado antes de pagar ---')
    pedido_2 = Pedido(1002)
    pedido_2.cancelar()
    pedido_2.pagar()       # inválido: está cancelado
