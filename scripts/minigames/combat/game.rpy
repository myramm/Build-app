init python in combat:
    class Entity:
        def __init__(self, hp, hue=0):
            self.hp = self.max = hp
            self.hue = hue
        
        @property
        def dmg(self):
            return self.max - self.hp
        
        def hit(self):
            self.hp -= 1


init python hide in combat:
    from store import FadeOver, ImageDissolve, MultipleTransition, Pause, Solid
    from store import im
    from store import combat as export


    black = Solid((0, 0, 0, 255))

    pause = Pause(.5)
    pulse = FadeOver(.1, 0, .2)

    wipevsplit = ImageDissolve('transitions/wipevsplit.png', .3, ramplen=4)


    def Combat(*args, **kwargs):
        return MultipleTransition([False, pulse,
                                   False, pulse,
                                   False, ImageDissolve(*args, **kwargs),
                                   black, pause,
                                   black, wipevsplit,
                                   True])


    export.wipeccw = Combat('transitions/wipeccw.png', 1.5)
    export.wipeccw2 = Combat('transitions/wipeccw2.png', 1.)

    export.snakein = Combat('transitions/snake.png', 1.75, ramplen=1)
    export.snakeout = Combat(im.Flip('transitions/snake.png', vertical=True),
                             1.75, ramplen=1, reverse=True)

    export.trapped = Combat('transitions/trapped.png', 1.5, ramplen=1)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
