init python early hide in io:
    '''
    This module eases RenPy text file access. It wraps renpy.file with
    the io.TextIOWrapper class for improved control over encoding and
    line endings.
    '''

    from io import BufferedReader, TextIOWrapper

    from renpy.exports import file
    from store import io as export


    class ReadableFile(object):
        def __init__(self, fn):
            self._raw = file(fn)
            self.closed = False
        
        def close(self):
            rv = self._raw.close()
            self.closed = True
            return rv
        
        def readable(self):
            return True
        
        def readinto(self, b):
            length = len(b)
            data = self.read(length)
            rv = len(data)
            b[:rv] = data
            return rv
        
        def seekable(self):
            return True
        
        def writable(self):
            return False
        
        def __getattr__(self, name):
            return getattr(self._raw, name)


    def open(fn, **kwargs):
        return TextIOWrapper(BufferedReader(ReadableFile(fn)), **kwargs)


    export.open = open
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
