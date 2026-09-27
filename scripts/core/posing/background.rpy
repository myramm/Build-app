init python hide:
    from math import ceil, floor


    identity = im.matrix.identity()

    maxx = config.screen_width
    maxy = config.screen_height
    midx = maxx / 2
    midy = maxy / 2


    @renpy.pure
    def _background(i, b, x, y, z):
        if z != 1.:
            z = float(z)
            x = floor(max(min(x - midx / z, maxx - maxx / z), 0))
            y = floor(max(min(y - midy / z, maxy - maxy / z), 0))
            i = im.Crop(i, (x, y, ceil(maxx / z), ceil(maxy / z)))
            i = im.Rotozoom(i, 0, z)
        if b:
            i = im.Blur(i, b)
        return i


    season = (('',), ('_christmas', ''), ('_halloween', ''))
    time = (('_morning', '_day', '_any'),
            ('_afternoon', '_day', '_any'),
            ('_evening', '_night', '_any'),
            ('_night', '_any'))


    @renpy.pure
    def _image(n, s, t):
        for s_ in season[s]:
            for t_ in time[t]:
                i = 'backgrounds/location_{}{}{}.jpg'.format(n, s_, t_)
                if renpy.loadable(i):
                    return i


    def background(x=midx, y=midy, z=1., b=1.7, l=None, o=0, s=None, t=None):
        n = l or player.location
        s = s if s is not None else Game.period_index()
        t = t if t is not None else min(3, max(0, game.timer._tod + o))
        if isinstance(n, Location):
            n = n._bg
        i = _image(n, s, t)
        if i:
            return _background(i, b, x, y, z)
        else:
            return Text("Background for '{}' not found.".format(n),
                        color=(255, 0, 0, 255), align=(.5, .1))


    store.background = background
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
