init -1 python:
    class Rect(object):
        def __init__(self, x, y, width, height, padding=(0, 0)):
            self.x = x
            self.y = y
            self.width = width
            self.height = height
            self.padx, self.pady = padding
        
        @property
        def position(self):
            return x, y
        
        def centerx(self, rect):
            return abs(width - rect.width) / 2 + self.x + rect.padx
        
        def centery(self, rect):
            return abs(height - rect.height) / 2 + self.y + rect.pady
        
        def leftalign(self, rect):
            return self.x + rect.padx
        
        def rightalign(self, rect):
            return self.x + self.width - rect.width - rect.padx
        
        def topalign(self, rect):
            return self.y + rect.pady
        
        def bottomalign(self, rect):
            return self.y + self.height - rect.height - rect.pady
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
