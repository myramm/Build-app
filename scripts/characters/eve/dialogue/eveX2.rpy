label eveX2_bath_eve:
    scene location_tattoo_bathroom_shower
    show eve a_empty b_naked_shower f_normal_down:
        xoffset 250
        xzoom -1

    if M_eve.get('biggus_dickus'):
        show eve od_dick01
    else:
        show eve od_scar

    show eve_arms_naked_shower_a_scrub as eve_arms:
        xoffset 250
        xzoom -1
    show location_tattoo_bathroom_shower_steam as steam
    pause
    show anon b_naked f_flirt_grin od_naked_dick1 behind eve
    with {'master': dissolve}
    pause
    show anon a_empty f_flirt:
        xoffset 90
    show anon_arms_naked_a_hips_eve as anon_arms behind eve_arms:
        xoffset 90
    with {'master': dissolve}
    anon "Hey there, beautifu-{w=.25}{nw}"
    hide eve_arms
    show eve a_surprised f_surprised_right m_talk
    extend "" with hpunch
    show anon a_surprised f_worried_surprised
    show eve a_cover f_surprised_sad -m_talk:
        xoffset -250
        xzoom 1
    hide anon_arms
    with {'master': dissolve}
    anon "W-whoa, relax..."
    show eve f_confused
    show anon a_sides f_happy
    with {'master': dissolve}
    anon "... It's just me."
    eve f_angry "Jesus, you scared me!"
    anon f_brag "Yeah, I noticed..."
    anon "... Heh, you about jumped out of your skin."
    show anon f_laugh
    pause
    show anon a_sides_nervous f_hurt
    show eve a_punch:
        xoffset -310
    eve "It's not funny!" with hpunch
    show anon a_defensive f_worried:
        xoffset 60
    show eve a_cover:
        xoffset -250
    with {'master': dissolve}
    anon "Ouch, I'm sorry!"
    eve f_concerned "Are you trying to give me a heart attack?!"
    anon "N-no."
    show anon a_sides
    with {'master': dissolve}
    anon "I didn't mean to scare you, honest..."
    anon "... I just wanted to join you."
    eve "Well, that's fine... just, maybe don't sneak up on me next time!"
    anon "Alright, noted."
    pause
    show eve a_crossed f_thinking_down
    with {'master': dissolve}
    eve "Tch, now where did the soap get off to?"
    pause
    show eve behind anon
    show anon a_point_down_other f_normal_low:
        xoffset 80
    with {'master': dissolve}
    anon "I think it fell over there."
    show anon a_sides behind eve
    show eve a_hip:
        xoffset 350
        xzoom -1
    with {'master': dissolve}
    pause
    eve "Ah."
    show anon a_surprised f_surprised_down
    show eve b_naked_shower_pickup02:
        xoffset 150
    with {'master': dissolve}
    pause
    show anon a_sides f_flirt_down
    show eve b_naked_shower_pickup
    with {'master': dissolve}
    eve "Geez, it's really slippery..."
    show anon od_naked_dick_grow
    with {'master': dissolve}
    pause
    show eve a_scrub b_naked_shower f_normal_down:
        xoffset 350
    with {'master': dissolve}
    eve "... So hey, how would you feel about going out for breakfast or something?"
    pause
    eve "{b}[firstname]{/b}?"
    show eve a_scrub02 f_confused_right
    pause
    show eve a_crossed_soap f_confused:
        xoffset -250
        xzoom 1
    with {'master': dissolve}
    eve "Are you listening to me?"
    pause
    show eve a_hip f_nervous_down
    with {'master': dissolve}
    eve "Oh my god, again?!"
    show anon a_defensive f_surprised od_naked_dick3
    with {'master': dissolve}
    anon "Huh?!"
    eve f_sexy "You're hard again!"
    anon f_confused_down "Oh, uhh..."
    anon "... Yeah."
    show anon a_rub f_happy of_blush
    with {'master': dissolve}
    anon "Sorry, I guess... you just have that effect on me."
    show eve a_crossed f_happy
    with {'master': dissolve}
    eve "Aww."
    pause
    eve f_nervous_right "Alright, we can do it again."
    show anon a_sides f_surprised -of_blush
    with {'master': dissolve}
    anon "Really?"
    eve f_drawing_look_anon @ -m_talk "Mhmm."
    show anon f_happy
    show eve f_nervous_right:
        xoffset 350
        xzoom -1
    with {'master': dissolve}
    eve "Just be gentle, okay?"
    eve "I'm still pretty sore from this morning."
    anon "Awesome."
    hide anon
    show eve b_naked_shower_kiss f_thinking_lip:
        xoffset 59
    with {'master': dissolve}
    eve @ -m_talk "Mmm."
    show eve f_happy_closed
    with {'master': dissolve}
    eve "God, you're good at that!"

    if M_eve.get('biggus_dickus'):
        show eve od_dick_grow
        pause 1.5
        show eve od_dick03
        eve f_confused_low "Haah!"
    else:

        pause

    eve f_nervous "Put it in me, {b}[firstname]{/b}!"

    $ renpy.dynamic(gender='trans' if M_eve.get('biggus_dickus') else 'cis')
    call scene_eve_sex_shower.repeat (gender)
    $ unlock_scene('Eve', '08_unlocked', variant=gender)

    scene expression background(512, 280, 2.4, l=L_tattooparlor_bathroom) as stage
    show anon a_towel b_shorts f_looking_down:
        xoffset -75
    show eve a_dry_hair b_naked_shower f_happy_closed:
        xoffset 350
        xzoom -1

    if M_eve.get('biggus_dickus'):
        show eve od_dick01
    else:
        show eve od_scar

    with fade
    pause
    show anon b_dressed_changing
    with {'master': dissolve}
    pause
    show anon a_sides b_dressed f_happy
    with {'master': dissolve}
    anon "Well, that was fun!"
    show eve f_nervous:
        xoffset -250
        xzoom 1
    with {'master': dissolve}
    eve "Yeah, it was."
    pause
    eve "I might have to take a raincheck on that breakfast though..."
    show eve a_towel_wrap01 b_naked
    with {'master': dissolve}
    eve f_normal "... Heh, I don't think I could sit in a booth right now."
    show eve a_towel_wrap02
    with {'master': dissolve}
    anon "Ah, that's okay."
    show eve a_sides b_towel
    with {'master': dissolve}
    anon "I doubt we'd find any places still serving breakfast this late anyways..."
    anon "... We slept 'til almost one!"
    eve f_sad "Oh."
    show anon f_worried
    show eve f_pouting
    pause
    anon f_normal "But, I could run out and grab us burgers or something!"
    eve f_surprised "Really?"
    anon "Yeah."
    anon "It could be like a breakfast in bed kinda thing..."
    anon "... You know, only it'll be lunch."
    eve f_happy "Heh, that sounds amazing!"
    anon "Cool."
    anon "You want fries or nah?"
    eve f_thinking_down "Ehh..."
    eve f_normal "... Nah. Just the burger for me."
    anon f_confused @ f_skeptical "You're sure?"
    eve f_happy @ -m_talk "Mhmm."
    anon f_normal "Alright then."
    anon "You just go relax... and I'll be back in a jiff with the munchies!"
    eve f_sexy "Oh, don't worry... I'll definitely be relaxing."
    eve "In bed..."
    show eve f_confused_low

    if gender == 'trans':
        eve "... With a bag of ice on my asshole."
    else:
        eve "... With a bag of ice between my legs."

    show eve f_nervous
    anon f_happy "Heh!"
    eve "It's been a busy day, you know?"
    anon f_flirt "Mmm, well the day isn't over yet..."
    eve f_surprised "Oh, yes it is!"
    show eve a_finger f_concerned
    with {'master': dissolve}
    eve "Don't even think about it, {b}[firstname]{/b}..."
    eve "... I'm closing shop for the day!"
    anon f_happy "Aww."
    show eve a_hip f_happy
    with {'master': dissolve}
    eve "Heh, just go get the food, tiger!"
    show anon a_salute
    with {'master': dissolve}
    anon "Yes, ma'am!"
    eve f_laugh "Hehe!"
    show anon a_sides:
        xoffset 600
    show eve a_sides f_happy:
        xoffset 375
        xzoom -1
    with {'master': dissolve}
    eve "Hey, {b}[firstname]{/b}?"
    show anon f_normal:
        xoffset 100
        xzoom -1
    with {'master': dissolve}
    anon @ -m_talk "Hmm?"
    eve f_nervous "You're the best boyfriend a girl could ask for, you know?!"
    show anon f_happy

    menu:
        "And you're the best girlfriend!":
            anon "Right back at you, beautiful!"
            show eve f_nervous_right o_blush
        "Duh.":

            show anon a_frustrated
            with {'master': dissolve}
            anon "I know, right?"
            show eve f_normal_up

    hide anon
    with {'master': dissolve}
    pause

    scene location_tattoo_bedroom_cutscene07 as cutscene
    show text "It was wonderful seeing Eve so happy and full of life. We joked and laughed and she filled me in on all the latest gossip from around school and the tattoo shop." as caption
    with fade
    pause
    hide caption with dissolve
    show text "It was one of the best lunches I ever had...\n" as caption with dissolve
    pause
    show location_tattoo_bedroom_cutscene07b as cutscene
    show text "\n... I didn't even mind when she ate all my french fries." as caption2
    with dissolve
    pause

    scene location_tattoo_bedroom_cutscene08
    show text "Afterwards we cuddled in bed and watched scary movies." as caption
    with fade
    pause
    hide caption with dissolve
    show text "Time always seemed to fly when I was with her and before we knew it, the time had come to say good night." as caption with dissolve
    pause
    hide caption with dissolve
    show text "Not a bad way to spend a day." as caption with dissolve
    pause

    scene expression background(l=L_tattooparlor_bedroom, o=1) as stage
    show anon
    show eve b_undies f_happy
    with fade
    eve "I wish you could stay..."
    anon "Yeah, me too."
    pause
    anon "I'll see you tomorrow, okay?"
    eve "Y-yeah, okay."
    hide anon
    show eve b_undies_kiss:
        xoffset -250
    with dissolve
    pause
    show anon:
        xoffset 100
    show eve b_undies f_happy:
        xoffset -100
    with dissolve
    eve "Good night, {b}[firstname]{/b}."
    anon a_wave "Good night, {b}Eve{/b}."
    hide anon with dissolve
    return


label eveX2_post_eve:
    show anon f_worried

    if game.timer.is_afternoon():
        anon @ f_worried_left "I was thinking, maybe we could go downstairs and eh..."
    else:
        anon @ f_worried_left "I was thinking, maybe we could eh..."

    show eve f_confused
    pause

    if game.timer.is_afternoon():
        eve "And what?"
    else:
        eve "What?"

    anon f_normal "... Well, I dunno about you but I could go for a shower."
    eve f_sexy "Oh, you want a shower, huh?"
    anon f_flirt @ -m_talk "Mhmm."
    eve f_confused "Or maybe it's me that you want..."
    show anon f_flirt_grin
    show eve a_thinking_sexy f_pouting
    with {'master': dissolve}
    eve "... naked and wet?"
    show anon a_point f_surprised
    show eve a_hip f_laugh
    with {'master': dissolve}
    anon "Yes, that!"
    anon f_happy "Definitely that!"
    show anon a_sides
    with {'master': dissolve}
    eve "Hehe!"
    eve f_sexy "Alright, let's go."
    show anon a_surprised f_surprised
    with {'master': dissolve}
    anon "Really?"
    hide eve
    with {'master': dissolve}
    eve "Yup!"
    show anon a_cheering f_grin
    with {'master': dissolve}
    pause
    hide anon
    with {'master': dissolve}
    anon "Wooo!"

    if game.timer.is_afternoon() and not M_eve.once('shower_grace'):
        jump eveX2_post_eve.grace

    scene expression background(512, 280, 2.4, l=L_tattooparlor_bathroom) as stage
    show eve b_naked_shower_pickup01:
        xoffset -150

    if M_eve.get('biggus_dickus'):
        show eve od_dick01
    else:
        show eve od_scar

    with fade
    pause
    show anon a_towel b_shorts f_shy_down:
        xzoom -1
    with {'master': dissolve}
    anon "This is awesome!"
    show anon a_sides
    with {'master': dissolve}
    show anon f_flirt_grin
    show eve a_hip b_naked f_happy:
        xoffset 100
        xzoom -1
    eve "Hehe!"
    pause
    hide eve
    with {'master': dissolve}
    eve "C'mon, {b}[firstname]{/b}!"
    anon f_worried_surprised "I'm coming!"
    show anon b_naked_undress_bottom
    with {'master': dissolve}
    pause

    label eveX2_post_eve.resume:
    scene location_tattoo_bathroom_shower
    show eve a_empty b_naked_shower f_normal_down:
        xoffset 250
        xzoom -1

    if M_eve.get('biggus_dickus'):
        show eve od_dick01
    else:
        show eve od_scar

    show eve_arms_naked_shower_a_scrub as eve_arms:
        xoffset 250
        xzoom -1
    show location_tattoo_bathroom_shower_steam as steam
    with fade
    pause
    show anon b_naked f_flirt_grin od_naked_dick1 behind eve
    with {'master': dissolve}





    show anon a_empty f_flirt:
        xoffset 90
    show anon_arms_naked_a_hips_eve as anon_arms behind eve_arms:
        xoffset 90
    show eve f_surprised_right
    show eve_arms_naked_shower_a_scrub02 as eve_arms
    with {'master': dissolve}
    eve "{i}*Gasp*{/i}"
    hide anon
    hide anon_arms
    show eve b_naked_shower_kiss f_happy_closed:
        xoffset -41
    hide eve_arms
    with {'master': dissolve}
    eve "God, you're good at that!"

    if M_eve.get('biggus_dickus'):
        show eve od_dick_grow
        pause 1.5
        show eve od_dick03
        eve f_confused_low "Haah!"
    else:

        pause

    eve f_nervous "Put it in me, {b}[firstname]{/b}!"

    $ renpy.dynamic(gender='trans' if M_eve.get('biggus_dickus') else 'cis')
    call scene_eve_sex_shower.repeat (gender)
    $ unlock_scene('Eve', '08_unlocked', variant=gender)

    scene expression background(512, 280, 2.4, l=L_tattooparlor_bathroom) as stage
    show anon a_towel b_shorts f_looking_down:
        xoffset -75
    show eve a_dry_hair b_naked_shower f_happy_closed:
        xoffset 350
        xzoom -1

    if M_eve.get('biggus_dickus'):
        show eve od_dick01
    else:
        show eve od_scar

    with fade
    pause
    show anon b_dressed_changing
    with {'master': dissolve}
    pause
    show anon a_sides b_dressed f_happy
    with {'master': dissolve}
    anon "Well, that was fun!"
    show eve f_nervous:
        xoffset -250
        xzoom 1
    with {'master': dissolve}
    eve "Yeah, it was."
    pause
    anon "We'll have to do it again sometime."
    show eve a_towel_wrap01 b_naked f_normal
    with {'master': dissolve}
    eve "Heh, totally!"
    show eve a_towel_wrap02
    with {'master': dissolve}
    pause
    show eve a_sides b_towel f_sexy
    with {'master': dissolve}
    eve "Come here."
    hide anon
    show eve b_towel_kiss:
        xoffset -350
    with {'master': dissolve}
    eve "Mmm."
    pause
    show anon a_sides f_shy:
        xoffset -75
    show eve b_towel f_confused:
        xoffset -250
    with {'master': dissolve}
    anon "You'd better cut that out..."
    anon f_happy "... Or we might just end up back in the shower again."
    eve f_happy @ f_laugh "Hehe!"
    pause
    eve "I guess, I'll see you later then?"
    show anon a_wave
    with {'master': dissolve}
    anon "You betcha."
    hide anon
    show eve a_hip:
        xoffset 375
        xzoom -1
    with {'master': dissolve}
    eve "Later, {b}[firstname]{/b}."
    anon "See ya, {b}Eve{/b}."
    return


label eveX2_post_eve.grace:
    scene expression background(712, 400, 3.5, l=L_tattooparlor_apartment) as stage
    show anon a_surprised f_shy_low:
        xoffset 500
    show eve b_dressed_scared f_thinking_lip:
        xoffset 177
    with fade
    pause
    hide anon
    show eve b_dressed_kiss:
        xoffset 75
    with {'master': dissolve}
    pause
    show anon a_surprised_up f_flirt_low behind eve:
        xoffset 375
    show eve b_dressed_scared f_laugh:
        xoffset 52
    with {'master': dissolve}
    eve "Hehe!"
    hide anon
    show eve b_dressed_kiss:
        xoffset -25
    with {'master': dissolve}
    pause
    show grace a_cover b_naked f_surprised:
        xzoom -1
    with {'master': dissolve}
    grace "{b}Eve{/b}!!"
    show anon a_surprised_up_both f_surprised behind eve:
        xoffset -150
        xzoom -1
    show eve b_dressed f_surprised:
        xoffset 0
        xzoom 1
    with {'master': fastdissolve}
    eve "Oh, crap!"
    show eve f_nervous_right o_blush
    show grace f_uneasy
    with {'master': dissolve}
    eve @ -m_talk "Umm..."
    show anon a_sides f_surprised_low
    show eve f_nervous
    with {'master': dissolve}
    eve "... Whoops."
    show anon f_surprised_down o_boner
    with {'master': dissolve}
    eve "Sorry, sis."
    show anon a_cover_boner f_surprised_teeth_down of_blush:
        xoffset -100
    with {'master': dissolve}
    eve "I forgot you were in here meditating."
    show anon f_surprised_left
    show eve a_hoodless_remove1 b_dressed_hoodless
    with {'master': dissolve}
    grace "N-no, it's okay..."
    show anon f_surprised_down
    show eve a_idle
    with {'master': dissolve}
    grace "... this is your house too after all."
    show anon f_surprised
    grace f_embarrassed "Let me just, umm-"
    show anon f_surprised_down
    grace "I'll throw some clothes on and we can-"
    show anon f_worried_left
    show eve f_normal -o_blush
    with {'master': dissolve}
    eve "{i}*Ahem*{/i} It's fine, {b}Grace{/b}."
    eve f_happy "We're just... passing through anyways..."
    show anon f_shy_left
    show grace f_suspicious
    show eve f_nervous_right o_blush
    with {'master': dissolve}
    eve "... On our way to... the bathroom."
    grace f_sad_down "Oh."
    eve f_nervous_down "Yeeeeeah."
    show anon f_surprised_left
    pause
    show anon f_surprised_teeth_left
    eve f_surprised_down @ -m_talk "!!!"
    show anon f_worried_left
    show eve f_worried_back_down
    grace f_uneasy "Well, okay then..."
    show anon f_worried
    grace "... Just, umm... be safe."
    eve @ -m_talk "Mhmm."
    show anon f_worried_left
    show eve a_up f_concerned behind anon:
        xoffset 50
    with {'master': dissolve}
    eve "C'mon, {b}[firstname]{/b}!"
    anon f_worried @ -m_talk "..."
    hide anon
    hide eve
    show grace f_sad:
        xoffset -550
        xzoom 1
    with {'master': dissolve}
    pause
    show grace a_vulnerable f_sad_down
    with {'master': dissolve}
    pause

    scene expression background(512, 280, 2.4, l=L_tattooparlor_bathroom) as stage
    show anon b_dressed_changing3:
        xzoom -1
    show eve b_naked_shower_pickup01:
        xoffset -150
    with fade
    pause
    show anon a_towel b_shorts f_shy_low
    with {'master': dissolve}
    anon "Well, that was awkward."
    show eve b_naked_shower_pickup02
    with {'master': dissolve}
    eve "Yeah."
    show anon a_sides f_worried_low
    with {'master': dissolve}
    pause
    anon "You okay?"
    show eve b_naked_shower_pickup01
    with {'master': dissolve}
    eve "Yeah."
    pause
    anon f_confused_low "Are you sure?"
    anon "Because it doesn't seem-"
    show anon a_surprised f_surprised
    show eve b_naked f_concerned:
        xoffset 0
        xzoom -1

    if M_eve.get('biggus_dickus'):
        show eve od_dick01
    else:
        show eve od_scar

    with {'master': dissolve}
    eve "I said, I'm fine, {b}[firstname]{/b}!"
    pause
    show anon a_sides f_worried
    with {'master': dissolve}
    anon "Oh kay..."
    hide eve
    with {'master': dissolve}
    eve "Hurry up and get your pants off."
    anon f_shy "Alright."
    show anon b_dressed_changing2
    with {'master': dissolve}
    pause
    jump eveX2_post_eve.resume
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
