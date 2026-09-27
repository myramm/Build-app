screen warehouse_storage():
    add L_warehouse_storage.background

    imagebutton:
        focus_mask True
        align .5, .95
        idle 'boxes/auto_option_generic_01.png'
        hover HoverImage('boxes/auto_option_generic_01.png')
        action MoveTo(L_warehouse_lab)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
