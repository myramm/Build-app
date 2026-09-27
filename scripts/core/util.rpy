init python early in util:
    '''
    A place for storing simple generic reusable components that don't
    natually fit elsewhere.
    '''

    def lerp(x, min=0., max=1.):
        return (1 - x) * min + x * max


    class notset(_object):
        '''
        A no-op class to be used as a sentinel value for unset keyword
        arguments when necessary.
        '''
        pass


    class struct(dict):
        '''
        A minimal pickle-safe dot-accessible dict implementation.
        '''
        
        __getattr__ = dict.get
        
        def __reduce__(self): 
            return (struct, (), None, None, self.iteritems())


    def version(v):
        try:
            return tuple(int(n) for n in v.split('.'))
        except:
            return None
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
