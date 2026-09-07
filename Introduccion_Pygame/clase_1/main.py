import pygame, sys

pygame.init()

WIDTH = 1200
HEIGHT = 720

display = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Introducción a Pygame")
clock = pygame.time.Clock()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #background
    display.fill((0,0,0))

    #text
    font = pygame.font.SysFont(None, 36)
    font_color = (255,255,255)
    text_render = font.render("LUIS ANDRES BOLAÑO MARTINEZ", True, font_color)

    #position text
    text_position = text_render.get_rect(
        center=(WIDTH // 2, HEIGHT // 2)
    )
    display.blit(text_render, text_position)

    #update display
    pygame.display.flip()


    clock.tick(60)


pygame.quit()
sys.exit()