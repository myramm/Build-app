label pc_hook_egay:
    if M_erik.is_state(S_erik_orc_order):
        anon "( Hmm... I guess I should just type in the name of the item {b}Erik{/b} wanted. )"

        anon "( What was it again? )"

    return

label pc_hook_egay_buy_success:
    anon "( Looks like I should get the package in the mailbox on {b}Tuesday{/b}. )"

    $ M_erik.trigger(T_erik_orc_ordered)
    return

label pc_hook_egay_buy_failure:
    call popup ('poor')
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
