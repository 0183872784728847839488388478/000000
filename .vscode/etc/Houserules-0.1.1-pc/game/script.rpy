label start:
    $ GoTo(bedroom)
    python:
        CharacterM41D.Equipped = wardrobeslotsmaid
        CharacterPlayer.Equipped = wardrobeslotsplayer
        Wardrobe("M41D", "puton", "White Gloves", "None", "no")
        Wardrobe("M41D", "puton", "Black Stockings", "None", "no")
        Wardrobe("M41D", "puton", "Maid Dress", "None", "no")
        Wardrobe("M41D", "puton", "Black Bra", "None", "no")
        Wardrobe("M41D", "puton", "Black Thong", "None", "no")
    jump start2

label start2:
    menu:
        "go to test grounds (dev room)":
            jump test_grounds
        "stay in game":
            pass

    developer "Welcome to House Rules v0.1.0. Please keep in mind that this is a very early build of the game. Many planned features are still being built and are not present in this version of the game."
    developer "All artwork in House Rules was made with Stable Diffusion AI Art engine."
    developer "Huge thanks to all the early testers for putting up with the horrible mess that was me learning how to Python."

    narrator "What is your name?"
    default povname = "Alex"
    default maidname = "M41D"
    default randomname = "Erin"
    default randomsentence = ""
    $ povname = renpy.input("(Protagonist is male, but feel free to use any name you like. The pronouns used will be he/him, at least for a good while.)", length=32, default="Alex", exclude="1234567890!@#$%^&*()-=_+[]{};':,./<>?")
    $ povname = povname.strip()
    if not povname:
        $ povname = "Alex"

    python:
        CharacterPlayer.Name = povname
    pov "My name is [povname]."

    narrator "Hi [povname], this game contains adult themed materials, art and writing, possibly some content your mom would really rather you didn't see. Please only proceed if you are above the legal age for such activities and are ok with all this."
    menu:
        "Yeah I'm an adult!":
            # jump content_selection
            jump intro
        "Heck no I'm out!":
            return
            # This ends the game.

label content_selection:
    maid "Please select content you're ok with. (PLACEHOLDER, NOTHING HERE NOW)"
    # Todo content selection menu with output saved as variables for the story.
    jump intro

label test_grounds:

    narrator "Welcome to the test grounds. This section wasn't really supposed to be in this build but as I didn't finish as much as I was hoping to, I decided to leave it in so you can at least have a peak into future content."

    menu:
        "Go back to start":
            jump start2
        "Location testing":
            jump location_testing
        "Task testing":
            jump action_testing
        "Time testing":
            jump time_testing
        "Paperdoll testing":
            jump paperdoll_testing
        #"Minigame testing":
            #jump minigame_testing

label location_testing:
    menu:
        "Go to bathroom":
            narrator "switching from [current_location[0]] to [bathroom[0]]"
            $ GoTo(bathroom)
        "Go to bedroom":
            narrator "switching from [current_location[0]] to [bedroom[0]]"
            $ GoTo(bedroom)
        "Go to foyer":
            narrator "switching from [current_location[0]] to [foyer[0]]"
            $ GoTo(foyer)
        "Go to kitchen":
            narrator "switching from [current_location[0]] to [kitchen[0]]"
            $ GoTo(kitchen)
        "Go to living room":
            narrator "switching from [current_location[0]] to [livingroom[0]]"
            $ GoTo(livingroom)
        "Enter WIP Navigation Mode":
            call screen nav(True)
            jump location_testing
        "return":
            jump test_grounds

    narrator "current location is [current_location[0]]"
    jump location_testing

label action_testing:
    menu:
        "Show my task list":
            call screen questlog()
        "Add a test task in the bedroom":
            $ action_manager.add_action(
                task="Slay a dragon", 
                location="bedroom", 
                notes="A dragon is pestering the princess, I should kill it.", 
                minigame="placeholder", 
                deadline=1,
                status="active", 
                tasktype="chore", 
                required="mandatory")
        "Add a test task in the bathroom":
            $ action_manager.add_action(
                task="Pee", 
                location="bathroom", 
                notes="I really need to peeeee", 
                minigame="placeholder", 
                deadline=1,
                status="active", 
                tasktype="chore", 
                required="mandatory")
        "Add a test task in the kitchen":
            $ action_manager.add_action(
                task="Make a coffee", 
                location="kitchen", 
                notes="I should drink some coffee...", 
                minigame="placeholder", 
                deadline=1,
                status="active", 
                tasktype="chore", 
                required="mandatory")
        "return":
            jump test_grounds
    jump action_testing


label time_testing:
    narrator "It is now [current_weekday_name] [current_timeperiod], this is game day number [current_day]"
    menu:
        "Add 1 period":
            $ AdvanceTime(1, None)
        "Add 3 periods":
            $ AdvanceTime(3, None)
        "Advance till morning":
            $ AdvanceTime(0, 1)
        "Advance 1 day":
            $ AdvanceDay(1, None, True)
        "Advance 3 days":
            $ AdvanceDay(3, None, True)
        "Advance till Wednesday":
            $ AdvanceDay(0, 2, 1)
        "What time is it?":
            $ ShowTime()
        "return":
            jump test_grounds
    jump time_testing

label paperdoll_testing:
    narrator "This area is for testing the paperdoll"
    menu:
        "Show random emote clothed":
            $ Paperdoll(actor="M41D", emote="random", pose="Basic", emoteoverride="default", clothes="default", genitals="default")
        "Show random emote in underwear":
            $ Paperdoll(actor="M41D", emote="random", pose="Basic", emoteoverride="default", clothes="underwear", genitals="default")
        "Show random emote naked":
            $ Paperdoll(actor="M41D", emote="random", pose="Basic", emoteoverride="default", clothes="naked", genitals="default")
        "Show random emote naked aroused":
            $ Paperdoll(actor="M41D", emote="random", pose="Basic", emoteoverride="default", clothes="naked", genitals="aroused")    
        "Face override test":
            $ override = renpy.input("range 1-203", allow="1234567890", length=3)
            $ Paperdoll(actor="M41D", emote="Neutral", pose="Basic", emoteoverride=[override], clothes="default", genitals="default")
        "Wardrobe test":
            narrator "Selecting an item changes M41D into that item. If the item is already equipped, the item should be unequipped instead."
            menu:
                "Tops":
                    menu:
                        "Maid Dress":
                            python:
                                if wardrobe_MaidDress in CharacterM41D.Equipped.values():
                                    Wardrobe(actor = "M41D", action="strip", item="Maid Dress", preset="None", override="no")
                                else:
                                    Wardrobe(actor = "M41D", action="puton", item="Maid Dress", preset="None", override="no")
                        "Black Dress":
                            python:
                                if wardrobe_DressBlack in CharacterM41D.Equipped.values():
                                    Wardrobe(actor = "M41D", action="strip", item="Black Dress", preset="None", override="no")
                                else:
                                    Wardrobe(actor = "M41D", action="puton", item="Black Dress", preset="None", override="no")
                        "Red Dress":
                            python:
                                if wardrobe_DressRed in CharacterM41D.Equipped.values():
                                    Wardrobe(actor = "M41D", action="strip", item="Red Dress", preset="None", override="no")
                                else:
                                    Wardrobe(actor = "M41D", action="puton", item="Red Dress", preset="None", override="no")
                        "Black Top":
                            python:
                                if wardrobe_TopBlack in CharacterM41D.Equipped.values():
                                    Wardrobe(actor = "M41D", action="strip", item="Black Top", preset="None", override="no")
                                else:
                                    Wardrobe(actor = "M41D", action="puton", item="Black Top", preset="None", override="no")
                        "return":
                            jump paperdoll_testing
                "Bras":
                    menu:
                        "Black Bra":
                            python:
                                if wardrobe_BraBlack in CharacterM41D.Equipped.values():
                                    Wardrobe(actor = "M41D", action="strip", item="Black Bra", preset="None", override="no")
                                else:
                                    Wardrobe(actor = "M41D", action="puton", item="Black Bra", preset="None", override="no")
                        "Pink Bra":
                            python:
                                if wardrobe_BraPink in CharacterM41D.Equipped.values():
                                    Wardrobe(actor = "M41D", action="strip", item="Pink Bra", preset="None", override="no")
                                else:
                                    Wardrobe(actor = "M41D", action="puton", item="Pink Bra", preset="None", override="no")
                        "White Bra":
                            python:
                                if wardrobe_BraWhite in CharacterM41D.Equipped.values():
                                    Wardrobe(actor = "M41D", action="strip", item="White Bra", preset="None", override="no")
                                else:
                                    Wardrobe(actor = "M41D", action="puton", item="White Bra", preset="None", override="no")
                        "Hotpink Bra":
                            python:
                                if wardrobe_BraHotpink in CharacterM41D.Equipped.values():
                                    Wardrobe(actor = "M41D", action="strip", item="Hotpink Bra", preset="None", override="no")
                                else:
                                    Wardrobe(actor = "M41D", action="puton", item="Hotpink Bra", preset="None", override="no")
                        "return":
                            jump paperdoll_testing
                "Panties":
                    menu:
                        "Black Thong":
                            python:
                                if wardrobe_ThongBlack in CharacterM41D.Equipped.values():
                                    Wardrobe(actor = "M41D", action="strip", item="Black Thong", preset="None", override="no")
                                else:
                                    Wardrobe(actor = "M41D", action="puton", item="Black Thong", preset="None", override="no")
                        "Pink Thong":
                            python:
                                if wardrobe_ThongPink in CharacterM41D.Equipped.values():
                                    Wardrobe(actor = "M41D", action="strip", item="Pink Thong", preset="None", override="no")
                                else:
                                    Wardrobe(actor = "M41D", action="puton", item="Pink Thong", preset="None", override="no")
                        "Hotpink Thong":
                            python:
                                if wardrobe_ThongHotpink in CharacterM41D.Equipped.values():
                                    Wardrobe(actor = "M41D", action="strip", item="Hotpink Thong", preset="None", override="no")
                                else:
                                    Wardrobe(actor = "M41D", action="puton", item="Hotpink Thong", preset="None", override="no")
                        "White Thong":
                            python:
                                if wardrobe_ThongPink in CharacterM41D.Equipped.values():
                                    Wardrobe(actor = "M41D", action="strip", item="Pink Thong", preset="None", override="no")
                                else:
                                    Wardrobe(actor = "M41D", action="puton", item="Pink Thong", preset="None", override="no")
                        "Black Panties":
                            python:
                                if wardrobe_PantiesBlack in CharacterM41D.Equipped.values():
                                    Wardrobe(actor = "M41D", action="strip", item="Black Panties", preset="None", override="no")
                                else:
                                    Wardrobe(actor = "M41D", action="puton", item="Black Panties", preset="None", override="no")
                        "Red Panties":
                            python:
                                if wardrobe_PantiesRed in CharacterM41D.Equipped.values():
                                    Wardrobe(actor = "M41D", action="strip", item="Red Panties", preset="None", override="no")
                                else:
                                    Wardrobe(actor = "M41D", action="puton", item="Red Panties", preset="None", override="no")
                        "Hotpink Panties":
                            python:
                                if wardrobe_PantiesHotpink in CharacterM41D.Equipped.values():
                                    Wardrobe(actor = "M41D", action="strip", item="Hotpink Panties", preset="None", override="no")
                                else:
                                    Wardrobe(actor = "M41D", action="puton", item="Hotpink Panties", preset="None", override="no")
                        "return":
                            jump paperdoll_testing
                "Arms":
                    menu:
                        "White Gloves":
                            python:
                                if wardrobe_GlovesWhite in CharacterM41D.Equipped.values():
                                    Wardrobe(actor = "M41D", action="strip", item="White Gloves", preset="None", override="no")
                                else:
                                    Wardrobe(actor = "M41D", action="puton", item="White Gloves", preset="None", override="no")
                        "return":
                            jump paperdoll_testing
                "Legs":
                    menu:
                        "Black Stockings":
                            python:
                                if wardrobe_StockingsBlack in CharacterM41D.Equipped.values():
                                    Wardrobe(actor = "M41D", action="strip", item="Black Stockings", preset="None", override="no")
                                else:
                                    Wardrobe(actor = "M41D", action="puton", item="Black Stockings", preset="None", override="no")
                        "Pink Stockings":
                            python:
                                if wardrobe_StockingsPink in CharacterM41D.Equipped.values():
                                    Wardrobe(actor = "M41D", action="strip", item="Pink Stockings", preset="None", override="no")
                                else:
                                    Wardrobe(actor = "M41D", action="puton", item="Pink Stockings", preset="None", override="no")
                        "Hotpink Stockings":
                            python:
                                if wardrobe_StockingsHotpink in CharacterM41D.Equipped.values():
                                    Wardrobe(actor = "M41D", action="strip", item="Hotpink Stockings", preset="None", override="no")
                                else:
                                    Wardrobe(actor = "M41D", action="puton", item="Hotpink Stockings", preset="None", override="no")
                        "White Stockings":
                            python:
                                if wardrobe_StockingsPink in CharacterM41D.Equipped.values():
                                    Wardrobe(actor = "M41D", action="strip", item="Pink Stockings", preset="None", override="no")
                                else:
                                    Wardrobe(actor = "M41D", action="puton", item="Pink Stockings", preset="None", override="no")
                        "return":
                            jump paperdoll_testing
                "return":
                    jump paperdoll_testing

        "Cycle genitals":
            python:
                if CharacterM41D.Genitals == bodypart_Vagina:
                    CharacterM41D.Genitals = bodypart_LargePenis
                else:
                    CharacterM41D.Genitals = bodypart_Vagina

                print(CharacterM41D.Genitals.BodypartSize)
            narrator "genitals switched, refresh paperdoll to re-render"
        "Clear Paperdoll":
            $ PaperdollKill(0.5)
        "Return":
            $ PaperdollKill(0.1)
            jump test_grounds
    jump paperdoll_testing

label minigame_testing:
    narrator "this area is for testing the minigames"
    menu:
        "test":
            call screen rhythm_game()
        "return":
            jump test_grounds
    jump minigame_testing