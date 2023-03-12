import pygame
import  Main_GRAPHICS
import main


class Player:
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.setup_states()
        self.set_upvelocities()
        self.setup_timers()


    def set_upvelocities(self):
        self.x_vel = 0
        self.y_vel = 0
    def setup_timers(self):
        self.walking_timer = 0
    def load_images(self):
        sheet = Main_GRAPHICS.Load_image.state_image('character_normal_left')
        self.frames = []
    def update(self,keys):
        if keys[pygame.K_UP]:
            self.y_vel = 5
        if keys[pygame.K_DOWN]:
            self.y_vel = -5
        if keys[pygame.K_LEFT]:
            self.x_vel = -5
        if keys[pygame.K_RIGHT]:
            self.x_vel = 5

