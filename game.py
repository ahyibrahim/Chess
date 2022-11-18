from re import T
import pygame

DISPLAY_HEIGHT = 800
DISPLAY_WIDTH = 800
TILE_SIZE = DISPLAY_WIDTH/8
WHITE_TILE = (239, 218, 180)
BLACK_TILE = (181, 135, 98)
COLUMNS = 'a b c d e f g h'
COLUMNS = COLUMNS.split()

(success, fail) = pygame.init()
pygame.display.set_caption('Chess')
surface = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
surface.fill(BLACK_TILE)
font = pygame.font.SysFont("freesanbold.ttf", 26)
row_counter = 8

for horizontal_tile in range(0, DISPLAY_HEIGHT, int(TILE_SIZE)):
    if (horizontal_tile/100) % 2 == 0:
        start = 0
        text_color = WHITE_TILE
    else:
        start = 100
        text_color = BLACK_TILE

    for vertical_tile in range(start, DISPLAY_WIDTH, int(TILE_SIZE)*2):
        pygame.draw.rect(surface, WHITE_TILE, pygame.Rect(
            vertical_tile, horizontal_tile, 100, 100))

    text = font.render(str(row_counter), True, text_color)
    text_rect = text.get_rect()
    text_rect.center = (DISPLAY_WIDTH - (TILE_SIZE * 0.07),
                        horizontal_tile + (TILE_SIZE * 0.1))
    surface.blit(text, text_rect)
    row_counter -= 1

for i, column in enumerate(COLUMNS):
    if i % 2 == 0:
        text_color = WHITE_TILE
    else:
        text_color = BLACK_TILE

    text = font.render(column, True, text_color)
    text_rect = text.get_rect()
    text_rect.center = ((DISPLAY_WIDTH/8) * i +
                        (TILE_SIZE * 0.07), DISPLAY_HEIGHT - (TILE_SIZE * 0.1))
    surface.blit(text, text_rect)


pygame.display.flip()

running = True
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
