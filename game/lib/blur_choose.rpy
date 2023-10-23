# Enable support for the GL2 renderer.
define config.gl2 = True

# A transform that brings in the blur effect.
transform blur_in:
    blur 0.0
    linear .5 blur 16.0

# A transform that brings out the blur effect.
transform blur_out:
    blur 16.0
    linear .5 blur 0.0

init python:

    def blur_menu(*args, **kwargs):
        """
        This is a function that displays a menu with the master layer blurred
        behind it.
        """

        # Apply the blur_in transform to the master layer.
        renpy.layer_at_list([ blur_in ], layer="master")
        renpy.pause(.5)

        # Proxy the call to renpy.display_menu, to actually display the menu.
        rv = renpy.display_menu(*args, **kwargs)

        # Use the blur_out transform to reduce the blur_effect.
        renpy.layer_at_list([ blur_out ], layer="master")
        renpy.pause(.5)

        # Remove the transform form the master layer.
        renpy.layer_at_list([ ], layer="master")

        return rv

    menu = blur_menu