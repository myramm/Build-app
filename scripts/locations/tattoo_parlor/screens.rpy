screen tattoo_parlor():
    add player.location.background

    imagebutton:
        focus_mask True
        action MoveTo(L_tattooparlor_interior)
        if M_eve.is_state(S_eve_clients_tattooshop_crowd, S_eve_clients_take_care_clients) and not game.timer.is_dark():
            pos 123, 388
            idle "objects/object_door_89_crowd.png"
            hover HoverImage("objects/object_door_89_crowd.png")
        else:
            pos 427, 388
            idle game.timer.image("objects/object_door_89{}.png")
            hover HoverImage(game.timer.image("objects/object_door_89{}.png"))

    if M_eve.finished_state(S_eve_visit_tattoo_shop):
        imagebutton:
            focus_mask True
            pos 665, 433
            idle game.timer.image("objects/object_door_143{}.png")
            hover HoverImage(game.timer.image("objects/object_door_143{}.png"))
            action MoveTo(L_tattooparlor_garage)

    imagebutton:
        focus_mask True
        pos 908, 487
        idle game.timer.image("objects/object_door_144{}.png")
        hover HoverImage(game.timer.image("objects/object_door_144{}.png"))
        action MoveTo(L_tattooparlor_alley)

    use mods_screens_hook("tattoo_parlor")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
