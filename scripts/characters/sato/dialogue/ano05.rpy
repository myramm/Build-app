label ano05_cell_sato:
    return


label ano05_cell_sato.fail:
    show anon a_point f_surprised with {'master': fastdissolve}
    anon "Look! A three-headed monkey!"
    show sato:
        flip
        xoffset 520
    show anon b_dressed_bending_phone
    with dissolve
    sato "A three-headed wh-"
    $ display.toast(dex_fail)
    show sato f_confused with hpunch:
        unflip
        xoffset 0
    sato f_angry @ f_confused "Hey, don't touch that!"
    show anon f_surprised_low a_surprised_up_both b_dressed with dissolve
    show sato f_normal
    anon a_behind_head f_sad_down "Oh, ehh... Sorry."
    sato "That's my daughter's phone."
    sato f_confused "She didn't send you up here to retrieve it, did she?"
    anon f_worried "N-no, sir."
    anon "I was just curious why a man like you had such a girly phone sitting on his desk."
    sato f_normal "She can't seem to tear herself away from it during work hours, so I had to confiscate it."
    anon "Gotcha."
    sato "I'll give it back to her once she's made her first sale."
    hide anon with dissolve
    return


label ano05_cell_sato.pass:
    anon @ a_point "That's a really neat sword you have up there!"
    show sato with dissolve:
        flip
        xoffset 520
    sato @ -m_talk "Hmm?"
    show anon b_dressed_bending_phone with dissolve
    pause .5
    show anon f_grin a_phone_josephine_give b_dressed
    hide phone
    with dissolve
    $ display.toast(dex_pass)
    anon @ -m_talk "( I'll take that. )"
    show anon f_shy_down a_idle with dissolve
    pause
    show anon f_grin
    sato "Oh, yes!"
    show sato f_smiling:
        unflip
        xoffset -30
    show anon f_normal
    with dissolve
    sato "Can you believe I won that a carnival?"
    anon f_surprised "Really?"
    sato "Yes, indeed."
    sato "Took nearly forty dollars at the quarter toss, but {b}Josephine{/b} insisted that I win it for her."
    anon "Is it real?"
    sato "Nah, it's just a replica."
    anon f_unimpressed "Oh."
    sato "It's got Hattori Hanzō's signature on it though!"
    anon f_confused "Hattori Hanzō?"
    anon "Who's that?"
    sato "No idea, really..."
    sato "... But I suspect he's someone who signs swords."
    pause
    anon f_normal "Right."
    anon @ a_wave "Well, carry on then."
    hide anon with dissolve

    $ player.go_to(L_dealership_showroom)
    scene expression player.location.background_blur with fade
    show anon f_grin with dissolve
    anon @ -m_talk "( Alright, that wasn't so hard. )"
    anon @ -m_talk "( I should get this phone back to {b}Josephine{/b} now. )"
    hide anon with dissolve
    return 'josie_phone'
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
