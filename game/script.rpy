
init:
    $ door_pass = "droid"

label before_main_menu:
    "In order to open the door you need to know the password."
    $ user_pass = renpy.input("Enter the password (5 characters)", "?????", length = 5)
    if user_pass == door_pass:
        return
    else:
        $ renpy.quit()

label start:

label dev_start:
    $ data_var_00000 = "demo"
    data_chr_00002 "Checking what version is this"
    if data_var_00000 == "dev":
        data_chr_00002 "Jumping To Dev Menu?"
        menu:
            "Yes!":
                jump dev_menu
            "No!":
                jump data_dialog_00000_00001
    elif data_var_00000 == "demo":
        data_chr_00002 "Demo Mode Enabled"
        data_chr_00002 "Starting the demo"
        jump data_dialog_00001_00000
    else:
        data_chr_00002 "Err: Devmode is disabled"
    jump end

label dev_menu:
    data_chr_00002 "Hello, Where Do You Wanna Warp?"
    menu:
        "Start?":
            jump data_dialog_00001_00000
        "EP 1":
            jump data_dialog_00001_00001
        "EP 2":
            jump data_dialog_00001_00002
        "EP 3":
            jump data_dialog_00001_00003
        "EP 4":
            jump data_dialog_00001_00004
        "End":
            jump end


label end:
    data_chr_00001_00001 "Sayonara"
    return
