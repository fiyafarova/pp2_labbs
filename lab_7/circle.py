import pygame

pygame.init()

width, height = 500, 500
radius = 25
step = 20
white = (255, 255, 255)
red = (192, 12, 12)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Move the ball")

ball_x, ball_y = width // 2, height // 2

running = True

while running:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and ball_x - radius > 0:
        ball_x -= step
    if keys[pygame.K_RIGHT] and ball_x + radius < width:
        ball_x += step
    if keys[pygame.K_UP] and ball_y - radius > 0:
        ball_y -= step
    if keys[pygame.K_DOWN] and ball_y + radius < height:
        ball_y += step

    screen.fill(white)
    pygame.draw.circle(screen, red, (ball_x, ball_y), radius)
    pygame.display.update()

pygame.quit()
