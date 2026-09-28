label nadya_pregnancy_notify:
    scene expression player.location.background
    "{i}*Brrrzzzt* *Brrrzzzt*{/i}"

    scene expression game.timer.image('location_warehouse_office_couch{}') as underlay:
        xoffset -671
    show nadya a_phone_talk b_dressed_couch:
        xoffset -500

    $ renpy.dynamic(stage=player.location.background_phone)
    show expression stage as stage
    show anon f_confused with dissolve:
        xzoom -1
    anon @ -m_talk "Hmm?"
    show anon a_phone f_normal_low with dissolve
    pause
    show anon a_phone_talk f_normal with dissolve:
        xoffset 500
        xzoom 1
    show expression stage as stage at phoneleft with phoneleft.show
    anon "{b}Nadya{/b}?"
    nadya "Da, is me."
    anon "Wow, I don't think you've ever called me before... Not once."
    anon "Is everything alright?"
    nadya f_happy "I have glorious news!"
    nadya "You are now papa to future leader of Bratva!"
    anon f_confused "Huh?"
    nadya "You... Are papa."
    anon "What are you talking about?"
    nadya f_eyeroll "Ugh, okay... I explain slowly...."
    nadya f_worried "... We make lots of sexy times, da?"
    anon "Yeah?"
    nadya "And you shoot your sexy times juices deep inside pussy..."
    anon "Uh huh?"
    nadya "... This makes baby."
    anon f_surprised_teeth @ -m_talk "!!!"
    anon f_shy "S-so, you're pregnant?!"
    nadya f_happy "Da, and you are papa."
    pause
    nadya f_sexy "I will be expecting child support payment in the amount of one million dollars."
    anon f_surprised "WHAT?!" with hpunch
    nadya "You have one month or I kill your friends..."
    nadya "... Understand?"
    anon f_worried_surprised "Wha- No!"
    anon "I can't come up with-"
    nadya f_laugh "Hah!!"
    nadya f_happy "Relax, pretty man... is joke!"
    show anon b_dressed_catch_breath
    with {'master': dissolve}
    nadya "I don't need monies."
    anon "Hah... hah..."
    show nadya f_confused
    pause
    anon "Oh, jesus..."
    pause
    show anon b_dressed f_unimpressed with dissolve
    pause
    anon "... You almost gave me a heart attack!"
    nadya f_laugh "Hahahaahaa!"
    nadya f_happy "You forget, I am legitimate business woman now."
    show anon f_tired
    nadya "I make monies for infinite babies."
    nadya "Is no problem."
    anon f_shy "R-right, yeah."
    anon "Phew!"
    nadya f_frowning "But know this..."
    nadya "... You will be good papa to this child or I cut off your beautiful cock!"
    anon "Heh, is that another joke?"
    nadya "No." (show_native="Nyet.")
    show anon f_worried_surprised
    nadya "This time is serious."
    show anon f_shock
    nadya "I will cook it in warehouse furnace and place in hotdog bun..."
    nadya "... Apply relish and then make you eat it!"
    show anon f_surprised_down o_boner with {'master': dissolve}
    anon @ -m_talk "..."
    nadya "Understand?!"
    anon f_worried "{i}*Gulp*{/i} Y-yes?"
    nadya f_happy "Good!"
    nadya "Then we are done talking."
    pause
    nadya "Come by warehouse and we'll celebrate."
    anon "O-okay."
    nadya "Farewell, {b}[firstname]{/b}" (show_native="Do svidaniya, {b}[firstname]{/b}.")
    show nadya a_phone with {'master': dissolve}
    anon "See ya, {b}Nadya{/b}."
    show expression stage as stage with {'master': phoneleft.hide}
    "{i}*Beep*{/i}"
    show anon a_phone f_worried_low with dissolve
    anon @ -m_talk "( Okay, that woman is terrifying... )"
    show anon a_pocket f_worried with dissolve:
        xoffset 0
        xzoom -1
    show anon a_surprised f_surprised_down with {'master': fastdissolve}
    anon @ -m_talk "( ... And why does this keep happening?! )"
    show anon a_sides f_thinking_down with {'master': dissolve}
    anon @ -m_talk "( I should maybe seek counseling. )"
    hide anon with dissolve
    return True


label nadya_pregnancy_notify.repeat:
    scene expression player.location.background
    "{i}*Brrrzzzt* *Brrrzzzt*{/i}"

    scene expression game.timer.image('location_warehouse_office_couch{}') as underlay:
        xoffset -671
    show nadya a_phone_talk b_dressed_couch:
        xoffset -500

    $ renpy.dynamic(stage=player.location.background_phone)
    show expression stage as stage
    show anon f_confused with dissolve:
        xzoom -1
    anon @ -m_talk "Hmm?"
    show anon a_phone f_normal_low with dissolve
    pause
    show anon a_phone_talk f_normal with dissolve:
        xoffset 500
        xzoom 1
    show expression stage as stage at phoneleft with phoneleft.show
    anon "{b}Nadya{/b}?"
    nadya "Da, is me."
    anon f_confused "Is everything alright?"
    nadya "I have glorious news!"
    nadya f_happy "We are to have another child."
    anon f_surprised "Another one?!"
    nadya @ -m_talk "Mhmm."
    anon f_normal "That's wonderful!"
    nadya "Come by warehouse and we'll celebrate."
    anon "O-okay."
    nadya "Farewell, {b}[firstname]{/b}" (show_native="Do svidaniya, {b}[firstname]{/b}.")
    anon "See ya, {b}Nadya{/b}."
    show expression stage as stage with {'master': phoneleft.hide}
    "{i}*Beep*{/i}"
    show anon a_phone f_normal_low with dissolve
    anon @ -m_talk "( I guess I'm going to be a papa again... )"
    anon f_grin @ -m_talk "( ... How exciting! )"
    hide anon with dissolve
    return True


label nadya_pregnant_labor_1:
    scene expression player.location.background_blur
    show anon f_normal with dissolve
    anon "Looks like I got a text."
    hide anon with dissolve
    return


label nadya_pregnant_labor_2:
    scene expression player.location.background_blur
    if player.location != L_map:
        show anon f_surprised a_phone with dissolve
    anon "{b}Nadya{/b} had the baby?!"
    anon "Holy crap!"
    pause
    anon "I'd better head to {b}the clinic{/b} to check on them."
    if player.location != L_map:
        hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
