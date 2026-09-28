label con01_init_iwanka:
    anon f_worried "Can I ask you something?"
    iwanka f_annoyed "It's not about my father again, is it?"
    anon "N-no, it's nothing like that..."
    anon "I was hoping I could talk to you about the maid working downstairs?"
    iwanka @ f_eyeroll "The maid?"
    anon "Yeah."
    iwanka "I try not to socialize with the help..."
    pause
    anon "It's just, your parents are kinda cruel to her, and I was hoping-"
    iwanka f_bored "I gotta be honest with you right now, {b}[firstname]{/b}, this is really boring..."
    anon "Oh."
    pause
    anon @ a_behind_head "Umm..."
    iwanka f_suspicious "Hey, have you ever thought about updating your look?"
    anon f_confused "Huh?"
    iwanka f_normal "I mean, this look you've cultivated is... Well, cute.. I guess..."
    iwanka "... In a sort of, hobo riding the rails kind of way."
    anon f_unimpressed "{b}Iwanka{/b}, I'd really like to get back to this {b}Consuela{/b} problem..."
    iwanka "Yeah, yeah, yeah... Hold on one second while I work my magic!"
    iwanka f_thinking "Hmm."
    iwanka f_smirk "I'm thinking you would look AMA-ZING in some Huge-Go Boss or Coochie!"
    iwanka "Is there a place we could buy those brands around here?"
    anon "Ehh, no."
    iwanka @ f_eyeroll "Eugh, of course there isn't!"
    iwanka f_annoyed "This town is like a freaking prison..."
    iwanka "... On planet bullshit."
    anon f_worried @ -m_talk "You're not gonna help me, are you?"
    iwanka f_thinking "I wonder if there's any off-brand equivalents?"
    anon f_sad_down "{i}*Sigh*{/i} Forget it."
    iwanka "Maybe we could order you something online?"
    hide anon with {'master': dissolve}
    iwanka f_excited "I think Barmani does online sales."
    iwanka @ f_laugh "Like, oh em gee!"
    iwanka "If a cute guy walks in wearing Barmani... My panties just instantly hit the floor!"
    iwanka @ f_laugh "Hehe, know what I mean?"
    iwanka f_normal @ -m_talk "Hmm?"
    iwanka f_suspicious "Where did he go?"
    hide anon with dissolve

    $ player.go_to(L_rump_lobby)
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
