screen pc_app_camslut(app):
    style_prefix 'app_slut'

    $ app.tmp.init(vids=False)

    use pc_window(app, base='#990000c0'):
        frame:
            style 'app_slut_main_frame'

            has side 'l c'
            hbox:
                frame:
                    has vbox
                    text _('xX-HOTKITTY69-Xx') bold True xalign .5
                    add 'pc_camslut_avatar'
                    text _('{image=pc_emoji_offline} OFFLINE') xalign .5
                    text _('Rating: ( {image=pc_emoji_star}{image=pc_emoji_star}{image=pc_emoji_star}{image=pc_emoji_star}{image=pc_emoji_star_half} )') xalign .5
                    null height 15
                    text _('Sex: Female')
                    text _('Age: 24')
                    text _('Cup Size: E')
                    text _('Hair: Dark Brown')
                    text _('Eyes: Gray')
                add Solid('5f0000', xsize=1)
            frame:
                has vbox
                button:
                    hover_background 'pc_camslut_button_over'
                    idle_background 'pc_camslut_button_idle'
                    selected_background 'pc_camslut_button_live'
                    selected_hover_background 'pc_camslut_button_over'
                    hbox:
                        add 'pc_camslut_webcam' yoffset 1
                        null width 15
                        text _('Videos') style_suffix 'button_text'
                    action (SelectedIf(app.tmp.vids),
                        Return((app.tmp.set('vids', not app.tmp.vids),
                                If(not app.tmp.vids,
                                   Call('pc_hook_camslut_vids')))))
                null height 10
                frame:
                    style 'app_slut_content_frame'
                    if app.tmp.vids:
                        grid 2 2:
                            for video in M_jenny.get('videos'):
                                imagebutton:
                                    idle 'pc_camslut_video_' + video + '_idle'
                                    hover 'pc_camslut_video_' + video + '_over'
                                    action Return(Call('pc_hook_camshow', video))
                            for i in xrange(0, 2 * 2 - len(M_jenny.get('videos'))):
                                null
                    else:
                        vbox:
                            text _('Hiiii!!... My name is HOTKITTY and I provide a premium {image=pc_emoji_star_cluster} cam service!! {image=pc_emoji_lips}')
                            null
                            text _('I am a beautiful 24 year old goddess with a killer body, amazing set of {image=pc_emoji_heart}{image=pc_emoji_heart}{image=pc_emoji_heart} and I love to play with my toyzzz!! LOL!')
                            null
                            text _('Here\'s a list of things I like to do in my live shows:')
                            text _('- Strip\n- Toys\n- Masturbation\n- Do requests on donations! {color=fdc016}$$${/color}')
                            null height 5
                            text _('For the generous Daddies out there, you can PM to send me private gifts!!!! See you soooon! xoxo')


style app_slut_button:
    padding (12, 5, 12, 6)
    xalign .5
    ysize 39

style app_slut_button_text:
    size 18
    yanchor .5
    ypos .6

style app_slut_content_frame:
    background '#f776'
    padding (10, 10)
    xfill True
    yminimum 315

style app_slut_frame:
    margin (20, 0)

style app_slut_grid:
    spacing 10

style app_slut_image_button:
    xalign .5

style app_slut_main_frame:
    padding (0, 20)
    xsize 600

style app_slut_text:
    outlines ((1, '0003', .5, .5),)

style app_slut_vbox:
    first_spacing 10
    spacing 5
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
