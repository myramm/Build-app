screen diary(start):
    style_prefix 'diary'

    default data = diary.pages()
    default max = len(data) - 1
    default page = start
    default zoom = renpy.mobile

    imagebutton:
        idle 'clear'
        action Return(page)
        keysym 'game_menu'

    fixed:
        if zoom:
            at Transform(anchor=(.65, .55), zoom=1.4)

        imagebutton:
            focus_mask True
            idle 'objects/closeup_diary_01.png'
            action NullAction()

        if page > 0:
            imagebutton:
                style_prefix 'diary_page'
                at flip
                xalign .01
                if zoom:
                    xpos .32
                idle 'diary_arrow_idle'
                hover 'diary_arrow_over'
                action SetScreenVariable('page', page - 1)
                keysym 'viewport_leftarrow', 'viewport_wheelup'

        if page < max:
            imagebutton:
                style_prefix 'diary_page'
                xalign .99
                idle 'diary_arrow_idle'
                hover 'diary_arrow_over'
                action SetScreenVariable('page', page + 1)
                keysym 'viewport_rightarrow', 'viewport_wheeldown'

        text str(page + 26):
            style_prefix 'diary_page'

        for i, line in enumerate(data[page]):
            text line:
                pos 527, 212 + 39 * i


style art_diary_text:
    size 25
    yoffset 28

style rt_diary_text:
    size 25
    yoffset -12

style diary_fixed:
    align (.5, .5)
    fit_first True

style diary_text:
    altruby_style style.art_diary_text
    anchor (.5, renpy.BASELINE)
    antialias True
    color '#111111'
    font 'fonts/alphabetizedcassettetapes-classic.ttf'
    layout 'nobreak'
    outlines ((absolute(1), '#1111110f', absolute(0), absolute(0)),)
    ruby_style style.rt_diary_text
    size 30
    xalign .5

style diary_page_image_button:
    focus_mask True
    yalign .55

style diary_page_text:
    anchor (.0, .85)
    color '#3336'
    kerning -1
    pos (.8675, .89)
    size 14
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
