import pygame
pygame.init()
#definir cores
black = (0,0,0)
white = (255,255,255)
blue = (0,0,255)

#fonte e função de texto
basicfont = pygame.font.SysFont("Arial", 50)
def pop_text():
    tela.blit(basicfont.render("end my suffering",True,(255,0,0)),(26,725))

#definir tela
size = (1200,900)
tela = pygame.display.set_mode(size)
pygame.display.set_caption('Mysterio')
clock = pygame.time.Clock()
guy = pygame.image.load('dood.png')

#largura e altura do personagem
thiccness = 50

#tela e caixa de texto
def frame():
    pygame.draw.rect(tela,black,(0,0,1200,900),50)
def text_box():
    pygame.draw.rect(tela,blue,(26,725,1150,175))
#placeholder de personagem
def dudu(x,y):
    tela.blit(guy,(x,y))
def npc():
    tela.blit(guy,(100,100))

def hi(x,y):
    if (x in range(50,151)) and (y in range(50,151)):
        pop_text()
def loop_jogo():
    exit = False
    x = 0
    y = 0
    
    x_speed = 0
    y_speed = 0
    
    while not exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True
            # Teclas e movimento
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    x_speed = -10
                elif event.key == pygame.K_d:
                    x_speed = 10
                elif event.key == pygame.K_s:
                    y_speed = 10
                elif event.key == pygame.K_w:
                    y_speed = -10
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
        npc()
        hi(x,y)
        pygame.display.update()
        clock.tick(60)

loop_jogo()
pygame.quit()
quit()