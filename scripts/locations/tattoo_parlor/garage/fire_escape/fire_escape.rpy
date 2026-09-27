label tattoo_parlor_fire_escape_dialogue:
    if M_eve.is_state(S_eve_visit_roof) and game.timer.is_evening():
        call expression game.dialog_select("tattoo_parlor_fireescape_eve_visit_roof")
        $ M_eve.trigger(T_eve_visited_roof)
    elif M_eve.is_state(S_eve_party_speak_to_jenny, S_eve_party_speak_to_odette):
        call expression game.dialog_select("tattoo_parlor_fire_escape_party_up_to_roof")
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
