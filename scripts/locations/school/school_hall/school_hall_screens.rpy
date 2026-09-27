screen school_hall():
    add player.location.background

    if M_dewitt.is_state(S_dewitt_paint_trail):
        add "paint_trail_02" at center

    imagebutton:
        focus_mask True
        pos (434,449)
        idle game.timer.image("objects/object_door_05{}.png")
        hover HoverImage(game.timer.image("objects/object_door_05{}.png"))
        action MoveTo(L_school_track)


    imagebutton:
        focus_mask True
        pos (615,407)
        idle game.timer.image("objects/object_door_62{}.png")
        hover HoverImage(game.timer.image("objects/object_door_62{}.png"))
        action MoveTo(L_school_musicclassroom)

    imagebutton:
        focus_mask True
        pos (362,411)
        idle game.timer.image("objects/object_door_63{}.png")
        hover HoverImage(game.timer.image("objects/object_door_63{}.png"))
        action MoveTo(L_school_scienceclassroom)

    imagebutton:
        focus_mask True
        pos (857,125)
        idle game.timer.image("objects/object_door_06{}.png")
        hover HoverImage(game.timer.image("objects/object_door_06{}.png"))
        action MoveTo(L_school_frenchclassroom)

    imagebutton:
        focus_mask True
        pos (666,377)
        idle game.timer.image("objects/object_door_112{}.png")
        hover HoverImage(game.timer.image("objects/object_door_112{}.png"))
        action MoveTo(L_school_floor2)

    imagebutton:
        focus_mask True
        pos (222,225)
        idle game.timer.image("objects/object_sign_01{}.png")
        hover HoverImage(game.timer.image("objects/object_sign_01{}.png"))
        action MoveTo(L_school_lefthallway)

    imagebutton:
        focus_mask True
        pos (694,225)
        idle game.timer.image("objects/object_sign_02{}.png")
        hover HoverImage(game.timer.image("objects/object_sign_02{}.png"))
        action MoveTo(L_school_righthallway)

    imagebutton:
        focus_mask True
        pos (36,235)
        idle game.timer.image("objects/object_locker_01{}.png")
        hover HoverImage(game.timer.image("objects/object_locker_01{}.png"))
        action MoveTo(L_school_locker_MC)

    imagebutton:
        focus_mask True
        align 0.5,0.95
        idle "boxes/auto_option_generic_01.png"
        hover HoverImage("boxes/auto_option_generic_01.png")
        action MoveTo(L_school_front)

    use mods_screens_hook("school_hall")

screen school_locker():
    add game.timer.image("mc_locker{}")

    imagebutton:
        focus_mask True
        pos (562,57)
        idle game.timer.image("objects/object_paper_01{}.png")
        hover HoverImage(game.timer.image("objects/object_paper_01{}.png"))
        action Show("school_locker_list")

    imagebutton:
        focus_mask True
        pos (332,61)
        idle game.timer.image("objects/object_report_01{}.png")
        hover HoverImage(game.timer.image("objects/object_report_01{}.png"))
        action HideAll(), Jump("school_locker_report")

    if not player.has_item("card04"):
        imagebutton:
            focus_mask True
            pos (308,599)
            idle game.timer.image("objects/object_card_02{}.png")
            hover HoverImage(game.timer.image("objects/object_card_02{}.png"))
            action Function(player.get_item, "card04"), ShowPopup('give', 'card04')

    if M_roxxy.is_state(S_roxxy_lolipop_for_lolipop, S_roxxy_lolipop_just_once) and not player.has_item("roxxy_homework") and not game.timer.is_dark():
        imagebutton:
            focus_mask True
            pos (675,440)
            idle "objects/object_homework_01.png"
            hover HoverImage("objects/object_homework_01.png")
            action Hide("school_locker"), Jump("roxxy_homework_pickup_dialogue")

    imagebutton:
        focus_mask True
        align (0.5,0.97)
        idle "boxes/auto_option_generic_02.png"
        hover HoverImage("boxes/auto_option_generic_02.png")
        action MoveTo(L_school_hall)

    use mods_screens_hook("school_locker")

screen roxxy_locker_sex_options():
    tag quick_menu

    imagebutton:
        focus_mask True
        pos (250,700)
        idle "buttons/judith_stage02_01.png"
        hover HoverImage("buttons/judith_stage02_01.png")
        action Hide("roxxy_locker_sex_options"), Jump("roxxy_locker_sex_loop")

    imagebutton:
        focus_mask True
        pos (450,700)
        idle "buttons/diane_stage01_02.png"
        hover HoverImage("buttons/diane_stage01_02.png")
        action Hide("roxxy_locker_sex_options"), Jump("roxxy_locker_sex_cum")

    if anim_toggle:
        if M_roxxy.get("sex speed") < .09:
            imagebutton:
                focus_mask True
                pos (250,735)
                idle "buttons/speed_02.png"
                hover HoverImage("buttons/speed_02.png")
                action Hide("roxxy_locker_sex_options"), Function(M_roxxy.set, "sex speed", M_roxxy.get("sex speed") + 0.03), Jump("roxxy_locker_sex_loop")

        if M_roxxy.get("sex speed") > .031:
            imagebutton:
                focus_mask True
                pos (450,735)
                idle "buttons/speed_01.png"
                hover HoverImage("buttons/speed_01.png")
                action Hide("roxxy_locker_sex_options"), Function(M_roxxy.set, "sex speed", M_roxxy.get("sex speed") - 0.03), Jump("roxxy_locker_sex_loop")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
