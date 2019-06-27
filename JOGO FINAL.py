import pygame
from random import *
import math

try:
    pygame.init()

except:
    print("ERRO IMPORTAÇÃO PYGAME")

#### RANDOM ####


rd1 = randint(0, 10)
rd2 = randint(1, 500)
rd3 = randint(1, 500)
rd4 = randint(1, 500)

UL_x = 50
UL_y = 70

#### UL ######

#Esquerda
UL_ang_left = randint(90, 270)
UL_ang_right = randint(18, 19)
UL_ang_up = randint(19, 21)

ang = randint(0, 360)

#### VIDEO ####

Wid = 500
Hei = 500

Win = pygame.display.set_mode((Wid, Hei))
pygame.display.set_caption("GENIUS", )

ZZ = 500
XX = 30

#### PLAYER ###

X = Wid / 2
Y = Hei / 2
Size = 50


#### COLORS ####

White = 255, 255, 255

Al = 230, 230, 230

Black = 0, 0, 0

Blue = 0, 0, 255

Red = 255, 0, 0


#### OBJECTS ###


ovel = 7

#### RUN #####

Main = True
PosXY = False
Start = False

while Main:
    clock = pygame.time.Clock()
    clock.tick(30)
    pygame.display.init()
    Win.fill((Al))

    pygame.display.update()

    #### CREAT ####
    Win.fill((Al))


    #### OBJETOS ####
    Rect_Up_Left = pygame.draw.rect(Win, Blue, ((UL_x, UL_y), (100, 70)))
    Rect_Up_Right = pygame.draw.rect(Win, Blue, ((400, 70), (50, 70)))
    Rect_Down_Left = pygame.draw.rect(Win, Blue, ((100, 350), (50, 90)))
    Rect_Down_Right = pygame.draw.rect(Win, Blue, ((300, 330), (150, 45)))

    ##### BORDAS #####
    Borda_Down = pygame.draw.rect(Win, Black, ((0, 470), (ZZ, XX)))
    Borda_Up = pygame.draw.rect(Win, Black, ((0, 0), (ZZ, XX)))
    Borda_Left = pygame.draw.rect(Win, Black, ((0, 0), (XX, ZZ)))
    Borda_Right = pygame.draw.rect(Win, Black, ((470, 0), (XX, ZZ)))
    #pygame.draw.rect(JANELA, COR, ((POSICAO), (TAMANHO)))


    #### PLAYER #####
    Player = pygame.draw.rect(Win, Red, (X - Size / 2, Y - Size / 2, Size, Size))
    pygame.display.update()



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            Start = True
            Main = False

        print(event)

    pygame.display.update()








while Start:
    pygame.display.init()
    clock = pygame.time.Clock()
    clock.tick(60)
    Win.fill((Al))

    pygame.display.update()

    ##### BORDAS #####
    Borda_Down = pygame.draw.rect(Win, Black, ((0, 470), (ZZ, XX)))
    Borda_Up = pygame.draw.rect(Win, Black, ((0, 0), (ZZ, XX)))
    Borda_Left = pygame.draw.rect(Win, Black, ((0, 0), (XX, ZZ)))
    Borda_Right = pygame.draw.rect(Win, Black, ((470, 0), (XX, ZZ)))
    #pygame.draw.rect(JANELA, COR, ((POSICAO), (TAMANHO)))

    #### RECT ###
    UL_x = UL_x + ovel * math.cos(ang)
    UL_y = UL_y - ovel * math.sin(ang)


    Rect_Up_Left = pygame.draw.rect(Win, Blue, ((UL_x, UL_y), (100, 70)))

    if (Rect_Up_Left.colliderect(Borda_Left) or UL_x <= 0) and 90 <= ang <= 270 :
        print("COLLIDIU Borda Esquerda")
        ang = ang - 180

    if (Rect_Up_Left.colliderect(Borda_Right) or UL_x >= 360) and 18 <= ang <= 19:
        print("COLLIDIU Borda Direita")
        ang = ang - 180

    if (Rect_Up_Left.colliderect(Borda_Down) or UL_y <= 0) and 180 < ang < 360:
        print("COLLIDIU Borda Baixo")
        ang = 180 - ang

    if Rect_Up_Left.colliderect(Borda_Up) and 21 <= ang <= 19:
        print("COLLIDIU Borda Cima")

        ang = ang - 180

    ang = ang % 360
    print(ang)
    #### COLISAO ####

    Rect_Up_Right = pygame.draw.rect(Win, Blue, ((400, 70), (50, 70)))
    Rect_Down_Left = pygame.draw.rect(Win, Blue, ((100, 350), (50, 90)))
    Rect_Down_Right = pygame.draw.rect(Win, Blue, ((300, 330), (150, 45)))


    ##### player #####
    Player = pygame.draw.rect(Win, Red, (X - Size / 2, Y - Size / 2, Size, Size))

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        print()
        X, Y = pygame.mouse.get_pos()

    #### COLLIDE ####





    #if Player.colliderect(Rect_Up_Left):
        #print("COLLIDIU Rect_Up_Left")
    #if Player.colliderect(Rect_Up_Right):
        #print("COLLIDIU Rect_Up_Right")
    #if Player.colliderect(Rect_Down_Left):
        #print("COLLIDIU Rect_Down_Left")
    #if Player.colliderect(Rect_Down_Right):
        #print("COLLIDIU Rect_Down_Right")


    #if Player.colliderect(Borda_Right):
        #print("PLAYER COLLIDIU BORDA DIREITA")
    #if Player.colliderect(Borda_Left):
        #print("PLAYER COLLIDIU BORDA ESQUERDA")
    #if Player.colliderect(Borda_Up):
        #print("PALYER COLLIDIU BORDA CIMA")
    #if Player.colliderect(Borda_Down):
        #print("PLAYER COLLIDIU BORDA BAIXO")


    pygame.display.update()

    pygame.display.flip()

    clock.tick(60)

pygame.quit()

