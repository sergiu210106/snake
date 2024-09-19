import pygame, sys
from game import Game
from food import Food
import colors
from pygame.math import Vector2

pygame.init()

game = Game()

SNAKEUPDATE = pygame.USEREVENT
pygame.time.set_timer(SNAKEUPDATE, 200)

while True:
    for event in pygame.event.get():
        if event.type == SNAKEUPDATE and game.state == "RUNNING":
            game.snake.update()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if event.type == pygame.KEYDOWN:
            if game.state == "STOPPED":
                game.state = "RUNNING"
            if event.key == pygame.K_UP and game.snake.direction != Vector2(0, 1):
                game.snake.direction = Vector2(0, -1)
            if event.key == pygame.K_DOWN and game.snake.direction != Vector2(0, -1):
                game.snake.direction = Vector2(0, 1)
            if event.key == pygame.K_LEFT and game.snake.direction != Vector2(1, 0):
                game.snake.direction = Vector2(-1, 0)
            if event.key == pygame.K_RIGHT and game.snake.direction != Vector2(-1, 0):
                game.snake.direction = Vector2(1, 0)

    game.update()