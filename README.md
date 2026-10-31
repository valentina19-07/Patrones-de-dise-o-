# Patrones de Diseño - Taller de Arquitectura de Software

Unidad Central del Valle del Cauca - Facultad de Ingeniería  
Docente: Jesús David Mejía Vergara

## Integrantes

- Juan Fernando Vargas
- Valentina González

## Lenguaje y ejecución

Python 3.10 o superior, sin dependencias externas. Cada ejercicio es un archivo independiente y se ejecuta así: `python carpeta/archivo.py` (ejemplo: `python creacionales/01_builder.py`).

## Patrones utilizados

| # | Patrón | Tipo | Archivo | Autor | Descripción del ejercicio |
|---|--------|------|---------|-------|---------------------------|
| 01 | Builder (obligatorio) | Creacional | creacionales/01_builder.py | Juan | Construcción paso a paso de computadores (oficina, gamer y personalizado) con Director y validación. |
| 02 | Factory Method | Creacional | creacionales/02_factory_method.py | Juan | Notificaciones por Email, SMS y Push creadas por subclases, sin if/elif en el cliente. |
| 03 | Singleton | Creacional | creacionales/03_singleton.py | Juan | Configuración global de la aplicación con una única instancia segura entre hilos. |
| 04 | Adapter (obligatorio) | Estructural | estructurales/04_adapter.py | Juan | Adapta una pasarela de pago legada a la interfaz moderna que usa la tienda. |
| 05 | Flyweight (obligatorio) | Estructural | estructurales/05_flyweight.py | Juan | Bosque de 10.000 árboles que comparten solo 3 objetos de tipo para ahorrar memoria. |
| 06 | Decorator | Estructural | estructurales/06_decorator.py | Valentina | Bebidas de café a las que se añaden extras (leche, chocolate, crema) que suman descripción y costo. |
| 07 | Observer (obligatorio) | Comportamiento | comportamiento/07_observer.py | Valentina | Canal de videos que notifica a sus suscriptores cada vez que publica. |
| 08 | Strategy | Comportamiento | comportamiento/08_strategy.py | Valentina | Carrito de compras con estrategias de descuento intercambiables en tiempo de ejecución. |
| 09 | Command | Comportamiento | comportamiento/09_command.py | Valentina | Editor de texto con deshacer y rehacer implementado con comandos. |
| 10 | State | Comportamiento | comportamiento/10_state.py | Valentina | Pedido de tienda en línea cuyo comportamiento cambia según su estado. |

## Organización del trabajo

- Juan: patrones 01 al 05 y README.
- Valentina: patrones 06 al 10 y configuración inicial del repositorio.

Cada archivo incluye comentarios que explican qué hace el patrón, qué problema resuelve y por qué es adecuado.
