screen cupid():
    add L_cupid.background

    imagebutton:
        focus_mask True
        pos (685,232)
        idle "objects/object_door_104.png"
        hover HoverImage("objects/object_door_104.png")
        action Hide("cupid"), MoveTo(L_cupid_dressroom)
    if L_cupid.is_here(M_kassy):
        imagebutton:
            focus_mask True
            pos (160,328)
            idle "objects/character_kass_01.png"
            hover HoverImage("objects/character_kass_01.png")
            action TalkTo(M_kassy)

    if player.location.is_here(M_debbie):
        imagebutton:
            focus_mask True
            pos (580,320)
            idle "objects/character_debbie_08.png"
            hover HoverImage("objects/character_debbie_08.png")
            action Hide("cupid"), Jump("debbie_cupid_outing")

    imagebutton:
        focus_mask True
        pos (463,280)
        idle "objects/object_jewelery_01.png"
        hover HoverImage("objects/object_jewelery_01.png")
        action If(
                    M_debbie.is_state(S_debbie_show_necklace, S_debbie_dressing_room, S_debbie_choose_gift),
                    [Hide("cupid"), Jump("cupid_jewelery_display")],
                    Show("cupid_ui", interface="Jewelery")
                 )

    imagebutton:
        focus_mask True
        align (0.5,0.97)
        idle "boxes/auto_option_generic_01.png"
        hover HoverImage("boxes/auto_option_generic_01.png")
        action Hide("cupid"), MoveTo(L_mall_floor2)

    imagebutton:
        focus_mask True
        pos (802,415)
        idle "objects/object_cupid_stand_01.png"
        hover HoverImage("objects/object_cupid_stand_01.png")
        action Show("cupid_ui", interface = "Plushes")

    imagebutton:
        focus_mask True
        pos (0,302)
        idle "objects/object_cupid_stand_02.png"
        hover HoverImage("objects/object_cupid_stand_02.png")
        action Show("cupid_ui", interface = "Flowers")

    use mods_screens_hook("cupid")

screen cupid_item_info(item):
    text "{color=#8995AD}[item.category]:{/color}\n\n{color=#5E6C8F}[item.name]{/color}" pos 130, 93
    imagebutton:
        idle "buttons/shop_button_" + str(item.price) + ".png"
        hover HoverImage("buttons/shop_button_" + str(item.price) + ".png")
        action BuyItem(item.item, buy_action=item.callback and Function(item.callback))
        pos 685, 93

screen cupid_ui(interface):
    imagebutton:
        idle "ground.png"
        action [Hide("cupid_item_info"), Hide("cupid_ui")]

    imagebutton idle "buttons/comic_ui_01.png" action NullAction() focus_mask True at truecenter

    $ items = []

    for item in cupidstore.items:
        if item.category == interface and not item.purchased:
            $ items.append(item)

    $ a = 0
    $ b = 0
    $ c = 0
    $ c2 = 0
    $ c3 = 0
    for item in items:
        $ c2 = math.trunc(c / 6)
        if c3 == 6:
            $ c3 = 0
        $ a = 123
        $ b = 163 + (c2 * 133)
        $ a += c3 * 130
        imagebutton:
            idle item.idle
            hover item.hover
            xpos a
            ypos b
            action Show("cupid_item_info", item = item)
        $ c += 1
        $ c3 += 1

screen cupid_dressingroom():
    add L_cupid_dressroom.background

    imagebutton:
        focus_mask True
        align (0.5,0.97)
        idle "boxes/auto_option_generic_01.png"
        hover HoverImage("boxes/auto_option_generic_01.png")
        action Hide("cupid_dressingroom"), Jump("cupid_dialogue")

    use mods_screens_hook("cupid_dressingroom")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
