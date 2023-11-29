import pygame

FPS = 60
WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
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
