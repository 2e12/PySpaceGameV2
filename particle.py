import pygame


class Particle:
    pos = [0, 0]
    speed = 1
    color = [160, 160, 160]

    def __init__(self, pos, speed, color):
        self.pos = pos
        self.speed = speed
        self.color = color
        i = 0;
        while i < len(self.color):
            self.color[i] = self.color[i] * self.speed
            i += 1

    def update(self, time):
        self.pos[1] = self.pos[1] + self.speed * time

    def render(self, screen):
        pygame.draw.rect(screen, self.color,
                         (self.pos[0], self.pos[1], 2, 6),
                         0)
