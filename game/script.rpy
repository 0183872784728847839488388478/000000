
init:
    $ door_pass = "00000"

label before_main_menu:
    "In order to open the door you need to know the password."
    $ user_pass = renpy.input(u"Enter the password (5 characters)", "00000", length = 5)
    if user_pass == door_pass:
        return
    else:
        $ renpy.quit()

label start:

label dev_start:
    $ data_var_00000 = "dev"
    data_chr_00002 "Checking if you are Dev or not"
    if data_var_00000 == "dev":
        data_chr_00002 "Jumping To Dev Menu?"
        menu:
            "Yes!":
                jump dev_menu
            "No!":
                jump data_dialog_00000_00001
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
