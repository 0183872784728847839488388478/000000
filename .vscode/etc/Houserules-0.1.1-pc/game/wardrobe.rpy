init python:
    
    # Wardrobe rules:
    # Slots:
    #   0:  Head            (headdress, mask maybe?)
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
    #   Available:          boolean
    #   Locked:             boolean
    #   Housing:            item
    # Item Properties:
    #   ItemName:           string
    #   ItemSlot:           integar
    #   LockSlot:           integar
    #   Special:            ??? (boons? Stuff? Status effects? idk)
    #   Directory:          path to file
    
    class WardrobeItem:
        def __init__(self,*, name=None, slot=None, lockslot=None, special=None, directory=None):
            self.ItemName   = name
            self.ItemSlot   = slot
            self.LockSlot   = lockslot or None
            self.Special    = special or None
            self.Directory  = directory

    wardrobe_StockingsBlack =   WardrobeItem(name="Black Stockings", slot=5, directory="StockingsBlack.png")
    wardrobe_StockingsWhite =   WardrobeItem(name="White Stockings", slot=5, directory="StockingsWhite.png")
    wardrobe_StockingsPink =    WardrobeItem(name="Pink Stockings", slot=5, directory="StockingsPink.png")
    wardrobe_StockingsHotpink = WardrobeItem(name="Hotpink Stockings", slot=5, directory="StockingsHotpink.png")

    wardrobe_PantiesBlack =     WardrobeItem(name="Black Panties", slot=1, directory="PantiesBlack.png")
    wardrobe_PantiesRed =       WardrobeItem(name="Red Panties", slot=1, directory="PantiesRed.png")
    wardrobe_PantiesHotpink =   WardrobeItem(name="Hopink Panties", slot=1, directory="PantiesHotpink.png")

    wardrobe_ThongBlack =       WardrobeItem(name="Black Thong", slot=1, directory="ThongBlack.png")
    wardrobe_ThongHotpink =     WardrobeItem(name="Hotpink Thong", slot=1, directory="ThongHotpink.png")
    wardrobe_ThongPink =        WardrobeItem(name="Pink Thong", slot=1, directory="ThongPink.png")
    wardrobe_ThongRed =         WardrobeItem(name="Red Thong", slot=1, directory="ThongRed.png")
    wardrobe_ThongWhite =       WardrobeItem(name="White Thong", slot=1, directory="ThongWhite.png")

    wardrobe_BraBlack =         WardrobeItem(name="Black Bra", slot=2, directory="BraBlack.png")
    wardrobe_BraHotpink =       WardrobeItem(name="Hotpink Bra", slot=2, directory="BraHotpink.png")
    wardrobe_BraPink =          WardrobeItem(name="Pink Bra", slot=2, directory="BraPink.png")
    wardrobe_BraWhite =         WardrobeItem(name="White Bra", slot=2, directory="BraWhite.png")
    wardrobe_BraRed =           WardrobeItem(name="Red Bra", slot=2, directory="BraRed.png")

    wardrobe_MaidDress =        WardrobeItem(name="Maid Dress", slot=3, lockslot=4, directory="MaidDress.png")
    wardrobe_DressRed =         WardrobeItem(name="Red Dress", slot=3, lockslot=4, directory="RedDress.png")
    wardrobe_DressBlack =       WardrobeItem(name="Black Dress", slot=3, lockslot=4, directory="BlackDress.png")

    wardrobe_TopBlack =         WardrobeItem(name="Black Top", slot=3, directory="TopBlack.png")

    wardrobe_GlovesWhite =      WardrobeItem(name="White Gloves", slot=6, directory="GlovesWhite.png")
