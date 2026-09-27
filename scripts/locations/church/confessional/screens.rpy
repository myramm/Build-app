screen church_confessional_left():
    add L_church_confessional_left.background

    imagebutton:
        focus_mask True
        align 0.5,0.95
        idle "boxes/auto_option_generic_01.png"
        hover HoverImage("boxes/auto_option_generic_01.png")
        action ExitLocation()

screen church_confessional_right():
    add L_church_confessional_right.background

    imagebutton:
        focus_mask True
        align 0.5,0.95
        idle "boxes/auto_option_generic_01.png"
        hover HoverImage("boxes/auto_option_generic_01.png")
        action ExitLocation()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
