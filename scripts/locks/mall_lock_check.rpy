label mall_lock_check:
    scene expression player.location.background_blur

    if game.timer.is_night() and destination != L_mall_parking_lot:
        show player 10 with dissolve
        player_name "( It's pretty late, I should be getting home. )"

        hide player with dissolve
        $ player.go_to(L_mall_parking_lot)

    elif M_debbie.is_state(S_debbie_cupid_store) and destination not in (L_mall, L_mall_floor2, L_cupid, L_cupid_dressroom):
        show player 1
        player_name "Hmm, I'm supposed to be {b}looking for a store called \"Cupid\"{/b}."

        show player 4
        player_name "{b}[deb_name]{/b} said it should be {b}on the second floor{/b}."


    elif M_debbie.is_state(S_debbie_choose_gift):
        show player 4 with dissolve
        player_name "Hmm, I should check out the necklace display for something {b}[deb_name]{/b} would like..."

        hide player with dissolve

    elif M_debbie.is_state(S_debbie_show_necklace):
        show player 4 with dissolve
        player_name "I should take this necklace to {b}[deb_name]{/b} and see if she likes it."

        hide player with dissolve

    elif M_debbie.is_state(S_debbie_dressing_room) and destination == L_mall_floor2:
        show player 14 with dissolve
        player_name "I have to wait for {b}[deb_name]{/b}."

        show player 13
        player_name "..."
        show player 10
        player_name "I wonder what's taking her so long?"

        hide player with dissolve

    elif M_jenny.is_state(S_jenny_get_a_mask) and destination == L_comicstore:
        jump cupid_store_waiting_line

    elif M_jenny.is_state(S_jenny_go_to_pink) and player.location == L_pink:
        if game.timer.now == M_diane.diaxx_cowsuit_ivy:
            return

        show anon f_worried with dissolve
        anon @ -m_talk "As I'm here, I may as well see if the clerk can help me."

        anon @ -m_talk "Hopefully they'll be done talking soon."

        hide anon with dissolve

    elif M_jenny.is_state(S_jenny_ivy_jane_leave_pink) and player.location == L_pink:
        show anon f_worried with dissolve
        anon @ -m_talk "Sold out?! I can't go back to {b}[jen_name]{/b} empty handed..."

        show anon a_thinking f_thinking
        pause
        anon a_point f_normal @ -m_talk "... But maybe {b}that toy on the counter{/b} would satisfy her?"

        hide anon with dissolve

    elif M_jenny.is_state(S_jenny_buy_vibrator) and player.location == L_pink:
        show anon with dissolve:
            xoffset -40
        anon @ -m_talk "I can't leave yet, {b}[jen_name]{/b} is waiting for me to {b}grab the UltraVibe 2000{/b}."

        show anon a_thinking f_thinking
        pause
        anon a_point f_surprised @ -m_talk "I think it's {b}the one above the very excited looking sex doll{/b}..."

        hide anon with dissolve
    else:

        return

    return True
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
