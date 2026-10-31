'''
PATRÓN: COMMAND (Comando)
TIPO: Comportamiento
AUTOR: Valentina

¿QUÉ HACE EL PATRÓN?
    Convierte una acción en un objeto. Así se puede guardar, encolar,
    registrar, deshacer y rehacer, y se desacopla quien pide la acción de
    quien la ejecuta.

PROBLEMA QUE RESUELVE
    Un editor de texto necesita las funciones Deshacer y Rehacer. Si las
    acciones (escribir, borrar) se ejecutan directamente sobre el texto, no
    queda registro de qué se hizo ni cómo revertirlo.

¿POR QUÉ COMMAND ES ADECUADO?
    - Cada acción es un objeto que sabe ejecutarse Y deshacerse.
    - El historial guarda los comandos y permite deshacer/rehacer en cadena.
    - Agregar una acción nueva (por ejemplo Pegar) no cambia el historial.

CÓMO EJECUTAR:  python comportamiento/09_command.py
'''

from abc import ABC, abstractmethod


# ---------------------------------------------------------------
# COMANDO (interfaz)
# ---------------------------------------------------------------
class Comando(ABC):
    @abstractmethod
    def ejecutar(self):
        pass

    @abstractmethod
    def deshacer(self):
        pass


# ---------------------------------------------------------------
# RECEPTOR: el objeto que realmente hace el trabajo
# ---------------------------------------------------------------
class Editor:
    def __init__(self):
        self.texto = ''


# ---------------------------------------------------------------
# COMANDOS CONCRETOS
# ---------------------------------------------------------------
class ComandoEscribir(Comando):
    def __init__(self, editor, texto):
        self._editor = editor
        self._texto = texto

    def ejecutar(self):
        self._editor.texto += self._texto

    def deshacer(self):
        largo_final = len(self._editor.texto) - len(self._texto)
        self._editor.texto = self._editor.texto[:largo_final]


class ComandoBorrar(Comando):
    def __init__(self, editor, cantidad):
        self._editor = editor
        self._cantidad = cantidad
        self._borrado = ''  # se guarda lo borrado para poder deshacer

    def ejecutar(self):
        texto = self._editor.texto
        corte = max(len(texto) - self._cantidad, 0)
        self._borrado = texto[corte:]
        self._editor.texto = texto[:corte]

    def deshacer(self):
        self._editor.texto += self._borrado


# ---------------------------------------------------------------
# INVOCADOR: guarda el historial y controla deshacer/rehacer
# ---------------------------------------------------------------
class HistorialComandos:
    def __init__(self):
        self._hechos = []
        self._deshechos = []

    def ejecutar(self, comando):
        comando.ejecutar()
        self._hechos.append(comando)
        self._deshechos.clear()  # una acción nueva invalida el rehacer

    def deshacer(self):
        if not self._hechos:
            print('No hay nada que deshacer.')
            return
        comando = self._hechos.pop()
        comando.deshacer()
        self._deshechos.append(comando)

    def rehacer(self):
        if not self._deshechos:
            print('No hay nada que rehacer.')
            return
        comando = self._deshechos.pop()
        comando.ejecutar()
        self._hechos.append(comando)


# ---------------------------------------------------------------
# PRUEBA DEL PATRÓN
# ---------------------------------------------------------------
if __name__ == '__main__':
    editor = Editor()
    historial = HistorialComandos()

    def mostrar(accion):
        print(f'{accion:<26} -> {editor.texto!r}')

    historial.ejecutar(ComandoEscribir(editor, 'Hola'))
    mostrar('Escribir Hola')

    historial.ejecutar(ComandoEscribir(editor, ' mundo'))
    mostrar('Escribir  mundo')

    historial.ejecutar(ComandoBorrar(editor, 3))
    mostrar('Borrar 3 caracteres')

    historial.deshacer()
    mostrar('Deshacer (borrado)')

    historial.deshacer()
    mostrar('Deshacer (escritura)')

    historial.rehacer()
    mostrar('Rehacer')
