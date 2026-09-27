define dead = (im.matrix.saturation(0.0) *
               im.matrix.contrast(0.93) *
               im.matrix.brightness(-.07))

define live = (im.matrix.saturation(2.38) *
               im.matrix.contrast(0.93) *
               im.matrix.brightness(0.07))

define over = (im.matrix.saturation(0.98) *
               im.matrix.contrast(1.07) *
               im.matrix.brightness(0.07))

define noop = (im.matrix.saturation(1.02) *
               im.matrix.contrast(0.93) *
               im.matrix.brightness(-.07))
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
