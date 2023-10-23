




label start:
    while not persistent.player_name:
        $ persistent.player_name = renpy.input("Your Name?")
        $ persistent.player_name = persistent.player_name.strip()
        $ data_player_00000 = persistent.player_name.strip()
    call function_betweenthedialog
    jump real_start



label real_start:
    menu:
        "Story 0":
            call data_menu_00001_00001

        "Story 1" if persistent.storage_story_00000_00000:
            call data_menu_00001_00002
            
    data_chr_00002 "Story Ended"
    jump real_start



label end:
    data_chr_00001_00001 "Sayonara"
    return


label exit:
    