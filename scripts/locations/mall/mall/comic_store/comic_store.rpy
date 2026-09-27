label comic_store_dialogue:
    $ player.go_to(L_comicstore)

    if M_june.is_state(S_june_cosplay_ready):
        call expression game.dialog_select("comic_store_june_cosplay_started")

    elif M_erik.is_state(S_erik_vr_needed):
        call expression game.dialog_select("comic_store_erik_vr_needed")

    elif L_comicstore.first_visit:
        call expression game.dialog_select("comic_store_first_visit")
        $ L_comicstore.visited()

    $ game.main()

label comic_store_jenny_buy_mask_callback:
    $ renpy.scene(layer='screens')
    call expression game.dialog_select("comic_store_bought_cyclone_mask")
    $ M_jenny.trigger(T_jenny_bought_mask)
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
