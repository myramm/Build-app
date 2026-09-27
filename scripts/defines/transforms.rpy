define local = Transform()

define phoneleft = Split(-15, 'left')
define phoneright = Split(15, 'right')


transform flip:
    xzoom -1

transform unflip:
    xzoom 1
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
