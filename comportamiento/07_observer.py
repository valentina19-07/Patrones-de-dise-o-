'''
PATRÓN: OBSERVER (Observador)
TIPO: Comportamiento
AUTOR: Valentina

¿QUÉ HACE EL PATRÓN?
    Define una dependencia uno-a-muchos: cuando un objeto (el sujeto) cambia
    de estado, todos sus observadores suscritos son notificados
    automáticamente.

PROBLEMA QUE RESUELVE
    Un canal de videos publica contenido nuevo y varias partes quieren
    enterarse (usuarios, servicio de correo...). Si los suscriptores
    preguntaran constantemente si hay videos nuevos, se desperdiciaría
    trabajo; si el canal los llamara directamente, quedaría acoplado a cada
    uno.

¿POR QUÉ OBSERVER ES ADECUADO?
    - El canal solo conoce la interfaz Observador, no las clases concretas.
    - Se puede suscribir o cancelar en tiempo de ejecución.
    - Cuando hay un video nuevo, todos se enteran sin que el canal sepa
      quiénes son.

CÓMO EJECUTAR:  python comportamiento/07_observer.py
'''

from abc import ABC, abstractmethod


# ---------------------------------------------------------------
# OBSERVADOR (interfaz)
# ---------------------------------------------------------------
class Observador(ABC):
    @abstractmethod
    def actualizar(self, canal, titulo):
        pass


# ---------------------------------------------------------------
# SUJETO: mantiene la lista de observadores y los notifica
# ---------------------------------------------------------------
class CanalVideos:
    def __init__(self, nombre):
        self.nombre = nombre
        self._suscriptores = []

    def suscribir(self, observador):
        if observador not in self._suscriptores:
            self._suscriptores.append(observador)

    def desuscribir(self, observador):
        if observador in self._suscriptores:
            self._suscriptores.remove(observador)

    def publicar_video(self, titulo):
        print(f'>>> {self.nombre} publicó el video: {titulo}')
        self._notificar(titulo)

    def _notificar(self, titulo):
        # Se recorre una copia por si alguien se desuscribe durante la notificación
        for observador in list(self._suscriptores):
            observador.actualizar(self.nombre, titulo)


# ---------------------------------------------------------------
# OBSERVADORES CONCRETOS
# ---------------------------------------------------------------
class Usuario(Observador):
    def __init__(self, nombre):
        self.nombre = nombre

    def actualizar(self, canal, titulo):
        print(f'    {self.nombre} recibió la notificación: {canal} subió {titulo}')


class ServicioCorreo(Observador):
    def actualizar(self, canal, titulo):
        print(f'    [Correo] Enviando resumen del nuevo video de {canal}: {titulo}')


# ---------------------------------------------------------------
# PRUEBA DEL PATRÓN
# ---------------------------------------------------------------
if __name__ == '__main__':
    canal = CanalVideos('Arquitectura Fácil')
    ana = Usuario('Ana')
    luis = Usuario('Luis')
    correo = ServicioCorreo()

    canal.suscribir(ana)
    canal.suscribir(luis)
    canal.suscribir(correo)

    canal.publicar_video('Patrón Observer en 10 minutos')

    print('--- Luis cancela su suscripción ---')
    canal.desuscribir(luis)

    canal.publicar_video('Patrón Strategy explicado')
