screen hill():
    add player.location.background

    if M_anon.is_state(S_ano27_init) and game.timer.is_evening():
        imagebutton:
            focus_mask True
            pos 389, 385
            idle M_jab.get_button_path('hill_limo')
            hover HoverImage(M_jab.get_button_path('hill_limo'))
            action TalkTo(M_jab)

    elif M_mia.is_state(S_mia_find_harold) and game.timer.is_day():
        imagebutton:
            focus_mask True
            pos (389,398)
            idle "objects/character_harold_02.png"
            hover HoverImage("objects/character_harold_02.png")
            action Hide("hill"), Jump("hill_harolds_car")

    imagebutton:
        focus_mask True
        pos (18,497)
        if not game.timer.is_dark():
            idle "objects/object_treehole_01.png"
            hover HoverImage("objects/object_treehole_01.png")
        else:
            idle "objects/object_treehole_01_night.png"
            hover HoverImage("objects/object_treehole_01_night.png")
        action Hide("hill"), Jump("hill_tree")

    if not player.has_picked_up_item("stick") and M_dewitt.is_state(S_dewitt_make_new_flute):
        imagebutton:
            focus_mask True
            pos (100,700)
            idle game.timer.image("objects/object_stick_01{}.png")
            hover HoverImage(game.timer.image("objects/object_stick_01{}.png"))
            action Hide("hill"), Jump("hill_dewitt_stick")

    use mods_screens_hook("hill")


screen hill_tree():
    imagebutton:
        focus_mask True
        align (0.45,0.65)
        if not game.timer.is_dark():
            idle "objects/object_scroll_01.png"
            hover HoverImage("objects/object_scroll_01.png")
        else:
            idle "objects/object_scroll_01_night.png"
            hover HoverImage("objects/object_scroll_01_night.png")
        action Hide("hill_tree"), Jump("hill_tree_get_scroll")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
