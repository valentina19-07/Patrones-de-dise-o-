'''
PATRÓN: FACTORY METHOD (Método de Fábrica)
TIPO: Creacional
AUTOR: Juan

¿QUÉ HACE EL PATRÓN?
    Define un método en una clase base para crear objetos, pero deja que las
    subclases decidan QUÉ clase concreta se instancia.

PROBLEMA QUE RESUELVE
    Un sistema envía notificaciones por Email, SMS y Push. Si el código cliente
    hace if/elif para decidir cuál clase crear, cada canal nuevo (por ejemplo
    WhatsApp) obliga a modificar ese código ya probado.

¿POR QUÉ FACTORY METHOD ES ADECUADO?
    - El código cliente solo depende de la abstracción Notificacion.
    - Agregar un canal = crear 2 clases nuevas, sin tocar las existentes
      (principio Abierto/Cerrado).
    - La lógica de creación queda aislada en un único lugar por canal.

CÓMO EJECUTAR:  python creacionales/02_factory_method.py
'''

from abc import ABC, abstractmethod


# ---------------------------------------------------------------
# PRODUCTO (interfaz común) y productos concretos
# ---------------------------------------------------------------
class Notificacion(ABC):
    @abstractmethod
    def enviar(self, destinatario, mensaje):
        pass


class NotificacionEmail(Notificacion):
    def enviar(self, destinatario, mensaje):
        return f'[EMAIL] Para {destinatario}: {mensaje}'


class NotificacionSMS(Notificacion):
    def enviar(self, destinatario, mensaje):
        return f'[SMS] Para {destinatario}: {mensaje[:40]}'


class NotificacionPush(Notificacion):
    def enviar(self, destinatario, mensaje):
        return f'[PUSH] Al dispositivo {destinatario}: {mensaje}'


# ---------------------------------------------------------------
# CREADOR (clase base) con el Factory Method
# ---------------------------------------------------------------
class Notificador(ABC):
    @abstractmethod
    def crear_notificacion(self):
        '''FACTORY METHOD: cada subclase decide qué producto crea.'''
        pass

    def notificar(self, destinatario, mensaje):
        # La lógica común usa el producto sin saber cuál clase concreta es
        notificacion = self.crear_notificacion()
        resultado = notificacion.enviar(destinatario, mensaje)
        print(resultado)
        return resultado


# ---------------------------------------------------------------
# CREADORES CONCRETOS
# ---------------------------------------------------------------
class NotificadorEmail(Notificador):
    def crear_notificacion(self):
        return NotificacionEmail()


class NotificadorSMS(Notificador):
    def crear_notificacion(self):
        return NotificacionSMS()


class NotificadorPush(Notificador):
    def crear_notificacion(self):
        return NotificacionPush()


# ---------------------------------------------------------------
# PRUEBA DEL PATRÓN
# ---------------------------------------------------------------
if __name__ == '__main__':
    canales = [
        (NotificadorEmail(), 'juan@correo.com'),
        (NotificadorSMS(), '+57 300 000 0000'),
        (NotificadorPush(), 'dispositivo-123'),
    ]

    # El cliente trata a todos los notificadores de forma uniforme
    for notificador, destino in canales:
        notificador.notificar(destino, 'Tu pedido #1024 fue enviado')
