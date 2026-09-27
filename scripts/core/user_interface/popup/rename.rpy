screen popup_rename(ref, current):
    modal True tag popup

    zorder 100

    default name = current
    default color = renpy.eval_who(ref, True).who_args.get('color', 'fefefe')

    use popup_generic():
        style_prefix 'rename_popup'

        side 'r c':

            add 'popup_name_[ref]'

            vbox:
                text _('Choose a name for:')

                null height 5

                frame:
                    style_prefix 'rename_popup_text_input'
                    input:
                        allow ('abcdefghijklmnopqrstuvwxyz'
                           'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
                           '0123456789 ')
                        color color
                        copypaste True
                        length 12
                        value ScreenVariableInputValue('name')

                null height 15

                textbutton _('Continue'):
                    action Return(name.strip())
                    keysym 'input_enter'
                    sensitive name.strip()


style rename_popup_button:
    xysize (170, 50)

style rename_popup_text_input_input:
    size 20

style rename_popup_side:
    spacing 20

style rename_popup_text:
    size 16
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
