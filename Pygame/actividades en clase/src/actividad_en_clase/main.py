import pygame
import sys

WIDTH = 1200
HEIGHT = 720

drawing = False      # Indica si el usuario mantiene presionado el clic
current_stroke = []  # Guarda los puntos del trazo actual
lines = []           # Guarda todos los trazos terminados

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Game loop
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            name_key = pygame.key.name(event.key)

            if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
                print(f"Presionaste: {name_key.upper()}")
            else:
                print(f"Presionaste: {name_key}")

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            drawing = True
            current_stroke = [event.pos]

        # Guardar trazo al soltar
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if drawing:
                drawing = False
                if len(current_stroke) > 1:
                    lines.append(current_stroke)
                current_stroke = []

        elif event.type == pygame.MOUSEMOTION and drawing:
            current_stroke.append(event.pos)

    screen.fill((255, 255, 255))

    # 1. Dibujar trazos pasados (CAMBIO AQUÍ: usas 'stroke', no 'current_stroke')
    for stroke in lines:
        if len(stroke) > 1:
            pygame.draw.lines(screen, (0, 0, 0), False, stroke, 5)

    # 2. Dibujar el trazo que se está realizando en tiempo real
    if drawing and len(current_stroke) > 1:
        pygame.draw.lines(screen, (0, 0, 0), False, current_stroke, 5)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()