import pygame
import Game_Data
Image1 = pygame.image.load('./Image/Main.png')
Image2 = pygame.image.load('./Image/CP816AA.png')
class Image:
    def __init__(self):
        pass
    def get_images(name, x, y, width, hegiht, colorkey, scale):
        # cut character graphics and set the position
        image = pygame.Surface((width, hegiht))
        image.blit(name, (0, 0), (x, y, width, hegiht), scale)
        image.set_colorkey(colorkey)
        image = pygame.transform.scale(image, (int(width * scale), int(hegiht * scale)))
        return image
attack =Image.get_images(Image2,4,8,70,70,(0, 0, 0),1)
attack = pygame.transform.scale(attack,(int(attack.get_width()*0.3),int(attack.get_height()*0.3)))
Dict_of_Image = {'xia':Image.get_images(Image1, 0, 0, 50, 50, (0, 0, 0), 1),
                'zuo':Image.get_images(Image1, 2, 66, 45, 50, (0, 0, 0), 1),
                'you':Image.get_images(Image1, 2, 184, 40, 55, (0, 0, 0), 1),
                'shang':Image.get_images(Image1, 2, 123, 40, 55, (0, 0, 0), 1),
                 'attack1':attack
                }