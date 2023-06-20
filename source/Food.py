from random import randint
from source.const import *


class Food:
    def __init__(self, tile, tiles, head, middles):
        self.TILE = tile
        self.TILES = tiles
        self.pos_x = 0
        self.pos_y = 0
        self.random(head, middles)
        self.eat_position = []
        self.condition = self.TILE // 3
        self.up = True

    def draw(self):
        pygame.draw.circle(displey, COLOR_FOOD, (MARGIN + self.pos_x * self.TILE + self.TILE // 2, MARGIN + self.pos_y * self.TILE + self.TILE // 3 + self.condition), self.TILE // 3, 0)
        pygame.draw.circle(displey, COLOR_WHITE, (MARGIN + self.pos_x * self.TILE + self.TILE // 2 + self.TILE // 8, MARGIN + self.pos_y * self.TILE + self.condition + self.TILE // 5), self.TILE // 10, 0)

    def random(self, head, middles):
        empty = []
        for x in range(self.TILES[0]):
            for y in range(self.TILES[1]):
                empty.append((x, y))
                if head.pos_x == x and head.pos_y == y:
                    del empty[-1]
                for i in range(len(middles)):
                    if middles[i].pos_x == x and middles[i].pos_y == y:
                        try:
                            del empty[-1]
                        except:
                            continue
        if len(empty) == 0:
            self.pos_x = -10
            self.pos_y = -10
        else:
            choice = randint(0, len(empty) - 1)
            self.pos_x = empty[choice][0]
            self.pos_y = empty[choice][1]
        empty.clear()

    def run(self):
        if self.up:
            if self.condition < self.TILE // 3:
                self.condition += 1
            else:
                self.up = False
        else:
            if self.condition >= 0:
                self.condition -= 1
            else:
                self.up = True
