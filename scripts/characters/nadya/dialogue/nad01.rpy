label nad01_lewd_nadya:
    show nadya b_naked_couch
    show anon a_behind_head b_sit f_shy with dissolve:
        xoffset -250
    anon "Umm..."
    anon a_idle f_shy_low "... Hi-low."
    show nadya f_confused
    pause
    anon f_shy "I err, mean... hello."
    nadya f_normal "Hello." (show_native="Zdravstvuyte.")
    nadya "I am please that you came."
    anon "Y-yeah, me too."
    pause
    anon "Were you and {b}Katya{/b} just-"
    show anon of_blush with {'master': dissolve}
    nadya f_sexy "Heh, wouldn't you like to know?"
    anon f_worried @ -m_talk "{i}*Gulp*{/i}"
    anon "S-so, what do you want from me?"
    nadya "I have job offer."
    show anon f_surprised -of_blush
    show nadya a_cig_lightup
    with dissolve
    pause
    show anon f_confused
    show nadya a_cig_smoking
    with {'master': dissolve}
    pause
    show nadya a_down_cig f_pouting o_smoke with dissolve
    pause
    show nadya f_sexy -o_smoke with {'master': dissolve}
    nadya "Is yours if it pleases you."
    anon "What kind of job offer?"
    nadya "You are resourceful man."
    nadya "Those are in short supply these days."
    pause
    nadya f_normal "As you can see, we are legitimate business now."
    nadya "And business is good."
    show anon a_point_self
    show nadya a_cig_smoking
    with {'master': dissolve}
    anon "Okay, but where do I come in?"
    show nadya a_down_cig f_pouting o_smoke
    with dissolve
    pause
    show anon a_idle
    show nadya f_normal -o_smoke
    with {'master': dissolve}
    nadya "Things will not always be so."
    nadya "In business, like in all things, there are obstacles to overcome."
    nadya "It is, how you say..."
    pause
    nadya "... Inevitability."
    show nadya a_cig_smoking with {'master': dissolve}
    anon "Go on."
    show nadya a_down_cig f_pouting o_smoke with dissolve
    pause
    show nadya f_normal -o_smoke with {'master': dissolve}
    nadya "So when these obstacles arise, it would be nice to know I can call on you for help."
    nadya "Should I require it."
    anon f_thinking a_thinking @ -m_talk "Hmm."
    show nadya a_cig_smoking with {'master': dissolve}
    anon f_confused a_idle "And if I refuse?"
    show nadya a_down_cig f_pouting o_smoke with dissolve
    pause
    show nadya f_normal -o_smoke with {'master': dissolve}
    nadya "Of course, you can always refuse."
    nadya "As I said before, we are now friends."
    show anon f_worried_surprised
    nadya f_angry "Unlike my father, piece of shit that he was..."
    show anon f_normal
    nadya f_normal "... I do not mistreat friends."
    show nadya a_cig_smoking with {'master': dissolve}
    anon a_thinking f_thinking_down "Interesting."
    show nadya a_down_cig f_pouting o_smoke with dissolve
    pause
    show nadya f_normal -o_smoke with {'master': dissolve}
    anon a_idle f_normal "So what's in it for me?"
    nadya f_happy "I am glad you ask."
    show nadya f_sexy
    pause
    nadya "You are very pretty man, {b}[firstname]{/b}..."
    show anon f_surprised
    nadya "... And I am woman with insatiable appetites."
    anon f_flirt "Oh?"
    nadya "I would very much like to make sexy times with you."
    show anon f_shy of_blush
    with {'master': dissolve}
    nadya "Regardless of your answer."
    anon "{i}*Gulp*{/i} S-sexy times?"
    nadya "Da."
    show anon f_shy_high
    show nadya a_cig_throw
    with dissolve
    pause
    show anon f_shy
    show nadya f_sexy b_naked_couch_open a_down
    with dissolve
    nadya "I would have you now."
    anon a_surprised f_surprised_low -of_blush "N-now?"
    nadya @ -m_talk "Mhmm."
    show anon a_idle f_surprised with {'master': dissolve}
    nadya "{b}Katya{/b} has skilled tongue but I would prefer you to finish me."
    nadya "Remove your clothes."
    anon a_idle f_flirt "O-okay."
    show anon a_remove_shorts1 f_shy_down with dissolve
    pause
    show nadya f_surprised_low
    show anon b_sit_back_remove_shorts2 od_dick_spring
    with {'master': dissolve}
    nadya "!!!"
    show anon b_sit_naked_remove_shirt od_dick2 with dissolve
    nadya "I did not expect this..." (show_native="Ya etogo ne ozhidal ...")
    show anon a_idle b_sit_naked f_normal with dissolve
    nadya "You're very large!"
    show anon f_shy_down
    pause
    anon f_shy "Oh, umm... thanks."
    nadya f_sexy "Come to me."
    show anon a_idle b_sit_naked_up f_shy_low od_naked_dick3:
        xoffset 0
    with dissolve
    pause

    call scene_nadya_blowjob
    $ unlock_scene('nadya', '01_unlocked')

    call scene_nadya_sex_office
    $ unlock_scene('nadya', '02_unlocked')

    call nadya_button_stage
    show nadya b_naked_couch a_cig_smoking
    show anon b_sit_back_remove_shorts2 f_shy_down od_dick1:
        xoffset -250
    with fade
    pause
    show anon a_remove_shorts1 b_sit
    show nadya a_down_cig f_pouting o_smoke
    with dissolve
    pause
    show anon a_idle b_sit f_confused
    show nadya f_normal -o_smoke
    with {'master': dissolve}
    nadya "So you will take job?"
    anon "Oh, umm..."
    anon "... Can I think about it?"
    show anon f_shy
    nadya "Da."
    nadya "Take all the time you need."
    show nadya a_cig_smoking with dissolve
    pause
    show nadya a_down_cig f_pouting o_smoke with dissolve
    pause
    show nadya f_sexy -o_smoke with {'master': dissolve}
    nadya "I hope you will return soon, for more sexy times?"
    anon f_flirt "Y-yeah, I think I will."
    nadya "This is good."
    nadya "I enjoy your cock very much."
    anon f_flirt_grin @ f_laugh "Heh, thanks."
    pause
    anon f_normal "So, goodbye... I guess?"
    nadya f_happy "Farewell, {b}[firstname]{/b}." (show_native="Do svidaniya, {b}[firstname]{/b}.")
    hide anon with dissolve
    show nadya a_cig_smoking with dissolve

    scene expression background(480, 272, 7, l='warehouse_main_vodka', o=1) as stage
    show svetlana b_dressed:
        xoffset -400
    with fade
    show anon with dissolve:
        xoffset 150
        xzoom -1
    anon f_surprised a_surprised_up_both "Oh, you're still here?"
    show svetlana with dissolve:
        xoffset 150
        xzoom -1
    svetlana "Da."
    show anon a_sides with dissolve
    pause
    svetlana "{b}Miss Chernyshevsky{/b} pays me to bodyguard."
    svetlana "If she is inside, I am here also."
    anon a_sides f_shy "I see."
    pause
    svetlana f_smirk "Sounds like you have happy sexy times, hmm?"
    anon a_surprised f_worried m_talk of_blush "Y-you could hear us?"
    show anon a_cover_boner3 f_shy_cringe -m_talk -of_blush with {'master': dissolve}
    svetlana f_laugh a_sides "Heh, da."
    show anon a_sides f_tired of_blush with {'master': dissolve}
    svetlana f_happy "{b}Miss Chernyshevsky{/b} is quite loud when she makes orgasm..."
    svetlana f_smirk "... And you give her many."
    anon f_normal @ f_flirt "Y-yeah."
    svetlana f_happy "This is good."
    svetlana "She is difficult woman to please."
    show anon -of_blush with dissolve
    pause
    svetlana f_curious a_hips "Is true you will be working with us?"
    anon f_surprised "She told you about that?"
    svetlana f_normal "Not in so many words..."
    svetlana "... But I am hearing things."
    pause
    svetlana "She offers job, yes?"
    anon f_normal "She did..."
    anon f_shy "... But to be honest, I'm not sure it's a good idea."
    anon "My father got involved with hers and it cost him his life."
    svetlana f_timid "{b}Miss Chernyshevsky{/b} is not her papa."
    svetlana "She is good woman."
    anon f_normal a_idle "You think so?"
    svetlana f_normal "I do."
    svetlana "She does not deal in drugs or slaves."
    svetlana "Legitimate business woman."
    anon "Yeah, that's what I've been hearing."
    svetlana f_smirk "{b}Katya{/b} says she is gentle lover as well."
    anon a_surprised f_surprised @ f_shock -m_talk "!!!"
    svetlana "Likes to cuddle and be little spoon."
    svetlana @ f_laugh "Haha!"
    anon a_behind_head f_shy of_blush "I uhh..."
    pause
    anon "... I need some time to consider."
    show anon a_sides with {'master': dissolve}
    svetlana f_happy "Oh, very well..."
    svetlana "... But you should take job."
    svetlana "She needs good man like you beside her."
    show anon -of_blush with {'master': dissolve}
    anon "We'll see what the future brings."
    pause
    anon f_normal "For now, I'd best be getting on my way."
    svetlana a_sides "Farewell, {b}[firstname]{/b}." (show_native="Do svidaniya, {b}[firstname]{/b}.")
    anon a_wave "Goodbye, {b}Svet{/b}."
    hide anon with dissolve

    scene expression background(l='warehouse', o=1) as stage with fade
    show anon with dissolve
    anon @ -m_talk "( Well, that was unexpected... )"
    anon f_thinking a_thinking @ -m_talk "( I'm not sure about working together with her. )"
    anon @ -m_talk "( She seems more trustworthy than her father, to be sure... )"
    anon @ -m_talk "( ... But it still feels risky. )"
    pause
    anon f_normal a_pocket @ -m_talk "( At least she's not pressuring me to make a decision right away. )"
    anon @ -m_talk "( I've got all the time in the world to consider it. )"
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
