image popup_eve_bulge_idle = 'popup_eve_bulge'
image popup_eve_bulge_over = im.MatrixColor('popups/popup_eve_bulge.png', over)
image popup_eve_vagina_idle = 'popup_eve_vagina'
image popup_eve_vagina_over = im.MatrixColor('popups/popup_eve_vagina.png', over)


screen popup_trap():
    modal True tag popup

    zorder 100

    frame:
        style_prefix 'trap_popup'

        has vbox
        label _('What are you hoping to see in {=trap_keyword}EVE\'S PANTIES{/}?')
        text _('This choice can only be made {b}once{/b} per play-through!')
        hbox:
            imagebutton:
                idle 'popup_eve_bulge_idle'
                hover 'popup_eve_bulge_over'
                action Return(True)
            imagebutton:
                idle 'popup_eve_vagina_idle'
                hover 'popup_eve_vagina_over'
                action Return(False)
        null height 10


style trap_keyword:
    color '758ab8'


style trap_popup_frame:
    padding (50, 50)
    xsize 800

style trap_popup_label:
    xalign .5

style trap_popup_hbox:
    spacing 125
    xalign .5

style trap_popup_text:
    color 'e66b80'
    size 17
    xalign .5

style trap_popup_vbox:
    spacing 30
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
