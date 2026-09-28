label ano28_cash_liu_money:
    $ renpy.dynamic(bank=L_bank_lobby.is_here(M_liu))

    anon "I have something for you."
    show anon a_backpack f_looking_down:
        xoffset 190
    show liu f_confused_down
    with {'master': dissolve}
    liu @ -m_talk "Hmm?"
    show anon a_stashed_bag
    show liu f_confused
    with {'master': dissolve}
    anon f_normal "Check it out."
    show anon a_stashed_bag_show
    show liu f_confused_down
    with dissolve
    show anon a_idle
    show liu a_bag_look
    with dissolve
    pause
    show anon f_grin
    liu f_surprised_down "!!!" with hpunch
    liu f_shocked "Where did you get this?!"
    anon f_normal "It's the money {b}Dad{/b} took from the mob."
    liu f_surprised "You found it?!"
    anon @ -m_talk "Mhmm."
    anon "That clue you gave me lead right to it."
    liu f_happy "That's amazing, {b}[firstname]{/b}!"
    anon "I know, right!"
    anon "So I want you to take out what's needed to clear {b}[deb_name]{/b}'s debt."
    liu f_normal "I can do that."
    anon f_thinking "Then I want you to split the remainder."
    liu "Okay."
    anon f_shy "Put half in my bank account..."
    liu @ -m_talk "Mhmm."
    anon f_normal "... and the other half in yours."
    show liu a_mouth_cover f_surprised m_talk with dissolve
    pause
    liu -m_talk "Y-you can't be serious!"
    anon "I'm serious."
    liu a_cover f_worried "I can't take half your money, {b}[firstname]{/b}."
    anon f_brag "Of course you can."
    show liu f_ashamed_down
    anon "I know how important you were to {b}Dad{/b} before he died..."
    anon f_normal "... And you need it."
    pause
    show liu a_sides f_nervous with {'master': dissolve}
    anon "Plus, I never could have accomplished all this without you."
    liu "I-"
    show liu f_nervous_lipbite
    pause
    liu f_happy "I don't know what to say."
    anon "You don't have to say anything, {b}Liu{/b}."

    if bank:
        show anon f_confused
        show liu f_happy_down_back
        pause
        show anon a_up f_surprised with {'master': fastdissolve}
        anon "Wait, what are you-"
        show anon b_dressed_blocking:
            xoffset 130
        show liu b_dressed_jump
        show liu_desk as counter behind liu
        with dissolve
        pause .1
        show liu b_dressed_bend with vpunch
        pause
        show anon b_dressed f_surprised_teeth
        show liu b_dressed f_surprised_down m_talk
        with dissolve
        pause
        show anon f_surprised
        show liu f_surprised
        with dissolve
        pause
        show liu f_laugh -m_talk
        pause
        show anon b_empty f_surprised_low:
            xoffset 0
        show liu b_dressed_hug:
            xoffset 0
    else:

        show anon b_empty f_shy_low
        show liu b_robe_hug:
            xoffset 190

    with {'master': dissolve}
    liu "You are the most wonderful man alive!"
    anon f_shy "Heh, seriously... you deserve it."
    hide anon

    if bank:
        show liu b_dressed_kiss_2:
            xoffset -100
    else:
        show liu b_robe_kiss:
            xoffset 90

    with dissolve
    liu "Mmm."
    pause
    show anon a_sides b_dressed f_shy
    show liu a_sides f_happy

    if bank:
        show anon:
            xoffset -140
        show liu b_dressed:
            xoffset -440
    else:

        show anon:
            xoffset 50
        show liu b_robe_hair:
            xoffset -250

    with dissolve
    anon "So you'll take care of everything for me?"
    liu "Y-yes, of course!"
    liu "I'll do anything you want me to, {b}[firstname]{/b}."
    anon "Thanks, {b}Liu{/b}."
    pause
    anon f_normal "Now, if you'll excuse me..."
    anon "... I have to go and tell {b}[deb_name]{/b} the good news."
    hide anon with dissolve
    pause
    liu a_cover f_sexy "Oh my god, he is the perfect man..."
    return 'ano28'
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
