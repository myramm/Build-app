image popup_hint = Frame('boxes/popup_generic_awesomo.png', 12, 12, 130, 20)

image shop_cost_idle = Frame(im.Crop('buttons/shop_generic.png',
                                     (0, 0, 148, 53)), 8, 8, 53, 8)
image shop_cost_over = Frame(im.Crop(im.MatrixColor('buttons/shop_generic.png', over),
                                     (0, 0, 148, 53)), 8, 8, 53, 8)
image shop_text_idle = Frame(im.Crop('buttons/shop_generic.png',
                                     (148, 0, 82, 53)), 8, 8, 8, 8)
image shop_text_over = Frame(im.Crop(im.MatrixColor('buttons/shop_generic.png', over),
                                    (148, 0, 82, 53)), 8, 8, 8, 8)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
