screen pc_login(auto=False):
    tag pc
    sensitive not auto and renpy.get_mode() == 'screen'

    default passwd = ''
    default warn = False

    if auto:
        for i in xrange(1, len(pc.user.passwd) + 1):
            timer i * .075 action SetScreenVariable('passwd', pc.user.passwd[:i])

    if warn:
        timer .275 action SetScreenVariable('warn', False)

    use pc_monitor():
        style_prefix 'pc_login'
        add 'pc_login_[pc.user]'

        vbox:
            add 'pc_avatar_[pc.user]':
                xalign .5

            text pc.user.name:
                style_suffix 'username_text'

            null height 20

            side 'l c b r':
                label _('PASSWORD:')

                frame:
                    style_prefix 'pc_login_text_input'
                    if warn:
                        background '#f777'
                    input:
                        pixel_width 280
                        value computer.login.ScreenVariableUpperInputValue('passwd')

                hbox:
                    text _('Password hint:')
                    text pc.user.hint

                textbutton '\u25ba':
                    action If(passwd.lower() == pc.user.passwd,
                              Return((pc.user.auth, Call('pc.desktop'))),
                              SetScreenVariable('warn', True))
                    keysym 'input_enter'

        imagebutton:
            action Return()
            hover 'pc_sys_exit_over'
            idle 'pc_sys_exit_idle'


init python in computer.login:
    from renpy.store import ScreenVariableInputValue


    class ScreenVariableUpperInputValue(ScreenVariableInputValue):
        def set_text(self, s):
            super(self.__class__, self).set_text(s.strip().upper())


style pc_login_button:
    yalign .5

style pc_login_button_text:
    font 'fonts/liberationsans-symbol.ttf'
    size 18

style pc_login_hbox:
    spacing 5

style pc_login_image_button:
    align (.025, .95)

style pc_login_label:
    align (1., .5)

style pc_login_side:
    spacing 10
    xalign .5

style pc_login_text_input_frame:
    background '#fff7'
    xmaximum 300

style pc_login_text_input_input:
    color '333'
    yalign .5

style pc_login_username_text:
    align (.5, .3)
    bold True
    size 16

style pc_login_vbox:
    spacing 20
    xalign .5
    ypos .135
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
