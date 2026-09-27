init -1 python:
    M_larry = Machine('larry', default_loc=[[L_NULL] * 4] * 2, vars={})

init -3 python:
    T_larry_msg_request = Trigger()
    T_larry_msg_relayed = Trigger()
    T_larry_msg_reward = Trigger()

init python:
    S_larry_start = State(_("Pending activation."))

    S_larry_msg_ready = State(_("A two-year crime spree! Larry had a good run, but he's in the police cells now."))
    S_larry_msg_sorry = State(_("Larry gave me a message for Mrs Johnson. I should speak to Erik before passing it on though."))
    S_larry_msg_given = State(_("Erik's going to deal with it. It\'s out of my hands, I should let Larry know."))
    S_larry_msg_done = State(_("Larry told me that the stolen goods were hidden behind a bush in the park, next to a white tree."))

    S_larry_end = State(_("Crime doesn't pay kids!"))

init python:

    S_larry_start.add(T_erik_thief_catch, S_larry_msg_ready,
                      actions=('setdefaultloc', [[L_police_basement] * 4] * 2))


    S_larry_msg_ready.add(T_larry_msg_request, S_larry_msg_sorry)
    S_larry_msg_sorry.add(T_larry_msg_relayed, S_larry_msg_given)
    S_larry_msg_given.add(T_larry_msg_reward, S_larry_msg_done,
                          actions=('condition', ('M_mia.get("stolen goods recovered")',
                                                 ('trigger', T_harold_found_goods), ())))


    S_larry_msg_done.add(T_harold_found_goods, S_larry_end)

init python:
    M_larry.add(
        S_larry_start,
        S_larry_msg_ready, S_larry_msg_sorry,
            S_larry_msg_given, S_larry_msg_done,
        S_larry_end)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
