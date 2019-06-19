import pygame

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

try:
    pygame.init()
except:
    print('deu ruim')

largura = 640
altura = 420
tamanho = 20
voltando = 0
sair = True

relogio = pygame.time.Clock()
fundo = pygame.display.set_mode((largura,altura))
pygame.display.set_caption('Determinacao')

def texto(msg,cor,tam,x,y):
    font = pygame.font.SysFont(None, tam)
    texto1 = font.render(msg,True,cor)
    fundo.blit(texto1,[x,y])


def fase1():
    if voltando == 1:
        pos_x = 600
        pos_y = 210
    else:
        pos_x = largura / 2
        pos_y = altura / 2
    velocidade_x = 0
    velocidade_y = 0
    fundo.fill((199,253,254))
    pygame.display.update()

    funcionando = True
    while funcionando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                funcionando = False
                global sair
                sair = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    velocidade_x = -10
                    velocidade_y = 0
                if event.key == pygame.K_RIGHT:
                    velocidade_x = 10
                    velocidade_y = 0
                if event.key == pygame.K_UP:
                    velocidade_y = -10
                    velocidade_x = 0
                if event.key == pygame.K_DOWN:
                    velocidade_y = 10
                    velocidade_x = 0
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    velocidade_x = 0
                    velocidade_y = 0

        if funcionando:
            fundo.fill((199,253,254))
            pygame.draw.rect(fundo, black, [pos_x, pos_y, tamanho, tamanho])
            pygame.draw.rect(fundo,red,[620,210,20,20])
            pos_x += velocidade_x
            pos_y += velocidade_y

            if pos_x + tamanho > largura:
                pos_x = largura-tamanho
            if pos_x < 0:
                pos_x = 0
            if pos_y + tamanho > altura:
                pos_y = altura-tamanho
            if pos_y < 0:
                pos_y = 0
            if pos_x == 620 and pos_y == 210:
                fase2()
            relogio.tick(30)
            texto('Fase 1', black, 50, 10, 10)
            pygame.display.update()

def fase2():
    global voltando
    if voltando == 2:
        pos_x = 600
        pos_y = 210
    else:
        pos_x = 20
        pos_y = 210
    velocidade_x = 0
    velocidade_y = 0
    fundo.fill(white)
    pygame.display.update()

    funcionando = True
    while funcionando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                funcionando = False
                global sair
                sair = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    velocidade_x = -10
                    velocidade_y = 0
                if event.key == pygame.K_RIGHT:
                    velocidade_x = 10
                    velocidade_y = 0
                if event.key == pygame.K_UP:
                    velocidade_y = -10
                    velocidade_x = 0
                if event.key == pygame.K_DOWN:
                    velocidade_y = 10
                    velocidade_x = 0
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    velocidade_x = 0
                    velocidade_y = 0

        if funcionando:
            fundo.fill(white)
            pygame.draw.rect(fundo, black, [pos_x, pos_y, tamanho, tamanho])
            pygame.draw.rect(fundo, red, [0, 210, 20, 20])
            pygame.draw.rect(fundo, red, [620, 210, 20, 20])
            pos_x += velocidade_x
            pos_y += velocidade_y

            if pos_x + tamanho > largura:
                pos_x = largura - tamanho
            if pos_x < 0:
                pos_x = 0
            if pos_y + tamanho > altura:
                pos_y = altura - tamanho
            if pos_y < 0:
                pos_y = 0
            if pos_x == 0 and pos_y == 210:
                voltando = 1
                fase1()
            if pos_x == 620 and pos_y == 210:
                voltando = 2
                fase3()
            relogio.tick(30)
            texto('Fase 2', black, 50, 10, 10)
            pygame.display.update()

def fase3():
    global voltando
    if voltando == 5:
        pos_x = 600
        pos_y = 210
    else:
        pos_x = 20
        pos_y = 210
    velocidade_x = 0
    velocidade_y = 0
    fundo.fill((255, 195, 254))
    pygame.display.update()

    funcionando = True
    while funcionando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                funcionando = False
                global sair
                sair = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    velocidade_x = -10
                    velocidade_y = 0
                if event.key == pygame.K_RIGHT:
                    velocidade_x = 10
                    velocidade_y = 0
                if event.key == pygame.K_UP:
                    velocidade_y = -10
                    velocidade_x = 0
                if event.key == pygame.K_DOWN:
                    velocidade_y = 10
                    velocidade_x = 0
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    velocidade_x = 0
                    velocidade_y = 0

        if funcionando:
            fundo.fill((255, 195, 254))
            pygame.draw.rect(fundo, black, [pos_x, pos_y, tamanho, tamanho])
            pygame.draw.rect(fundo,red,[0,210,20,20])
            pygame.draw.rect(fundo, red, [620, 210, 20, 20])
            pos_x += velocidade_x
            pos_y += velocidade_y

            if pos_x + tamanho > largura:
                pos_x = largura-tamanho
            if pos_x < 0:
                pos_x = 0
            if pos_y + tamanho > altura:
                pos_y = altura-tamanho
            if pos_y < 0:
                pos_y = 0
            if pos_x == 0 and pos_y == 210:
                voltando = 2
                fase2()
            if pos_x == 620 and pos_y == 210:
                voltando = 3
                fase4()
            relogio.tick(30)
            texto('Fase 3', black, 50, 10, 10)
            pygame.display.update()

def fase4():
    global voltando
    pos_x = 20
    pos_y = 210
    velocidade_x = 0
    velocidade_y = 0
    fundo.fill((71, 195, 254))
    pygame.display.update()

    funcionando = True
    while funcionando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                funcionando = False
                global sair
                sair = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    velocidade_x = -10
                    velocidade_y = 0
                if event.key == pygame.K_RIGHT:
                    velocidade_x = 10
                    velocidade_y = 0
                if event.key == pygame.K_UP:
                    velocidade_y = -10
                    velocidade_x = 0
                if event.key == pygame.K_DOWN:
                    velocidade_y = 10
                    velocidade_x = 0
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    velocidade_x = 0
                    velocidade_y = 0

        if funcionando:
            fundo.fill((71, 195, 254))
            pygame.draw.rect(fundo, black, [pos_x, pos_y, tamanho, tamanho])
            pygame.draw.rect(fundo,red,[0,210,20,20])
            pos_x += velocidade_x
            pos_y += velocidade_y

            if pos_x + tamanho > largura:
                pos_x = largura-tamanho
            if pos_x < 0:
                pos_x = 0
            if pos_y + tamanho > altura:
                pos_y = altura-tamanho
            if pos_y < 0:
                pos_y = 0
            if pos_x == 0 and pos_y == 210:
                voltando = 5
                fase3()
            relogio.tick(30)
            texto('Fase 4', black, 50, 10, 10)
            texto('Sala Final', black, 80, 200, 200)
            pygame.display.update()

while sair:
    for event in pygame.event.get():
        fundo.fill(white)
        texto('Menu do joguinho krl', blue, 30, 213, 30)
        texto('Vai desgraza', black, 30, 60, 80)
        pygame.draw.rect(fundo, black, [60, 120, 135, 27])
        texto('Jogar(C)', white, 30, 87, 125)
        pygame.draw.rect(fundo, black, [200, 120, 135, 27])
        texto('Sair(S)', white, 30, 230, 125)
        pygame.display.update()
        if event.type == pygame.MOUSEBUTTONDOWN:
            x = pygame.mouse.get_pos()[0]
            y = pygame.mouse.get_pos()[1]
            if x > 60 and y > 120 and x < 205 and y < 147:
                fase1()
            elif x > 200 and y > 125 and x < 335 and y < 147:
                sair = False
        if event.type == pygame.QUIT:
            sair = False



pygame.quit()
quit()