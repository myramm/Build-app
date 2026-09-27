screen eriks_house_entrance():
    tag eriks_house

    add game.timer.image("backgrounds/location_erik_house_inside_day{}.jpg")

    imagebutton:
        focus_mask True
        pos (401,40)
        idle game.timer.image("objects/object_door_30{}.png")
        hover HoverImage(game.timer.image("objects/object_door_30{}.png"))
        action MoveTo(L_erikhouse_mrsjroom)

    imagebutton:
        focus_mask True
        pos (340,0)
        idle game.timer.image("objects/object_door_68{}.png")
        hover HoverImage(game.timer.image("objects/object_door_68{}.png"))
        action MoveTo(L_erikhouse_erikroom)

    imagebutton:
        focus_mask True
        pos (576,325)
        idle game.timer.image("objects/object_door_31{}.png")
        hover HoverImage(game.timer.image("objects/object_door_31{}.png"))
        action MoveTo(L_erikhouse_basement)

    imagebutton:
        focus_mask True
        align (0.5,0.97)
        idle "boxes/auto_option_08.png"
        hover HoverImage("boxes/auto_option_08.png")
        action MoveTo(L_erikhouse)

    if player.location.is_here(M_mrsj):
        imagebutton:
            focus_mask True
            pos (700,300)
            idle "objects/character_mrsj_01.png"
            hover HoverImage("objects/character_mrsj_01.png")
            action Hide("eriks_house_entrance"), Jump("mrsj_button_dialogue")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
