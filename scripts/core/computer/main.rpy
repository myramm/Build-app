label pc(system):
    $ renpy.dynamic(pc=computer.Session(system))
    label pc.auth:
    call pc.login ()
    while True:
        call screen empty()
        label pc.pre:
        python hide:
            try:
                _return is True and renpy.jump('pc.quit')
                renpy.run(_return)
            except renpy.game.JumpException as e:
                renpy.scene(layer='screens')
                raise
    label pc.quit:
    return


label pc.connect(user):
    if M_jenny.get('pc_hacked'):
        $ pc.push(user)
        call pc.login ()
    else:
        call pc_hook_remote_fail
    return

label pc.disconnect():
    $ pc.pop()
    call pc.desktop ()
    return

label pc.login():
    if M_player.get('pc_know_{}_passwd'.format(pc.user)):
        show screen pc_login(auto=True)
        pause .8 + len(pc.user.passwd) * .075
        call pc.desktop ()
    else:
        show screen pc_login()
        if renpy.has_label('pc_hook_login_{}'.format(pc.user)):
            call expression 'pc_hook_login_{}'.format(pc.user)
    return

label pc.desktop():
    show screen pc_desktop()
    if renpy.has_label('pc_hook_desktop_{}'.format(pc.user)):
        call expression 'pc_hook_desktop_{}'.format(pc.user)
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
