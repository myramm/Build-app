screen entrance():
    add L_home_entrance.background

    imagebutton:
        focus_mask True
        if M_debbie.is_state(S_debbie_diane_visit) and game.timer.is_evening():
            pos 697, 234
            idle "objects/object_door_35_evening02.png"
            hover HoverImage("objects/object_door_35_evening02.png")
        elif M_diane.is_state(S_diane_debbie_evening_visit) and game.timer.is_evening():
            pos 697, 234
            idle "objects/object_door_35_evening03.png"
            hover HoverImage("objects/object_door_35_evening03.png")
        else:
            pos 698, 235
            idle game.timer.image("objects/object_door_35{}.png")
            hover HoverImage(game.timer.image("objects/object_door_35{}.png"))
        action MoveTo(L_home_kitchen)

    imagebutton:
        focus_mask True
        pos 140, 166
        idle game.timer.image("objects/object_stairs_02{}.png")
        hover HoverImage(game.timer.image("objects/object_stairs_02{}.png"))
        action MoveTo(L_home_hallway)

    imagebutton:
        focus_mask True
        pos (0,243)
        if not game.timer.is_dark():
            idle "objects/object_door_39.png"
            hover HoverImage("objects/object_door_39.png")
        else:
            idle "objects/object_door_39_night.png"
            hover HoverImage("objects/object_door_39_night.png")
        action MoveTo(L_home_livingroom)

    if player.location.is_here(M_debbie) and M_debbie.is_set("chores"):
        imagebutton:
            focus_mask True
            pos (550,350)
            idle "objects/character_debbie_04.png"
            hover HoverImage("objects/character_debbie_04.png")
            action Hide("entrance"), Jump("vacuum_dialogue")

    imagebutton:
        focus_mask True
        pos (350,700)
        idle "boxes/auto_option_08.png"
        hover HoverImage("boxes/auto_option_08.png")
        action MoveTo(L_home)

    if not player.has_picked_up_item("attic_key"):
        imagebutton:
            focus_mask True
            pos (982,356)
            idle game.timer.image("objects/object_key_01{}.png")
            hover HoverImage(game.timer.image("objects/object_key_01{}.png"))
            action Function(player.get_item, "attic_key"), Hide("entrance"), Jump("attic_key")

    use mods_screens_hook("entrance")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
