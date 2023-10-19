




label start:
    

    
    data_chr_00002 "Checking what version is this{nw}"

    call function_betweenthedialog

    data_chr_00002 "Detected: {b}[data_var_00000]{/b} mode{nw}"

    call function_betweenthedialog


    while not persistent.player_name:
        $ persistent.player_name = renpy.input("Your Name?")
        $ persistent.player_name = persistent.player_name.strip()
    call function_betweenthedialog
    
    jump real_start



label real_start:

    menu:
        "Story 0":
            call function_betweenthedialog
            call data_dialog_00000_00001
            $ persistent.storage_story_00000_00000 = True

        "Story 1" if persistent.storage_story_00000_00000:
            default persistent.data_points_story_1_0000 = 0

            if persistent.data_points_story_1_0000 == 0:
                call function_betweenthedialog
                call data_dialog_00001_00000
                $ persistent.data_points_story_1_0000 += 1

            if persistent.data_points_story_1_0000 == 1:
                call function_betweenthedialog
                call data_dialog_00001_00001
                $ persistent.data_points_story_1_0000 += 1

            if persistent.data_points_story_1_0000 == 2:
                call function_betweenthedialog
                call data_dialog_00001_00002
                $ persistent.data_points_story_1_0000 += 1

            if persistent.data_points_story_1_0000 == 3:
                call function_betweenthedialog
                call data_dialog_00001_00003
                $ persistent.data_points_story_1_0000 += 1

            if persistent.data_points_story_1_0000 == 4:
                call function_betweenthedialog
                call data_dialog_00001_00004
                $ persistent.data_points_story_1_0000 += 1
            
            $ data_points_story_1_0000 = 0
    data_chr_00002 "Story Ended"
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
    