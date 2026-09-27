screen popup_notice(message, caption, disp):
    use popup_generic():
        style_prefix 'notice_popup'

        vbox:

            label message

            frame:
                minimum (300, 125)
                has transform
                maxsize (300, 125)
                frame:
                    minimum (300, 125)
                    add disp align .5, .5

            text caption

    key 'dismiss' action Hide('popup')


style keyword:
    bold True
    size 17


style notice_popup_frame is default:

    align (.5, .5)

style notice_popup_label:
    xalign .5

style notice_popup_text:
    size 16
    xalign .5
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
