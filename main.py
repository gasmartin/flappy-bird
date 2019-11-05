import pygame

screen_width = 576
screen_height = 512
screen_mode = (screen_width, screen_height)

pygame.display.init()
screen = pygame.display.set_mode(screen_mode)

background_image = pygame.image.load("assets/sprites/background-day.png")

def draw_background():
    screen.blit(background_image, (0, 0))
    screen.blit(background_image, (288, 0))

playing = True
while playing:
    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
    draw_background()
    pygame.display.update()
