# Ctrl + Shift + P, then select interpreter
# Choose an interpreter that works
import pygame
from hero import Hero
from enemy import Enemy
from fleet import Fleet

# Game settings
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 600
GAME_SIDE_MARGIN = 20
GAME_TOP_MARGIN = 20
GAME_BOTTOM_MARGIN = 20
GAME_BORDER_WIDTH = 3

GAME_TOP_WALL = GAME_TOP_MARGIN + GAME_BORDER_WIDTH
GAME_RIGHT_WALL = WINDOW_WIDTH - GAME_SIDE_MARGIN - GAME_BORDER_WIDTH
GAME_BOTTOM_WALL = WINDOW_HEIGHT - GAME_BOTTOM_MARGIN - GAME_BORDER_WIDTH
GAME_LEFT_WALL = GAME_SIDE_MARGIN + GAME_BORDER_WIDTH

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Media files
player_image = pygame.image.load('media/si-player.gif')
bullet_image = pygame.image.load('media/si-bullet.gif')
enemy_image = pygame.image.load('media/si-enemy.gif')

pygame.init()
clock = pygame.time.Clock()
game_display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
score_font = pygame.font.SysFont('Arial', 22, True)
title_font = pygame.font.SysFont('Arial', 26, True)
pygame.display.set_caption('SPACE INVADERS!')


def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            hero.is_alive = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                hero.set_direction_left()
            elif event.key == pygame.K_RIGHT:
                hero.set_direction_right()
            elif event.key == pygame.K_SPACE:
                hero.shoot(bullet_image)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                hero.set_direction_none()
            elif event.key == pygame.K_RIGHT:
                hero.set_direction_none()


hero = Hero(player_image, 200, GAME_BOTTOM_WALL - player_image.get_height())

fleet = Fleet(3, 5, 4, enemy_image, GAME_LEFT_WALL + 1, GAME_TOP_WALL + 1)

# Main Game Loop
while hero.is_alive:

    handle_events()

    hero.move(GAME_LEFT_WALL, GAME_RIGHT_WALL)

    fleet.handle_wall_collision(GAME_LEFT_WALL, GAME_RIGHT_WALL)

    fleet.move_over(GAME_LEFT_WALL, GAME_RIGHT_WALL)

    game_display.blit(game_display, (0, 0))

    game_display.fill(BLACK)

    pygame.draw.rect(game_display, WHITE,
                     (GAME_SIDE_MARGIN, GAME_TOP_MARGIN,
                      WINDOW_WIDTH - GAME_SIDE_MARGIN * 2,
                      WINDOW_HEIGHT - GAME_BOTTOM_MARGIN * 2))

    pygame.draw.rect(game_display, BLACK,
                     (GAME_LEFT_WALL, GAME_TOP_WALL,
                      WINDOW_WIDTH - GAME_LEFT_WALL - GAME_SIDE_MARGIN - GAME_BORDER_WIDTH,
                      WINDOW_HEIGHT - GAME_TOP_WALL - GAME_BOTTOM_MARGIN - GAME_BORDER_WIDTH))

    hero.show(game_display)
    fleet.show(game_display)

    for bullet in hero.bullets_fired:
        if bullet.has_collided_with_top_wall(GAME_TOP_WALL):
            bullet.is_alive = False

    hero.remove_dead_bullets()

    for bullet in hero.bullets_fired:
        bullet.move()
        bullet.show(game_display)

    # score_text = score_font.render(str(snake.score), False, WHITE)
    # game_display.blit(score_text, (0,0))

    pygame.display.update()

    clock.tick(30)

pygame.display.quit()
pygame.quit
