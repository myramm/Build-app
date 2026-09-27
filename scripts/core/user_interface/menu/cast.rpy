screen cast():
    modal True tag menu


    default cast = tuple(v for k, v in sorted(persistent.cookie_jar.items(),
                                              key=lambda k: k[0].lower()))

    use common_menu():
        style_prefix 'cast'

        side 't b c':

            frame:
                has hbox
                textbutton _('Back') action Return()
                textbutton _('Reset'):
                    action Confirm(
                    _('Are you sure you want to reset the Cookie Jar?'),
                    Function(lock_all_scenes))
                    style_suffix 'warn_button'

            label _('Choose a character to see a list of their unlocked scenes!')

            vpgrid:
                cols 9
                draggable True
                mousewheel True
                for character in cast:
                    imagebutton:
                        focus_mask True
                        if character['unlocked']:
                            idle character['idle']
                            hover HoverImage(character['idle'])
                            action ShowMenu('character', character)
                        else:
                            idle character['locked_idle']
                            hover HoverImage(character['locked_idle'])
                            action ShowPopup('locked', 'character')


style cast_button is menu_button


style cast_button_text is menu_button_text


style cast_frame:
    margin (0, 10, 0, 20)
    xalign .5

style cast_hbox:
    spacing 150
    xalign .5

style cast_label:
    margin (0, 20, 0, 0)
    xalign .5

style cast_label_text:
    size 16

style cast_side:
    xfill True
    yfill True

style cast_vpgrid:
    align (.5, .5)
    xspacing 10
    yspacing 15

style cast_warn_button:
    xalign 1.
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
