init -1 python:
    M_odette = Machine(
        'odette',
        default_loc=[[L_tattooparlor_garage, L_tattooparlor_interior,
                      L_tattooparlor_interior, L_tattooparlor_garage]],
        vars={'sex speed': 0.3,
              'test': 0,
              'proposed_sex': False,
              'bike_1st_time': True,
              'hide_sex_proposal_options': False,
              'gotta_have_that_dick': False},
        can_talk=[False, True, True, False],
        pregnancy_chance=1.0,
        default_pregnancy_schedule={
            "":                 LocationSchedule([[L_tattooparlor_garage, L_tattooparlor_interior, L_tattooparlor_garage, L_tattooparlor_garage]]),
            "_pregnant_bump":   LocationSchedule([[L_tattooparlor_garage, L_tattooparlor_interior, L_tattooparlor_garage, L_tattooparlor_garage]]),
            "_pregnant_belly":  LocationSchedule([[(L_tattooparlor_garage,
                                                    L_tattooparlor_bathroom), L_tattooparlor_interior, L_tattooparlor_garage, L_tattooparlor_garage]]),
            "_baby_twins":      LocationSchedule([[L_tattooparlor_garage, L_tattooparlor_interior, L_tattooparlor_garage, L_tattooparlor_garage]]),
            "_baby_girl":       LocationSchedule([[L_tattooparlor_garage, L_tattooparlor_interior, L_tattooparlor_garage, L_tattooparlor_garage]]),
            "_baby_boy":        LocationSchedule([[L_tattooparlor_garage, L_tattooparlor_interior, L_tattooparlor_garage, L_tattooparlor_garage]])})


init -3 python:
    T_ode00_init = Trigger()

    T_ode01_init = Trigger()

    T_ode02_init = Trigger()
    T_ode02_find = Trigger()
    T_ode02_fear = Trigger()
    T_ode02_tomb = Trigger()
    T_ode02_wake = Trigger()
    T_ode02_warn = Trigger()


init python:
    S_ode00_init = State()
    S_ode00_done = State()


    S_ode01_init = State(_("I wonder how Grace and Odette are getting on at the tattoo parlor."))
    S_ode01_done = State(_("How do I end up agreeing to this stuff?"))


    S_ode02_init = State(_("Church graveyard. Dead of night. Full moon. Welp!"))
    S_ode02_find = State(_("Well I'm here... things seem... different. I should look around."))
    S_ode02_fear = State(_("I bailed! I mean, what could go wrong. Entering a crypt. In a graveyard, During a full moon. D:"))
    S_ode02_tomb = State(_("I've come this far and... what is Odette even wearing?! What could she be planning?"))
    S_ode02_wake = State()
    S_ode02_warn = State(_("Is Odette really a creature of the night? Did Eve know?! To the tattoo parlor I go!"))
    S_ode02_done = State()


init python:
    S_ode00_init.add(T_ode00_init, S_ode00_done)
    S_ode00_done.add(T_all_sleep, S_ode01_init,
                     actions=('priority', 1,
                              'location', ('eve', {'place': L_tattooparlor_interior}),
                              'force', ('eve', {'tod': [0, 1]}),
                              'location', ('grace', {'place': L_tattooparlor_interior}),
                              'force', ('grace', {'tod': [0, 1]}),
                              'location', {'place': L_tattooparlor_interior},
                              'force', {'tod': [0, 1]}))

    S_ode01_init.add(T_ode01_init, S_ode01_done,
                     actions=('unforce', 'eve',
                              'unforce', 'grace',
                              'unforce', None,
                              'setdefaultloc', [[L_tattooparlor_garage, L_tattooparlor_interior,
                                                 L_tattooparlor_interior, L_church_crypt],
                                                [L_tattooparlor_garage, L_tattooparlor_interior,
                                                 L_tattooparlor_apartment, L_church_crypt]],
                              'setcantalk', [True] * 4))
    S_ode01_done.add(T_all_tick, S_ode02_init)

    S_ode02_init.add(T_ode02_init, S_ode02_find)
    S_ode02_find.add(T_ode02_find, S_ode02_fear)
    S_ode02_fear.add(T_ode02_fear, S_ode02_tomb)
    S_ode02_tomb.add(T_ode02_tomb, S_ode02_wake)
    S_ode02_wake.add(T_ode02_wake, S_ode02_warn,
                     actions=('location', ('eve', {'place': L_tattooparlor_interior}),
                              'force', ('eve', {'tod': 0}),
                              'location', ('grace', {'place': L_tattooparlor_interior}),
                              'force', ('grace', {'tod': 0}),
                              'location', {'place': L_tattooparlor_interior},
                              'force', {'tod': 0}))
    S_ode02_warn.add(T_ode02_warn, S_ode02_done,
                     actions=('unforce', 'eve',
                              'unforce', 'grace',
                              'unforce', None))


init python:
    M_odette.add(
        S_ode00_init, S_ode00_done,
        S_ode01_init, S_ode01_done,
        S_ode02_init, S_ode02_find, S_ode02_fear, S_ode02_tomb, S_ode02_wake,
            S_ode02_warn, S_ode02_done)


init python:
    def ode02_hint():
        if not M_odette.is_state(S_ode02_init, S_ode02_fear):
            return
        
        inbox = player.messages
        
        fullmoon = game.timer.is_fullmoon()
        sent = next((m for m in inbox if m.startswith('ode02_')), None)
        message = sent or ['ode02_hint', 'ode02_preg', 'ode02_baby'][
            bisect.bisect((1, 5), M_odette.pregnancy.stage)]
        
        
        if fullmoon and not sent and game.timer.is_afternoon():
            player.receive_message(message)
        
        
        elif fullmoon and not sent and game.timer.days_since_lunar(.5) > 0:
            player.receive_message(message)
        
        
        elif not fullmoon and sent:
            inbox.remove(message)


    M_odette.add_action(T_all_tick, ('exec', ode02_hint))
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
