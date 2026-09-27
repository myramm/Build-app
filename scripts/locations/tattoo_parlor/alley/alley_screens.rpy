screen tattoo_parlor_alleyway():
    add L_tattooparlor_alley.background

    imagebutton:
        focus_mask True
        align 0.5,0.95
        idle "boxes/auto_option_generic_01.png"
        hover HoverImage("boxes/auto_option_generic_01.png")
        action ExitLocation()

    if player.location.is_here(M_tuuku):
        imagebutton:
            focus_mask True
            if M_eve.party_in_progress or player.location.is_here(M_pilly) or game.timer.is_dark():
                pos 118, 361
                idle M_tuuku.get_button_path(3)
                hover HoverImage(M_tuuku.get_button_path(3))
            else:
                pos 116, 354
                idle M_tuuku.get_button_path(4)
                hover HoverImage(M_tuuku.get_button_path(4))
            action TalkTo(M_tuuku)

    use mods_screens_hook("tattoo_parlor_alleyway")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
