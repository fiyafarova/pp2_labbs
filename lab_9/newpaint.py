import pygame
import sys
import math

pygame.init()

WIDTH, HEIGHT = 800, 600
FPS = 60
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint")
clock = pygame.time.Clock()


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BG_COLOR = WHITE
current_color = BLACK

# Настройки кисти
brush_size = 5
min_brush = 1
max_brush = 50

# Инструменты
TOOL_PENCIL = "pencil"
TOOL_RECTANGLE = "rectangle"
TOOL_CIRCLE = "circle"
TOOL_ERASER = "eraser"
TOOL_LINE = "line"
TOOL_SQUARE = "square"
TOOL_RIGHT_TRIANGLE = "right_triangle"
TOOL_EQUILATERAL_TRIANGLE = "equilateral_triangle"
TOOL_RHOMBUS = "rhombus"
tool = TOOL_PENCIL

#Холст
canvas = pygame.Surface((WIDTH, HEIGHT))
canvas.fill(BG_COLOR)

color_palette = [
    (0, 0, 0),        # Black
    (255, 0, 0),      # Red
    (0, 255, 0),      # Green
    (0, 0, 255),      # Blue
    (255, 255, 0),    # Yellow
    (255, 165, 0),    # Orange
    (255, 255, 255),  # White
    (128, 0, 128),    # Purple
    (255, 192, 203),  # pink
    (90, 50, 50),  # Brown
]


font = pygame.font.Font(None, 30)

def draw_ui():
    for i, color in enumerate(color_palette):
        pygame.draw.rect(screen, color, (10 + i * 35, 10, 30, 30))
    
    # Кнопки размера кисти
    pygame.draw.rect(screen, (200, 200, 200), (650, 10, 30, 30))
    pygame.draw.rect(screen, (200, 200, 200), (690, 10, 30, 30))
    
    plus = font.render("+", True, BLACK)
    minus = font.render("-", True, BLACK)
    screen.blit(plus, (657, 10))
    screen.blit(minus, (697, 10))
    
    # Индикатор размера кисти
    label = font.render(f"Кисть: {brush_size}", True, BLACK)
    screen.blit(label, (550, 15))
    
    # Список инструментов
    tools = [
        ("1: Pencil", 10, 50),
        ("2: Rectangle", 10, 80),
        ("3: Circle", 10, 110),
        ("4: Eraser", 10, 140),
        ("5: Line", 10, 170),
        ("6: Square", 10, 200),
        ("7: Right triangle", 10, 230),
        ("8: Equilateral triangle", 10, 260),
        ("9: Rhombus", 10, 290)
    ]
    
    for text, x, y in tools:
        text_surface = font.render(text, True, BLACK)
        screen.blit(text_surface, (x, y))

def get_color_from_palette(pos):
    #Выбор цвета
    x, y = pos
    if 10 <= y <= 40:
        for i, color in enumerate(color_palette):
            if 10 + i * 35 <= x <= 10 + i * 35 + 30:
                return color
    return None

#Основные переменные
drawing = False
start_pos = None
last_pos = None

while True:
    mouse_pos = pygame.mouse.get_pos()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        elif event.type == pygame.KEYDOWN:
            # Выбор инструмента
            if event.key == pygame.K_1:
                tool = TOOL_PENCIL
            elif event.key == pygame.K_2:
                tool = TOOL_RECTANGLE
            elif event.key == pygame.K_3:
                tool = TOOL_CIRCLE
            elif event.key == pygame.K_4:
                tool = TOOL_ERASER
                current_color = WHITE
            elif event.key == pygame.K_5:
                tool = TOOL_LINE
            elif event.key == pygame.K_6:
                tool = TOOL_SQUARE
            elif event.key == pygame.K_7:
                tool = TOOL_RIGHT_TRIANGLE
            elif event.key == pygame.K_8:
                tool = TOOL_EQUILATERAL_TRIANGLE
            elif event.key == pygame.K_9:
                tool = TOOL_RHOMBUS
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  #Левая кнопка мыши
                selected = get_color_from_palette(event.pos)
                
                if selected is not None:
                    current_color = selected
                    tool = TOOL_ERASER if selected == WHITE else TOOL_PENCIL
                
                #управление размером кисти
                elif 650 <= event.pos[0] <= 680 and 10 <= event.pos[1] <= 40:
                    brush_size = min(max_brush, brush_size + 1)
                elif 690 <= event.pos[0] <= 720 and 10 <= event.pos[1] <= 40:
                    brush_size = max(min_brush, brush_size - 1)
                
                else:
                    drawing = True
                    start_pos = event.pos
                    last_pos = event.pos
        
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 and drawing:
                end_pos = event.pos
                
                if tool == TOOL_RECTANGLE:
                    rect = pygame.Rect(
                        min(start_pos[0], end_pos[0]),
                        min(start_pos[1], end_pos[1]),
                        abs(end_pos[0] - start_pos[0]),
                        abs(end_pos[1] - start_pos[1])
                    )
                    pygame.draw.rect(canvas, current_color, rect, brush_size)
                
                elif tool == TOOL_CIRCLE:
                    radius = int(((end_pos[0] - start_pos[0])**2 + (end_pos[1] - start_pos[1])**2)**0.5)
                    pygame.draw.circle(canvas, current_color, start_pos, radius, brush_size)
                
                elif tool == TOOL_LINE:
                    pygame.draw.line(canvas, current_color, start_pos, end_pos, brush_size)
                
                elif tool == TOOL_SQUARE:
                    size = min(abs(end_pos[0] - start_pos[0]), abs(end_pos[1] - start_pos[1]))
                    rect = pygame.Rect(
                        start_pos[0],
                        start_pos[1],
                        size * (1 if end_pos[0] > start_pos[0] else -1),
                        size * (1 if end_pos[1] > start_pos[1] else -1)
                    )
                    pygame.draw.rect(canvas, current_color, rect, brush_size)
                
                elif tool == TOOL_RIGHT_TRIANGLE:
                    points = [
                        start_pos,
                        (start_pos[0], end_pos[1]),
                        end_pos
                    ]
                    pygame.draw.polygon(canvas, current_color, points, brush_size)
                
                elif tool == TOOL_EQUILATERAL_TRIANGLE:
                    width = end_pos[0] - start_pos[0]
                    height = int(width * math.sqrt(3) / 2)
                    points = [
                        start_pos,
                        (start_pos[0] + width, start_pos[1]),
                        (start_pos[0] + width // 2, start_pos[1] - height)
                    ]
                    pygame.draw.polygon(canvas, current_color, points, brush_size)
                
                elif tool == TOOL_RHOMBUS:
                    center_x = (start_pos[0] + end_pos[0]) // 2
                    center_y = (start_pos[1] + end_pos[1]) // 2
                    width = abs(end_pos[0] - start_pos[0]) // 2
                    height = abs(end_pos[1] - start_pos[1]) // 2
                    points = [
                        (center_x, center_y - height),
                        (center_x + width, center_y),
                        (center_x, center_y + height),
                        (center_x - width, center_y)
                    ]
                    pygame.draw.polygon(canvas, current_color, points, brush_size)
                
                drawing = False
    
    #Непрерывное рисование
    if drawing and tool in [TOOL_PENCIL, TOOL_ERASER]:
        if last_pos and mouse_pos:
            pygame.draw.line(canvas, current_color, last_pos, mouse_pos, brush_size)
        last_pos = mouse_pos
    
    #Отображение всего
    screen.blit(canvas, (0, 0))
    draw_ui()
    
    if drawing and tool in [TOOL_RECTANGLE, TOOL_CIRCLE, TOOL_LINE, TOOL_SQUARE, 
                           TOOL_RIGHT_TRIANGLE, TOOL_EQUILATERAL_TRIANGLE, TOOL_RHOMBUS]:
        temp_surface = screen.copy()
        
        if tool == TOOL_RECTANGLE:
            rect = pygame.Rect(
                min(start_pos[0], mouse_pos[0]),
                min(start_pos[1], mouse_pos[1]),
                abs(mouse_pos[0] - start_pos[0]),
                abs(mouse_pos[1] - start_pos[1])
            )
            pygame.draw.rect(temp_surface, current_color, rect, brush_size)
        
        elif tool == TOOL_CIRCLE:
            radius = int(((mouse_pos[0] - start_pos[0])**2 + (mouse_pos[1] - start_pos[1])**2)**0.5)
            pygame.draw.circle(temp_surface, current_color, start_pos, radius, brush_size)
        
        elif tool == TOOL_LINE:
            pygame.draw.line(temp_surface, current_color, start_pos, mouse_pos, brush_size)
        
        elif tool == TOOL_SQUARE:
            size = min(abs(mouse_pos[0] - start_pos[0]), abs(mouse_pos[1] - start_pos[1]))
            rect = pygame.Rect(
                start_pos[0],
                start_pos[1],
                size * (1 if mouse_pos[0] > start_pos[0] else -1),
                size * (1 if mouse_pos[1] > start_pos[1] else -1)
            )
            pygame.draw.rect(temp_surface, current_color, rect, brush_size)
        
        elif tool == TOOL_RIGHT_TRIANGLE:
            points = [
                start_pos,
                (start_pos[0], mouse_pos[1]),
                mouse_pos
            ]
            pygame.draw.polygon(temp_surface, current_color, points, brush_size)
        
        elif tool == TOOL_EQUILATERAL_TRIANGLE:
            width = mouse_pos[0] - start_pos[0]
            height = int(width * math.sqrt(3) / 2)
            points = [
                start_pos,
                (start_pos[0] + width, start_pos[1]),
                (start_pos[0] + width // 2, start_pos[1] - height)
            ]
            pygame.draw.polygon(temp_surface, current_color, points, brush_size)
        
        elif tool == TOOL_RHOMBUS:
            center_x = (start_pos[0] + mouse_pos[0]) // 2
            center_y = (start_pos[1] + mouse_pos[1]) // 2
            width = abs(mouse_pos[0] - start_pos[0]) // 2
            height = abs(mouse_pos[1] - start_pos[1]) // 2
            points = [
                (center_x, center_y - height),
                (center_x + width, center_y),
                (center_x, center_y + height),
                (center_x - width, center_y)
            ]
            pygame.draw.polygon(temp_surface, current_color, points, brush_size)
        
        screen.blit(temp_surface, (0, 0))
    
    pygame.display.flip()
    clock.tick(FPS)