from object import Object


class Player(Object):
    move_left = False
    move_right = False

    def __init__(self, pos, color):
        super().__init__(pos, 1, color)

    def update(self, time, width):
        side_offset = 35
        if self.move_left and self.pos[0] > side_offset:
            self.pos[0] -= time
        if self.move_right and self.pos[0] + self.size[0] < width - side_offset:
            self.pos[0] += time
