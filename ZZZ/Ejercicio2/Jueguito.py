import pygame
import random
import math
import sys
import os

# Inicializar pygame
pygame.init()

# Establece el tamaño de la pantalla
screen_width = 880
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Función para obtener la ruta de los recursos
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS  # Para entornos empaquetados (como un .exe)
    except Exception:
        base_path = os.path.abspath(".")  # Si no está empaquetado, usa la ruta local
    return os.path.join(base_path, relative_path)  # Devuelve la ruta correcta

# Cargar imagen de fondo
asset_background = resource_path('ZZZ/Ejercicio2/assets/images/background.png')
background = pygame.image.load(asset_background)
background = pygame.transform.scale(background, (screen_width, screen_height))


# Cargar icono de ventana
asset_icon = resource_path('ZZZ/Ejercicio2/assets/images/ufo.png')
icon = pygame.image.load(asset_icon)

# Cargar sonido de fondo
asset_sound = resource_path('ZZZ/Ejercicio2/assets/audios/background_music.mp3')
background_sound = pygame.mixer.music.load(asset_sound)

# Cargar imagen del jugador
asset_playerimg = resource_path('ZZZ/Ejercicio2/assets/images/space-invaders.png')
playerimg = pygame.image.load(asset_playerimg)

# Cargar imagen de la bala
asset_bulletimg = resource_path('ZZZ/Ejercicio2/assets/images/bullet.png')
bulletimg = pygame.image.load(asset_bulletimg)

# Cargar fuente para texto de game over
asset_over_font = resource_path('ZZZ/Ejercicio2/assets/fonts/RAVIE.TTF')
over_font = pygame.font.Font(asset_over_font, 60)

# Cargar fuente para texto de puntuación
asset_font = resource_path('ZZZ/Ejercicio2/assets/fonts/comicbd.ttf')
font = pygame.font.Font(asset_font, 32)

# Establecer titulo de la ventana
pygame.display.set_caption("ManuSpace Invasor")

# Establecer icono de ventana
pygame.display.set_icon(icon)

# Reproducir sonido de fondo en loop
pygame.mixer.music.play(-1)

# Crear reloj para controlar la velocidad del juego
clock = pygame.time.Clock()

# Posicion inicial del jugador
playerX = 370
playerY = 470
playerX_change = 0
playerY_change = 0

# Lista para almacenar posiciones de los enemigos
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
no_of_enemies = 10

# Se inicializan las variables para guardar las posciones de los enemigos
for i in range(no_of_enemies):
    # Se carga la imagen del enemigo 1 y 2
    enemy1 = resource_path('ZZZ/Ejercicio2/assets/images/enemy1.png')
    enemyImg.append(pygame.image.load(enemy1))
    
    enemy2 = resource_path('ZZZ/Ejercicio2/assets/images/enemy2.png')
    enemyImg.append(pygame.image.load(enemy2))
    
    # Se asigna una posición aleatoria en X y en Y para el enemigo
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(0, 150))
    
    # Se establece la velocidad de movimiento del enemigo X y Y
    enemyX_change.append(5)
    enemyY_change.append(20)

# Variables de la bala
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"

# Se inicializa la puntuación en 0
score = 0

# Función para mostrar la puntuación en la pantalla
def show_score():
    score_value = font.render("SCORE: " + str(score), True, (255, 255, 255))
    screen.blit(score_value, (10, 10))

# Función para dibujar al jugador en la pantalla
def player(x, y):
    screen.blit(playerimg, (x, y))

# Función para dibujar al enemigo en la pantalla
def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))

# Función para disparar la bala
def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletimg, (x + 16, y + 10))

# Función para comprobar si hubo colisión entre bala y enemigo
def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) +
                         (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False

# Función para mostrar el texto de "Game over" en pantalla
def game_over_text():
    over_text = over_font.render("ManuPerdiste", True, (255, 255, 255))
    text_rect = over_text.get_rect(
        center=(int(screen_width / 2), int(screen_height / 2)))
    screen.blit(over_text, text_rect)

# Función principal del juego
def gameloop():
    global score
    global playerX
    global playerX_change
    global playerY
    global playerY_change
    global bulletX
    global bulletY
    global collision
    global bullet_state

    in_game = True
    while in_game:
        # Maneja eventos, actualiza y renderiza el juego
        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                in_game = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                # Maneja el movimiento del jugador y el disparo
                if event.key == pygame.K_LEFT:
                    playerX_change = -5
                if event.key == pygame.K_RIGHT:
                    playerX_change = 5
                if event.key == pygame.K_SPACE:
                    if bullet_state == "ready":
                        bulletX = playerX  # Establecer la posición de la bala según la del jugador
                        fire_bullet(bulletX, bulletY)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    playerX_change = 0

        # Aquí se actualiza la posición del jugador
        playerX += playerX_change

        if playerX <= 0:
            playerX = 0
        elif playerX >= 736:
            playerX = 736

        # Bucle que se ejecuta para cada enemigo
        for i in range(no_of_enemies):
            if enemyY[i] > 440:
                for j in range(no_of_enemies):
                    enemyY[j] = 2000
                game_over_text()

            enemyX[i] += enemyX_change[i]
            if enemyX[i] <= 0:
                enemyX_change[i] = 5
                enemyY[i] += enemyY_change[i]
            elif enemyX[i] >= 736:
                enemyX_change[i] = -5
                enemyY[i] += enemyY_change[i]

            # Comprobar si hubo colisión entre enemigo y bala
            collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
            if collision:
                bulletY = 454  # Restablecer la posición de la bala
                bullet_state = "ready"
                score += 1
                enemyX[i] = random.randint(0, 736)
                enemyY[i] = random.randint(0, 150)
            enemy(enemyX[i], enemyY[i], i)

        if bulletY < 0:
            bulletY = 454
            bullet_state = "ready"

        if bullet_state == "fire":
            fire_bullet(bulletX, bulletY)
            bulletY -= bulletY_change

        player(playerX, playerY)
        show_score()

        pygame.display.update()
        clock.tick(120)

gameloop()
