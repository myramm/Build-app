screen popup_money(value, message):
    on 'hide' action Play('audio', random.choice((audio.coins1, audio.coins2)))

    use popup_generic():
        style_prefix 'money_popup'

        vbox:

            label _('You have gained some {=money_keyword}MONEY{/}!')

            frame:
                yminimum 125
                has grid 2 1
                text '[value]' style_suffix 'value_text'
                add 'popup_money' yalign .5

            text message

    key 'dismiss' action Hide('popup')


style money_keyword:
    color '65cd26'


style money_popup_frame is default:

    xalign .5

style money_popup_label:
    xalign .5

style money_popup_grid:
    align (.5, .5)
    spacing 10

style money_popup_text:
    size 16
    xalign .5

style money_popup_value_text:
    bold True
    size 30
    align (1., .5)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
