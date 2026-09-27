define eyeopen = Blink(.8)
define fasteyeopen = Blink(.15)

define eyeshut = Blink(.4, reverse=True)
define fasteyeshut = Blink(.15, reverse=True)

define sliteyeopen = Blink(.8, time_warp=renpy.partial(util.lerp, max=.3))
define sliteyeshut = Blink(.4, reverse=True, time_warp=renpy.partial(util.lerp, min=.3))

define wideeyeopen = Blink(.8, time_warp=renpy.partial(util.lerp, max=.7))
define wideeyeshut = Blink(.4, reverse=True, time_warp=renpy.partial(util.lerp, min=.7))

define fastdissolve = Dissolve(.2)
define slowdissolve = Dissolve(.8)

define flash = Fade(.25, 0.0, .75, color='fff')
define flashbulb = Fade(.1, 0.0, .2, color='fff')

define fastfade = Fade(.2, 0., .2)
define longfade = Fade(.5, 1., .5)
define slowfade = Fade(2., 1., 2.)
define gameover = Fade(2., 0., .5)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
