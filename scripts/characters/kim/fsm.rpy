init -1 python:
    M_kim = Machine(
        'kim',
        default_loc=[[L_dealership_showroom,
                      L_dealership_showroom,
                      L_dealership_lounge,
                      L_NULL]],
        vars={'eotm': False,
              'russians': False,
              'state': None,
              'wallet': None})


    def kim_cleanup():
        M_kim.set_default_locations([[L_NULL] * 4])
        M_kim.set('state', 'fled')
        if M_josie.is_state(S_jos01_spot):
            M_kim.unforce(machine=M_josie)
            M_yoyo.place(machine=M_josie, place=L_dealership_showroom)
            M_yoyo.force(flag=True, machine=M_josie)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
