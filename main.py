import pygame

pygame.init()
win = pygame.display.set_mode((500, 500))


run = True
pad1_x =  0
pad1_y = 240
pad2_x = 490
pad2_y = 240
ball_x = 200
ball_y = 200
vel_x = 5
vel_y = 3
vel_pad_y1 = 0
vel_pad_y2 = 0
t = 0


while run:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    
    
    #paddle 1 controls
    if keys[pygame.K_UP] and pad1_y >= 10:
        vel_pad_y1 -= 2
        if vel_pad_y1 < -10:
            vel_pad_y1 = -10

        

    if keys[pygame.K_DOWN] and pad1_y <= 440:
        vel_pad_y1 += 2
        if vel_pad_y1 > 10:
            vel_pad_y1 = 10


    #velocity + pos
    pad1_y += vel_pad_y1


    #wall fix
    if pad1_y < 0:
        pad1_y = 0
        vel_pad_y1 = 0
    if pad1_y > 450:
        pad1_y = 450
        vel_pad_y1 = 0


    #friction
    if vel_pad_y1 > 0:
        vel_pad_y1 -= 1
        if vel_pad_y1 < 0:
            vel_pad_y1 = 0
    elif vel_pad_y1 < 0:
        vel_pad_y1 += 1
        if vel_pad_y1 > 0:
            vel_pad_y1 = 0


    #paddle 2 controls
    if keys[pygame.K_w] and pad2_y >= 10:
        vel_pad_y2 -= 2
        if vel_pad_y2 < -10:
            vel_pad_y2 = -10


    if keys[pygame.K_s] and pad2_y <= 440:
        vel_pad_y2 += 2
        if vel_pad_y2 > 10:
            vel_pad_y2 = 10


    #velocity + pos
    pad2_y += vel_pad_y2

    #wall fix
    if pad2_y < 0:
        pad2_y = 0
        vel_pad_y2 = 0
    if pad2_y > 450:
        pad2_y = 450
        vel_pad_y2 = 0


    #friction
    if vel_pad_y2 > 0:
        vel_pad_y2 -= 1
        if vel_pad_y2 < 0:
            vel_pad_y2 = 0
    elif vel_pad_y2 < 0:
        vel_pad_y2 += 1
        if vel_pad_y2 > 0:
            vel_pad_y2 = 0


    #ball hit wall
    if ball_x >= 495 or ball_x <= 5:
        vel_x *= -1
    if ball_y >= 495 or ball_y <= 5:
        vel_y *= -1
        

    #ball vel + paddle vel
    if (pad1_x + 20) >= (ball_x - 5) and (pad1_y - 5 <= ball_y <= pad1_y + 55):   
        vel_x *= -1
        vel_y += vel_pad_y1
    if (pad2_x - 20) <= (ball_x + 5) and (pad2_y - 5 <= ball_y <= pad2_y + 55):
        vel_x *= -1
        vel_y += vel_pad_y2


    #friction
    t += 1
    if t == 60:
        if vel_y > 0:
            vel_y -= 1
            if vel_y < 0:
                vel_y = 0
        elif vel_y < 0:
            vel_y += 1
            if vel_y > 0:
                vel_y = 0
        t = 0
        
        

    #vel of ball
    ball_x += vel_x
    ball_y += vel_y
    



    
    
#add velocity from paddles to vel_x & vel_y


#keys | value
    win.fill((0, 0, 0))
    pygame.draw.rect(win, (30, 50, 250), (pad1_x, pad1_y, 10, 50))
    pygame.draw.rect(win, (220, 30, 10), (pad2_x, pad2_y, 10, 50))
    pygame.draw.circle(win, (255, 255, 255), (ball_x, ball_y), 5)
    pygame.display.update() #colision at begining of loop or copy/paste above
pygame.quit()
