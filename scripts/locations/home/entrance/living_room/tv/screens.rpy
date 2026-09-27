screen tv(chan=0):
    sensitive renpy.get_mode() == 'screen'

    default prg = chan

    $ prgdn = (prg - 1) % 8
    $ prgup = (prg + 1) % 8

    imagebutton:
        focus_mask True
        pos 398, 636
        idle 'tv_onoff_idle'
        hover 'tv_onoff_over'
        action Return(True)

    imagebutton:
        focus_mask True
        pos 393, 678
        idle 'tv_prgdn_idle'
        hover 'tv_prgdn_over'
        action Return((SetLocalVariable('prg', prgdn),
                       Call('tv_switch', prgdn)))

    imagebutton:
        focus_mask True
        pos 554, 679
        idle 'tv_prgup_idle'
        hover 'tv_prgup_over'
        action Return((SetLocalVariable('prg', prgup),
                       Call('tv_switch', prgup)))


screen tv_auth():
    sensitive renpy.get_mode() == 'screen'
    style_prefix 'tv_auth'
    zorder -1

    default active = None
    default account = ''
    default passwd = ''

    if active is not None:
        imagebutton:
            idle 'clear'
            action SetScreenVariable('active', None)

    button:
        ypos 327

        if active == 'account':
            action NullAction()
            key_events True
            input:
                allow ' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
                copypaste True
                pixel_width 262
                value ScreenVariableInputValue('account')
        else:
            action SetScreenVariable('active', 'account')
            keysym 'toggle_skip'
            text account

    button:
        ypos 399

        if active == 'passwd':
            action NullAction()
            key_events True
            input:
                allow ' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
                copypaste True
                pixel_width 262
                value ScreenVariableInputValue('passwd')
        else:
            action SetScreenVariable('active', 'passwd')
            keysym 'toggle_skip'
            text passwd

    imagebutton:
        idle 'buttons/enter_01.png'
        hover im.MatrixColor('buttons/enter_01.png', over)
        pos (460, 445)
        action If(account == 'L6bv12R' and passwd == '12345',
                  Return(Call('tv_auth')),
                  Return((SetLocalVariable('passwd', ''),
                          SetLocalVariable('active', None),
                          Call('tv_auth_fail'))))
        keysym 'input_enter'


style tv_auth_button:
    padding (4, 4)
    xpos 390
    xsize 270

style tv_auth_input:
    color 'ff4bdf'
    size 16

style tv_auth_text is tv_auth_input
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
