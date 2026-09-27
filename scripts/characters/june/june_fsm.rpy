init -1 python:
    M_june = Machine('june',
                     default_loc=[[L_school_computerlab, L_school_computerlab,
                                   L_NULL, L_NULL],
                                  [L_NULL] * 4],
                     vars={'sex speed': .3,
                           'hang_time': False,
                           'excuse': None})

    M_june.add_action(T_all_sleep, ('assign', ('hang_time', False)))


init -3 python:
    T_june_fork_setup = Trigger()
    T_june_fork_date = Trigger()

    T_june_date_ask = Trigger()
    T_june_date_lost = Trigger()
    T_june_date_lame = Trigger()
    T_june_date_sorry = Trigger()
    T_june_date_request = Trigger()

    T_june_cosplay_bought = Trigger()
    T_june_cosplay_given = Trigger()
    T_june_cosplay_bork = Trigger()


init python:
    S_june_start = State(_("Nothing in life is guaranteed."))

    S_june_date_ready = State(_("June is interested in playing games together. I should ask her to hang out some time."))
    S_june_date_visit = State(_("Wow! June is so cool! We're going to play tonight in my room!"))
    S_june_date_shame = State(_("I think I embarrassed June calling her game gross... I should go see her."))
    S_june_date_done = State()

    S_june_cosplay_ready = State(_("I promised to help June with her orc cosplay. Cosmic Cumics should have what I need."))
    S_june_cosplay_acquired = State(_("There's not much to this outfit... I can\'t wait to show June!"))
    S_june_cosplay_demo = State(_("June's going to give me a sneak peek at her orc costume next time we hang out!"))

    S_june_end = State()


init python:

    S_june_start.add(T_mrsj_fork_setup, S_june_end)
    S_june_start.add(T_mrsj_fork_steal, S_june_date_ready,
                     actions=('priority', 1,
                              'trigger', T_june_date_ask))


    S_june_date_ready.add(T_june_date_ask, S_june_date_visit,
                          actions=('assign', ('hang_time', True),
                                   'assign', ('excuse', None)))
    S_june_date_visit.add(T_all_sleep, S_june_date_ready,
                          actions=('assign', ('excuse', '"tired"')))
    S_june_date_visit.add(T_june_date_lost, S_june_date_ready,
                          actions=('assign', ('excuse', '"retry"')))
    S_june_date_visit.add(T_june_date_lame, S_june_date_shame)
    S_june_date_shame.add(T_june_date_sorry, S_june_date_visit,
                          actions=('assign', ('hang_time', True),
                                   'assign', ('excuse', None)))
    S_june_date_visit.add(T_june_date_request, S_june_date_done,
                          actions=('assign', ('excuse', None)))
    S_june_date_done.add(T_all_sleep, S_june_cosplay_ready,
                         actions=('condition', ('player.has_item("orcette_cosplay")',
                                                ('trigger', T_june_cosplay_bought), ())))


    S_june_cosplay_ready.add(T_june_cosplay_bought, S_june_cosplay_acquired)
    S_june_cosplay_acquired.add(T_june_cosplay_given, S_june_cosplay_demo,
                                actions=('assign', ('hang_time', True)))
    S_june_cosplay_demo.add(T_june_cosplay_bork, S_june_end,
                            actions=('exec', A_hoes_before_bros.unlock,
                                     'clear', ('player', 'is_virgin')))


init python:
    M_june.add(
        S_june_start,
        S_june_date_ready, S_june_date_visit,
            S_june_date_shame, S_june_date_done,
        S_june_cosplay_ready, S_june_cosplay_acquired, S_june_cosplay_demo,
        S_june_end)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
