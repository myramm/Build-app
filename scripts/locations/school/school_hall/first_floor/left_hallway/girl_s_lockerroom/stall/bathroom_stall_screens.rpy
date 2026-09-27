screen bathroom_stall():
    add player.location.background

    imagebutton:
        focus_mask True
        align 0.5,0.95
        idle "boxes/auto_option_generic_01.png"
        hover HoverImage("boxes/auto_option_generic_01.png")
        action ExitLocation()

    use mods_screens_hook('bathroom_stall')
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
