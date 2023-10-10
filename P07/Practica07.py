import pygame
import time

pygame.init()


velx1 = 0
vely1 = 5
velx2 = 5
vely2 = 0
terminar = False
win = pygame.display.set_mode((760,640)) 

img1 = pygame.image.load("1.png")
img2 = pygame.image.load("2.png")
tam_image1 = img1.get_rect()
tam_image2 = img2.get_rect()
tam_image1.left = 230
tam_image1.top = 200
tam_image2.left = 230
tam_image2.top = 500


while not terminar:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: terminar = True
    tam_image1.left += velx1
    tam_image1.top += vely1
    tam_image2.left += velx2
    tam_image2.top += vely2
    if tam_image1.left <= 0 or tam_image1.right >= 760.0:
        velx1 =- velx1
    if tam_image1.top <= 0 or tam_image1.bottom >= 640.0:
        vely1 =- vely1
    if tam_image2.left <= 0 or tam_image2.right >= 760.0:
        velx2 =- velx2
    if tam_image2.top <= 0 or tam_image2.bottom >= 640.0:
        vely2 =- vely2
    time.sleep(0.01)
    win.fill((0,0,0))
    win.blit(img1,tam_image1)
    #win.fill((0,0,0))
    win.blit(img2,tam_image2)
    pygame.display.flip()
pygame.quit()


