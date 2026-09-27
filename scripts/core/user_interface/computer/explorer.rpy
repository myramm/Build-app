screen pc_explorer(cols, rows, refs, layout='rows', style=None):
    style_prefix 'pc_explorer'

    frame:
        has grid cols rows
        transpose layout != 'rows'

        for i in pc.apps.fetch(refs):

            button:
                if i.action:
                    action Return(i.action)

                vbox:

                    frame:
                        style_suffix 'icon'
                        background 'pc_icon_' + i.icon + '_idle'
                        hover_background 'pc_icon_' + i.icon + '_over'
                    text i.name:
                        if style:
                            style_suffix style + '_text'

        for i in xrange(cols * rows - len(refs)):
            null


style pc_explorer_button:
    padding (5, 5)

style pc_explorer_icon:
    xysize (80, 70)
    xalign .5

style pc_explorer_frame:
    padding (10, 10)

style pc_explorer_grid:
    xspacing 10

style pc_explorer_text:
    color '111'
    hover_color '333'
    size 13
    text_align .5
    xalign .5
    xmaximum 80

style pc_explorer_light_text is pc_explorer_text:

    color 'eee'
    hover_color 'fff'
    outlines ((absolute(.5), '333', 1, 1),)

style pc_explorer_vbox:
    spacing 5
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
