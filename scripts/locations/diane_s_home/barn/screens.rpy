screen dianes_barn_building():
    add L_diane_barn_building.background

    if L_diane_barn_building.is_here(M_diane):
        imagebutton:
            focus_mask True
            pos (635,506)
            idle "characters/diane/buttons/character_diane_shirtless_construction.png"
            hover HoverImage("characters/diane/buttons/character_diane_shirtless_construction.png")
            action TalkTo(M_diane)

    use mods_screens_hook("dianes_barn_building")

screen dianes_barn():
    add L_diane_barn.background

    imagebutton:
        focus_mask True
        pos (563,482)
        idle game.timer.image("objects/object_door_107{}.png")
        hover HoverImage(game.timer.image("objects/object_door_107{}.png"))
        action MoveTo(L_diane_barn_garden)

    imagebutton:
        focus_mask True
        pos (247,472)
        idle game.timer.image("objects/object_door_134{}.png")
        hover HoverImage(game.timer.image("objects/object_door_134{}.png"))
        action MoveTo(L_diane_barn_interior)

    if L_diane_barn.is_here(M_daisy):
        imagebutton:
            focus_mask True
            pos (812, 487)
            idle "characters/daisy/buttons/character_daisy_picking.png"
            hover HoverImage("characters/daisy/buttons/character_daisy_picking.png")
            action TalkTo(M_daisy)

    use mods_screens_hook("dianes_barn")

screen dianes_barn_interior():
    add L_diane_barn_interior.background
    if player.location.is_here(M_daisy):
        if game.timer.is_dark():
            imagebutton:
                focus_mask True
                pos (198, 61)
                idle "characters/daisy/buttons/character_daisy_sleeping.png"
                hover HoverImage("characters/daisy/buttons/character_daisy_sleeping.png")
                action TalkTo("daisy")
        else:
            imagebutton:
                focus_mask True
                if M_daisy.pregnancy.gave_birth:
                    pos (27,413)
                    idle "characters/daisy/buttons/character_daisy_baby_" + M_daisy.pregnancy.baby_gender +".png"
                    hover HoverImage("characters/daisy/buttons/character_daisy_baby_" + M_daisy.pregnancy.baby_gender +".png")
                else:
                    pos (27,413)
                    idle "characters/daisy/buttons/character_daisy_[M_daisy.outfit.get][M_daisy.pregnancy.to_string].png"
                    hover HoverImage("characters/daisy/buttons/character_daisy_" + M_daisy.outfit.get + M_daisy.pregnancy.to_string + ".png")
                action TalkTo("daisy")
    imagebutton:
        focus_mask True
        pos (929,364)
        idle game.timer.image("objects/object_door_138{}.png")
        hover HoverImage(game.timer.image("objects/object_door_138{}.png"))
        action MoveTo(L_diane_barn_garden)

    imagebutton:
        focus_mask True
        align 0.5,0.95
        idle "boxes/auto_option_generic_01.png"
        hover HoverImage("boxes/auto_option_generic_01.png")
        action ExitLocation()

    if player.location.is_here(M_diane):
        imagebutton:
            focus_mask True
            if M_diane.pregnancy.gave_birth:
                pos (715,375)
                idle M_diane.get_button_path('casual', use_day_timer=True, use_baby=True)
                hover HoverImage(M_diane.get_button_path('casual', use_day_timer=True, use_baby=True))
            else:
                pos (613,357)
                idle "characters/diane/buttons/character_diane_[M_diane.outfit.get][M_diane.pregnancy.to_string].png"
                hover HoverImage("characters/diane/buttons/character_diane_" + M_diane.outfit.get + M_diane.pregnancy.to_string + ".png")
            action TalkTo(M_diane)

    use mods_screens_hook("dianes_barn_interior")

screen dianes_barn_garden():
    add L_diane_barn_garden.background

    imagebutton:
        focus_mask True
        pos (55,395)
        idle game.timer.image("objects/object_door_135{}.png")
        hover HoverImage(game.timer.image("objects/object_door_135{}.png"))
        action MoveTo(L_diane_barn_interior)

    imagebutton:
        focus_mask True
        align 0.5,0.95
        idle "boxes/auto_option_generic_01.png"
        hover HoverImage("boxes/auto_option_generic_01.png")
        action ExitLocation()

    imagebutton:
        focus_mask True
        pos (686,315)
        idle game.timer.image("objects/object_door_09{}_02.png")
        hover HoverImage(game.timer.image("objects/object_door_09{}_02.png"))
        action MoveTo(L_diane_shed)

    imagebutton:
        focus_mask True
        if not game.timer.is_dark():
            pos (928,420)
        else:
            pos (928,416)
        idle game.timer.image("objects/object_crack_01{}.png")
        hover HoverImage(game.timer.image("objects/object_crack_01{}.png"))
        action MoveTo(L_church_graveyard)

    if M_daisy.is_state(S_daisy_assembled_statue, S_daisy_viewed_statue):
        imagebutton:
            focus_mask True
            pos (150,496)
            idle "objects/object_statue_garden_01.png"
            hover HoverImage("objects/object_statue_garden_01.png")
            action Hide("dianes_barn_garden"), Jump("barn_garden_statue_dialogue")

    imagebutton:
        focus_mask True
        pos (36,535)
        idle game.timer.image("objects/object_garden_01{}.png")
        hover HoverImage(game.timer.image("objects/object_garden_01{}.png"))
        if M_daisy.is_state(S_daisy_awakened_statue):
            action MoveTo(L_diane_yard)
        else:
            action Show("garden01_options")

    use mods_screens_hook("dianes_barn_garden")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
