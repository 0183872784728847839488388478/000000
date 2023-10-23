label data_menu_00001_00001_00001:
    menu:
        "You Already Read The Story 1"
        "Epiloge":
            call data_dialog_00001_00000
        "EP 1":
            call data_dialog_00001_00001
        "EP 2":
            call data_dialog_00001_00002
        "EP 3":
            call data_dialog_00001_00003
        "EP 4":
            call data_dialog_00001_00004
        "Re-Read":
            call data_dialog_00001_00000
            call data_dialog_00001_00001
            call data_dialog_00001_00002
            call data_dialog_00001_00003
            call data_dialog_00001_00004
            return
        "Back":
            return