import pygame, random
from pygame.math import Vector2


class Food:
    def __init__(self):
        self.position = Vector2(5, 6) 

class Snake:
    def __init__(self):
        self.body = [Vector2(6,9), Vector2(5, 9), Vector2(4, 9)]
        self.direction = Vector2(1,0)
        self.addSegment = False
        self.eatSound = pygame.mixer.Sound("Sounds/eat.mp3")
        self.wallSound = pygame.mixer.Sound("Sounds/wall.mp3")
    
    def update(self):
        self.body.insert(0, self.body[0] + self.direction) 
        if self.addSegment == False:
            self.body = self.body[:-1]
        else:
            self.addSegment = False
    def reset(self):
        self.body = [Vector2(6,9), Vector2(5, 9), Vector2(4, 9)]
        self.direction = Vector2(1,0)
        self.addSegment = False 
    
    
        