import pygame
import time
from stars import Stars
from gamethread import GameThread
from gamefield import GameField
from player import Player


class Game:
    size = None
    screen = None
    star_background = None
    game_field = None
    game_speed = 1
    game_thread = None
    player = None
    fps = 60
    frame_rate_counter = 0
    actual_frame_rate = 0
    running = True
    gameover = False
    waiting = True
    font = None
    padding = 20
    score = 0
    random_color = [255, 0, 0]
    milestone = 2000
    hit = 0
    highscore = 0

    def __init__(self, size):
        self.size = size
        pygame.font.init()
        self.score = 0
        self.star_background = Stars(self.size)
        self.font = pygame.font.Font("res/font.ttf", 28)
        self.screen = pygame.display.set_mode(size)
        if not self.gameover:
            self.new_game()
        self.game_thread = GameThread(self)
        self.game_thread.start()
        self.loop()

    def new_game(self):
        self.running = True
        self.waiting = True
        self.gameover = False
        self.milestone = 2000
        self.game_speed = 1
        self.lives = 4
        self.game_field = GameField(self.size)
        self.player = Player([self.size[0] / 2 - Player.size[0] / 2, self.size[1] - 80], [255, 255, 255])

    def draw_score(self):
        fps = self.font.render("x" + str(round(self.game_speed, 2)), False, (255, 255, 255))
        self.screen.blit(fps, (self.padding, self.padding))
        lives = self.font.render(str(self.lives) + " Lives", False, (255, 255, 255))
        self.screen.blit(lives, (self.size[0] - lives.get_width() - self.padding, self.padding))
        score = self.font.render(str(int(self.score)), False, (255, 255, 100))
        self.screen.blit(score, ((self.size[0] / 2) - score.get_width() / 2, self.padding))
        if self.waiting:
            start = self.font.render("Press any key to start", False, self.random_color)
            self.screen.blit(start, ((self.size[0] / 2) - start.get_width() / 2, (self.size[1] - start.get_height()) - self.padding - 140))

            highscore = self.font.render("Highscore: " + str(int(self.highscore)), False, (255, 255, 255))
            self.screen.blit(highscore, ((self.size[0] / 2) - highscore.get_width() / 2, self.padding + self.size[1] / 2))

    def render_game(self):
        self.star_background.render(self.screen)
        self.game_field.render(self.screen)
        self.player.render(self.screen)
        self.draw_score()

    def update_score(self):
        if not self.gameover:
            self.score += self.game_speed * 50
        if self.score > self.highscore:
            self.highscore = self.score

    def game_over_animation(self):
        if self.game_speed > 1:
            self.game_speed -= 0.01
        if self.player.pos[1] < self.size[1]:
            self.player.pos[1] += 0.5
        else:
            new = True
            for obj in self.game_field.objects:
                if obj.pos[1] < self.size[1]:
                    new = False
            if new:
                self.new_game()

    def update_game(self):
        self.star_background.update(2 * self.game_speed)

        if self.score > self.milestone and not self.waiting:
            self.milestone += 3500 * self.game_speed + 1
            print(self.milestone)
            self.game_speed += 0.5

        if not self.waiting:
            self.game_field.update(4 * self.game_speed, self.gameover)
            if self.lives <= 0:
                self.gameover = True

            if self.game_field.is_colliding(self.player):
                if not self.lives <= 0:
                    self.lives -= 1
                    self.hit = 10
            self.player.update(4 * self.game_speed, self.size[0])

    def event_handling(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if not self.waiting:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.player.move_left = True
                    if event.key == pygame.K_RIGHT:
                        self.player.move_right = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.player.move_left = False
                    if event.key == pygame.K_RIGHT:
                        self.player.move_right = False
            if self.waiting:
                if event.type == pygame.KEYDOWN:
                    self.score = 0
                    self.game_speed = 1
                    self.waiting = False

    def loop(self):
        while self.running:
            self.frame_rate_counter += 1
            if self.hit == 0:
                self.screen.fill((0, 0, 0))
            else:
                self.screen.fill(self.random_color)
            self.render_game()
            pygame.display.flip()

