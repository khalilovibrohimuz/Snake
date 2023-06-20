import pygame
pygame.init()


SCALE = 100
WIDTH = pygame.display.get_desktop_sizes()[0][0] * SCALE // 100
HEIGHT = pygame.display.get_desktop_sizes()[0][1] * SCALE // 100
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2
displey = pygame.display.set_mode((WIDTH, HEIGHT), pygame.SCALED | pygame.FULLSCREEN)


PLAYGROUND_SIZE = (1280, 800)
MARGIN = HALF_HEIGHT - PLAYGROUND_SIZE[1] // 2
FONT_SCORE = pygame.font.Font('source/assets/font/courier.ttf', 40)
FONT_GAME_OVER = pygame.font.Font('source/assets/font/ethnocentric.ttf', 120)


COLOR_WHITE = (255, 255, 255, 255)
COLOR_BLACK = (0, 0, 0, 255)
COLOR_BACKGROUND = (80, 160, 100, 255)
COLOR_PLAYGROUND = (200, 180, 140, 255)
COLOR_TEXT = (255, 255, 0, 255)
COLOR_FOOD = (255, 60, 80, 255)
