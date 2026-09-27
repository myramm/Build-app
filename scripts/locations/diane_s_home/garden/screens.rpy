screen dianes_garden():
    add L_diane_garden.background

    imagebutton:
        focus_mask True
        pos (26,369)
        idle game.timer.image("objects/object_door_08{}.png")
        hover HoverImage(game.timer.image("objects/object_door_08{}.png"))
        action MoveTo(L_diane_kitchen)

    if not L_diane_shed.locked and not game.timer.is_night():
        imagebutton:
            focus_mask True
            pos (686,315)
            idle game.timer.image("objects/object_door_09{}_02.png")
            hover HoverImage(game.timer.image("objects/object_door_09{}_02.png"))
            action Hide("dianes_garden"), Function(playSound), Jump(game.dialog_select("garden_shed_transition"))

    else:
        imagebutton:
            focus_mask True
            pos (686,345)
            idle game.timer.image("objects/object_door_09{}.png")
            hover HoverImage(game.timer.image("objects/object_door_09{}.png"))
            action MoveTo(L_diane_shed)

    if M_diane.is_state(S_diane_clean_garden, S_diane_clean_garden_report, S_diane_go_to_mall, S_diane_go_to_consumr, S_diane_get_bug_spray, S_diane_clear_bug_infested_garden):
        imagebutton:
            focus_mask True
            pos (36,535)
            idle game.timer.image("objects/object_garden_01_dead{}.png")
            hover HoverImage(game.timer.image("objects/object_garden_01_dead{}.png"))
            action Show("garden01_options")
    else:
        imagebutton:
            focus_mask True
            pos (36,535)
            idle game.timer.image("objects/object_garden_01{}.png")
            hover HoverImage(game.timer.image("objects/object_garden_01{}.png"))
            if M_diane.is_state(S_diane_check_shed_light):
                action MoveTo(L_diane_yard)
            else:
                action Show("garden01_options")

    if L_diane_garden.is_here(M_diane) and not M_diane.is_state(S_dia01_find):
        imagebutton:
            focus_mask True
            if M_diane.is_state(S_diane_dump_pump, S_diane_daylight_drinking, S_diane_make_drink, S_diane_return_drink, S_diane_drunken_garden_work):
                pos (347,493)
                idle "characters/diane/buttons/character_diane_06.png"
                hover HoverImage("characters/diane/buttons/character_diane_06.png")
            else:
                pos (491,397)
                if M_diane.get("aunt drink made"):
                    idle "characters/diane/buttons/character_diane_03.png"
                    hover HoverImage("characters/diane/buttons/character_diane_03.png")
                else:
                    idle "characters/diane/buttons/character_diane_01.png"
                    hover HoverImage("characters/diane/buttons/character_diane_01.png")
            action TalkTo(M_diane)

    imagebutton:
        focus_mask True
        if not game.timer.is_dark():
            pos (928,420)
        else:
            pos (928,416)
        idle game.timer.image("objects/object_crack_01{}.png")
        hover HoverImage(game.timer.image("objects/object_crack_01{}.png"))
        action MoveTo(L_church_graveyard)

    imagebutton:
        focus_mask True
        align (0.5,0.97)
        idle "boxes/auto_option_generic_01.png"
        hover HoverImage("boxes/auto_option_generic_01.png")
        action MoveTo(L_diane_yard)

    use mods_screens_hook("dianes_garden")

screen garden01_options():
    imagebutton:
        idle "ground.png"
        action Hide("garden01_options")

    imagebutton:
        focus_mask True
        align (0.5,0.82)
        idle "boxes/garden_option_01.png"
        hover HoverImage("boxes/garden_option_01.png")
        action Hide("garden01_options"), Hide("dianes_barn_garden"), Hide("dianes_garden"), Jump("diane_garden_check")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
