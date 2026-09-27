screen pc_monitor():
    style_prefix 'pc_monitor'

    frame:
        transclude

    imagebutton:
        idle 'pc_monitor_[pc.system]'
        focus_mask 'pc_monitor'
        action NullAction()

    if pc.system == 'anon':
        imagebutton:
            idle 'pc_sticky_idle'
            hover 'pc_sticky_over'
            pos 824, 657
            if not M_player.get('pc_know_anon_passwd'):
                action Return((pc.user.auth, Jump('pc.auth')))


style pc_monitor_frame:
    margin (90, 125, 90, 115)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
