# Tarea 1: DCCampeonato 🏃‍♂️🏆

* Nombre: Pablo Bustos
* Sección: 4
* Usuario GitHub: pablobustose

## Consideraciones generales :octocat:

Se logra realizar todo lo solicitado en el enunciado, a excepción del bonus. Se logra crear una partida de manera correcta. Se muestran todos los posibles entrenadores a escoger con sus respectivos programones. Todos los inputs están considerados con errores de usuario. Los menus poseen las funciones de volver o salir de la partida, cerrando el programa. Están todos los valores correctamente restringidos (mantienen mínimos, máximos y no permite la ejecución de ciertas funcionalidades si no poseen el valor mínimo, por ejemplo, crear un objeto sin la energía necesaria). Se logra realizar la ronda del campeonato de buena manera, generando parejas al azar y eliminando a los perdedores de la liga. Se muestra de manera clara el estado del entrenador y de la liga, facilitando la lectura del usuario. 

### Cosas implementadas y no implementadas :white_check_mark: :x:


#### Programación Orientada a Objetos (18pts) (22%%)
##### ✅ Diagrama
##### ✅ Definición de clases, atributos, métodos y properties		
##### ✅ Relaciones entre clases
#### Preparación programa: 11 pts (7%)			
##### ✅ Creación de partidas
#### Entidades: 28 pts (19%)
##### ✅ Programón
##### ✅ Entrenador		
##### ✅ Liga	
##### ✅ Objetos		
#### Interacción Usuario-Programa 57 pts (38%)
##### ✅ General	
##### ✅ Menú de Inicio
##### ✅ Menú Entrenador
##### ✅ Menu Entrenamiento
##### ✅ Simulación ronda campeonato
##### ✅ Ver estado del campeonato
##### ✅ Menú crear objeto
##### ✅ Menú utilizar objeto
##### ✅ Ver estado del entrenador
##### ✅ Robustez
#### Manejo de archivos: 12 pts (8%)
##### ✅ Archivos CSV
##### ✅ Parámetros
#### Bonus: 5 décimas
##### ❌ Mega Evolución
##### ❌ CSV dinámico

## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```main.py```. Los archivos deben estar guardados en la misma carpeta, en donde se deben encontrar su interior (```main.py```, ```entrenadores.py```, ```funciones.py```, ```liga.py```, ```menus.py```, ```objetos.py```, ```parametros.py```, ```programon.py```). Además se deben incorporar a esta carpeta los archivos con los datos entregados (```entrenadores.csv```, ```objetos.csv```, ```programones.csv```).


## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```random```: ```randint```, ```random```
2. ```abc```: ```ABC```, ```abstractmethod```

### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```entrenador.py```: Contiene a ```Entrenador```. Módulo hecho para la realización exclusiva de la clase ```Entrenador```.
2. ```funciones.py```: Contiene a ```validar_respuesta``` ```crear_lista_entrenadores```, ```crear_lista_programones```, ```crear_lista_objetos```, ```crear_clases_entrenadores```, ```entrenar_programon```, ```generar_pares```. Módulo hecho para la realización de necesidades más internas sobre la jugabilidad del código.
3. ```liga.py```: Contiene a ```LigaProgramon```. Módulo hecho para la realización exclusiva de la clase ```LigaProgramon```.
4. ```menus.py```: Contiene a ```menu_inicial```, ```menu_entrenador```. . Módulo hecho para la creación de los menus utilizados a lo largo del juego.
5. ```objetos.py```: Contiene a ```Objetos```, ```Baya```, ```Pocion```, ```Caramelo```. Módulo hecho para la realización exclusiva de la clase ```Objetos``` y sus subclases.
6. ```programon.py```: Contiene a ```Programon```, ```Planta```, ```Fuego```, ```Agua```. Módulo hecho para la realización exclusiva de la clase ```Programon``` y sus subclases.
7. ```parametros.py```: Módulo hecho para almacenar todos los parámetros estandar realizados a lo largo del código.


## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. El primero en combatir siempre es el usuario. Si este pierde, no se imprimen los resultados de los otros combates. Consideré que quedaba más claro que el usuario había perdido y que no le era de importancia el saber del resto de los resultados.

