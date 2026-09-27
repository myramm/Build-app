screen beach_house_kitchen():
    add player.location.background

    imagebutton:
        focus_mask True
        pos 956, 90
        idle game.timer.image("objects/object_door_156{}.png")
        hover HoverImage(game.timer.image("objects/object_door_156{}.png"))
        action MoveTo(L_beachhouse_entrance)

    imagebutton:
        focus_mask True
        pos 233, 320
        idle game.timer.image("objects/object_door_157{}.png")
        hover HoverImage(game.timer.image("objects/object_door_157{}.png"))
        action MoveTo(L_beach)

    if L_beachhouse_kitchen.is_here(M_consuela):
        imagebutton:
            focus_mask True
            if M_consuela.is_state(S_con04_done) and M_consuela.outfit.is_naked:
                pos 321, 578
                idle game.timer.image("character_consuela_beachhouse_kitchen_naked{}")
                hover HoverImage(game.timer.image("character_consuela_beachhouse_kitchen_naked{}"))
            elif M_consuela.is_state(S_con04_done):
                pos 321, 578
                idle game.timer.image("character_consuela_beachhouse_kitchen{}")
                hover HoverImage(game.timer.image("character_consuela_beachhouse_kitchen{}"))
            else:
                pos 53, 430
                idle game.timer.image("character_consuela_beachhouse_kitchen_standing{}")
                hover HoverImage(game.timer.image("character_consuela_beachhouse_kitchen_standing{}"))

            action TalkTo(M_consuela)

    use mods_screens_hook("beach_house_kitchen")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
