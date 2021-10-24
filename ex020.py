#Faça um programa em python que abra e reproduza áudio de um arquivo mp3
import pygame
pygame.mixer.init()
pygame.mixer.music.load('TremDasOnze.mp3')
input()
pygame.event.wait()
