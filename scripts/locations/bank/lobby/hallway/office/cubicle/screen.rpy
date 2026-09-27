screen bank_cubicle():
    add L_bank_cubicle.background

    if L_bank_cubicle.is_here(M_tina):
        imagebutton:
            focus_mask True
            pos 424, 316
            idle M_tina.get_button_path('bank_cubicle')
            hover HoverImage(M_tina.get_button_path('bank_cubicle'))
            action TalkTo(M_tina)

    imagebutton:
        focus_mask True
        align .5, .95
        idle 'boxes/auto_option_generic_01.png'
        hover HoverImage('boxes/auto_option_generic_01.png')
        action MoveTo(L_bank_office)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
