from source.const import *


class Head:
    def __init__(self, tile, tiles, pos, step, angle):
        self.TILE = tile
        self.TILES = tiles
        self.pos_x = pos[0]
        self.pos_y = pos[1]
        self.step = step
        self.angle = angle
        self.rotate = True
        self.remember = 'none'
        self.init_control = True
        self.rotated = 0
        self.update()
        self.goal = 'forward'
        self.image = 0

    def run(self):
        self.forward()
        self.update()

    def update(self):
        if self.pos_x >= self.TILES[0]:
            self.pos_x = 0
        if self.pos_x < 0:
            self.pos_x = self.TILES[0] - 1
        if self.pos_y >= self.TILES[1]:
            self.pos_y = 0
        if self.pos_y < 0:
            self.pos_y = self.TILES[1] - 1
        if self.angle == 'north':
            self.rotated = 0
        if self.angle == 'west':
            self.rotated = 90
        if self.angle == 'south':
            self.rotated = 180
        if self.angle == 'east':
            self.rotated = 270
        if self.step == 'right':
            self.step = 'left'
        else:
            self.step = 'right'
        self.image = pygame.transform.scale(pygame.image.load(f'source/assets/picture/snake/headforward{self.step}.png'), (self.TILE, self.TILE))
        self.image = pygame.transform.rotate(self.image, self.rotated)
        self.goal = 'forward'

    def draw(self):
        displey.blit(self.image, (MARGIN + self.pos_x * self.TILE, MARGIN + self.pos_y * self.TILE))

    def forward(self):
        if self.angle == 'east':
            self.pos_x += 1
        if self.angle == 'west':
            self.pos_x -= 1
        if self.angle == 'south':
            self.pos_y += 1
        if self.angle == 'north':
            self.pos_y -= 1
        if self.remember != 'none':
            self.angle = self.remember
            self.remember = 'none'
            self.init_control = True
        self.rotate = True
