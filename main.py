import pygame
import os
pygame.init()

WIDTH, HEIGHT = (1000, 700)
SHIP_WIDTH, SHIP_HEIGHT = (60, 45)
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ShipGame")
BORDER = pygame.Rect(WIDTH / 2, 0, 10, HEIGHT)
WHITE = (255, 255, 155)
BLACK = (0, 0, 0)
FPS = 60

SPACE_IMAGE = pygame.image.load(os.path.join("Assets", "Space.jpg"))
SPACE = pygame.transform.scale(SPACE_IMAGE,(WIDTH, HEIGHT))
PLAYER1_IMAGE = pygame.image.load(os.path.join("Assets", "Ship1.jpg"))
PLAYER1_SHIP = pygame.transform.scale(PLAYER1_IMAGE, (SHIP_WIDTH, SHIP_HEIGHT))
PLAYER2_IMAGE = pygame.image.load(os.path.join("Assets", "Ship2.png"))
PLAYER2_SHIP = pygame.transform.scale(PLAYER2_IMAGE, (SHIP_WIDTH, SHIP_HEIGHT))


def draw_window():
    WIN.blit(SPACE, (0, 0))
    pygame.draw.rect(WIN, BLACK, BORDER)
    WIN.blit(PLAYER1_SHIP, (100, 350))
    WIN.blit(PLAYER2_SHIP, (900, 350))
    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw_window()



       # pygame.quit()


if __name__ == "__main__":
    main()
