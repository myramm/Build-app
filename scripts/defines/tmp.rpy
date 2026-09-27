image tmp = ParameterizedText(align=(.5, .1),
                              color='f0f',
                              outlines=((4, '0007', 0, 0), (1, 'f0f', 0, 0)),
                              size=24)

image tmp_tile = im.Rotozoom(im.Twocolor('_transparent_tile.png',
                                         'f0f', '000'), 0, .5)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
