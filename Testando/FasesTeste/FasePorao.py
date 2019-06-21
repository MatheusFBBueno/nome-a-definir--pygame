import pygame
from Fases.player import Player
from Fases.wall import Wall

def fasePorao():
    guy = pygame.image.load('images/dood.png')
    camac = pygame.image.load('images/bed.png')

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    BLUE = (50, 50, 255)
    LIME = (26, 242, 152)
    NADA = (255,255,255,0)
    marrom_bombom = (188, 100, 28)

    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    background = pygame.image.load("images/FasePorao.png")

    pygame.init()
    fonte = pygame.font.Font('pokemon_fire_red.ttf', 24)

    guyF = pygame.image.load('images/dood_frontal.png')
    guyL = pygame.image.load('images/dood_left.png')
    guyR = pygame.image.load('images/dood_right.png')
    guyB = pygame.image.load('images/dood_back.png')
    guyF = pygame.transform.scale(guyF,(100,100))
    guyL = pygame.transform.scale(guyL,(100,100))
    guyR = pygame.transform.scale(guyR,(100,100))
    guyB = pygame.transform.scale(guyB,(100,100))

    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

    pygame.display.set_caption('Test')

    # lista de sprites
    all_sprite_list = pygame.sprite.Group()

    # paredes (x_pos, y_pos, width, height)
    wall_list = pygame.sprite.Group()

    wall = Wall(0, 0, 0, 600)
    wall_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(10, 0, 790, 0)
    wall_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(790, 0, 0, 590)
    wall_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(0, 590, 790, 0)
    wall_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    #---

    wall = Wall(180, 170, 10, 10)
    wall_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(NADA)

    wall = Wall(450, 100, 790, 10)
    wall_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(NADA)

    wall = Wall(380, 0, 10, 110)
    wall_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(NADA)

    wall = Wall(230, 150, 10, 10)
    wall_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(NADA)

    wall = Wall(280, 130, 10, 10)
    wall_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(NADA)

    wall = Wall(320, 110, 10, 10)
    wall_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(NADA)


    #---

    '''
    cama = Interagivel(10, 10, 100, 100, ["time", "to", "sleep"])
    camac = pygame.transform.scale(camac, (100, 100))
    wall_list.add(cama)
    all_sprite_list.add(cama)
    cama.carregarImagem(camac)
    '''

    textbox = Wall(10, 500, 780, 90)
    textbox.image.fill(BLUE)
    wall_list.add(textbox)
    all_sprite_list.add(textbox)

    # Jogador
    player = Player(200, 10,100,100)
    guy = pygame.transform.scale(guy, (100, 100))
    player.definirImagem(guyF,guyB,guyL,guyR)
    player.walls = wall_list
    all_sprite_list.add(player)

    clock = pygame.time.Clock()
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
    chave1 = False
    chave2 = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.changespeed(-5, 0)
                elif event.key == pygame.K_RIGHT:
                    player.changespeed(5, 0)
                elif event.key == pygame.K_UP:
                    player.changespeed(0, -5)
                elif event.key == pygame.K_DOWN:
                    player.changespeed(0, 5)
                if event.key == pygame.K_q:
                    keyq = True
                if event.key == pygame.K_w:
                    keyw = True
                if event.key == pygame.K_e:
                    keye = True
                if event.key == pygame.K_r:
                    keyr = True
                if event.key == pygame.K_t:
                    keyt = True
                if event.key == pygame.K_y:
                    keyy = True
                if event.key == pygame.K_u:
                    keyu = True
                if event.key == pygame.K_i:
                    keyi = True
                if event.key == pygame.K_o:
                    keyo = True
                if event.key == pygame.K_p:
                    keyp = True
                if event.key == pygame.K_a:
                    keya = True
                if event.key == pygame.K_s:
                    keyS = True
                if event.key == pygame.K_d:
                    keyd = True
                if event.key == pygame.K_f:
                    keyf = True
                if event.key == pygame.K_g:
                    keyg = True
                if event.key == pygame.K_h:
                    keyh = True
                if event.key == pygame.K_j:
                    keyj = True
                if event.key == pygame.K_k:
                    keyk = True
                if event.key == pygame.K_l:
                    keyl = True
                if event.key == pygame.K_z:
                    keyz = True
                if event.key == pygame.K_x:
                    keyx = True
                if event.key == pygame.K_c:
                    keyc = True
                if event.key == pygame.K_v:
                    keyv = True
                if event.key == pygame.K_b:
                    keyb = True
                if event.key == pygame.K_n:
                    keyn = True
                if event.key == pygame.K_m:
                    keym = True
                if event.key == pygame.K_BACKSPACE:
                    backspace = True
                if event.key == pygame.K_SPACE:
                    space = True


            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.changespeed(5, 0)
                elif event.key == pygame.K_RIGHT:
                    player.changespeed(-5, 0)
                elif event.key == pygame.K_UP:
                    player.changespeed(0, 5)
                elif event.key == pygame.K_DOWN:
                    player.changespeed(0, -5)
                if event.key == pygame.K_q:
                    keyq = False
                if event.key == pygame.K_w:
                    keyw = False
                if event.key == pygame.K_e:
                    keye = False
                if event.key == pygame.K_r:
                    keyr = False
                if event.key == pygame.K_t:
                    keyt = False
                if event.key == pygame.K_y:
                    keyy = False
                if event.key == pygame.K_u:
                    keyu = False
                if event.key == pygame.K_i:
                    keyi = False
                if event.key == pygame.K_o:
                    keyo = False
                if event.key == pygame.K_p:
                    keyp = False
                if event.key == pygame.K_a:
                    keya = False
                if event.key == pygame.K_s:
                    keyS = False
                if event.key == pygame.K_d:
                    keyd = False
                if event.key == pygame.K_f:
                    keyf = False
                if event.key == pygame.K_g:
                    keyg = False
                if event.key == pygame.K_h:
                    keyh = False
                if event.key == pygame.K_j:
                    keyj = False
                if event.key == pygame.K_k:
                    keyk = False
                if event.key == pygame.K_l:
                    keyl = False
                if event.key == pygame.K_z:
                    keyz = False
                if event.key == pygame.K_x:
                    keyx = False
                if event.key == pygame.K_c:
                    keyc = False
                if event.key == pygame.K_v:
                    keyv = False
                if event.key == pygame.K_b:
                    keyb = False
                if event.key == pygame.K_n:
                    keyn = False
                if event.key == pygame.K_m:
                    keym = False
                if event.key == pygame.K_BACKSPACE:
                    backspace = False
                if event.key == pygame.K_SPACE:
                    space = False

        keyset = [keyq, keyw, keye, keyr, keyt, keyy, keyu, keyi, keyo, keyp, keya, keyS, keyd, keyf, keyg, keyh, keyj,
                  keyk, keyl, keyz, keyx, keyc, keyv, keyb, keyn, keym, backspace, space]
        all_sprite_list.update()

        screen.blit(background, (0, 0))

        all_sprite_list.draw(screen)
        textbox.image.fill(BLUE)
        pygame.display.flip()

        clock.tick(60)

pygame.quit()