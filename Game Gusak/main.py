import pygame
from pygame.constants import QUIT, K_DOWN, K_UP, K_LEFT, K_RIGHT
import random
import os
pygame.init()  # перше що потрібно зробити для того щоб розпочати нашу
# гру нам треба ініціювати
#  сам pygame
FPS = pygame.time.Clock()
HEIGT = 800
WIDTH = 1200

FONT = pygame.font.SysFont("Verdana", 20 )

COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_BLUE = (0, 0, 255)
COLOR_GREEN = (0, 255, 0)
COLOR_ORANGE = (190, 100, 5)

main_display = pygame.display.set_mode((WIDTH, HEIGT))

bg =pygame.transform.scale(pygame.image.load('background.png'), (WIDTH, HEIGT))
# трансформиуем картинку
bg_X1 = 0
bg_X2 = bg.get_width()
bg_move = 1

IMAGE_PATH = 'Goose'
PLAYER_IMAGES = os.listdir(IMAGE_PATH)


player_size = (20, 20)
# player = pygame.Surface((player_size))
player = pygame.image.load('player.png').convert_alpha()
# player.fill((COLOR_BLACK))
player_rect = player.get_rect()  # get_rect поверне координати X Y нашого
# гравця, до того
# і ми будемо змінювати їх на одиницю
# при кожний ітерації циклу
# player_speed = [1, 1]
player_move_down = [0, 4]
player_move_right = [4, 0]
player_move_up = [0, -4]
player_move_left = [-4, 0]

'''Создаем противника'''


def create_enemy():
    enemy_size = (30, 30)
    # enemy = pygame.Surface(enemy_size)
    enemy = pygame.transform.scale(pygame.image.load(
        'enemy.png').convert_alpha(), (100, 35))
    # enemy.fill(COLOR_BLUE)
    enemy_rect = pygame.Rect(WIDTH, random.randint(150, 650), *enemy_size)
    enemy_move = [random.randint(-8, -4), 0]
    return [enemy, enemy_rect, enemy_move]


CREATE_ENEMY = pygame.USEREVENT + 1  # cоздаем собитие - event CREATE_ENEMY
pygame.time.set_timer(CREATE_ENEMY, 1500)  # собитие и промежуток времени

enemies = []


def create_bonus():
    bonus_size = (30, 30)
    bonus = pygame.transform.scale(pygame.image.load(
        'bonus.png').convert_alpha(), (90, 150))
    # bonus = pygame.Surface(bonus_size)
    # bonus.fill(COLOR_GREEN)
    bonus_rect = pygame.Rect(random.randint(200, 1000), 0,  *bonus_size)
    bonus_move = [0, random.randint(4, 8)]
    return [bonus, bonus_rect, bonus_move]


CREATE_BONUS = pygame.USEREVENT + 2  # cоздаем собитие - event CREATE_BONUS
pygame.time.set_timer(CREATE_BONUS, 3000)  # собитие и промежуток времени

CHANGE_IMAGE = pygame.USEREVENT + 3
pygame.time.set_timer(CHANGE_IMAGE, 200)

bonuses = []

score = 0
image_index = 0

playing = True
while playing:
    FPS.tick(120)
    for event in pygame.event.get():
        if event.type == QUIT:
            playing = False
        if event.type == CREATE_ENEMY:
            enemies.append(create_enemy())
        if event.type == CREATE_BONUS:
            bonuses.append(create_bonus())
        if event.type == CHANGE_IMAGE:
            player = pygame.image.load(os.path.join(IMAGE_PATH, PLAYER_IMAGES[
                image_index]))
            image_index += 1
            if image_index >= len(PLAYER_IMAGES):
                image_index = 0


    bg_X1 -= bg_move
    bg_X2 -= bg_move

    if bg_X1 < -bg.get_width():
        bg_X1 = bg.get_width()

    if bg_X2 < -bg.get_width():
        bg_X2 = bg.get_width()

    # main_display.fill(COLOR_BLACK)  # фон був
    main_display.blit(bg, (bg_X1, 0))
    main_display.blit(bg, (bg_X2, 0))  # фон стал
    # щоб зрозуміти яка клавіша натиснута на момент кожної ітерації
    # використовується  знову ж таки список
    keys = pygame.key.get_pressed()

    if keys[K_RIGHT] and player_rect.right < WIDTH:
        player_rect = player_rect.move(player_move_right)

    if keys[K_DOWN] and player_rect.bottom < HEIGT:
        player_rect = player_rect.move(player_move_down)

    if keys[K_UP] and player_rect.top > 0:
        player_rect = player_rect.move(player_move_up)

    if keys[K_LEFT] and player_rect.left > 0:
        player_rect = player_rect.move(player_move_left)

    for enemy in enemies:   # расположение врагов
        enemy[1] = enemy[1].move(enemy[2])
        main_display.blit(enemy[0], enemy[1])

        if player_rect.colliderect(enemy[1]):
            playing = False


    for bonus in bonuses:   # расположение бонусов
        bonus[1] = bonus[1].move(bonus[2])
        main_display.blit(bonus[0], bonus[1])

        if player_rect.colliderect(bonus[1]):
            score += 1
            bonuses.pop(bonuses.index(bonus))
    # enemy_rect = enemy_rect.move(enemy_move)

    #     if player_rect.bottom >= HEIGT:    # Первый способ изменения направления
    #         player_speed = random.choice(([1, -1], [-1, -1]))
    #     # if player_rect.bottom >= HEIGT:      # Второй способ изменения направления
    #     #     player_speed[1] = -player_speed[1]   # напраление можно менять пользуясь индексами списка
    #     if player_rect.right >= WIDTH:
    #         player_speed = random.choice(([-1, -1], [-1, 1]))
    # # При первом способе изменения направления может быть зависание объекта!!!!!!
    # #     if player_rect.right >= WIDTH:
    # #         player_speed[0] = -player_speed[0]
    #     if player_rect.top < 0:
    #         player_speed = random.choice(([1, 1], [-1, 1]))
    #     # if player_rect.top < 0:      # Второй способ изменения направления
    #     #     player_speed[1] = -player_speed[1]
    #     if player_rect.left < 0:
    #         player_speed = random.choice(([1, -1], [1, 1]))
    #     # if player_rect.left < 0:      # Второй способ изменения направления
    #     #     player_speed[0] = -player_speed[0]

    #  print(player_rect.bottom)
    main_display.blit(FONT.render(str(score), True, COLOR_WHITE,
                                  COLOR_ORANGE), (WIDTH-50, 20))
    main_display.blit(player, player_rect)
    # main_display.blit(enemy, enemy_rect)
    # print(len(enemies))
    # print(len(bonuses))
    # player_rect = player_rect.move(player_speed)
    pygame.display.flip()

    for enemy in enemies:  # удалить лишних врагов
        if enemy[1].left < 0:
            enemies.pop(enemies.index(enemy))

    for bonus in bonuses:  # удалить лишних врагов
        if bonus[1].bottom > HEIGT:
            bonuses.pop(bonuses.index(bonus))


