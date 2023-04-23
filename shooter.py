import pygame
import random

# initialize pygame
pygame.init()

# set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Shooting Game")

# set up the clock
clock = pygame.time.Clock()

# define colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# set up the player
player_width = 50
player_height = 50
player_x = screen_width // 2 - player_width // 2
player_y = screen_height - player_height - 10
player_speed = 5
player = pygame.Rect(player_x, player_y, player_width, player_height)

# set up the bullet
bullet_width = 10
bullet_height = 30
bullet_speed = 10
bullet_list = []

# set up the enemy
enemy_width = 50
enemy_height = 50
enemy_speed = 3
enemy_list = []

# set up the score
score = 0
font = pygame.font.SysFont(None, 30)

# game loop
game_over = False
while not game_over:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # fire a bullet
                bullet_x = player_x + player_width // 2 - bullet_width // 2
                bullet_y = player_y - bullet_height
                bullet_list.append(pygame.Rect(bullet_x, bullet_y, bullet_width, bullet_height))

    # handle input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.left > 0:
        player.left -= player_speed
    elif keys[pygame.K_RIGHT] and player.right < screen_width:
        player.right += player_speed

    # move bullets
    for bullet in bullet_list:
        bullet.top -= bullet_speed

    # move enemies and check for collision
    for enemy in enemy_list:
        enemy.top += enemy_speed
        if enemy.colliderect(player):
            game_over = True
        for bullet in bullet_list:
            if enemy.colliderect(bullet):
                bullet_list.remove(bullet)
                enemy_list.remove(enemy)
                score += 1

    # spawn enemies
    if len(enemy_list) < 10 and random.randint(1, 50) == 1:
        enemy_count = random.randint(1, 5)
        for i in range(enemy_count):
            enemy_x = random.randint(0, screen_width - enemy_width)
            enemy_y = -enemy_height
            enemy_list.append(pygame.Rect(enemy_x, enemy_y, enemy_width, enemy_height))

    # draw screen
    screen.fill(white)
    for bullet in bullet_list:
        pygame.draw.rect(screen, black, bullet)
    for enemy in enemy_list:
        pygame.draw.rect(screen, red, enemy)
    pygame.draw.rect(screen, black, player)
    score_text = font.render("Score: " + str(score), True, black)
    screen.blit(score_text, (10, 10))
    pygame.display.update()

    # set up the clock
    clock.tick(60)

# quit pygame
pygame.quit()
