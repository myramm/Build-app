screen tattoo_parlor_apartment():
    add L_tattooparlor_apartment.background

    imagebutton:
        focus_mask True
        pos 408, 315
        idle game.timer.image("objects/object_door_148{}.png")
        hover HoverImage(game.timer.image("objects/object_door_148{}.png"))
        action MoveTo(L_tattooparlor_bedroom)

    imagebutton:
        focus_mask True
        pos 854, 329
        idle game.timer.image("objects/object_door_147{}.png")
        hover HoverImage(game.timer.image("objects/object_door_147{}.png"))
        action MoveTo(L_tattooparlor_fire_escape)

    if player.location.is_here(M_grace) and not M_eve.pregnancy.character_bedridden:
        imagebutton:
            focus_mask True
            if game.timer.is_evening() and M_eve.finished_state(S_eve_make_up_dress_table) and not M_grace.pregnancy and not M_odette.pregnancy and game.timer.is_weekend():
                pos 131, 441
                if M_odette.bike_1st_time or not M_eve.is_state(S_eve_end):
                    idle M_grace.get_button_path(5)
                    hover HoverImage(M_grace.get_button_path(5))
                else:
                    idle M_grace.get_button_path(6)
                    hover HoverImage(M_grace.get_button_path(6))
            elif M_grace.pregnancy:
                pos 186, 330
                idle M_grace.get_button_path(8, use_baby=True)
                hover HoverImage(M_grace.get_button_path(8, use_baby=True))
            elif M_eve.finished_state(S_eve_make_up_dress_table):
                pos 149, 480
                idle M_grace.get_button_path(11)
                hover HoverImage(M_grace.get_button_path(11))
            else:
                pos 149, 480
                idle M_grace.get_button_path(2)
                hover HoverImage(M_grace.get_button_path(2))
            action TalkTo(M_grace)

    use mods_screens_hook("tattoo_parlor_apartment")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
