label ano26_talk_liu:
    show liu f_worried a_holdup
    show anon of_ski_mask f_angry a_tiny_gun with dissolve
    anon "You there!"
    anon f_worried "Umm... pretty girl, behind the counter!"
    liu f_confused "Y-yeah?"
    anon a_behind_head "I uhh..."
    pause
    anon a_tiny_gun f_angry "... I need you to do exactly what I say, understand?"
    liu f_wincing @ -m_talk "!!!"
    liu f_frightened "Yes, sir!"
    anon a_tiny_gun_move "You can start by coming out from behind that desk!"
    show anon a_tiny_gun
    show liu f_ashamed_down
    with {'master': dissolve}
    liu "Oh, umm..."
    pause
    anon "C'mon, I don't have all day!"
    liu f_worried "O-okay."
    show anon f_surprised
    show liu b_dressed_desk_jump1
    with dissolve
    anon @ -m_talk "!!!"
    hide liu
    show liu b_dressed_desk_jump2 f_worried_down
    with {'master': dissolve}
    anon f_surprised "Whoa, don't do that... you're gonna-"
    show liu b_dressed_desk_jump3 f_nervous_down with dissolve
    pause .3
    show anon f_shock_low
    show liu b_dressed_jump_fall
    with fastdissolve
    liu "!!!"
    hide liu
    show anon f_hurt
    with hpunch
    pause
    anon a_tiny_gun_down f_worried_low "... Fall."
    pause
    anon "Are you alright?"
    show liu b_dressed_bend
    with dissolve
    liu "Y-yeah, I think so."
    show anon f_confused
    show liu a_hold_arm b_dressed f_ashamed_down o_blush
    with dissolve
    anon "You could have just walked around..."
    liu f_annoyed "Well, I wanted it to look convincing for the cameras!"
    anon f_worried "Oh, right."
    anon "T-that makes sense, I guess..."
    pause
    show liu f_confused
    anon "Erm... speaking of..."
    show anon a_tiny_gun f_angry
    show liu a_holdup f_frightened -o_blush
    with dissolve
    pause
    liu "Do you have to point it right at me?"
    anon f_worried "Don't worry, it's not loaded."
    liu f_worried "Oh."
    liu "Well... o-okay then."
    anon f_normal "You look nice today."
    liu f_happy "Heh, thanks."
    anon f_angry "Now, where's the vault?!"
    liu f_worried "D-downstairs!"
    anon f_skeptical "Good girl."
    anon a_tiny_gun_move m_talk "Take me there..."
    show liu f_wincing
    anon a_tiny_gun f_angry -m_talk "... And no funny business, you got it?!"
    liu f_frightened "Yes, of course!"
    hide liu
    show anon f_flirt:
        xoffset -500
        xzoom -1
    with {'master': dissolve}
    anon "Mmm, you smell good too."
    liu "Hehe."
    hide anon with {'master': dissolve}
    anon "How are you doing over there, {b}Tony{/b}?"

    scene expression background(256, 576, 8., l=L_bank_lobby) as stage
    show bankguard b_dressed_sleep
    show tony b_casual a_gun_lower o_ski_mask f_angry
    with fade
    tony "This is pathetic."
    show tony a_gun_poke with dissolve
    show tony a_gun_lower with dissolve
    show tony a_gun_poke with dissolve
    show tony a_gun_lower with dissolve
    pause
    show tony a_gun_down f_sad with {'master': dissolve}:
        xoffset 500
        xzoom -1
    tony "You know, I think this guy might be dead."
    liu "No, he's just old."
    liu "He'll be like that until lunch time."
    tony "Should I even bother tying him up?"
    anon "Better safe than sorry, don't you think?"
    tony "{i}*Sigh*{/i} Yeah, I suppose."
    show tony with dissolve:
        xoffset 0
        xzoom 1
    pause
    tony "Jesus, I feel like an asshole."
    show tony with {'master': dissolve}:
        xoffset 500
        xzoom -1
    tony "You two go on ahead."
    tony "I'll meet ya down there in a second."
    anon "Alright."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
