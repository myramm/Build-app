screen recovery_room():
    default occupant = machines.get(ward[player.location.var_name], None)

    add L_hospital_recovery1.background

    imagebutton:
        focus_mask True
        pos 29, 244
        idle 'object_poster_01'
        hover HoverImage('object_poster_01')
        action HideAll(), Jump('hospital_recovery_poster')

    if occupant:
        default img = 'character_{}_hospital_{}'.format(occupant,
                                                        occupant.pregnancy.baby_gender)

        if occupant is M_eve:
            add 'character_grace_10':
                pos (584, 395)
                zoom .78

        imagebutton:
            focus_mask True
            align 1., 1.
            idle img
            hover HoverImage(img)
            action TalkTo(occupant)

    imagebutton:
        focus_mask True
        align .5, .95
        idle 'boxes/auto_option_generic_01.png'
        hover HoverImage('boxes/auto_option_generic_01.png')
        action MoveTo(L_hospital_floor3)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
