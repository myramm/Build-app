init -1 python:
    M_consuela = Machine(
        'consuela',
         default_loc=[[L_NULL,
                       L_rump_kitchen,
                       L_rump_lobby,
                       L_NULL]],
         vars={'sex speed': .4,
               'sex_location': '',
               'bot_return': None,
               'done_anal': False},
         pregnancy_chance=0.05,
         default_pregnancy_schedule={
             "":                LocationSchedule([[L_beachhouse_entrance] * 2 + [L_NULL] * 2]),
             "_pregnant_bump":  LocationSchedule([[L_beachhouse_entrance] * 2 + [L_NULL] * 2]),
             "_pregnant_belly": LocationSchedule([[L_beachhouse_entrance] * 2 + [L_NULL] * 2]),
             "_baby_twins":     LocationSchedule([[L_beachhouse_entrance] * 2 + [L_hospital_floor2, L_NULL]]),
             "_baby_girl":      LocationSchedule([[L_beachhouse_entrance] * 2 + [L_hospital_floor2, L_NULL]]),
             "_baby_boy":       LocationSchedule([[L_beachhouse_entrance] * 2 + [L_hospital_floor2, L_NULL]])})


init -3 python:
    T_con01_init = Trigger()
    T_con01_plan = Trigger()
    T_con01_idea = Trigger()
    T_con01_deal = Trigger()
    T_con01_take = Trigger()
    T_con01_give = Trigger()
    T_con01_skip = Trigger()

    T_con02_init = Trigger()
    T_con02_tell = Trigger()
    T_con02_job1 = Trigger()
    T_con02_job2 = Trigger()
    T_con02_job3 = Trigger()
    T_con02_scam = Trigger()
    T_con02_ptsd = Trigger()
    T_con02_done = Trigger()

    T_con03_init = Trigger()
    T_con03_door = Trigger()
    T_con03_sing = Trigger()
    T_con03_done = Trigger()

    T_con04_init = Trigger()
    T_con04_wake = Trigger()
    T_con04_hint = Trigger()


init python:
    S_con00_init = State()
    S_con00_done = State(_("That poor maid... I wonder if I can help her somehow..."))

    S_con01_init = State(_("I don't know what to do, maybe someone at the Rump estate can help."))
    S_con01_plan = State(_("A replacement... Maybe Ricky has an idea of where to look?"))
    S_con01_idea = State(_("Desperate prostitutes? Well, they must need toys, maybe I should ask at Pink..."))
    S_con01_deal = State(_("Replacing Consuela with a Thotbot is pretty contrived, but needs must!"))
    S_con01_take = State(_("The Thotbot must have arrived by now, I should head to Pink."), delay=3)
    S_con01_give = State(_("I should get this Thotbot over to the Rump estate."))
    S_con01_skip = State()
    S_con01_done = State(_("I feel so guilty... I never realized how much I'd up-end Consuela\'s life..."))

    S_con02_init = State(_("I need to help find Consuela a new job. I should try asking the priest at the church."))
    S_con02_tell = State(_("Consuela will be so happy when I tell her the good news!"))
    S_con02_job1 = State(_("I should introduce Consuela to Father Keeves at the church."))
    S_con02_job2 = State(_("Oh well... We can see if there's a job opening at school."))
    S_con02_job3 = State(_("Finding a job is harder than I thought... Maybe the hospital?"))
    S_con02_scam = State(_("Success! I just need to help fetch her uniform from the hospital storage room."))
    S_con02_ptsd = State(_("Welp! Time to head back to reception. This better have been worth it."))
    S_con02_done = State(_("I hope I get to see more of Consuela!"), delay=6)

    S_con03_init = State(_("You know, I feel like taking a nap in the beach house tonight."))
    S_con03_door = State(_("I should probably stop checking my phone and answer the door."))
    S_con03_wait = State(_("Consuela's going to be keeping the beach house clean... For free!"))
    S_con03_sing = State(_("I wonder how Consuela's getting on at the beach house."))
    S_con03_done = State(_("Consuela's got moves! I should check in from time to time."), delay=7)

    S_con04_init = State(_("That beach house bed is pretty tempting tonight."), delay=7)
    S_con04_wake = State(_("What a racket, I should go see what's going on!"))
    S_con04_hint = State(_("An afternoon snack in the beach house would really hit the spot."), delay=1)
    S_con04_done = State()


init python hide:

    S_con00_init.add(T_ano18_flee, S_con00_done,
                     actions=('priority', 1))
    S_con00_done.add(T_all_sleep, S_con01_init)


    hide = ('location', {'place': L_NULL}, 'force', {'flag': True})
    S_con01_init.add(T_con01_init, S_con01_plan)
    S_con01_plan.add(T_con01_plan, S_con01_idea)
    S_con01_idea.add(T_con01_idea, S_con01_deal)
    S_con01_deal.add(T_con01_deal, S_con01_take)
    S_con01_take.add(T_con01_take, S_con01_give)
    S_con01_give.add(T_con01_give, S_con01_done, actions=hide)
    S_con01_done.add(T_all_tick, S_con02_init,
                     actions=('unforce', None,
                              'setdefaultloc', [[L_mall_parking_lot,
                                                 L_mall_parking_lot,
                                                 L_NULL,
                                                 L_NULL],
                                                [L_NULL] * 4]))


    skip = ('trigger', T_con01_skip)
    S_con01_init.add(T_con01_skip, S_con01_skip, actions=skip)
    S_con01_plan.add(T_con01_skip, S_con01_skip, actions=skip)
    S_con01_idea.add(T_con01_skip, S_con01_skip, actions=skip)
    S_con01_deal.add(T_con01_skip, S_con01_skip, actions=skip)
    S_con01_take.add(T_con01_skip, S_con01_skip, actions=skip)
    S_con01_give.add(T_con01_skip, S_con01_skip, actions=skip)
    S_con01_skip.add(T_con01_skip, S_con01_done,
                     actions=('set', 'bot_return') + hide)


    S_con02_init.add(T_con02_init, S_con02_tell)
    S_con02_tell.add(T_con02_tell, S_con02_job1,
                     actions=('location', {'place': L_NULL},
                              'force', {'flag': True}))
    S_con02_job1.add(T_con02_job1, S_con02_job2)
    S_con02_job2.add(T_con02_job2, S_con02_job3)
    S_con02_job3.add(T_con02_job3, S_con02_scam,
                     actions=('location', ('roz', {'place': L_hospital_storageroom}),
                              'force', ('roz', {'flag': True})))
    S_con02_scam.add(T_con02_scam, S_con02_ptsd,
                     actions=('unforce', 'roz'))
    S_con02_ptsd.add(T_con02_ptsd, S_con02_done,
                     actions=('unforce', None,
                              'setdefaultloc', [[L_NULL, L_NULL,
                                                 L_hospital_floor2,
                                                 L_hospital_floor2]]))
    S_con02_done.add(T_all_sleep, S_con02_done,
                     actions=('condition', ('player.has_item("beach_house_key")',
                                            ('trigger', T_con02_done), ())))
    S_con02_done.add(T_con02_done, S_con03_init)


    S_con03_init.add(T_con03_init, S_con03_door)
    S_con03_door.add(T_con03_door, S_con03_wait)
    S_con03_wait.add(T_all_sleep, S_con03_sing,
                     actions=('setdefaultloc', [[L_beachhouse_entrance,
                                                 L_beachhouse_kitchen,
                                                 L_hospital_floor2,
                                                 L_hospital_floor2],
                                                [L_NULL, L_NULL,
                                                 L_hospital_floor2,
                                                 L_hospital_floor2]]))
    S_con03_sing.add(T_con03_sing, S_con03_done)
    S_con03_done.add(T_con03_done, S_con04_init)


    S_con04_init.add(T_con04_init, S_con04_wake)
    S_con04_wake.add(T_con04_wake, S_con04_hint)
    S_con04_hint.add(T_con04_hint, S_con04_done,
                     actions=('clear', ('player', 'is_virgin')))


init python:
    M_consuela.add(
        S_con00_init, S_con00_done,
        S_con01_init, S_con01_plan, S_con01_idea, S_con01_deal, S_con01_take,
            S_con01_give, S_con01_skip, S_con01_done,
        S_con02_init, S_con02_tell, S_con02_job1, S_con02_job2, S_con02_job3,
            S_con02_scam, S_con02_ptsd, S_con02_done,
        S_con03_init, S_con03_door, S_con03_wait, S_con03_sing, S_con03_done,
        S_con04_init, S_con04_wake, S_con04_hint, S_con04_done)

    M_consuela.outfit.set_default_outfit_schedule([['dressed', 'dressed', 'hospital', 'hospital']])
    M_consuela.add_action(T_all_sleep, ('assign', ('doing_anal', False)))
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
