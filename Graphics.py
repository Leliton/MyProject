import pygame
from Load_image import *
from Main import *
from Game_Data import *
class Character():
    def __init__(self, left, top):
        # self.image = pygame.image.load(name)
        self.direction = Dict_of_Image['you']
        self.image = self.direction
        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.top = top
        self.Stop = True
        self.speed = 7
    def display_char(self):
        window.blit(self.direction,self.rect)
    def move(self):
        if self.direction == Dict_of_Image['zuo']:
            self.rect.left -= self.speed
            if self.rect.left <= 0:
                self.rect.left = 0
        elif self.direction == Dict_of_Image['you']:
            self.rect.left += self.speed
            if self.rect.left >= WINDOW_SIZE.width-self.rect.width:
                self.rect.left = WINDOW_SIZE.width-self.rect.width
        elif self.direction == Dict_of_Image['shang']:
            self.rect.top -= self.speed
            if self.rect.top <= 0:
                self.rect.top = 0
        elif self.direction == Dict_of_Image['xia']:
            self.rect.top += self.speed
            if self.rect.top >= WINDOW_SIZE.height-self.rect.height:
                self.rect.top = WINDOW_SIZE.height-self.rect.height
player = Character(600,600)
class attack():
    def __init__(self,player):
        self.image = Dict_of_Image['attack1']
        self.direction = player.direction
        self.rect = self.image.get_rect()
        if self.direction == Dict_of_Image['shang']:
            self.rect.left = player.rect.left + player.rect.width/2-self.rect.width/2
            self.rect.top = player.rect.top - self.rect.height
        elif self.direction == Dict_of_Image['xia']:
            self.rect.left = player.rect.left + player.rect.width/2-self.rect.width/2
            self.rect.top = player.rect.top + self.rect.height
        elif self.direction == Dict_of_Image['zuo']:
            self.rect.left = player.rect.left - self.rect.width/2-self.rect.width/2
            self.rect.top = player.rect.top + player.rect.width/2 - self.rect.width/2
        elif self.direction == Dict_of_Image['you']:
            self.rect.left = player.rect.left + player.rect.width
            self.rect.top = player.rect.top + player.rect.width/2 - self.rect.width/2
        self.speed = 10
        self.state = True
    def displayattack(self):
        window.blit(self.image,self.rect)
    def move(self):
        if  self.direction == Dict_of_Image['shang']:
            if self.rect.top >0:
                self.rect.top -= self.speed
            else:
                self.state = False
        elif self.direction == Dict_of_Image['xia']:
            if self.rect.top + self.rect.height<WINDOW_SIZE.height:
                self.rect.top += self.speed
            else:
                self.state = False
        elif self.direction == Dict_of_Image['zuo']:
            if self.rect.left >0:
                self.rect.left -=self.speed
            else:
                self.state = False
        elif self.direction == Dict_of_Image['you']:
            if self.rect.left+self.rect.width< WINDOW_SIZE.width:
                self.rect.left +=self.speed
            else:
                self.state = False