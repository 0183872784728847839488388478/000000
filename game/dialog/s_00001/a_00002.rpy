label data_dialog_00001_00002:

    $ renpy.notify('CHAPTER 2')
    
    data_ep_0 "Auriel woke up in the middle of the night and found her room had changed"

    $ renpy.notify('Auriel\'s Bedroom ')

    data_ep_0 "It now decorated with luxurious furniture"

    data_chr_00004_00000_00001 "How The Hell This Happened?"

    data_ep_0 "The Door In the middle of the room is suddenly glowing blue"

    data_ep_0 "Confused and startled, she stood up and tried to open the door. "

    play sound data_sound_footstep_indoor

    play sound data_sound_door_open

    data_ep_0 "It swung open with ease this time."

    play sound data_sound_door_close

    data_ep_0 "The Free Standing Door is Connected to a long hallway full of stars"

    data_ep_0 "she walk thru the door to see a beautiful scenery "

    $ renpy.notify('????? Corridor')

    data_ep_0 "as she walks thru she see a another door coming in the view"

    data_ep_0 "Auriel run to the door and open it"

    #Running

    play sound data_sound_door_open

    $ renpy.notify('??????')

    data_ep_0 "she sees a desk, tables, bookshelfs are full to the brim of books, chairs on every corridor and a big clock on the high wall"

    play music library_5 loop

    #Ticking Clock

    data_ep_0 "she hears a so satisfying yet so mystrious song playing through the whole room"

    data_ep_0 "She went to the desk and found a note on the desk"

    data_chr_00003_00003 "\"Congratulations Auriel, you passed the entrance exam,\" "

    data_chr_00003_00003 "\"I hope giving this library full of knowledge about the whole world help you.\""

    data_ep_0 "Auriel was still staring at the note, trying to process the information."

    data_chr_00004_00000_00001 "I passed the entrance exam?"
     
    data_ep_0 "she repeated to herself."
    
    data_ep_0 "as she wondered what this meant for her"

    play music data_music_library_3 loop

    data_ep_0 "She explore the library and found that every corridor that have a sign infront of it "

    $ renpy.notify('Library\'s Corridor')

    data_ep_0 "with certain number indicating to it and hears the song changing based on where she walking thru"

    data_chr_00004_00000_00001 "8?"

    $ renpy.notify('Library\'s 8th Corridor')

    data_ep_0 "She went to a corridor with a sign \"8\" and went to the shelf to drag a book out"

    #Magic Book Show

    data_ep_0 "Its a magic book its named \"Saint\""

    data_ep_0 "She open and read a page of a book "

    play audio data_sound_page_flip

    data_chr_00003_00004 "\[Thunder\]: A Class Legendary 8 Spell That Can Strike A Lightning On The Target Point"

    data_chr_00004_00000_00001 "hmm what? is this a spell? Let's try this. \[Thunder\]"

    data_ep_0 "She Tried To Cast It But It Did Not Work"

    data_ep_0 "Suddenly A Piece of paper dropped from the ceiling"

    data_chr_00004_00000_00001 "wheres that paper come from?"

    data_ep_0 "looks up and grab the paper"

    data_ep_0 "She open the paper and read the text written to it"

    data_chr_00003_00003 "\"To Cast Library Kind Spell You Can Think Of The Rarity, Book, Class, Type, Name Of The Spell and Level Of The Spell\""

    data_chr_00004_00000_00001 "what.... okay then"

    #Casting Sound

    data_ep_0 "She Tried To Cast The Spell Again"

    stop music
    
    data_chr_00004_00000_00001 "\[Legendary: Saint: Light: Lightning: 6\]"
    
    play sound data_sound_lightning
    
    $ renpy.pause(15)

    
    
    play music data_music_library_3 loop

    data_ep_0 "Suddenly a lightning strike to the room destroying the corridor and causing a fire"

    #Fire Sound

    data_ep_0 "She run out of the corridor and look back on what she done"

    stop sound

    data_ep_0 "to her surprise everything is back to normal with a another paper placed on one of the tables"

    data_chr_00003_00003 "\"Using a magic in the library can be dangerous so I made a testing room near the door you went in.\""

    data_chr_00003_00003 "\"Also you can't damage anything in the library so don't worry about what you did\""

    data_chr_00003_00003 "\"When Casting A Spell The Chanting Does Not Matter it's about how you define that spell you want\""

    data_chr_00004_00000_00001 "good grief I thought I destroy the library"

    data_ep_0 "She felt relieved after not getting a scolding paper"

    data_chr_00004_00000_00001 "every book here is interesting....time to read every book..."

    $ renpy.notify('Fast Forward')

    stop music

    data_ep_0 "As the time passes by she read a book after book but then a ring of a bell can be heard "

    #Ticking Sounds

    play sound data_sound_bell

    data_ep_0 "She panicked and look at the time"

    data_ep_0 "It's 7 o'Clock"

    data_chr_00004_00000_00001 "Good Grief I'm Gonna Be Late"

    return



