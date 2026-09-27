init python hide in credits:
    '''
    Self-contained data preparation for the Credits screen. Executes in
    a sandbox to avoid unnecessary leaking into the global scope and
    publishes the data into the credits namespace for use in the menu.
    '''

    from itertools import groupby
    from math import ceil
    from operator import itemgetter

    from renpy.display.behavior import Adjustment
    from store import FontGroup, credits as export
    from store.io import open


    group = '{{color=#{}}}{},{{/color}}'

    team = (('strayerror', _('Code, TA & Posing')),
            ('CreamyCookie', _('HR & PR')),
            ('', ''),
            ('AoiichiNiiSan', _('Music & SFX')),
            ('CaptainSploosh', _('Dialogue & Writing')),
            ('Sam9', _('Server side & Website')))

    ex = ('Catbug', 'Dogeek', 'Hurfy', 'NhKPaNdA')
    qa = ('Axios',
          'Kennyannydenny',
          'KingM',
          'Livingston',
          'mil578',
          'PornNStuff')


    class PageableAdjustment(Adjustment):
        restart_interaction_at_limit = True
        
        def pgdn(self):
            self.change(self.value + self.page)
        
        def pgup(self):
            self.change(self.value - self.page)


    def sign(v):
        return cmp(v, 0)


    font = FontGroup().add('DejaVuSans.ttf', None, None)


    with open('scripts/data/sourcehansans-patron.txt', encoding='utf8') as f:
        for r in f.read().split():
            start, __, end = r.partition('-')
            start = int(start, 16)
            end = int(end, 16) if end else start
            
            font.add('fonts/sourcehansans-patron.otf', start, end)

    with open('pledge_list.txt', encoding='utf8') as f:
        pledges = '.'.join(' '.join(
            group.format(c, ', '.join(n for n, _ in g)) for c, g in groupby(
                (l.strip().split(',') for l in f),
                key=itemgetter(1))).rsplit(',', 1))

    export.adjustment = PageableAdjustment
    export.font = font
    export.pledges = pledges
    export.sign = sign

    half = int(ceil(len(team) / 2.0))
    export.team = tuple(team[i:i + half] for i in xrange(0, len(team), half))

    export.ex = ex
    export.qa = qa
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
