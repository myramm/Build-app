screen mode():
    modal True tag menu


    default opts = 2 + (firstname != 'PUBLICSAVE')

    use common_menu():
        style_prefix 'mode'

        vbox:

            label _('Choose an option:')

            grid opts 1:
                style_prefix 'modes'
                frame:
                    has vbox
                    textbutton _('Clean Game') action Start('start_clean')
                    text _('For new players\n(who want to play)')
                    text _('Start from scratch')
                    text _('Start with $20')
                    text _('Start with zero stats')

                frame:
                    has vbox
                    textbutton _('Cheats Enabled') action Start('start_cheat')
                    text _('For returning players\n(who want to fap)')
                    text _('Skippable mini-games')
                    text _('Start with lots of money')
                    text _('Start with max stats')

                if opts > 2:
                    frame:
                        has vbox
                        textbutton _('New Content') action StartRecap()
                        text _('For returning players\n(who know the story)')
                        text _('Skip to new content')
                        text _('Start with some savings')
                        text _('Start with some stats')

            text _('*** This option will only be available during alpha development ***')


style mode_label:
    xalign .5

style mode_label_text:
    size 20

style mode_text:
    color '8b94aa'
    size 16
    xalign .5

style mode_vbox:
    align (.5, .5)
    spacing 50

style modes_button is menu_button


style modes_button_text is menu_button_text


style modes_frame is menu_frame:

    padding (35, 35)
    xminimum 250

style modes_grid:
    spacing 35

style modes_text:
    color 'ccc'
    size 16
    text_align .5
    xalign .5

style modes_vbox:
    spacing 25
    xalign .5
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
