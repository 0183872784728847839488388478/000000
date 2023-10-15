init:
    $ demo_pass = "droid"
    $ dev_pass = "00000"
    $ persistent.anticheat = renpy.random.randint(100000, 999999)
    $ renpy.save_persistent()

    python:
        def max_points(*values):
            return [ i for i, v in enumerate(values) if v == max(values) ]

label splashscreen:
    "In order to open the door you need to know the password."
    $ user_pass = renpy.input("Enter the password", "?????", length = 7)

    if user_pass == demo_pass:
        data_chr_00002 "Correct :D"
        $ data_var_00000 = "demo"

    elif user_pass == dev_pass:
        data_chr_00002 "Correct :D"
        $ data_var_00000 = "dev"
    else:
        $ renpy.quit()


    return