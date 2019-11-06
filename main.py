import pygame as pg
from random import randint
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

vec = pg.math.Vector2

player_image = pg.image.load("assets/sprites/yellowbird-midflap.png")
player_pos = vec(100, 100)
player_dy = 1
player_angle = 0
player_vel = vec(0, 0)
player_acc = vec(0, 1.8)
gravity = vec(0, 0.8)

pipe_top_image = pg.image.load("assets/sprites/pipe-green-top.png")
pipe_bottom_image = pg.image.load("assets/sprites/pipe-green-bottom.png")

pipes = []


def generate_pipe():
    pipe = {}
    gap_y = randint(60, 240)
    pipe['pipe_top_x'] = WIDTH + 50
    pipe['pipe_top_y'] = gap_y - 320
    pipe['pipe_bottom_x'] = WIDTH + 50
    pipe['pipe_bottom_y'] = gap_y + BIRD_GAP
    pipe['has_passed'] = False
    return pipe


def jump():
    global player_vel
    player_vel.y = -11


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


def update_pipes():
    for pipe in pipes:
        pipe['pipe_top_x'] -= 1
        pipe['pipe_bottom_x'] -= 1


def draw_pipes():
    for pipe in pipes:
        screen.blit(
            pipe_top_image, (pipe['pipe_top_x'], pipe['pipe_top_y'])
        )
        screen.blit(
            pipe_bottom_image, (pipe['pipe_bottom_x'], pipe['pipe_bottom_y'])
        )


def update_player():
    global player_pos, player_vel
    if player_vel.y <= 0:
        player_vel += gravity
    player_pos += player_vel + player_acc


def draw_player():
    global player_y
    screen.blit(player_image, player_pos)


score = 0


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


pipes.append(generate_pipe())


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

    update_pipes()

    for pipe in pipes:
        player_rect = pg.Rect(player_pos.x, player_pos.y, 34, 24)
        pipe_top_rect = pg.Rect(pipe['pipe_top_x'], pipe['pipe_top_y'], 52, 320)
        pipe_bottom_rect = pg.Rect(pipe['pipe_bottom_x'], pipe['pipe_bottom_y'], 52, 320)
        if player_pos.x > pipe['pipe_top_x'] and not pipe['has_passed']:
            score += 1
            pipe['has_passed'] = not pipe['has_passed']
            print(score)
        if player_rect.colliderect(pipe_top_rect) or \
            player_rect.colliderect(pipe_bottom_rect):
            playing = False
            break
        if pipe['pipe_top_x'] == 420:
            pipes.append(generate_pipe())
        elif pipe['pipe_top_x'] + 55 <= 0:
            pipes.remove(pipe)

    screen.fill(BLACK)

    draw_background()
    draw_pipes()
    draw_bases()

    update_player()
    draw_player() 

    hud()

    pg.display.flip()

pg.quit()
