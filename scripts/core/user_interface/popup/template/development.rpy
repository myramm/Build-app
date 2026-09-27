init python in popup:
    def alpha():
        return ('popup_notice',
                _('This part is {=alpha_keyword}UNDER CONSTRUCTION{/}!'),
                _('The game is still in alpha. More content next release!'),
                'popup_construction')


    def missing():
        return ('popup_notice',
                _('Ooops! You found a {=alpha_keyword}MISSING{/} popup!'),
                '{b}Ref{/b}: [name!r], [args!r]',
                renpy.random.choice(('minigame01_bad02',
                                     'minigame01_bad03b',
                                     'minigame01_bad05b',
                                     'minigame01_bad06b',
                                     'minigame01_bad07',
                                     'minigame01_bad08',
                                     'minigame01_good01b',
                                     'minigame01_good02b',
                                     'minigame01_good03b',
                                     'minigame01_good04b')))


style alpha_keyword:
    color 'ffb957'
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
