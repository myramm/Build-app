

screen say(who, what, native=None):
    style_prefix 'say'

    window:
        id 'window'
        has vbox

        if who is not None:

            window:
                id 'namebox'
                style 'namebox'
                text who id 'who'

        if native is None:
            text what id 'what' style_suffix 'dialogue'
        else:
            text native id 'native' style_suffix 'dialogue' slow_abortable True slow_cps True
            text what id 'what' style_suffix 'thought'


init python:
    config.character_id_prefixes.append('namebox')


style say_window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style say_window:
    align (.5, 1.)
    background Frame('boxes/dialogue_chatbox.png', 12, 12)
    padding (80, 20)
    xfill True
    ysize 122

style say_label:
    bold True
    yalign .5

style say_vbox:
    spacing 8
    xfill True

style say_thought:
    color 'ccc'
    italic True
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
