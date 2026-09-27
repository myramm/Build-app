screen popup_generic():
    style_prefix 'popup'
    frame:
        transclude


style popup_button is menu_button


style popup_button_text is menu_button_text


style popup_label_text:
    size 20

style popup_frame:
    align (.5, .5)
    background 'menu_frame'
    padding (30, 30)
    xsize 500

style popup_vbox:
    spacing 10
    xfill True
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
