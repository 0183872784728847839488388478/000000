label data_menu_00001_00001:
    $ renpy.notify('Story 0')
    call function_betweenthedialog
    call data_dialog_00000_00001
    $ persistent.storage_story_00000_00000 = True
    return