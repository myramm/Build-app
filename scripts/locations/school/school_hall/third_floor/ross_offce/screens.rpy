screen mrs_ross_office():
    add game.timer.image("backgrounds/location_school_office3_day{}.jpg")

    if player.location.is_here(M_ross):
        if (M_ross.is_state(S_ross_paint_with_body) and game.timer.is_evening()) or M_ross.is_state(S_ross_end):
            imagebutton:
                focus_mask True
                pos (89,542)
                idle game.timer.image("objects/character_ross_03{}.png")
                hover HoverImage(game.timer.image("objects/character_ross_03{}.png"))
                action Hide("mrs_ross_office"), Jump("button_ross_office_dialogue")
        else:
            imagebutton:
                focus_mask True
                pos (560,463)
                idle "objects/character_ross_02.png"
                hover HoverImage("objects/character_ross_02.png")
                action Hide("mrs_ross_office"), Jump("button_ross_office_dialogue")

    imagebutton:
        focus_mask True
        align (0.5,0.97)
        idle "boxes/auto_option_generic_02.png"
        hover HoverImage("boxes/auto_option_generic_02.png")
        action MoveTo(L_school_floor3)

    use mods_screens_hook("mrs_ross_office")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
