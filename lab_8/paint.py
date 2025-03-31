import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
FPS = 60
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("пеинт")
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BG_COLOR = WHITE
current_color = BLACK

brush_size = 5
min_brush = 1
max_brush = 50

TOOL_PENCIL = "pencil"
TOOL_RECTANGLE = "rectangle"
TOOL_CIRCLE = "circle"
TOOL_ERASER = "eraser"
TOOL_LINE = "line"
tool = TOOL_PENCIL

canvas = pygame.Surface((WIDTH, HEIGHT))
canvas.fill(BG_COLOR)

color_palette = [
    (0, 0, 0),        # Black
    (255, 0, 0),      # Red
    (0, 255, 0),      # Green
    (0, 0, 255),      # Blue
    (255, 255, 0),    # Yellow
    (255, 165, 0),    # Orange
    (255, 255, 255),  # White (eraser)
    (128, 0, 128),    # Purple
    (255,192,203),    # pink
]

font = pygame.font.Font(None, 30)

def draw_ui():
    # интерфейс
    for i, color in enumerate(color_palette):
        pygame.draw.rect(screen, color, (10 + i * 35, 10, 30, 30))
    
    pygame.draw.rect(screen, (200, 200, 200), (650, 10, 30, 30))
    pygame.draw.rect(screen, (200, 200, 200), (690, 10, 30, 30))
    
    plus = font.render("+", True, BLACK)
    minus = font.render("-", True, BLACK)
    screen.blit(plus, (657, 10))
    screen.blit(minus, (697, 10))
    
    
    label = font.render(f"Brush: {brush_size}", True, BLACK)
    screen.blit(label, (550, 15))
    
    tools = [
        ("1: Pencil", 10, 50),
        ("2: Rectangle", 10, 80),
        ("3: Circle", 10, 110),
        ("4: Eraser", 10, 140),
        ("5: Line", 10, 170)
    ]
    
    for text, x, y in tools:
        text_surface = font.render(text, True, BLACK)
        screen.blit(text_surface, (x, y))

def get_color_from_palette(pos):
    #выбрать цвет
    x, y = pos
    if 10 <= y <= 40:
        for i, color in enumerate(color_palette):
            if 10 + i * 35 <= x <= 10 + i * 35 + 30:
                return color
    return None

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
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  #left mouse button
                selected = get_color_from_palette(event.pos)
                
                if selected is not None:
                    current_color = selected
                    tool = TOOL_ERASER if selected == WHITE else TOOL_PENCIL
                
                #brush size controls
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
                
                drawing = False
    
    #continuous drawing for pencil and eraser
    if drawing and tool in [TOOL_PENCIL, TOOL_ERASER]:
        if last_pos and mouse_pos:
            pygame.draw.line(canvas, current_color, last_pos, mouse_pos, brush_size)
        last_pos = mouse_pos
    
    # display everything
    screen.blit(canvas, (0, 0))
    draw_ui()
    
    if drawing and tool in [TOOL_RECTANGLE, TOOL_CIRCLE, TOOL_LINE]:
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
        screen.blit(temp_surface, (0, 0))
    
    pygame.display.flip()
    clock.tick(FPS)