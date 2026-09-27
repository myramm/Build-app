init -1 python:
    M_terry = Machine("terry", default_loc = [[L_pier, L_pier, L_pier, L_pier]],
                      vars = {"bait talk": False,},
    )

init -3 python:

    T_terry_intro = Trigger()
    T_terry_secret_lure = Trigger()
    T_terry_tigger = Trigger()
    T_terry_lure_trade = Trigger()
    T_terry_retire = Trigger()
    T_terry_overjoyed_swim = Trigger()
    T_terry_hang_tigger = Trigger()

init python:

    S_terry_start = State()
    S_terry_secret = State(_("The secret behind his fishing"))
    S_terry_lure = State(_("The lure that made Terry famous for his fishing"))
    S_terry_nemesis = State(_("Sara tells you the cause of Terry's drunken state"))
    S_terry_drunk = State(_("Terry is out drunk for the day"))
    S_terry_trade = State()
    S_terry_bored = State()
    S_terry_retire = State()
    S_terry_tigger_sign = State()
    S_terry_end = State()


    S_terry_start.add(T_terry_intro, S_terry_secret,
                      actions=('set', ('sara', 'met')))
    S_terry_secret.add(T_terry_secret_lure, S_terry_lure)
    S_terry_lure.add(T_all_sleep, S_terry_nemesis)
    S_terry_nemesis.add(T_terry_tigger, S_terry_drunk,
                        actions = ["location", {"place": L_NULL},
                                   "force", {"flag": True},
                                   ],
                        )
    S_terry_drunk.add(T_all_sleep, S_terry_trade,
                      actions = ["unforce", None],
                      )
    S_terry_trade.add(T_terry_lure_trade, S_terry_bored)
    S_terry_bored.add(T_terry_retire, S_terry_retire)
    S_terry_retire.add(T_terry_overjoyed_swim, S_terry_tigger_sign)
    S_terry_tigger_sign.add(T_terry_hang_tigger, S_terry_end)

    M_terry.set_priority(1)

    M_terry.add(S_terry_start, S_terry_secret, S_terry_lure, S_terry_nemesis,
                S_terry_drunk, S_terry_trade, S_terry_bored, S_terry_retire,
                S_terry_tigger_sign, S_terry_end)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
