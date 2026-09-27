image sex_controls = Frame(im.Crop('buttons/button_sex_options.png',
                                   (0, 5, 285, 30)),
                           left=130, top=0, right=130, bottom=0)


style sex_button:
    xminimum 150
    ypadding 5

style sex_button_text:
    idle_color 'ddd'
    hover_color 'fff'
    insensitive_color '999'
    xalign .5
    size 14

style sex_frame:
    background 'sex_controls'
    padding (50, 0)
    xalign .5

style sex_vbox:
    spacing 5
    xalign .5
    yanchor 1.
    ypos .975
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
