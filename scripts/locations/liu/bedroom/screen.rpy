screen liu_bedroom():
    add L_liu_bedroom.background

    imagebutton:
        focus_mask True
        pos 200, 305
        idle game.timer.image('objects/object_door_201{}.png')
        hover HoverImage(game.timer.image('objects/object_door_201{}.png'))
        action MoveTo(L_liu_lounge)

    if M_anon.is_state(S_ano24_find):

        imagebutton:
            focus_mask True
            pos 356, 339
            idle game.timer.image('objects/object_dresser_kim{}.png')
            hover HoverImage(game.timer.image('objects/object_dresser_kim{}.png'))
            action HideAll(), Jump('liu_bedroom_wardrobe')

        imagebutton:
            focus_mask True
            pos 46, 292
            if M_liu.get('ano24_statue', False):
                idle game.timer.image('objects/object_statue_kim_body{}.png')
                hover HoverImage(game.timer.image('objects/object_statue_kim_body{}.png'))
            else:
                idle game.timer.image('objects/object_statue_kim_all{}.png')
                hover HoverImage(game.timer.image('objects/object_statue_kim_all{}.png'))
            action HideAll(), Jump('liu_bedroom_statue')

        if M_liu.get('ano24_statue', False):
            imagebutton:
                focus_mask True
                pos 46, 292
                idle PulseImage(game.timer.image('objects/object_statue_kim_head{}.png'),
                                HoverImage(game.timer.image('objects/object_statue_kim_head{}.png')),
                                delay1=.4, delay2=.4)
                hover HoverImage(game.timer.image('objects/object_statue_kim_head{}.png'))
                action HideAll(), Jump('liu_bedroom_stash')

        imagebutton:
            focus_mask True
            pos 579, 313
            idle game.timer.image('objects/object_frame_kim{}.png')
            hover HoverImage(game.timer.image('objects/object_frame_kim{}.png'))
            action HideAll(), Jump('liu_bedroom_picture')

        imagebutton:
            focus_mask True
            pos 780, 188
            idle game.timer.image('objects/object_nuke_kim{}.png')
            hover HoverImage(game.timer.image('objects/object_nuke_kim{}.png'))
            action HideAll(), Jump('liu_bedroom_bomb')

    if M_anon.finished_state(S_ano28_clue):
        imagebutton:
            focus_mask True
            pos 579, 313
            idle game.timer.image('objects/object_frame_liu{}.png')
            hover HoverImage(game.timer.image('objects/object_frame_liu{}.png'))
            action HideAll(), Jump('liu_bedroom_painting')

    if L_liu_bedroom.is_here(M_liu):
        imagebutton:
            focus_mask True
            pos 628, 380
            idle M_liu.get_button_path('home_bed', use_day_timer=True)
            hover HoverImage(M_liu.get_button_path('home_bed', use_day_timer=True))
            action TalkTo(M_liu)


screen ano24_find_stash():
    layer 'master'

    add 'location_liu_bedroom_statue_coseup'

    imagebutton:
        focus_mask True
        pos 127, 148
        idle 'objects/object_documents_statue.png'
        hover HoverImage('objects/object_documents_statue.png')
        action Return()
        sensitive renpy.get_mode() == 'screen'
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
