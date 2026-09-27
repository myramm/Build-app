screen bank_lobby():
    add L_bank_lobby.background

    imagebutton:
        focus_mask True
        pos 731, 468
        idle 'objects/object_door_190.png'
        hover HoverImage('objects/object_door_190.png')
        action MoveTo(L_bank_hallway)

    if L_bank_lobby.is_here(M_tony):
        imagebutton:
            focus_mask True
            pos 195, 511
            idle M_tony.get_button_path('bank_guard')
            hover HoverImage(M_tony.get_button_path('bank_guard'))
            action TalkTo(M_tony)
    else:
        if game.timer.is_dow(1) and game.timer.is_morning():
            add 'character_bankguard_sleeping_borderless':
                pos 195, 554
        imagebutton:
            focus_mask True
            pos 64, 454
            idle 'objects/object_atm_01.png'
            hover HoverImage('objects/object_atm_01.png')
            action HideAll(), Jump('bank_lobby_atm')

    if M_liu.where not in L_bank.get_all_children_inclusive():
        add 'object_bank_teller':
            pos 910, 469

    if L_bank_lobby.is_here(M_liu):
        imagebutton:
            focus_mask True
            if M_anon.is_state(S_ano14_init) and M_liu.finished_state(S_liu01_init):
                pos 408, 440
                idle 'characters/liu/buttons/character_liu_02.png'
                hover HoverImage('characters/liu/buttons/character_liu_02.png')
            elif M_anon.is_state(S_ano14_sobs):
                pos 499, 440
                idle 'characters/liu/buttons/character_liu_03.png'
                hover HoverImage('characters/liu/buttons/character_liu_03.png')
            elif M_anon.is_state(S_ano26_talk):
                pos 900, 467
                idle 'characters/liu/buttons/character_liu_04.png'
                hover HoverImage('characters/liu/buttons/character_liu_04.png')
            else:
                pos 904, 465
                idle M_liu.get_button_path('bank', use_pregnancy=True)
                hover HoverImage(M_liu.get_button_path('bank', use_pregnancy=True))
            action TalkTo(M_liu)

    if L_bank_lobby.is_here(M_tina):
        imagebutton:
            focus_mask True
            pos 239, 397
            at flip
            idle M_tina.get_button_path('bank', use=('bump', 'belly'))
            hover HoverImage(M_tina.get_button_path('bank', use=('bump', 'belly')))
            action TalkTo(M_tina)

    imagebutton:
        focus_mask True
        align .5, .95
        idle 'boxes/auto_option_generic_01.png'
        hover HoverImage('boxes/auto_option_generic_01.png')
        action MoveTo(L_bank)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
