label yoy01_wait_yoyo:
    show anon a_sides with dissolve
    yoyo f_confused "Anda siap untuk berjalan di kaki {b}Kim{/b}?"

    anon f_unimpressed "Tidak."

    hide anon
    show yoyo f_annoyed
    with {'master': dissolve}
    yoyo "Hai!!"

    show yoyo a_hips f_angry
    with {'master': dissolve}
    yoyo "Kembalilah ke sini dan mohon maaf, dasar bocah nakal!!"

    return


label yoy01_hold_yoyo:
    show yoyo a_clasp f_shy
    with None
    show anon a_sides
    show yoyo a_clench
    with dissolve
    yoyo "Anda datang untuk meminta maaf?"

    anon "Ah, tidak... itu tidak perlu."

    show yoyo a_clasp
    with {'master': dissolve}
    yoyo "Anda yakin?"

    yoyo f_happy "Apakah krim pisang."

    jump yoy01_meet_dealership_showroom.choice
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
