label park_douches_button_dialogue:
    if M_dewitt.is_state(S_dewitt_eve_meet_up):
        call expression game.dialog_select("park_dewitt_douches_meet_up")
        $ M_dewitt.trigger(T_dewitt_gang_deal)
    elif M_eve.is_state(S_eve_tuuku_with_douches) and game.timer.is_evening():
        if M_eve.get("talked_tuuku_douches"):
            call expression game.dialog_select("park_douches_eve_tuuku_with_douches_repeat")
        else:
            call expression game.dialog_select("park_douches_eve_tuuku_with_douches_first")
            $ M_eve.set("talked_tuuku_douches", True)

    elif player.stats.chr() < 10 and not M_park_douches.once('met'):
        call park_douches_intro
        call park_douches_battle_dialogue
    else:
        if player.stats.chr() < 10:
            call park_douches_greet
        else:
            call park_douches_respect

        menu park_douches_menu:
            "Rap battle." if player.stats.chr() < 10:
                call expression 'park_douches_rematch_{}'.format(
                    bisect.bisect((4, 7, 9), player.stats.chr()) + 1)
                call park_douches_battle_dialogue

            "Reset {color=e66f05}{b}CHR{/b}{/color} stat to play rap battles. (Cheat)" if game.cheat_mode and player.stats.chr() > 9:
                menu:
                    "This will reset the {color=e66f05}{b}charisma{/b}{/color} stat to zero to allow the rap battles to be played. {b}Are you sure?{/b}"
                    "Yes, I'm sure, take away my {color=e66f05}{b}charisma{/b}{/color}.":

                        $ player.stats._chr = 0
                        jump park_douches_button_dialogue
                    "Stop! This is not what I want!":

                        pass
            "Never mind.":

                call park_douches_dismiss

    $ game.main()


label park_douches_battle_dialogue:
    call expression 'park_douches_battle_{}'.format(player.stats.chr() + 1)

    show screen rap_battle(bisect.bisect((4, 7), player.stats.chr()))
    call screen empty() with dissolve
    hide screen rap_battle

    if _return:
        call expression 'park_douches_battle_{}_pass'.format(player.stats.chr() + 1)
        $ player.increase_chr()
        call popup ('chr', True)
        if player.stats.chr() > 9:
            $ A_eminem.unlock()
    else:
        call park_douches_battle_fail
        call popup ('chr', False)

    $ game.timer.tick()
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
