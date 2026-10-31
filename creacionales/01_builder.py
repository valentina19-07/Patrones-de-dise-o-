'''
PATRÓN: BUILDER (Constructor)
TIPO: Creacional
AUTOR: Juan

¿QUÉ HACE EL PATRÓN?
    Separa la construcción de un objeto complejo de su representación final.
    Permite crear el objeto paso a paso, y que un mismo proceso de construcción
    genere distintas configuraciones.

PROBLEMA QUE RESUELVE
    Un Computador tiene muchas piezas (procesador, RAM, disco, gráfica, wifi...).
    Con un constructor de 6 parámetros el código es ilegible
    (¿qué significa Computador('i7', 16, 512, None, True, False)?) y muchas
    piezas son opcionales.

¿POR QUÉ BUILDER ES ADECUADO?
    - Cada paso tiene un nombre claro (con_ram, con_almacenamiento...).
    - Lo opcional simplemente no se invoca.
    - El Director guarda «recetas» reutilizables (PC de oficina, PC gamer).
    - El Builder valida que el objeto esté completo antes de entregarlo.

CÓMO EJECUTAR:  python creacionales/01_builder.py
'''


def _si_no(valor):
    return 'Sí' if valor else 'No'


# ---------------------------------------------------------------
# PRODUCTO: el objeto complejo que queremos construir
# ---------------------------------------------------------------
class Computador:
    def __init__(self):
        self.procesador = None
        self.ram_gb = 0
        self.almacenamiento_gb = 0
        self.tarjeta_grafica = None
        self.tiene_wifi = False
        self.refrigeracion_liquida = False

    def __str__(self):
        grafica = self.tarjeta_grafica or 'Integrada'
        return (
            f'CPU: {self.procesador} | RAM: {self.ram_gb} GB | '
            f'Disco: {self.almacenamiento_gb} GB | Gráfica: {grafica} | '
            f'WiFi: {_si_no(self.tiene_wifi)} | '
            f'Refrigeración líquida: {_si_no(self.refrigeracion_liquida)}'
        )


# ---------------------------------------------------------------
# BUILDER: ofrece los pasos de construcción
# ---------------------------------------------------------------
class ComputadorBuilder:
    def __init__(self):
        self._computador = Computador()

    # Cada paso devuelve self para poder encadenar llamadas (interfaz fluida)
    def con_procesador(self, procesador):
        self._computador.procesador = procesador
        return self

    def con_ram(self, gb):
        self._computador.ram_gb = gb
        return self

    def con_almacenamiento(self, gb):
        self._computador.almacenamiento_gb = gb
        return self

    def con_tarjeta_grafica(self, modelo):
        self._computador.tarjeta_grafica = modelo
        return self

    def con_wifi(self):
        self._computador.tiene_wifi = True
        return self

    def con_refrigeracion_liquida(self):
        self._computador.refrigeracion_liquida = True
        return self

    def construir(self):
        # Validación: no se entrega un objeto incompleto
        if not self._computador.procesador:
            raise ValueError('Un computador necesita procesador.')
        if self._computador.ram_gb <= 0:
            raise ValueError('Un computador necesita memoria RAM.')
        resultado = self._computador
        self._computador = Computador()  # se reinicia para reutilizar el builder
        return resultado


# ---------------------------------------------------------------
# DIRECTOR: conoce recetas predefinidas de construcción
# ---------------------------------------------------------------
class DirectorComputadores:
    def __init__(self, builder):
        self._builder = builder

    def construir_pc_oficina(self):
        return (self._builder
                .con_procesador('Intel Core i3')
                .con_ram(8)
                .con_almacenamiento(256)
                .con_wifi()
                .construir())

    def construir_pc_gamer(self):
        return (self._builder
                .con_procesador('AMD Ryzen 9')
                .con_ram(32)
                .con_almacenamiento(2000)
                .con_tarjeta_grafica('NVIDIA RTX 4080')
                .con_wifi()
                .con_refrigeracion_liquida()
                .construir())


# ---------------------------------------------------------------
# PRUEBA DEL PATRÓN
# ---------------------------------------------------------------
if __name__ == '__main__':
    builder = ComputadorBuilder()
    director = DirectorComputadores(builder)

    print('--- PC de oficina (receta del Director) ---')
    print(director.construir_pc_oficina())

    print('--- PC gamer (receta del Director) ---')
    print(director.construir_pc_gamer())

    print('--- PC personalizado (sin Director, paso a paso) ---')
    pc_personalizado = (ComputadorBuilder()
                        .con_procesador('AMD Ryzen 5')
                        .con_ram(16)
                        .con_almacenamiento(1000)
                        .con_tarjeta_grafica('NVIDIA RTX 4060')
                        .construir())
    print(pc_personalizado)

    print('--- Validación: intentar construir sin procesador ---')
    try:
        ComputadorBuilder().con_ram(8).construir()
    except ValueError as error:
        print(f'Error esperado: {error}')
