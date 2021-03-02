
#====DESAFIO PYTHON 19 CV ====

#Programa para abrir e reproduzir um aúdio em Mp3

import pygame

pygame.mixer.init()

pygame.mixer.music.load("manual.mp3")
pygame.mixer.music.play()
pygame.mixer.music.set_volume(1)
input('Agora você escuta?')