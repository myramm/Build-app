screen trailer_bedroom():
    add player.location.background

    if not player.has_picked_up_item("roxxy_panties"):
        imagebutton:
            focus_mask True
            pos (509,254)
            idle game.timer.image("objects/object_panties_03{}.png")
            hover HoverImage(game.timer.image("objects/object_panties_03{}.png"))
            action Hide("trailer_bedroom"), Jump("trailer_bedroom_roxxy_panties")

    imagebutton:
        focus_mask True
        pos (819,136)
        idle game.timer.image("objects/object_door_88{}.png")
        hover HoverImage(game.timer.image("objects/object_door_88{}.png"))
        action MoveTo(L_trailer_interior)

    if player.location.is_here(M_roxxy):
        imagebutton:
            focus_mask True
            pos (41,404)
            idle "objects/character_roxxy_03.png"
            hover HoverImage("objects/character_roxxy_03.png")
            action TalkTo(M_roxxy)

    use mods_screens_hook("trailer_bedroom")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
