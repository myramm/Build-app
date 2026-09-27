

screen quick_menu():

    zorder 100

    if quick_menu:

        hbox:
            style_prefix 'quick'

            textbutton _('Hide') action HideInterface()


            textbutton _('Skip') action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _('Auto') action Preference('auto-forward', 'toggle')
            textbutton _('Save') action ShowMenu('save')
            textbutton _('Q.Save') action QuickSave()
            textbutton _('Q.Load') action QuickLoad()
            textbutton _('Prefs') action ShowMenu('preferences')


init python:
    config.overlay_screens.append('quick_menu')


default quick_menu = True


style quick_hbox:
    align (.5, 1.)

style quick_button:
    padding (8, 4, 8, 0)

style quick_button_text:
    hover_color '66c1e0'
    idle_color 'aaa'
    insensitive_color '8888'
    selected_color '09c'
    size 12

style quick_hbox:
    variant 'touch'
    spacing 15
    xalign 1.
    xoffset -62

style quick_button_text:
    variant 'touch'
    size 17
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
