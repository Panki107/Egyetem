import pygame
import sys
import time
import random

pygame.init()

WIDTH=800
HEIGHT=600
font = pygame.font.SysFont("Arial", 36)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Akasztófa béta")

szavak = ["alma", "asztal", "barack", "narancs", "kutya", "macska", "kocsi"]
valasztas = random.randint(0, len(szavak) - 1)
szo = szavak[valasztas]
talalt = []

feher = (255, 255, 255)
piros = (255, 0, 0)
fekete = (0, 0, 0)
zold = (0, 128, 0)

player_pos = [6, 160]
player_size = 90
player_speed = 2

clock = pygame.time.Clock()

db=0
a=True
while a:
    bekertbetu=""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            key = event.key
            bekertbetu=pygame.key.name(key)

    if bekertbetu in szo and bekertbetu != "":
        talalt.append(bekertbetu)
    elif bekertbetu != "":
        player_pos[0] += 90
        db = db+1
    if player_pos[0] < 0:
        player_pos[0] = 0
    if player_pos[0] > WIDTH - player_size:
        player_pos[0] = WIDTH - player_size
    if player_pos[1] < 0:
        player_pos[1] = 0
    if player_pos[1] > HEIGHT - player_size:
        player_pos[1] = HEIGHT - player_size
    szo_display = ""
    for betu in szo:
        if betu in talalt:
            szo_display += betu + " "
        else:
            szo_display += "_ "


    background_image = pygame.image.load("palya.png")
    player_image = pygame.image.load("emberrendes.png")
    player_image = pygame.transform.scale(player_image, (player_size , player_size))

    screen.blit(background_image, (0, 0))
    screen.blit(player_image, player_pos)
    word_surface = font.render(szo_display.strip(), True, fekete)
    screen.blit(word_surface, (420 - word_surface.get_width() // 2, 55))

    text_surface = font.render(f"Hibák száma: {db}", True, fekete)
    screen.blit(text_surface, (10, 70))

    if player_pos[0] >= 630:
        for i in range(2):
            player_pos[1] += 2
            if player_pos[1] >= 480:
                vesztes_üzenet = f"Vesztettél! A helyes szó: a(z) {szo} volt."
                vesztes_üzenet = font.render(vesztes_üzenet, True, piros)
                screen.blit(vesztes_üzenet, (20, 300))
                a = False
                pygame.display.flip()
                time.sleep(3)

    if set(szo) == set(talalt):
        nyertes_üzenet = f"Nyertél! A helyes szó: a(z) {szo} volt."
        nyertes_üzenet = font.render(nyertes_üzenet, True, zold)
        screen.blit(nyertes_üzenet, (20,300))
        pygame.display.flip()
        time.sleep(3)
        for _ in range(10):  # 10 ugrás
            for offset in [10, -10]:  # Fel-le mozgás
                player_pos[1] += offset
                screen.blit(background_image, (0, 0))
                screen.blit(player_image, player_pos)
                screen.blit(word_surface, (420 - word_surface.get_width() // 2, 55))
                screen.blit(text_surface, (10, 70))
                screen.blit(nyertes_üzenet, (20, 300))
                pygame.display.flip()
                time.sleep(0.1)  # Kis késleltetés az animációhoz
    pygame.display.flip()
    clock.tick(30)
