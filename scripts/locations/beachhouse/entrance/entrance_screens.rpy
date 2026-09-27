screen beach_house_entrance():
    add player.location.background

    imagebutton:
        focus_mask True
        pos (183,283)
        idle game.timer.image("objects/object_door_117{}.png")
        hover HoverImage(game.timer.image("objects/object_door_117{}.png"))
        action MoveTo(L_beachhouse_kitchen)

    imagebutton:
        focus_mask True
        pos (632,25)
        idle game.timer.image("objects/object_stairs_08{}.png")
        hover HoverImage(game.timer.image("objects/object_stairs_08{}.png"))
        action MoveTo(L_beachhouse_bedroom)

    if L_beachhouse_entrance.is_here(M_consuela):
        imagebutton:
            focus_mask True
            pos 489, 414

            if 1 < M_consuela.pregnancy.stage < 5 and M_consuela.outfit.is_naked:
                pos 497, 366
                idle M_consuela.get_button_path('beachhouse_naked', use_pregnancy=True)
                hover HoverImage(M_consuela.get_button_path('beachhouse_naked', use_pregnancy=True))
            elif M_consuela.pregnancy.stage > 1:
                pos 488, 366
                idle M_consuela.get_button_path('beachhouse', use_baby=True)
                hover HoverImage(M_consuela.get_button_path('beachhouse', use_baby=True))
            elif M_consuela.is_state(S_con04_done) and M_consuela.outfit.is_naked:
                idle game.timer.image("character_consuela_beachhouse_naked{}")
                hover HoverImage(game.timer.image("character_consuela_beachhouse_naked{}"))
            elif M_consuela.is_state(S_con04_done):
                idle game.timer.image("character_consuela_beachhouse{}")
                hover HoverImage(game.timer.image("character_consuela_beachhouse{}"))
            else:
                idle game.timer.image("character_consuela_beachhouse_panties{}")
                hover HoverImage(game.timer.image("character_consuela_beachhouse_panties{}"))

            action TalkTo(M_consuela)

    imagebutton:
        focus_mask True
        align 0.5,0.95
        idle "boxes/auto_option_generic_01.png"
        hover HoverImage("boxes/auto_option_generic_01.png")
        action ExitLocation()

    use mods_screens_hook("beach_house_entrance")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
