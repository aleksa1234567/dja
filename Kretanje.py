import pygame
import sys

pygame.init()

# Prozor
screen = pygame.display.set_mode((1000,600))
pygame.display.set_caption("Kretanje")

# Krompirko
krompirko = pygame.Rect((500,300),(70,20))
dirx,diry = 0,0
speed = 10

# Casovnik
clock = pygame.time.Clock()

# Game loop
while True:
    clock.tick(60)
    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                dirx = 1
                diry = 0
            if event.key == pygame.K_a:
                dirx = -1
                diry = 0
            if event.key == pygame.K_w:
                dirx = 0
                diry = -1
            if event.key == pygame.K_s:
                dirx = 0
                diry = 1
            
    # Update
    krompirko.x += dirx*speed
    krompirko.y += diry*speed
    # Draw
    screen.fill("black")
    pygame.draw.rect(screen,"red",krompirko)
    # Show
    pygame.display.flip()
