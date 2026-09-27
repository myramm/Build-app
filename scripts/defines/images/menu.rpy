image menu_background = '#0b0d17'
image menu_condom = Image('backgrounds/menu_condom.png', yanchor=59)
image menu_tissue = Image('backgrounds/menu_tissue.png', yanchor=190)
image menu_trash = Image('backgrounds/menu_trash.png', yanchor=284)

image menu_frame = Frame('boxes/popup_generic.png',
                         left=50, top=50, right=50, bottom=50)
image menu_frame_fade = Transform('menu_frame', alpha=.25)

image menu_frame_dark = Fixed('menu_frame', Window('#0007', margin=(4, 4)))
image menu_frame_opaque = Fixed(Window('menu_background', margin=(4, 4)), 'menu_frame')

image menu_bar_full = '#404f7e'
image menu_bar_empty = '#2c3758'
image menu_bar_thumb = '#8c95b1'

image menu_btn = 'buttons/button_generic_popup_full.png'
image menu_btn_idle = Frame('menu_btn',
                            left=14, top=9, right=10, bottom=17)
image menu_btn_over = Frame(im.MatrixColor(ImageReference('menu_btn'), over),
                            left=14, top=9, right=10, bottom=17)
image menu_btn_noop = Frame(im.MatrixColor(ImageReference('menu_btn'), noop),
                            left=14, top=9, right=10, bottom=17)
image menu_btn_live = Frame(im.MatrixColor(ImageReference('menu_btn'), live),
                            left=14, top=9, right=10, bottom=17)

define warn = im.matrix.saturation(1.55) * im.matrix.contrast(1.07) * im.matrix.hue(110)

image warn_btn = im.MatrixColor(ImageReference('menu_btn'), warn)
image warn_btn_idle = Frame('warn_btn',
                            left=14, top=9, right=10, bottom=17)
image warn_btn_over = Frame(im.MatrixColor(ImageReference('warn_btn'), over),
                            left=14, top=9, right=10, bottom=17)
image warn_btn_noop = Frame(im.MatrixColor(ImageReference('warn_btn'), noop),
                            left=14, top=9, right=10, bottom=17)
image warn_btn_live = Frame(im.MatrixColor(ImageReference('warn_btn'), live),
                            left=14, top=9, right=10, bottom=17)

image delete_btn_idle = 'buttons/delete_button_01.png'
image delete_btn_over = im.MatrixColor('buttons/delete_button_01.png', over)

image slot_compat = Transform('popup_generic_warning', offset=(-3, -4), zoom=.9)
image slot_broken = Transform('pizza_mark_bad', offset=(-3, -3), zoom=.5)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
