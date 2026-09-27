screen tattoo_parlor_roof():
    add L_tattooparlor_roof.background

    if not M_eve.party_in_progress:
        imagebutton:
            focus_mask True
            pos 404, 389
            idle game.timer.image("objects/object_tent_01{}.png")
            hover HoverImage(game.timer.image("objects/object_tent_01{}.png"))
            action MoveTo(L_tattooparlor_tent)

    imagebutton:
        focus_mask True
        pos 713, 454
        idle game.timer.image("objects/object_stairs_12{}.png")
        hover HoverImage(game.timer.image("objects/object_stairs_12{}.png"))
        action MoveTo(L_tattooparlor_fire_escape)

    if L_tattooparlor_roof.is_here(M_eve):
        imagebutton:
            focus_mask True
            if M_eve.is_state(S_eve_voyeurism_follow_roof):
                pos 135, 390
                idle M_eve.get_button_path(8)
                hover HoverImage(M_eve.get_button_path(8))
            else:
                pos 920, 340
                idle M_eve.get_button_path(10, use_day_timer=True)
                hover HoverImage(M_eve.get_button_path(10, use_day_timer=True))
            action TalkTo(M_eve)

    if L_tattooparlor_roof.is_here(M_grace) and not M_eve.pregnancy.character_bedridden:
        imagebutton:
            focus_mask True
            pos 588, 416
            idle M_grace.get_button_path(3)
            hover HoverImage(M_grace.get_button_path(3))
            action TalkTo(M_grace)

    if player.location.is_here(M_jenny) and M_eve.party_in_progress:
        imagebutton:
            focus_mask True
            pos 258, 332
            idle M_jenny.get_button_path(6)
            hover HoverImage(M_jenny.get_button_path(6))
            action TalkTo(M_jenny)

    if player.location.is_here(M_odette) and M_eve.party_in_progress:
        imagebutton:
            focus_mask True
            pos 447, 299
            idle M_odette.get_button_path(3)
            hover HoverImage(M_odette.get_button_path(3))
            action TalkTo(M_odette)

    if player.location.is_here(M_tuuku):
        imagebutton:
            focus_mask True
            pos 77, 378
            idle M_tuuku.get_button_path(1)
            hover HoverImage(M_tuuku.get_button_path(1))
            action TalkTo(M_tuuku)

    use mods_screens_hook("tattoo_parlor_roof")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
