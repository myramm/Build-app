screen liu_lounge():
    add L_liu_lounge.background

    imagebutton:
        focus_mask True
        pos 25, 284
        idle game.timer.image('objects/object_door_199{}.png')
        hover HoverImage(game.timer.image('objects/object_door_199{}.png'))
        action MoveTo(L_apt_hall2)

    if M_kim.state is None and M_kim.wallet is None:
        imagebutton:
            focus_mask True
            pos 194, 427
            idle game.timer.image('objects/object_wallet{}.png')
            hover HoverImage(game.timer.image('objects/object_wallet{}.png'))
            action HideAll(), Jump('liu_lounge_wallet')

    imagebutton:
        focus_mask True
        pos 482, 282
        idle game.timer.image('objects/object_door_200{}.png')
        hover HoverImage(game.timer.image('objects/object_door_200{}.png'))
        action MoveTo(L_liu_bedroom)

    if M_anon.is_state(S_ano24_seek, S_ano24_find):
        imagebutton:
            focus_mask True
            pos 201, 532
            idle game.timer.image('objects/object_kim_documents_01{}.png')
            hover HoverImage(game.timer.image('objects/object_kim_documents_01{}.png'))
            action HideAll(), Jump('liu_lounge_bag')

        imagebutton:
            focus_mask True
            pos 857, 554
            idle game.timer.image('objects/object_kim_documents_03{}.png')
            hover HoverImage(game.timer.image('objects/object_kim_documents_03{}.png'))
            action HideAll(), Jump('liu_lounge_folder')

        imagebutton:
            focus_mask True
            pos 559, 588
            idle game.timer.image('objects/object_kim_documents_02{}.png')
            hover HoverImage(game.timer.image('objects/object_kim_documents_02{}.png'))
            action HideAll(), Jump('liu_lounge_case')

    if L_liu_lounge.is_here(M_liu):
        imagebutton:
            focus_mask True
            if M_liu.pregnancy:
                pos 771, 277
                idle M_liu.get_button_path('home_lounge', use=('bump', 'belly', 'baby'))
                hover HoverImage(M_liu.get_button_path('home_lounge', use=('bump', 'belly', 'baby')))
            else:
                pos 795, 414
                idle M_liu.get_button_path('home_tea', use_day_timer=True)
                hover HoverImage(M_liu.get_button_path('home_tea', use_day_timer=True))
            action TalkTo(M_liu)

    if not player.has_picked_up_item('card06'):
        imagebutton:
            focus_mask True
            pos 557, 708
            idle game.timer.image('objects/object_card_06{}.png')
            hover HoverImage(game.timer.image('objects/object_card_06{}.png'))
            action HideAll(), Jump('liu_lounge_card')
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
