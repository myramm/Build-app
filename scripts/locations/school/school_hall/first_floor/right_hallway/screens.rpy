screen school_right_hallway():
    add player.location.background

    if M_dewitt.is_state(S_dewitt_paint_trail):
        add "paint_trail_01" at center

    imagebutton:
        focus_mask True
        pos (350,700)
        idle "boxes/door07_option_01.png"
        hover HoverImage("boxes/door07_option_01.png")
        action MoveTo(L_school_hall)

    imagebutton:
        focus_mask True
        pos (14,205)
        idle game.timer.image("objects/object_locker_02{}.png")
        hover HoverImage(game.timer.image("objects/object_locker_02{}.png"))
        action MoveTo(L_school_locker_eve)

    imagebutton:
        focus_mask True
        pos (127,274)
        idle game.timer.image("objects/object_locker_03{}.png")
        hover HoverImage(game.timer.image("objects/object_locker_03{}.png"))
        action MoveTo(L_school_locker_mia)
    imagebutton:
        focus_mask True
        pos (210,328)
        idle game.timer.image("objects/object_locker_04{}.png")
        hover HoverImage(game.timer.image("objects/object_locker_04{}.png"))
        action MoveTo(L_school_locker_erik)

    imagebutton:
        focus_mask True
        pos (275,370)
        idle game.timer.image("objects/object_locker_05{}.png")
        hover HoverImage(game.timer.image("objects/object_locker_05{}.png"))
        action MoveTo(L_school_locker_ronda)

    imagebutton:
        focus_mask True
        pos (312,387)
        idle game.timer.image("objects/object_door_109{}.png")
        hover HoverImage(game.timer.image("objects/object_door_109{}.png"))
        action MoveTo(L_school_bridgetoffice)

    imagebutton:
        focus_mask True
        pos (619,436)
        idle game.timer.image("objects/object_posters_02{}.png")
        hover HoverImage(game.timer.image("objects/object_posters_02{}.png"))
        action Hide("school_right_hallway"), Jump("prom_poster")

    imagebutton:
        focus_mask True
        pos (683,364)
        idle game.timer.image("objects/object_door_110{}.png")
        hover HoverImage(game.timer.image("objects/object_door_110{}.png"))
        action MoveTo(L_school_assemblyhall)

    imagebutton:
        focus_mask True
        pos (766,325)
        idle game.timer.image("objects/object_locker_08{}.png")
        hover HoverImage(game.timer.image("objects/object_locker_08{}.png"))
        action MoveTo(L_school_locker_dexter)

    imagebutton:
        focus_mask True
        pos (847,279)
        idle game.timer.image("objects/object_locker_07{}.png")
        hover HoverImage(game.timer.image("objects/object_locker_07{}.png"))
        action MoveTo(L_school_locker_kevin)

    imagebutton:
        focus_mask True
        pos (952,219)
        idle game.timer.image("objects/object_locker_06{}.png")
        hover HoverImage(game.timer.image("objects/object_locker_06{}.png"))
        action MoveTo(L_school_locker_annie)

    if player.location.is_here(M_eve) and not M_dewitt.is_state(S_dewitt_attend_talent_show):
        imagebutton:
            focus_mask True
            pos (498,421)
            if M_eve.is_state(S_eve_ross_argument):
                idle "characters/eve/buttons/character_eve_02.png"
                hover HoverImage("characters/eve/buttons/character_eve_02.png")
            else:
                idle "characters/eve/buttons/character_eve_05.png"
                hover HoverImage("characters/eve/buttons/character_eve_05.png")
            action TalkTo(M_eve)

    if player.location.is_here(M_chad):
        imagebutton:
            focus_mask True
            pos (400,422)
            idle "objects/character_chad_01.png"
            hover HoverImage("objects/character_chad_01.png")
            action TalkTo(M_chad)

    use mods_screens_hook("school_right_hallway")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
