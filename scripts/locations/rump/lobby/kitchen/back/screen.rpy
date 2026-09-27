screen mayor_rumps_backyard():
    add L_rump_back.background

    imagebutton:
        focus_mask True
        pos 428, 323
        idle game.timer.image('objects/object_door_160{}.png')
        hover HoverImage(game.timer.image('objects/object_door_160{}.png'))
        action MoveTo(L_rump_kitchen)

    if L_rump_back.is_here(M_rump) and game.timer.is_evening():
        imagebutton:
            focus_mask True
            pos 836, 389
            idle M_rump.get_button_path('jacuzzi', use_day_timer=True)
            hover HoverImage(M_rump.get_button_path('jacuzzi', use_day_timer=True))
            action TalkTo(M_rump)

    if L_rump_back.is_here(M_thotbot) and not M_melonia.pregnancy.character_bedridden:
        imagebutton:
            focus_mask True
            pos 582, 301
            idle M_thotbot.get_button_path('rump_backyard' + M_melonia.pregnancy.to_full_string)
            hover HoverImage(M_thotbot.get_button_path('rump_backyard' + M_melonia.pregnancy.to_full_string))
            action TalkTo(M_thotbot)

    if L_rump_back.is_here(M_melonia):
        imagebutton:
            focus_mask True
            if M_melonia.is_state(S_mel01_init):
                pos 645, 301
                at flip
                idle M_melonia.get_button_path('backyard')
                hover HoverImage(M_melonia.get_button_path('backyard'))
            elif game.timer.is_afternoon() and not 1 <= M_melonia.pregnancy.stage <= 4:
                pos 866, 371
                if M_anon.finished_state(S_ano20_done):
                    idle M_melonia.get_button_path('tub_topless')
                    hover HoverImage(M_melonia.get_button_path('tub_topless'))
                else:
                    idle M_melonia.get_button_path('tub')
                    hover HoverImage(M_melonia.get_button_path('tub'))
            else:
                pos 583, 303
                idle M_melonia.get_button_path('backyard', use=('bump', 'belly'))
                hover HoverImage(M_melonia.get_button_path('backyard', use=('bump', 'belly')))
            action TalkTo(M_melonia)

    if L_rump_back.is_here(M_consuela) and L_rump_back.is_here(M_ricky):
        imagebutton:
            focus_mask True
            pos 132, 366
            idle game.timer.image('characters/consuela/buttons/character_consuela_rump_backyard{}.png')
            hover HoverImage(game.timer.image('characters/consuela/buttons/character_consuela_rump_backyard{}.png'))
            action TalkTo(M_consuela)
    elif L_rump_back.is_here(M_ricky):
        imagebutton:
            focus_mask True
            if M_melonia.is_state(S_mel01_find, S_mel01_help):
                pos 911, 308
                idle game.timer.image('characters/ricky/buttons/character_ricky_yard{}_tub.png')
                hover HoverImage(game.timer.image('characters/ricky/buttons/character_ricky_yard{}_tub.png'))
            else:
                if game.timer.is_evening():
                    pos 132, 366
                else:
                    pos 118, 357
                idle game.timer.image('characters/ricky/buttons/character_ricky_yard{}.png')
                hover HoverImage(game.timer.image('characters/ricky/buttons/character_ricky_yard{}.png'))
            action TalkTo(M_ricky)

    if M_melonia.between_states(S_mel01_init, S_mel01_find) and game.timer.is_day() or M_melonia.finished_state(S_mel01_done) and game.timer.is_morning():
        imagebutton:
            focus_mask True
            pos 811, 565
            idle game.timer.image('objects/object_net{}.png')
            hover HoverImage(game.timer.image('objects/object_net{}.png'))
            action HideAll(), Jump('rump_back_net')
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
