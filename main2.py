import pygame

class Ball():
    def __init__(self, x_pos, y_pos, x_vel, y_vel, radius, win):     #I can remove if too long
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.x_vel = x_vel
        self.y_vel = y_vel
        self.radius = radius
        self.win = win
        self.timer = 0

    def draw(self):
        pygame.draw.circle(self.win, (255, 255, 255), (self.x_pos, self.y_pos), self.radius)

    def move(self):
        #ball hit wall
        if self.x_pos >= 495 or self.x_pos <= 5:
            self.x_vel *= -1
        if self.y_pos >= 495 or self.y_pos <= 5:
            self.y_vel *= -1

        #friction
        self.timer += 1
        if self.timer == 60:
            if self.y_vel > 0:
                self.y_vel -= 1
                if self.y_vel < 0:
                    self.y_vel = 0
            elif self.y_vel < 0:
                self.y_vel += 1
                if self.y_vel > 0:
                    self.y_vel = 0
            self.timer = 0

        #vel of ball
        self.x_pos += self.x_vel
        self.y_pos += self.y_vel
    


class Game():
    def __init__(self, width, height):   #We dont need to  keep balls or score, both start at 0
        self.balls = []
        self.score = 0
        self.width = width
        self.height = height
        pygame.init()
        self.win = pygame.display.set_mode((width, height))
        self.run()

    def run(self):
        run = True
        ball = Ball(250, 250, 5, 3, 5, self.win)
        while run:
            pygame.time.delay(50)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            self.win.fill((0, 0, 0))
            ball.draw()
            ball.move()
            pygame.display.update()

Game(500, 500)

