image cam = Fixed(
    'vfx/cam.png',
    HBox(Text('\u26ab', color='c70401', size=48, yalign=.5,
              outlines=((absolute(1), 'c704011f', 0, 0),)),
         Text('LIVE', color='000', size=32, yalign=.5,
              outlines=((absolute(1), '0000001f', 0, 0),)), xalign=.5))

image rec = Fixed(
    'vfx/cam.png',
    HBox(Text('\u26ab', color='c70401', size=48, yalign=.5,
              outlines=((absolute(1), 'c704011f', 0, 0),)),
         Text('REC', color='000', size=32, yalign=.5,
              outlines=((absolute(1), '0000001f', 0, 0),)), xalign=.5),
    Chrono(anchor=(1., .5), color='000', pos=(880, 56), size=25))
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
