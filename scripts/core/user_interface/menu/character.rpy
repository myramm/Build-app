screen character(c):
    modal True tag menu


    use common_menu():
        style_prefix 'character'

        side 't b c':

            frame:
                textbutton _('Back') action ShowMenu('cast')

            label _('Choose a scene to replay it, some will prompt you to choose a variant!')

            vpgrid:
                cols 5
                draggable True
                mousewheel True

                for k, unlocked in sorted(c['gallery'].items()):
                    fixed:
                        fit_first True

                        imagebutton:
                            focus_mask True
                            if unlocked:
                                idle c['gallery_image'] + k[:2] + '.png'
                                hover HoverImage(c['gallery_image'] + k[:2] + '.png')
                                action (With(fade),
                                    Function(renpy.call, "replay_INITS",
                                             c['gallery_labels'][k[:2] + '_label'],
                                             c))
                            else:
                                idle 'cookie_jar/cookie_jar_box_locked.png'
                                hover HoverImage('cookie_jar/cookie_jar_box_locked.png')
                                action ShowPopup('locked', 'scene')

                        text report_scene(c, k[:2] + '_label') or ''


style character_button is menu_button


style character_button_text is menu_button_text


style character_frame:
    margin (0, 10, 0, 20)
    xalign .5

style character_label:
    margin (0, 20, 0, 0)
    xalign .5

style character_label_text:
    size 16

style character_side:
    xfill True
    yfill True

style character_text:
    align (1., 1.)
    offset (-6, -5)
    outlines ((2, '0003', 0, 0), (1, '000', 0, 0))

style character_vpgrid:
    spacing 15
    xalign .5
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
