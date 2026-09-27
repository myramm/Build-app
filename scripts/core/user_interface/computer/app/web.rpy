screen pc_app_web(app):
    style_prefix 'app_web'

    use pc_window(app, ' - '.join((__(app.title), __('Internet Sexplorer')))):
        side 't c':

            vbox:
                style_prefix 'app_web_url'

                frame:
                    text app.tmp.host + app.tmp.path

                add Solid('333', ysize=1)

            frame:
                if app:
                    transclude


style app_web_frame:
    margin (10, 10, 10, 0)

style app_web_url_frame:
    background 'pc_web_url'
    margin (20, 5, 60, 5)
    padding (63, 3, 85, 3)
    xfill True
    ysize 40

style app_web_url_text:
    color '121212'
    yanchor renpy.BASELINE
    ypos 17

style app_web_vbox:
    spacing 10
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
