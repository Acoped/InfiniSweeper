import pygame
from pygame.locals import *
from game.Entity import Entity
from game.Board import Board
import datetime
import os
import copy

def launch_from_init():


    # Very small 4 x 4 (for testing purposes)
    width = 5
    height = 4
    bombs = 3
    tile_sz_px = 32
    arrowkey_movement_cells = 3
    full_screen = False

    """
    # Small 9 x 9
    width = 9
    height = 9
    bombs = 10
    tile_sz_px = 32
    arrowkey_movement_cells = 1
    full_screen = False
    """

    """
    # Medium 16 x 16
    width = 16
    height = 16
    bombs = 40
    tile_sz_px = 16
    arrowkey_movement_cells = 1
    full_screen = False
    """

    """
    # Large 30 x 16
    width = 30
    height = 16
    bombs = 99
    tile_sz_px = 64
    arrowkey_movement_cells = 1
    full_screen = False
    """

    """
    # Whole screeen (HD)
    width = 240
    height = 135
    bombs = 6694
    tile_sz_px = 8
    arrowkey_movement_cells = 1
    full_screen = True
    """

    """
    # Whole screeen (1440p)
    width = 320
    height = 180
    bombs = 11900
    tile_sz_px = 8
    arrowkey_movement_cells = 1
    full_screen = True
    """

    """
    # Whole screeen (1440p) WORLD RECORD SIZE!
    width = 640
    height = 360
    bombs = 47600
    tile_sz_px = 4
    arrowkey_movement_cells = 1
    full_screen = True
    """

    increased_border = False

    min_viewport = [120, 72]
    viewport = [2560, 1440]
    frame_rate = 60              # does this need to be  high?
    title = "InfiniSweeper"

    main(width, height, bombs, tile_sz_px, full_screen, increased_border, min_viewport, viewport, frame_rate, title, arrowkey_movement_cells)


def main(width, height, bombs, tile_sz_px, full_screen, increased_border, min_viewport, viewport, frame_rate, title, arrow_key_movement_cells=4):
    black = (0, 0, 0)
    white = (255, 255, 255)
    yellow = (255, 255, 0)
    blue = (0, 0, 255)
    maroon = (128, 0, 0)

    pygame.init()

    board = Board(width, height, bombs, tile_sz_px, increased_border=increased_border)
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

    timer = pygame.time.Clock()
    timer_started = False

    # xs = load_sprite("../resources/tiles/XS/XS.png", 0, 0)
    # xs = Entity("../resources/tiles/XS/XS.png", 0, 0, 72, 72)
    # xs2 = xs.__copy__()
    # xs2.update(72, 0)

    start = True
    change = True

    left_down = False       # whether left mouse button is being held down
    right_down = False      # whether right mouse button is being held down
    shift_down = False      # whether shift button is being held down
    double_click_timer = 0  # Timer for detecting left mouse button double clicks
    dt = 0                  # delta for left mouse button double click timer

    font = pygame.font.SysFont("monospace", 12)

    transparent_background = pygame.Surface((200, 150))  # the size of your rect
    transparent_background.set_alpha(192)  # alpha level
    transparent_background.fill((255, 255, 255))  # this fills the entire surface

    window_x = 0
    window_y = 30

    window_pos = os.environ['SDL_VIDEO_WINDOW_POS'] = '%d,%d' % (window_x, window_y)

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
            pygame.display.quit()
            pygame.quit()
            break
        elif event.type == KEYDOWN:
            # ESCAPE -> Quits the game
            if event.key == K_ESCAPE:
                pygame.display.quit()
                pygame.quit()
            # R -> Restarts the game
            if event.key == K_r:
                board = Board(width, height, bombs, tile_sz_px, increased_border=increased_border)
                board.place_bombs()
                board.find_islands()
                board.set_screen(screen)
                board.draw_start()
                pygame.display.update()
            # P -> Screenshot
            if event.key == K_p:
                pygame.image.save(screen, "screenshot.png")
            # Arrow Keys -> Window movement, if not in fullscreen
            if not full_screen:
                if event.key == K_DOWN or event.key == K_UP or event.key == K_LEFT or event.key == K_RIGHT:
                    init_size_tuple = pygame.display.get_surface().get_size()
                    before_screen = pygame.image.tostring(screen, "RGBA")
                    if event.key == K_DOWN:
                        window_y += tile_sz_px * arrow_key_movement_cells
                    if event.key == K_UP:
                        window_y -= tile_sz_px * arrow_key_movement_cells
                    if event.key == K_LEFT:
                        window_x -= tile_sz_px * arrow_key_movement_cells
                    if event.key == K_RIGHT:
                        window_x += tile_sz_px * arrow_key_movement_cells
                    move_window(window_x, window_y)
                    screen.blit(pygame.image.fromstring(before_screen, init_size_tuple, "RGBA"), (0, 0))
                    pygame.display.flip()

        if not (board.win or board.lose):
            # Example on how to show clock on TAB press while playing, although this is REALLY inefficient
            """
            if event.type == KEYDOWN:
                if event.key == K_TAB:
                    # menu with clock here!
                    screen.blit(transparent_background, (0, 0))
                    timer_text = font.render(
                        "Your time: " + datetime.datetime.utcfromtimestamp(timer.tick() // 1000).strftime("%H:%M:%S"), 1,
                        maroon)
                    screen.blit(timer_text, (0, 0))
                    pygame.display.update()
            if event.type == KEYUP:
                if event.key == K_TAB:
                    # redraw the entire board?
                    # board.draw_start()
                    pygame.display.update()
            """
            if event.type == KEYDOWN:
                if event.key == K_RSHIFT or event.key == K_LSHIFT:
                    shift_down = True
                    print("shift down")
            if event.type == KEYUP:
                if event.key == K_RSHIFT or event.key == K_LSHIFT:
                    shift_down = False
                    print("shift up")
            if event.type == MOUSEBUTTONUP:

                if not timer_started:
                    timer_started = True
                    timer.tick()

                button = event.button

                # LEFT CLICK -> Opens tile
                if button == 1:

                    print(left_down, right_down, shift_down)

                    change = True

                    mouse_pos = pygame.mouse.get_pos()

                    if check_both(left_down, right_down, shift_down):
                        print('double hold then released left')
                        board.double_open_tile_from_mouse(mouse_pos)

                    left_down = False

                    if mouse_pos[0] < (board.w * tile_sz_px) and mouse_pos[1] < (board.h * tile_sz_px):
                        board.open_tile_from_mouse(mouse_pos)

                # MIDDLE CLICK
                elif button == 2:
                    pass

                # RIGHT CLICK -> Marks as flag
                elif button == 3:
                    change = True

                    mouse_pos = pygame.mouse.get_pos()

                    if check_both(left_down, right_down, shift_down):
                        print('double hold then released right')
                        board.double_open_tile_from_mouse(mouse_pos)

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

                    mouse_pos = pygame.mouse.get_pos()

                    # Detecting double click:
                    if double_click_timer == 0:  # First mouse click.
                        double_click_timer = 0.001  # Start the timer.
                    # Click again before 0.5 seconds to double click.
                    elif double_click_timer < 0.5:
                        print('double click')
                        board.double_open_tile_from_mouse(mouse_pos)
                        double_click_timer = 0
                        change = True

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
            # Increase timer after mouse was pressed the first time.
            if double_click_timer != 0:
                double_click_timer += dt
                # Reset after 0.5 seconds.
                if double_click_timer >= 0.5:
                    print('too late')
                    double_click_timer = 0
        # lose
        if board.lose:
            ms = timer.tick()
            screen.blit(transparent_background, (0, 0))
            msg_bg_color = black
            text1 = font.render("You LOSE! :(", 1, msg_bg_color)
            text2 = font.render(str(board.w) + " x " + str(board.h) + " = " + str(board.w * board.h) + " cells", 1, msg_bg_color)
            text3 = font.render(str(board.bombs) + " bombs", 1, msg_bg_color)
            text4 = font.render("Your time: " + datetime.datetime.utcfromtimestamp(ms//1000).strftime("%H:%M:%S"), 1, msg_bg_color)
            text5 = font.render("R to restart", 1, msg_bg_color)
            text6 = font.render("P to print screen", 1, msg_bg_color)
            text7 = font.render("ESC to quit", 1, msg_bg_color)
            screen.blit(text1, (10, 10))
            screen.blit(text2, (10, 30))
            screen.blit(text3, (10, 50))
            screen.blit(text4, (10, 70))
            screen.blit(text5, (10, 90))
            screen.blit(text6, (10, 110))
            screen.blit(text7, (10, 130))
        elif board.win:
            ms = timer.tick()
            screen.blit(transparent_background, (0, 0))
            msg_bg_color = black
            text1 = font.render("You WIN! :D", 1, msg_bg_color)
            text2 = font.render(str(board.w) + " x " + str(board.h) + " = " + str(board.w * board.h) + " cells", 1, msg_bg_color)
            text3 = font.render(str(board.bombs) + " bombs", 1, msg_bg_color)
            text4 = font.render("Your time: " + datetime.datetime.utcfromtimestamp(ms//1000).strftime("%H:%M:%S"), 1, msg_bg_color)
            text5 = font.render("R to restart", 1, msg_bg_color)
            text6 = font.render("P to print screen", 1, msg_bg_color)
            text7 = font.render("ESC to quit", 1, msg_bg_color)
            screen.blit(text1, (10, 10))
            screen.blit(text2, (10, 30))
            screen.blit(text3, (10, 50))
            screen.blit(text4, (10, 70))
            screen.blit(text5, (10, 90))
            screen.blit(text6, (10, 110))
            screen.blit(text7, (10, 130))

        dt = clock.tick(frame_rate) / 1000

def move_window(x, y):
    # Set where the display will move to
    os.environ['SDL_VIDEO_WINDOW_POS'] = '%d,%d' % (x, y)

    init_size_tuple = pygame.display.get_surface().get_size()
    init_size = list(init_size_tuple)

    init_size[0] += 1
    pygame.display.set_mode((init_size[0], init_size[1]))
    init_size[0] -= 1
    pygame.display.set_mode((init_size[0], init_size[1]))


# Checks if both left and right mouse buttons are (were...) being held (double click (release...)), also accounts for shift click (release)!
def check_both(left, right, shift):
    if left and right:
        return True
    elif shift and left:
        return True
    else:
        return False


if __name__ == "__main__":
    launch_from_init()
