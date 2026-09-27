screen toast(message):
    zorder 100
    style_prefix 'toast'

    frame at notify_appear:
        text message

    timer 3.25 action Hide('toast')


style toast_frame:
    align (1., 1.)
    background Transform('notify', xzoom=-1)
    padding (40, 6, 10, 5)
    yoffset -135


init python hide in display:
    from renpy import store
    from renpy.exports import hide_screen, restart_interaction, show_screen
    from renpy.store import display as export


    def toast(message):
        if store._in_replay:
            return
        
        renpy.hide_screen('toast')
        renpy.show_screen('toast', message=message)
        renpy.restart_interaction()


    export.toast = toast
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
