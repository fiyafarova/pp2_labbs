import pygame
import random
from color_palette import *

pygame.init()

WIDTH = 600
HEIGHT = 600
CELL = 30
GRID_WIDTH = WIDTH // CELL  # Ширина 
GRID_HEIGHT = HEIGHT // CELL  # Высота
FPS = 5  #начальная скорость игры

#экран
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Змейка")

def draw_grid(): #сетка на экране
    for i in range(GRID_WIDTH):
        for j in range(GRID_HEIGHT):
            pygame.draw.rect(screen, colorGRAY, (i * CELL, j * CELL, CELL, CELL), 1)


def draw_grid_chess():    #шахматный фон
    colors = [colorWHITE, colorGRAY]
    for i in range(GRID_WIDTH):
        for j in range(GRID_HEIGHT):
            pygame.draw.rect(screen, colors[(i + j) % 2], (i * CELL, j * CELL, CELL, CELL))


class Point: #класс для представления точки/позиции на сетке
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x}, {self.y}"

class Snake: #змейка
    def __init__(self):
        #начальное тело змейки
        self.body = [Point(10, 11), Point(10, 12), Point(10, 13)]
        self.dx = 1  #направление по горизонтали
        self.dy = 0  #направление по вертикали
        self.score = 0  #счет игрока
        self.level = 1  #текущий уровень
        self.food_eaten = 0  #съеденная еда
        self.food_to_next_level = 3  #еды для перехода на след уровень

    def move(self): #движение змейки
       
        #перемещение каждого сегмента в позицию предыдущего
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y

        #перемещение головы в соответствии с направлением
        self.body[0].x += self.dx
        self.body[0].y += self.dy

    def draw(self):       #отрисовка змейки
        head = self.body[0]
        pygame.draw.rect(screen, colorRED, (head.x * CELL, head.y * CELL, CELL, CELL)) # голова красная
        for segment in self.body[1:]: # тело желтое
            pygame.draw.rect(screen, colorYELLOW, (segment.x * CELL, segment.y * CELL, CELL, CELL))

    def check_collision(self, food):   #Проверка столкновения с едой

        head = self.body[0]
        if head.x == food.pos.x and head.y == food.pos.y:
            self.score += 10
            self.food_eaten += 1

            if self.food_eaten >= self.food_to_next_level:   #Проверка перехода на новый уровень
                self.level += 1
                self.food_eaten = 0
                return "level_up"
            
            self.body.append(Point(head.x, head.y))  #Добавление нового сегмента
            return True
        return False

    def check_wall_collision(self):     #Проверка столкновения со стенами
        head = self.body[0]
        if head.x < 0 or head.x >= GRID_WIDTH or head.y < 0 or head.y >= GRID_HEIGHT:
            return True
        return False

    def check_self_collision(self):       #Проверка столкновения с собой
        
        head = self.body[0]
        for segment in self.body[1:]:
            if head.x == segment.x and head.y == segment.y:
                return True
        return False

class Food:  #еда
    def __init__(self, snake):
        self.pos = self.generate_position(snake)

    def generate_position(self, snake):        #генерация случайной позиции для еды
        while True:
            x = random.randint(0, GRID_WIDTH - 1)
            y = random.randint(0, GRID_HEIGHT - 1)
            #проверка, что позиция не на змейке
            valid_position = True
            for segment in snake.body:
                if segment.x == x and segment.y == y:
                    valid_position = False
                    break
            if valid_position:
                return Point(x, y)

    def draw(self):
        #отрисовка еды зеленая
        pygame.draw.rect(screen, colorGREEN, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))

def draw_score_and_level(snake):
    #отображение счета и уровня
    font = pygame.font.SysFont(None, 36)
    score_text = font.render(f"Score: {snake.score}", True, colorBLACK)
    level_text = font.render(f"Level: {snake.level}", True, colorBLACK)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 50))

def game_over_screen():
    #экран окончания игры
    screen.fill(colorWHITE)
    font = pygame.font.SysFont(None, 72)
    game_over_text = font.render("GAME OVER", True, colorRED)
    screen.blit(game_over_text, (WIDTH//2 - 180, HEIGHT//2 - 50))
    pygame.display.flip()
    pygame.time.wait(2000)

def main():
    clock = pygame.time.Clock()
    snake = Snake()
    food = Food(snake)
    running = True
    game_active = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and game_active:
                # Управление змейкой
                if event.key == pygame.K_RIGHT and snake.dx != -1:
                    snake.dx = 1
                    snake.dy = 0
                elif event.key == pygame.K_LEFT and snake.dx != 1:
                    snake.dx = -1
                    snake.dy = 0
                elif event.key == pygame.K_DOWN and snake.dy != -1:
                    snake.dx = 0
                    snake.dy = 1
                elif event.key == pygame.K_UP and snake.dy != 1:
                    snake.dx = 0
                    snake.dy = -1

        if game_active:
            #отрисовка игровых элементов
            draw_grid_chess()
            snake.move()
            
            #проверка столкновений
            if snake.check_wall_collision() or snake.check_self_collision():
                game_active = False
                game_over_screen()
                break
            
            #проверка съедения еды
            result = snake.check_collision(food)
            if result == "level_up":
                #увеличение скорости на новом уровне
                global FPS
                FPS += 1
                food = Food(snake)
            elif result:
                food = Food(snake)
            
            #отрисовка игровых элементов
            snake.draw()
            food.draw()
            draw_score_and_level(snake)
            
            pygame.display.flip()
            clock.tick(FPS)
        

    pygame.quit()

if __name__ == "__main__":
    main()