screen eriks_basement_backroom():
    add L_erikhouse_backroom.background

    imagebutton:
        focus_mask True
        pos (733,231)
        idle "objects/object_door_82.png"
        hover HoverImage("objects/object_door_82.png")
        action MoveTo(L_erikhouse_basement)

    if M_mrsj.get('poker_after_party'):
        imagebutton:
            focus_mask True
            pos (0,315)
            idle "images/objects/character_mrsj_02.png"
            hover HoverImage("images/objects/character_mrsj_02.png")
            action Hide("eriks_basement_backroom"), Jump("mrsj_afterpoker_fun")

    else:
        imagebutton:
            focus_mask True
            pos (0,385)
            idle "objects/object_couch_01.png"
            hover HoverImage("objects/object_couch_01.png")
            action If(M_anon.is_state(S_ano17_erik, S_ano17_porn),
                      MoveTo(L_erikhouse), 
                      ShowPopup('alpha'))

    imagebutton:
        focus_mask True
        pos (888,539)
        idle "objects/object_aquarium_01.png"
        hover HoverImage("objects/object_aquarium_01.png")
        action MoveTo(L_erikhouse_aquarium)

    if L_erikhouse_backroom.is_here(M_iwanka):
        imagebutton:
            focus_mask True
            pos 848, 234
            idle "characters/iwanka/buttons/character_iwanka_basement.png"
            hover HoverImage("characters/iwanka/buttons/character_iwanka_basement.png")
            action TalkTo(M_iwanka)

    if L_erikhouse_backroom.is_here(M_erik):
        imagebutton:
            focus_mask True
            pos 702, 489
            idle "characters/erik/buttons/character_erik_basement_back_fishtank.png"
            hover HoverImage("characters/erik/buttons/character_erik_basement_back_fishtank.png")
            action TalkTo(M_erik)

    use mods_screens_hook("eriks_basement_backroom")

screen eriks_aquarium():
    add player.location.background

    if not player.has_picked_up_item("eriks_cards"):
        imagebutton:
            focus_mask True
            pos (350,450)
            idle "objects/object_box_02.png"
            hover HoverImage("objects/object_box_02.png")
            action Hide("eriks_aquarium"), Jump("eriks_aquarium_cards")

    imagebutton:
        focus_mask True
        align (0.5,0.97)
        idle "boxes/auto_option_generic_01.png"
        hover HoverImage("boxes/auto_option_generic_01.png")
        action MoveTo(L_erikhouse_backroom)

    use mods_screens_hook('eriks_aquarium')
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
