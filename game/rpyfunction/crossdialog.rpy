init python:
    import random # Get the random functionality for Python

    def random_number(a,b):
        output = random.randint(a,b)
        return output


label function_betweenthedialog:
    $ _history_list = []
    image loading_0 = "gui/loading/1.png"
    image loading_1 = "gui/loading/2.png"
    image loading_2 = "gui/loading/3.png"
    image loading_3 = "gui/loading/4.png"
    image blank = "gui/noi.png"

    stop music
    stop audio
    stop sound
    
    "{fast}Loading{nw}"
    $ looptimes = random_number(3,5)
    scene loading_0
    $ renpy.notify('LOADING...')
    while looptimes > 0:
        pause 0.2
        scene loading_1
        
        pause 0.2
        scene loading_2
        pause 0.2
        scene loading_3
        $ looptimes -= 1
    scene blank at center
    $ renpy.notify('')
    $ _history_list = []

