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
    "In order to open the door you need to know the password."
    $ user_pass = renpy.input("Enter the password", "", length = 7)

    if user_pass == demo_pass:
        data_chr_00002 "Welcome Tester{nw}"
        $ data_var_00000 = "demo"

    elif user_pass == dev_pass:
        data_chr_00002 "Welcome Developer{nw}"
        $ data_var_00000 = "dev"
    else:
        data_chr_00002 "You Really Are An Idiot Trying To Do Stuff{nw}"
        $ renpy.quit()


    return