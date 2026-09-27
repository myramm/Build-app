screen attic():
    add player.location.background

    imagebutton:
        focus_mask True
        pos (214,640)
        idle game.timer.image("objects/object_door_41{}.png")
        hover HoverImage(game.timer.image("objects/object_door_41{}.png"))
        action MoveTo(L_home_hallway)

    if not player.has_picked_up_item("fishing_rod"):
        imagebutton:
            focus_mask True
            pos (220,365)
            idle game.timer.image("objects/object_rod_01{}.png")
            hover HoverImage(game.timer.image("objects/object_rod_01{}.png"))
            action Function(player.get_item, "fishing_rod"), Hide("attic"), Jump("fishing_rod")

    if not player.has_picked_up_item("ring"):
        imagebutton:
            focus_mask True
            pos (262,198)
            idle game.timer.image("objects/object_ring_01{}.png")
            hover HoverImage(game.timer.image("objects/object_ring_01{}.png"))
            action Function(player.get_item, "ring"), Hide("attic"), Jump("ring")

    imagebutton:
        focus_mask True
        pos (287,500)
        idle game.timer.image("objects/object_safe_01{}.png")
        hover HoverImage(game.timer.image("objects/object_safe_01{}.png"))
        action ShowPopup('alpha')

    imagebutton:
        focus_mask True
        pos (450,390)
        idle game.timer.image("objects/object_dress_01{}.png")
        hover HoverImage(game.timer.image("objects/object_dress_01{}.png"))
        action ShowPopup('alpha')

    imagebutton:
        focus_mask True
        pos 807, 398
        idle game.timer.image('objects/object_globe_01{}.png')
        hover HoverImage(game.timer.image('objects/object_globe_01{}.png'))
        action HideAll(), Jump("home_attic_globe")

    if M_anon.finished_state(S_ano13_tony):
        imagebutton:
            focus_mask True
            pos 674, 528
            idle game.timer.image('objects/object_box_04{}.png')
            hover HoverImage(game.timer.image('objects/object_box_04{}.png'))
            action HideAll(), Jump('home_attic_evidence')

    imagebutton:
        focus_mask True
        pos (128, 638)
        idle game.timer.image("objects/object_picture_01{}.png")
        hover HoverImage(game.timer.image("objects/object_picture_01{}.png"))
        action ShowPopup('alpha')

    imagebutton:
        focus_mask True
        pos 888, 289
        idle game.timer.image('objects/object_painting_01{}.png')
        hover HoverImage(game.timer.image('objects/object_painting_01{}.png'))
        action HideAll(), Jump('home_attic_painting')

    imagebutton:
        focus_mask True
        pos (178,548)
        idle game.timer.image("objects/object_discs_01{}.png")
        hover HoverImage(game.timer.image("objects/object_discs_01{}.png"))
        action ShowPopup('alpha')

    imagebutton:
        focus_mask True
        pos (739, 618)
        idle game.timer.image("objects/object_carpet_01{}.png")
        hover HoverImage(game.timer.image("objects/object_carpet_01{}.png"))
        action Hide("attic"), Jump("peep_hole_dialogue")

    if not player.has_picked_up_item("cheerleader_outfit"):
        imagebutton:
            focus_mask True
            pos (345,375)
            idle game.timer.image("objects/object_outfit_01{}.png")
            hover HoverImage(game.timer.image("objects/object_outfit_01{}.png"))
            action Hide("attic"), Jump("cheerleader_outfit")

    use mods_screens_hook("attic")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
