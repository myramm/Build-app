screen warehouse_depot():
    add L_warehouse_depot.background

    imagebutton:
        focus_mask True
        pos 511, 236
        idle game.timer.image('objects/object_door_208{}.png')
        hover HoverImage(game.timer.image('objects/object_door_208{}.png'))
        action MoveTo(L_warehouse_office)

    if L_warehouse_office.is_here(M_nadya):
        imagebutton:
            focus_mask True
            pos 433, 234
            idle M_svetlana.get_button_path('warehouse_stairs')
            hover HoverImage(M_svetlana.get_button_path('warehouse_stairs'))
            action TalkTo(M_svetlana)

    if L_warehouse_depot.is_here(M_nadya):
        imagebutton:
            focus_mask True
            pos 274, 447
            idle M_nadya.get_button_path('warehouse_main', use=('bump', 'belly', 'baby'), use_day_timer=True)
            hover HoverImage(M_nadya.get_button_path('warehouse_main', use=('bump', 'belly', 'baby'), use_day_timer=True))
            action TalkTo(M_nadya)

    imagebutton:
        focus_mask True
        pos 804, 427
        idle game.timer.image('objects/object_door_209{}.png')
        hover HoverImage(game.timer.image('objects/object_door_209{}.png'))
        action MoveTo(L_warehouse_lab)

    imagebutton:
        focus_mask True
        pos 95, 427
        idle game.timer.image('objects/object_door_210{}.png')
        hover HoverImage(game.timer.image('objects/object_door_210{}.png'))
        action MoveTo(L_warehouse_furnace)

    imagebutton:
        focus_mask True
        pos 95, 427
        idle game.timer.image('objects/object_door_210{}.png')
        hover HoverImage(game.timer.image('objects/object_door_210{}.png'))
        action MoveTo(L_warehouse_furnace)

    imagebutton:
        focus_mask True
        align .5, .95
        idle 'boxes/auto_option_generic_01.png'
        hover HoverImage('boxes/auto_option_generic_01.png')
        action MoveTo(L_warehouse)


screen ano27_peek_warehouse_depot():
    layer 'master'
    sensitive renpy.get_mode() == 'screen'

    default opts = (('cards',    'objects/object_thugs_warehouse_cards',    (713, 225)),
                    ('drink',    'objects/object_thugs_warehouse_standing', (417, 420)),
                    ('forklift', 'objects/object_forklift_evening',         (796, 401)),
                    (False,      'objects/object_door_210_anon',            ( 95, 424)),
                    ('lab',      'objects/object_door_209_night',           (804, 427)),
                    ('office',   'objects/object_door_208_night',           (511, 236)))

    add 'backgrounds/location_warehouse_main_night.jpg'

    for item, img, pos in opts:
        imagebutton:
            focus_mask True
            pos pos
            idle img + '.png'
            hover HoverImage(img + '.png')
            action Return(item)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
