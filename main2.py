import pygame
from math import sqrt

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
        if self.timer == 60: #the problem is here
            if self.y_vel > 1:
                self.y_vel -= 1
                if self.y_vel < 1:
                    self.y_vel = 1
            elif self.y_vel < 1:
                self.y_vel += 1
                if self.y_vel > 1:
                    self.y_vel = 1
            self.timer = 1

        #vel of ball
        self.x_pos += self.x_vel
        self.y_pos += self.y_vel
    

class Paddle():
    def __init__(self, x_pos, y_pos, win):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.x_vel = 0
        self.y_vel = 0
        self.win = win
        self.width = 10
        self.height = 50

    def draw(self):
        pygame.draw.rect(self.win, (255, 255, 255), (self.x_pos, self.y_pos, self.width, self.height))
    
    def up(self):
        if self.y_pos >= 10:
            self.y_vel -= 2
            if self.y_vel < -10:
                self.y_vel = -10

    def  down(self):
        if self.y_pos <= 440:
            self.y_vel += 2
            if self.y_vel > 10:
                self.y_vel = 10

    def update(self):
        self.y_pos += self.y_vel
        if self.y_pos < 0:
            self.y_pos = 0
            self.y_vel = 0
        if self.y_pos > 450:
            self.y_pos = 450
            self.y_vel = 0

    def collision(self, ball: Ball):
        cx = ball.x_pos
        cy = ball.y_pos
        radius = ball.radius
        rx = self.x_pos
        ry = self.y_pos
        rw = self.width
        rh = self.height

        testX = cx
        testY = cy

        if (cx < rx):
            testX = rx  
        elif (cx > rx+rw):
            testX = rx+rw
        if (cy < ry):
            testY = ry      
        elif (cy > ry+rh): 
            testY = ry+rh

        distX = cx-testX
        distY = cy-testY
        distance = sqrt( (distX*distX) + (distY*distY) )

        
        if (distance <= radius):
            return True
        
        return False


class Game():
    def __init__(self, width, height):   #We dont need to  keep balls or score, both start at 0
        self.balls = []
        self.paddles = []
        self.score = 0
        self.width = width
        self.height = height
        pygame.init()
        self.win = pygame.display.set_mode((width, height))
        self.run()

    def run(self):
        run = True
        
        self.balls.append(Ball(250, 250, 5, 3, 5, self.win))
        self.balls.append(Ball(300, 250, 5, 3, 5, self.win))
        paddle1 = Paddle(20, 200, self.win)
        paddle2 = Paddle(470, 200, self.win)

        self.paddles.append(paddle1)
        self.paddles.append(paddle2)
        

        while run:
            keys = pygame.key.get_pressed()

            if keys[pygame.K_UP]:
                paddle1.up()

            if keys[pygame.K_DOWN]:
                paddle1.down()


            if keys[pygame.K_w]:
                paddle2.up()

            if keys[pygame.K_s]:
                paddle2.down()
            

            pygame.time.delay(50)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            self.win.fill((0, 0, 0))

            for ball in self.balls:
                ball.move()

                
            for paddle in self.paddles:
                paddle.update()
                
            for paddle in self.paddles:
                for  ball in self.balls:
                    if paddle.collision(ball):
                        ball.x_vel *= -1

            for ball in self.balls:
                ball.draw()

                
            for paddle in self.paddles:
                paddle.draw()
                    
                    


            pygame.display.update()



Game(500, 500)

