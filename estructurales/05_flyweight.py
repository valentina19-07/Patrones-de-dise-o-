'''
PATRÓN: FLYWEIGHT (Peso Ligero)
TIPO: Estructural
AUTOR: Juan

¿QUÉ HACE EL PATRÓN?
    Reduce el consumo de memoria compartiendo las partes comunes e inmutables
    (estado INTRÍNSECO) entre muchos objetos, y guardando aparte lo que es
    único de cada uno (estado EXTRÍNSECO).

PROBLEMA QUE RESUELVE
    Un videojuego dibuja un bosque de 10.000 árboles. Si cada árbol guarda su
    propio nombre, color y textura, se repiten los mismos datos miles de veces
    y se desperdicia memoria (solo hay 3 especies distintas).

¿POR QUÉ FLYWEIGHT ES ADECUADO?
    - Hay muchísimos objetos con datos repetidos (especie, color, textura).
    - Esos datos repetidos no cambian, así que se pueden compartir.
    - Cada árbol solo guarda lo propio: su posición (x, y).
    - Una fábrica garantiza que no se creen tipos duplicados.

CÓMO EJECUTAR:  python estructurales/05_flyweight.py
'''

import random


# ---------------------------------------------------------------
# FLYWEIGHT: estado INTRÍNSECO (compartido e inmutable)
# ---------------------------------------------------------------
class TipoArbol:
    def __init__(self, nombre, color, textura):
        self.nombre = nombre
        self.color = color
        self.textura = textura

    def dibujar(self, x, y):
        # x e y (estado extrínseco) llegan por parámetro, no se guardan aquí
        return f'{self.nombre} ({self.color}, {self.textura}) dibujado en ({x}, {y})'


# ---------------------------------------------------------------
# FÁBRICA DE FLYWEIGHTS: reutiliza los tipos ya creados
# ---------------------------------------------------------------
class FabricaTipoArbol:
    _tipos = {}

    @classmethod
    def obtener_tipo(cls, nombre, color, textura):
        clave = (nombre, color, textura)
        if clave not in cls._tipos:
            cls._tipos[clave] = TipoArbol(nombre, color, textura)
        return cls._tipos[clave]

    @classmethod
    def total_tipos(cls):
        return len(cls._tipos)


# ---------------------------------------------------------------
# CONTEXTO: estado EXTRÍNSECO (único de cada árbol) + referencia al flyweight
# ---------------------------------------------------------------
class Arbol:
    def __init__(self, x, y, tipo):
        self.x = x
        self.y = y
        self.tipo = tipo

    def dibujar(self):
        return self.tipo.dibujar(self.x, self.y)


class Bosque:
    def __init__(self):
        self.arboles = []

    def plantar(self, x, y, nombre, color, textura):
        tipo = FabricaTipoArbol.obtener_tipo(nombre, color, textura)
        self.arboles.append(Arbol(x, y, tipo))


# ---------------------------------------------------------------
# PRUEBA DEL PATRÓN
# ---------------------------------------------------------------
if __name__ == '__main__':
    random.seed(42)  # resultados repetibles
    TOTAL = 10000
    especies = [
        ('Pino', 'verde oscuro', 'corteza rugosa'),
        ('Roble', 'verde claro', 'corteza lisa'),
        ('Cerezo', 'rosado', 'corteza fina'),
    ]

    bosque = Bosque()
    for _ in range(TOTAL):
        nombre, color, textura = random.choice(especies)
        bosque.plantar(random.randint(0, 1000), random.randint(0, 1000),
                       nombre, color, textura)

    print(f'Árboles plantados: {len(bosque.arboles)}')
    print(f'Objetos TipoArbol (flyweights) creados: {FabricaTipoArbol.total_tipos()}')
    print(bosque.arboles[0].dibujar())
    print(bosque.arboles[1].dibujar())

    pinos = [a for a in bosque.arboles if a.tipo.nombre == 'Pino'][:2]
    print(f'Dos pinos comparten el mismo objeto TipoArbol: {pinos[0].tipo is pinos[1].tipo}')

    sin_flyweight = TOTAL * 3
    con_flyweight = FabricaTipoArbol.total_tipos() * 3
    print(f'Datos de especie guardados SIN Flyweight: {sin_flyweight}')
    print(f'Datos de especie guardados CON Flyweight: {con_flyweight}')
