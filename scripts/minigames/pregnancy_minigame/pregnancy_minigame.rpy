label call_pregnancy_minigame(return_label, machine):
    if player.pregnancy_chance > 0 and not machine.pregnancy.is_pregnant and machine.get('fertile', True):

        if not persistent.seen_warning_pregnancy:
            show screen popup_pregnancy
            $ persistent.seen_warning_pregnancy = True

        show screen pregnancy_minigame(int(
            (player.pregnancy_chance + player.counter_pregnancy_tries / 100.) *
            machine.pregnancy.chance * 100))
        with fade
        call screen empty()
        hide screen pregnancy_minigame

        if _return:
            $ machine.pregnancy.get_pregnant()
            $ player.counter_pregnancy_tries = 0

            scene pregnancy_minigame_02 onlayer screens
            with flash
            pause
            hide pregnancy_minigame_02 onlayer screens
        else:

            $ player.counter_pregnancy_tries += 1

            scene pregnancy_minigame_03 onlayer screens
            with hpunch
            pause
            hide pregnancy_minigame_03 onlayer screens

    if return_label:
        jump expression return_label

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
