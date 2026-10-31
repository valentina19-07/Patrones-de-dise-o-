'''
PATRÓN: ADAPTER (Adaptador)
TIPO: Estructural
AUTOR: Juan

¿QUÉ HACE EL PATRÓN?
    Convierte la interfaz de una clase existente en otra interfaz que el
    cliente espera, permitiendo que clases incompatibles trabajen juntas.

PROBLEMA QUE RESUELVE
    Una tienda en línea trabaja con la interfaz ProcesadorPago, que cobra
    en pesos con el método pagar(monto). Se quiere usar una pasarela de pago
    legada (de un proveedor externo, que NO se puede modificar) cuyo método
    es realizar_transaccion(centavos, codigo_moneda) y devuelve un texto.
    Las interfaces son incompatibles.

¿POR QUÉ ADAPTER ES ADECUADO?
    - No se modifica la tienda ni la pasarela legada.
    - El adaptador traduce los datos (pesos a centavos) y la respuesta
      (texto a booleano).
    - La tienda no sabe si habla con una pasarela moderna o con una legada.

CÓMO EJECUTAR:  python estructurales/04_adapter.py
'''

from abc import ABC, abstractmethod


# ---------------------------------------------------------------
# INTERFAZ OBJETIVO (Target): la que espera el cliente
# ---------------------------------------------------------------
class ProcesadorPago(ABC):
    @abstractmethod
    def pagar(self, monto_cop):
        pass


class PasarelaModerna(ProcesadorPago):
    '''Ya cumple la interfaz esperada, no necesita adaptador.'''

    def pagar(self, monto_cop):
        print(f'[Pasarela moderna] Cobrando ${monto_cop:,.0f} COP')
        return True


# ---------------------------------------------------------------
# CLASE ADAPTADA (Adaptee): interfaz incompatible que no podemos cambiar
# ---------------------------------------------------------------
class PasarelaLegada:
    def realizar_transaccion(self, centavos, codigo_moneda):
        print(f'[Pasarela legada] Transacción de {centavos} centavos en {codigo_moneda}')
        return f'TX-OK-{centavos}'


# ---------------------------------------------------------------
# ADAPTADOR: implementa la interfaz objetivo y delega en la legada
# ---------------------------------------------------------------
class AdaptadorPasarelaLegada(ProcesadorPago):
    def __init__(self, pasarela_legada):
        self._pasarela = pasarela_legada

    def pagar(self, monto_cop):
        centavos = int(round(monto_cop * 100))                 # traduce el dato
        respuesta = self._pasarela.realizar_transaccion(centavos, 'COP')
        return respuesta.startswith('TX-OK')                   # traduce la respuesta


# ---------------------------------------------------------------
# CLIENTE: solo conoce la interfaz ProcesadorPago
# ---------------------------------------------------------------
class Tienda:
    def __init__(self, procesador):
        self._procesador = procesador

    def finalizar_compra(self, total):
        if self._procesador.pagar(total):
            print(f'Compra exitosa por ${total:,.0f} COP')
        else:
            print('Pago rechazado')


# ---------------------------------------------------------------
# PRUEBA DEL PATRÓN
# ---------------------------------------------------------------
if __name__ == '__main__':
    print('--- Tienda con pasarela moderna ---')
    Tienda(PasarelaModerna()).finalizar_compra(150000)

    print('--- Tienda con pasarela legada (a través del adaptador) ---')
    Tienda(AdaptadorPasarelaLegada(PasarelaLegada())).finalizar_compra(150000)
