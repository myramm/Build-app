label yoy01_wait_yoyo:
    show anon a_sides with dissolve
    yoyo f_confused "You ready to grover at {b}Kim{/b} feet?"
    anon f_unimpressed "Nope."
    hide anon
    show yoyo f_annoyed
    with {'master': dissolve}
    yoyo "Hey!!"
    show yoyo a_hips f_angry
    with {'master': dissolve}
    yoyo "Come back here and beg forgiveness, you bad boy!!"
    return


label yoy01_hold_yoyo:
    show yoyo a_clasp f_shy
    with None
    show anon a_sides
    show yoyo a_clench
    with dissolve
    yoyo "You come for aporogy pie?"
    anon "Aww, no... that's not necessary."
    show yoyo a_clasp
    with {'master': dissolve}
    yoyo "You sure?"
    yoyo f_happy "Is banana cream."
    jump yoy01_meet_dealership_showroom.choice
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
