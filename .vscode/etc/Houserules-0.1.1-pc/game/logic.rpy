# Location = [0 Location name, 1 navigation button, 2 morning bg, 3 afternoon bg, 4 evening bg, 5 night bg, 6 location down, 7 location left, 8 location right, 9 location up]
default bathroom    = ["bathroom",      "navigate_bathroom.png",    "bg_bathroom.png",      "bg_bathroom.png",      "bg_bathroom.png",      "bg_bathroom.png",      "foyer",          None,           None,         None        ]
default bedroom     = ["bedroom",       "navigate_bedroom.png",     "bg_bedroom.png",       "bg_bedroom.png",       "bg_n_bedroom.png",     "bg_n_bedroom.png",     "livingroom",     None,           None,         None        ]
default corridor    = ["corridor",      "navigate_frontdoor.png",   "bg_corridor.png",      "bg_corridor.png",      "bg_corridor.png",      "bg_corridor.png",      "foyer",          None,           None,         None        ]
default foyer       = ["foyer",         "navigate_foyer.png",       "bg_foyer.png",         "bg_foyer.png",         "bg_foyer.png",         "bg_foyer.png",         "livingroom",     "office",       "bathroom",   "corridor"  ]
default kitchen     = ["kitchen",       "navigate_kitchen.png",     "bg_kitchen.png",       "bg_kitchen.png",       "bg_n_kitchen.png",     "bg_n_kitchen.png",     "livingroom",     None,           None,         None        ]
default livingroom  = ["livingroom",    "navigate_livingroom.png",  "bg_livingroom.png",    "bg_livingroom.png",    "bg_n_livingroom.png",  "bg_n_livingroom.png",  "foyer",          "bedroom",      "kitchen",    None        ]
default office      = ["homeoffice",    "navigate_office.png",      "bg_office.png",        "bg_office.png",        "bg_office.png",        "bg_office.png",        "foyer",          None,           None,         None        ]

default current_time            = 3                                                                                             # first scene is evening
default current_location        = office                                                                                        # game begins in the office
default current_day             = 0
default bgtime                  = current_time + 1
default time_period = ["Wakeup",    "Morning",      "Afternoon",    "Evening",      "Night"]                                    # 0-4,  0=Wakeup, 4=Night
default week_day    = ["Monday",    "Tuesday",      "Wednesday",    "Thursday",     "Friday",   "Saturday",     "Sunday"]       # 0-6,  0=Monday, 6=Sunday
default current_weekday         = 6                                                                                             # game starts on Sunday
default current_weekday_name    = week_day[current_weekday]
default current_timeperiod      = time_period[current_time]

image Monday        = "displays/monday.png"
image Tuesday       = "displays/tuesday.png"
image Wednesday     = "displays/wednesday.png"
image Thursday      = "displays/thursday.png"
image Friday        = "displays/friday.png"
image Saturday      = "displays/saturday.png"
image Sunday        = "displays/sunday.png"

image Wakeup        = "displays/wakeup.png"
image Morning       = "displays/morning.png"
image Afternoon     = "displays/afternoon.png"
image Evening       = "displays/evening.png"
image Night         = "displays/night.png"

default wardrobeslotsmaid   = {0: None, 1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None, 9: None, 10: None, 11: None, 12: None, 13: None, 14: None, 15: None}
default wardrobeslotsplayer = {0: None, 1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None, 9: None, 10: None, 11: None, 12: None, 13: None, 14: None, 15: None}
default tasklist = []

default actordictionary = {
    "M41D"      : CharacterM41D,
    "Player"    : CharacterPlayer
    }

default itemdictionary = {
    "Black Stockings"   :   wardrobe_StockingsBlack,
    "White Stockings"   :   wardrobe_StockingsWhite,
    "Pink Stockings"    :   wardrobe_StockingsPink,
    "Hotpink Stockings" :   wardrobe_StockingsHotpink,
    "Black Panties"     :   wardrobe_PantiesBlack,
    "Red Panties"       :   wardrobe_PantiesRed,
    "Hotpink Panties"   :   wardrobe_PantiesHotpink,
    "Black Thong"       :   wardrobe_ThongBlack,
    "White Thong"       :   wardrobe_ThongWhite,
    "Pink Thong"        :   wardrobe_ThongPink,
    "Hotpink Thong"     :   wardrobe_ThongHotpink,
    "Black Bra"         :   wardrobe_BraBlack,
    "White Bra"         :   wardrobe_BraWhite,
    "Pink Bra"          :   wardrobe_BraPink,
    "Hotpink Bra"       :   wardrobe_BraHotpink,
    "Maid Dress"        :   wardrobe_MaidDress,
    "Red Dress"         :   wardrobe_DressRed,
    "Black Dress"       :   wardrobe_DressBlack,
    "Black Top"         :   wardrobe_TopBlack,
    "White Gloves"      :   wardrobe_GlovesWhite
}

default navigationdictionary = {
    "bathroom"      :   bathroom,
    "bedroom"       :   bedroom,
    "corridor"      :   corridor,
    "foyer"         :   foyer,
    "kitchen"       :   kitchen,
    "livingroom"    :   livingroom,
    "living room"   :   livingroom,
    "office"        :   office
}

default wardrobeEC = 0  #Wardrobe Error Code

# Zorders:
# 0-40              - Backgrounds and backgorund detail
#   1                   - GoTo() background
# 41-100            - Paperdoll M41D
# 101-500           - Reserved for future
# 501-600           - Navigation and buttons
#   601                 - ShowTime() weekday
#   602                 - ShowTime() time
# 601-700           - Popups and splashes

screen nav(n=True):

    python:
        NavStart = str(store.current_location[0])
        if NavStart in store.navigationdictionary:
            navdown     = store.navigationdictionary[NavStart][6]
            navleft     = store.navigationdictionary[NavStart][7]
            navright    = store.navigationdictionary[NavStart][8]
            navup       = store.navigationdictionary[NavStart][9]
            down        = "images/buttons/navigate_"+ str(navdown) + "_%s.png"
            left        = "images/buttons/navigate_"+ str(navleft) + "_%s.png"
            right       = "images/buttons/navigate_"+ str(navright) + "_%s.png"
            up          = "images/buttons/navigate_"+ str(navup) + "_%s.png"
            # print(f"Current position is {NavStart}, the accesible locations are {navleft} to the left, {navright} to the right, {navup} in the front and {navdown} to the back.")
        else:
            print(f"Location {NavStart} not in the dictionary")


        if n == True:
            pass
        elif n == False:
            _window_show(trans=None, auto=False)
            #renpy.with_statement(Dissolve(0.5))
        elif n == "Skip":
            pass
        else:
            print("Invalid navigation selected")


    default posTopLeft   = {"x" : 63,      "y" : 780}
    default posTopMid    = {"x" : 735,     "y" : 780}
    default posTopRight  = {"x" : 1405,    "y" : 780}
    default posBotLeft   = {"x" : 63,      "y" : 910}
    default posBotMid    = {"x" : 735,     "y" : 910}
    default posBotRight  = {"x" : 1405,    "y" : 910}


    #button down
    if navdown != None:
        imagebutton auto down xpos posBotMid["x"] ypos posBotMid["y"] focus_mask True action Function(GoTo, navdown) hover_sound "audio/pop.wav"
    #button up
    if navup != None:
        imagebutton auto up xpos posTopMid["x"] ypos posTopMid["y"] focus_mask True action Function(GoTo, navup) hover_sound "audio/pop.wav"
    #button left
    if navleft != None:
        imagebutton auto left xpos posBotLeft["x"] ypos posBotLeft["y"] focus_mask True action Function(GoTo, navleft) hover_sound "audio/pop.wav"
    #button right
    if navright != None:
        imagebutton auto right xpos posBotRight["x"] ypos posBotRight["y"] focus_mask True action Function(GoTo, navright) hover_sound "audio/pop.wav"
    #action button
    imagebutton auto "images/buttons/navigate_tasks_%s.png" xpos posTopLeft["x"] ypos posTopLeft["y"] focus_mask True action Function(myTasks) hover_sound "audio/pop.wav"
    imagebutton auto "images/buttons/navigate_action_%s.png" xpos posTopRight["x"] ypos posTopRight["y"] focus_mask True action Function(myReturn) hover_sound "audio/pop.wav"

screen questlog():
    python:
        action_manager.show_pending_actions()
    image("buttons/back_overlay.png")
    image("buttons/tasks.png")
    imagebutton auto "images/buttons/x_%s.png" xpos 1540 ypos 50 focus_mask True action Function(myReturn) hover_sound "audio/pop.wav"
    viewport:
        draggable True
        mousewheel True
        scrollbars "vertical"
        xpos 310
        ypos 150
        hbox:
            vbox:
                xsize 300
                for i in action_manager.show_pending_actions():
                    text "[i]"
            vbox:
                xsize 1000
                for i in action_manager.show_pending_notes():
                    text "[i]"

init python:
    import random
    import pygame_sdl2 as pygame
    from random import randint
    from renpy.exports import displayable, call

    def myReturn(): 
        return True
    
    def myTasks():
        renpy.call_screen(questlog()) #does not work, no idea why

    class CharData:
        def __init__(self,*, name=None, ass=None, gen=None, chest=None):
            self.Name           = name
            self.Inventory      = None
            self.Equipped       = None
            self.Ass            = ass or bodypart_FlatAss
            self.Genitals       = gen or bodypart_Vagina
            self.Breasts        = chest or bodypart_FlatBreasts

    CharacterM41D   = CharData(name='M41D',     ass=bodypart_AverageAss,    gen=bodypart_Vagina,        chest=bodypart_AverageBreasts)
    CharacterPlayer = CharData(name='Alex',     ass=bodypart_FlatAss,       gen=bodypart_SmallPenis,    chest=bodypart_FlatBreasts)
    
    def GoTo(place):                                                                    # TODO rewrite, this function does not verify input with location directory, also can't do random, it's ass and whoever wrote it is a stinky doodoo
        if isinstance(place, str):
            place = store.navigationdictionary[place]                                   # if for whatever reason the input is given as a string this converts it back into the object
        else:
            pass
        store.current_location = place                                                  # this should replace current_location with string name of the room for use in conversations
        print(f"new location is {store.current_location[0]}")
        bgtime = store.current_time + 1                                                 # this sets the value to the correct slot of the location array
        if store.current_time == 0:                                                             
            bgtime = 2                                                                  # this forces morning bg during wakeup sequence
        #print (f"current time is {store.current_time}")
        #print (f"bgtime is {bgtime}")
        renpy.scene()                                                                   # this removes the previous background
        renpy.show(place[bgtime][:-4], layer="master")                                  # this should pull the proper scene name for the room based on current time
        #renpy.with_statement(Dissolve(0.7))                                             # this adds a dissolve transition at 0.7s length to the image

    def ShowTime():
        renpy.show(current_weekday_name, layer="screens")                           
        renpy.show (current_timeperiod, layer="screens")
        renpy.with_statement(Dissolve(1)) 
        renpy.pause(0.5)
        renpy.hide(current_weekday_name, layer="screens")
        renpy.hide(current_timeperiod, layer="screens")
        renpy.with_statement(Dissolve(1)) 

    def ShowPic(Picture1, Picture2):
        renpy.show(Picture1)
        renpy.with_statement(Dissolve(0.7))
        renpy.show(Picture2)
        renpy.with_statement(Dissolve(0.7))
        renpy.pause(0.5)
        renpy.hide(Picture1)
        renpy.with_statement(Dissolve(0.7))
        renpy.hide(Picture2)
        renpy.with_statement(Dissolve(0.7))

    class Action:
        def __init__(self, task, location, notes, minigame, deadline, status, tasktype, required):
            self.task = task
            self.location = location
            self.notes = notes
            self.minigame = minigame
            self.deadline = deadline
            self.status = status
            self.tasktype = tasktype
            self.required = required

    class ActionManager:
        def __init__(self):
            self.pending_actions = []

        def add_action(self, task, location, notes, minigame, deadline, status, tasktype, required):
            #status:    active, completed, failed
            #tasktypes: chore, action, forced, secretforced
            #required:  optional, mandatory
            new_action = Action(task, location, notes, minigame, deadline, status, tasktype, required)
            for action in self.pending_actions:
                if action.task == task and action.location == location and action.notes == notes and action.deadline == deadline:
                    print("This action is already on the list")
                    return
            self.pending_actions.append(new_action)
            print(f"New action '{task}' added to pending actions.")

        def remove_action(self, task):
            found = False
            for action in self.pending_actions:
                if action.task == task:
                    self.pending_actions.remove(action)
                    found = True
                    print(f"Action '{task}' removed from pending actions.")
                    break

            if not found:
                print(f"No action found with task '{task}'.")

        def show_pending_actions(self):
            tasklist = []
            if not self.pending_actions:
                # print("No pending actions.")
                pass
            else:
                print("appending tasklist")
                for index, action in enumerate(self.pending_actions, start=1):
                    tasklist.append(f"{index}. {action.task}")
                    print(tasklist[-1])                     # Print the current task in the loop
            return tasklist                                 # Return the tasklist.append(f"{index}. Task: {action.task} | Notes: {action.notes}")populated tasklist

        def show_pending_notes(self):
            noteslist = []
            if not self.pending_actions:
                # print("No pending actions.")
                pass
            else:
                print("appending noteslist")
                for index, action in enumerate(self.pending_actions, start=1):
                    noteslist.append(f"{action.notes}")
                    print(noteslist[-1])                    # Print the current note in the loop
            return noteslist                                # Return the tasklist.append(f"{index}. Task: {action.task} | Notes: {action.notes}")populated tasklist

    action_manager = ActionManager()                        # Create an instance of the ActionManager class
    #   action_manager.show_pending_actions()               # Show pending actions
    #   action_manager.remove_action("Call plumber")        # Remove an action
    #   action_manager.show_pending_actions()               # Show updated pending actions


    # This fucntion needs to be redesinged for when I want to just jump to next day wakeup from any given point of the previous day
    def AdvanceDay(n=1, desired_weekday=None, show_time=False):                    # n = how many days to add or desired_weekday AS INT = where to skip to in the week
        print(f"It was {store.current_weekday_name}, game day {store.current_day}")
        if desired_weekday == None:                                                     # if desired_day is not set, simple addition
            store.current_day = store.current_day + n                                   # current day (since game start) is increased by n
            store.current_weekday = store.current_weekday + n                           # current weekday is advanced by n
        else:                                                                           # if desired_day is set, ignore n
            if desired_weekday <= current_weekday:                                      # if desired weekday is lower than current, eg we have Thursday and we want Tuesday
                x = 6 - store.current_weekday + desired_weekday + 1
                store.current_day = store.current_day + x
                store.current_weekday = store.current_weekday + x
            else:                                                                       # if desired weekday is higher than current, eg we have Monday, we want Wednesday
                x = store.current_weekday - desired_weekday
                store.current_day = store.current_day + x
                store.current_weekday = store.current_weekday + x
        while store.current_weekday > 6:                                                # if current weekday is higher than 6 (sunday) roll back to following day next week
            store.current_weekday = store.current_weekday - 7
        store.current_weekday_name = week_day[store.current_weekday]
        place = current_location                               
        GoTo(place)                                                                     # refresh background
        if show_time == True:
            ShowTime()
        print(f"It is now {store.current_weekday_name}, game day {store.current_day}")

    def AdvanceTime(n=1, desired_time=None):                                        # n = how many periods of time to add or desided_time AS INT = where to skip in time
        print(f"It was {current_weekday_name} {current_timeperiod}")
        if desired_time == None:
            store.current_time = store.current_time + n                                 # this adds n to the current_time (default 1, meaning moving from morning to afternoon etc.) If desired 
        else:
            if desired_time <= store.current_time:                                      # if desired time is lower than the current, advance 1 day
                AdvanceDay(1, None, False)
            store.current_time = desired_time                                           # if desired time stated (as an array spot 0-5), move to desired time
        while store.current_time > 4:                               
            store.current_time = store.current_time - 5                                 # while current_time exceeds 4, as in is greater than "Night", move to next day wakeup. Might need more work for certain scenarios.
            AdvanceDay(1, None, False)
        store.current_timeperiod = store.time_period[store.current_time]                # store current time period as string eg "Morning"
        print(f"Now it is {current_weekday_name} {current_timeperiod}")
        place = current_location                               
        if store.current_time == 0:
            renpy.play("wakeup.wav")
        GoTo(place)                                                                     # refresh background
        ShowTime()
    
    def Wardrobe(actor = "M41D", action="None", item="None", preset="None", override="no"):            #WIP
        
        # Wardrobe rules:
            # Slots:
                #   0:  Head
                #   1:  Underbottom     (panties, Panties, boyshorts)
                #   2:  Undertop        (bra, corset)
                #   3:  Overtop         (tops, shirts)
                #   4:  Overbottom      (skirts, shorts, pants)
                #   5:  Legwear         (socks, stockings, thights)
                #   6:  Hands           (gloves)
                #   7:  MiscFront       (chastity)
                #   8:  MiscBack        (anal plug)
                #   9:  Neck            (necklace, collar)
                #   10: PiercingEars    (earings)
                #   11: PiercingLips    (lip piercing)
                #   12: PiercingTongue  (tongue piercing)
                #   13: PiercingBelly   (belly button piercing)
                #   14: PiercingGenital (genital piercing)
                #   15: PiercingBrow    (brow piercing)
            # Slot Properties:
                #   Available:          = None
                #   Locked:             = "Locked"
                #   Housing:            = "Item_Name"
            # Item Properties:
                #   ItemName:           string
                #   ItemSlot:           integar
                #   LockSlot:           integar
                #   Special:            ??? (boons? Stuff? Status effects? idk)
                #   Directory:          path to file
    
        if item in itemdictionary:
            item_object = itemdictionary[item]
            #print(item_object.ItemName)
        else:
            print("Item not found in the dictionary.")
            return

        if actor in actordictionary:
            actor_object = actordictionary[actor]
            #print(actor_object.Name)
        else:
            print("Actor not found in the dictionary.")
            return
        
        if action == "None":
            pass
        elif action == "puton" or action == "on":
            # check if the slot of the item is not locked
            requestedSlot = item_object.ItemSlot
            if actor_object.Equipped[item_object.ItemSlot] == "Locked":
                if override == "no":
                    print("Slot is locked")
                else:
                    pass # if override is on, ignore lock
            else:
                actor_object.Equipped[item_object.ItemSlot] = item_object
        elif action == "takeoff" or action == "off" or action == "strip":
            if item_object in actor_object.Equipped.values():
                actor_object.Equipped[item_object.ItemSlot] = None
            else:
                print(f"{item_object.Item_Name} is not equipped so it can't be stripped")
        elif action == "hide":
            pass
        elif action == "unhide":
            pass
        elif action == "check":
            renpy.pause(0.1) #spit out all possible errors this item could generate
        else:
            print("Action not defined")
            return

        print(actor_object)

    def Paperdoll(actor="M41D", emote="Neutral", pose="Basic", emoteoverride="default", clothes="default", genitals="default"): #WIP

        Ahegao = [
            { "face": 78 },
            { "face": 77 },
            { "face": 76 },
            { "face": 75 },
            { "face": 74 },
            { "face": 73 },
            { "face": 72 },
            { "face": 71 },
            { "face": 70 }
        ]

        Angry = [
            { "face": 54 },
            { "face": 53 },
            { "face": 52 },
            { "face": 51 },
            { "face": 50 },
            { "face": 49 },
            { "face": 48 },
            { "face": 47 },
            { "face": 46 },
            { "face": 45 },
            { "face": 44 },
            { "face": 43 },
            { "face": 42 },
            { "face": 41 },
            { "face": 40 },
            { "face": 39 },
            { "face": 38 }
        ]

        Annoyed = [
            { "face": 46 },
            { "face": 45 },
            { "face": 44 },
            { "face": 43 },
            { "face": 42 },
            { "face": 41 },
            { "face": 40 },
            { "face": 39 },
            { "face": 157 }
        ]

        Annoyed_Questioning = [
            { "face": 157 },
            { "face": 155 }
        ]

        Crying = [
            { "face": 194 },
            { "face": 193 },
            { "face": 192 },
            { "face": 191 },
            { "face": 190 },
            { "face": 189 },
            { "face": 188 },
            { "face": 187 },
            { "face": 186 }
        ]

        Disgusted = [
            { "face": 50 },
            { "face": 38 }   
        ]

        Displeased = [
            { "face": 96 },
            { "face": 95 },
            { "face": 94 },
            { "face": 93 },
            { "face": 92 },
            { "face": 91 },
            { "face": 90 },
            { "face": 89 },
            { "face": 88 },
            { "face": 86 },
            { "face": 85 },
            { "face": 60 },
            { "face": 59 },
            { "face": 58 },
            { "face": 57 },
            { "face": 56 },
            { "face": 55 },
            { "face": 54 },
            { "face": 53 },
            { "face": 52 },
            { "face": 51 },
            { "face": 50 },
            { "face": 46 },
            { "face": 45 },
            { "face": 44 },
            { "face": 43 },
            { "face": 42 },
            { "face": 41 },
            { "face": 40 },
            { "face": 39 },
            { "face": 38 }
        ]

        Displeased_Very = [
            { "face": 49 },
            { "face": 48 },
            { "face": 47 }
        ]

        Dominating = [
            { "face": 28 },
            { "face": 27 },
            { "face": 26 },
            { "face": 25 },
            { "face": 24 },
            { "face": 23 },
            { "face": 22 },
            { "face": 21 },
            { "face": 20 },
            { "face": 185 },
            { "face": 184 },
            { "face": 183 },
            { "face": 182 },
            { "face": 181 },
            { "face": 180 },
            { "face": 179 },
            { "face": 178 },
            { "face": 177 },
            { "face": 176 },
            { "face": 175 },
            { "face": 174 },
            { "face": 173 },
            { "face": 172 },
            { "face": 171 },
            { "face": 170 },
            { "face": 169 },
            { "face": 168 },
            { "face": 167 },
            { "face": 166 },
            { "face": 165 },
            { "face": 164 },
            { "face": 163 },
            { "face": 162 },
            { "face": 161 },
            { "face": 160 },
            { "face": 159 }
        ]

        Furious = [
            { "face": 69 },
            { "face": 68 },
            { "face": 67 },
            { "face": 66 },
            { "face": 65 },
            { "face": 64 },
            { "face": 63 },
            { "face": 62 },
            { "face": 61 }
        ]

        Furious_Questioning = [
            { "face": 67 },
            { "face": 66 },
            { "face": 64 },
            { "face": 62 },
            { "face": 47 }
        ]

        Happy = [
            { "face": 7 },
            { "face": 6 },
            { "face": 5 },
            { "face": 4 },
            { "face": 3 },
            { "face": 2 },
            { "face": 140 }
        ]

        Neutral = [
            { "face": 99 },
            { "face": 84 },
            { "face": 83 },
            { "face": 82 },
            { "face": 81 },
            { "face": 80 },
            { "face": 79 },
            { "face": 203 },
            { "face": 202 },
            { "face": 201 },
            { "face": 200 },
            { "face": 199 },
            { "face": 198 },
            { "face": 197 },
            { "face": 196 },
            { "face": 195 },
            { "face": 105 },
            { "face": 104 },
            { "face": 102 },
            { "face": 1 }
        ]

        Pleased = [
            { "face": 9 },
            { "face": 8 },
            { "face": 7 },
            { "face": 4 },
            { "face": 3 },
            { "face": 2 },
            { "face": 10 }
        ]

        Pleased_Very = [
            { "face": 6 },
            { "face": 5 },
            { "face": 4 }
        ]

        Neutral_Questioning = [
            { "face": 98 },
            { "face": 97 },
            { "face": 87 },
            { "face": 83 },
            { "face": 82 },
            { "face": 199 },
            { "face": 198 },
            { "face": 19 },
            { "face": 18 },
            { "face": 17 },
            { "face": 16 },
            { "face": 156 },
            { "face": 15 },
            { "face": 147 },
            { "face": 14 },
            { "face": 13 },
            { "face": 12 },
            { "face": 11 },
            { "face": 100 },
            { "face": 1 }
        ]

        Sad = [
            { "face": 1 } #placeholder
        ]

        Shocked = [
            { "face": 158 },
            { "face": 154 },
            { "face": 153 },
            { "face": 152 },
            { "face": 151 },
            { "face": 150 },
            { "face": 149 },
            { "face": 148 },
            { "face": 146 },
            { "face": 145 },
            { "face": 144 },
            { "face": 143 },
            { "face": 142 },
            { "face": 141 },
            { "face": 134 },
            { "face": 133 },
            { "face": 132 },
            { "face": 131 }
        ]

        Sleep = [
            { "face": 114 },
            { "face": 113 },
            { "face": 112 },
            { "face": 111 },
            { "face": 110 },
            { "face": 109 },
            { "face": 108 },
            { "face": 107 },
            { "face": 106 }
        ]

        Seductive = [
            { "face": 27 },
            { "face": 26 },
            { "face": 25 },
            { "face": 24 },
            { "face": 23 },
            { "face": 22 },
            { "face": 21 },
            { "face": 20 }
        ]

        Surprised = [
            { "face": 37 },
            { "face": 36 },
            { "face": 35 },
            { "face": 34 },
            { "face": 33 },
            { "face": 32 },
            { "face": 31 },
            { "face": 30 },
            { "face": 29 },
            { "face": 147 },
            { "face": 139 },
            { "face": 136 },
            { "face": 135 },
            { "face": 101 }
        ]

        Teasing = [
            { "face": 29 },
            { "face": 28 }
        ]

        Yandere = [
            { "face": 129 },
            { "face": 128 },
            { "face": 127 },
            { "face": 126 },
            { "face": 125 },
            { "face": 124 },
            { "face": 123 },
            { "face": 122 },
            { "face": 121 },
            { "face": 120 },
            { "face": 119 },
            { "face": 118 },
            { "face": 117 },
            { "face": 116 },
            { "face": 115 }
        ]

        Yandere_Dominating = [
            { "face": 129 },
            { "face": 128 },
            { "face": 127 },
            { "face": 126 },
            { "face": 125 },
            { "face": 123 },
            { "face": 122 },
            { "face": 121 },
            { "face": 120 },
            { "face": 119 },
            { "face": 118 },
            { "face": 117 },
            { "face": 116 }
        ]

        Yandere_Obsessive = [
            { "face": 124 }
        ]

        emotedictionary = {
            "Ahegao"                : Ahegao,
            "Angry"                 : Angry,
            "Annoyed"               : Annoyed,
            "Annoyed_Questioning"   : Annoyed_Questioning,
            "Annoyed Questioning"   : Annoyed_Questioning,
            "Crying"                : Crying,
            "Disgusted"             : Disgusted,
            "Displeased"            : Displeased,
            "Displeased_Very"       : Displeased_Very,
            "Displeased Very"       : Displeased_Very,
            "Very Displeased"       : Displeased_Very,
            "Dominating"            : Dominating,
            "Furious"               : Furious,
            "Furious_Questioning"   : Furious_Questioning,
            "Furious Questioning"   : Furious_Questioning,
            "Happy"                 : Happy,
            "Neutral"               : Neutral,
            "Pleased"               : Pleased,
            "Pleased_Very"          : Pleased_Very,
            "Pleased Very"          : Pleased_Very,
            "Very Pleased"          : Pleased_Very,
            "Neutral_Questioning"   : Neutral_Questioning,
            "Neutral Questioning"   : Neutral_Questioning,
            "Sad"                   : Sad,
            "Shocked"               : Shocked,
            "Sleep"                 : Sleep,
            "Seductive"             : Seductive,
            "Surprised"             : Surprised,
            "Teasing"               : Teasing,
            "Yandere"               : Yandere,
            "Yandere_Dominating"    : Yandere_Dominating,
            "Yandere Dominating"    : Yandere_Dominating,
            "Yandere_Obsessive"     : Yandere_Obsessive,
            "Yandere Obsessive"     : Yandere_Obsessive
        }

        if actor in actordictionary:
            actor_object = store.actordictionary[actor]
            #print(actor_object.Name)
        else:
            print("Actor not found in the dictionary.")
            return

        if emote in emotedictionary:
            emote_object = emotedictionary[emote]
            #print(emote_object)
        elif emote == "random" or emote == "Random":
            random_emotion_key = random.choice(list(emotedictionary.keys()))
            emote_object = emotedictionary[random_emotion_key]
        else:
            print("Emote not found in the dictionary.")

        random_emote = random.choice(emote_object)
        #print(f"Random face selected from the range is {random_face}")
        if emoteoverride == "default":
            pass
        else:
            random_face = emoteoverride
            print(f"Random face selected from the range is overriden by {random_face}")
        random_face = random_emote["face"]

        wardrobe = actor_object.Equipped

        body            = "images/paperdoll_" + str(actor_object.Name) + "/base.png"
        face            = "images/paperdoll_" + str(actor_object.Name) + "/emotes/" + str(random_face) + ".png"
        
        
        if wardrobe[0] == None:
            head        = 0
        else:
            head        = "images/paperdoll_" + str(actor_object.Name) + "/head/" + str(wardrobe[0].Directory)

        if wardrobe[1] == None:
            underbottom = 0
        else:
            underbottom = "images/paperdoll_" + str(actor_object.Name) + "/underbottom/" + str(wardrobe[1].Directory)

        if wardrobe[2] == None:
            undertop    = 0
        else:
            undertop    = "images/paperdoll_" + str(actor_object.Name) + "/undertop/" + str(wardrobe[2].Directory)

        if wardrobe[3] == None:
            overtop     = 0
        else:
            overtop     = "images/paperdoll_" + str(actor_object.Name) + "/overtop/" + str(wardrobe[3].Directory)
        
        if wardrobe[4] == None:
            overbottom  = 0
        else:
            overbottom  = "images/paperdoll_" + str(actor_object.Name) + "/overbottom/" + str(wardrobe[4].Directory)

        if wardrobe[5] == None:
            legwear     = 0
        else:
            legwear     = "images/paperdoll_" + str(actor_object.Name) + "/legwear/" + str(wardrobe[5].Directory)

        if wardrobe[6] == None:
            hands       = 0
        else:
            hands       = "images/paperdoll_" + str(actor_object.Name) + "/hands/" + str(wardrobe[6].Directory)

        if wardrobe[7] == None:
            miscfront   = 0
        else:
            miscfront   = "images/paperdoll_" + str(actor_object.Name) + "/miscfront/" + str(wardrobe[7].Directory)
        
        if wardrobe[8] == None:
            miscback    = 0
        else:
            miscback    = "images/paperdoll_" + str(actor_object.Name) + "/miscback/" + str(wardrobe[8].Directory)

        if genitals == "default":
            arousal = 0 #TODO area for expansion
        elif genitals == "aroused" or genitals =="wet" or genitals == "erect":
            arousal = 1
        elif genitals == "dry" or genitals == "flaccid":
            arousal = 0
        else:
            print("Genitals defined incorrectly, defaulting")
            
        genitalsa = "images/paperdoll_" + str(actor_object.Name) + "/genitals/" + str(actor_object.Genitals.BodypartSize) + str(arousal) + ".png"

        PaperdollKill(0)

        renpy.show("body", what=Image(str(body)), layer="master", zorder = 41)
        renpy.show("face", what=Image(str(face)), layer="master", zorder = 43) #43,44,45,46 reserved for possible face overhaul

        if clothes == "default":
            if underbottom != 0:
                renpy.show("underbottom", what=Image(str(underbottom)), layer="master", zorder = 49)
            else:
                renpy.show("genitals", what=Image(str(genitalsa)), layer="master", zorder = 48)
            if undertop != 0:
                renpy.show("undertop", what=Image(str(undertop)), layer="master", zorder = 50)
            if legwear != 0:
                renpy.show("legwear", what=Image(str(legwear)), layer="master", zorder = 47)
            if overtop != 0:
                renpy.show("overtop", what=Image(str(overtop)), layer="master", zorder = 52)
            if overbottom != 0:
                renpy.show("overbottom", what=Image(str(overbottom)), layer="master", zorder = 53)
            if hands != 0:
                renpy.show("hands", what=Image(str(hands)), layer="master", zorder = 54)
        elif clothes == "underwear":
            if underbottom != 0:
                renpy.show("underbottom", what=Image(str(underbottom)), layer="master", zorder = 49)
            else:
                renpy.show("genitals", what=Image(str(genitalsa)), layer="master", zorder = 48)
            if undertop != 0:
                renpy.show("undertop", what=Image(str(undertop)), layer="master", zorder = 50)
            if legwear != 0:
                renpy.show("legwear", what=Image(str(legwear)), layer="master", zorder = 47)
        elif clothes == "naked":
            renpy.show("genitals", what=Image(str(genitalsa)), layer="master", zorder = 48)
        else:
            print("Clothes incorrectly defined")

        #renpy.with_statement(Dissolve(0.1)) #needs work, looks off
        #TODO fix penis and maid dress to more precise layer cuts

    def PaperdollKill(x=0.5):
        renpy.hide("body")
        renpy.hide("face")
        renpy.hide("underbottom")
        renpy.hide("undertop")
        renpy.hide("overbottom")
        renpy.hide("overtop")
        renpy.hide("legwear")
        renpy.hide("hands")
        renpy.hide("genitals")
        renpy.with_statement(Dissolve(x))

    







    ############################################################### MINIGAMES ###############################################################