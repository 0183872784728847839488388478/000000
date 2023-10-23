label data_menu_00001_00002:
    $ renpy.notify('Story 1')
    default persistent.data_points_story_1_00000 = 0

    if persistent.data_points_story_1_00000 == 0:
        call function_betweenthedialog
        call data_dialog_00001_00000
        $ persistent.data_points_story_1_00000 += 1


    if persistent.data_points_story_1_00000 == 1:
        call function_betweenthedialog
        call data_dialog_00001_00001
        $ persistent.data_points_story_1_00000 += 1


    if persistent.data_points_story_1_00000 == 2:
        call function_betweenthedialog
        call data_dialog_00001_00002
        $ persistent.data_points_story_1_00000 += 1


    if persistent.data_points_story_1_00000 == 3:
        call function_betweenthedialog
        call data_dialog_00001_00003
        $ persistent.data_points_story_1_00000 += 1


    if persistent.data_points_story_1_0000 == 4:
        call function_betweenthedialog
        call data_dialog_00001_00004
        $ persistent.data_points_story_1_00000 += 1


    $ persistent.data_points_story_1_00000 = 5
    
    if persistent.data_points_story_1_00000 == 5:
        $ renpy.notify('Story 1 - Complete')
        call data_menu_00001_00001_00001


    return