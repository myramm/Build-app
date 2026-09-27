label mayor_rumps_kitchen_dialogue:

    if M_anon.is_state(S_ano18_yell):
        call ano18_yell_rump_kitchen
        $ M_anon.trigger(T_ano18_yell)

    $ game.main()
    return


label rump_kitchen_cabinet:
    show screen rump_kitchen_cabinet()

    if M_iwanka.is_state(S_iwa01_find):
        call iwa01_find_cabinet
    elif not M_iwanka.finished_state(S_iwa01_find):
        call rump_kitchen_cabinet_dialogue
    else:
        $ _return = None

    while not _return:
        call screen empty()

        if M_iwanka.is_state(S_iwa01_find):
            if _return == 'uniform':
                $ player.get_item('maid_uniform')
                call popup ('give', 'maid_uniform')
                $ M_iwanka.trigger(T_iwa01_find)
            else:
                call iwa01_find_cabinet.hint
        else:
            if _return == 'uniform':
                call rump_kitchen_cabinet_dialogue.uniform

    hide screen rump_kitchen_cabinet

    $ game.main()
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
