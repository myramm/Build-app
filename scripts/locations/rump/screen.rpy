screen mayor_rumps_frontyard():
    add L_rump_front.background

    if not game.timer.is_night() and not M_anon.is_state(S_ano20_cops, S_ano20_done):
        add game.timer.image('characters/bodyguard/buttons/character_bodyguard_front{}02.png'):
            pos 684, 415

    imagebutton:
        focus_mask True
        pos 854, 398
        idle game.timer.image('objects/object_door_142{}.png')
        hover HoverImage(game.timer.image('objects/object_door_142{}.png'))
        action MoveTo(L_rump_lobby)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
