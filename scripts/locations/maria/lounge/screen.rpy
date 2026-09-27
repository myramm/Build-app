screen maria_lounge():
    add L_maria_lounge.background

    imagebutton:
        focus_mask True
        pos 889, 284
        idle game.timer.image('objects/object_door_202{}.png')
        hover HoverImage(game.timer.image('objects/object_door_202{}.png'))
        action MoveTo(L_apt_hall3)

    imagebutton:
        focus_mask True
        pos 432, 281
        idle game.timer.image('objects/object_door_203{}.png')
        hover HoverImage(game.timer.image('objects/object_door_203{}.png'))
        action MoveTo(L_maria_bedroom)

    if M_anon.between_states(S_ano25_sick, S_ano26_done):
        imagebutton:
            focus_mask True
            pos 10, 462
            idle M_maria.get_button_path('home_sleeping', use=('bump', 'belly'), use_day_timer=True)
            hover HoverImage(M_maria.get_button_path('home_sleeping', use=('bump', 'belly'), use_day_timer=True))
            action TalkTo(M_maria)
    elif L_maria_lounge.is_here(M_maria):
        imagebutton:
            focus_mask True
            if game.timer.is_evening():
                pos 194, 322
            elif 1 < M_maria.pregnancy.stage:
                pos 590, 299
            else:
                pos 593, 364
            idle M_maria.get_button_path('home', use=('bump', 'belly', 'baby'), use_day_timer=True)
            hover HoverImage(M_maria.get_button_path('home', use=('bump', 'belly', 'baby'), use_day_timer=True))
            action TalkTo(M_maria)

    if L_maria_lounge.is_here(M_tony):
        imagebutton:
            focus_mask True
            if game.timer.is_evening():
                pos 0, 436
            else:
                pos 17, 362
            idle M_tony.get_button_path('couch', use_day_timer=True)
            hover HoverImage(M_tony.get_button_path('couch', use_day_timer=True))
            if game.timer.is_day() or not L_maria_lounge.is_here(M_maria):
                action TalkTo(M_tony)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
