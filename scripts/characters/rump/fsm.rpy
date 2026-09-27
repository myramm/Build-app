init -1 python:
    M_rump = Machine(
        'rump',
        default_loc=[[L_rump_office, [L_rump_office] * 6 + [L_rump_back],
                      L_rump_back, L_NULL],
                     [[L_mall] * 8 + [L_rump_back], [L_mall] * 3 + [L_rump_back],
                      L_rump_back, L_NULL]],
        vars={'sex speed': .3,
              'seen speech mall': False,
              'rump_n_cunt': False,
              'state': None,
              'can see speech mall': True})

    def rump_wc_scene():
        return game.timer.is_weekday() and \
               not M_anon.finished_state(S_ano20_cops) and \
               random.random() < .125

    def rump_cleanup():
        M_rump.set_default_locations([[L_NULL] * 4])
        M_rump.set('state', 'jailed')
        if M_josie.is_state(S_jos01_spot):
            M_rump.unforce(machine=M_josie)


init python:
    M_rump.add_action(T_all_sleep, ('assign', ('rump_n_cunt', 'rump_wc_scene()')))

    M_rump.outfit.set_default_outfit_schedule(
        [['dressed', 'dressed', 'swimsuit', 'dressed']])
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
