label ano14_find_bank_vault:
    return


label ano14_find_bank_vault.pass:
    scene expression background(192, 400, 3.) as stage
    show anon:
        flip
    with fade
    anon @ a_point "I found it!"

    liu "Nice job!"

    liu "Ugh, these things are always so heavy..."

    pause
    show liu a_bank_box with {'master': dissolve}:
        flip
    liu "Ini dia."

    show liu a_idle
    show anon a_bank_box
    with dissolve
    anon "Terima kasih."

    anon f_shy_low "Now, let's see what you were hiding, {b}Dad{/b}..."

    show anon a_bank_box_open
    pause
    anon f_surprised_low "W-what the-"

    liu f_worried @ -m_talk "Hmm?"

    scene expression background(192, 424, 6.) as stage
    show closeup_bank_box
    with fade
    anon "It's empty!!"

    liu "Kosong?"

    scene expression background(192, 400, 3.) as stage
    show anon f_worried a_bank_box_open:
        flip
    show liu f_worried:
        flip
    with fade
    anon "Yeah, there's nothing in here..."

    show anon a_bank_box with {'master': dissolve}
    liu "Ya ampun."

    liu @ f_curious "Why would your father hide the key to an empty lockbox?"

    anon "Saya tidak tahu!"

    show anon a_idle
    show liu a_bank_box
    with dissolve
    pause
    hide liu with {'master': dissolve}
    anon f_unimpressed "Ya, sial."

    anon "I thought I was finally getting somewhere..."

    pause
    anon f_worried "Does the bank keep records of what's inside these lockboxes?"

    show liu with {'master': dissolve}:
        flip
    liu "No, I'm afraid not."

    anon f_sad_down "{i}*Huh*{/i}"

    anon "Now what am I supposed to do?"

    liu "I'm really sorry, {b}[firstname]{/b}..."

    liu "I wish there was more I could do to help you."

    anon f_worried "No, you did plenty."

    anon "Thanks for helping me, {b}Liu{/b}."

    liu "Tidak masalah."

    liu "Just let me know if you need anything else, yeah?"

    anon "Akan dilakukan."

    hide anon with dissolve

    $ game.timer.tick()
    $ player.go_to(L_bank)
    scene expression background(520, 416, 3.) as stage with slowfade
    show anon f_angry with dissolve
    anon @ -m_talk "( Damnit, an empty box!! )"

    anon @ -m_talk "( Are you kidding me?! )"

    pause
    anon f_worried @ -m_talk "( Now I'm all the way back to square one. )"

    anon @ -m_talk "( I should go let {b}Tony{/b} know that I hit another dead end... )"

    hide anon with dissolve
    return


label ano14_find_bank_vault.fail:
    scene expression background(192, 400, 3.) as stage
    show anon f_skeptical
    with fade
    anon @ -m_talk "( I just can't seem to keep the number in my head... )"

    if player.has_item('picture4'):
        anon f_normal @ -m_talk "( Better dig the {b}photo out of my backpack{/b} and {b}have another look{/b}. )"

    else:
        anon f_normal @ -m_talk "( Better dig the {b}note I made out of my backpack{/b} and {b}have another look{/b}. )"

    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
