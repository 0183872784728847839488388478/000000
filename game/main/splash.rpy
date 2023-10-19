init:
    $ demo_pass = "droid"
    $ dev_pass = "00000"
    $ persistent.anticheat = renpy.random.randint(100000, 999999)
    $ renpy.save_persistent()

    python:
        def max_points(*values):
            return [ i for i, v in enumerate(values) if v == max(values) ]

label splashscreen:
    call data_dialog_chr_00000_00000
    return