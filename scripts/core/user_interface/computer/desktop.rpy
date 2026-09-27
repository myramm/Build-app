screen pc_desktop():
    tag pc
    sensitive renpy.get_mode() == 'screen'

    use pc_monitor():

        frame:
            add 'pc_wallpaper_[pc.user]'
            use pc_explorer(8, 4, pc.apps.root, layout='cols', style='light') id 'pc_apps'

        draggroup as wmgr:
            xpos -90
            xysize (1024, 643)

            $ wmgr.z_serial = pc.tmp.z.max

            for app in pc.apps:
                use expression app.screen pass (app)

        button:
            style_prefix 'pc_taskbar'
            action NullAction()
            has side 'l r'

            imagebutton:
                if len(pc.stack) > 1:
                    action Return(Call('pc.disconnect'))
                    idle 'pc_sys_quit_idle'
                    hover 'pc_sys_quit_over'
                else:
                    action Return()
                    idle 'pc_sys_halt_idle'
                    hover 'pc_sys_halt_over'

            hbox:
                add 'pc_tray_wifi' yalign .5
                add 'pc_tray_volume' yalign .5


style pc_taskbar_button:
    background '#fff7'
    padding (10, 2)
    xfill True
    yalign 1.

style pc_taskbar_hbox:
    align (1., .5)
    spacing 10

style pc_taskbar_side:
    xfill True
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
