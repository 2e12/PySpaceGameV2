from object import Object
import random


class GameField:
    size = None
    objects = []

    def __init__(self, field_size):
        self.objects = []
        self.size = field_size
        self.generate(int((self.size[0] / self.size[1]) * 13))

    def generate(self, amount):
        for i in range(amount):
            self.objects.append(self.create_object(self.size[1] + 300))

    def is_colliding(self, player):
        i = 0
        while i < len(self.objects):
            if self.objects[i].collide:
                if self.objects[i].pos[1] + self.objects[i].size[1] > player.pos[1] and self.objects[i].pos[1] - self.objects[i].size[1] < player.pos[1]:
                    if (self.objects[i].pos[0] < player.pos[0] + player.size[0]) & (self.objects[i].pos[0] +
                                                                                    self.objects[i].size[0] >
                                                                                    player.pos[0]):
                        self.objects[i].collide = False
                        return True
            i += 1
        return False

    def create_object(self, offset):
        x = random.randint(0, self.size[0] - Object.size[0])
        y = random.randint(0, self.size[1]) - offset
        speed = random.randint(7, 10) / 10
        color = [200, 0, 0]
        obj = Object([x, y], speed, color)
        return obj

    def update(self, speed, gameover):
        i = 0
        while i < len(self.objects):
            self.objects[i].update(speed)
            if self.objects[i].pos[1] > self.size[1]:
                if not gameover:
                    self.objects[i] = self.create_object(0)
                    self.objects[i].pos[1] = 0 - self.objects[i].size[1]
                else:
                    self.objects[i].pos[1] = self.size[1]
            i += 1

    def render(self, screen):
        i = 0
        while i < len(self.objects):
            self.objects[i].render(screen)
            i += 1
