# Ctrl + Shift + P, then select interpreter
# Choose an interpreter that works
import pygame

# Media files
player_image = pygame.image.load('si-player.gif')

pygame.init()
clock = pygame.time.Clock()
game_display = pygame.display.set_mode((400, 600))
score_font = pygame.font.SysFont('Arial', 22, True)
title_font = pygame.font.SysFont('Arial', 26, True)
pygame.display.set_caption('SPACE INVADERS!')

x_coordinate = 200
y_coordinate = 575
should_move_right = False
should_move_left = False


def handle_events():
    global x_coordinate, y_coordinate, is_playing, should_move_left, should_move_right
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_playing = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                should_move_left = True
                should_move_right = False
            elif event.key == pygame.K_RIGHT:
                should_move_right = True
                should_move_left = False
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    should_move_left = False
                if event.key == pygame.K_RIGHT:
                    should_move_right = False


# Main Game Loop
is_playing = True
while is_playing:

    handle_events()

    if should_move_right:
        x_coordinate += 10
    elif should_move_left:
        x_coordinate -= 10

    game_display.blit(game_display, (0, 0))

    game_display.fill((0, 0, 0))
    game_display.blit(player_image, (x_coordinate, y_coordinate))
    #score_text = score_font.render(str(snake.score), False, WHITE)
    #game_display.blit(score_text, (0,0))

    pygame.display.update()

    clock.tick(30)

pygame.display.quit()
pygame.quit
