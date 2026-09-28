label mar01_init_apt_lobby:
    scene expression background(512, 440, 2.) as stage
    show anon f_sad_down with dissolve
    anon @ -m_talk "( Hmm, I wonder if {b}Tina{/b} knew {b}my dad{/b}? )"
    show anon f_thinking
    pause
    anon @ -m_talk "( I should probably ask her about him... )"
    show maria b_casual_magic a_groceries with dissolve
    anon @ -m_talk "Hmm?"
    anon f_surprised "{b}Maria{/b}?!"
    maria "What the-"
    anon f_confused "How come you're here?"
    maria "I'm bringing groceries home..."
    anon "Home?"
    anon f_surprised "Wait, you and {b}Tony{/b} live here?"
    maria f_sexy "What, did ya think {b}Tony{/b} and I lived at the pizzeria?"
    anon f_shy @ a_behind_head "Ehh."
    anon "N-no, of course not."
    maria @ f_laugh "Jesus, could ya imagine?"
    pause
    anon "You want some help with those?"
    maria "Nah, it's fine."
    maria "I got 'em."
    anon "Oh, c'mon... I insist."
    maria a_groceries_give "Well, alright then."
    show maria a_idle
    show anon a_grocery_bags
    with dissolve
    maria "Follow me, handsome."
    hide maria with dissolve
    maria "We're on the {b}third floor, room 302{/b}."
    anon "Got it."
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
