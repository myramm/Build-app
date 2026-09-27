label dealership_office_dialogue:

    $ game.main()
    return


label dealership_office_cell:
    jump sato_button_dialogue


label dealership_office_vest:
    if M_anon.is_state(S_ano09_vest):
        call ano09_vest_dealership_office_vest
        $ player.get_item('vest')
        call popup ('give', 'vest')
        $ M_anon.trigger(T_ano09_vest)
    else:
        call dealership_office_vest_dialogue

    $ game.main()
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
