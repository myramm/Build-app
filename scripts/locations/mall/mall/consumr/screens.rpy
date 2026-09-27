screen consumr():
    add player.location.background

    imagebutton:
        focus_mask True
        pos (174,281)
        idle "objects/object_shop_01.png"
        hover HoverImage("objects/object_shop_01.png")
        action ShowPopup('shop', 'parts')

    imagebutton:
        focus_mask True
        pos (454,584)
        idle "objects/object_shop_03.png"
        hover HoverImage("objects/object_shop_03.png")
        action ShowPopup('shop', 'swimsuit')

    imagebutton:
        focus_mask True
        pos (88,261)
        idle "objects/object_shop_02.png"
        hover HoverImage("objects/object_shop_02.png")
        action ShowPopup('shop', 'supersaga_webcam')

    imagebutton:
        focus_mask True
        pos (820,524)
        idle "objects/object_shop_05.png"
        hover HoverImage("objects/object_shop_05.png")
        action ShowPopup('shop', 'bike',
                         buy_action=Function(player.upgrade_transport, 1))

    imagebutton:
        focus_mask True
        pos (60,606)
        idle "objects/object_shop_06.png"
        hover HoverImage("objects/object_shop_06.png")
        action ShowPopup('shop', 'milkjug',
                         buy_action=Function(milk_jug_callback),
                         own_action=Function(milk_jug_callback, True))

    imagebutton:
        focus_mask True
        pos (170,620)
        idle "objects/object_shop_07.png"
        hover HoverImage("objects/object_shop_07.png")
        action ShowPopup('shop', 'exterminator')

    imagebutton:
        focus_mask True
        pos (230,618)
        idle "objects/object_shop_08.png"
        hover HoverImage("objects/object_shop_08.png")
        action ShowPopup('shop', 'eradicator')

    imagebutton:
        focus_mask True
        pos (290,616)
        idle "objects/object_shop_09.png"
        hover HoverImage("objects/object_shop_09.png")
        action ShowPopup('shop', 'annihilator',
                         buy_action=Function(bug_spray_callback),
                         own_action=Function(bug_spray_callback, True))

    imagebutton:
        focus_mask True
        pos (350,608)
        idle "objects/object_shop_10.png"
        hover HoverImage("objects/object_shop_10.png")
        action ShowPopup('shop', 'gas_can')

    imagebutton:
        focus_mask True
        pos (536,515)
        idle "objects/object_shop_11.png"
        hover HoverImage("objects/object_shop_11.png")
        action ShowPopup('shop', 'wrench')

    imagebutton:
        focus_mask True
        pos (380,388)
        idle "objects/object_shop_12.png"
        hover HoverImage("objects/object_shop_12.png")
        action ShowPopup('shop', 'cat_food')

    imagebutton:
        focus_mask True
        pos (326,381)
        idle "objects/object_shop_chickenstock01.png"
        hover HoverImage("objects/object_shop_chickenstock01.png")
        action If(M_okita.is_set("talked with veronica"),
                  ShowPopup('shop', 'chicken_stock'),
                  (HideAll(), Jump("consumr_chicken_stock_dialogue")))

    imagebutton:
        focus_mask True
        pos 379, 560
        idle "objects/object_shop_13.png"
        hover HoverImage("objects/object_shop_13.png")
        action ShowPopup('shop', 'candle',
                         buy_action=Function(candle_callback),
                         own_action=Function(candle_callback, True))

    imagebutton:
        focus_mask True
        pos (700,400)
        idle "objects/character_vero_01.png"
        hover HoverImage("objects/character_vero_01.png")
        action Hide("consumr"), Jump("veronica_button_dialogue")

    imagebutton:
        focus_mask True
        pos (350,700)
        idle "boxes/auto_option_03.png"
        hover HoverImage("boxes/auto_option_03.png")
        action MoveTo(L_mall)

    use mods_screens_hook("consumr")


label consumr_chicken_stock_dialogue:
    scene expression player.location.background_blur
    show player 4
    with dissolve
    if M_okita.is_state(S_okita_get_ingredients):
        player_name "Hmm, {b}Miss Okita said vegetable stock{/b}, but they only have chicken..."

        player_name "Maybe the clerk can help me?"

    else:
        player_name "I don't see why I would need chicken stock right now..."

    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
