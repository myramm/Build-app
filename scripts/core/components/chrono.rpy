init python hide:
    '''
    A stopwatch-like text displayable which updates in realtime.
    '''

    fmt = '{:0>2}:{:0>2}:{:0>2}:{:0>2}'


    class Chrono(DynamicDisplayable):
        def __init__(self, **kwargs):
            super(self.__class__, self).__init__(self.displayable, **kwargs)
        
        def displayable(self, st, at, **kwargs):
            s = int(at)
            
            d = s // 86400
            s %= 86400
            h = s // 3600
            s %= 3600
            i = s // 60
            s %= 60
            
            return Text(fmt.format(d, h, i, s), **kwargs), .2


    store.Chrono = Chrono
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
