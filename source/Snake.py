from source import Head
from source import Body


class Snake:
    def __init__(self, tile, tiles, pos, step, angle):
        self.TILE = tile
        self.TILES = tiles
        self.pos = pos
        self.step = step
        self.angle = angle
        self.head = Head.Head(self.TILE, self.TILES, self.pos, self.step, self.angle)
        self.middles = []
        for a in range(2):
            if len(self.middles) > 0:
                self.middles.append(Body.Body(self.TILE, self.TILES, self.middles[len(self.middles) - 1].step))
            else:
                self.middles.append(Body.Body(self.TILE, self.TILES, self.head.step))
            for i in range(len(self.middles))[::-1]:
                if i == 0:
                    self.middles[i].pos_x = self.head.pos_x
                    self.middles[i].pos_y = self.head.pos_y
                    self.middles[i].rotated = self.head.rotated
                    self.middles[i].step = self.head.step
                    self.middles[i].goal = self.head.goal
                else:
                    self.middles[i].pos_x = self.middles[i - 1].pos_x
                    self.middles[i].pos_y = self.middles[i - 1].pos_y
                    self.middles[i].rotated = self.middles[i - 1].rotated
                    self.middles[i].step = self.middles[i - 1].step
                    self.middles[i].goal = self.middles[i - 1].goal
            self.head.run()

    def draw(self):
        for i in range(len(self.middles)):
            self.middles[i].draw(i == len(self.middles) - 1)
        self.head.draw()

    def left(self):
        if self.head.angle == 'north' or self.head.angle == 'south':
            if self.head.rotate:
                if self.head.angle == 'north':
                    self.head.goal = 'left'
                if self.head.angle == 'south':
                    self.head.goal = 'right'
                self.head.angle = 'west'
                self.head.rotate = False
                if self.head.init_control:
                    self.head.remember = 'west'
                    self.head.init_control = False

    def right(self):
        if self.head.angle == 'north' or self.head.angle == 'south':
            if self.head.rotate:
                if self.head.angle == 'north':
                    self.head.goal = 'right'
                if self.head.angle == 'south':
                    self.head.goal = 'left'
                self.head.angle = 'east'
                self.head.rotate = False
                if self.head.init_control:
                    self.head.remember = 'east'
                    self.head.init_control = False

    def up(self):
        if self.head.angle == 'east' or self.head.angle == 'west':
            if self.head.rotate:
                if self.head.angle == 'east':
                    self.head.goal = 'left'
                if self.head.angle == 'west':
                    self.head.goal = 'right'
                self.head.angle = 'north'
                self.head.rotate = False
                if self.head.init_control:
                    self.head.remember = 'north'
                    self.head.init_control = False

    def down(self):
        if self.head.angle == 'east' or self.head.angle == 'west':
            if self.head.rotate:
                if self.head.angle == 'east':
                    self.head.goal = 'right'
                if self.head.angle == 'west':
                    self.head.goal = 'left'
                self.head.angle = 'south'
                self.head.rotate = False
                if self.head.init_control:
                    self.head.remember = 'south'
                    self.head.init_control = False
