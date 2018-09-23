import pygame
from pygame.locals import *


# An advanced sprite class, subclassing PyGame's own Sprite
class Entity(pygame.sprite.Sprite):

    def __init__(self, src, x_pos, y_pos, w, h):
        pygame.sprite.Sprite.__init__(self)
        self.src = src
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.w = w
        self.h = h
        self.image = pygame.image.load(src)
        self.rect = Rect(self.x_pos, self.y_pos, self.w, self.h)

    def update(self, x_pos, y_pos):
        self.rect.x = x_pos
        self.rect.y = y_pos

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def __copy__(self):
        return type(self)(self.src, self.x_pos, self.y_pos, self.w, self.h)
