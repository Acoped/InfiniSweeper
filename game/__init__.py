import pygame
from pygame.locals import *
from game.Entity import Entity
from game.Board import Board


def main():


    """
    # Small 9 x 9
    width = 9
    height = 9
    bombs = 10
    tile_sz_px = 8
    """

    """
    # Medium 16 x 16
    width = 16
    height = 16
    bombs = 40
    tile_sz_px = 8
    """


    # Large 30 x 16
    width = 30
    height = 16
    bombs = 99
    tile_sz_px = 16


    """
    # Whole screeen (HD)
    width = 240
    height = 135
    bombs = 6694
    tile_sz_px = 8
    """

    """
    # Whole screeen (1440p)
    width = 320
    height = 180
    bombs = 11900
    tile_sz_px = 8
    """

    full_screen = False

    min_viewport = [120, 72]
    viewport = [2560, 1440]
    frame_rate = 60
    title = "InfiniSweeper"

    black = (0, 0, 0)
    white = (255, 255, 255)

    pygame.init()

    board = Board(width, height, bombs, tile_sz_px)
    board.place_bombs()
    board.find_islands()

    if not full_screen:
        viewport = board.calculate_screen_res()
    min_viewport = viewport

    screen = pygame.display.set_mode(viewport, HWSURFACE | DOUBLEBUF)
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

    left_down = False       # whether left mouse button is being held down
    right_down = False      # whether right mouse button is being held down

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
        elif event.type == KEYDOWN:
            # ESCAPE -> Quits the game
            if event.key == K_ESCAPE:
                pygame.quit()
            # R -> Restarts the game
            if event.key == K_r:
                board = Board(width, height, bombs, tile_sz_px)
                board.place_bombs()
                board.find_islands()
                board.set_screen(screen)
                board.draw_start()
                pygame.display.update()

        elif event.type == MOUSEBUTTONUP:
            button = event.button

            # LEFT CLICK -> Opens tile
            if button == 1:
                change = True

                mouse_pos = pygame.mouse.get_pos()

                if check_both(left_down, right_down):
                    print('double hold then released left')
                    board.double_open_tile_from_mouse(mouse_pos)

                left_down = False

                board.open_tile_from_mouse(mouse_pos)

            # MIDDLE CLICK
            elif button == 2:
                pass

            # RIGHT CLICK -> Marks as flag
            elif button == 3:
                change = True

                mouse_pos = pygame.mouse.get_pos()

                if check_both(left_down, right_down):
                    print('double hold then released right')

                right_down = False

                board.mark_from_mouse_pos(mouse_pos)

            # SCROLL UP
            elif button == 4:
                pass

            # SCROLL DOWN
            elif button == 5:
                pass

        elif event.type == MOUSEBUTTONDOWN:

            button = event.button

            # LEFT HOLD DOWN STARTED
            if button == 1:
                left_down = True

            # RIGHT HOLD DOWN STARTED
            elif button == 3:
                right_down = True

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


# Checks if both left and right mouse buttons are (were...) being held
def check_both(left, right):
    if left and right:
        return True
    else:
        return False


if __name__ == "__main__":
    main()
