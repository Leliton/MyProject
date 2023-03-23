import pygame
from Load_image import *
from Game_Data import *
from Graphics import *
window = pygame.display.set_mode(Game_Data.WINDOW_SIZE.size)
attacklist = []
class MainGame(object):
    def __init__(self):
        pygame.init()
        #gamewindow
        window.fill(Game_Data.BG_COLOR)
        #game name
        self.Caption = pygame.display.set_caption('Lee`s Advanture')
        #game fps
        self.fps = pygame.time.Clock()
    def Start_Game(self):
        while True:
            self.fps.tick(Game_Data.FRAME_PER_SEC)
            #get game event
            window.fill(BG_COLOR)
            window.blit(self.Info("Score %d" % 0), (15, 15))
            self.GetEvent()
            Character.display_char(player)
            self.blitattack()
            if not player.Stop:
                player.move()
            #self.updata_sprites()
            pygame.display.update()
    def Info(self,test):
        pygame.font.init()
        #get font
        font = pygame.font.SysFont('kaiti',20)
        #write font
        fontinfo = font.render(test,True,TEXT_COLOR)
        return fontinfo
    def GetEvent(self):
        Event_List = pygame.event.get()
        for event in Event_List:
            #quit game
            if event.type == pygame.QUIT:
                MainGame.game_over()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    player.direction = Dict_of_Image['shang']
                    player.Stop = False
                elif event.key == pygame.K_s:
                    #Character.moveD(player)
                    player.direction = Dict_of_Image['xia']
                    player.Stop = False
                elif event.key == pygame.K_a:
                    #Character.moveL(player)
                    player.direction = Dict_of_Image['zuo']
                    player.Stop = False
                elif event.key == pygame.K_d:
                    #Character.moveR(player)
                    player.direction = Dict_of_Image['you']
                    player.Stop = False
                elif event.key == pygame.K_j:
                    charattack = attack(player)
                    attacklist.append(charattack)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_s or event.key == pygame.K_w or event.key == pygame.K_a or event.key == pygame.K_d:
                    player.Stop = True

    def blitattack(self):
        for bullet in attacklist:
            if bullet.state:
                bullet.displayattack()
                bullet.move()
            else:
                attacklist.remove(bullet)
    @staticmethod
    def game_over():
        print('Gameover')
        pygame.quit
        exit()


if __name__ == '__main__':
    game = MainGame()
    game.Start_Game()