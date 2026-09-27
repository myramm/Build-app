label mailbox_dialogue:
    $ player.location.call_screen(False)

label mailbox_item:
    scene expression player.location.background_blur

    if game.mail["player"] == "m_orcette_package":
        call expression game.dialog_select("mailbox_orcette")
        $ player.get_item("orcette")
        $ M_erik.trigger(T_erik_orc_collect)

    elif game.mail["player"] == "m_pizza_pamphlet":
        call expression game.dialog_select("mailbox_pizza_pamphlet")

    elif game.mail["player"] == "m_newspaper":
        call expression game.dialog_select("mailbox_newspaper")

    $ player.location.call_screen(False)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
