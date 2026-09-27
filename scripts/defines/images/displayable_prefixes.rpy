init -10 python:
    def jenny_face_scale(s):
        return Transform(s, xzoom=-.76, yzoom=.76,
                         xoffset=129, yoffset=144)

    config.displayable_prefix["jenny_face"] = jenny_face_scale
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
