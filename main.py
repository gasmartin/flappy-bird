import pygame

screen_width = 576
screen_height = 512
screen_mode = (screen_width, screen_height)

window_fps = 60

pygame.init()
pygame.display.init()
screen = pygame.display.set_mode(screen_mode)
pygame.display.set_caption("Flappy Bird")

clock = pygame.time.Clock()

# importação dos efeitos sonoros
sounds = dict()
sounds['die'] = pygame.mixer.Sound('assets/audio/die.wav')
sounds['hit'] = pygame.mixer.Sound('assets/audio/hit.wav')
sounds['point'] = pygame.mixer.Sound('assets/audio/point.wav')
sounds['swoosh'] = pygame.mixer.Sound('assets/audio/swoosh.wav')
sounds['wing'] = pygame.mixer.Sound('assets/audio/wing.wav')


background_image = pygame.image.load("assets/sprites/background-day.png")

base_image = pygame.image.load("assets/sprites/base.png")
base_x = 0

player_image = pygame.image.load("assets/sprites/yellowbird-midflap.png")
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
    font = pygame.font.Font("assets/fonts/Flappy-Bird.ttf", tam)
    text = font.render("{}".format(text), True, color)
    screen.blit(text, ((screen_width/2 - 20), 0))


def hud():
    text(score, 64, (0, 0, 0))
    text(score, 58, (255, 255, 255))


def main_menu():
    start = pygame.image.load('assets/sprites/message.png')
    screen.blit(start, (195,90))


def gameover():
    end = pygame.image.load('assets/sprites/gameover.png')
    screen.blit(end, (195,200))

playing = True
while playing:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            playing = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                jump()

    screen.fill((0, 0, 0))

    draw_background()
    draw_bases()

    update_player()
    draw_player()

    hud()
    
    pygame.display.update()
    clock.tick(window_fps)
    print("FPS:", clock.get_fps())

pygame.quit()
