## Here is the place where you can customize the skin of your diary. 
## You can safety modify this file.


init -1: ## <-- Don't touch this one /!\

    ## The position of the diary screen in game
    ## If 0, the screen is under the textbox, if 2, the screen is over the textbox
    define diary_zorder = 0

    ## If true, the game is freezed when the player open the diary screen.
    define diary_modal = False

    ## Add between the {} all the category you want to display on the left page. 
    ## The others will be displayed on the right page.
    ## Be sure to add a comma between the categories
    define left_page = {_("General"),}


#_______________Image costumization___________________

## You can change the path of all the images to your own images.
image open_book = "assets/open_book.png"
image book_close_idle = "assets/book_close_idle.png"
image book_close_hover = "assets/book_close_hover.png"
image completed = "assets/completed.png"
image in_progress = "assets/in_progress.png"
image journal_divider = "assets/journal_divider.png"



#___________________Texts and styles_______________________


## The style that is used for the categories
style category_style is text:
    xalign 0.5 #if 0.0 text is at left, if 0.5 text is centered, if 1.0 text is at right 
    color "#63050e"
    font "questmanager/assets/PermanentMarker-Regular.ttf"
    size 45
    bold False
    italic False
    strikethrough False



## The style that is used for the pending events
## The pending events are displayed with "???"
style quest_pending_style is text:
    color "#172993"
    font "questmanager/assets/Pacifico-Regular.ttf"
    size 35
    bold False
    italic False
    strikethrough False

## The style that is used for the unlocked events
style quest_unlocked_style is text:
    color "#172993"
    font "questmanager/assets/Pacifico-Regular.ttf"
    size 35
    bold False
    italic False
    strikethrough False

## The style that is used for the in progress events
style quest_in_progress_style is text:
    color "#172993"
    font "questmanager/assets/Pacifico-Regular.ttf"
    size 35
    bold False
    italic False
    strikethrough False

## The style that is used for the completed events
style quest_completed_style is text:
    yalign .5
    color "#172993"
    font "questmanager/assets/Pacifico-Regular.ttf"
    size 35
    bold False
    italic True
    strikethrough False

## The style that is used for the done events
style quest_done_style is text:
    color "#172993"
    font "questmanager/assets/Pacifico-Regular.ttf"
    size 35
    bold False
    italic False
    strikethrough True

## The style that is used for the failed events
style quest_failed_style is text:
    color "#e12345"
    font "questmanager/assets/Pacifico-Regular.ttf"
    size 35
    bold False
    italic False
    strikethrough False


#___________Buttons____________

style open_diary_screen_btn is button:
    #background "" xalign .5 yalign .5
    #hover_background ""
    xysize(120,55)

style open_diary_screen_btn is text:
    size 35
    xalign .5