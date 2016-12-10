import pygame as pg
import sys


class objeto:
    def __init__(self, path, puntos, velocidad):
        self.startPosition = 0,0
        self.puntos = puntos
        self.image = pg.image.load(path)
        self.image = pg.transform.scale(self.image, (20,20))
        self.rect = self.image.get_rect().move(self.startPosition)
        self.defaultMovement = velocidad
        self.previousRect = self.rect

    def render(self, surface):
        self.previousRect = self.rect.copy()
        surface.fill((255,255,255),  self.previousRect)
        self.rect.top+=self.defaultMovement
        surface.blit(self.image, self.rect)


class personaje:
    def __init__(self, surface):
        self.startPosition = 0,325
        self.endPosition = 0,520
        self.image = pg.image.load("assets/kiper.jpg")
        self.image = pg.transform.scale(self.image, (75,75))
        self.rect = self.image.get_rect().move(self.startPosition)
        self.defaultMovement = 40
        self.previousRect = self.rect


    def render(self, surface):
        surface.fill((255,255,255),  self.previousRect)
        surface.blit(self.image, self.rect)

    def move(self, key):
        self.previousRect = self.rect.copy()
        if key == pg.K_LEFT and self.rect.left > 0:
            self.rect.left -= self.defaultMovement

        if key == pg.K_RIGHT and self.rect.left <= self.endPosition[1]:
            self.rect.left += self.defaultMovement

