label bank_cubicle_dialogue:

    if M_tina.is_state(S_tin02_talk):
        call tin02_talk_bank_cubicle
        if _return:
            $ M_tina.set('sex', game.timer._game_day)
        $ renpy.dynamic(schedule=False)
        call tina_button_bank.choice
        $ M_tina.trigger(T_tin02_talk)

    $ game.main()
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
