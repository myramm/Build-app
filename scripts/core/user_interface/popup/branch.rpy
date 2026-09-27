screen popup_branch():
    modal True tag popup

    zorder 100

    side 'c t':
        style_prefix 'branch_popup'

        use popup_warning():
            text _('Story branches in {b}Summertime Saga{/b} allow choices to impact a character\'s progression!')
            text _('This is one of those moments, choose wisely!')
            null height 5
            hbox:
                textbutton _('Go Back') action Return(False)
                textbutton _('Continue') action Return(True)

        frame:
            style_prefix 'branch_popup_hint'
            text _('Remember to save!')


style branch_popup_button:
    xysize (130, 50)

style branch_popup_button_text:
    bold True
    size 14

style branch_popup_hbox:
    spacing 100
    xalign .5

style branch_popup_hint_frame:
    background 'popup_hint'
    padding (12, 12, 130, 20)
    xalign .8
    yoffset 2
    ysize 52

style branch_popup_hint_text:
    bold True
    outlines ((1, '000', 0, 0),)
    yalign .5

style branch_popup_side:
    align (.5, .5)
    yoffset -26


label popup_branch(action):
    call screen popup_branch
    python:
        if not _return:
            game.main()
        renpy.run(action)
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
