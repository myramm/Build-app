screen warehouse_bushes():
    add L_warehouse_bushes.background

    imagebutton:
        focus_mask True
        align .5, .95
        idle 'boxes/auto_option_generic_01.png'
        hover HoverImage('boxes/auto_option_generic_01.png')
        action MoveTo(L_warehouse)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
