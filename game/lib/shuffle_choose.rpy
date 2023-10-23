default shuffle = False

init python:
    renpy_menu = menu

    def menu(items):
        items = list(items)

        if shuffle:
            renpy.random.shuffle(items)

        return renpy_menu(items)