init python hide:
    '''
    Wrest the gun from Raz by spam clicking/tapping. Strength is
    critical, home you been hitting the gym, bro!
    '''

    from bisect import bisect


    class TugOfWarMinigame(renpy.python.NoRollback):
        __version__ = 0
        
        base = .1
        
        def __init__(self, strength, **kwargs):
            super(TugOfWarMinigame, self).__init__(**kwargs)
            self.phase = 'intro'
            self.force = self.base * max(strength / 5., .2)
            self.swing = 3.5
            self.twist = 'right'
        
        def start(self):
            self.phase = 'running'
        
        @property
        def frame(self):
            return bisect((5. / 3., 5 - 5. / 3.), self.swing)
        
        def pull(self, skew):
            self.twist = skew
            
            if skew == 'left':
                self.swing -= self.force
            else:
                self.swing += self.base * (1 + (.75 / self.swing))
            
            if not 1 < self.swing < 5:
                self.phase = 'outro'


    store.TugOfWarMinigame = TugOfWarMinigame
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
