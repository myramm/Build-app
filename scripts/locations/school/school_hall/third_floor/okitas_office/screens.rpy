screen mrs_okitas_office():
    add game.timer.image("backgrounds/location_school_office4_day{}.jpg")

    if not player.has_picked_up_item("goggles"):
        imagebutton:
            focus_mask True
            pos (126,471)
            idle "objects/object_goggles_01.png"
            hover HoverImage("objects/object_goggles_01.png")
            action Hide("mrs_okitas_office"), Jump("picked_up_goggles")

    if not player.has_picked_up_item("blueprints"):
        imagebutton:
            focus_mask True
            pos (250,577)
            idle "objects/object_blueprints_01.png"
            hover HoverImage("objects/object_blueprints_01.png")
            action Hide("mrs_okitas_office"), Jump("picked_up_blueprints")

    if player.location.is_here(M_okita):
        if M_okita.is_state(S_okita_xray_perving):
            imagebutton:
                focus_mask True
                pos (196,309)
                idle "objects/character_okita_02.png"
                hover HoverImage("objects/character_okita_02.png")
                action Hide("mrs_okitas_office"), Jump("button_okita_xray")

        if M_okita.is_state(S_okita_end):
            imagebutton:
                focus_mask True
                pos (486,415)
                idle "objects/character_okita_03.png"
                hover HoverImage("objects/character_okita_03.png")
                action Hide("mrs_okitas_office"), Jump("okita_pre_hscene_repeatable")

    imagebutton:
        focus_mask True
        pos (862,445)
        idle game.timer.image("objects/object_konterina_01{}.png")
        hover HoverImage(game.timer.image("objects/object_konterina_01{}.png"))
        action Hide("mrs_okitas_office"), Jump("konterina_button_dialogue")

    if not player.has_picked_up_item("labcoat"):
        imagebutton:
            focus_mask True
            pos (816,569)
            idle "objects/object_coat_01.png"
            hover HoverImage("objects/object_coat_01.png")
            action Hide("mrs_okitas_office"), Jump("picked_up_labcoat")

    imagebutton:
        focus_mask True
        align (0.5,0.97)
        idle "boxes/auto_option_generic_02.png"
        hover HoverImage("boxes/auto_option_generic_02.png")
        action MoveTo(L_school_floor3)

    use mods_screens_hook("mrs_okitas_office")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
