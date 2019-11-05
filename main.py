import pygame

screen_width = 576
screen_height = 512
screen_mode = (screen_width, screen_height)

pygame.init()
pygame.display.init()
screen = pygame.display.set_mode(screen_mode)
pygame.display.set_caption("Flappy Bird")

background_image = pygame.image.load("assets/sprites/background-day.png")

base_image = pygame.image.load("assets/sprites/base.png")
base_x = 0

player_image = pygame.image.load("assets/sprites/yellowbird-midflap.png")
player_x, player_y = 170, 200


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


def draw_player():
    screen.blit(player_image, (player_x, player_y))


score = 10


def text(text, tam, color):
    font = pygame.font.Font("assets/fonts/Flappy-Bird.ttf", tam)
    text = font.render("{}".format(text), True, color)
    screen.blit(text, ((screen_width/2 - 20), 0))


def hud():
    text(score, 64, (0, 0, 0))
    text(score, 58, (255, 255, 255))


def main_menu():
    font = pygame.font.Font("assets/fonts/Flappy-Bird.ttf", 70)
    text = font.render("Flappy Bird", True, (0, 0, 0))
    screen.blit(text, (160,90))
    font2 = pygame.font.Font("assets/fonts/Flappy-Bird.ttf", 70)
    text2 = font.render("Flappy Bird", True, (255, 255, 255))
    screen.blit(text2, (165,85))



playing = True
while playing:
    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
    draw_background()
    draw_bases()
    draw_player()
    hud()
    pygame.display.update()
