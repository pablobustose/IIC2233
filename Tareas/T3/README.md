# Tarea 3: DCCard-Jitsu 🐧🥋

* Nombre: Pablo Bustos
* Sección: 4
* Usuario GitHub: pablobustose

**Dejar claro lo que NO pudieron implementar y lo que no funciona a la perfección. Esto puede sonar innecesario pero permite que el ayudante se enfoque en lo que sí podría subir su puntaje.**

## Consideraciones generales :octocat:

El desarrollo del código es adecuado. El servidor es el encargado de procesar y validar ciertas funcionalidades y el cliente recibe e interpreta lo dicho por el servidor. Se logran comprobar los requisitos para que un usuario pueda entrar a la sala de espera, notificando al usuario en caso de que hayan errores. Se logra avanzar a la ventana de juego tras terminar el timer de la sala de espera. Los resultados de las batallas entre cartas son los correctos, se le notifica a cada usuario su respectivo resultado de la batalla y se van actualizando las fichas de victoria. Si una carta pierde o empata una batalla, se agrega correctamente al final del mazo, como se indica en el enunciado. Si no es seleccionada una carta antes de que el timer termine, se selecciona una de manera aleatoria. En resumen, la funcionalidad del código es la esperada según el enunciado. Un único detalle es que el servidor al recibir muchas tareas simultáneas, a veces tiene pequeños problemas al mandar y/o recibir mensajes, por lo que algunos errores podrían desencadenarse gracias a esto. Se le implementaron locks para intentar solucionarlo, pero no estoy del todo seguro si estos lograron eliminar o aminorar el problema. 
### Cosas implementadas y no implementadas :white_check_mark: :x:

#### Networking: 26 pts (19%)
##### ✅ Protocolo	
##### ✅ Correcto uso de sockets		
##### ✅ Conexión	
##### ✅ Manejo de Clientes	
##### 🟠 Desconexión Repentina
#### Arquitectura Cliente - Servidor: 31 pts (23%)			
##### ✅ Roles			
##### 🟠 Consistencia		
##### ✅ Logs
#### Manejo de Bytes: 27 pts (20%)
##### ✅ Codificación			
##### ✅ Decodificación			
##### ✅ Encriptación		
##### ✅ Desencriptación	
##### ✅ Integración
#### Interfaz Gráfica: 27 pts (20%)	
##### ✅ Ventana inicio		
##### ✅ Sala de Espera			
##### ✅ Ventana de juego							
##### ✅ Ventana final
#### Reglas de DCCard-Jitsu: 17 pts (13%)
##### ✅ Inicio del juego			
##### ✅ Ronda				
##### ✅ Termino del juego
#### Archivos: 8 pts (6%)
##### ✅ Parámetros (JSON)		
##### ✅ Cartas.py	
##### ✅ Cripto.py
#### Bonus: 8 décimas máximo
##### ❌ Cheatcodes	
##### ❌ Bienestar	
##### ❌ Chat

## Ejecución Servidor :computer:
El módulo principal del servidor a ejecutar es  ```main.py```. Los archivos deben estar guardados en la misma carpeta, en donde se deben encontrar su interior (```main.py```, ```cripto.py```, ```cartas.py```,  ```servidor.py```, ```parametros.json```, ```utils.py```).

## Ejecución Cliente
El módulo principal del cliente a ejecutar es  ```main.py```. Los archivos deben estar guardados en la misma carpeta, en donde se deben encontrar su interior (```main.py```, ```utils.py```, ```parametros.json```,  ```sprites```, ```ventana_inicio.ui```, ```ventana_juego.ui```, ```ventana_espera.ui```, ```ventana_final.ui```, ```frontend```, ```backend```). 
Dentro de ```frontend``` se debe encontrar (```ventana_inicio.py```, ```ventana_espera.py```, ```ventana_juego.py```, ```ventana_final.py```). 
Dentro de ```backend``` se debe encontrar (```cartas.py```, ```cliente.py```, ```cripto.py```, ```interfaz.py```).

## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```random```: ```randint```, ```shuffle```
2. ```PyQt5.QtCore```: ```QObject```, ```pyqtSignal```, ```QTimer```, ```Qt```
3. ```PyQt5.QtWidgets```: ```QLabel```, ```QApplication```
4. ```PyQt5.QtGui```: ```QPixmap```
5. ```PyQt5```: ```uic```
6. ```os```: ```path```
7. ```socket```
8. ```threading```
9. ```json```
10. ```sys```
11. ```time```

### Librerías propias - Servidor :computer:
Los módulos que fueron creados para el ```Servidor```fueron los siguientes:

1. ```servidor```: Contiene a ```Servidor```. Realizada para encargarse de crear el servidor a utilizar, el cual tendrá todas las funciones necesarias para controlar el flujo y desarrollo del juego.
2. ```utils.```: Realizada para la lectura adecuada de los archivos de parámetros de tipo JSON

### Librerías propias - Cliente
Los módulos que fueron creados para el ```Cliente``` fueron los siguientes:

1. ```cliente```: Contiene a ```Cliente```. Realizada para encargarse de crear el cliente, el cual tendrá todas las funciones necesarias para tener un adecuado desarrollo del juego, manteniendo informado al jugador de lo que está sucediendo
2. ```utils```: Realizada para la lectura adecuada de los archivos de parámetros de tipo JSON
3. ```interfaz```: Contiene a ```Interfaz```, la cual contiene a todas las instancias de las ventanas para así tener una mejor conexión entre estas.
4. ```ventana_inicio```: Contiene a ```VentanaInicio```. Realizada para encargarse de crear la ventana de inicio y mostrarsela al usuario mientras sea necesario.
7. ```ventana_juego```: Contiene a ```VentanaJuego```. Realizada para encargarse de crear la ventana de juego y mostrarsela al usuario mientras sea necesario.
8. ```ventana_espera```: Contiene a ```VentanaEspera```. Realizada para encargarse de crear la ventana de espera y mostrarsela al usuario mientras sea necesario.
9. ```ventana_final```: Contiene a ```VentanaFinal```. Realizada para encargarse de crear la ventana final y mostrarsela al usuario mientras sea necesario.


## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. Ambos usuarios deben haber corrido el código para comenzar con los intentos para ingresar a la ventana de espera.

PD: Para el envío desde y hacia el servidor, se utilizaron diferentes "tipos" de mensaje, en donde se facilita la comprensión y clasificación de este tanto para el cliente como para el servidor. Algunos de estos son:
- login: para la verificación del nombre de usuario
- actualizar_nombres: para actualizar el nombre de usuario a todos cuando entra uno nuevo
- ventana_espera: soluciona la temática de la ventana de espera
- iniciar_timer: inicia el timer de la ventana de espera
- parar_timer_espera: para el timer cuando alguien se sale de la ventana de espera
- inicio_partida: se da inicio a la partida
- carta_seleccionada: cuando se confirma la selección de una carta por parte del cliente
- resultado_batalla: el servidor le anuncia a cada uno su resultado de la pelea
- terminar timer: el servidor avisa a las ventanas que el timer se debe terminar porque ya eligieron cartas los dos
- actualizar_triunfos: actualiza las fichas de triunfos en cada ventana de juego


## Referencias de código externo :book:

Para realizar mi tarea saqué código de:
1.AF3-2022-2: En esta actividad formativa se crea el módulo ```utils.```, el cual fue agregado tanto para el cliente como para el usuario. Este ayuda a la lectura de los archivos JSON, ya que los parámetros están en este formato.
