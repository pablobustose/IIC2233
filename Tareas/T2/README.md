# Tarea 2: DCCruz vs Zombies :zombie::seedling::sunflower:

* Nombre: Pablo Bustos
* Sección: 4
* Usuario GitHub: pablobustose

## Consideraciones generales :octocat:

El código realiza todo lo solicitado. Se logra una buena conexión entre el frontend y el backend. Se crean y muestran tanto las instancias de las plantas como las de los zombies, generando su respectivo movimiento y funcionalidad. Se logra generar el impacto de los guisantes con los zombies, que estos muerdan y eliminen a las plantas. Cuando los zombies cruzan a la casa pierde el usuario, y cuando se eliminan todos los zombies gana el usuario. Los cheatcodes se implementaron de buena manera también. 
A considerar: Por lo general, cuando dos o más zombies comen una planta, suelen tener problemas los zombies que no mataron a la planta. 


### Cosas implementadas y no implementadas :white_check_mark: :x:

#### Ventanas: 39 pts (40%)
##### ✅ Ventana de Inicio
##### ✅ Ventana de Ranking	
##### ✅ Ventana principal
##### ✅ Ventana de juego	
##### ✅ Ventana post-ronda
#### Mecánicas de juego: 46 pts (47%)			
##### ✅ Plantas
##### ✅ Zombies
##### ✅ Escenarios		
##### ✅ Fin de ronda	
##### ✅ Fin de juego	
#### Interacción con el usuario: 22 pts (23%)
##### ✅ Clicks	
##### ✅ Animaciones
#### Cheatcodes: 8 pts (8%)
##### ✅ Pausa
##### ✅ S + U + N
##### ✅ K + I + L
#### Archivos: 4 pts (4%)
##### ✅ Sprites
##### ✅ Parametros.py
##### ✅ K + I + L
#### Bonus: 9 décimas máximo
##### ❌ Crazy Cruz Dinámico
##### ❌ Pala
##### ❌ Drag and Drop Tienda
##### ❌ Música juego

## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```main.py```. Los archivos deben estar guardados en la misma carpeta, en donde se deben encontrar su interior (```main.py```, ```parametros.py```, ```puntajes.txt```,  ```aplicacion.py```, ```ventana_inicio.ui```, ```ventana_juego.ui```, ```ventana_post_ronda.ui```, ```ventana_principal.ui```, ```ventana_ranking.ui```, ```frontend```, ```backend```). 
Dentro de ```frontend``` se debe encontrar (```ventana_inicio.py```, ```ventana_juego.py```, ```ventana_post_ronda.py```, ```ventana_principal.py```, ```ventana_ranking.py```, ```sonidos```, ```sprites```). 
Dentro de ```backend``` se debe encontrar (```logica_inicio.py```, ```logica_juego.py```, ```plantas.py```, ```zombies.py```, ```logica_ranking.py```, ```aparicion_zombies.py```).

## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```random```: ```randint```
2. ```PyQt5.QtCore```: ```QObject```, ```pyqtSignal```, ```QTimer```, ```Qt```
3. ```PyQt5.QtWidgets```: ```QLabel```, ```QApplication```
4. ```PyQt5.QtGui```: ```QPixmap```
5. ```PyQt5```: ```uic```
6. ```os```: ```path```

### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```logica_inicio```: Contiene a ```LogicaInicio```. Realizada para encargarse de verificar el input del usuario en la ventana de inicio
2. ```logica_juego```: Contiene a ```LogicaJuego```. Realizada para encargarse de toda la logística del juego, mandándole señales a la ventana de juego para que esta le muestre al usuario lo que está ocurriendo.
3. ```logica_ranking```: Contiene a ```LogicaRanking```. Realizada para encargarse de hacer el top 5 de los mejores puntajes y enviárselo a la ventana del ranking para que sean mostrados
4. ```plantas```: Contiene todas las clases de las plantas, soles y guisantes. Realizada para encargarse de crear las clases para luego ser instanciadas y utilizadas a lo largo del juego.
5. ```zombies```: Contiene las clases de los dos tipos de zombies. Realizada para encargarse de crear las clases de los zombies para luego ser instanciados y utilizados a lo largo del juego.
6. ```ventana_inicio```: Contiene a ```VentanaInicio```. Realizada para encargarse de crear la ventana de inicio y mostrarsela al usuario mientras sea necesario.
7. ```ventana_juego```: Contiene a ```VentanaJuego```. Realizada para encargarse de crear la ventana de juego y mostrarsela al usuario mientras sea necesario.
8. ```ventana_post_ronda```: Contiene a ```VentanaPostRonda```. Realizada para encargarse de crear la ventana post ronda y mostrarsela al usuario mientras sea necesario.
9. ```ventana_ranking```: Contiene a ```VentanaRanking```. Realizada para encargarse de crear la ventana del ranking y mostrarsela al usuario mientras sea necesario.
10. ```aplicacion```: Contiene a ```DCCruz```. Realizada para encargarse de crear la aplicacion para poder conectar tanto el front como el back y lograr cumplir con lo solicitado. Dentro de esta se realiza la gran mayoría de las conexiones de las señales.


## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. Multipliqué por 10 los ms del intervalo de aparición de los zombies. Consideré que era más lógico que estos aparezcan cada 7 segundos aprox. en vez que cada 0.7 segundos aprox. (que son los valores aproximados que retorna ```aparicion_zombies``` )
2. Para el uso de los cheatcodes, se deben presionar las teclas en orden y no al mismo tiempo.
3. El concepto de "zombies restantes" hace referencia a los zombies que aún no han aparecido en la pantalla y que faltan por crearse a lo largo de la ronda
4. El botón salir de ```VentanaJuego``` conduce al usuario a la post-ronda. En el enunciado faltó detallar mejor ese detalle, ya que se podía interpretar también que este botón conduzca a la ```VentanaInicio```. Sin embargo, consideré que era mejor realizarlo de esta manera y así todas las partidas te manden a la post-ronda independiente de lo que pase.
5. Cambié los costos de las plantas, velocidad de los zombies y su intervalo de mordida para que sea más veloz el juego y así poder mejorar su jugabilidad.
