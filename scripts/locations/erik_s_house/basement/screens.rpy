screen eriks_basement():
    add L_erikhouse_basement.background

    imagebutton:
        focus_mask True
        pos 879, 310
        idle 'objects/object_door_81.png'
        hover HoverImage('objects/object_door_81.png')
        action MoveTo(L_erikhouse_backroom)

    imagebutton:
        focus_mask True
        pos 137, 308
        idle 'objects/object_stairs_01.png'
        hover HoverImage('objects/object_stairs_01.png')
        action MoveTo(L_erikhouse_entrance)

    if L_erikhouse_basement.is_here(M_erik) and M_anon.is_state(S_ano17_talk, S_ano17_porn):
        imagebutton:
            focus_mask True
            pos 37, 439
            idle "characters/erik/buttons/character_erik_basement_booze.png"
            hover HoverImage("characters/erik/buttons/character_erik_basement_booze.png")
            action TalkTo(M_erik)
    else:
        imagebutton:
            focus_mask True
            pos 37, 475
            idle "objects/object_cabinet_01.png"
            hover HoverImage("objects/object_cabinet_01.png")
            action If(player.location.is_here(M_erik),
                      Show("cabinet01_options"), NullAction())

    if player.location.is_here(M_erik, M_mrsj):
        imagebutton:
            focus_mask True
            pos (393,353)
            idle "objects/object_poker_02.png"
            hover HoverImage("objects/object_poker_02.png")
            action Hide("eriks_basement"), Jump("mrsj_poker")

    else:
        imagebutton:
            focus_mask True
            pos (394,505)
            idle "objects/object_poker_01.png"
            hover HoverImage("objects/object_poker_01.png")
            if M_anon.is_state(S_ano17_erik, S_ano17_talk, S_ano17_porn):
                action MoveTo(L_erikhouse)
            else:
                action If(player.location.is_here(M_erik),
                          Show("poker01_options"), NullAction())

    if not M_anon.is_state(S_ano17_erik, S_ano17_talk, S_ano17_porn):

        if M_dewitt.is_state(S_dewitt_clean_graffiti) and not player.has_item("beer"):
            imagebutton:
                focus_mask True
                pos (72,621)
                idle "objects/object_beer_01.png"
                hover HoverImage("objects/object_beer_01.png")
                action Hide("eriks_basement"), Jump("eriks_basement_dewitt_get_beer")

        if M_dewitt.is_state(S_dewitt_replace_guitar) and player.has_item("fake_guitar"):
            imagebutton:
                focus_mask True
                pos (635,338)
                idle "objects/object_guitar_01.png"
                hover HoverImage("objects/object_guitar_01.png")
                action Hide("eriks_basement"), Jump("eriks_basement_dewitt_replace_guitar")

        if player.location.is_here(M_erik) and not player.location.is_here(M_mrsj) and not erik_drunk:
            imagebutton:
                focus_mask True
                pos (855,410)
                idle "objects/character_erik_01.png"
                hover HoverImage("objects/character_erik_01.png")
                action Hide("eriks_basement"), Jump("erik_button_dialogue")

    use mods_screens_hook("eriks_basement")

screen cabinet01_options():
    imagebutton:
        idle "ground.png"
        action Hide("cabinet01_options")

    imagebutton:
        focus_mask True
        pos (350,600)
        idle "boxes/cabinet01_option_01.png"
        hover HoverImage("boxes/cabinet01_option_01.png")
        action Hide("cabinet01_options"), Hide("eriks_basement"), Jump("cabinet")

screen poker01_options():
    imagebutton:
        idle "ground.png"
        action Hide("poker01_options")

    imagebutton:
        focus_mask True
        pos (350,600)
        idle "boxes/poker01_option01.png"
        hover HoverImage("boxes/poker01_option01.png")
        action Hide("poker01_options"), Hide("eriks_basement"), Jump("poker_table")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
