screen tattoo_parlor_garage():
    add L_tattooparlor_garage.background

    if not player.has_picked_up_item("odette_panties"):
        imagebutton:
            focus_mask True
            pos 579, 363
            idle game.timer.image("objects/object_panties_08.png")
            hover HoverImage(game.timer.image("objects/object_panties_08.png"))
            action HideAll(), Jump("tattoo_parlor_garage_pantie_collection")

    imagebutton:
        focus_mask True
        pos 78, 125
        idle game.timer.image("objects/object_ladder_02{}.png")
        hover HoverImage(game.timer.image("objects/object_ladder_02{}.png"))
        action MoveTo(L_tattooparlor_fire_escape)

    imagebutton:
        focus_mask True
        align 0.5,0.95
        idle "boxes/auto_option_generic_01.png"
        hover HoverImage("boxes/auto_option_generic_01.png")
        action ExitLocation()

    if player.location.is_here(M_odette):
        imagebutton:
            focus_mask True
            if M_eve.odette_depressed and not M_odette.pregnancy:
                pos 462, 430
                idle M_odette.get_button_path(4)
                hover HoverImage(M_odette.get_button_path(4))
            elif (game.timer.is_evening() and (M_odette.pregnancy or M_grace.pregnancy)) or M_eve.finished_state(S_eve_make_up_dress_table):
                pos 402, 425
                idle M_odette.get_button_path(5, use_baby=True)
                hover HoverImage(M_odette.get_button_path(5, use_baby=True))
            else:
                pos 289, 502
                idle M_odette.get_button_path(2)
                if M_odette.can_talk:
                    hover HoverImage(M_odette.get_button_path(2))
            action TalkTo(M_odette)

    if player.location.is_here(M_grace) and M_eve.party_in_progress:
        imagebutton:
            focus_mask True
            pos 412, 289
            idle M_grace.get_button_path(4)
            hover HoverImage(M_grace.get_button_path(4))
            action TalkTo(M_grace)

    use mods_screens_hook("tattoo_parlor_garage")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
