screen police_basement():
    add player.location.background

    imagebutton:
        focus_mask True
        pos (841,224)
        idle "images/objects/object_door_51.png"
        hover HoverImage("images/objects/object_door_51.png")
        action MoveTo(L_police_lobby)

    if player.location.is_here(M_yumi):
        imagebutton:
            focus_mask True
            pos (536,418)
            idle "images/objects/character_yumi_01.png"
            hover HoverImage("images/objects/character_yumi_01.png")
            action TalkTo(M_yumi)

    if L_police_basement.is_here(M_rump):
        imagebutton:
            focus_mask True
            pos (318,291)
            idle 'characters/rump/buttons/character_rump_jail.png'
            hover HoverImage('characters/rump/buttons/character_rump_jail.png')
            action TalkTo(M_rump)

    elif M_roxxy.get("trailer foreclosed") and M_roxxy.finished_state(S_roxxy_check_trailer):
        imagebutton:
            focus_mask True
            pos (318,291)
            idle "images/objects/object_cell_04.png"
            hover HoverImage("images/objects/object_cell_04.png")
            action Hide("police_basement"), Jump("crystal_cell_button")

    elif M_larry.finished_state(S_larry_start):
        imagebutton:
            focus_mask True
            pos (318,291)
            idle "images/objects/object_cell_03.png"
            hover HoverImage("images/objects/object_cell_03.png")
            action TalkTo(M_larry)

    else:
        imagebutton:
            focus_mask True
            pos (314,286)
            idle "images/objects/object_cell_01.png"
            hover HoverImage("images/objects/object_cell_01.png")
            action Hide("police_basement"), Jump("police_cell_dialogue")

    imagebutton:
        focus_mask True
        pos (31,237)
        idle "images/objects/object_cell_02.png"
        hover HoverImage("images/objects/object_cell_02.png")
        action Hide("police_basement"), Jump("police_cell_dialogue")

    use mods_screens_hook("police_basement")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
