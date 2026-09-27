init -1 python:
    M_angelica = Machine("angelica", default_loc=[[L_church, L_church, L_church_angelica, L_church_angelica]],
                        vars={'sex speed': .3},
    )

init -3 python:

    T_angelica_house_visit = Trigger()
    T_angelica_ritual_deal = Trigger()
    T_angelica_requires_whip = Trigger()
    T_angelica_sinful_thoughts = Trigger()
    T_angelica_strapon_request = Trigger()
    T_angelicas_final_ritual = Trigger()

init python:
    S_angelica_start = State()

    M_angelica.add(S_angelica_start)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
