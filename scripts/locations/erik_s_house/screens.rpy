screen eriks_house():
    tag eriks_house

    add game.timer.image("backgrounds/location_erik_house_day{}.jpg")

    if not game.timer.is_dark():
        if getPlayingSound("<loop 7 to 114>audio/ambience_suburb.ogg"):
            $ playSound("<loop 7 to 114>audio/ambience_suburb.ogg", 1.0)
    else:
        if getPlayingSound("<loop 8 to 179>audio/ambience_suburb_night.ogg"):
            $ playSound("<loop 8 to 179>audio/ambience_suburb_night.ogg", 1.0)

    imagebutton:
        focus_mask True
        pos (350,417)
        idle game.timer.image("objects/object_door_18{}.png")
        hover HoverImage(game.timer.image("objects/object_door_18{}.png"))
        action MoveTo(L_erikhouse_entrance)

    imagebutton:
        focus_mask True
        pos (846,410)
        idle game.timer.image("objects/object_door_67{}.png")
        hover HoverImage(game.timer.image("objects/object_door_67{}.png"))
        action MoveTo(L_erikhouse_backyard)

    imagebutton:
        focus_mask True
        if game.mail["erik"]:
            pos (735,480)
            idle game.timer.image("objects/object_mailbox_erik01{}.png")
            hover HoverImage(game.timer.image("objects/object_mailbox_erik01{}.png"))
        else:
            pos (735,500)
            idle game.timer.image("objects/object_mailbox_erik02{}.png")
            hover HoverImage(game.timer.image("objects/object_mailbox_erik02{}.png"))
        action MoveTo(L_erikhouse_mailbox)

screen eriks_mailbox():
    add player.location.background

    imagebutton:
        idle "ground.png"
        action MoveTo(L_erikhouse)

    if game.mail["erik"] == "m_magazine":
        imagebutton:
            focus_mask True
            pos (310,455)
            idle game.timer.image("objects/object_mailbox_item01{}.png")
            hover HoverImage(game.timer.image("objects/object_mailbox_item01{}.png"))
            action HideAll(), Jump("eriks_mailbox_item")

    elif game.mail["erik"] == "m_dad_letter":
        imagebutton:
            focus_mask True
            pos (510,345)
            idle game.timer.image("objects/object_mailbox_item03{}.png")
            hover HoverImage(game.timer.image("objects/object_mailbox_item03{}.png"))
            action HideAll(), Jump("eriks_mailbox_item")

    elif game.mail["erik"] == "m_pizza_pamphlet":
        imagebutton:
            focus_mask True
            pos (240,480)
            idle game.timer.image("objects/object_mailbox_item02{}.png")
            hover HoverImage(game.timer.image("objects/object_mailbox_item02{}.png"))
            action HideAll(), Jump("eriks_mailbox_item")

    elif game.mail["erik"] == "m_newspaper":
        imagebutton:
            focus_mask True
            pos (250,575)
            idle game.timer.image("objects/object_mailbox_item05{}.png")
            hover HoverImage(game.timer.image("objects/object_mailbox_item05{}.png"))
            action HideAll(), Jump("eriks_mailbox_item")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
