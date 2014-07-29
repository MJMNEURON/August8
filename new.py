from __future__ import print_function
import pygame
from pygame.locals import *
import math
import random

W, H=800, 600
fixation_point_duration=1000
fixation_color=[255,0,0]
fixation_radius=10
stimulus_duration=200
wait_duration=200
correctness_duration=2000
font_size=100
text_color=[0, 0, 0]
background_color=[128,128,128]
numgenerated=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


def print_number(number, position):
    image = font.render(number, True, text_color, background_color)
    size=image.get_size()
    window.blit(image,[W/2-18,H/2-33])
    pygame.time.wait(stimulus_duration)

def print_text(sentence, position):
    text = font.render(sentence, True, text_color, background_color)
    size=text.get_size()
    window.blit(text,[W/2-230,H/2-33])
    pygame.time.wait(stimulus_duration)    

def draw_fixation():
    pygame.draw.circle(window, fixation_color, [W/2,H/2], fixation_radius)

def response():
    resp=[]
    while resp==[]:
        window.fill(background_color)
        pygame.display.flip()
        for e in pygame.event.get():
            if e.type == KEYDOWN:
                if e.key == K_ESCAPE:
                    raise Exception
                if e.key == K_LEFT:
                    resp = -1
                elif e.key == K_RIGHT:
                    resp = 1                   
    return resp

def do_trial():
        randomnum=random.choice([0,1,2,3,4,5,6,7,8,9])
        count=random.choice([1,2,3,4,5,6])        
        random.shuffle(numgenerated)
           
        window.fill(background_color)
        draw_fixation()
        pygame.display.flip()
        pygame.time.wait(fixation_point_duration)

        series=[]
        window.fill(background_color)

        for i in range (0, count):
            print_number(numgenerated[i], [W/2-18,H/2-33])
            series.append(numgenerated[i])
            pygame.display.flip()
            pygame.time.wait(stimulus_duration)
            i+=1
               

        window.fill(background_color)
        pygame.display.flip()
        pygame.time.wait(wait_duration)
        print_number(num[randomnum], [W/2-18,H/2-33])
        pygame.display.flip()
        pygame.time.wait(stimulus_duration)

         
        resp=[]
        while (resp==[]):
            resp=response()

            print (resp)
            print (numgenerated)
            print (num[randomnum])
            print (series)
            print (numgenerated-series)

        if num[randomnum] not in series:
            if resp==-1:
                print_text("You are wrong.", [W/2-500, H/2-33])
                pygame.display.flip()
                pygame.time.wait(correctness_duration)
            else:
                print_text("You are right.", [W/2-500, H/2-33])
                pygame.display.flip()
                pygame.time.wait(correctness_duration)
        else:
            if resp==1:
                print_text("You are wrong.", [W/2-500, H/2-33])
                pygame.display.flip()
                pygame.time.wait(correctness_duration)

            else:
                print_text("You are right.", [W/2-500, H/2-33])
                pygame.display.flip()
                pygame.time.wait(correctness_duration)

    
try:
    pygame.init()
#   window = pygame.display.set_mode([W, H])
    window = pygame.display.set_mode([W, H], FULLSCREEN | HWSURFACE | DOUBLEBUF)

    font=pygame.font.Font(None, font_size)
    for total in range (1,9):
        do_trial()
        total+=1
    
finally:
    pygame.quit()
        
    
