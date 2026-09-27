screen warehouse_lab():
    add L_warehouse_lab.background

    imagebutton:
        focus_mask True
        pos 877, 342
        idle game.timer.image('objects/object_door_215{}.png')
        hover HoverImage(game.timer.image('objects/object_door_215{}.png'))
        action MoveTo(L_warehouse_storage)

    imagebutton:
        focus_mask True
        pos 23, 352
        idle game.timer.image('objects/object_door_214{}.png')
        hover HoverImage(game.timer.image('objects/object_door_214{}.png'))
        action MoveTo(L_warehouse_depot)

    if L_warehouse_lab.is_here(M_khadne):
        imagebutton:
            focus_mask True
            pos 307, 433
            action TalkTo(M_khadne)
            if M_khadne.is_state(S_kha01_lewd):
                idle M_khadne.get_button_path('warehouse_sit2')
                hover HoverImage(M_khadne.get_button_path('warehouse_sit2'))
            else:
                idle M_khadne.get_button_path('warehouse_sit')
                hover HoverImage(M_khadne.get_button_path('warehouse_sit'))
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
