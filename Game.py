

import pygame
from pygame import *

import random
from random import *

import time
from time import *


p = 3

class CP(object):
    def __init__(self,screen):

        self.x = 300
        self.y = 120

        self.displayList = []

        self.useList = ["up","down","right","left"]


    def display(self,use):

        global p
        self.displayList = []

        self.i = 0

        while self.i <= p:
            a = choice(use)
            self.displayList.append(a)
            self.i += 1

    def pp(self):

        for temp in self.displayList:
            if temp == "up":
                self.U(screen,self.x,self.y,"u")
            elif temp == "down":
                self.U(screen,self.x,self.y,"d")
            elif temp == "right":
                self.U(screen,self.x,self.y,"r")
            elif temp == "left":
                self.U(screen,self.x,self.y,"l")


    def U(self,screen,x,y,a):
        screen = screen
        image = pygame.image.load("./photo/"+a+".png").convert()

        screen.blit(background, (0, 0))
        pygame.display.update()
        sleep(0.3)

        screen.blit(image,(x,y))
        pygame.display.update()
        sleep(0.3)


def End(screen,end):

    if end == "win":
        screen = screen
        image = pygame.image.load("./photo/Good.gif").convert()
        screen.blit(background, (0, 0))
        screen.blit(image,(250,120))
        pygame.display.update()

    elif end == "lose":
        screen = screen
        image = pygame.image.load("./photo/Lose.jpg").convert()
        screen.blit(background, (0, 0))
        screen.blit(image,(250,120))
        pygame.display.update()




if __name__ == "__main__":

    screen =  pygame.display.set_mode((828,505),0,32)

    background = pygame.image.load("./photo/bg1.png").convert()

    read = pygame.image.load("./photo/read.png").convert()

    start = pygame.image.load("./photo/start.jpeg").convert()

    hard = pygame.image.load("./photo/hard.png").convert()

    pr = CP(screen)

while True:

    screen.blit(background, (0, 0))
    screen.blit(read, (200, 200))
    pygame.display.update()
    sleep(2)
    screen.blit(background, (0, 0))
    screen.blit(start, (250, 120))
    pygame.display.update()
    sleep(1)
    pr.display(pr.useList)
    print(pr.displayList)
    pr.pp()
    put = []

    screen.blit(background, (0, 0))
    pygame.display.update()
    q =1

    while q:
        for event in pygame.event.get():
            if event.type == QUIT:
                print("exit")
                exit()

            elif event.type == KEYDOWN:
                if event.key == K_UP:
                    put.append("up")
                    print("get")

                elif event.key == K_DOWN:
                    put.append("down")
                    print("get")

                elif event.key == K_RIGHT:
                    put.append("right")
                    print("get")

                elif event.key == K_LEFT:
                    put.append("left")
                    print("get")

                elif event.key == K_q:
                    print("exit")
                    exit()
                elif event.key == K_SPACE:

                    a = put == pr.displayList

                    if a:
                        End(screen,"win")
                        p += 1
                        q = 1
                        while q:
                            for event in pygame.event.get():
                                if event.type == KEYDOWN:
                                    if event.key == K_SPACE:
                                        screen.blit(background, (0, 0))
                                        screen.blit(hard, (200, 200))
                                        pygame.display.update()
                                        sleep(1)
                                        q = 0

                    else:
                        End(screen,"lose")
                        q = 1
                        while q:
                            for event in pygame.event.get():
                                if event.type == KEYDOWN:
                                    if event.key == K_SPACE:
                                        q = 0


        pygame.display.update()