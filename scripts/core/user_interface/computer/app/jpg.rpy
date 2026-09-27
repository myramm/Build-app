screen pc_app_jpg(app):
    use pc_window(app, title=__(app.title) + '.jpg'):
        add 'pc_image_[app.args[0]]'
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
