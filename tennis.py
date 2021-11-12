# import global and drawings
#moving the paddles 
#moving the ball
#keeping score
import pygame
import random
import time
#initialize pygame
pygame.init()
#colors globals 
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
black = (0,0,0)
white = (255,255,255)
orange = (255,127,0)
yellow = (255,255,0)
violet = (127,0,255)
brown = (102,51,0)
#screen globals
screen_width = 600
screen_height = 400
game_screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Tiny Tennis")
font = pygame.font.SysFont('monospace',75)
#ball globals 
ball_x = int(screen_width/2) # ball is at the center 
ball_y = int(screen_height/2) # ball is at the center 
ball_xv = 3 # speed of ball in x axis it will move 3 pixels at a time 
ball_yv = 3 # speed of ball in y axis 
ball_r = 20 # radius of ball 
#draw paddle 1 
paddle1_x = 10 
paddle1_y = 10
paddle1_w = 25 
paddle1_h = 100

#draw paddle 2 
paddle2_x = screen_width-35
paddle2_y = 10
paddle2_w = 25
paddle2_h = 100
#initialize the scores 
player1_score = 0
player2_score = 0
pygame.mouse.set_visible(0) # make mouse invisible in game screen
do_main = True
while do_main:
    pressed = pygame.key.get_pressed() # shorter reference to the function
    pygame.key.set_repeat() # repeat the action of key until it is released
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            do_main = False
    if pressed[pygame.K_ESCAPE]:
        do_main = False
    if pressed[pygame.K_w]:
        paddle1_y -= 5
    elif pressed[pygame.K_s]:
        paddle1_y += 5
    if pressed[pygame.K_UP]:
        paddle2_y -= 5
    elif pressed[pygame.K_DOWN]:
        paddle2_y += 5
    # location of ball is updated 
    ball_x  += ball_xv
    ball_y  += ball_yv
    #if ball is out of game screen , bounce back 
    if ball_y-ball_r<=0 or ball_y + ball_r>=screen_height:
        ball_yv *= -1
    #if paddles collide with boundaries ,reset to the borders coordinates
    if paddle1_y < 0:
        paddle1_y = 0
    elif paddle1_y+paddle1_h > screen_height:
        paddle1_y = screen_height-paddle1_h 
    if paddle2_y < 0 :
        paddle2_y = 0
    elif paddle2_y +paddle2_h > screen_height :
        paddle2_y= screen_height - paddle2_h
    #collision of ball with paddles
    #left paddle
    if ball_x < paddle1_x + paddle1_w and ball_y >= paddle1_y and ball_y<= paddle1_y+ paddle1_h:
        ball_xv *= -1
    #right paddle 
    if ball_x > paddle2_x and ball_y >= paddle2_y and ball_y <= paddle2_y+paddle2_h:
        ball_xv *= -1
    #plyaer score
    if ball_x <= 0 :
        player2_score += 1
        ball_x = int(screen_width/2)
        ball_y = int(screen_height/2)
    elif ball_x >= screen_width:
        player1_score += 1
        ball_x = int(screen_width/2)
        ball_y = int(screen_height/2)
    game_screen.fill(black)
    paddle1 = pygame.draw.rect(game_screen,white,(paddle1_x,paddle1_y,paddle1_w,paddle1_h),0)
    paddle2 = pygame.draw.rect(game_screen,white,(paddle2_x,paddle2_y,paddle2_w,paddle2_h),0)
    net = pygame.draw.line(game_screen,yellow,(300,5),(300,400))
    ball = pygame.draw.circle(game_screen,blue,(ball_x,ball_y),ball_r,0)

    score_text = font.render(str(player1_score)+ " " + str(player2_score),1,white)
    game_screen.blit(score_text,(screen_width/2-score_text.get_width()/2,10))
    pygame.display.update()
    time.sleep(0.016666667)
pygame.quit()