screen pizzeria_interior():
    add L_pizzeria_interior.background

    imagebutton:
        focus_mask True
        pos 0, 223
        idle game.timer.image('objects/object_door_125{}.png')
        hover HoverImage(game.timer.image('objects/object_door_125{}.png'))
        action MoveTo(L_pizzeria_kitchen)

    if L_pizzeria_interior.is_here(M_tony):
        imagebutton:
            focus_mask True
            pos 333, 264
            if M_maria.pregnancy.stage > 4:
                idle M_tony.get_button_path('counter', machine=M_maria, use_pregnancy=False, use_baby=game.timer.is_morning())
                hover HoverImage(M_tony.get_button_path('counter', machine=M_maria, use_pregnancy=False, use_baby=game.timer.is_morning()))
            else:
                idle 'characters/tony/buttons/character_tony_counter.png'
                hover HoverImage('characters/tony/buttons/character_tony_counter.png')
            action TalkTo(M_tony)

    if M_anon.finished_state(S_ano04_test) and not M_anon.is_state(S_ano11_prep) and game.timer.is_day():
        imagebutton:
            focus_mask True
            pos 613, 295
            idle 'objects/object_pizza_01.png'
            hover HoverImage('objects/object_pizza_01.png')
            action HideAll(), Jump('pizzeria_interior_job')

    imagebutton:
        focus_mask True
        align .5, .95
        idle 'boxes/auto_option_08.png'
        hover HoverImage('boxes/auto_option_08.png')
        action MoveTo(L_pizzeria_exterior)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
