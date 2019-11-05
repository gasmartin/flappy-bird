import pygame

screen_width = 576
screen_height = 512
screen_mode = (screen_width, screen_height)

pygame.display.init()
screen = pygame.display.set_mode(screen_mode)
pygame.display.set_caption("Flappy Bird")

background_image = pygame.image.load("assets/sprites/background-day.png")

base_image = pygame.image.load("assets/sprites/base.png")
base_x = 0

def draw_background():
    screen.blit(background_image, (0, 0))
    screen.blit(background_image, (288, 0))

def draw_bases():
    global base_x
    screen.blit(base_image, (base_x, 400))
    screen.blit(base_image, (base_x + 336, 400))
    base_x -= 1
    if base_x <= -96:
        base_x = 0

playing = True
while playing:
    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
    draw_background()
    draw_bases()
    pygame.display.update()
