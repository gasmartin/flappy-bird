import pygame

screen_width = 800
screen_height = 600
screen_mode = (screen_width, screen_height)

screen = pygame.display.set_mode(screen_mode)

playing = True
while playing:
    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False

    pygame.display.update()
