init -1 python:
    M_mrsj = Machine('mrsj',
                     default_loc = [[L_erikhouse_entrance,
                                     L_erikhouse_entrance,
                                     L_erikhouse_mrsjroom,
                                     L_erikhouse_mrsjroom]],
                     vars = {'poker_after_party': False,
                             'sex speed': .3})

    def mrsj_cupid_coupling():
        erik = M_erik.get_default_locations()
        for day in erik[0:4]:
            day[0] = L_school_computerlab
        M_erik.set_default_locations(erik)
        june = M_june.get_default_locations()
        for day in june:
            day[2] = L_erikhouse_erikroom
        M_june.set_default_locations(june)


init -3 python:
    T_mrsj_intro_met = Trigger()

    T_mrsj_yoga_request = Trigger()
    T_mrsj_yoga_pass = Trigger()
    T_mrsj_yoga_fail = Trigger()
    T_mrsj_yoga_thanks = Trigger()

    T_mrsj_fork_crush = Trigger()
    T_mrsj_fork_setup = Trigger()
    T_mrsj_fork_steal = Trigger()

    T_mrsj_cupid_tell = Trigger()
    T_mrsj_cupid_happy = Trigger()
    T_mrsj_cupid_news = Trigger()


init python:
    S_mrsj_start = State(_("A completely avoidable encounter."))
    S_mrsj_intro_busy = State(_("Mrs Johnson is a pretty chill landlady to Erik."))
    S_mrsj_intro_done = State(_("Mrs Johnson is a pretty chill landlady to Erik."))

    S_mrsj_yoga_ready = State(_("I wonder what Mrs Johnson makes of hosting parties in the basement."))
    S_mrsj_yoga_class = State(_("Mrs Johnson asked me to assist Anna with yoga class at the gym tonight."))
    S_mrsj_yoga_retry = State(_("That was embarrassing! I should go over the worksheet then report back to Anna at the gym in the evening."))
    S_mrsj_yoga_report = State(_("I should let Mrs Johnson know the class was a success!"))
    S_mrsj_yoga_done = State(_("With all that yoga every day it's no wonder she\'s so hot!"))

    S_mrsj_fork_ready = State(_("Mrs Johnson is worried Erik isn't meeting girls. Who would Erik even like? I should ask him."))
    S_mrsj_fork_meet = State(_("Erik's interested in June. I should go seek her out in the computer lab at school."))

    S_mrsj_cupid_ready = State(_("June wants to game with Erik! He'll be psyched! I should let him know as soon as possible."))
    S_mrsj_cupid_date = State(_("Erik's going to speak to June. Fingers crossed for him."))
    S_mrsj_cupid_couple = State(_("I wonder how June and Erik got on. I should swing by Erik's and ask him."))
    S_mrsj_cupid_report = State(_("Mrs Johnson will be pleased to know it all worked out for Erik. I should let her know."))

    S_mrsj_end = State()


init python:

    S_mrsj_start.add(T_mrsj_intro_met, S_mrsj_intro_busy,
                     actions=('setdefaultloc', [[L_erikhouse_entrance,
                                                 L_yoga_room,
                                                 L_erikhouse_mrsjroom,
                                                 L_erikhouse_mrsjroom]],
                              'location', {'place': L_NULL},
                              'force', {'tod': 0}))
    S_mrsj_intro_busy.add(T_all_sleep, S_mrsj_intro_done,
                         actions=('unforce', None))


    S_mrsj_intro_done.add(T_erik_vr_given, S_mrsj_yoga_ready,
                          actions=('location', {'place': L_erikhouse_entrance},
                                   'force', {'tod': 2},
                                   'priority', 1))


    S_mrsj_yoga_ready.add(T_mrsj_yoga_request, S_mrsj_yoga_class,
                          actions=('location', {'place': L_NULL},
                                   'location', ('anna', {'place': L_yoga_room}),
                                   'force', ('anna', {'tod': 2})))
    S_mrsj_yoga_class.add(T_mrsj_yoga_pass, S_mrsj_yoga_report,
                          actions=('unforce', 'anna'))
    S_mrsj_yoga_class.add(T_mrsj_yoga_fail, S_mrsj_yoga_retry)
    S_mrsj_yoga_retry.add(T_mrsj_yoga_pass, S_mrsj_yoga_report)
    S_mrsj_yoga_report.add(T_mrsj_yoga_thanks, S_mrsj_yoga_done,
                           actions=('unforce', None,
                                    'priority', 0))


    S_mrsj_yoga_done.add(T_erik_fork_match, S_mrsj_fork_ready,
                         actions=('priority', 1))


    S_mrsj_fork_ready.add(T_mrsj_fork_crush, S_mrsj_fork_meet)
    S_mrsj_fork_meet.add(T_mrsj_fork_setup, S_mrsj_cupid_ready)
    S_mrsj_fork_meet.add(T_mrsj_fork_steal, S_mrsj_end)


    S_mrsj_cupid_ready.add(T_mrsj_cupid_tell, S_mrsj_cupid_date)
    S_mrsj_cupid_date.add(T_all_sleep, S_mrsj_cupid_couple,
                          actions=('location', ('erik', {'place': L_erikhouse_entrance}),
                                   'force', ('erik', {'flag': True}),
                                   'location', ('june', {'place': L_erikhouse_entrance}),
                                   'force', ('june', {'flag': True})))
    S_mrsj_cupid_couple.add(T_mrsj_cupid_happy, S_mrsj_cupid_report,
                            actions=('unforce', 'erik',
                                     'unforce', 'june',
                                     'exec', mrsj_cupid_coupling))
    S_mrsj_cupid_report.add(T_mrsj_cupid_news, S_mrsj_end,
                            actions=('exec', A_bros_before_hoes.unlock,
                                     'clear', ('player', 'is_virgin')))

init python:
    M_mrsj.add(
        S_mrsj_start, S_mrsj_intro_busy, S_mrsj_intro_done,
        S_mrsj_yoga_ready, S_mrsj_yoga_class, S_mrsj_yoga_retry,
            S_mrsj_yoga_report, S_mrsj_yoga_done,
        S_mrsj_fork_ready, S_mrsj_fork_meet,
        S_mrsj_cupid_ready, S_mrsj_cupid_date,
            S_mrsj_cupid_couple, S_mrsj_cupid_report,
        S_mrsj_end)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
