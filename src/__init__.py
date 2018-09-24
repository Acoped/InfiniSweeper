import pygame
from pygame.locals import *
from src.Entity import Entity
from src.Board import Board

full_screen = False
min_viewport = [120, 72]
viewport = [2560, 1440]
frame_rate = 25
title = "InfiniSweeper"

black = (0, 0, 0)
white = (255, 255, 255)


def main():
    pygame.init()

    board = Board(30, 16, 99, 8)
    # board = Board(320, 180, 11900, 8)
    board.place_bombs()
    viewport = board.calculate_screen_res()
    min_viewport = viewport

    screen = pygame.display.set_mode(viewport, HWSURFACE | DOUBLEBUF | RESIZABLE)
    if full_screen:
        pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

    pygame.display.set_caption(title)

    clock = pygame.time.Clock()

    # xs = load_sprite("../resources/tiles/XS/XS.png", 0, 0)
    # xs = Entity("../resources/tiles/XS/XS.png", 0, 0, 72, 72)
    # xs2 = xs.__copy__()
    # xs2.update(72, 0)

    # Game loop
    while True:

        pygame.display.flip()

        # ALL DRAW CODE SHOULD GO BELOW THIS COMMENT
        screen.fill(black)
        # xs.draw(screen)
        # xs2.draw(screen)
        board.draw(screen)
        # ALL DRAW CODE SHOULD GO ABOVE THIS COMMENT

        # EVENT HANDLING
        event = pygame.event.poll()
        # Handle exit and escape
        if event.type == pygame.QUIT:
            break
        # Handle window resizing
        elif event.type == VIDEORESIZE:
            if not full_screen:
                viewport[0], viewport[1] = event.size
                if viewport[0] < min_viewport[0]:
                    viewport[0] = min_viewport[0]
                if viewport[1] < min_viewport[1]:
                    viewport[1] = min_viewport[1]
                screen = pygame.display.set_mode(viewport, HWSURFACE | DOUBLEBUF | RESIZABLE)
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
        # /EVENT HANDLING

        clock.tick(frame_rate)


if __name__ == "__main__":
    main()
