init python:
    import random # Get the random functionality for Python

    def random_number(a,b):
        output = random.randint(a,b)
        return output


label function_betweenthedialog:
    stop music
    stop audio
    stop sound
    
    
    $ looptimes = random_number(3,8)

    $ renpy.notify('LOADING')
    while looptimes > 0:
        $ renpy.pause(0.5)
        $ renpy.notify('LOADING.')
        $ renpy.pause(0.5)
        $ renpy.notify('LOADING..')
        $ renpy.pause(0.5)
        $ renpy.notify('LOADING...')
        $ looptimes -= 1
    $ renpy.notify('')
