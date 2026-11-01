# Space Defender 🚀

## 1. Descripción del proyecto

Space Defender es un videojuego 2D desarrollado en Python utilizando Pygame y GitHub Copilot como asistente de programación.

El jugador controla una nave espacial, dispara a un enemigo y acumula puntos mientras evita los proyectiles enemigos. Cuenta con tres vidas y permite reiniciar la partida después de perder.

## 2. Tecnologías utilizadas

- Python 3.13
- Pygame 2.6.1
- Visual Studio Code
- GitHub Copilot
- Git y GitHub

## 3. Ejecución del videojuego

Abrir una terminal dentro de la carpeta del proyecto y ejecutar:

```powershell
py -3.13 -m pip install pygame
py -3.13 main.py
```

Controles:
- Flechas izquierda y derecha: mover la nave.
- Barra espaciadora: disparar.
- Tecla R: reiniciar después de Game Over.

## 4. Evidencia de vibecoding

### Prompt 1: Primera versión
Se solicitó a GitHub Copilot crear un videojuego 2D de 800 × 600 píxeles con nave azul, enemigo rojo, movimiento horizontal, disparos y puntuación.

Objetivo: construir una versión básica y funcional antes de agregar características más complejas.

Resultado: la IA generó el código inicial en main.py. Se comprobaron el movimiento, los disparos y la puntuación.

### Prompt 2: Sistema de vidas y Game Over
Se solicitó agregar tres vidas, ataques periódicos del enemigo, detección de impactos contra la nave, pantalla Game Over y reinicio mediante R.

Motivo del refinamiento: la primera versión no tenía un desafío de supervivencia ni una condición para perder.

Resultado: se implementaron las nuevas funcionalidades y se verificó que funcionaran sin afectar las existentes.

### Prompt 3: Comprensión del código
Se pidió a Copilot analizar main.py sin modificarlo y explicar movimiento, disparos, colisiones, vidas, puntuación y reinicio. También se solicitó identificar una posible limitación.

Motivo: comprender y evaluar el código generado en lugar de aceptarlo sin revisión.

Resultado: se identificó que los proyectiles enemigos descendían verticalmente sin apuntar hacia la nave.

### Prompt 4: Disparos direccionales
Se solicitó modificar los disparos enemigos para calcular la dirección hacia la posición de la nave al momento de disparar, conservando una trayectoria fija después del lanzamiento.

Motivo: mejorar el comportamiento enemigo y resolver la limitación identificada en el análisis anterior.

Resultado: los disparos adquirieron dirección y se comprobó que las demás funciones siguieran funcionando.

## 5. Validación y errores encontrados

Se realizaron pruebas manuales de:
- Movimiento horizontal de la nave.
- Disparos y detección de impactos.
- Actualización de puntuación.
- Pérdida de vidas.
- Pantalla Game Over.
- Reinicio con R.
- Nueva trayectoria de los disparos enemigos.

Durante el desarrollo, Pygame no pudo instalarse con Python 3.15. Para resolverlo, se instaló Python 3.13 y posteriormente Pygame 2.6.1.

También se identificó una limitación del comportamiento enemigo y se corrigió mediante un nuevo prompt.

## 6. Comprensión del código

- actualizar_juego(): actualiza posiciones, proyectiles y colisiones.
- manejar_eventos(): procesa las entradas del teclado.
- dibujar_juego(): dibuja los objetos y muestra vidas y puntuación.
- reiniciar_juego(): restablece el estado inicial de la partida.
- colliderect(): detecta intersecciones entre los objetos rectangulares.

## 7. Reflexión final

Aprendí que la inteligencia artificial puede ayudar a desarrollar aplicaciones más rápidamente, especialmente cuando se proporcionan instrucciones claras y progresivas.

Una ventaja del vibecoding es que permite construir prototipos funcionales y mejorar el código mediante conversaciones con la IA. Una limitación es que el resultado generado no necesariamente funciona correctamente o cumple todos los requisitos, por lo que debemos comprobarlo.

Comprendo cómo funcionan el movimiento de la nave, los disparos, las colisiones, el sistema de vidas y la puntuación. Necesito seguir reforzando la organización del código en funciones y los cálculos utilizados para determinar trayectorias.

Este proyecto me permitió practicar el proceso de solicitar código, ejecutarlo, detectar limitaciones, mejorar las instrucciones y validar los resultados.