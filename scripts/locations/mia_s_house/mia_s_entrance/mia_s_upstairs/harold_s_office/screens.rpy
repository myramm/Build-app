screen harolds_house_office():
    add player.location.background

    imagebutton:
        focus_mask True
        align (0.5,0.97)
        idle "boxes/auto_option_generic_01.png"
        hover HoverImage("boxes/auto_option_generic_01.png")
        action ExitLocation()

    use mods_screens_hook("harolds_house_office")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
