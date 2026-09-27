screen hospital_lobby():
    use mods_screens_hook("hospital_lobby")

    add game.timer.image("backgrounds/location_hospital_first{}.jpg")

    imagebutton:
        focus_mask True
        pos (0,0)
        if L_hospital_lobby.is_here(M_roz):
            if Game.is_christmas():
                idle "objects/object_desk_09_hat.png"
                hover HoverImage("objects/object_desk_09_hat.png")
            else:
                idle "objects/object_desk_09.png"
                hover HoverImage("objects/object_desk_09.png")
            action TalkTo(M_roz)

        else:
            idle "objects/object_desk_09_empty.png"
            hover HoverImage("objects/object_desk_09_empty.png")
            action If(M_roz.is_state(S_roz_access_phone),
                      (Hide("hospital_lobby"), Show("hospital_front_desk")),
                      MoveTo(L_hospital))

    imagebutton:
        focus_mask True
        pos (466,458)
        idle "objects/object_elevator_01.png"
        hover HoverImage("objects/object_elevator_01.png")
        action MoveTo(L_hospital_elevator)

    imagebutton:
        focus_mask True
        align (0.5,0.97)
        idle "boxes/auto_option_generic_01.png"
        hover HoverImage("boxes/auto_option_generic_01.png")
        action MoveTo(L_hospital)

screen hospital_front_desk():
    add "backgrounds/location_hospital_desk.jpg"

    imagebutton:
        focus_mask True
        pos (338,183)
        idle "objects/object_box_01.png"
        hover HoverImage("objects/object_box_01.png")
        action Hide("hospital_front_desk"), Show("roz_locker")

    imagebutton:
        focus_mask True
        align (0.5,0.97)
        idle "boxes/auto_option_generic_01.png"
        hover HoverImage("boxes/auto_option_generic_01.png")
        action MoveTo(L_hospital_lobby)

screen roz_locker():
    add "backgrounds/location_hospital_box.jpg"

    imagebutton:
        focus_mask True
        pos 202, 430
        idle "objects/object_picture_roz.png"
        hover HoverImage("objects/object_picture_roz.png")
        action HideAll(), Call('hospital_lobby_photo')

    if not player.has_item("hospital_access_card"):
        imagebutton:
            focus_mask True
            pos 580, 50
            idle "objects/object_card_01.png"
            hover HoverImage("objects/object_card_01.png")
            action (Function(player.get_item, "hospital_access_card"),
                    ShowPopup('give', 'hospital_access_card'),
                    Function(roz_card_acquired))

    imagebutton:
        focus_mask True
        align 0.5, 0.97
        idle "boxes/auto_option_generic_01.png"
        hover HoverImage("boxes/auto_option_generic_01.png")
        action Hide("roz_locker"), If(L_hospital_lobby.is_here(M_roz),
                                    Jump("hospital_desk_caught"),
                                    Show("hospital_front_desk"))
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
