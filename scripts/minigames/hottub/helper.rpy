label minigame_hottub(min=1, max=10):
    $ renpy.dynamic(mouse_visible=False)
    show screen minigame_hottub(min, max) with fade
    call screen empty()
    hide screen minigame_hottub
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
