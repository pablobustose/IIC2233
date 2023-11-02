# Tarea 0: Star Advanced

* Nombre: Pablo Bustos
* Sección: 4
* Usuario GitHub: pablobustose

## Consideraciones generales :octocat:

Se logra realizar todo lo solicitado en el enunciado, a excepción del bonus. Se logra crear una partida de manera correcta. La creación y retorno del tablero funciona de buena manera, en donde se va actualizando a medida que va avanzando el juego. Se logra determinar el número correcto de bestias e implementarlas en el tablero de forma aleatoria. Se logra una buena implementación de los menus, en donde se logra volver atrás si se desea y los inputs solicitados están a prueba de errores del usuario (solo considera valores dentro del rango solocitado y nada más). Guardar y cargar partidas también se logran realizar, además de mostrar el ranking de los 10 mejores resultados de partidas finalizadas con su jugador respectivo (ya sea de usuarios que ganaron y que perdieron, sin considerar partidas guardadas y no finalizadas).

### Cosas implementadas y no implementadas :white_check_mark: :x:

#### Programación Orientada a Objetos (18pts) (22%%)
##### ✅ Menú de Inicio
##### ✅ Funcionalidades		
##### ✅ Puntajes
#### Flujo del Juego (30pts) (36%) 
##### ✅ Menú de Juego
##### ✅ Tablero		
##### ✅ Bestias	
##### ✅ Guardado de partida		
#### Término del Juego 14pts (17%)
##### ✅ Fin del juego	
##### ✅ Puntajes	
#### Genera: 15 pts (15%)
##### ✅ Menús
##### ✅ Parámetros
##### ✅ PEP-8
#### Bonus: 3 décimas
##### ❌ 

## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```codigo.py```. El archivo debe ser abierto desde una carpeta llamada "T0", en donde se deben encontrar todos los archivos subidos en GitHub en su interior (```funciones.py```, ```menus.py```, ```parametros.py```, ```tablero.py```). Además se debe crear los siguientes archivos y directorios adicionales:
1. ```partidas``` en ```T0```


## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```math```: ```ceil```
2. ```random```: ```randint```
3. ```os```: ```path```, ```listdir```

### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```funciones```: Contiene a ```creacion_tablero```, ```cantidad_bestias```, ```posicion_bestias```, ```despejar_sector```, ```descubrir_sector```, ```comprobar_rango```. Módulo hecho para la realización de necesidades más internas sobre la jugabilidad del código.
2. ```menus```: Contiene a ```menu_inicial```, ```menu_juego```, ```guardar_partida```, ```cargar_partida```, ```guardar_puntaje```, ```ranking```. Módulo hecho para la realización de necesidades más externas a la jugabilidad del código.

## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. Un usuario solo tendrá una partida guardada a la vez. Si se desea guardar una nueva partida, esta borrará la anterior para poder ser guardada.
2. Se deberá crear una carpeta llamada ```partidas``` dentro de T0 (carpeta desde donde se deberá ejecutar el código) para que el funcionamiento del juego sea posible (específicamente al momento de guardar y cargar partidas).
