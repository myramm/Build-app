init python hide in phone:
    from json import load

    from renpy.exports import file
    from store import phone as exports

    from store.util import struct


    with file('scripts/data/text_messages.json') as f:
        data = load(f)


    class Message(struct):
        def __init__(self, name):
            super(Message, self).__init__(data[name])
            self.disp = renpy.displayable(self.image)
        
        @property
        def content(self):
            out = self.preview
            if 'content' in self:
                out += ' ' + self['content']
            return out


    def texts(messages):
        for m in messages:
            yield Message(m)


    exports.data = data
    exports.texts = texts


init python hide:
    def read():
        if not game.new_message:
            return
        
        game.new_message = False
        game.read_message = True


    phone.read = read
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
