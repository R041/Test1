import tdl
import os

absolute_path = os.path.abspath(__file__)
directory_name = os.path.dirname(absolute_path)
os.chdir(directory_name)

SCREEN_WIDTH = 80
SCREEN_HEIGHT = 80
LIMIT_FPS = 10

################
# HANDLE INPUT #
################
def input():
    global playerx, playery

    keypress = False
    for event in tdl.event.get():
        if event.type == "KEYDOWN":
            user_input = event
            keypress = True
    if not keypress:
        return

    # Handle movement keys
    if user_input.key == "UP":
        playery -= 1

    elif user_input.key == "DOWN":
        playery += 1

    elif user_input.key == "LEFT":
        playerx -= 1

    elif user_input.key == "RIGHT":
        playerx += 1

    # Quit game key
    elif user_input.key == "ESCAPE":
        return True

##########
# RENDER #
##########
def render():
    tdl.flush()

##################
# MAIN GAME LOOP #
##################
tdl.set_font('arial10x10.png', greyscale=True, altLayout=True)
tdl.set_fps(LIMIT_FPS)
console = tdl.init(SCREEN_WIDTH, SCREEN_HEIGHT, title="HSMud", fullscreen=False)

playerx = SCREEN_WIDTH//2
playery = SCREEN_HEIGHT//2

while not tdl.event.is_window_closed():
    console.draw_char(playerx, playery, " ", bg=None, fg=None)
    exit = input()
    console.draw_char(playerx, playery, '@', bg=None, fg=(255, 255, 255))
    # update()
    render()
    if exit:
        break