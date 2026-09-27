image choice_idle = Frame('buttons/choice.png', 45, 9)
image choice_over = Frame(im.MatrixColor('buttons/choice.png', over), 45, 9)

image notify = Frame(im.Crop('buttons/choice.png', (250, 0, 250, 30)),
                          left=0, top=9, right=45, bottom=9)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
