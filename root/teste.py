import pygame
pygame.init()
#definir cores
black = (0,0,0)
white = (255,255,255)
blue = (0,0,255)

#fonte e função de texto
basicfont = pygame.font.SysFont("Arial", 30)
def pop_text(line,posx,posy):
    tela.blit(basicfont.render(line,True,(0,0,0)),(posx,posy))

#definir tela
size = (1200,900)
tela = pygame.display.set_mode(size)
pygame.display.set_caption('Mysterio')
clock = pygame.time.Clock()
guy = pygame.image.load('dood.png')

#largura e altura do personagem
thiccness = 50
#classe base de interagiveis
class Interagivel:
    def __init__(self,posx,posy,thiccness):
        self.x = posx
        self.y = posy
        self.thiccness = thiccness
    __lines = ["Olá!","isso é um teste de texto."]
    text_x = 26
    text_y = 725
    def say_hi(self,playerX,playerY,playerthicc,action):
        if (playerX in range(self.x-(thiccness+int(playerthicc/2)),self.x+(thiccness+int(playerthicc/2))) and (playerY in range(self.y-(thiccness+int(playerthicc/2)),self.y+(thiccness+int(playerthicc/2))))) and action:
            for i in range(len(self.__lines)):
                pop_text(self.__lines[i],self.text_x,self.text_y)
                self.text_y += 22
            self.text_y= 725
    def exist(self):
        tela.blit(guy,(self.x,self.y))
            

#tela e caixa de texto
def frame():
    pygame.draw.rect(tela,black,(0,0,1200,900),50)
def text_box():
    pygame.draw.rect(tela,blue,(26,725,1150,175))
#placeholder de personagem
def dudu(x,y):
    tela.blit(guy,(x,y))

def loop_jogo():
    exit = False
    x = 0
    y = 0
    
    x_speed = 0
    y_speed = 0
    action = False    
    while not exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True
            # Teclas e movimento
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    x_speed = -5
                elif event.key == pygame.K_d:
                    x_speed = 5
                elif event.key == pygame.K_s:
                    y_speed = 5
                elif event.key == pygame.K_w:
                    y_speed = -5
                elif event.key == pygame.K_SPACE and action == False:
                    action = True
                elif event.key == pygame.K_SPACE and action == True:
                    action = False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    x_speed = 0
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    y_speed = 0            
        x += x_speed
        y += y_speed
        #Verificar limite da tela
        if x_speed >= 0 and x > 1175 - thiccness:
            x_speed = 0
        if x_speed <= 0 and x < 25:
            x_speed = 0
        if y_speed >= 0 and y > 670:
            y_speed = 0
        if y_speed <= 0 and y < 26:
            y_speed = 0
        if x > 1175 - thiccness:
            x = 1175 - thiccness

        if x < 25:
            x = 25
        if y > 670:
            y = 673
        if y < 26:
            y = 26

        tela.fill(white)
        text_box()
        frame()
        dudu(x,y)
        npc = Interagivel(100,100,50)
        npc.exist()
        npc.say_hi(x,y,thiccness,action)
        pygame.display.update()
        clock.tick(60)

loop_jogo()
pygame.quit()
quit()

