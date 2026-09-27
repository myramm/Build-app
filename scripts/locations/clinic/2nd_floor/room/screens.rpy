screen hospital_2nd_floor_room():
    add player.location.background

    imagebutton:
        focus_mask True
        pos (69,274)
        idle "objects/object_door_79.png"
        hover HoverImage("objects/object_door_79.png")
        action MoveTo(L_hospital_room_bathroom)

    if L_hospital_room.is_here(M_micoe):
        imagebutton:
            focus_mask True
            pos (300,390)
            idle "objects/character_micoe.png"
            hover HoverImage("objects/character_micoe.png")
            action Hide("hospital_2nd_floor_room"), Jump("micoe_button_dialogue")

    imagebutton:
        focus_mask True
        align (0.5,0.97)
        idle "boxes/auto_option_generic_01.png"
        hover HoverImage("boxes/auto_option_generic_01.png")
        action MoveTo(L_hospital_floor2)

    use mods_screens_hook("hospital_2nd_floor_room")


screen hospital_2nd_floor_bathroom():
    add player.location.background

    imagebutton:
        focus_mask True
        pos (882,10)
        idle "objects/object_door_139.png"
        hover HoverImage("objects/object_door_139.png")
        action MoveTo(L_hospital_room)

    use mods_screens_hook("hospital_2nd_floor_bathroom")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
