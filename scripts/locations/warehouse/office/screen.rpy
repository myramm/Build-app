screen warehouse_office():
    add L_warehouse_office.background

    if L_warehouse_office.is_here(M_nadya):
        imagebutton:
            focus_mask True
            if M_nadya.is_state(S_nad01_lewd):
                pos 0, 389
                idle M_nadya.get_button_path('warehouse_office_couch', use_day_timer=True)
                hover HoverImage(M_nadya.get_button_path('warehouse_office_couch', use_day_timer=True))
            else:
                pos 0, 387
                idle M_nadya.get_button_path('warehouse_office_couch_dressed', use=('bump', 'belly', 'baby'), use_day_timer=True)
                hover HoverImage(M_nadya.get_button_path('warehouse_office_couch_dressed', use=('bump', 'belly', 'baby'), use_day_timer=True))
            action TalkTo(M_nadya)

    if L_warehouse_office.is_here(M_katya):
        imagebutton:
            focus_mask True
            pos 619, 347 at Transform(crop=(0, 0, 142, 145))
            idle M_katya.get_button_path('warehouse_sit')
            hover HoverImage(M_katya.get_button_path('warehouse_sit'))
            action TalkTo(M_katya)

    imagebutton:
        focus_mask True
        align .5, .95
        idle 'boxes/auto_option_generic_01.png'
        hover HoverImage('boxes/auto_option_generic_01.png')
        action MoveTo(L_warehouse_depot)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
