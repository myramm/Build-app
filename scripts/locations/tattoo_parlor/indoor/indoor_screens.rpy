screen tattoo_parlor_interior():
    add player.location.background

    imagebutton:
        focus_mask True
        pos (9,280)
        idle game.timer.image("objects/object_door_90{}.png")
        hover HoverImage(game.timer.image("objects/object_door_90{}.png"))
        action Hide("tattoo_parlor_interior"), Jump("tattoo_parlor_dialogue")

    if player.location.is_here(M_grace) and not M_eve.pregnancy.character_bedridden:
        imagebutton:
            focus_mask True
            if M_eve.is_state(S_eve_clients_tattooshop_crowd, S_eve_clients_take_care_clients) and not game.timer.is_dark():
                pos 629, 397
                idle M_grace.get_button_path(7)
                hover HoverImage(M_grace.get_button_path(7))
            else:

                if M_grace.pregnancy.gave_birth:
                    pos 880, 335
                elif M_grace.pregnancy.stage > 2:
                    pos 897, 337
                else:
                    pos 901, 338
                idle M_grace.get_button_path(1, use_baby=True)
                hover HoverImage(M_grace.get_button_path(1, use_baby=True))
            action TalkTo(M_grace)

    if M_ross.is_state(S_ross_get_paint_grace) and not player.has_item("ink"):
        imagebutton:
            focus_mask True
            pos (627,563)
            idle "objects/object_boxes_01.png"
            hover HoverImage("objects/object_boxes_01.png")
            action If(M_ross.get("talked to grace") and not player.has_item("ink"), [Hide("tattoo_parlor_interior"), Jump("tattoo_pick_up_boxes")])

    if player.location.is_here(M_odette):
        imagebutton:
            focus_mask True
            pos 474, 419
            idle M_odette.get_button_path(1, use_baby=True)
            hover HoverImage(M_odette.get_button_path(1, use_baby=True))
            action TalkTo(M_odette)

    use mods_screens_hook("tattoo_parlor_interior")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
