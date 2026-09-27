label tattoo_parlor_roof_dialogue:
    if M_eve.is_state(S_eve_party_speak_to_jenny):
        call expression game.dialog_select("tattoo_parlor_roof_eve_party_speak_to_jenny")
        $ M_eve.get_state().change_description("{b}[jen_name]{/b} is here at the party! I should talk to her.")
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
