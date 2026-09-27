screen pizzeria_kitchen():
    add L_pizzeria_kitchen.background

    if M_anon.is_state(S_ano11_prep):
        add 'object_door_126_patch':
            pos 385, 313

    imagebutton:
        focus_mask True
        pos 386, 315
        if M_anon.is_state(S_ano11_prep):
            idle 'objects/object_door_126_closed.png'
            hover HoverImage('objects/object_door_126_closed.png')
        else:
            idle game.timer.image('objects/object_door_126{}.png')
            hover HoverImage(game.timer.image('objects/object_door_126{}.png'))
        action MoveTo(L_pizzeria_storage)

    if M_anon.finished_state(S_ano11_done):
        add game.timer.image('objects/object_plaque{}.png'):
            alpha .25
            pos 244, 294
            zoom .99

        imagebutton:
            focus_mask True
            pos 240, 290
            idle game.timer.image('objects/object_plaque{}.png')
            hover HoverImage(game.timer.image('objects/object_plaque{}.png'))
            action HideAll(), Jump('pizzeria_kitchen_eotm')

    imagebutton:
        focus_mask True
        pos 142, 307
        idle game.timer.image('objects/object_door_127{}.png')
        hover HoverImage(game.timer.image('objects/object_door_127{}.png'))
        action MoveTo(L_pizzeria_interior)

    if L_pizzeria_kitchen.is_here(M_tony):
        imagebutton:
            focus_mask True
            pos 616, 357
            idle 'characters/tony/buttons/character_tony_03.png'
            hover HoverImage('characters/tony/buttons/character_tony_03.png')
            action TalkTo(M_tony)

    if M_anon.between_states(S_ano25_sick, S_ano26_done):
        pass
    elif L_pizzeria_kitchen.is_here(M_maria):
        imagebutton:
            focus_mask True
            pos 672, 331
            if M_maria.pregnancy.stage in (3, 4):
                idle 'characters/maria/buttons/character_maria_02.png'
                hover HoverImage('characters/maria/buttons/character_maria_02.png')
            elif 1 < M_maria.pregnancy.stage < 5 or M_maria.pregnancy.stage > 4 and game.timer.is_afternoon():
                pos 616, 288
                idle M_maria.get_button_path('kitchen', use_baby=True)
                hover HoverImage(M_maria.get_button_path('kitchen', use_baby=True))
            else:
                idle 'characters/maria/buttons/character_maria_01.png'
                hover HoverImage('characters/maria/buttons/character_maria_01.png')
            action TalkTo(M_maria)

    use mods_screens_hook("pizzeria_kitchen")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
