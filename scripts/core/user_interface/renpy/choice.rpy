

screen choice(items):
    style_prefix 'choice'

    vbox:
        for i in items:
            $ disabled = i.kwargs.get('disabled', False)
            button:
                if not disabled:
                    hover_background 'choice_over'
                text i.caption:
                    style "choice_button_text"
                    if not disabled:
                        idle_color 'eee'
                        hover_color 'fff'
                    else:
                        idle_color '777'
                        hover_color '777'
                action If(not disabled, i.action, NullAction())


define config.narrator_menu = True


style choice_vbox:
    spacing 10
    xalign .5
    yanchor .5
    ypos .45

style choice_button:
    background 'choice_idle'
    padding (3, 5, 3, 4)
    xsize 450

style choice_button_text:
    insensitive_color '444'
    size 16
    xalign .5
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
