screen pc_app_saga(app):
    style_prefix 'app_saga'

    $ app.tmp.init(step=1)

    use pc_window(app):
        frame:

            if app.tmp.step == 1:
                add 'pc_saga_splash'

            if app.tmp.step == 2:
                add 'pc_saga_menu'
                timer 24. action Return(app.tmp.set('step', 6))

            if app.tmp.step == 6:
                add 'pc_saga_menu_static'

            if app.tmp.step == 3:
                viewport:
                    if app.focused:
                        edgescroll (150, 500)
                    add 'pc_saga_bedroom'

            if app.tmp.step == 4:
                add 'pc_saga_ex'

            imagebutton:
                idle 'clear'
                action Return((app.tmp.set('step', app.tmp.step % 4 + 1),
                           If(app.tmp.step == 3, Call('pc_hook_saga_ex'))))


style app_saga_frame:
    xysize (512, 336)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
