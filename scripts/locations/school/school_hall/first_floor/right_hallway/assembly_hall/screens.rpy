screen assembly_hall():
    add player.location.background

    imagebutton:
        focus_mask True
        pos (761,348)
        idle game.timer.image("objects/object_door_111{}.png")
        hover HoverImage(game.timer.image("objects/object_door_111{}.png"))
        action MoveTo(L_school_righthallway)

    if M_dewitt.is_state(S_dewitt_attend_talent_show):
        imagebutton:
            focus_mask True
            pos (431,262)
            idle "objects/character_dewitt_05.png"
            hover HoverImage("objects/character_dewitt_05.png")
            action Hide("assembly_hall"), Jump(game.dialog_select("assembly_hall_dewitt_attend_talent_show"))

    elif M_dewitt.is_state(S_dewitt_talent_show):
        imagebutton:
            focus_mask True
            pos (431,262)
            idle "objects/character_dewitt_05.png"
            action NullAction()

        imagebutton:
            focus_mask True
            pos (9,369)
            idle "objects/character_kevin_03.png"
            hover HoverImage("objects/character_kevin_03.png")
            action Hide("assembly_hall"), Jump(game.dialog_select("assembly_hall_dewitt_talent_show"))

    elif L_school_assemblyhall.is_here(M_eve):
        imagebutton:
            focus_mask True
            pos 620, 356
            idle "characters/eve/buttons/character_eve_04.png"
            hover HoverImage("characters/eve/buttons/character_eve_04.png")
            action TalkTo(M_eve)

    use mods_screens_hook("assembly_hall")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
