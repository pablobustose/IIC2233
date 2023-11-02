from os import path

RUTA_CRUZ = path.join("frontend", "sprites", "CrazyRuz", "crazyCruz.png")
RUTA_BRAINS = path.join("frontend", "sprites", "Elementos de juego", "textoFinal.png")
RUTA_LOGO = path.join("frontend", "sprites", "Elementos de juego", "logo.png")
RUTA_FONDO = path.join("frontend", "sprites", "Fondos", "fondoMenu.png")
RUTA_FONDO_ABUELA = path.join("frontend", "sprites", "Fondos", "jardinAbuela.png")
RUTA_FONDO_NOCTURNO = path.join("frontend", "sprites", "Fondos", "salidaNocturna.png")
RUTA_SOL = path.join("frontend", "sprites", "Elementos de juego", "sol.png")
RUTA_GIRASOL1 = path.join("frontend", "sprites", "Plantas", "girasol_1.png")
RUTA_GIRASOL2 = path.join("frontend", "sprites", "Plantas", "girasol_2.png")
RUTA_CLASICA1 = path.join("frontend", "sprites", "Plantas", "lanzaguisantes_1.png")
RUTA_CLASICA2 = path.join("frontend", "sprites", "Plantas", "lanzaguisantes_2.png")
RUTA_CLASICA3 = path.join("frontend", "sprites", "Plantas", "lanzaguisantes_3.png")
RUTA_AZUL1 = path.join("frontend", "sprites", "Plantas", "lanzaguisantesHielo_1.png")
RUTA_AZUL2 = path.join("frontend", "sprites", "Plantas", "lanzaguisantesHielo_2.png")
RUTA_AZUL3 = path.join("frontend", "sprites", "Plantas", "lanzaguisantesHielo_3.png")
RUTA_PAPA1 = path.join("frontend", "sprites", "Plantas", "papa_1.png")
RUTA_PAPA2 = path.join("frontend", "sprites", "Plantas", "papa_2.png")
RUTA_PAPA3 = path.join("frontend", "sprites", "Plantas", "papa_3.png")
RUTA_ZOMBIE_LENTO_CAMINANDO_1 = path.join("frontend", "sprites", "Zombies", "Caminando", "zombieNicoWalker_1.png")
RUTA_ZOMBIE_LENTO_CAMINANDO_2 = path.join("frontend", "sprites", "Zombies", "Caminando", "zombieNicoWalker_2.png")
RUTA_ZOMBIE_RAPIDO_CAMINANDO_1 = path.join("frontend", "sprites", "Zombies", "Caminando", "zombieHernanRunner_1.png")
RUTA_ZOMBIE_RAPIDO_CAMINANDO_2 = path.join("frontend", "sprites", "Zombies", "Caminando", "zombieHernanRunner_2.png")
RUTA_ZOMBIE_LENTO_COMIENDO_1 = path.join("frontend", "sprites", "Zombies", "Comiendo", "zombieNicoComiendo_1.png")
RUTA_ZOMBIE_LENTO_COMIENDO_2 = path.join("frontend", "sprites", "Zombies", "Comiendo", "zombieNicoComiendo_2.png")
RUTA_ZOMBIE_LENTO_COMIENDO_3 = path.join("frontend", "sprites", "Zombies", "Comiendo", "zombieNicoComiendo_3.png")
RUTA_ZOMBIE_RAPIDO_COMIENDO_1 = path.join("frontend", "sprites", "Zombies", "Comiendo", "zombieHernanComiendo_1.png")
RUTA_ZOMBIE_RAPIDO_COMIENDO_2 = path.join("frontend", "sprites", "Zombies", "Comiendo", "zombieHernanComiendo_2.png")
RUTA_ZOMBIE_RAPIDO_COMIENDO_3 = path.join("frontend", "sprites", "Zombies", "Comiendo", "zombieHernanComiendo_3.png")
RUTA_GUISANTE1 = path.join("frontend", "sprites", "Elementos de juego", "guisante_1.png")
RUTA_GUISANTE2 = path.join("frontend", "sprites", "Elementos de juego", "guisante_2.png")
RUTA_GUISANTE3 = path.join("frontend", "sprites", "Elementos de juego", "guisante_3.png")
RUTA_GUISANTE_AZUL1 = path.join("frontend", "sprites", "Elementos de juego", "guisanteHielo_1.png")
RUTA_GUISANTE_AZUL2 = path.join("frontend", "sprites", "Elementos de juego", "guisanteHielo_2.png")
RUTA_GUISANTE_AZUL3 = path.join("frontend", "sprites", "Elementos de juego", "guisanteHielo_3.png")

# Los intervalos están en milisegundos
INTERVALO_DISPARO = 2000 
INTERVALO_IMPACTO = 100
VELOCIDAD_GUISANTE = 300
INTERVALO_SOLES_GIRASOL = 20000
INTERVALO_TIEMPO_MORDIDA = 3000 ######## 5000
INTERVALO_APARICION_SOLES = 5000
INTERVALO_MOVIMIENTO_GIRASOL = 1000
# El daño y la vida tienen las mismas medidas
DANO_PROYECTIL = 5
DANO_MORDIDA = 50       ########################################## es 5
VIDA_PLANTA = 100
VIDA_ZOMBIE = 80
VIDA_PAPA_2 = 125 #Vida en donde cambiará de tener la imagen 1 a 2
VIDA_PAPA_3 = 50 #Vida en donde cambiará de tener la imagen 2 a 3
# Número de zombies por carril
N_ZOMBIES = 7
# Porcentaje de ralentización
RALENTIZAR_ZOMBIE = 0.25
POSICION_X_INICIAL_ZOMBIE = 983
# Soles iniciales por ronda
SOLES_INICIALES = 250
# Número de soles generados por planta
CANTIDAD_SOLES = 2
# Número de soles agregados a la cuenta por recolección
SOLES_POR_RECOLECCION = 50
# Número de soles agregados a la cuenta por Cheatcode
SOLES_EXTRA = 25
# Ponderadores de escenarios
PONDERADOR_NOCTURNO = 0.8
PONDERADOR_DIURNO = 0.9
# La velocidad del zombie en milisegundos
VELOCIDAD_ZOMBIE = 3000 ############ es 5000
# Puntaje por eliminar zombie
PUNTAJE_ZOMBIE_DIURNO = 50
PUNTAJE_ZOMBIE_NOCTURNO = 100
# Costo por avanzar de ronda
COSTO_AVANZAR = 500
# Costo tiendas
COSTO_LANZAGUISANTE = 100
COSTO_LANZAGUISANTE_HIELO = 150
COSTO_GIRASOL = 50
COSTO_PAPA = 75
# Caracteres de nombre usuario
MIN_CARACTERES = 3
MAX_CARACTERES = 15
#Cheatcodes
CHEATCODE_SOLES_EXTRA = "sun"
CHEATCODE_KILL_ZOMBIES = "kil"

print(RUTA_AZUL1)