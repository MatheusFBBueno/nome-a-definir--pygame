import pygame
from player import Player
from wall import Wall
from interagivel import Interagivel
from texto import inserttext


#Constantes globais
guyF = pygame.image.load('images/dood_frontal.png')
guyL = pygame.image.load('images/dood_left.png')
guyR = pygame.image.load('images/dood_right.png')
guyB = pygame.image.load('images/dood_back.png')
guyF = pygame.transform.scale(guyF,(100,100))
guyL = pygame.transform.scale(guyL,(100,100))
guyR = pygame.transform.scale(guyR,(100,100))
guyB = pygame.transform.scale(guyB,(100,100))

# Cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (50, 50, 255)
BROWN= (188,100,28)
GRAY= (89,82,78)
# tamanho da tela
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


pygame.init()
fonte= pygame.font.Font('pokemon_fire_red.ttf',24)
 
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
 
pygame.display.set_caption('Test')

# lista de sprites
all_sprite_list = pygame.sprite.Group()
 
# paredes (x_pos, y_pos, width, height)
wall_list = pygame.sprite.Group()
 
wall = Wall(0, 0, 10, 600)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)


wall = Wall(10, 0, 790, 10)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)
 
wall = Wall(790, 10, 10, 590)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(10, 590, 790, 10)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)

wall = Wall(10,490,780,10)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.paint(BLACK)
textbox = Wall(10,500,780,90)
textbox.image.fill(BLUE) 
wall_list.add(textbox)
all_sprite_list.add(textbox)

# Jogador
player = Player(100, 10,100,100)
player.definirImagem(guyF,guyB,guyL,guyR)
player.walls = wall_list
all_sprite_list.add(player)

clock = pygame.time.Clock()

#variáveis de locais visitados
visited_basement = False
visited_garden = False

#variáveis de inventário
inv_faca= False

def quarto(visited_basement,visited_garden,inv_faca):
    done = False
    keyq = False
    keyw = False
    keye = False
    keyr = False
    keyt = False
    keyy = False
    keyu = False
    keyi = False
    keyo = False
    keyp = False
    keya = False
    keyS = False
    keyd = False
    keyf = False
    keyg = False
    keyh = False
    keyj = False
    keyk = False
    keyl = False
    keyz = False
    keyx = False
    keyc = False
    keyv = False
    keyb = False
    keyn = False
    keym = False
    backspace = False   
    space = False
    porta_porao = Interagivel(300,470,100,20,["Entrar no Porao?","S/N"])
    porta_porao.image.fill((209,176,12))
    all_sprite_list.add(porta_porao)
    
    
    camac = pygame.image.load('images/bed.png')
    cama = Interagivel(10,10,100,100,["time","to","sleep"])
    camac = pygame.transform.scale(camac, (100, 100))
    wall_list.add(cama)
    all_sprite_list.add(cama)
    cama.carregarImagem(camac)

    img_faca = pygame.image.load("images/knife.png")
    img_faca = pygame.transform.scale(img_faca,(25,25))
    faca = Interagivel(500,200,25,25,["Uma faca esta no chao","pegar a faca?","S/N"])
    faca.carregarImagem(img_faca)
    
    porta_jardim = Interagivel(770,100,20,100,["Sair para o jardim?","S/N"])
    porta_jardim.image.fill((209,176,12))
    
    if visited_basement:
        player.rect.y =370
        all_sprite_list.add(faca)
        all_sprite_list.add(porta_jardim)
    if visited_garden:
        player.rect.x= 660
        player.rect.y= 100
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                quit()
    
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.changespeed(-5, 0)
                elif event.key == pygame.K_RIGHT:
                    player.changespeed(5, 0)
                elif event.key == pygame.K_UP:
                    player.changespeed(0, -5)
                elif event.key == pygame.K_DOWN:
                    player.changespeed(0, 5)
                if event.key == pygame.K_s:
                    keyS = True
                if event.key == pygame.K_n:
                    keyn = True
        
            
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.changespeed(5, 0)
                elif event.key == pygame.K_RIGHT:
                    player.changespeed(-5, 0)
                elif event.key == pygame.K_UP:
                    player.changespeed(0, 5)
                elif event.key == pygame.K_DOWN:
                    player.changespeed(0, -5)
                if event.key == pygame.K_s:
                    keyS = False
                if event.key == pygame.K_n:
                    keyn = False
        
        keyset =[keyq,keyw,keye,keyr,keyt,keyy,keyu,keyi,keyo,keyp,keya,keyS,keyd,keyf,keyg,keyh,keyj,keyk,keyl,keyz,keyx,keyc,keyv,keyb,keyn,keym,backspace,space]
        all_sprite_list.update()
        #transição para porão
        if porta_porao.sayhi(player,textbox,fonte) and keyset[11]:
            all_sprite_list.remove(porta_porao)
            all_sprite_list.remove(cama)
            wall_list.remove(cama)
            if visited_basement:
                all_sprite_list.remove(porta_jardim)
                all_sprite_list.remove(faca)
            porao(visited_basement)
             
        if visited_basement:
            if faca.sayhi(player,textbox,fonte) and keyset[11]:
                faca.rect.x = 750
                faca.rect.y = 520
                inv_faca = True
            #transição para jardim
            if porta_jardim.sayhi(player,textbox,fonte) and keyset[11]:
                all_sprite_list.remove(porta_jardim)
                if not inv_faca:
                    all_sprite_list.remove(faca)
                all_sprite_list.remove(cama)
                wall_list.remove(cama)
                all_sprite_list.remove(porta_porao)
                jardim(visited_basement,visited_garden)
        screen.fill(BROWN)
        all_sprite_list.draw(screen)
        textbox.image.fill(BLUE)
        pygame.display.flip()
    
        clock.tick(60)

def porao(visited_basement):
    done = False
    keyq = False
    keyw = False
    keye = False
    keyr = False
    keyt = False
    keyy = False
    keyu = False
    keyi = False
    keyo = False
    keyp = False
    keya = False
    keyS = False
    keyd = False
    keyf = False
    keyg = False
    keyh = False
    keyj = False
    keyk = False
    keyl = False
    keyz = False
    keyx = False
    keyc = False
    keyv = False
    keyb = False
    keyn = False
    keym = False
    backspace = False   
    space = False
    player.rect.y=30
    porta_quarto = Interagivel(300,10,100,20,["Entrar no quarto?","S/N"])
    porta_quarto.image.fill((209,176,12))
    all_sprite_list.add(porta_quarto)

    
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.changespeed(-5, 0)
                elif event.key == pygame.K_RIGHT:
                    player.changespeed(5, 0)
                elif event.key == pygame.K_UP:
                    player.changespeed(0, -5)
                elif event.key == pygame.K_DOWN:
                    player.changespeed(0, 5)
                if event.key == pygame.K_s:
                    keyS = True
                if event.key == pygame.K_n:
                    keyn = True
        
            
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.changespeed(5, 0)
                elif event.key == pygame.K_RIGHT:
                    player.changespeed(-5, 0)
                elif event.key == pygame.K_UP:
                    player.changespeed(0, 5)
                elif event.key == pygame.K_DOWN:
                    player.changespeed(0, -5)
                if event.key == pygame.K_s:
                    keyS = False
                if event.key == pygame.K_n:
                    keyn = False
        
        keyset =[keyq,keyw,keye,keyr,keyt,keyy,keyu,keyi,keyo,keyp,keya,keyS,keyd,keyf,keyg,keyh,keyj,keyk,keyl,keyz,keyx,keyc,keyv,keyb,keyn,keym,backspace,space]
        all_sprite_list.update()
        if porta_quarto.sayhi(player,textbox,fonte) and keyset[11]:
            all_sprite_list.remove(porta_quarto)
            visited_basement = True
            quarto(visited_basement,visited_garden,inv_faca)

        screen.fill(GRAY)
        all_sprite_list.draw(screen)
        textbox.image.fill(BLUE)
        pygame.display.flip()
    
        clock.tick(60)

def jardim(visited_basement,visited_garden):
    done = False
    keyq = False
    keyw = False
    keye = False
    keyr = False
    keyt = False
    keyy = False
    keyu = False
    keyi = False
    keyo = False
    keyp = False
    keya = False
    keyS = False
    keyd = False
    keyf = False
    keyg = False
    keyh = False
    keyj = False
    keyk = False
    keyl = False
    keyz = False
    keyx = False
    keyc = False
    keyv = False
    keyb = False
    keyn = False
    keym = False
    backspace = False   
    space = False
    player.rect.x = 30
    player.rect.y=100
    porta_quarto = Interagivel(10,100,20,100,["Entrar no quarto?","S/N"])
    porta_quarto.image.fill((209,176,12))
    all_sprite_list.add(porta_quarto)

    path_mirror = Interagivel(770,100,20,100,["Uma porta para uma sala estranha.","continuar?","S/N"])
    path_mirror.image.fill((209,176,12))
    all_sprite_list.add(path_mirror)
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.changespeed(-5, 0)
                elif event.key == pygame.K_RIGHT:
                    player.changespeed(5, 0)
                elif event.key == pygame.K_UP:
                    player.changespeed(0, -5)
                elif event.key == pygame.K_DOWN:
                    player.changespeed(0, 5)
                if event.key == pygame.K_s:
                    keyS = True
                if event.key == pygame.K_n:
                    keyn = True
        
            
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.changespeed(5, 0)
                elif event.key == pygame.K_RIGHT:
                    player.changespeed(-5, 0)
                elif event.key == pygame.K_UP:
                    player.changespeed(0, 5)
                elif event.key == pygame.K_DOWN:
                    player.changespeed(0, -5)
                if event.key == pygame.K_s:
                    keyS = False
                if event.key == pygame.K_n:
                    keyn = False
        
        keyset =[keyq,keyw,keye,keyr,keyt,keyy,keyu,keyi,keyo,keyp,keya,keyS,keyd,keyf,keyg,keyh,keyj,keyk,keyl,keyz,keyx,keyc,keyv,keyb,keyn,keym,backspace,space]
        all_sprite_list.update()
        #transição para quarto
        if porta_quarto.sayhi(player,textbox,fonte) and keyset[11]:
            all_sprite_list.remove(porta_quarto)
            all_sprite_list.remove(path_mirror)
            visited_garden = True
            quarto(visited_basement,visited_garden,inv_faca)
        #transição para labirinto de espelhos
        if path_mirror.sayhi(player,textbox,fonte) and keyset[11]:
            all_sprite_list.remove(porta_quarto)
            all_sprite_list.remove(path_mirror)
            mirror_room()
        screen.fill((22,119,35))
        all_sprite_list.draw(screen)
        textbox.image.fill(BLUE)
        pygame.display.flip()
    
        clock.tick(60)

def mirror_room():
    done = False
    keyq = False
    keyw = False
    keye = False
    keyr = False
    keyt = False
    keyy = False
    keyu = False
    keyi = False
    keyo = False
    keyp = False
    keya = False
    keyS = False
    keyd = False
    keyf = False
    keyg = False
    keyh = False
    keyj = False
    keyk = False
    keyl = False
    keyz = False
    keyx = False
    keyc = False
    keyv = False
    keyb = False
    keyn = False
    keym = False
    backspace = False   
    space = False
    all_sprite_list.remove(player)
    guyf2 = pygame.transform.scale(guyF,(60,60))
    guyb2= pygame.transform.scale(guyB,(60,60))
    guyl2 = pygame.transform.scale(guyL,(60,60))
    guyr2= pygame.transform.scale(guyR,(60,60))
    player2 = Player(100, 10,60,60)
    player2.definirImagem(guyf2,guyb2,guyl2,guyr2)
    player2.walls = wall_list
    all_sprite_list.add(player2)

    player.rect.x = 30
    player.rect.y=100
    path_forest = Interagivel(770,100,20,100,["A saida leva para um bosque","proceder?","S/N"])
    path_forest.image.fill((209,176,12))
    all_sprite_list.add(path_forest)

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player2.changespeed(-5, 0)
                elif event.key == pygame.K_RIGHT:
                    player2.changespeed(5, 0)
                elif event.key == pygame.K_UP:
                    player2.changespeed(0, -5)
                elif event.key == pygame.K_DOWN:
                    player2.changespeed(0, 5)
                if event.key == pygame.K_s:
                    keyS = True
                if event.key == pygame.K_n:
                    keyn = True
        
            
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player2.changespeed(5, 0)
                elif event.key == pygame.K_RIGHT:
                    player2.changespeed(-5, 0)
                elif event.key == pygame.K_UP:
                    player2.changespeed(0, 5)
                elif event.key == pygame.K_DOWN:
                    player2.changespeed(0, -5)
                if event.key == pygame.K_s:
                    keyS = False
                if event.key == pygame.K_n:
                    keyn = False
        
        keyset =[keyq,keyw,keye,keyr,keyt,keyy,keyu,keyi,keyo,keyp,keya,keyS,keyd,keyf,keyg,keyh,keyj,keyk,keyl,keyz,keyx,keyc,keyv,keyb,keyn,keym,backspace,space]
        all_sprite_list.update()

        if path_forest.sayhi(player2,textbox,fonte) and keyset[11]:
            all_sprite_list.remove(path_forest)
            all_sprite_list.remove(player2)
            all_sprite_list.add(player)
            forest()

        screen.fill((WHITE))
        all_sprite_list.draw(screen)
        textbox.image.fill(BLUE)
        pygame.display.flip()
    
        clock.tick(60)
def forest():
    done = False
    keyq = False
    keyw = False
    keye = False
    keyr = False
    keyt = False
    keyy = False
    keyu = False
    keyi = False
    keyo = False
    keyp = False
    keya = False
    keyS = False
    keyd = False
    keyf = False
    keyg = False
    keyh = False
    keyj = False
    keyk = False
    keyl = False
    keyz = False
    keyx = False
    keyc = False
    keyv = False
    keyb = False
    keyn = False
    keym = False
    backspace = False   
    space = False
    player.rect.x = 30
    player.rect.y=100
    porta_quarto = Interagivel(10,100,20,100,["Entrar no quarto?","S/N"])
    porta_quarto.image.fill((209,176,12))
    all_sprite_list.add(porta_quarto)
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.changespeed(-5, 0)
                elif event.key == pygame.K_RIGHT:
                    player.changespeed(5, 0)
                elif event.key == pygame.K_UP:
                    player.changespeed(0, -5)
                elif event.key == pygame.K_DOWN:
                    player.changespeed(0, 5)
                if event.key == pygame.K_s:
                    keyS = True
                if event.key == pygame.K_n:
                    keyn = True
        
            
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.changespeed(5, 0)
                elif event.key == pygame.K_RIGHT:
                    player.changespeed(-5, 0)
                elif event.key == pygame.K_UP:
                    player.changespeed(0, 5)
                elif event.key == pygame.K_DOWN:
                    player.changespeed(0, -5)
                if event.key == pygame.K_s:
                    keyS = False
                if event.key == pygame.K_n:
                    keyn = False
        
        keyset =[keyq,keyw,keye,keyr,keyt,keyy,keyu,keyi,keyo,keyp,keya,keyS,keyd,keyf,keyg,keyh,keyj,keyk,keyl,keyz,keyx,keyc,keyv,keyb,keyn,keym,backspace,space]
        all_sprite_list.update()

        if porta_quarto.sayhi(player,textbox,fonte) and keyset[11]:
            all_sprite_list.remove(porta_quarto)
            visited_garden = True
            quarto(visited_basement,visited_garden,inv_faca)

        screen.fill((22,119,35))
        all_sprite_list.draw(screen)
        textbox.image.fill(BLUE)
        pygame.display.flip()

        clock.tick(60)

def final_room():
    done = False
    keyq = False
    keyw = False
    keye = False
    keyr = False
    keyt = False
    keyy = False
    keyu = False
    keyi = False
    keyo = False
    keyp = False
    keya = False
    keyS = False
    keyd = False
    keyf = False
    keyg = False
    keyh = False
    keyj = False
    keyk = False
    keyl = False
    keyz = False
    keyx = False
    keyc = False
    keyv = False
    keyb = False
    keyn = False
    keym = False
    backspace = False   
    space = False
    player.rect.x = 30
    player.rect.y=100
    porta_quarto = Interagivel(10,100,20,100,["Entrar no quarto?","S/N"])
    porta_quarto.image.fill((209,176,12))
    all_sprite_list.add(porta_quarto)

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.changespeed(-5, 0)
                elif event.key == pygame.K_RIGHT:
                    player.changespeed(5, 0)
                elif event.key == pygame.K_UP:
                    player.changespeed(0, -5)
                elif event.key == pygame.K_DOWN:
                    player.changespeed(0, 5)
                if event.key == pygame.K_s:
                    keyS = True
                if event.key == pygame.K_n:
                    keyn = True
            
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.changespeed(5, 0)
                elif event.key == pygame.K_RIGHT:
                    player.changespeed(-5, 0)
                elif event.key == pygame.K_UP:
                    player.changespeed(0, 5)
                elif event.key == pygame.K_DOWN:
                    player.changespeed(0, -5)
                if event.key == pygame.K_s:
                    keyS = False
                if event.key == pygame.K_n:
                    keyn = False
        
        keyset =[keyq,keyw,keye,keyr,keyt,keyy,keyu,keyi,keyo,keyp,keya,keyS,keyd,keyf,keyg,keyh,keyj,keyk,keyl,keyz,keyx,keyc,keyv,keyb,keyn,keym,backspace,space]
        all_sprite_list.update()

        if porta_quarto.sayhi(player,textbox,fonte) and keyset[11]:
            all_sprite_list.remove(porta_quarto)
            visited_garden = True
            quarto(visited_basement,visited_garden,inv_faca)

        screen.fill((22,119,35))
        all_sprite_list.draw(screen)
        textbox.image.fill(BLUE)
        pygame.display.flip()

        clock.tick(60)
def loop_principal():
    done = False
    while not done:
        quarto(visited_basement,visited_garden,inv_faca)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                quit()
            
loop_principal()
pygame.quit()