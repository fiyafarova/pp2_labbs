
import pygame
import os
import sys

pygame.mixer.init()
pygame.init()

WIDTH, HEIGHT = 700, 400

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BUTTON_COLOR = (255, 102, 178)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Music Player")

font = pygame.font.Font(None, 36)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

songs = [
    os.path.abspath(os.path.join(BASE_DIR, "songs", "/Users/sofiyasafarova/Desktop/2sem/pp2/lab_7/Crazy Frog - Axel А (radio mix).mp3")),
    os.path.abspath(os.path.join(BASE_DIR, "songs", "/Users/sofiyasafarova/Desktop/2sem/pp2/lab_7/Wiz Khalifa & Charlie Puth - See You Again.mp3")),
    os.path.abspath(os.path.join(BASE_DIR, "songs", "/Users/sofiyasafarova/Desktop/2sem/pp2/lab_7/Rihanna Feat. Eminem - Love The Way You Lie.mp3"))
]

songs = [song for song in songs if os.path.exists(song)]

if not songs:
    print("No valid songs found. Add MP3 files in the directory.")
    exit()

current_index = 0

buttons = {
    "Play": pygame.Rect(320, 130, 80, 40),
    "Stop": pygame.Rect(320, 230, 80, 40),
    "Prev": pygame.Rect(160, 180, 80, 40),
    "Next": pygame.Rect(480, 180, 80, 40)
}

def play_music():
    pygame.mixer.music.load(songs[current_index])
    pygame.mixer.music.play()
    print(f"Playing: {songs[current_index]}")

def stop_music():
    pygame.mixer.music.stop()
    print("Music Stopped")

def next_song():
    global current_index
    current_index = (current_index + 1) % len(songs)
    play_music()

def previous_song():
    global current_index
    current_index = (current_index - 1) % len(songs)
    play_music()

running = True

while running:
    screen.fill(WHITE)

    song_text = font.render(f"Now Playing: {os.path.basename(songs[current_index])}", True, BLACK)
    screen.blit(song_text, (50, 50))

    for text, rect in buttons.items():
        pygame.draw.rect(screen, BUTTON_COLOR, rect)
        label = font.render(text, True, WHITE)
        screen.blit(label, (rect.x + 15, rect.y + 10))

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                play_music()
            elif event.key == pygame.K_s:
                stop_music()
            elif event.key == pygame.K_d:
                next_song()
            elif event.key == pygame.K_a:
                previous_song()

        if event.type == pygame.MOUSEBUTTONDOWN:
            for action, rect in buttons.items():
                if rect.collidepoint(event.pos):
                    if action == "Play":
                        play_music()
                    elif action == "Stop":
                        stop_music()
                    elif action == "Next":
                        next_song()
                    elif action == "Prev":
                        previous_song()

pygame.quit()
sys.exit()