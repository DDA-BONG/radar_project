import random

class Target:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

        # 속도 반드시 초기화
        self.vx = random.randint(-3, 3)
        self.vy = random.randint(-3, 3)

    def move(self):
        self.x += self.vx
        self.y += self.vy

    def position(self):
        return (self.x, self.y)