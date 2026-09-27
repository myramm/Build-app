screen mayor_rumps_bedroom():
    add L_rump_master.background

    imagebutton:
        focus_mask True
        pos 51, 244
        idle game.timer.image('objects/object_door_165{}.png')
        hover HoverImage(game.timer.image('objects/object_door_165{}.png'))
        action MoveTo(L_rump_lobby)

    if M_anon.is_state(S_ano18_hide):
        imagebutton:
            focus_mask True
            pos 413, 377
            idle game.timer.image('objects/object_bed_13{}.png')
            hover HoverImage(game.timer.image('objects/object_bed_13{}.png'))
            action HideAll(), Jump('rump_bedroom_bed')

    imagebutton:
        focus_mask True
        pos 260, 331
        idle game.timer.image('objects/object_painting_04{}.png')
        hover HoverImage(game.timer.image('objects/object_painting_04{}.png'))
        action HideAll(), Jump('rump_bedroom_painting')

    if L_rump_master.is_here(M_melonia):
        imagebutton:
            focus_mask True
            if 2 <= M_melonia.pregnancy.stage <= 4:
                pos 800, 322
                idle M_melonia.get_button_path('bedroom', use=('bump', 'belly'), use_day_timer=True)
                hover HoverImage(M_melonia.get_button_path('bedroom', use=('bump', 'belly'), use_day_timer=True))
            elif M_melonia.outfit.is_naked:
                pos 641, 333
                idle M_melonia.get_button_path('bedroom_naked')
                hover HoverImage(M_melonia.get_button_path('bedroom_naked'))
            elif game.timer.is_evening():
                pos 673, 337
                idle M_melonia.get_button_path('bedroom', use_day_timer=True)
                hover HoverImage(M_melonia.get_button_path('bedroom', use_day_timer=True))
            else:
                pos 769, 310
                idle M_melonia.get_button_path('bedroom', use=('bump', 'belly'), use_day_timer=True)
                hover HoverImage(M_melonia.get_button_path('bedroom', use=('bump', 'belly'), use_day_timer=True))
            action TalkTo(M_melonia)

    if L_rump_master.is_here(M_thotbot) and not M_melonia.pregnancy.character_bedridden:
        imagebutton:
            focus_mask True
            pos 530, 316
            idle M_thotbot.get_button_path('rump_bedroom' + M_melonia.pregnancy.to_full_string)
            hover HoverImage(M_thotbot.get_button_path('rump_bedroom' + M_melonia.pregnancy.to_full_string))
            action TalkTo(M_thotbot)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
