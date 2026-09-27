label bank_vault_dialogue:
    if M_anon.is_state(S_ano26_move):
        call ano26_move_bank_vault
        $ M_anon.trigger(T_ano26_move)

    $ game.main()
    return


label bank_vault_boxes:
    scene onlayer screens
    show screen minigame_vault()
    with fade
    call screen empty()
    hide screen minigame_vault

    if _return == 11082:
        call ano14_find_bank_vault.pass
        $ M_anon.trigger(T_ano14_find)
    else:

        call ano14_find_bank_vault.fail

    $ game.main()
    return


label bank_vault_case:
    if M_anon.is_state(S_ano26_take):
        call ano26_take_case
        call popup ('give', 'case')
        $ player.get_item('case')
        $ player.go_to(L_pizzeria_exterior)
        $ M_anon.trigger(T_ano26_take)
    else:
        call bank_vault_case_dialogue

    $ game.main()
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
