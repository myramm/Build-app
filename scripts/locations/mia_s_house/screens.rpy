screen mias_house():
    add player.location.background

    imagebutton:
        focus_mask True
        pos (571,442)
        idle game.timer.image("objects/object_door_24{}.png")
        hover HoverImage(game.timer.image("objects/object_door_24{}.png"))
        action MoveTo(L_miahouse_entrance)

    if player.location.is_here(M_mia):
        imagebutton:
            focus_mask True
            pos (270,480)
            idle "objects/character_mia_02.png"
            hover HoverImage("objects/character_mia_02.png")
            action Hide("mias_house"), Jump("mia_dialogue_mias_house_front")

    imagebutton:
        focus_mask True
        if game.mail["mia"]:
            pos (830,480)
            idle game.timer.image("objects/object_mailbox_mia01{}.png")
            hover HoverImage(game.timer.image("objects/object_mailbox_mia01{}.png"))

        else:
            pos (830,500)
            idle game.timer.image("objects/object_mailbox_mia02{}.png")
            hover HoverImage(game.timer.image("objects/object_mailbox_mia02{}.png"))
        action MoveTo(L_miahouse_mailbox)

    use mods_screens_hook("mias_house")

screen mias_mailbox():
    add player.location.background

    imagebutton:
        idle "ground.png"
        action MoveTo(L_miahouse)

    if game.mail["mia"] == "m_pizza_pamphlet":
        imagebutton:
            focus_mask True
            pos (240,480)
            idle game.timer.image("objects/object_mailbox_item02{}.png")
            hover HoverImage(game.timer.image("objects/object_mailbox_item02{}.png"))
            action HideAll(), Jump("mias_mailbox_item")

    elif game.mail["mia"] == "m_newspaper":
        imagebutton:
            focus_mask True
            pos (250,575)
            idle game.timer.image("objects/object_mailbox_item05{}.png")
            hover HoverImage(game.timer.image("objects/object_mailbox_item05{}.png"))
            action HideAll(), Jump("mias_mailbox_item")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
