import pygame
import random
import time
from color_palette import *

pygame.init()

WIDTH = 600
HEIGHT = 600
CELL = 30
GRID_WIDTH = WIDTH // CELL
GRID_HEIGHT = HEIGHT // CELL
FPS = 5  

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Змейка NEW")

def draw_grid(): #сетка
    for i in range(GRID_WIDTH):
        for j in range(GRID_HEIGHT):
            pygame.draw.rect(screen, colorGRAY, (i * CELL, j * CELL, CELL, CELL), 1)

def draw_grid_chess(): #фон
    colors = [colorWHITE, colorGRAY]
    for i in range(GRID_WIDTH):
        for j in range(GRID_HEIGHT):
            pygame.draw.rect(screen, colors[(i + j) % 2], (i * CELL, j * CELL, CELL, CELL))

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x}, {self.y}"

class Snake:
    def __init__(self):
        self.body = [Point(10, 11), Point(10, 12), Point(10, 13)]
        self.dx = 1  # Направление по X
        self.dy = 0  # Направление по Y
        self.score = 0
        self.level = 1
        self.food_eaten = 0
        self.food_to_next_level = 3

    def move(self):
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y
        
        self.body[0].x += self.dx
        self.body[0].y += self.dy

    def draw(self):
        head = self.body[0]
        pygame.draw.rect(screen, colorRED, (head.x * CELL, head.y * CELL, CELL, CELL))
        for segment in self.body[1:]:
            pygame.draw.rect(screen, colorYELLOW, (segment.x * CELL, segment.y * CELL, CELL, CELL))

    def check_collision(self, food):
        #проверка столкновения с едой
        head = self.body[0]
        if head.x == food.pos.x and head.y == food.pos.y:
            self.score += food.weight * 5  #Учитываем вес еды
            self.food_eaten += 1
            
            if self.food_eaten >= self.food_to_next_level:
                self.level += 1
                self.food_eaten = 0
                return "level_up"
            
            #Добавляем сегменты в зависимости от веса еды
            for _ in range(food.weight):
                self.body.append(Point(head.x, head.y))
            return True
        return False

    def check_wall_collision(self):
        head = self.body[0]
        return head.x < 0 or head.x >= GRID_WIDTH or head.y < 0 or head.y >= GRID_HEIGHT

    def check_self_collision(self):
        head = self.body[0]
        return any(head.x == segment.x and head.y == segment.y for segment in self.body[1:])

class Food:
    def __init__(self, snake):
        self.weight = random.choice([1, 1, 1, 2, 2, 3])  #Разные веса еды
        self.spawn_time = time.time()  #Время появления
        self.lifetime = random.randint(5, 15)  #Время жизни в секундах
        self.pos = self.generate_position(snake)
        self.color = self.get_color_by_weight()

    def generate_position(self, snake):
        while True:
            x = random.randint(0, GRID_WIDTH - 1)
            y = random.randint(0, GRID_HEIGHT - 1)
            if not any(segment.x == x and segment.y == y for segment in snake.body):
                return Point(x, y)

    def get_color_by_weight(self):
        #Цвет в зависимости от веса
        return {
            1: colorGREEN,   # Обычная еда
            2: colorBLUE,    # Редкая еда
            3: colorPURPLE   # Очень редкая еда
        }.get(self.weight, colorGREEN)

    def is_expired(self):
        #Проверка истекшего времени
        return time.time() - self.spawn_time > self.lifetime

    def draw(self):
        #Отрисовка еды с таймером
        pygame.draw.rect(screen, self.color, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))
        
        #Отрисовка таймера
        remaining_time = max(0, self.lifetime - (time.time() - self.spawn_time))
        timer_text = pygame.font.SysFont(None, 20).render(f"{int(remaining_time)}", True, colorBLACK)
        screen.blit(timer_text, (self.pos.x * CELL + 5, self.pos.y * CELL + 5))

def draw_game_info(snake):
    font = pygame.font.SysFont(None, 36)
    score_text = font.render(f"Score: {snake.score}", True, colorBLACK)
    level_text = font.render(f"Level: {snake.level}", True, colorBLACK)
    speed_text = font.render(f"Speed: {FPS}", True, colorBLACK)
    
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 50))
    screen.blit(speed_text, (10, 90))

def game_over_screen():
    screen.fill(colorWHITE)
    font = pygame.font.SysFont(None, 72)
    game_over_text = font.render("GAME OVER", True, colorRED)
    screen.blit(game_over_text, (WIDTH//2 - 180, HEIGHT//2 - 50))
    pygame.display.flip()
    pygame.time.wait(2000)

def main():
    global FPS
    clock = pygame.time.Clock()
    snake = Snake()
    food = Food(snake)
    running = True
    game_active = True
    last_food_check = time.time()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and game_active:
                if event.key == pygame.K_RIGHT and snake.dx != -1:
                    snake.dx, snake.dy = 1, 0
                elif event.key == pygame.K_LEFT and snake.dx != 1:
                    snake.dx, snake.dy = -1, 0
                elif event.key == pygame.K_DOWN and snake.dy != -1:
                    snake.dx, snake.dy = 0, 1
                elif event.key == pygame.K_UP and snake.dy != 1:
                    snake.dx, snake.dy = 0, -1

        if game_active:
            draw_grid_chess()
            snake.move()
            
            #Проверка столкновений
            if snake.check_wall_collision() or snake.check_self_collision():
                game_active = False
                game_over_screen()
                break
            
            #Проверка еды каждые 0.5 секунды
            if time.time() - last_food_check > 0.5:
                if food.is_expired():
                    food = Food(snake)
                last_food_check = time.time()
            
            #Проверка съедения еды
            result = snake.check_collision(food)
            if result == "level_up":
                FPS += 1
                food = Food(snake)
            elif result:
                food = Food(snake)
            
            snake.draw()
            food.draw()
            draw_game_info(snake)
            
            pygame.display.flip()
            clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()