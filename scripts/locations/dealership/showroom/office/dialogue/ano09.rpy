label ano09_vest_dealership_office_vest:
    if L_dealership_office.is_here(M_sato):
        jump ano09_vest_dealership_office_vest.caught
    else:
        jump ano09_vest_dealership_office_vest.evaded

    return


label ano09_vest_dealership_office_vest.caught:
    scene expression background(b=.5) as stage:
        anchor (int(208*2.5), int(360*2.5))
        pos (.5, .5)
        zoom 2.5
    show sato:
        xoffset 400
    show anon f_worried a_jacket with dissolve:
        flip
        xoffset -350
    sato "Permisi?"

    show anon f_surprised with fastdissolve:
        unflip
        xoffset 200
    anon @ -m_talk "!!!{nw}"

    show layer master:
        easein_elastic 1. xpos -300
    anon @ -m_talk "!!!{fast}"

    anon f_worried @ -m_talk "Hmm?"

    sato "What do you think you're doing?"

    anon "Oh, uhh, {b}Josephine{/b} asked me to get this for her."

    sato "She did?"

    anon "Ya, tuan."

    pause
    sato f_confused "What does she need that for?"

    sato "She didn't destroy her uniform again, did she?"

    anon "T-tidak..."

    pause
    anon "She just wants me to-"

    sato f_normal "Actually, never mind..."

    sato "... So long as the building isn't on fire, I don't care."

    anon @ -m_talk "..."
    sato "Carry on."

    hide sato with dissolve
    anon "Terima kasih."

    hide anon with dissolve
    return


label ano09_vest_dealership_office_vest.evaded:
    scene expression background(200, 360, 2.5) as stage
    show anon a_jacket with dissolve:
        flip
        xoffset -350
    anon "Here's the vest {b}Josephine{/b} wanted me to get."

    anon "I should get back to the front desk and see about getting that discount now."

    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
