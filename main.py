import pygame
from checkers.game import Game
from checkers.cfg import WIN, FPS, WIDTH, HEIGHT, SQUARE_SIZE, RED

pygame.display.set_caption('Шашки')

def main() -> None:
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()

    pygame.quit()


main()
