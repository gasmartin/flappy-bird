import pygame as pg
from settings import *

pg.init()
pg.mixer.init()
screen = pg.display.set_mode(MODE)
pg.display.set_caption(TITLE)
clock = pg.time.Clock()

# importação dos efeitos sonoros
sounds = dict()
sounds['die'] = pg.mixer.Sound('assets/audio/die.wav')
sounds['hit'] = pg.mixer.Sound('assets/audio/hit.wav')
sounds['point'] = pg.mixer.Sound('assets/audio/point.wav')
sounds['swoosh'] = pg.mixer.Sound('assets/audio/swoosh.wav')
sounds['wing'] = pg.mixer.Sound('assets/audio/wing.wav')


background_image = pg.image.load("assets/sprites/background-day.png")

base_image = pg.image.load("assets/sprites/base.png")
base_x = 0

player_image = pg.image.load("assets/sprites/yellowbird-midflap.png")
player_x, player_y = 170, 200
player_dy = 1
player_angle = 0


def jump():
    print("JUMP")


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


def update_player():
    # player_y += player_dy
    pass


def draw_player():
    global player_y
    screen.blit(player_image, (player_x, player_y))


score = 10


def text(text, tam, color):
    font = pg.font.Font("assets/fonts/Flappy-Bird.ttf", tam)
    text = font.render("{}".format(text), True, color)
    screen.blit(text, ((WIDTH/2 - 20), 0))


def hud():
    text(score, 64, (0, 0, 0))
    text(score, 58, (255, 255, 255))


def main_menu():
    start = pg.image.load('assets/sprites/message.png')
    screen.blit(start, (195, 90))


def gameover():
    end = pg.image.load('assets/sprites/gameover.png')
    screen.blit(end, (195, 200))


playing = True


while playing:
    clock.tick(FPS)

    events = pg.event.get()
    for event in events:
        if event.type == pg.QUIT:
            playing = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                jump()

    screen.fill(BLACK)

    draw_background()
    draw_bases()

    update_player()
    draw_player()

    hud()

    pg.display.update()

pg.quit()
