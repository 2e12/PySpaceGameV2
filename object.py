import pygame


class Object:
    pos = [0, 0]
    size = [50, 50]
    speed = 1
    color = [160, 160, 160]

    def __init__(self, pos, speed, color):
        self.pos = pos
        self.speed = speed
        self.color = color
        self.collide = True
        i = 0
        while i < len(self.color):
            color = self.color[i] * self.speed
            if color > 255:
                color = 255
            self.color[i] = color
            i += 1

    def update(self, time):
        self.pos[1] = self.pos[1] + self.speed * time

    def render(self, screen):
        pygame.draw.rect(screen, self.color,
                         (self.pos[0], self.pos[1], self.size[0], self.size[1]),
                         0)
