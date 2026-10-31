'''
PATRÓN: SINGLETON
TIPO: Creacional
AUTOR: Juan

¿QUÉ HACE EL PATRÓN?
    Garantiza que una clase tenga UNA sola instancia en toda la aplicación y
    ofrece un punto de acceso global a ella.

PROBLEMA QUE RESUELVE
    La configuración de la aplicación (idioma, moneda, modo debug) debe ser la
    misma para todos los módulos. Si cada módulo crea su propia configuración,
    los cambios de uno no los ve el otro y se generan inconsistencias.

¿POR QUÉ SINGLETON ES ADECUADO?
    - Una única instancia compartida = una única fuente de verdad.
    - Evita duplicar recursos (la configuración se carga una sola vez).
    - Aquí se usa un lock para que también sea seguro con varios hilos.

CÓMO EJECUTAR:  python creacionales/03_singleton.py
'''

import threading


class ConfiguracionApp:
    _instancia = None
    _lock = threading.Lock()

    def __new__(cls):
        # Doble verificación: evita bloquear el lock cuando la instancia ya existe
        if cls._instancia is None:
            with cls._lock:
                if cls._instancia is None:
                    instancia = super().__new__(cls)
                    instancia._inicializada = False
                    cls._instancia = instancia
        return cls._instancia

    def __init__(self):
        # __init__ se ejecuta en cada llamada a ConfiguracionApp();
        # esta bandera evita reiniciar los valores ya guardados
        if self._inicializada:
            return
        self._inicializada = True
        self._valores = {
            'idioma': 'es',
            'moneda': 'COP',
            'modo_debug': False,
        }

    def obtener(self, clave, por_defecto=None):
        return self._valores.get(clave, por_defecto)

    def establecer(self, clave, valor):
        self._valores[clave] = valor


# ---------------------------------------------------------------
# PRUEBA DEL PATRÓN
# ---------------------------------------------------------------
if __name__ == '__main__':
    modulo_a = ConfiguracionApp()
    modulo_b = ConfiguracionApp()

    print(f'¿Son la misma instancia? {modulo_a is modulo_b}')

    modulo_a.establecer('idioma', 'en')
    print(f'El módulo B ve el idioma: {modulo_b.obtener("idioma")}')

    # Prueba con 10 hilos creando la configuración al mismo tiempo
    instancias = []

    def crear():
        instancias.append(ConfiguracionApp())

    hilos = [threading.Thread(target=crear) for _ in range(10)]
    for hilo in hilos:
        hilo.start()
    for hilo in hilos:
        hilo.join()

    print(f'Instancias distintas creadas por 10 hilos: {len({id(i) for i in instancias})}')
