init python hide in diary:
    '''
    Layout, formatting, and content for Jenny's diary. This immutable
    data set will be used by helper functions to dynamically construct
    the diary's contents interposing special event pages as needed.
    '''

    from itertools import groupby

    from renpy.loader import game_files
    from renpy.store import M_jenny, diary as export

    from store.io import open


    extra = {}
    sep = lambda x: x != '---\n'
    parse = lambda f: tuple(tuple(l.strip() for l in g)
                            for k, g in groupby(f, key=sep) if k)
    key = 'diary_extra_'

    path = 'scripts/data/diary/'
    offset = len(path)
    for _, fn in game_files:
        if fn.startswith(path) and fn.endswith('.txt'):
            with open(fn, encoding='utf8') as f:
                extra[key + fn[offset:-4]] = parse(f)

    data = extra.pop(key + 'default')


    def pages():
        co = M_jenny.diary_progress
        rv = list(data[:co])
        
        ex = reversed(sorted((v, extra[k])
                             for k, v in M_jenny._vars.items()
                             if v and k in extra))
        
        for (i, _), v in ex:
            rv[i:i] = v
        
        return rv


    export.pages = pages
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
