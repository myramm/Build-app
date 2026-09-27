image popup_minigame_poker = Window('object_poker_01',
                                    padding=(0, 50, 0, 20))
image popup_minigame_yoga = Window('popups/popup_minigame_yoga.png',
                                   padding=(0, 30, 0, 0))


init python in popup:
    def minigame(ref):
        return ('popup_notice',
                _('You have unlocked a new {=minigame_keyword}MINIGAME{/}!')) \
             + minigame.data[ref]


    minigame.data = {
        'basketball': (_('Basketball'), 'popup_minigame_basketball'),
        'gardening': (_('Gardening'), 'object_garden_01'),
        'poker': (_('Poker'), 'popup_minigame_poker'),
        'yoga': (_('Yoga'), 'popup_minigame_yoga')}


style minigame_keyword:
    color 'e66f05'
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
