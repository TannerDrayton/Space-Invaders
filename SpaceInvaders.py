# Ctrl + Shift + P, then select interpreter
# Choose an interpreter that works
import pygame

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

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Media files
player_image = pygame.image.load('si-player.gif')

pygame.init()
clock = pygame.time.Clock()
game_display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
score_font = pygame.font.SysFont('Arial', 22, True)
title_font = pygame.font.SysFont('Arial', 26, True)
pygame.display.set_caption('SPACE INVADERS!')

x_coordinate = 200
y_coordinate = GAME_BOTTOM_WALL - player_image.get_height()
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
                elif event.key == pygame.K_RIGHT:
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

    game_display.fill(BLACK)

    pygame.draw.rect(game_display, WHITE,
                     (GAME_SIDE_MARGIN, GAME_TOP_MARGIN,
                      WINDOW_WIDTH - GAME_SIDE_MARGIN * 2,
                      WINDOW_HEIGHT - GAME_BOTTOM_MARGIN * 2))

    pygame.draw.rect(game_display, BLACK,
                     (GAME_LEFT_WALL, GAME_TOP_WALL,
                      WINDOW_WIDTH - GAME_LEFT_WALL - GAME_SIDE_MARGIN - GAME_BORDER_WIDTH,
                      WINDOW_HEIGHT - GAME_TOP_WALL - GAME_BOTTOM_MARGIN - GAME_BORDER_WIDTH))

    game_display.blit(player_image, (x_coordinate, y_coordinate))
    # score_text = score_font.render(str(snake.score), False, WHITE)
    # game_display.blit(score_text, (0,0))

    pygame.display.update()

    clock.tick(30)

pygame.display.quit()
pygame.quit
