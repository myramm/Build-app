label ano13_clue_home_attic_evidence:
    scene expression background(696, 436, 4.) as stage
    show anon f_worried_low with dissolve
    anon @ -m_talk "( This must be the box of evidence. )"

    if not M_anon.finished_state(S_ano13_hint):
        anon @ -m_talk "( It looks like {b}[deb_name]{/b} didn't even open it... )"

        pause
        anon f_thinking @ -m_talk "( Maybe she couldn't bring herself to look? )"

    show anon b_dressed_pickup with dissolve
    anon @ -m_talk "Hmm."

    show anon b_dressed f_looking_down a_box_attic with dissolve
    pause
    anon a_box_attic_take @ -m_talk "( I thought there'd be more here... )"

    pause
    anon @ a_box_attic_cloth f_worried_low -m_talk "( Some of {b}Dad{/b}'s clothes. )"

    pause
    anon f_surprised_low a_box_attic_bowling "Whoa."

    anon f_shy_low @ -m_talk "( This is the trophy {b}Dad{/b} and I won in that father-son bowling league when I was twelve. )"

    anon @ -m_talk "( We must have played a thousand frames that summer... It was so much fun! )"

    pause
    anon @ -m_talk "( I was upset when we finished third but {b}Dad{/b} was really proud. )"

    anon @ -m_talk "( He told me that it didn't matter where we finished. )"

    anon @ -m_talk "( The important thing was that we had fun and spent some quality time together. )"

    pause
    anon a_box_attic_take f_shy_down @ -m_talk "( I wonder what else is in here? )"

    pause
    anon a_box_attic_pic2 f_shy_low @ -m_talk "( Hey, I remember this! )"


    scene expression background(840, 448, 10.) as stage
    show closeup_picture2
    with fade
    anon "( The carnival was in town and {b}Dad{/b} decided we should all go and have some fun. )"

    anon "( {b}[jen_name]{/b} was too scared to get on the ferris wheel so {b}Dad{/b} took her for cotton candy while {b}[deb_name]{/b} and I rode. )"

    pause
    anon "( Look how happy she was... )"

    pause

    scene expression background(696, 436, 4.) as stage
    show anon a_box_attic_pic2 f_shy_low
    with fade
    anon @ -m_talk "( I wonder if she would like to have this? )"

    anon a_box_attic_take f_shy_down @ -m_talk "( Okay, next up we have... )"

    pause
    anon f_surprised_down "Mustahil!"

    anon f_shy_low a_box_attic_chicken @ -m_talk "( This is the rubber chicken I gave to {b}Dad{/b} for Father's Day when I was seven years old! )"

    anon @ f_laugh -m_talk "( Hah, I can't believe he kept this... )"

    anon @ -m_talk "( {b}[deb_name]{/b} gave {b}[jen_name]{/b} and I ten dollars and let us pick out our own gifts. )"

    anon @ -m_talk "( {b}[jen_name]{/b} got him a mustache comb and a can of Dapper Dan hair treatment... )"

    anon @ -m_talk "( ... And I got him this rubber chicken. )"

    pause
    anon @ -m_talk "( {b}[jen_name]{/b} thought it was stupid but {b}Dad{/b} said he loved it. )"

    anon @ -m_talk "( It sat on his nightstand for an entire year. )"

    pause
    anon @ -m_talk "( I guess it ended up on his desk at work. )"

    anon f_sad_down @ -m_talk "{i}*Mengendus*{/i}"

    anon @ -m_talk "( Oh man, this is bringing up a lot of memories... )"

    anon a_box_attic_take f_looking_down @ -m_talk "( What else do we have? )"

    pause
    anon a_box_attic_pic1 f_sad_smile_down @ -m_talk "..."

    scene expression background(840, 448, 10.) as stage
    show closeup_picture3_framed
    with fade
    anon "( This is from one of our family camping trips. )"

    anon "( {b}Dad{/b} and I used to take this little boat out on the lake and fish all morning. )"

    anon "( We called it \"The Dink\" and it was the perfect size for the two of us. )"

    pause
    anon "{i}*Mengendus*{/i}"

    anon "( {b}[deb_name]{/b} would make us bacon and egg sandwiches and we'd share a big thermos of coffee... )"

    anon "( ... And {b}[jen_name]{/b} would always beg to go with us but {b}Dad{/b} would tell her it was our special father-son bonding time. )"

    pause

    scene expression background(696, 436, 4.) as stage
    show anon a_box_attic_pic1 f_sad_down
    with fade
    anon @ -m_talk "{i}*Mengendus*{/i}"

    anon @ -m_talk "( He always had her help him with the fish fry though. )"

    anon @ -m_talk "( She'd greet us with a big smile on the dock when we came back with our catch. )"

    pause
    anon a_box_attic_pic1_eyes @ -m_talk "( Ugh, this was a bad idea... )"

    anon @ -m_talk "( ... It's just making me emotion- )"

    show anon a_box_attic_pic1_drop f_surprised_down with fastdissolve
    pause
    show anon a_box_attic f_shock_down with {'master': dissolve}
    "{i}*Crunch*{/i}"

    anon f_surprised_down "Astaga!"

    show anon b_dressed_pickup with dissolve:
        xoffset -200
    anon "Tidak!"


    scene expression background(840, 448, 10.) as stage
    show closeup_picture3_broken
    with fade
    anon @ -m_talk "( Ah, man... It's broken. )"

    pause
    anon @ -m_talk "Hmm?"

    anon @ -m_talk "( What's that peeking out the side? )"


    scene expression background(696, 436, 4.) as stage
    show anon a_box_attic_pic1_look f_surprised_low
    with fade
    anon @ -m_talk "( There's something else in the frame, under the picture of {b}Dad{/b} and I... )"

    show anon a_box_attic_photo with dissolve
    anon "What the hell?!"


    scene expression background(840, 448, 10.) as stage
    show closeup_picture4
    show closeup_picture4_key
    with fade
    anon @ -m_talk "( That's {b}Dad{/b} with {b}Mayor Rump{/b}! )"

    anon @ -m_talk "( I wonder when this was taken? )"

    pause
    anon @ -m_talk "( And who's this other guy?! )"

    anon @ -m_talk "( He looks shady as hell! )"

    pause

    scene expression background(696, 436, 4.) as stage
    show anon a_box_attic_photo f_thinking
    with fade
    anon @ -m_talk "( Could this be the mob boss? )"

    show anon f_worried_low
    pause
    anon @ -m_talk "( The cops must have missed this too. )"

    anon @ -m_talk "( I can't imagine they would have sent it back to us. )"

    anon a_idle f_worried @ -m_talk "( I should {b}get this to Tony{/b}, and see what he makes of it. )"

    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
