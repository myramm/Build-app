label jab_button_dialogue:
    if M_anon.is_state(S_ano27_init):
        scene expression background()
        show screen popup_finale() with dissolve
        call screen empty()
        hide screen popup_finale with dissolve
        if not _return:
            jump jab_button_dialogue.skip

    call jab_button_stage

    if M_anon.is_state(S_ano27_init):
        call ano27_init_jab
        $ player.remove_item('case')
        $ M_anon.trigger(T_ano27_init)

    elif M_anon.is_state(S_ano27_jabb):
        call ano27_jabb_jab
        $ M_anon.trigger(T_ano27_jabb)

    elif M_anon.is_state(S_ano27_peek, S_ano27_yolo):
        call ano27_peek_jab
    else:

        call jab_button_cargo
        if _return == 'escape':
            $ player.go_to(L_warehouse_depot)

    label jab_button_dialogue.skip:
    $ game.main()
    return


label jab_button_stage:
    if L_warehouse_cargo.is_here(M_jab):
        scene expression background(304, 368, 4) as stage
        show thug b_dressed_leaning
    else:
        scene expression player.location.background_blur as stage
        show thug
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
