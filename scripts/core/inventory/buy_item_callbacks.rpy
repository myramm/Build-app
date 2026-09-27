init python:
    def bug_spray_callback(already_owned=False):
        if M_diane.is_state(S_diane_get_bug_spray):
            renpy.scene(layer='screens')
            if already_owned:
                renpy.jump('consumr_diane_buy_bug_spray_owned')
            else:
                renpy.jump('consumr_diane_buy_bug_spray_brought')

    def milk_jug_callback(already_owned=False):
        if M_diane.is_state(S_diane_buy_milk_jug):
            renpy.scene(layer='screens')
            if already_owned:
                renpy.jump('consumr_diane_get_milk_jug_owned')
            else:
                renpy.jump('consumr_diane_get_milk_jug_bought')

    def candle_callback(already_owned=False):
        if M_eve.is_state(S_eve_make_up_go_to_mall):
            renpy.scene(layer='screens')
            if already_owned:
                renpy.jump('consumr_eve_get_candle_owned')
            else:
                renpy.jump('consumr_eve_get_candle_bought')

    def bad_monster_callback(already_owned=False):
        if M_jenny.is_state(S_jenny_buy_bad_monster):
            renpy.call('bad_monster_callback')

    def ccot_callback():
        M_erik.trigger(T_erik_card_acquired)

    def cyclone_mask_callback():
        if M_jenny.is_state(S_jenny_buy_mask):
            renpy.call('comic_store_jenny_buy_mask_callback')

    def sea_dogs_saga_callback():
        M_kevin.trigger(T_kevin_bought_seadogs)

    def virtualsaga_callback():
        M_erik.trigger(T_erik_vr_bought_headset)

    def world_of_orcette_callback():
        M_erik.trigger(T_erik_vr_bought_game)

    def orc_cosplay_callback():
        M_june.trigger(T_june_cosplay_bought)

    def cupid_chocolates_callback():
        if M_eve.is_state(S_eve_make_up_go_to_mall):
            renpy.scene(layer='screens')
            renpy.jump("cupid_store_bought_chocolates_eve_callback")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
