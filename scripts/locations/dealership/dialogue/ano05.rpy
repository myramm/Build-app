label ano05_sale_dealership:
    scene expression background(512, 480, 1.75) as stage
    show tony_overlay_o_scooter as scooter
    with fade
    show anon f_grin behind scooter at flip with dissolve
    anon @ -m_talk "( Holy crap, I did it! )"

    anon @ a_cheering -m_talk "( I bought my very first vehicle! )"

    anon @ -m_talk "( {b}I can't wait to show Tony{/b}. )"

    hide anon
    hide scooter
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
