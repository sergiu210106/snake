import pygame, random, colors
from food import Food
from pygame.math import Vector2
from food import Snake

class Game:
    def __init__(self):
        self.state = "RUNNING"
        self.windowSize = 750
        self.cellSize = 30
        self.numberOfCells = 25
        self.OFFSET = 75
        self.food = Food()
        self.snake = Snake()
        self.food.position = self.generateRandomFoodPos()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.windowSize + 2 * self.OFFSET, self.windowSize + 2 * self.OFFSET))
        self.titleFont = pygame.font.Font(None, 60)
        self.scoreFont = pygame.font.Font(None, 40)
        self.score = 0
        pygame.display.set_caption("Snake")
    def generateRandomCell(self):
        x = random.randint(0, self.numberOfCells - 1)
        y = random.randint(0, self.numberOfCells - 1)
        return Vector2(x, y)
    def generateRandomFoodPos(self):
        position = self.generateRandomCell()
        while position in self.snake.body:
            position = self.generateRandomCell()
        return position
    def draw(self):
        #food
        foodRect = pygame.Rect(self.OFFSET + self.food.position.x * self.cellSize, 
                               self.OFFSET + self.food.position.y * self.cellSize, 
                               self.cellSize, self.cellSize)
        foodSurface = pygame.image.load("food.png")
        self.screen.blit(foodSurface, foodRect) 
        
        for segment in self.snake.body:
            segmentRect = pygame.Rect(self.OFFSET + segment.x * self.cellSize,
                                      self.OFFSET + segment.y * self.cellSize,
                                      self.cellSize, self.cellSize)
            pygame.draw.rect(self.screen, colors.darkGreen, segmentRect, 0, 7)
            
            
    def checkCollisionWithFood(self):
        if self.snake.body[0] == self.food.position:
            self.food.position = self.generateRandomFoodPos()
            self.snake.addSegment = True
            self.score += 1
            self.snake.eatSound.play()
    def checkCollisionWithWalls(self):
        if self.snake.body[0].x >= self.numberOfCells or self.snake.body[0].x < 0:
            self.gameOver()
        if self.snake.body[0].y >= self.numberOfCells or self.snake.body[0].y < 0:
            self.gameOver()
    def checkCollisionsWithTail(self):
        headlessBody = self.snake.body[1:]
        if self.snake.body[0] in headlessBody:
            self.gameOver()
    def checkCollisions(self):
        self.checkCollisionWithFood()
        self.checkCollisionWithWalls()
        self.checkCollisionsWithTail()
    def update(self):
        self.screen.fill(colors.green)
        self.checkCollisions()
        self.draw()
        pygame.draw.rect(self.screen, colors.darkGreen, (self.OFFSET - 5, self.OFFSET - 5, self.windowSize + 10, self.windowSize + 10), 5)
        
        titleSurface = self.titleFont.render("Retro Snake", True, colors.darkGreen)
        self.screen.blit(titleSurface, (self.OFFSET - 5, 20))
        
        scoreSurface = self.scoreFont.render(str(self.score), True, colors.darkGreen)
        self.screen.blit(scoreSurface, (self.OFFSET - 5, self.OFFSET + self.windowSize + 10))
        
        pygame.display.update()
        self.clock.tick(60)
    def gameOver(self):
        self.snake.reset()
        self.food.position = self.generateRandomFoodPos()
        self.state = "STOPPED"
        self.score = 0
        self.snake.wallSound.play()
