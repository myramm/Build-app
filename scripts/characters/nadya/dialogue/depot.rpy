label nadya_button_depot:
    $ renpy.dynamic(rng=random.random())

    pause .1
    show nadya f_surprised
    show svetlana f_surprised

    if rng < .33:
        show svetlana a_surprised
        "{i}*CRASH*{/i}" with hpunch
        show svetlana a_sides
    elif rng < .66:
        "{i}*Eeeeeeohhmmmm*{/i}" with hpunch
    else:
        "{i}*Glugglugglugglug*{/i}"
        show svetlana a_crossed

    show nadya a_angry f_angry:
        xoffset 675
        xzoom -1
    with {'master': dissolve}

    if rng < .66:
        nadya "Hey, be careful!"
    else:
        nadya "Hey, no drinking the merchandise!"

    show svetlana:
        xoffset 450
    with {'master': dissolve}

    if rng < .33:
        nadya "If you break vodka, I deduct from paycheck!"
    elif rng < .66:
        nadya "Forklift is not toy!"
    else:
        nadya "This is not Russia!"
        nadya "Work now, drink later!"

    svetlana f_eyeroll "What a bunch of idiots... " (show_native="Chto za kucha idiotov...")
    show anon a_wave behind nadya with {'master': dissolve}:
        xoffset -100
    anon "Hey, {b}Nadya{/b}."
    show nadya a_idle f_confused:
        xoffset 100
        xzoom 1
    show svetlana a_sides f_curious:
        xoffset -100
        xzoom 1
    with {'master': dissolve}
    nadya @ -m_talk "Hmm?"
    show svetlana f_happy
    nadya f_normal "Oh, hello, {b}[firstname]{/b}." (show_native="Oh, privet, {b}[firstname]{/b}.")
    show anon a_sides
    with {'master': dissolve}
    nadya "What brings you to warehouse?"

    menu nadya_button_depot.choice:
        "How's business?":
            jump nadya_button_depot.business
        "Hello, {b}Svetlana{/b}.":

            if M_svetlana.finished_state(S_sve01_lewd):
                jump nadya_button_depot.greet
            else:
                $ M_svetlana.trigger(T_sve01_init)
                jump nadya_button_depot.envy
        "Sex.":

            jump nadya_button_depot.sex
        "Just saying hello.":

            pass

    anon f_normal "I was just in the neighborhood and though I'd say hello."
    nadya f_confused "This is American dating ritual?"
    anon f_confused "Ehh, no?"
    nadya f_happy "Oh, so you make special visit because you like me, yes?"
    anon "Uhh, sure."
    anon f_normal "Yeah, let's go with that."
    svetlana f_smirk_back a_hips "I think the boy is in love." (show_native="Dumayu, mal'chik vlyublen.")
    nadya f_happy "Who could blame him?" (show_native="Kto mog yego vinit'?")
    nadya f_sexy "Why don't you come back this evening after work?"
    show svetlana f_smirk
    nadya "We can make sexy times until the sun rises."
    anon f_flirt "{i}*Gulp*{/i} Until the sun rises?"
    anon "Y-yeah, maybe..."
    nadya f_happy "Good."
    nadya "Later then."
    anon f_normal a_wave "See ya, {b}Nadya{/b}."
    pause
    anon a_idle "{b}Svet{/b}."
    svetlana a_wave "Farewell, {b}[firstname]{/b}." (show_native="Do svidaniya, {b}[firstname]{/b}.")
    hide anon with dissolve
    return


label nadya_button_depot.business:
    anon f_normal "How's the new business, Nadya?"
    nadya "Ehh, is good."
    nadya "The vodka makes big monies."
    show nadya a_angry f_angry:
        xoffset 675
        xzoom -1
    show svetlana f_concerned_back
    with {'master': dissolve}
    nadya "Despite the fact that my workers are idiots!" (show_native="Pri tom chto moi rabochiye idioty!")
    show nadya a_idle with dissolve
    pause
    nadya f_normal "I'm considering expansion maybe..."
    anon f_confused "Oh, yeah?"
    show nadya:
        xoffset 100
        xzoom 1
    show svetlana f_happy
    with {'master': dissolve}
    anon "More vodka or something different?"
    nadya "This is undecided."
    show anon f_normal
    nadya "I have many interests."
    nadya "Perhaps something for women would be good."
    nadya f_angry "I grow tired of stupid men!"
    show svetlana a_hips f_annoyed with {'master': dissolve}:
        xoffset 450
        xzoom -1
    svetlana "I agree." (show_native="Ya soglasen.")
    anon f_surprised "Huh."
    anon f_shy "Well, good luck with that, I guess..."
    show svetlana a_sides f_normal with {'master': dissolve}:
        xoffset -100
        xzoom 1
    nadya f_sexy "Heh, I do not need luck..."
    nadya "... I am Russian."
    show svetlana f_smirk_back
    nadya "We grab opportunity by the balls and squeeze."
    show anon a_behind_head
    show svetlana f_smirk
    with {'master': dissolve}
    anon "{i}*Gulp*{/i} R-right."
    show anon a_sides
    with {'master': dissolve}
    anon "Gotcha."
    jump nadya_button_depot.choice


label nadya_button_depot.envy:
    show anon a_wave f_normal with {'master': dissolve}
    anon "Hey, {b}Svet{/b}."
    show nadya a_sides f_surprised with {'master': dissolve}
    svetlana f_surprised "Ehh..."
    svetlana "... H-hello."
    nadya f_angry "Have you been flirting with my man?!" (show_native="Ty flirtoval s moim muzhchinoy?!")
    show anon a_surprised f_surprised_teeth
    show svetlana a_up f_timid:
        xoffset 450
        xzoom -1
    with {'master': dissolve}
    svetlana "No, I would never do that!" (show_native="Net, ya by nikogda etogo ne sdelal!")
    svetlana "I swear!" (show_native="Ya klyanus'!")
    show anon a_sides
    show svetlana a_sides
    show nadya a_crossed
    with {'master': dissolve}
    nadya @ -m_talk "Hmph."
    anon f_worried "Umm, is there a problem?"
    show nadya a_point_angry:
        xoffset -275
    show svetlana:
        xoffset -100
        xzoom 1
    with {'master': dissolve}
    nadya "You want make sexy times with {b}Svetlana{/b}?!"
    show anon f_worried_surprised a_surprised_up with {'master': dissolve}
    anon "WHAT?!"
    anon "N-no, I wasn't-"
    show nadya a_hips
    anon a_sides "Err, I mean I was... just trying to be polite... is all."
    nadya "You think she is pretty?"
    anon f_shy "Well, I mean... Yeah, she's pretty but I wasn't trying to-"
    show nadya a_finger
    show svetlana f_happy_down
    with {'master': dissolve}
    nadya "Prettier than me?!"
    anon f_surprised "Huh?!"
    anon "I didn't say-"
    nadya a_point "You want I should share your pretty cock with bodyguard, da?!"
    show anon a_rub f_shy of_blush
    show svetlana o_blush
    with {'master': dissolve}
    anon "Holy crap, did somebody turn the heat up or something?!"
    show svetlana f_timid_down
    anon "Because, it's like super hot in here all of a sudden..."
    nadya a_hips "You listen to me, American boy..."
    show anon f_surprised a_surprised
    show svetlana f_surprised
    with {'master': dissolve}
    nadya "... Nobody fucks {b}Svetlana{/b} without I say so!"
    nadya "Understand?!"
    show anon a_sides f_worried -of_blush
    show svetlana f_concerned
    with {'master': dissolve}
    anon "Look, seriously... I was just trying to be polite."
    nadya a_crossed @ -m_talk "Mhmm."
    pause
    show svetlana -o_blush with {'master': dissolve}
    nadya f_frowning "Very well."
    show nadya a_idle:
        xoffset 675
        xzoom -1
    show svetlana f_concerned_back
    with dissolve
    show nadya a_point with {'master': dissolve}:
        xoffset 100
        xzoom 1
    nadya "But I keep eyes on you, eh?"
    show svetlana f_concerned
    anon f_shy "Y-yeah, I got it."
    show nadya a_idle f_happy
    show svetlana f_normal
    with {'master': dissolve}
    nadya "Good."
    jump nadya_button_depot.choice


label nadya_button_depot.greet:


    jump nadya_button_depot.envy


label nadya_button_depot.sex:
    show anon a_behind_head f_shy of_blush with {'master': dissolve}
    anon "I was wondering... if... erm..."
    nadya f_sexy "Oh, you want make sexy times now?"

    if M_svetlana.finished_state(S_sve01_lewd):
        menu:
            "Yes please!":
                anon "Yes-"
            "With Svetlana?":

                if M_svetlana.once('ask_nadya'):
                    jump nadya_button_depot.svet
                else:
                    jump nadya_button_depot.wonder

    show anon a_sides f_surprised
    show svetlana f_timid:
        xoffset 450
        xzoom -1
    with {'master': dissolve}
    svetlana "Eh, pardon {b}Miss Chernyshevsky{/b} but {b}Katya{/b} has scheduled meeting with-"
    show anon f_worried_surprised
    nadya f_frowning "I am well aware of schedule!"
    nadya "{b}Katya{/b} can manage meeting on her own today."
    svetlana "D-da, of course."
    svetlana "Apologies."
    show anon f_shy
    nadya f_normal "Watch door."
    nadya "I take {b}[firstname]{/b} to cargo area for making sexy times."
    svetlana f_normal "As you wish, {b}Miss Chernyshevsky{/b}."
    show svetlana:
        xoffset -100
        xzoom 1
    show nadya a_point f_sexy:
        xoffset -275
    with {'master': dissolve}
    nadya "Come, we go now."
    show anon f_worried:
        xoffset -600
        xzoom -1
    hide nadya
    with {'master': dissolve}
    anon "Right behind you."
    hide anon with dissolve
    pause
    show svetlana a_crossed f_timid
    with {'master': dissolve}
    svetlana "{i}*Sigh*{/i}"

    scene expression background(304, 368, 4, l=L_warehouse_cargo) as stage
    show thug f_surprised
    show nadya a_crossed f_frowning:
        xoffset 150
        xzoom -1
    with fade
    pause
    jab "{b}Miss Chernyshevsky{/b}!"
    jab "I-"
    pause
    jab "Why you come storage room?!"
    nadya "Get out."
    jab f_confused "Get out?!"
    jab "But I haven't finished with-"
    show anon f_confused behind nadya with {'master': dissolve}:
        xoffset -100
    nadya f_angry "You giving back talk?!"
    show thug a_defensive f_concerned with {'master': dissolve}
    jab "N-no, I'm not-"
    show anon a_surprised f_surprised_teeth o_boner
    show thug f_wincing
    show nadya a_angry:
        xoffset 225
    nadya "{b}Jab{/b}, get the fuck out!" with hpunch
    show anon a_sides f_surprised_down
    show thug a_idle f_concerned
    with {'master': dissolve}
    jab "Da, of course!"
    show anon a_facepalm f_worried_down
    with {'master': dissolve}
    jab "Apologies!"
    show anon a_sides f_worried
    with {'master': dissolve}
    jab "I go now."
    show anon:
        xoffset -600
        xzoom -1
    show nadya a_hips f_eyeroll
    hide thug
    with dissolve
    pause
    show nadya a_hips f_frowning with {'master': dissolve}:
        xoffset -350
        xzoom 1
    nadya "He is loyal and good worker..."
    show anon:
        xoffset -100
        xzoom 1
    with {'master': dissolve}
    nadya "... But brain is size of peanut!"
    anon "If you say so."
    nadya "Is true."
    pause
    show nadya a_sides f_happy_back:
        xoffset 450
        xzoom -1
    with {'master': dissolve}
    nadya "Now..."
    show anon f_surprised_down
    show nadya f_sexy_down:
        xoffset -125
        xzoom 1
    with {'master': dissolve}
    nadya "... Let's see your beautiful cock, eh?"
    show anon f_worried_left of_blush with {'master': dissolve}
    anon "Umm, here?"
    show anon f_worried
    nadya f_sexy "Da."
    anon "Wouldn't you rather go up to your office?"
    show nadya a_crossed f_frowning with {'master': dissolve}
    nadya "No." (show_native="Nyet.")
    nadya "{b}Katya{/b} needs office for making important business."
    nadya "I would not cause interruption with sexy times."
    pause
    show nadya a_hips f_pouting with {'master': dissolve}
    nadya "Now, remove pants."
    anon "Alright."
    show nadya f_sexy_down
    anon f_worried_down "Umm..."
    show anon a_remove_shorts_boner -o_boner with dissolve
    show anon b_shirt_undress_bottom o_boner -of_blush
    show nadya a_sides f_surprised_down
    with dissolve
    pause
    show anon a_sides b_shirt f_worried -o_boner od_dick4 of_blush with {'master': dissolve}
    nadya f_sexy_down "Mmm, good boy."
    show anon f_shy
    pause
    show nadya a_idle f_sexy with {'master': dissolve}
    nadya "Your big cock makes me very excite..."
    show anon f_surprised_low
    show nadya a_undress1 f_sexy_down
    with dissolve
    show nadya b_dressed_undress2 with dissolve
    pause
    show anon f_flirt_low
    show nadya a_hips b_pantless o_pantless_cum_drip
    with {'master': dissolve}
    nadya f_sexy "... Come look..."
    show anon f_flirt
    hide nadya
    with dissolve

    call scene_nadya_sex_cargo.repeat
    $ unlock_scene('nadya', '03_unlocked')

    scene expression background(304, 368, 4, l=L_warehouse_cargo) as stage
    show nadya a_sides b_pantless f_happy:
        xzoom -1

    if _return == 'inside':
        show nadya o_pantless_cum_drip

    with fade
    nadya "Come..."
    show anon a_sides b_shirt f_shy_low:
        xoffset -50
        xzoom -1
    show nadya b_dressed_undress2 f_sexy_high -o_pantless_cum_drip
    with {'master': dissolve}
    nadya "... We go back to warehouse now."
    show anon f_shy
    show nadya a_undress1 b_dressed f_happy
    with dissolve
    pause
    show nadya a_hips with {'master': dissolve}
    anon f_worried "Wait a second..."
    show anon a_point_down f_confused_low:
        xoffset 450
        xzoom 1
    show nadya f_confused
    with {'master': dissolve}
    anon "... We're just gonna leave this mess here?"
    show anon f_disgusted_low
    nadya "Ehh, da?"
    show anon a_sides f_disgusted with dissolve:
        xoffset -50
        xzoom -1
    pause
    nadya f_normal "Do not concern yourself with mess."
    nadya "{b}Jab{/b} will clean."
    show anon a_surprised f_worried_surprised with {'master': dissolve}
    anon "{b}Jab{/b}?"
    pause
    show nadya f_confused
    anon "You're really gonna make him clean up my-"
    show anon a_sides f_surprised_left_low with dissolve
    pause
    anon f_worried "M-my uhh..."
    nadya f_sexy "Sexy time juices?"
    anon f_shy "Y-yeah."
    nadya f_laugh "Haha!"
    nadya f_normal "Of course."
    nadya "Is his job to clean up my messes."
    anon f_worried "Okay, but-"
    nadya "Do not be concerned with {b}Jab{/b}."
    nadya "Consider it penance for all the money he takes from you and friends... Eh?"
    show anon a_rub f_shy with {'master': dissolve}
    anon "Alright, I suppose that makes sense."
    show anon b_empty f_surprised_down
    show nadya b_dressed_kiss_cheek_shirt:
        xoffset -50
    show anon_overlay_dick_shirt_od_dick2 as dick:
        xoffset -50
        xzoom -1
    with dissolve
    pause
    show anon a_sides b_shirt f_happy
    show nadya a_sides b_dressed f_happy:
        xoffset 250
    hide dick
    with {'master': dissolve}
    nadya "This was fun."
    nadya "We do more later."
    anon "Sounds good."
    nadya "Farewell, {b}[firstname]{/b}." (show_native="Do svidaniya, {b}[firstname]{/b}.")
    show anon a_wave
    hide nadya
    with {'master': dissolve}
    anon "Farewell, {b}Nadya{/b}." (show_native="Do svidaniya, {b}Nadya{/b}.")
    pause
    show anon a_sides with dissolve
    pause .4
    show anon a_surprised_up_both f_surprised_down with dissolve
    pause
    show anon b_shirt_undress_bottom with dissolve
    show anon a_remove_shorts b_dressed with dissolve
    show anon a_sides f_surprised with dissolve
    pause
    show anon a_surprised f_surprised_left with dissolve
    pause
    show anon a_sides f_worried with dissolve
    hide anon with dissolve
    return 'afterglow'


label nadya_button_depot.svet:
    anon "W-with {b}Svetlana{/b}?"
    show anon a_sides
    with {'master': dissolve}
    nadya f_confused "{b}Svetlana{/b}, are you in the mood for sexy times?"
    show svetlana a_hips f_smirk:
        xoffset 450
        xzoom -1
    with {'master': dissolve}
    svetlana "I'm always in the mood for sexy times..."
    show nadya a_shoo f_happy
    with {'master': dissolve}
    nadya "Hehe, go."
    show nadya a_hips
    show svetlana f_happy
    with {'master': dissolve}
    nadya "Enjoy yourself."
    show anon a_empty b_empty f_surprised:
        xoffset -546
        xzoom -1
    show svetlana b_dressed_pull_anon:
        xoffset -500
        xzoom 1
    with {'master': dissolve}
    svetlana "Thank you, {b}Nadya{/b}." (show_native="Spasibo, {b}Nadya{/b}.")
    hide anon
    hide svetlana
    with {'master': dissolve}
    nadya "Don't break him." (show_native="Ne slomay yego.")
    svetlana "I won't!" (show_native="Ya ne budu!")

    scene expression background(512, 416, 2.8, l=L_warehouse_furnace) as stage
    show thug:
        xoffset -200
    with fade
    show svetlana b_dressed_pull_anon f_happy
    show anon a_empty b_empty f_surprised:
        xoffset -46
        xzoom -1
    show thug f_surprised
    with {'master': dissolve}
    pause
    show anon a_surprised b_dressed f_worried
    show svetlana b_dressed f_annoyed:
        xzoom -1
    show thug a_defensive
    with {'master': dissolve}
    svetlana "Beat it, {b}Jab{/b}!"
    show anon a_sides
    show thug a_sides f_concerned
    with {'master': dissolve}
    jab "What, again?!"
    show anon f_surprised
    show svetlana f_glaring
    pause
    show anon f_worried:
        xoffset 454
        xzoom 1
    show thug a_confused f_confused_down:
        xoffset 700
        xzoom -1
    show svetlana f_normal
    with {'master': dissolve}
    jab "... Bunch of assholes." (show_native="... Kucha pridurkov.")
    hide thug
    show svetlana a_undress f_happy_down
    with {'master': dissolve}
    pause
    show svetlana b_naked
    with {'master': dissolve}
    anon "I kinda feel bad for him."
    show svetlana b_naked_undress
    with {'master': dissolve}
    pause
    show anon:
        xoffset -46
        xzoom -1
    show svetlana a_sides b_naked f_happy
    with {'master': dissolve}
    svetlana "You can invite him back to watch if you want?"
    anon f_normal "Well, I don't feel {i}that{/i} bad..."
    svetlana @ f_laugh "Hehe!"
    svetlana "Now remove clothes, we must be quick."
    label nadya_button_depot.merge:
    show anon a_surprised f_shy_down
    with {'master': dissolve}
    anon "Oh, right."
    show svetlana f_smirk_low
    show anon b_shirt_undress_bottom
    with {'master': dissolve}
    pause
    show anon a_sides b_shirt f_flirt
    with {'master': dissolve}
    svetlana f_smirk "Lovely." (show_native="Prekrasnyy.")

    menu:
        "Blowjob.":
            anon "Maybe you could..."
            show anon f_flirt_down
            show svetlana f_curious
            pause
            show svetlana f_curious_low
            pause
            svetlana f_curious "You want I should suck you off?"
            anon f_flirt "Yes, please."
            show svetlana a_hips f_concerned
            with {'master': dissolve}
            svetlana "Hmm, I was hoping for something more... mutually gratifying."
            show anon a_surprised_up_both f_worried
            with {'master': dissolve}
            anon "Well, we don't have to-"
            svetlana f_smirk "... But I suppose you can owe me one."
            show anon a_sides f_flirt
            with {'master': dissolve}
            anon "Y-yeah, totally..."
            anon "... I'm always up for-"
            show anon od_dick2
            with {'master': dissolve}
            svetlana f_annoyed "Sit down and shut up."
            show anon a_salute f_worried_surprised od_dick_spring
            with {'master': dissolve}
            anon "Yes, ma'am!"
            hide anon
            show svetlana a_sides f_happy_down:
                xoffset -500
                xzoom 1
            with {'master': dissolve}
            pause

            call scene_svetlana_furnace_blowjob.repeat
            $ unlock_scene('svetlana', '01_unlocked', variant='repeat')
        "Sex.":

            anon "So you want to-"
            svetlana "Da."
            svetlana "I would ride you again, like before."
            show anon od_dick2
            show svetlana f_smirk_low
            with {'master': dissolve}
            anon "Y-yeah, sure..."
            show anon od_dick_spring
            with {'master': dissolve}
            anon "... Last time was amazing, we-"
            show anon od_dick4
            show svetlana a_hips f_smirk
            with {'master': dissolve}
            svetlana f_annoyed "Shut up and lie back."
            show anon a_salute f_worried_surprised
            with {'master': dissolve}
            anon "Yes, ma'am!"
            hide anon
            show svetlana a_sides f_happy_down:
                xoffset -500
                xzoom 1
            with {'master': dissolve}
            pause

            call scene_svetlana_furnace_cowgirl.repeat
            $ unlock_scene('svetlana', '02_unlocked', variant='repeat')

    scene expression background(512, 416, 2.8, l=L_warehouse_furnace) as stage
    show svetlana a_undress b_naked f_happy_down:
        xzoom -1
    show anon a_remove_shorts f_happy:
        xoffset -200
        xzoom -1
    with fade
    anon "Well, as usual... that was awesome!"
    show anon a_sides
    show svetlana b_dressed
    with {'master': dissolve}
    svetlana "I enjoy too."
    show svetlana a_sides f_happy
    with {'master': dissolve}
    svetlana "Your penis is excellent!"
    anon @ f_brag "You know, I never get tired of hearing that..."
    svetlana f_smirk "Heh, I should get back to {b}Miss Chernyshevsky{/b}."
    anon f_worried "Oh, right.."
    anon "I suppose I should get going as well."
    anon f_shy "Thanks for the uhh-"
    show anon a_behind_head
    with {'master': dissolve}
    anon "You know."
    hide anon
    show svetlana b_dressed_kiss
    with {'master': dissolve}
    anon "!!!"
    svetlana @ -m_talk "Mmm."
    pause
    show anon a_sides b_dressed f_flirt_grin:
        xoffset -200
        xzoom -1
    show svetlana b_dressed f_happy
    with {'master': dissolve}
    svetlana "My pleasure."
    show anon:
        xoffset 300
        xzoom 1
    show svetlana a_sides:
        xoffset 575
    with {'master': dissolve}
    pause
    hide svetlana
    show anon a_wipe f_drink
    with {'master': dissolve}
    anon @ -m_talk "{i}*Phew*{/i}"
    show anon a_sides f_tired_happy
    with {'master': dissolve}
    pause
    anon f_flirt_grin @ -m_talk "( From Russia with love, indeed. )"
    hide anon with dissolve
    return 'afterglow'


label nadya_button_depot.wonder:
    anon f_shy "So, hey... I was wondering..."
    nadya f_confused @ -m_talk "Hmm?"
    show anon a_sides
    with {'master': dissolve}
    anon f_shy_left "... The other day, when {b}Svetlana{/b} and I... You know..."
    show nadya f_frowning
    show svetlana a_fist_mouth f_glaring
    with {'master': dissolve}
    svetlana @ -m_talk "{i}*Clears throat*{/i}"
    show anon f_worried
    show svetlana a_crossed
    with {'master': dissolve}
    pause
    show anon f_worried_surprised
    pause
    anon "I uhh... w-was that a one time thing or-"
    show anon a_surprised_shoulders f_surprised_teeth
    show nadya a_point_angry f_angry:
        xoffset -275
    show svetlana a_facepalm f_eyeroll
    with {'master': dissolve}
    nadya "YOU PREFER {b}SVETLANA{/b} TO ME?!"
    show anon a_surprised_up_both f_worried_surprised
    show svetlana a_sides f_bored
    with {'master': dissolve}
    anon "W-what, NO!"
    show anon -of_blush
    with {'master': dissolve}
    anon "I didn't-"
    show nadya a_angry:
        xoffset -325
    with {'master': dissolve}
    nadya "YOU DID!"
    nadya "YOU SAY SO!"
    show anon a_cover_boner
    with {'master': dissolve}
    anon "N-no, no!"
    nadya "YOU LIKE {b}SVETLANA{/b}'S BIG TITS AND THINK HER PUSSY IS TIGHTER THAN MINE?!"
    show anon f_shock
    pause
    nadya "HUH?!"
    anon f_worried_surprised "I-"
    nadya "{b}SVETLANA{/b} HOLD HIM!"
    show anon f_surprised_teeth
    show nadya a_knife_pull
    with {'master': dissolve}
    svetlana f_concerned "Da, {b}Miss Chernyshevsky{/b}."
    show anon a_empty b_empty f_confused_back
    show svetlana b_dressed_restrain_anon:
        xoffset -218
        xzoom -1
    show nadya a_knife
    with {'master': dissolve}
    anon "W-wait, what are you-"
    show anon f_afraid
    show nadya a_knife_brandish
    with {'master': dissolve}
    nadya "I'M GOING TO CUT OFF YOUR BALLS AND SHOVE THEM UP YOUR ASS!!!"
    anon "NO, NO, NO!"
    anon f_worried_surprised "I don't prefer {b}Svetlana{/b} to you, I swear!!"
    anon "I was just trying to be inclusive!"
    nadya "I'LL PULL YOUR INTESTINES OUT THROUGH DICK HOLE!!!"
    anon f_afraid_close "Eeeep!"
    pause
    show nadya f_happy
    show svetlana f_happy
    pause
    show nadya a_knife f_laugh
    show svetlana f_laugh
    with {'master': dissolve}
    nadya "HAH!"
    show nadya b_dressed_laugh
    with {'master': dissolve}
    nadya "Hahahahaah!!!"
    show anon f_afraid_peek
    svetlana "Hehe!"
    anon f_surprised_low "Wha-"
    nadya "Ahahaah!!!"
    show anon f_surprised
    show nadya a_knife b_dressed f_happy
    show svetlana f_happy
    with {'master': dissolve}
    nadya @ f_happy "You should have-"
    show anon f_confused
    show nadya a_knife_pull
    with {'master': dissolve}
    nadya @ f_happy "Seen your face!!"
    show anon f_confused_low
    show nadya a_sides b_dressed_laugh f_laugh
    show svetlana f_laugh
    with {'master': dissolve}
    nadya "Hahahaah!"
    show anon a_ouch b_dressed f_disgusted_low
    show svetlana b_dressed
    with {'master': dissolve}
    svetlana "Hehe!"
    anon "... T-that was a joke?"
    show anon a_sides f_worried
    show nadya b_dressed f_happy
    show svetlana f_happy
    with {'master': dissolve}
    nadya "I don't care who you make sexy times with!"
    nadya f_pouting "What, you think we're exclusive?!"
    anon @ f_confused "N-no?"
    nadya f_normal "{b}[firstname]{/b}, I am head of Bratva..."
    nadya "... I will not be tied down to anyone."
    anon f_worried @ -m_talk "Umm..."
    show nadya a_hips
    with {'master': dissolve}
    nadya "I fuck who I want, when I want."
    nadya "Understand?"
    show anon a_point_back
    with {'master': dissolve}
    anon "... S-so it's okay if {b}Svetlana{/b} and I-"
    nadya f_happy "Of course!"
    show nadya a_shoo
    with {'master': dissolve}
    nadya "Go, go."
    show nadya a_sides
    with {'master': dissolve}
    nadya "Enjoy yourselves!"
    show anon a_empty b_empty f_surprised:
        xoffset -546
        xzoom -1
    show svetlana b_dressed_pull_anon:
        xoffset -500
        xzoom 1
    with {'master': dissolve}
    svetlana "Thank you, {b}Nadya{/b}." (show_native="Spasibo, {b}Nadya{/b}.")
    hide anon
    hide svetlana
    with {'master': dissolve}
    nadya "Don't break him." (show_native="Ne slomay yego.")
    svetlana "I won't!" (show_native="Ya ne budu!")

    scene expression background(512, 416, 2.8, l=L_warehouse_furnace) as stage
    with fade
    show svetlana b_dressed_pull_anon f_happy
    show anon a_empty b_empty f_surprised:
        xoffset -46
        xzoom -1
    with {'master': dissolve}
    pause
    show anon a_surprised b_dressed
    show svetlana b_dressed:
        xzoom -1
    with {'master': dissolve}
    anon "Were you in on that?!"
    svetlana "Of course, was my idea."
    anon f_skeptical "Seriously?"
    svetlana "Is good to remind you who is boss here, yes?"
    show anon a_sides f_unimpressed
    with {'master': dissolve}
    pause
    show svetlana a_undress
    with {'master': dissolve}
    svetlana "Impressive you didn't piss yourself."
    show anon f_unimpressed_low
    show svetlana b_naked f_happy_down
    with {'master': dissolve}
    anon "Yeah, thanks."
    show anon f_flirt_low
    show svetlana b_naked_undress
    with {'master': dissolve}
    pause
    show thug f_surprised behind anon:
        xoffset 150
    show svetlana a_sides b_naked f_normal
    with {'master': dissolve}
    jab "What is going on in furnace room?!"
    show anon f_surprised:
        xoffset 325
        xzoom 1
    with {'master': dissolve}
    svetlana f_annoyed "{b}Jab{/b} get lost!"
    show anon f_worried
    jab f_concerned "But this is my room..."
    show anon f_worried_left
    show svetlana a_hips
    with {'master': dissolve}
    svetlana "You don't have a room, idiot." (show_native="U tebya net mesta, idiot.")
    show thug f_angry
    svetlana "Now scram!"
    show anon f_worried
    pause
    show svetlana f_glaring
    pause
    show svetlana f_normal
    show thug a_confused f_confused_down:
        xoffset 700
        xzoom -1
    with {'master': dissolve}
    jab "I'm so sick of this. Can't get any peace!" (show_native="Zayebali, blyad'. Nigde v pokoye ne ostavyat!")
    hide thug
    with {'master': dissolve}
    pause
    show anon f_worried behind svetlana:
        xoffset -175
        xzoom -1
    with {'master': dissolve}
    anon "That was awkward."
    show svetlana a_sides
    with {'master': dissolve}
    svetlana "Never mind him."
    svetlana "Remove clothes, we must be quick."
    anon f_confused @ -m_talk "Hmm?"
    jump nadya_button_depot.merge
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
