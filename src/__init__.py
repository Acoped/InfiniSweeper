import pygame
from pygame.locals import *
from src.Entity import Entity
from src.Board import Board


def main():
    full_screen = True
    min_viewport = [120, 72]
    viewport = [2560, 1440]
    frame_rate = 60
    title = "InfiniSweeper"

    black = (0, 0, 0)
    white = (255, 255, 255)

    pygame.init()

    # board = Board(9, 9, 10, 8)
    # board = Board(30, 16, 99, 8)
    board = Board(320, 180, 11900, 8)
    board.place_bombs()
    board.find_islands()

    # viewport = board.calculate_screen_res()
    min_viewport = viewport

    screen = pygame.display.set_mode(viewport, HWSURFACE | DOUBLEBUF | RESIZABLE)
    if full_screen:
        pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

    board.set_screen(screen)

    pygame.display.set_caption(title)

    clock = pygame.time.Clock()

    # xs = load_sprite("../resources/tiles/XS/XS.png", 0, 0)
    # xs = Entity("../resources/tiles/XS/XS.png", 0, 0, 72, 72)
    # xs2 = xs.__copy__()
    # xs2.update(72, 0)

    start = True
    change = True

    # Game loop
    while True:

        # ALL DRAW CODE SHOULD GO BELOW THIS COMMENT
        # screen.fill(black)
        # xs.draw(screen)
        # xs2.draw(screen)

        # Only update screen on change
        if change:
            # board.draw(screen)
            if start:
                board.draw_start()
                start = False
            pygame.display.update()
            change = False
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
        elif event.type == MOUSEBUTTONUP:
            button = event.button
            # left click
            if button == 1:
                change = True
                mouse_pos = pygame.mouse.get_pos()
                board.open_tile_from_mouse(mouse_pos)
            # middle click
            elif button == 2:
                pass
            # right click
            elif button == 3:
                pass
            # scroll up
            elif button == 4:
                pass
            # scroll down
            elif button == 5:
                pass
        # Unhide the lines below later for "sunken effect" on held down unopened tiles
        """
        elif pygame.mouse.get_pressed()[0]:
            change = True
            mouse_pos = pygame.mouse.get_pos()
            board.draw_hold(mouse_pos)
        """
        """
        elif event.type == MOUSEBUTTONDOWN:
            change = True
            mouse_pos = pygame.mouse.get_pos()
            board.draw_hold(mouse_pos)"""
        # /EVENT HANDLING

        clock.tick(frame_rate)


if __name__ == "__main__":
    main()
