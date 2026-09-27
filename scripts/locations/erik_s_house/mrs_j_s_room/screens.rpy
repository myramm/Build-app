screen mrs_johnsons_room():
    add player.location.background

    imagebutton:
        focus_mask True
        pos (696,498)
        idle game.timer.image("objects/object_ball_01{}.png")
        hover HoverImage(game.timer.image("objects/object_ball_01{}.png"))
        action Hide("mrs_johnsons_room"), Jump("mrsj_ball")

    if player.location.is_here(M_mrsj):
        if game.timer.is_dark() and M_erik.finished_state(S_erik_learn_prep):
            imagebutton:
                focus_mask True
                pos (826,300)
                idle "objects/character_mrsj_03.png"
                hover HoverImage("objects/character_mrsj_03.png")
                action Hide("mrs_johnsons_room"), Jump("mrsj_button_dialogue")

        elif game.timer.is_dark() and M_mrsj.finished_state(S_mrsj_cupid_report):
            imagebutton:
                focus_mask True
                pos (250,420)
                idle "objects/character_mrsj_04.png"
                hover HoverImage("objects/character_mrsj_04.png")
                action Hide("mrs_johnsons_room"), Jump("mrsj_button_dialogue")

        else:
            imagebutton:
                focus_mask True
                pos (0,410)
                idle game.timer.image("objects/object_bed_04_day{}.png")
                hover HoverImage(game.timer.image("objects/object_bed_04_day{}.png"))
                action Hide("mrs_johnsons_room"), Jump("mrsj_button_dialogue")

    imagebutton:
        focus_mask True
        align (0.5,0.97)
        idle "boxes/auto_option_generic_01.png"
        hover HoverImage("boxes/auto_option_generic_01.png")
        action MoveTo(L_erikhouse_entrance)

    use mods_screens_hook("mrs_johnsons_room")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
