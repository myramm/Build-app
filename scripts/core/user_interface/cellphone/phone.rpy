screen phone(app='main', *args):
    imagebutton:
        idle 'clear'
        action Hide('phone'), Jump('cellphone_exit')

    button:
        action NullAction()
        align (.5, .8)

        has frame
        style_prefix 'phone'

        if app != 'main':
            imagebutton:
                idle 'phone_back_idle'
                hover 'phone_back_over'
                pos (10, 10)
                action Show('phone', None, 'main')

        frame:
            style_prefix 'phone_battery'
            has hbox
            for i in xrange(3 - game.timer._tod):
                add 'phone_battery_chunk'

        imagebutton:
            idle 'phone_wifi'
            pos (52, -4)
            action If(persistent.skip_debug_menu_popup,
                      Show('debug_menu', None, 'general'),
                      Show('debug_menu_popup'))

        use expression 'phone_app_{}'.format(app) pass (*args)


screen phone_app_main():
    vbox:
        style_prefix 'phone_app'

        text _('My Phone')

        grid 3 2:
            style_prefix 'phone_menu'

            imagebutton:
                idle 'phone_app_goals_idle'
                hover 'phone_app_goals_over'
                action Show('phone', None, 'goals')
            imagebutton:
                idle 'phone_app_stats_idle'
                hover 'phone_app_stats_over'
                action Show('phone', None, 'stats')
            imagebutton:
                idle 'phone_app_texts_idle'
                hover 'phone_app_texts_over'
                action Show('phone', None, 'texts'), Function(phone.read)
            add 'phone_app_photo'
            imagebutton:
                idle 'phone_app_feats_idle'
                hover 'phone_app_feats_over'
                action Show('phone', None, 'feats'), Function(phone.seen)
            add 'phone_app_codex'


screen phone_app_feats():
    default data = phone.feats(persistent.achievements)

    vbox:
        style_prefix 'phone_app'

        text _('Achievements')

        label __('{} OF {} UNLOCKED').format(data.count, data.total) style 'phone_feats_label'

        add 'phone_feats_line':
            xalign .5

        frame:
            style_prefix 'phone_feats'

            has vpgrid
            cols 1
            draggable True
            mousewheel True
            yinitial 0.

            for icon, desc in data.feats:
                hbox:
                    add icon:
                        subpixel True
                        yalign .5
                    text desc


screen phone_app_goals():
    vbox:
        style_prefix 'phone_app'

        text _('Goal Tracker')

        frame:
            style_prefix 'phone_goals'

            has vpgrid
            cols 1
            draggable True
            mousewheel True
            yinitial 0.

            for icon, hint in phone.goals(machines):
                hbox:
                    add icon:
                        subpixel True
                        yalign .5
                        zoom .5
                    text renpy.filter_text_tags(hint, allow=())


screen phone_app_stats():
    vbox:
        style_prefix 'phone_app'

        text _('Stats Tracker')

        add 'phone_stats_image':
            xalign .5

        add phone.CellPhoneStatsApp(player.stats):
            xalign .5
            yoffset -10


screen phone_app_texts(message=None):
    vbox:
        style_prefix 'phone_app'

        text _('Text Messaging')

        if message:
            use phone_app_texts_view(message)
        else:
            use phone_app_texts_list()


screen phone_app_texts_list():
    style_prefix 'phone_texts'

    frame:
        has vpgrid
        cols 1
        draggable True
        mousewheel True
        yinitial 1.

        for m in phone.texts(player.messages):
            button:
                action Show('phone', None, 'texts', m)
                has vbox
                text m.sender color '777'
                text m.preview


screen phone_app_texts_view(message):
    style_prefix 'phone_texts_view'

    frame:
        add message.disp:
            xoffset -6

        label renpy.substitute(_('[sender] is texting you...'), message)
        text message.content
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
