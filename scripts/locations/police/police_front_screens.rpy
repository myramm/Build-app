screen police_parking_lot():
    add L_police_front.background

    imagebutton:
        focus_mask True
        alt "Police Lobby Door"
        pos 523, 421
        idle game.timer.image("objects/object_door_154{}.png")
        hover HoverImage(game.timer.image("objects/object_door_154{}.png"))
        action MoveTo(L_police_lobby)

    if L_police_front.is_here(M_eve):
        imagebutton:
            focus_mask True
            alt "Talk to Eve and Grace"
            pos 369, 422
            idle M_eve.get_button_path(7)
            hover HoverImage(M_eve.get_button_path(7))
            action TalkTo(M_eve)

    use mods_screens_hook("police_parking_lot")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
