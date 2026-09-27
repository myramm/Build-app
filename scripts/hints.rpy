screen changelog_hints():
    modal True tag popup

    zorder 100

    default spoiler = False

    key 'dismiss' action Hide('popup')

    add 'menu_background' alpha .6

    use popup_generic():
        style_prefix 'popup'

        vbox:
            spacing 0

            if spoiler:
                label _('[config.version] Spoilers')

                null height 15

                text "Iwanka" bold True color character.iwanka.who_args['color']
                null height 5
                text _("Extra position and sex dialogue for her existing scene. Complete her arc, then speak to her.")
                null height 12

                text "Kim" bold True color character.yoyo.who_args['color']
                null height 5
                text _("New micro event and scene. Speak to her in the deslership showroom to start the event.")
                null height 12

                text "Liu" bold True color character.liu.who_args['color']
                null height 5
                text _("Extra position and sex dialogue for her bedroom scene. Trigger it by talking to her in her apartment.")
                null height 12

                text "Melonia" bold True color character.melonia.who_args['color']
                null height 5
                text _("Extra position and sex dialogue for her bedroom scene. Slight variances pre and post the Mayor's arrest too.")
                null height 12

                text "Melonia" bold True color character.melonia.who_args['color']
                null height 5
                text _("A second extra position accessed via the one above. Plus unique lead-out dialogue for both of these positions.")
                null height 12

                text "Odette" bold True color character.odette.who_args['color']
                null height 5
                text _("Extra position and sex dialogue for her crypt scene. Speak to her to find out when she'll next be there.")
                null height 12

                text "Tina" bold True color character.tina.who_args['color']
                null height 5
                text _("Extra position and sex dialogue for her apartment scene. Set it up by speaking to her in the bank earlier in the day.")
                null height 12

            else:
                label _('[config.version] Hints')

                null height 15

                text "Iwanka" bold True color character.iwanka.who_args['color']
                null height 5
                text _("Be it on the yacht, or in her bedroom, Iwanka's finally ready to get back in the saddle and go for a ride.")
                null height 12

                text "Kim" bold True color character.yoyo.who_args['color']
                null height 5
                text _("She has ways of making you talk. Though, perhaps somewhat ironically, it all starts with you going to talk to her.")
                null height 12

                text "Liu" bold True color character.liu.who_args['color']
                null height 5
                text _("She was always positionally bold in the bedroom, so it's about time she was able to catch a breather now and then.")
                null height 12

                text "Melonia" bold True color character.melonia.who_args['color']
                null height 5
                text _("Finally bringing her kink to bare (pun absolutely intended) in the bedroom. Un-PC doesn't quite do her justice. D:")
                null height 12

                text "Melonia" bold True color character.melonia.who_args['color']
                null height 5
                text _("Oh, put a-- Actually, on second thought, a sock really isn't going to do it. {i}Builds on the scene above.{/i}")
                null height 12

                text "Odette" bold True color character.odette.who_args['color']
                null height 5
                text _("It always felt like there ought to be a little more action in the crypt. No. Stahp. It's not Eve. ¬_¬")
                null height 12

                text "Tina" bold True color character.tina.who_args['color']
                null height 5
                text _("She's used to being in control, so Anon wanting to switch things up in her apartment catches her off guard.")
                null height 12

            null height 20
            text _("* {i}Some content requires scenes to be played twice.{/i}")
            null height 35

            textbutton (_('Not cryptic enough') if spoiler else _('Less cryptic')):
                action ToggleScreenVariable('spoiler')
                text_size 16
                xsize 240
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
