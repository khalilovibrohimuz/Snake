from time import time as current_time
from source.const import *
from source import Snake
from source import Body
from source import Food


class Game:
    def __init__(self):
        self.playing = True
        self.TILE = 80  # min = 20, max = 200
        self.TILES = (PLAYGROUND_SIZE[0] // self.TILE, PLAYGROUND_SIZE[1] // self.TILE)
        self.active = False
        self.speed = 4
        self.music = pygame.mixer.Sound("source/assets/audio/music/theme short.mp3")
        self.score = 0
        self.delay = 0
        self.snake = Snake.Snake(self.TILE, self.TILES, (self.TILES[0] // 2 - 1, self.TILES[1] // 2), 'right', 'east')
        self.food = Food.Food(self.TILE, self.TILES, self.snake.head, self.snake.middles)

    def start(self):
        self.music.play(-1)
        while self.playing:
            self.run()
            pygame.display.flip()
            pygame.time.Clock().tick(60)
            displey.fill(COLOR_BACKGROUND)

    def run(self):
        self.control()
        self.food.run()

        if self.active and current_time() >= self.delay:
            if self.TILES[0] * self.TILES[1] <= len(self.snake.middles):
                self.game_over("win")
            for i in range(len(self.snake.middles))[::-1]:
                if self.snake.middles[i].pos_x == self.snake.head.pos_x and self.snake.middles[i].pos_y == self.snake.head.pos_y:
                    self.game_over('lose')
            i = 0
            while i < len(self.food.eat_position):
                if self.food.eat_position[i][0] == self.snake.middles[-1].pos_x and self.food.eat_position[i][1] == \
                        self.snake.middles[-1].pos_y:
                    self.snake.middles.append(Body.Body(self.TILE, self.TILES, self.snake.middles[len(self.snake.middles) - 1].step))
                    del self.food.eat_position[i]
                i += 1
            for i in range(len(self.snake.middles))[::-1]:
                if i == 0:
                    self.snake.middles[i].pos_x = self.snake.head.pos_x
                    self.snake.middles[i].pos_y = self.snake.head.pos_y
                    self.snake.middles[i].rotated = self.snake.head.rotated
                    self.snake.middles[i].step = self.snake.head.step
                    self.snake.middles[i].goal = self.snake.head.goal
                else:
                    self.snake.middles[i].pos_x = self.snake.middles[i - 1].pos_x
                    self.snake.middles[i].pos_y = self.snake.middles[i - 1].pos_y
                    self.snake.middles[i].rotated = self.snake.middles[i - 1].rotated
                    self.snake.middles[i].step = self.snake.middles[i - 1].step
                    self.snake.middles[i].goal = self.snake.middles[i - 1].goal
            self.delay = current_time() + 0.060 * self.speed
            self.snake.head.run()
            if self.snake.head.pos_x == self.food.pos_x and self.snake.head.pos_y == self.food.pos_y:
                self.score += 11 - self.speed
                self.food.eat_position.append((self.food.pos_x, self.food.pos_y))
                self.food.random(self.snake.head, self.snake.middles)

        self.draw_game()

    def control(self):
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                self.playing = False
                self.music.stop()
            if ev.type == pygame.KEYDOWN:
                self.active = True
                if ev.key == pygame.K_ESCAPE:
                    self.game_over('lose')
                if ev.key == pygame.K_LEFT or ev.key == pygame.K_a or ev.key == pygame.K_KP_4:
                    self.snake.left()
                if ev.key == pygame.K_RIGHT or ev.key == pygame.K_d or ev.key == pygame.K_KP_6:
                    self.snake.right()
                if ev.key == pygame.K_UP or ev.key == pygame.K_w or ev.key == pygame.K_KP_8:
                    self.snake.up()
                if ev.key == pygame.K_DOWN or ev.key == pygame.K_s or ev.key == pygame.K_KP_5:
                    self.snake.down()

    def game_over(self, status):
        label = 0
        self.music.fadeout(2400)
        if status == 'win':
            label = FONT_GAME_OVER.render("YOU WIN!", True, COLOR_TEXT)
        elif status == 'lose':
            label = FONT_GAME_OVER.render("GAME OVER!", True, COLOR_TEXT)
        score = FONT_GAME_OVER.render(str(self.score), True, COLOR_TEXT)
        for y in range(HEIGHT + label.get_height(), HALF_HEIGHT - label.get_height() // 2, -4):
            for keyDown in pygame.event.get():
                if keyDown.type == pygame.QUIT:
                    break
            displey.fill(COLOR_BACKGROUND)
            displey.blit(label, (HALF_WIDTH - label.get_width() // 2, y - label.get_height() // 2))
            displey.blit(score, (HALF_WIDTH - score.get_width() // 2, y + label.get_height() // 2))
            pygame.display.flip()
        for i in range(24):
            for keyDown in pygame.event.get():
                if keyDown.type == pygame.QUIT:
                    break
            pygame.time.delay(60)
        exit()

    def draw_game(self):
        pygame.draw.rect(displey, COLOR_PLAYGROUND, (MARGIN, MARGIN, PLAYGROUND_SIZE[0], PLAYGROUND_SIZE[1]))
        self.food.draw()
        self.snake.draw()
        text = FONT_SCORE.render('Score:', True, COLOR_TEXT)
        show_score = FONT_SCORE.render(str(self.score), True, COLOR_TEXT)
        displey.blit(text, (WIDTH - MARGIN - text.get_width(), MARGIN))
        displey.blit(show_score, (WIDTH - MARGIN - show_score.get_width(), MARGIN + 40))
