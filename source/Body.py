from source.const import *


class Body:
    def __init__(self, tile, tiles, step):
        self.TILE = tile
        self.TILES = tiles
        self.pos_x = 0
        self.pos_y = 0
        self.rotated = 0
        self.goal = 'forward'
        self.step = step
        self.image = 0

    def draw(self, index):
        if index:
            self.image = pygame.transform.scale(pygame.image.load(f'source/assets/picture/snake/end{self.goal}{self.step}.png'), (self.TILE, self.TILE))
        else:
            self.image = pygame.transform.scale(pygame.image.load(f'source/assets/picture/snake/mid{self.goal}{self.step}.png'), (self.TILE, self.TILE))
        self.image = pygame.transform.rotate(self.image, self.rotated)
        displey.blit(self.image, (MARGIN + self.pos_x * self.TILE, MARGIN + self.pos_y * self.TILE))
