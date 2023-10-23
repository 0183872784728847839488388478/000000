init python:
    import random # Get the random functionality for Python

    def random_number(a,b):
        output = random.randint(a,b)
        return output


label function_betweenthedialog:
    $ renpy.block_rollback()
    $ _history_list = []
    $ minutes, seconds = divmod(int(renpy.get_game_runtime()), 60)
    image loading_0 = "gui/loading/1.png"
    image loading_1 = "gui/loading/2.png"
    image loading_2 = "gui/loading/3.png"
    image loading_3 = "gui/loading/4.png"
    image blank = "gui/noi.png"

    stop music
    stop audio
    stop sound

    play music data_music_library_1 loop
    $ looptimes = random_number(3,5)
    $ luck = random_number(0,255)
    scene loading_0 with dissolve
    if luck < 255:
        $ renpy.notify('LOADING...')
    else:
        $ looptimes = 7
        $ renpy.notify('Why This Exist?')

    while looptimes > 0:
        $ renpy.block_rollback()
        pause 0.2
        scene loading_1
        pause 0.2
        scene loading_2
        pause 0.2
        scene loading_3
        $ looptimes -= 1

    scene blank with dissolve
    $ renpy.notify('')
    $ _history_list = []
    stop music
    stop audio
    stop sound
    $ timeout_label = None
    $ timeout = 5.0
    $ shuffle = False
    $ del looptimes
    $ renpy.block_rollback()
    return

