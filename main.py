import pygame
import SET
import Main_GRAPHICS
import random
class MainGame:
    window=None
    Player = None
    def __init__(self):
        pygame.display.init()
        MainGame.window = pygame.display.set_mode([SET.GAME_WIDTH, SET.GAME_HEIGHT])
        pygame.display.set_caption("LELITON")
        MainGame.Player = Character(600,300)
    def GameStart(self):
        while True:
            #display of the screen
            self.getEvent()
            MainGame.window.fill(SET.BG_color)
            MainGame.window.blit(self.Info("Score%d"%4),(10,10))
            #display character on the screen
            Character.display_char(MainGame.Player)
            pygame.display.update()
    def getEvent(self):
        eventList = pygame.event.get()
        for event in eventList:
            if event.type == pygame.QUIT:
                self.endgame()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    Character.move(MainGame.Player)
                    print("xia")
                if event.key == pygame.K_UP:
                    print("shang")
                if event.key == pygame.K_LEFT:
                    print("zuo")
                if event.key == pygame.K_RIGHT:
                    print("you")
    def Info(self,test):
        pygame.font.init()
        #get font
        font = pygame.font.SysFont('kaiti',18)
        #write font
        fontinfo = font.render(test,True,SET.TEXT_COLOR)
        return fontinfo
    def endgame(self):
        exit()

class Character:
    # location of character(left,top)
    # load image of Character
    Image1 = pygame.image.load('Charater image/ga10/CP501AB.png')
    Image2 = pygame.image.load('Charater image/ga10/CP502AB.png')
    def __init__(self, left, top):
        self.character_image = {
                'character_normal_stand': Character.get_images(Character.Image1, 10, 7, 50, 60, (0, 0, 0), 1),
                'character_normal_left': Character.get_images(Character.Image1, 13, 66, 50, 60, (0, 0, 0), 1),
                'character_normal_left2': Character.get_images(Character.Image1, 67, 68, 50, 55, (0, 0, 0), 1),
                'character_normal_right': Character.get_images(Character.Image1, 5, 185, 50, 60, (0, 0, 0), 1),
                'character_normal_right2': Character.get_images(Character.Image1, 60, 186, 50, 60, (0, 0, 0), 1),
                'character_normal_behind': Character.get_images(Character.Image1, 8, 122, 50, 60, (0, 0, 0), 1)}
        self.state = 'character_normal_stand'
        self.image = self.character_image[self.state]
        # get graphics rect
        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.top = top
        self.speed = 10
    def display_char(self):
        self.image = self.character_image[self.state]
        MainGame.window.blit(self.image,self.rect)
    def move(self):
        if self.rect =='character_normal_stand':
            self.rect.top += self.speed
        if self.rect == 'character_normal_left' or 'character_normal_left2':
            self.rect.left -= self.speed
        if self.rect == 'character_normal_right' or 'character_normal_right2' :
            self.rect.left += self.speed
        if self.rect == 'character_normal_behind':
            self.rect.top -= self.speed
    def get_images(sheet, x, y, width, hegiht, colorkey, scale):
        # cut character graphics and set the position
        image = pygame.Surface((width, hegiht))
        image.blit(sheet, (0, 0), (x, y, width, hegiht), scale)
        image.set_colorkey(colorkey)
        image = pygame.transform.scale(image, (int(width * scale), int(hegiht * scale)))
        return image

    def state_image(self):
        pass








def main():
    game = MainGame()
    game.GameStart()


if __name__ == '__main__':
    main()