import math

import pygame


pygame.init()

ANCHO = 800
ALTO = 600
FPS = 60

FONDO = (15, 18, 35)
AZUL = (50, 140, 255)
ROJO = (230, 60, 60)
BLANCO = (240, 240, 240)
AMARILLO = (255, 210, 70)

pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Space Defender")
reloj = pygame.time.Clock()
fuente = pygame.font.Font(None, 36)
fuente_grande = pygame.font.Font(None, 72)

VELOCIDAD_NAVE = 6
VELOCIDAD_ENEMIGO = 4
VELOCIDAD_PROYECTIL = 8
VELOCIDAD_PROYECTIL_ENEMIGO = 4.5
INTERVALO_DISPARO_ENEMIGO = 1400


def reiniciar_juego():
    """Restablece los elementos y el marcador para una nueva partida."""
    global nave, enemigo, direccion_enemigo
    global proyectiles, proyectiles_enemigos, puntuacion, vidas
    global juego_terminado, proximo_disparo_enemigo

    nave = pygame.Rect(ANCHO // 2 - 25, ALTO - 70, 50, 40)
    enemigo = pygame.Rect(ANCHO // 2 - 25, 60, 50, 35)
    direccion_enemigo = 1
    proyectiles = []
    proyectiles_enemigos = []
    puntuacion = 0
    vidas = 3
    juego_terminado = False
    proximo_disparo_enemigo = (
        pygame.time.get_ticks() + INTERVALO_DISPARO_ENEMIGO
    )


def manejar_eventos():
    """Procesa el cierre de ventana y las teclas del jugador."""
    global ejecutando

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
        elif evento.type == pygame.KEYDOWN:
            if juego_terminado and evento.key == pygame.K_r:
                reiniciar_juego()
            elif not juego_terminado and evento.key == pygame.K_SPACE:
                proyectiles.append(
                    pygame.Rect(nave.centerx - 3, nave.top - 12, 6, 12)
                )


def actualizar_juego():
    """Actualiza movimiento, disparos, impactos y puntuacion."""
    global direccion_enemigo, puntuacion, vidas
    global juego_terminado, proximo_disparo_enemigo

    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        nave.x -= VELOCIDAD_NAVE
    if teclas[pygame.K_RIGHT]:
        nave.x += VELOCIDAD_NAVE
    nave.clamp_ip(pantalla.get_rect())

    enemigo.x += VELOCIDAD_ENEMIGO * direccion_enemigo
    if enemigo.left <= 0 or enemigo.right >= ANCHO:
        direccion_enemigo *= -1

    ahora = pygame.time.get_ticks()
    if ahora >= proximo_disparo_enemigo:
        x = float(enemigo.centerx - 3)
        y = float(enemigo.bottom)
        origen_x = x + 3
        origen_y = y + 6

        # Calcula una dirección hacia la posición actual de la nave.
        direccion_x = nave.centerx - origen_x
        direccion_y = nave.centery - origen_y
        distancia = math.hypot(direccion_x, direccion_y)
        velocidad_x = (
            direccion_x / distancia * VELOCIDAD_PROYECTIL_ENEMIGO
        )
        velocidad_y = (
            direccion_y / distancia * VELOCIDAD_PROYECTIL_ENEMIGO
        )

        proyectiles_enemigos.append(
            {
                "rect": pygame.Rect(round(x), round(y), 6, 12),
                "x": x,
                "y": y,
                "velocidad_x": velocidad_x,
                "velocidad_y": velocidad_y,
            }
        )
        proximo_disparo_enemigo = ahora + INTERVALO_DISPARO_ENEMIGO

    for proyectil in proyectiles[:]:
        proyectil.y -= VELOCIDAD_PROYECTIL
        if proyectil.bottom < 0:
            proyectiles.remove(proyectil)
        elif proyectil.colliderect(enemigo):
            proyectiles.remove(proyectil)
            puntuacion += 1
            enemigo.x = ANCHO // 2 - enemigo.width // 2

    for proyectil in proyectiles_enemigos[:]:
        # Conserva la dirección calculada al disparar y actualiza su posición.
        proyectil["x"] += proyectil["velocidad_x"]
        proyectil["y"] += proyectil["velocidad_y"]
        proyectil["rect"].topleft = (
            round(proyectil["x"]),
            round(proyectil["y"]),
        )

        if (
            proyectil["rect"].right < 0
            or proyectil["rect"].left > ANCHO
            or proyectil["rect"].bottom < 0
            or proyectil["rect"].top > ALTO
        ):
            proyectiles_enemigos.remove(proyectil)
        elif proyectil["rect"].colliderect(nave):
            proyectiles_enemigos.remove(proyectil)
            vidas -= 1
            if vidas == 0:
                juego_terminado = True
            break


def dibujar_juego():
    """Dibuja los elementos de la partida y la informacion en pantalla."""
    pantalla.fill(FONDO)

    pygame.draw.polygon(
        pantalla,
        AZUL,
        [
            (nave.centerx, nave.top),
            (nave.left, nave.bottom),
            (nave.centerx, nave.bottom - 10),
            (nave.right, nave.bottom),
        ],
    )
    pygame.draw.rect(pantalla, ROJO, enemigo)

    for proyectil in proyectiles:
        pygame.draw.rect(pantalla, BLANCO, proyectil)
    for proyectil in proyectiles_enemigos:
        pygame.draw.rect(pantalla, AMARILLO, proyectil["rect"])

    texto_puntuacion = fuente.render(f"Puntuacion: {puntuacion}", True, BLANCO)
    texto_vidas = fuente.render(f"Vidas: {vidas}", True, BLANCO)
    pantalla.blit(texto_puntuacion, (10, 10))
    pantalla.blit(texto_vidas, (ANCHO - texto_vidas.get_width() - 10, 10))

    if juego_terminado:
        texto_fin = fuente_grande.render("GAME OVER", True, BLANCO)
        texto_final = fuente.render(
            f"Puntuacion final: {puntuacion}", True, BLANCO
        )
        texto_reinicio = fuente.render("Presiona R para reiniciar", True, BLANCO)
        pantalla.blit(
            texto_fin,
            texto_fin.get_rect(center=(ANCHO // 2, ALTO // 2 - 50)),
        )
        pantalla.blit(
            texto_final,
            texto_final.get_rect(center=(ANCHO // 2, ALTO // 2 + 10)),
        )
        pantalla.blit(
            texto_reinicio,
            texto_reinicio.get_rect(center=(ANCHO // 2, ALTO // 2 + 55)),
        )

    pygame.display.flip()


reiniciar_juego()
ejecutando = True
while ejecutando:
    manejar_eventos()

    if not juego_terminado:
        actualizar_juego()

    dibujar_juego()
    reloj.tick(FPS)

pygame.quit()
