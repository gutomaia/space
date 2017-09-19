import pygame
from kinematic import Kinematic
from consts import Vector
import math


class Player(Kinematic):

    def __init__(self, max_speed=40, max_acceleration=15, weight=0.25):
        super(Player, self).__init__(
            max_speed=max_speed,
            max_acceleration=max_acceleration,
            weight=weight
            )

    def render(self, screen):
        screen.blit(self.image, self.position)


class Missile(Player):

    def __init__(self, position):
        super(Missile, self).__init__(
            max_speed=15,
            max_acceleration=5,
            weight=2
            )

        self.position = position
        self.image = pygame.image.load('assets/PNG/Sprites/Missiles/spaceMissiles_001.png').convert()
        self.image.set_colorkey((255,255,255))

    def render(self,screen):
        rotated = pygame.transform.rotate(self.image, self.direction)
        screen.blit(rotated, self.position)



    def move(interval):
        if self.move != None:
            self.move.play(interval)
