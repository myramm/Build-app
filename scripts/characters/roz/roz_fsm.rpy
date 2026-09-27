init -1 python:
    M_roz = Machine('roz',
                    default_loc=[[L_hospital_lobby, L_hospital_lobby, L_hospital_lobby, L_NULL]],
                    vars={'fun time': False,
                          'sex speed': .4})

    def roz_prank():
        M_roz.place(place=L_hospital_floor2)
        M_roz.force(tod=game.timer._tod)

    def roz_card_acquired():
        M_roz.trigger(T_roz_access_card)

init -3 python:
    T_roz_access_denied = Trigger()
    T_roz_access_ask = Trigger()
    T_roz_access_prank = Trigger()
    T_roz_access_card = Trigger()
    T_roz_access_debt = Trigger()

    T_roz_obits_ask = Trigger()
    T_roz_obits_acquired = Trigger()

init python:
    S_roz_start = State(_("You'll know when it\'s time."))

    S_roz_access_enquire = State(_("Hmmm, maybe the receptionist can help get me into the storage room..."))
    S_roz_access_phone = State(_("Seems like I should be able to distract the receptionist using an intercom."))
    S_roz_access_ambush = State(_("Huge success! Key card acquired! Time to hit the storage room!"))

    S_roz_obits_collect = State(_("Roz said I could find the obituaries in the storage room on the second floor."))

init python:

    S_roz_start.add(T_roz_access_denied, S_roz_access_enquire,
                    actions=('priority', 1))
    S_roz_access_enquire.add(T_roz_access_ask, S_roz_access_phone)
    S_roz_access_phone.add(T_roz_access_prank, S_roz_access_phone,
                           actions=('exec', roz_prank))
    S_roz_access_phone.add(T_all_sleep, S_roz_access_phone,
                           actions=('unforce', None))
    S_roz_access_phone.add(T_roz_access_card, S_roz_start,
                           actions=('unforce', None,
                                    'priority', 0))


    S_roz_start.add(T_roz_obits_ask, S_roz_obits_collect,
                    actions=('priority', 1))
    S_roz_obits_collect.add(T_roz_obits_acquired, S_roz_start,
                  actions=('exec', A_oldies_goodies.unlock,
                           'clear', ('player', 'is_virgin'),
                           'priority', 0))

init python:
    M_roz.add(
        S_roz_start,
        S_roz_access_enquire, S_roz_access_phone, S_roz_access_ambush,
        S_roz_obits_collect)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
