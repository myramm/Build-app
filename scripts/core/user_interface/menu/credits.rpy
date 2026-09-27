screen credits():
    modal True tag menu


    default scroll = credits.adjustment()

    on 'replace' action Play('music', '<loop 241.5>audio/music_credits.ogg',
                             fadein=.7, fadeout=.7, if_changed=True)

    use common_menu():
        style_prefix 'credits'

        vbox:
            grid 2 1:
                style_prefix 'creator_credit'
                label _('Owner & Creator')
                text 'DarkCookie'

            null height 20

            grid 2 1:
                for column in credits.team:
                    grid 2 len(column):
                        style_prefix 'credit'
                        for name, role in column:
                            label role
                            text name

            null height 10

            hbox:
                style_prefix 'ex_credit'
                label _('Former Staff')
                null width 10
                for ex in credits.ex[:-1]:
                    text ex
                    label ','
                    null width 5
                label 'and'
                null width 5
                text credits.ex[-1]

            null height 5

            hbox:
                style_prefix 'qa_credit'
                label _('QA Testers')
                null width 10
                for qa in credits.qa[:-1]:
                    text qa
                    label ','
                    null width 5
                label 'and'
                null width 5
                text credits.qa[-1]

            null height 20

            label _('Special thanks to all our key pledging contributors!')

            null height 10

            side 'c b':
                fixed:
                    style_prefix 'pledge'
                    viewport:
                        draggable True
                        mousewheel True
                        edgescroll (20, 20, credits.sign)
                        yadjustment scroll
                        text credits.pledges
                    if scroll.value > 0:
                        textbutton '\u25b2':
                            action Function(scroll.pgup)
                    if scroll.value < scroll.range:
                        textbutton '\u25bc':
                            action Function(scroll.pgdn)
                            yalign 1.


                side 'l r':
                    textbutton _('Back') action Return()
                    textbutton _('About') action ShowMenu('about')


style creator_credit_label_text:
    size 18

style creator_credit_text take creator_credit_label_text


style credit_grid:
    xalign .5
    xspacing 10
    yspacing 5

style credit_hbox:
    xalign .5

style credit_label:
    xalign 1.

style credit_label_text is credits_label_text


style credit_text:
    bold True
    color '3598db'

style credits_button is menu_button


style credits_button_text is menu_button_text


style credits_grid:
    spacing 30
    xalign .5

style credits_label:
    xalign .5

style credits_label_text:
    color '9098a3'
    italic True

style credits_side:
    spacing 20
    xfill True

style pledge_button:
    hover_background '#54555c77'
    idle_background '#3b3d4577'
    xfill True
    ysize 20

style pledge_button_text:
    align (.5, .5)

style pledge_text:
    font credits.font
    language 'western'
    line_spacing 1
    text_align .5

style ex_credit_text:
    color '144c72'

style qa_credit_text:
    color '9b59b6'
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
