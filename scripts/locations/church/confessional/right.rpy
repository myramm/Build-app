label church_confessional_right_dialogue:
    if M_mia.is_state(S_mia_priest_act):
        call expression game.dialog_select("confessional_right_mia_priest_act_pre")
        menu:
            "Pray?" if player.stats.chr() < 3:
                $ display.toast(chr_fail)
                call expression game.dialog_select("confessional_right_mia_priest_act_pray")

                $ M_mia.trigger(T_helen_convince_fail)

            "Change." if player.stats.chr() >= 3:
                $ display.toast(chr_pass)
                call expression game.dialog_select("confessional_right_mia_priest_act_change")
                $ M_mia.trigger(T_helen_convince_change)
                jump expression game.dialog_select("church_dialogue")
    else:

        call expression game.dialog_select("confessional_right_empty")

    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
