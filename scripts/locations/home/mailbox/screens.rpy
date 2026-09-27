screen mailbox():
    add player.location.background

    imagebutton:
        idle "ground.png"
        action MoveTo(L_home)

    if game.mail["player"] == "m_orcette_package":
        imagebutton:
            focus_mask True
            pos (300,345)
            idle game.timer.image("mailbox_package{}")
            hover HoverImage(game.timer.image("mailbox_package{}"))
            action HideAll(), Jump("mailbox_item")

    elif game.mail["player"] == "m_bank_statement":
        imagebutton:
            focus_mask True
            pos (243,428)
            idle game.timer.image("objects/object_mailbox_item06{}.png")
            hover HoverImage(game.timer.image("objects/object_mailbox_item06{}.png"))
            action Show("bank_statement")

    elif game.mail["player"] == "m_pizza_pamphlet":
        imagebutton:
            focus_mask True
            pos (240,480)
            idle game.timer.image("objects/object_mailbox_item02{}.png")
            hover HoverImage(game.timer.image("objects/object_mailbox_item02{}.png"))
            action HideAll(), Jump("mailbox_item")

    elif game.mail["player"] == "m_newspaper":
        imagebutton:
            focus_mask True
            pos (250,575)
            idle game.timer.image("objects/object_mailbox_item05{}.png")
            hover HoverImage(game.timer.image("objects/object_mailbox_item05{}.png"))
            action HideAll(), Jump("mailbox_item")

    use mods_screens_hook("mailbox")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
