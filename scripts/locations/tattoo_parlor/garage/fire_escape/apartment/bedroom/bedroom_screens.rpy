screen tattoo_parlor_bedroom():
    add L_tattooparlor_bedroom.background

    if not player.has_picked_up_item("eve_panties"):
        imagebutton:
            focus_mask True
            pos 556, 187
            idle game.timer.image("objects/object_panties_07.png")
            hover HoverImage(game.timer.image("objects/object_panties_07.png"))
            action HideAll(), Jump("tattoo_parlor_bedroom_pantie_collection")

    imagebutton:
        focus_mask True
        pos 182, 176
        idle game.timer.image("objects/object_door_149{}.png")
        hover HoverImage(game.timer.image("objects/object_door_149{}.png"))
        action MoveTo(L_tattooparlor_apartment)

    imagebutton:
        focus_mask True
        pos 37, 93
        idle game.timer.image("objects/object_door_150{}.png")
        hover HoverImage(game.timer.image("objects/object_door_150{}.png"))
        action MoveTo(L_tattooparlor_bathroom)

    if player.location.is_here(M_eve):
        imagebutton:
            focus_mask True
            action TalkTo(M_eve)
            if game.timer.is_weekend() and game.timer.is_morning():
                pos 357, 397
                idle M_eve.get_button_path(12, use_day_timer=True)
                hover HoverImage(M_eve.get_button_path(12, use_day_timer=True))
            elif M_eve.pregnancy.stage > 1:
                pos 403, 262
                idle M_eve.get_button_path(13, use_day_timer=True, use_baby=True)
                hover HoverImage(M_eve.get_button_path(13, use_day_timer=True, use_baby=True))
            else:
                pos 557, 386
                idle M_eve.get_button_path(11)
                hover HoverImage(M_eve.get_button_path(11))

    use mods_screens_hook("tattoo_parlor_bedroom")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
