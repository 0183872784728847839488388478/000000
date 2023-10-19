init python:

    class Bodypart:
        def __init__(self,*, name=None, size=None, special=None, directory=None):
            self.BodypartName   = name
            self.BodypartSize   = size or 0
            self.Special        = special or None
            self.Directory      = directory or ""

    bodypart_FlatBreasts        = Bodypart(name="flat chest", size=0, special=None, directory="")
    bodypart_TinyBreasts        = Bodypart(name="tiny chest", size=1, special=None, directory="")
    bodypart_SmallBreasts       = Bodypart(name="small chest", size=2, special=None, directory="")
    bodypart_AverageBreasts     = Bodypart(name="average chest", size=3, special=None, directory="")
    bodypart_LargeBreasts       = Bodypart(name="Large chest", size=4, special=None, directory="")
    bodypart_HugeBreasts        = Bodypart(name="Huge chest", size=5, special=None, directory="")

    bodypart_Vagina             = Bodypart(name="pussy", size=0, special=None, directory="")
    bodypart_TinyPenis          = Bodypart(name="tiny penis", size=1, special=None, directory="")
    bodypart_SmallPenis         = Bodypart(name="small penis", size=2, special=None, directory="")
    bodypart_AveragePenis       = Bodypart(name="average penis", size=3, special=None, directory="")
    bodypart_LargePenis         = Bodypart(name="Large penis", size=4, special=None, directory="")
    bodypart_HugePenis          = Bodypart(name="Huge penis", size=5, special=None, directory="")

    bodypart_FlatAss            = Bodypart(name="flat ass", size=0, special=None, directory="")
    bodypart_TinyAss            = Bodypart(name="budding ass", size=1, special=None, directory="")
    bodypart_SmallAss           = Bodypart(name="small ass", size=2, special=None, directory="")
    bodypart_AverageAss         = Bodypart(name="average ass", size=3, special=None, directory="")
    bodypart_LargeAss           = Bodypart(name="Large ass", size=4, special=None, directory="")
    bodypart_HugeAss            = Bodypart(name="Huge ass", size=5, special=None, directory="")

    breastsdictionary = {
        "breasts0"  :   bodypart_FlatBreasts,
        "breasts1"  :   bodypart_TinyBreasts,
        "breasts2"  :   bodypart_SmallBreasts,
        "breasts3"  :   bodypart_AverageBreasts,
        "breasts4"  :   bodypart_LargeBreasts,
        "breasts5"  :   bodypart_HugeBreasts
    }

    genitalsdictionary = {
        "genitals0"  :   bodypart_Vagina,
        "genitals1"  :   bodypart_TinyPenis,
        "genitals2"  :   bodypart_SmallPenis,
        "genitals3"  :   bodypart_AveragePenis,
        "genitals4"  :   bodypart_LargePenis,
        "genitals5"  :   bodypart_HugePenis
    }

    assdictionary = {
        "ass0"  :   bodypart_FlatAss,
        "ass1"  :   bodypart_TinyAss,
        "ass2"  :   bodypart_SmallAss,
        "ass3"  :   bodypart_AverageAss,
        "ass4"  :   bodypart_LargeAss,
        "ass5"  :   bodypart_HugeAss
    }

    bodypartdictionary = {
        "breasts"   :   breastsdictionary,
        "genitals"  :   genitalsdictionary,
        "ass"       :   assdictionary
    }