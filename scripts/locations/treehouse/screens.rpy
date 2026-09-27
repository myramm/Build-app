screen treehouse():
    add L_treehouse.background

    imagebutton:
        focus_mask True
        pos (309,71)
        idle game.timer.image("objects/object_treehouse_01{}.png")
        hover HoverImage(game.timer.image("objects/object_treehouse_01{}.png"))
        action MoveTo(L_treehouse_ladder)

    imagebutton:
        focus_mask True
        if M_anon.is_state(S_ano28_dink) and game.timer.is_day():
            pos 233, 611
            idle game.timer.image("objects/object_boat{}.png")
            hover HoverImage(game.timer.image("objects/object_boat{}.png"))
        else:
            pos 233, 637
            idle game.timer.image("objects/object_boat_birdless{}.png")
            hover HoverImage(game.timer.image("objects/object_boat_birdless{}.png"))
        action HideAll(), Jump('treehouse_dink')

    if not player.has_item("wood_pile") and (M_ross.is_state(S_ross_get_easels) or M_dewitt.is_state([S_dewitt_garage_find_paint, S_dewitt_ask_deb_paint, S_dewitt_ask_diane_paint, S_dewitt_shed_get_paint, S_dewitt_make_replacement_guitar])):
        imagebutton:
            focus_mask True
            pos (145,684)
            idle game.timer.image("objects/object_pile_01{}.png")
            hover HoverImage(game.timer.image("objects/object_pile_01{}.png"))
            action Hide("treehouse"), Jump("treehouse_got_wood_pile")

    if L_treehouse.is_here(M_erik):
        imagebutton:
            focus_mask True
            pos 888, 548
            idle game.timer.image("characters/erik/buttons/character_erik_treehouse_outside.png")
            hover HoverImage(game.timer.image("characters/erik/buttons/character_erik_treehouse_outside.png"))
            action TalkTo(M_erik)

    use mods_screens_hook("treehouse")


screen treehouse_ladder():
    add L_treehouse_ladder.background

    imagebutton:
        focus_mask True
        pos (502,39)
        idle game.timer.image("objects/object_door_83{}.png")
        hover HoverImage(game.timer.image("objects/object_door_83{}.png"))
        action MoveTo(L_treehouse_interior)

    imagebutton:
        focus_mask True
        align (0.5,0.97)
        idle "boxes/auto_option_generic_01.png"
        hover HoverImage("boxes/auto_option_generic_01.png")
        action MoveTo(L_treehouse)

    use mods_screens_hook("treehouse_ladder")


screen treehouse_interior():
    add L_treehouse_interior.background

    if M_anon.finished_state(S_ano16_tree):
        imagebutton:
            focus_mask True
            pos 358, 204
            idle game.timer.image("objects/object_window_02{}.png")
            hover HoverImage(game.timer.image("objects/object_window_02{}.png"))
            action HideAll(), Jump('treehouse_window')

    if L_treehouse_interior.is_here(M_erik):
        imagebutton:
            focus_mask True
            pos 533, 393
            idle game.timer.image("characters/erik/buttons/character_erik_treehouse_inside.png")
            hover HoverImage(game.timer.image("characters/erik/buttons/character_erik_treehouse_inside.png"))
            action TalkTo(M_erik)

    imagebutton:
        focus_mask True
        pos 465, 659
        idle game.timer.image("objects/object_door_84{}.png")
        hover HoverImage(game.timer.image("objects/object_door_84{}.png"))
        action MoveTo(L_treehouse_ladder)

    if M_okita.is_state(S_okita_get_controller, S_okita_get_controller_info) and not player.has_picked_up_item("controller"):
        imagebutton:
            focus_mask True
            pos 275, 541
            idle game.timer.image("objects/object_controller_01{}.png")
            hover HoverImage(game.timer.image("objects/object_controller_01{}.png"))
            action Hide("treehouse_interior"), Jump("treehouse_got_controller")

    imagebutton:
        focus_mask True
        pos 18, 674
        idle game.timer.image("objects/object_box_03{}.png")
        hover HoverImage(game.timer.image("objects/object_box_03{}.png"))
        action Hide("treehouse_interior"), Hide("ui"), Show("treehouse_box")

    use mods_screens_hook("treehouse_interior")


screen treehouse_box():
    add "backgrounds/location_treehouse_box.jpg"

    if not player.has_item("binoculars"):
        imagebutton:
            focus_mask True
            pos 545, 254
            idle "objects/object_binoculars.png"
            hover HoverImage("objects/object_binoculars.png")
            action Hide("treehouse_box"), Jump("treehouse_box_binoculars")

    if not player.has_item("lure01"):
        imagebutton:
            focus_mask True
            pos (450,390)
            idle "objects/object_lure_01.png"
            hover HoverImage("objects/object_lure_01.png")
            action Hide("treehouse_box"), Jump("lure_02")

    imagebutton:
        focus_mask True
        align (0.5,0.97)
        idle "boxes/auto_option_generic_01.png"
        hover HoverImage("boxes/auto_option_generic_01.png")
        action Hide("treehouse_box"), Jump("treehouse_interior_dialogue")


screen ano28_dink_dink():
    layer 'master'
    sensitive renpy.get_mode() == 'screen'

    default open = 'a'

    add 'location_treehouse_cutscene06[open]'

    if open != 'c':
        imagebutton:
            focus_mask True
            sensitive renpy.get_mode() == 'screen'
            if open == 'a':
                pos 84, 239
                idle 'backgrounds/location_treehouse_cutscene06_shut.png'
                hover HoverImage('backgrounds/location_treehouse_cutscene06_shut.png')
                action SetScreenVariable('open', 'b'), With(dissolve), Return(False)
            else:
                pos 333, 442
                idle 'backgrounds/location_treehouse_cutscene06_cash.png'
                hover HoverImage('backgrounds/location_treehouse_cutscene06_cash.png')
                action SetScreenVariable('open', 'c'), With(dissolve), Return(False)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
