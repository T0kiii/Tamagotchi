# Tamagotchi

Juego mascota virtual con GUI en Python (V)

## Objetivos

- Aplicación multiplataforma con interfaz gráfica:
  - Varias ventanas o una única con menús desplegables? (J) depende de cómo planteemos el gameplay
  - Menú para navegar por la interfaz
  - Panel para pequeñas animaciones
  - Botones para interactuar con la mascota
  
- Debe guardar el progreso en algún formato para poder recuperar la información de la partida la próxima vez que se abra
- Lanzar un servicio para que corra en segundo plano en vez de cargar partida? Si se hace, cuándo se guardaría partida?

    (J) Al ser una aplicación sobre cuidar a tu mascota, nos interesa que los acontencimientos sigan ocurriendo aún con la aplicación apagada. No tiene         sentido que la situación de tu mascota sea la misma cuando cierras la app que cuando la abres porque tu mascota siempre se encontraría tal y como la       dejaste. No se si esto es muy complicado de hacer (?)

- Las acciones para interactuar con la mascota en principio serán:
  - Alimentar
  - Limpiar
  - Mimar

VARIABLE PRINCIPAL: SALUD
OBJETIVO: QUE EL BICHO NO MUERA
 
La salud depende de varios factores:
 
    - Alimentación:
      Debe ser alimentado diariamente un par de veces(?) con comida
 
    - Estamina: nivel de energía
      Energía para realizar juegos con el usuario, sin ella el bicho estará demasiado cansado para jugar
      
    - Felicidad:
      La felicidad Depende del nivel de sociabilidad y atención que reciba por parte del usuario
      
    - Higiene:  
      A niveles muy bajos puede afectar a la salud
      
Valores aleatorios:

    - Mood: estado de ánimo
      Depende de cómo se levante nuestra mascota, introduce aleatoriedad.
      
      
- Debemos diseñar un sistema que interrelacione estas variables

SALUD (100%)

- comer X veces al día afecta a su - ALIMENTACIÓN(25%), el no hacerlo irá rebajando sus stats y viceversa
    
- jugar X veces al día afecta a su - ESTAMINA (25%) y - FELICIDAD (25%), el no hacerlo irá rebajando sus stats y viceversa
                                 
- lavar X veces a la mascota afecta a su - HIGIENE (25%), el no hacerlo irá rebajando sus stats más lentamente que el resto (?) y viceversa

- que tu mascota quiera jugar o no dependerá de su  - ESTAMINA y - MOOD (por ejemplo, si ESTAMINA < X y MOOD es X, la mascota no quiere jugar)
                                                   Tenemos que encontrar una forma de volver a la normalidad en el caso de que la falta de estamina no te permita jugar con la mascota y por tanto aumentar la estamina a niveles aceptables
                                                 
                                                 
   

