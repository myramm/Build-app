screen church_graveyard():
    add L_church_graveyard.background

    if game.timer.is_fullmoon() and game.timer.is_night():
        add 'location_church_graveyard_night_fullmoon'

    imagebutton:
        focus_mask True
        pos 360, 545
        if game.timer.is_fullmoon() and game.timer.is_night() and L_church_crypt.is_here(M_odette):
            idle game.timer.image('objects/object_crypt{}_glow.png')
            hover HoverImage(game.timer.image('objects/object_crypt{}_glow.png'))
        else:
            idle game.timer.image('objects/object_crypt{}.png')
            hover HoverImage(game.timer.image('objects/object_crypt{}.png'))
        action HideAll(), Jump('church_graveyard_crypt')

    if M_aqua.is_set("tomb search") and not game.timer.is_dark():
        imagebutton:
            focus_mask True
            pos 82, 519
            idle "objects/object_tomb_03.png"
            hover HoverImage("objects/object_tomb_03.png")
            action Hide("church_graveyard"), Jump("right_tombstone")

    imagebutton:
        focus_mask True
        pos 223, 506
        idle game.timer.image('objects/object_tomb_01{}.png')
        hover HoverImage(game.timer.image('objects/object_tomb_01{}.png'))
        action HideAll(), Jump("church_graveyard_grave")

    imagebutton:
        focus_mask True
        if not game.timer.is_dark():
            pos 627, 223
        else:
            pos 626, 223
        if not M_player.is_set("pet cat") and not game.timer.is_dark():
            idle "objects/object_tomb_04.png"
            hover HoverImage("objects/object_tomb_04.png")
            action Hide("church_graveyard"), Jump("stray_cat")
        else:
            idle game.timer.image("objects/object_tomb_02{}.png")
            hover HoverImage(game.timer.image("objects/object_tomb_02{}.png"))
            action ShowPopup('alpha')

    imagebutton:
        focus_mask True
        align .5, .95
        idle 'boxes/auto_option_generic_01.png'
        hover HoverImage('boxes/auto_option_generic_01.png')
        action MoveTo(church_graveyard_exit_location())


screen church_graveyard_crypt():
    layer 'master'
    sensitive renpy.get_mode() == 'screen'

    default open = False

    add game.timer.image('location_church_graveyard_crypt_door{}')

    if game.timer.is_fullmoon() and game.timer.is_night() and L_church_crypt.is_here(M_odette):
        imagebutton:
            focus_mask True
            if open:
                idle 'backgrounds/location_church_graveyard_crypt_door_button_open_night.png'
                hover HoverImage('backgrounds/location_church_graveyard_crypt_door_button_open_night.png')
                action Return(False)
            else:
                idle 'backgrounds/location_church_graveyard_crypt_door_button_night.png'
                hover HoverImage('backgrounds/location_church_graveyard_crypt_door_button_night.png')
                action SetScreenVariable('open', True), With(dissolve), Return(False)

    if renpy.get_mode() == 'screen':
        imagebutton:
            focus_mask True
            align .5, .95
            idle 'boxes/auto_option_generic_01.png'
            hover HoverImage('boxes/auto_option_generic_01.png')
            action Return()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
