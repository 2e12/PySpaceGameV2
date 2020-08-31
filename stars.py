from particle import Particle
import random


class Stars:
    size = None
    particles = []

    def __init__(self, filed_size):
        self.particles = []
        self.size = filed_size
        self.generate(int((self.size[0] / self.size[1]) * 100))

    def generate(self, amount):
        for i in range(amount):
            self.particles.append(self.create_particle())

    def create_particle(self):
        x = random.randint(0, self.size[0])
        y = random.randint(0, self.size[1])
        speed = random.randint(3, 10) / 10
        color = [random.randint(100, 240), random.randint(100, 240), random.randint(100, 240)]
        particle = Particle([x, y], speed, color)
        return particle

    def update(self, speed):
        i = 0
        while i < len(self.particles):
            self.particles[i].update(speed)

            if self.particles[i].pos[1] > self.size[1]:
                self.particles[i] = self.create_particle()
                self.particles[i].pos[1] = 0
            i += 1

    def render(self, screen):
        i = 0
        while i < len(self.particles):
            self.particles[i].render(screen)
            i += 1
