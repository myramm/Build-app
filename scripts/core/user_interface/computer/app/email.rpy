screen pc_app_email(app):
    style_prefix 'app_email'

    $ app.tmp.init(open=False)

    use pc_window(app):
        frame:
            has side 't c'

            hbox:
                label _('COMPOSE')
                add 'pc_email_search'

            side 'l r c':
                vbox:
                    style_prefix 'app_email_nav'
                    textbutton _('INBOX'):
                        if app.tmp.open:
                            action Return(app.tmp.set('open', False))
                    label _('SENT')
                    label _('DRAFT')
                    label _('SPAM')
                    label _('TRASH')
                    frame:
                        add 'pc_email_contacts' align .5, .5

                add 'pc_email_scroll'

                if app.tmp.open:
                    use pc_app_email_header(pc.mail.mail[app.tmp.open]):
                        use expression 'pc_app_email_' + app.tmp.open
                else:
                    fixed:
                        style_prefix 'app_email_inbox'
                        vbox:
                            for mail in pc.mail:
                                use pc_app_email_item(app, mail)
                        text _('We reserve the right to collect and sell your data. Thank God people don\'t read this.')


screen pc_app_email_item(app, msg):
    button:
        style_prefix 'app_email_list'
        style_suffix msg.state + '_button'

        action Return((msg.read, app.tmp.set('open', msg.ref), msg.hook))

        has hbox
        add 'pc_email_[msg.state]_box' align .5, .5
        label msg.sender style_suffix 'sender_label'
        hbox:
            style_suffix 'subject_hbox'
            text msg.short
            if msg.att:
                add 'pc_email_att' align 1., .5
        label msg.date style_suffix 'date_label'


screen pc_app_email_header(msg):
    frame:
        style_prefix 'app_email_message'
        has side 't b c'
        vbox:
            frame:
                style_prefix 'app_email_header'
                has vbox
                hbox:
                    label _('from')
                    text msg.sndr
                hbox:
                    label _('subject')
                    text msg.sub bold True
            add Solid('4a6184aa', ysize=3)
        vbox:
            style_prefix 'app_email_footer'
            add Solid('4a6184aa', ysize=3)
            label _('No threats found. Inspected by Gaspersigh Anti-Virus.')
        fixed:
            transclude


screen pc_app_email_419():
    style_prefix 'mail_plain'
    frame:
        text _('Dear Beloved Friend,\n\nI know this message will come to you as a surprise but I am Prince Kaosu Uzu of Nigeria. I am presently being held captive in a cage and in need of assistance. I have many money, hidden in my palace. If you send a ransom to this adress below, my captores will release me and I will reward you with many gold, and women.\n\nAny money will do. Please send quickly!\n\n123 Starvation Lane, Shack 5\n\nBest regards,\n\nKao the best prince')

screen pc_app_email_beg():
    style_prefix 'mail_plain'
    frame:
        text _('wil pay $15 4 u 2 rite \'i <3 SS\' on thm')

screen pc_app_email_cam():
    style_prefix 'mail_camslut'
    frame:
        has side 't c'

        fixed:
            fit_first 'height'
            add 'pc_icon_cam_idle' zoom .7
            text _('"Woohoo! You just got paid!"')

        frame:
            style_prefix 'mail_camslut_body'
            has vbox

            text _('Click below to collect your monthly earnings!')
            button:
                style_prefix 'mail_camslut_earnings'
                has hbox
                label '$' text_bold True text_color 'fdc016' xsize 38
                label '445.00' xmargin 20
            text _('Your earnings will be sent from your CAMslut account to your bank!')
            text _('Thank you for using our premium service. Please contact us at support@camslut.dc if you have any issues with money transfers. Stay sexy!\n\n- CAMslut Team')

screen pc_app_email_ptv():
    style_prefix 'mail_pink'
    add 'pc_email_msg_pink'
    vbox:
        text _('*** Do not forward or share your account details.***') size 10
        label _('Subscription Number: {b}L6bv12R{/b}\nPassword: {b}12345{/b}')
        text _('Thank you for subscribing to our premium satellite service! We offer the best adult content on demand.\n\n- The Pink Team')

screen pc_app_email_toy():
    style_prefix 'mail_lewdtoys'
    add 'pc_email_msg_toy'
    vbox:
        text _('Item: Deep Blue') bold True size 16
        null height 10
        text _('The Deep Blue is part of our new glow in the dark butt plug collection!')
        null height 70
        text _('Thank you for your online purchase! All our orders can take up to 4 business days to reach their destination. If you have not received your package, please contact us at support@lewdtoys.dc.\n\n- LewdToys')
        text _('*All products have been tested on animals*') size 8 yoffset -8

screen pc_app_email_twt():
    style_prefix 'mail_plain'
    frame:
        has vbox
        text _('"Oye mami, I wanted to show you mi Pinga Latina {image=pc_emoji_wink}"')
        add 'pc_email_msg_sombrero'


style app_email_hbox:
    spacing 10

style app_email_label:
    background 'pc_email_read'
    padding (20, 8)
    ysize 34

style app_email_label_text:
    align (.5, .6)
    color '235'

style app_email_side:
    spacing 10


style app_email_inbox_fixed:
    xysize (600, 350)

style app_email_inbox_text:
    align (.5, 1.)
    color '235'
    size 10

style app_email_inbox_vbox:
    spacing 3

style app_email_frame:
    margin (10, 10)


style app_email_nav_button is app_email_nav_label:

    hover_background 'pc_email_over'
    idle_background 'pc_email_unread'

style app_email_nav_button_text is app_email_nav_label_text


style app_email_nav_frame is app_email_label:

    xpadding 10
    xysize (75, None)

style app_email_nav_label is app_email_nav_frame:

    background 'pc_email_unread'

style app_email_nav_label_text is app_email_label_text


style app_email_nav_vbox:
    spacing 3


style app_email_list_read_button:
    hover_background 'pc_email_over'
    idle_background 'pc_email_read'
    padding (14, 10)
    xfill True

style app_email_list_unread_button is app_email_list_read_button:

    hover_background 'pc_email_over'
    idle_background 'pc_email_unread'


style app_email_list_column:
    yalign .5
    yminimum 18

style app_email_list_hbox:
    spacing 10
    xfill True

style app_email_list_text:
    color '235'
    yalign .5

style app_email_list_date_label is app_email_list_column:

    xsize 70

style app_email_list_date_label_text is app_email_list_text:

    xalign 1.

style app_email_list_sender_label is app_email_list_column:

    xsize 150

style app_email_list_sender_label_text is app_email_list_text


style app_email_list_subject_hbox is app_email_list_column:

    xsize 290

style app_email_list_subject_hbox_text is app_email_list_text



style app_email_message_frame:
    background 'pc_email_unread'
    margin (0, 0)
    padding (3, 3)
    xysize (600, 350)

style app_email_message_side:
    yfill True


style app_email_footer_label:
    margin (10, 10)

style app_email_footer_label_text:
    color '235'
    size 10

style app_email_header_frame:
    ymargin 8

style app_email_header_hbox:
    spacing 8

style app_email_header_label:
    xsize 70

style app_email_header_label_text:
    color '999'
    xalign 1.

style app_email_header_text:
    color '235'

style app_email_header_vbox:
    spacing 5


style mail_plain_frame:
    margin (10, 10, 10, 0)

style mail_plain_text:
    color '235'
    size 12

style mail_plain_vbox:
    spacing 10

style mail_html_text:
    xalign .5
    size 12


style mail_camslut_earnings_button:
    background 'pc_camslut_button_idle'
    padding (3, 10)
    xalign .5

style mail_camslut_earnings_hbox:
    spacing 2

style mail_camslut_earnings_label:
    xalign .5

style mail_camslut_earnings_label_text is mail_html_text:

    outlines ((1, '9f2307', 0, 0),)
    size 14

style mail_camslut_body_frame:
    background '#d24646'
    padding (55, 10, 55, 0)
    xalign .5
    yfill True

style mail_camslut_body_text is mail_html_text


style mail_camslut_body_vbox:
    spacing 10
    xfill True

style mail_camslut_frame:
    background '#9a2727'
    padding (30, 10, 30, 0)

style mail_camslut_side:
    spacing 10
    yfill True

style mail_camslut_text:
    align (.5, .5)
    bold True


style mail_lewdtoys_text is mail_html_text


style mail_lewdtoys_vbox:
    pos (.5, .075)
    spacing 10
    xanchor .5
    xmaximum 500


style mail_pink_label:
    xalign .5

style mail_pink_label_text is mail_html_text:

    line_spacing 3
    size 14

style mail_pink_text is mail_html_text:

    color 'c45afb'

style mail_pink_vbox:
    pos (.5, .375)
    spacing 15
    xanchor .5
    xmaximum 375
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
