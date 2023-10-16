label data_dialog_00001_00001:
    
    $ renpy.notify('CHAPTER 1')
    
    data_ep_0 "12 Years has passed and she is now 15 years old"

    $ renpy.notify('???')

    data_ep_0 "One night while returning to her bedroom to sleep"

    data_ep_0 "she remembered her father's promise"

    data_ep_0 "she grabs a key from her breast pocket"

    #Keys Ringing
    define data_chr_00005_00000_00000 = data_chr_00005_00001_00001
    data_chr_00005_00000_00000 "One day we will go there and spend sometime"

    data_ep_0 "promise to make her father\'s promise come true at least"

    play sound data_sound_footstep_indoor fadeout 1

    data_ep_0 "Auriel arrived to her bedroom\'s door and she open it"

    play sound data_sound_door_open volume 1.0 fadeout 1
    
    $ renpy.notify('Bedroom')

    data_ep_0 "Her room have a Comfy bed\, cabinet\, a chandelier and a Door to nothing..."
    
    play sound data_sound_door_close fadeout 1
    
    #Surpise Auriel Here

    data_ep_0 "She is surprise theres a free standing door on her room"

    play sound data_sound_footstep_indoor

    data_ep_0 "She went on the front of the door and tried to open the door" 

    play sound none

    data_ep_0 "But its so heavy that it cant even budge and gave up"

    data_ep_0 "She change to her sleeping outfit and went to bed.."

    $ renpy.notify('The Next Day')

    play sound data_sound_morning
    "8 hours has passed and she woken up from her sleep"

    data_chr_00005_00000_00000 "*ahhh good morning from nightmares*"
    # Yawning
    $ renpy.notify('Bedroom')
    
    play sound data_sound_footstep_indoor
    
    data_ep_0 "Auriel went to her cabinet to change to her usual dress and inspect the heavy door on the middle of the room"
    
    stop sound
    
    data_ep_0 "and found that theres symbol that use ancient symbol"

    data_ep_0 "there are 8 symbols and 1 that are glowing"

    data_chr_00005_00000_00000 "*I have no clue what are these...oh no am late for entrance exam*"

    play sound data_sound_door_open volume 1.0

    data_ep_0 "she remembered about her entrance exam and went to the kitchen to cook..."
    
    play sound data_sound_door_close
    
    data_ep_0 "Auriel is settled in a remote mansion in the middle of the woods."
    
    stop music fadeout 1

    data_ep_0 "She inherited the mansion after her father passed away and is likely still processing the grief."

    data_ep_0 "She lives there by herself and often spends her days alone."

    data_ep_0 "she would rather be alone than having the maid guild assign a maid to a mantion at the middle of the forest full of monsters "

    data_ep_0 "after she finish cooking and eat"

    play sound data_sound_door_open volume 1.0

    data_ep_0 "she left the mantion and went thru the wilderness to get in the academy"
    
    play sound data_sound_door_close
    
    play music data_place_forest loop
    
    $ renpy.notify('Wilderness')
    
    play music data_place_natural loop
    data_ep_0 "on this world anyone with the age of 13 and above are called adults and all child restrictions are lift"

    "after an hour and a half of walk and breaks she reach the academy"

    $ renpy.notify('Kingdom\'s Academy')

    play music data_place_kingdom_crowd loop volume 0.5

    data_ep_0 "the kingdom\'s academy is the largest academy in the continent that even Royalty\, Nobles\, and Commoners from different kingdom are all together in a single academy because of its reputation"

    data_ep_0 "this is her first time going into the academy"
    
    data_chr_00005_00000_00000 "{i}It So Big!{/i}" #Someone surely gonna get this out of context

    data_ep_0 "she was shock because of the size of the entrance that she froze for while"
    
    stop music fadeout 1

    play sound bell

    data_ep_0 "as the academy\'s bell started to ring Auriel went to a classrooms"

    $ renpy.notify('Classroom')

    #Chair Moving

    data_ep_0 "on the room there are 120 chairs"

    data_ep_0 "they are allowed to pick what chair they want"

    data_ep_0 "as per usual.. Cheating in any way will immediately kick you out and never be able to take the exam for a year"

    data_ep_0 "she pick the chair on the center-right from the door and wait for other participants to start the exam"

    play sound data_sound_footstep_indoor

    data_ep_0 "a professor go to the front of the room to sign the start of the exam"

    data_chr_00003_00002 "you may begin"

    play sound data_sound_page_flip fadeout 1

    data_ep_0 "everyone in the room flip their papers and start answering the exam"

    data_ep_0 "it would take 3 Hours to finish entrance exam"

    data_ep_0 "the exam contains question about Magic, Types, Monster, Topography, History, Abilities, Elements, Artifacts and More."

    data_ep_0 "the exam is very hard you need to get atleast 40\% to pass and only 25k or less students pass the entrance exam per year"

    data_ep_0 "she finish the exam 1 hour before the time limit and take a nap"

    $ renpy.notify('Classroom')

    play sound data_sound_bell

    data_ep_0 "bell rang as the exam is about to close"

    data_ep_0 "Auriel woke up just as the professor about to announce something."

    data_ep_0 "Her eyes slowly adjusted to the bright lights of the room"

    data_ep_0 "as she struggled to keep from yawning."
    
    data_ep_0 "She was exhausted after having taken the entrance exam"

    data_ep_0 "which she\'d spent nearly all of her time preparing for. Despite her tiredness"

    data_ep_0 "Auriel was curious what it was that the professor was announcing"

    data_ep_0 "so she sat forward in her chair and focused on listening."

    data_chr_00003_00002 "Times up everyone flip your papers. make sure to put a name on it. the passing names will be posted in the academy's board tommorow with what room you will be in"
    
    play sound data_sound_footstep_indoor
    data_ep_0 "she left the room and return to her home"

    return
