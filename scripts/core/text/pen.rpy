init python hide:
    '''
    A custom text tag to intended to give a very rough approximation of
    coloured fibre tip pens by using text outlines of varying opacities
    to bleed the edges of the characters ever do slightly.
    '''

    pens = {'aqua': '286d6a',
            'black': '111111',
            'blue': '2b3187',
            'indigo': '4b0082',
            'lime': '00b300',
            'maroon': '5a0a35',
            'navy': '060c57',
            'neonpink': 'd70087',
            'orange': 'c64e39',
            'pink': 'b51080',
            'purple': '823894',
            'red': '9b0404',
            'silver': '736e7c',
            'yellow': 'b39800'}


    def pen_tag(tag, argument, contents):
        pen = pens[argument]
        depth = 0
        
        yield (renpy.TEXT_TAG, 'color=' + pen)
        yield (renpy.TEXT_TAG, 'outlinecolor=' + pen + '0f')
        
        for tag in contents:
            tok, txt = tag
            if tok is renpy.TEXT_TAG:
                depth += txt.startswith('pen=')
                if depth is 0:
                    if txt == 'b':
                        yield (renpy.TEXT_TAG, 'outlinecolor=' + pen + '44')
                        yield (renpy.TEXT_TAG, 'k=2')
                        continue
                    if txt == '/b':
                        yield (renpy.TEXT_TAG, '/k')
                        yield (renpy.TEXT_TAG, '/outlinecolor')
                        continue
                depth -= txt == '/pen'
            yield tag
        
        yield (renpy.TEXT_TAG, '/outlinecolor')
        yield (renpy.TEXT_TAG, '/color')


    config.custom_text_tags['pen'] = pen_tag
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
