




label start:
    

    
    data_chr_00002 "Checking what version is this"

    call function_betweenthedialog

    data_chr_00002 "Detected: {b}[data_var_00000]{/b} mode"

    call function_betweenthedialog

    if data_var_00000 == "dev":
        $ player_name = "Droid"

        data_chr_00002 "[player_name] Jumping To Dev Menu?"
        menu:
            "Yes!":
                jump dev_menu
            "No!":
                pass

    elif data_var_00000 == "demo":
        data_chr_00002 "Demo Mode Enabled"
        data_chr_00002 "Starting the demo"
        pass

    else:
        
        data_chr_00002 "Err: Devmode is disabled"
        jump end

    while not player_name:
        $ player_name = renpy.input("Your Name?")
        $ player_name = player_name.strip()
    call function_betweenthedialog
    
    jump real_start



label real_start:

    menu:
        "Story 0":
            call function_betweenthedialog
            call data_dialog_00000_00001

        "Story 1":
            
            if data_points_story_1_0000 == 0:
                call function_betweenthedialog
                call data_dialog_00001_00000
                $ data_points_story_1_0000 += 1

            if data_points_story_1_0000 == 1:
                call function_betweenthedialog
                call data_dialog_00001_00001
                $ data_points_story_1_0000 += 1

            if data_points_story_1_0000 == 2:
                call function_betweenthedialog
                call data_dialog_00001_00002
                $ data_points_story_1_0000 += 1

            if data_points_story_1_0000 == 3:
                call function_betweenthedialog
                call data_dialog_00001_00003
                $ data_points_story_1_0000 += 1

            if data_points_story_1_0000 == 4:
                call function_betweenthedialog
                call data_dialog_00001_00004
                $ data_points_story_1_0000 += 1
            data_chr_00002 "Story Ended"
            $ data_points_story_1_0000 = 0

    jump end


label dev_menu:
    
    data_chr_00002 "Hello, Where Do You Wanna Warp?"
    menu:
        "Start?":
            call data_dialog_00001_00000
        "EP 1":
            call data_dialog_00001_00001
        "EP 2":
            call data_dialog_00001_00002
        "EP 3":
            call data_dialog_00001_00003
        "EP 4":
            call data_dialog_00001_00004
        "End":
            jump end
    call function_betweenthedialog
    jump dev_menu



label end:
    data_chr_00001_00001 "Sayonara"
    return


label exit:
    