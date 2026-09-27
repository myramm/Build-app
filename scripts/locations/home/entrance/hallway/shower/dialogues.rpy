label shower_jenny_pregnant:
    scene expression L_home_shower.background_blur
    show jenny b_towel a_idle f_gross_down:
        flip
        xoffset 500
    show anon f_flirt with dissolve
    pause
    jenny "{i}*Sigh*{/i} I am never going to forgive him for this shit..."

    show anon f_surprised_teeth a_surprised_up_both with dissolve
    jenny "That bastard should be waiting on me twenty-four seven!"

    show anon at Position (xoffset=-100) with dissolve
    jenny "Catering to my every need!"

    hide anon with dissolve
    jenny "Rubbing feet..."

    scene expression L_home_hallway.background_blur
    show anon f_worried with dissolve
    anon @ -m_talk "( Yeah, I probably shouldn't go in there right now... )"

    hide anon with dissolve
    return

label shower_jenny_peep:
    anon "( Is she... Masturbating?! )"

    anon "( Oh, this is awesome! )"

    pause
    anon "( I wish, I could stand here and keep watching... )"

    pause
    anon "( I'd better go before she sees me. )"

    return

label shower_jenny_pissed_at_handjob:
    pause
    anon "( I wonder if she realizes I'm watching her? )"

    pause
    anon "( Would she even care if I joined her? )"

    anon "( I mean, after what we've been doing for her camshows, showering together doesn't seem so taboo... )"

    pause
    anon "( Nah, she might freak out and hit me with something. )"

    anon "( Not worth it. )"

    return

label shower_jenny_blowjob_intro_repeat:
    anon "( Heh, and there's my cue... )"

    menu:
        "Enter.":
            call scene_shower_with_vfx
            show jenny f_sexy b_shower a_hips
            show anon b_naked od_naked_dick3
            with fade
            jenny "It's about damn time!"

            jenny "I didn't think you were ever going to join me!"

            anon "Well, here I am..."

            show jenny f_grin_down a_shower_soap1 with dissolve
            anon "So, what do you wanna-"

            show anon f_surprised
            show jenny a_shower_soap2 with dissolve
            pause
            show jenny a_shower_soap3 with dissolve
            pause
            show jenny f_grin b_shower_soaping with dissolve
            anon @ -m_talk "..."
            jenny "Apa yang kamu katakan?"

            anon f_worried "Was I saying something?"

            show jenny f_laugh
            jenny "Ha ha ha!"

            show jenny f_grin
            menu:
                "Seks oral.":
                    jenny "You wanna have a little fun?"

                    show jenny b_shower a_hips with dissolve
                    anon f_normal "Ya!"

                    if M_jenny.get("dominance") <= 0:
                        jenny "Well then, you know what comes next..."

                        anon f_worried "Do I have to?"

                        jenny "C'mon, doggy..."

                        jenny "You gotta beg for your treat!"

                        anon "{i}*Huh*{/i}"

                        jump bj_shower_repeat_sub
                    else:
                        anon f_skeptical "And before you ask, I'm not begging!"

                        show jenny f_upset
                        jenny "Ya, ya."

                        jenny "I'm well aware."

                        call scene_shower_with_vfx_zoom
                        show jenny_shower_bj_mc
                        show jenny_shower_bj pre_talk
                        with fade
                        jenny "Just shut up and enjoy, asshole."

                        jump bj_shower_repeat_dom

                "Seks." if M_jenny.finished_inclusive(S_jenny_end):
                    label jenny_shower_sex_intro_replay:
                    if store._in_replay is not None:
                        $ player.location = L_home_shower
                        call scene_shower_with_vfx
                        show jenny f_grin b_shower_soaping
                        show anon b_naked f_worried od_naked_dick3
                        with fade
                        pause
                    show jenny b_shower a_hips with dissolve
                    jenny "Hmm, I think I deserve the treat today."

                    anon "Apa maksudmu?"

                    jenny "I mean, you're going to fuck me."

                    anon f_surprised @ -m_talk "!!!"
                    anon f_normal "Okay, sure!"

                    show jenny b_shower_back a_down f_normal o_shower_back_soap
                    with dissolve
                    jenny "Ah ah ah, not so fast!"

                    show anon b_side_naked_forward a_react f_side_shock_down od_empty zorder 0
                    show jenny b_shower_butt1 f_shower_butt1 o_empty zorder 1
                    with dissolve
                    jenny "You wanna stick it in?"

                    jenny "You've gotta beg for it!"

                    show jenny b_shower_butt with dissolve
                    anon f_side_shy_down "Ugh, this again?!"

                    show jenny b_shower_butt1 with dissolve
                    jenny "C'mon, loser."

                    jenny "Beg your princess!"

                    show jenny b_shower_butt with dissolve
                    if M_jenny.get("dominance") <= 0:
                        anon "{i}*Huh*{/i}"

                        anon "Tolong, {b}Putri [jen_name]{/b}..."

                        show jenny b_shower_butt1 with dissolve
                        jenny "Tolong apa?"

                        anon "Please, can I stick it inside you?"

                        jenny "Hmm, I think you can do better..."

                        anon "PLEASE?!"

                        jenny "Hahahah!!"

                        jenny "Alright, do it!"

                        show jenny_shower_sex 1
                        hide anon
                        hide jenny
                        jenny "!!!" with hpunch
                        $ animated = True
                        $ anim_toggle = True
                        $ M_jenny.set('sex speed', .12)
                        show expression AnimatedImage("jenny_shower_sex", [1,2,3,4,5,6,7,8], M_jenny) as jenny_shower_sex at Position(xalign = 0.0, yoffset = 0) with dissolve
                        jenny "Wow, you really are excited!"

                        anon "Y-ya!"

                    else:
                        pause
                        show jenny_shower_sex 1
                        hide anon
                        hide jenny
                        jenny "What the-" with hpunch
                        $ animated = True
                        $ anim_toggle = True
                        $ M_jenny.set('sex speed', .12)
                        show expression AnimatedImage("jenny_shower_sex", [1,2,3,4,5,6,7,8], M_jenny) as jenny_shower_sex at Position(xalign = 0.0, yoffset = 0) with dissolve
                        jenny "... Oh, fuuuuuuuuck!"

                        pause
                        jenny "I didn't say you could-"

                        anon "Anda ingin saya berhenti?"

                        jenny "TIDAK!"

                        jenny "Jangan berhenti!"

                    jump jenny_shower_sex_loop
        "Tidak sekarang.":
            anon "( Hmm, nah... )"

            anon "( I'm not really in the mood to mess with her today. )"

            pause
            $ renpy.end_replay()
            return

label shower_jenny_blowjob_intro_first:
    if store._in_replay is not None:
        $ player.location = L_home_shower
        call scene_shower_with_vfx
        with None
        $ M_jenny.set('rng', randomizer())
        if M_jenny.get('rng') > 50:
            show jenny b_shower_scene_d1
            pause
            show jenny b_shower_scene_d_rub with dissolve
        else:
            show jenny b_shower_scene_e_rub
    anon "( I wonder if she realizes I'm watching her? )"

    pause
    anon "( Would she even care if I joined her? )"

    anon "( I mean, after what we've been doing for her camshows, showering together doesn't seem so taboo... )"

    pause
    anon "( Nah, she'd might freak out and hit me with- )"

    if M_jenny.get('rng') > 50:
        show jenny b_shower a_hips f_sexy_camera
        with dissolve
    jenny "Are you just gonna stand there and watch?"

    anon "!!!" with hpunch

    if M_jenny.get('rng') < 50:
        show jenny b_shower_back f_normal a_down
        with dissolve
    anon "Hah?!"

    anon "aku tidak-"

    jenny "Hehe, would you just take your clothes off and get in here already!"

    anon "B-benarkah?"

    jenny "Ya!"

    anon "Oke."

    call scene_shower_with_vfx
    show jenny f_sexy b_shower a_hips
    show anon b_naked f_worried od_naked_dick3
    with fade
    anon "So, ehh..."

    anon "Do you need a hand or something?"

    show jenny f_grin
    jenny "Did you seriously just ask if I needed a hand?"

    anon "..."
    show jenny f_laugh
    jenny "Pfft, hahaha!"

    jenny "That's so pathetic!"

    show jenny f_grin
    anon f_skeptical "Diam!"

    show jenny f_laugh
    jenny "Haha!"

    show jenny f_grin
    anon "Did you just invite me in to make fun of me?"

    show jenny a_shower_soap1 with dissolve
    jenny "Tidak."

    jenny "I actually was thinking we would mess around a little bit."

    show jenny f_grin_down a_shower_soap2 with dissolve
    pause
    show jenny a_shower_soap3 with dissolve
    anon f_worried "{i}*Gulp*{/i} B-benarkah?"

    show jenny f_grin a_shower_soap2 o_shower_soap1 with dissolve
    jenny "Ya."

    pause
    show jenny f_upset a_shower_soap1 with dissolve
    jenny "Of course, that was before you fed me that stupid line."

    show jenny f_grin_down a_shower_soap4 with dissolve
    anon @ -m_talk "..."
    show jenny f_grin b_shower_soaping o_empty with dissolve
    jenny "So now, I'm thinking... You'll have to beg for it."

    anon f_skeptical "Hah?"

    pause
    show jenny f_eyeroll b_shower a_hips with dissolve
    jenny "You wanna help me wash, don't you?"

    show jenny f_upset
    anon f_worried "Y-ya."

    show jenny f_grin
    jenny "Then be a good doggy and beg!"

    anon "You want me to beg?"

    jenny "Lanjutkan."

    anon "..."
    if M_jenny.get("dominance") <= 0:
        anon "P-please?"

        jenny "Tolong apa?"

        anon "Please, let me wash you..."

        jenny "Now bark like a dog."

        anon "Dengan serius?!"

        show jenny f_laugh
        jenny "Ah ah ah, I said bark!"

        anon @ -m_talk "..."
        jump bj_shower_repeat_sub
    else:
        anon f_skeptical "Mustahil!"

        jenny "Yes, way!"

        anon "..."
        show jenny f_upset
        jenny "C'mon {b}[firstname]{/b}, do it!"

        anon "Tidak!"

        show jenny f_angry
        jenny "Beg or get out!"

        anon "Screw this, I'm outta here."

        jenny "Apa?!"

        jenny "You're seriously going to walk away from me right now?!"

        anon "You know I hate this humiliation stuff, {b}[jen_name]{/b}!"

        anon "If that's all you brought me in here for, then just forget it!"

        show jenny f_angry_pouting
        jenny "..."
        show jenny f_angry
        jenny "Grr, fine!"

        call scene_shower_with_vfx_zoom
        show jenny_shower_bj_mc
        show jenny_shower_bj pre_look
        with fade
        anon "!!!"
        show jenny_shower_bj pre_talk
        jenny "You really take the fun out of all this!"

        show jenny_shower_bj pre_look
        anon "A-apa yang kamu lakukan?!"

        show jenny_shower_bj pre_talk
        jenny "What the fuck does it look like I'm doing?!"

        jump bj_shower_repeat_dom

label shower_jenny_snoop_around_for_laptop:
    scene expression player.location.background_blur with None
    show anon f_grin with dissolve
    anon @ -m_talk "( Hmm, this is {b}my chance to sneak into her room and look through her diary{/b}. )"

    anon f_normal @ -m_talk "( I should hurry! )"

    hide anon with dissolve
    return

label shower_jenny_snoop_around:
    scene expression player.location.background_blur with None
    show anon with dissolve
    anon @ -m_talk "( Hmm, this is {b}my chance to sneak into her room and look for that camera{/b}. )"

    anon @ -m_talk "( I should hurry! )"

    hide anon with dissolve
    return

label shower_mom_sis_check:
    scene shower_cutscene1
    show text _ ("I rushed upstairs towards {b}[jen_name]{/b}'s cursing.\nThe scene upon entering was almost comical. {b}[jen_name]{/b} was absolutely flustered and looked like a drowned rat.\nThe exposed pipe was spouting water all over the place and making quite a mess.") as caption
    with fade
    pause

    scene expression L_home_shower.background_blur
    show anon f_surprised
    show jenny f_upset b_wet a_hips
    with fade
    jenny "About time you showed up!"

    anon "How did this happen?!"

    jenny "How should I know! Do I look like a plumber to you?! All I did was turn on the sink!"

    anon f_skeptical "What am I supposed to do?"

    jenny "Fix it obviously! You're the only man around here after all!"

    show jenny f_gross
    show anon f_grumpy
    anon "Fine! I guess I'll {b}head downstairs and see about shutting off the water valve{/b}..."

    hide anon
    hide jenny
    with dissolve
    return

label shower_mom_close_valve:
    scene expression L_home_shower.background_blur
    show jenny f_upset b_wet a_hips
    show anon f_surprised
    with dissolve
    jenny "The water's still spraying everywhere!"

    jenny "{b}Go to the basement and shut off the water valve{/b}!"

    hide anon
    hide jenny
    with dissolve
    return

label shower_mom_pipe_check:
    scene expression L_home_shower.background_blur
    show jenny b_wet a_hips f_upset
    show anon f_worried
    with dissolve
    jenny "Looks like you got it. The water stopped."

    anon "Yeah, I turned off the water valve. Now what?"

    jenny "What are you asking me for? I don't know, replace it or something?"

    anon @ a_point_self "I've never worked on anything like this before!"

    jenny "Well, you're living in a house with girls now, which means you need to learn how to fix these kinda things!"

    show jenny f_gross
    anon f_skeptical "Okay! Okay! I guess I'll {b}go to Consum-R and see about getting a pipe wrench{/b}."

    show anon f_surprised_low
    anon @ -m_talk "..."
    show jenny f_normal_low
    pause
    show jenny f_angry
    jenny @ -m_talk "..."
    jenny "Did you get a good look, you little perv?!"

    anon f_tired_happy a_behind_head "aku tidak-"

    jenny "Oh please, you think I can't tell when someone is staring at my tits?"

    anon f_surprised_low @ -m_talk "..."
    jenny "Ada apa denganmu?"

    anon f_surprised a_idle "I'm sorry, {b}[jen_name]{/b}. I was just-"

    jenny "Oh, diamlah!"

    show anon f_tired
    jenny "If you're going to stare, at least be a man about it!"

    jenny "Denying it or making excuses just makes you look like a wimp."

    jenny "No one wants to be checked out by a spineless little wimp!"

    anon f_depressed "..."
    show jenny f_upset
    jenny "If you had gotten up here to deal with this pipe situation sooner, perhaps I'd be in a better mood."

    jenny "... But since you decided to take your sweet time..."

    show jenny f_grin
    jenny "I think you should take this..."

    show jenny f_grin_down b_pull1_wet with dissolve
    show anon f_surprised
    pause
    show jenny b_pull2 with dissolve
    pause
    show jenny b_pull3 with dissolve
    show jenny b_pull4 with dissolve
    pause
    show anon f_shock of_blush
    show jenny b_panties f_upset a_shirt
    with dissolve
    jenny "... Downstairs to the wash for me."

    anon @ -m_talk "!!!" with hpunch
    show anon f_flirt
    anon "S-sure..."

    show jenny a_hips f_angry
    show anon a_shirt_jenny f_flirt_low
    with dissolve
    jenny @ -m_talk "..."
    jenny "Stop staring and go! I don't want to wait around all day for you to {b}fix that pipe{/b}!"

    anon f_shock @ -m_talk "!!!"
    hide anon with dissolve
    pause
    show jenny f_grin
    jenny "Heh, I knew it!"

    jenny "That little loser has a thing for me!"

    hide jenny with dissolve
    return

label shower_mom_fix_pipe_no_wrench:
    scene expression L_home_shower.background_blur
    show anon f_surprised
    if not game.timer.is_dark():
        show jenny f_upset b_panties a_hips
        with dissolve
        jenny "Are you finally going to fix the sink?"

        jenny "Hurry it up already!"

        hide jenny with dissolve
        show anon f_thinking a_thinking
    with dissolve
    anon @ -m_talk "( I need a {b}wrench{/b} to fix the broken pipe. )"

    hide anon
    with dissolve
    return

label shower_mom_fix_pipe_wrench:
    scene location_home_bathroom_cutscene02
    show text _ ("Once I got back home I headed upstairs to fix the bathroom sink.\nI replaced the joint with a new length of pipe and tightened it as much as I could.\nIt kind of felt weird having {b}[deb_name]{/b} and {b}[jen_name]{/b} watch me the whole time.\nLucky for me, the repairs went smoothly...") as caption
    with fade
    pause

    scene expression L_home_shower.background_blur
    show anon:
        flip
    show jenny f_upset a_crossed:
        flip
        xoffset 200
    show old_debbie 62f at left
    with fade
    debbie "Wow!!"

    debbie "Great work, {b}[firstname]{/b}!"

    show old_debbie 61f
    jenny "Finally..."

    show old_debbie 62f
    debbie "Don't be rude, {b}[jen_name]{/b}. It was nice of him to fix this for us..."

    show old_debbie 61f
    anon "Hehe, tidak masalah."

    anon "I was happy to do it."

    anon "... Besides, {b}[jen_name]{/b} is right. Fixing stuff like this is my responsibility now."

    show anon a_behind_head
    show jenny f_gross
    show old_debbie 62f
    debbie "You're going to make some lucky girl a great husband one day!"

    show anon a_idle f_shy
    show old_debbie 61f
    jenny "Pfft..."

    show jenny f_upset
    jenny "Don't say things like that, you'll give him a big head!"

    show anon f_grumpy
    show jenny f_grin
    jenny "He's still a wimp, after all."

    show old_debbie 61f
    anon "I am not a wimp!"

    jenny "Hah, whatever, wimp!"

    show old_debbie 62f
    debbie "... Don't listen to her, {b}[firstname]{/b}. She's only teasing because she loves you."

    show jenny f_angry
    show old_debbie 59f
    jenny "... As if!"

    show anon f_surprised
    show jenny f_eyeroll
    jenny "... Now can you two get out? I've been waiting to shower all day!"

    show jenny f_upset
    show old_debbie 60f
    show anon f_normal
    debbie "C'mon, {b}[firstname]{/b}. Let's get out of {i}princess{/i}' way before her foul mood infects us."

    show jenny f_grin
    show old_debbie 59f
    jenny "Heh, like calling me \"princess\" is an insult..."

    hide old_debbie
    hide jenny
    hide anon
    with dissolve
    return

label shower_mom_shower_peek_after:
    scene location_home_hallway_day
    show player 3
    player_name "( {b}[deb_name]{/b}'s body looks real good, but I don't want to peek at her too long... )"

    player_name "( It would be really awkward if she caught me. )"

    hide player with dissolve
    return

label shower_mom_shower_peek:
    player_name "( !!! )"
    show old_debbie_shower 6a_6b_6c
    player_name "( {b}[deb_name]{/b}'s in the shower! )"

    player_name "( Wow... )"

    player_name "( She has such a great body! )"

    player_name "( I can't believe she left the door cracked like this! )"

    player_name "( I can see everything! )"

    hide old_debbie_shower 6a_6b_6c
    scene shower06a
    player_name "..."
    scene shower06d
    player_name "( I'd better go before she sees me. )"

    scene hallway
    show player 79 with dissolve
    player_name "Wah..."

    player_name "I can't believe I'm living with this beautiful woman now!"

    player_name "... It's a shame she only sees me as my father's kid."

    show player 78 with dissolve
    player_name "( !!! )"
    show player 81
    player_name "I'd better get back to my room before somebody sees this tent I'm pitching..."

    hide player with dissolve
    return

label shower_mom_walk_in:
    player_name "(Luar biasa!)"

    show old_debbie_shower 6a_6b_6c
    pause
    player_name "( I wonder if her breasts feel as soft as her legs. )"

    player_name "( They look... Perfect! )"

    hide old_debbie_shower 6a_6b_6c
    scene shower06a
    pause
    scene shower06d
    player_name "( I wonder what would happen if I just walked in there? )"

    player_name "( She would probably get mad but what if she's okay with it? )"

    show old_debbie_shower 6a_6b_6c
    player_name "( I could always pretend like I didn't realize she was in the shower... )"

    return

label shower_mom_walk_in_yes:
    player_name "( I can't resist... I'm going in! )"

    hide old_debbie_shower 6a_6b_6c
    call scene_shower_with_vfx
    show player 5 at left
    show old_debbie 35b at right
    with dissolve
    debbie "( !!! )"
    show player 29 with dissolve
    player_name "Ups!"

    show player 3
    show old_debbie 35c
    debbie "Sweetie, what are you doing in here?!!"

    show old_debbie 35
    debbie "I'm naked!"

    show old_debbie 34
    show player 42 at Position (xoffset=38) with dissolve
    player_name "Sorry, {b}[deb_name]{/b}! I didn't think anyone was in here!"

    debbie "..."
    show old_debbie 35
    debbie "It's... Alright..."

    debbie "If you need something in the bathroom, just knock."

    debbie "I'll be done in a few minutes, okay?"

    show old_debbie 34
    show player 37 with dissolve
    player_name "Oke..."

    show player 3 with dissolve
    show old_debbie 35
    debbie "Now let me finish my shower, sweetie."

    show old_debbie 33
    debbie "And close the door behind you!"

    show old_debbie 32
    show player 29
    player_name "Akan berhasil!"

    hide player with dissolve
    show old_debbie 35
    debbie "Is this because of the-"

    debbie "..."
    debbie "The kissing..."

    debbie "I should be more careful with him."

    hide old_debbie with dissolve
    scene hallway
    show player 24 with dissolve
    player_name "( Ugh... That was awkward... )"

    player_name "(Mengapa menurutku itu ide yang bagus?)"

    pause
    show player 37 at Position (xoffset=41) with dissolve
    player_name "( I hope she isn't too mad at me. )"

    hide player with dissolve
    return

label shower_mom_walk_in_no:
    player_name "I probably shouldn't."

    player_name "I don't want her to be upset."

    hide old_debbie_shower 6a_6b_6c
    return

label shower_mom_sex:
    show old_debbie_shower 6a_6b_6c
    return

label shower_mom_sex_walk_in_pre:
    call scene_shower_with_vfx
    with dissolve
    show old_debbie 35 at right
    show player 1 at left
    debbie "Oh, {b}[firstname]{/b}... I didn't expect you to just barge in like that!"

    show old_debbie 33
    debbie "Though, now that you're here..."

    show old_debbie 36
    debbie "Care to join me, sweetie?"

    hide old_debbie
    hide player
    show debbies 37 with dissolve
    return

label shower_mom_sex_walk_in_after:
    call scene_shower_with_vfx
    show debbies 37_36 at Position (xpos=474)
    pause 4.8
    show debbies 35
    player_name "I love showering with you, {b}[deb_name]{/b}."

    show debbies 76 with dissolve
    pause .1
    show debbies 41_76
    pause 4
    show debbies 42 at Position (xoffset=38)
    debbie "Can I help you down here too?"

    show debbies 43 at Position (xoffset=38)
    debbie "Jadi..."

    show debbies 44 at Position (xoffset=38)
    debbie "What do you have planned today?"

    show debbies 43 at Position (xoffset=38)
    debbie "Something fun?"

    show debbies 72_71 at Position (xoffset=38)
    pause 4
    show debbies 45 at Position (xoffset=38) with dissolve
    debbie "You're all hard. It's up to you now, sweetie..."

    show debbies 73 at Position (xoffset=38) with dissolve
    return

label shower_mom_sex_wash:
    player_name "I want to wash you this time."

    show debbies 50 with dissolve
    debbie "Go ahead, sweetie."

    show debbies 51
    pause 1
    show debbies 52_53_52_51
    pause
    show debbies 54
    player_name "So soft..."

    return

label shower_mom_sex_wash_handjob:
    show debbies 45 with dissolve
    pause .4
    show debbies 73_74
    pause
    show debbies 73
    player_name "{b}[deb_name]{/b}, I'm gonna..."

    show debbies 47 at Position(xpos=526,ypos=768)
    player_name "HNNGGG!!!"

    show white zorder 4 with dissolve
    show debbies 47 at Position(xpos=526,ypos=768)
    show playersex 33 zorder 3 at Position(xpos=610,ypos=880)
    hide white with dissolve
    pause
    show debbies 48
    hide playersex
    with dissolve
    debbie "Hmm, anak baik."

    return

label shower_mom_sex_finger:
    player_name "I haven't washed {i}everywhere{/i} yet..."

    show debbies 55 at Position(xpos=688,ypos=768) with dissolve
    pause .35
    show debbies 56_55
    pause 4
    debbie "... I'm almost there, sweetie..."

    show debbies 56
    debbie "I- Aaaaah!!!"

    show debbies 50 at Position(xpos=498,ypos=768) with dissolve
    debbie "How do you always know exactly where to rub?"

    show debbies 49
    player_name "I dunno, just a feeling I guess?"

    show debbies 50
    return

label shower_mom_sex_blowjob:
    show debbies 111 with dissolve
    debbie "How about a special treat?"

    show debbies 110
    player_name "Yes, please..."

    show debbies 112 at Position(xpos=512) with dissolve
    pause .3
    show expression AnimatedImage("debbies", [113,114], M_debbie) as debbies at Position(xpos=513) with dissolve
    $ animated = True
    call screen debbie_shower_blowjob_options

label debbie_shower_blowjob_loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                show expression AnimatedImage("debbies", [113,114], M_debbie) as debbies at Position(xpos=513) with dissolve
                $ animated = True
            pause 5
            call expression game.dialog_select("debbie_shower_blowjob_hscene_dialog")
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [113,114]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "debbies {}".format(pose_list[pose_counter]) as debbies at Position(xpos=513) with dissolve
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call expression game.dialog_select("debbie_shower_blowjob_hscene_dialog")
        $ animcounter += 1
    call screen debbie_shower_blowjob_options

label debbie_shower_blowjob_hscene_dialog:
    if animcounter == 1 and randomizer() < 25:
        player_name "Ya Tuhan!{p=1}{nw}"

    if animcounter == 4 and randomizer() < 25:
        player_name "I can't-{p=1}{nw}"

    return

label debbie_shower_blowjob_cum_in:
    show debbies 113 at Position(xpos=513)
    pause .3
    show debbies 116 at Position(xpos=517)
    player_name "HNNGGG!!!"

    debbie "( !!! )"
    show white with dissolve
    hide white with dissolve
    pause
    show debbies 117 at Position(xpos=523) with dissolve
    debbie "HMMPH!!!"

    show debbies 118 at Position(xpos=516)
    debbie "{i}*Meneguk*{/i}"

    show debbies 115 at Position(xpos=531)
    debbie "... Oh, that was a lot!"

    show debbies 110 at Position(xpos=512)
    player_name "Maaf, {b}[deb_name]{/b}."

    show debbies 111
    debbie "No, don't apologize, sweetie."

    debbie "I love the taste!"

    return

label debbie_shower_blowjob_cum_out:
    show debbies 113 at Position(xpos=513)
    pause .3
    show debbies 116 at Position(xpos=517)
    player_name "HNNGGG!!!"

    debbie "( !!! )"
    show white with dissolve
    show debbies 115 at Position(xpos=531)
    show playersex 74 at Position(xpos=530,ypos=519)
    hide white with dissolve
    pause
    show playersex 75 at Position(xpos=574,ypos=655)
    debbie "Heheh, look at the mess you made of my face!"

    debbie "... I'm covered..."

    player_name "Maaf, {b}[deb_name]{/b}."

    debbie "Tidak apa-apa!"

    debbie "We're in the shower so it's easy to clean off!"

    debbie "... Just help me get it out of my hair."

    return

label shower_mom_sex_already_fingered:
    show debbies 49
    player_name "Can I put it in?"

    show debbies 50
    debbie "Sweetie, I just came... It's a little too sensitive right now..."

    debbie "I'll finish you off with my hand."

    return

label shower_mom_sex_fuck_pre:
    show debbies 49 with dissolve
    if randomizer() <= 33:
        player_name "{b}[deb_name]{/b}..."

        player_name "Can I put it inside you?"

        show debbies 50
        debbie "Of course, sweetie..."

        show debbies 57 at Position(xpos=688,ypos=768) with dissolve
        debbie "Oh, I've been waiting all day for this..."

    elif randomizer() <= 66:
        player_name "{b}[deb_name]{/b}, I want to do it with you."

        show debbies 50
        debbie "Oh sayang..."

        debbie "You are insatiable."

        debbie "Hold my leg and give me that big cock!"

        show debbies 57 at Position(xpos=688,ypos=768) with dissolve
        pause
    else:
        player_name "{b}[deb_name]{/b}, I want you."

        show debbies 50
        debbie "I was hoping you would."

        debbie "Give me that beautiful cock of yours."

        show debbies 57 at Position(xpos=688,ypos=768) with dissolve
        pause
    show debbies 58 with dissolve
    debbie "Haah!"

    show debbies 59 with dissolve
    pause
    return

label mom_shower_sex_loop:
    show screen xray_scr
    pause
    hide screen xray_scr
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                show expression AnimatedImage("debbies", [59,60,61], M_debbie) as debbies at Position(xpos = 688,ypos = 768)
                $ animated = True
            pause 5
            if animcounter in [1,2,3]:
                call expression game.dialog_select("debbie_shower_hscene_dialog")
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [59,60,61]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "debbies {}".format(pose_list[pose_counter]) as debbies at Position(xpos = 688,ypos = 768)
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            if animcounter in [1,2,3]:
                call expression game.dialog_select("debbie_shower_hscene_dialog")
        $ animcounter += 1
    call screen shower_mom_sex_options

label debbie_shower_hscene_dialog:
    if randomizer() <= 33:
        if animcounter == 1:
            debbie "Ahhhh!!!{p=1}{nw}"

            debbie "Give it to me, sweetie!{p=2}{nw}"

        elif animcounter == 3:
            debbie "Cum for me!{p=2}{nw}"

    elif randomizer() <= 66:
        if animcounter == 1:
            debbie "Ohh!!{p=1}{nw}"

        elif animcounter == 2:
            debbie "Sweetie! Deeper!{p=2}{nw}"

        elif animcounter == 3:
            player_name "{b}[deb_name]{/b}, I love you!{p=2}{nw}"

            debbie "I love you too!{p=2}{nw}"

    else:
        if animcounter == 2:
            player_name "I love the way your tits bounce.{p=2}{nw}"

            debbie "Yeah, well, I love your huge cock!{p=2}{nw}"

        elif animcounter == 3:
            debbie "Ahh!!{p=1}{nw}"

            debbie "Yes, that's the spot!{p=2}{nw}"

    return

label mom_shower_sex_cum:
    call expression game.dialog_select("mom_shower_sex_cum_pre")
    $ cum = True
    call expression game.dialog_select("mom_shower_sex_cum_after")
    $ persistent.cookie_jar["Debbie"]["unlocked"] = True
    $ persistent.cookie_jar["Debbie"]["gallery"]["07_unlocked"] = True
    jump expression game.dialog_select("mom_shower_end")

label mom_shower_sex_cum_pre:
    if randomizer() <= 33:
        player_name "UHHH!"

    elif randomizer() <= 66:
        debbie "Give it to me, sweetie!"

        debbie "Cum deep inside me!"

    else:
        debbie "HAAAAAHH!"

    return

label mom_shower_sex_cum_after:
    show debbies 60
    show white zorder 4 with dissolve
    hide white with dissolve
    pause
    if randomizer() <= 50:
        player_name "That felt good..."


    show playersex 53 zorder 3 at Position(xpos=663,ypos=632)
    show debbies 57
    with dissolve
    if randomizer() <= 50:
        debbie "You let out so much..."

        debbie "Such a mess."

        debbie "Good thing we're in the shower..."

    else:
        debbie "Ohh!"

        debbie "God, I love this cock of yours!"

        player_name "Hehe, I'm pretty sure it feels the same way about you..."

        debbie "Ha ha ha!"

        debbie "Hold on to me for a second. My legs are a little wobbly after all that!"

    return

label mom_shower_end_dialogue:
    hide playersex
    hide debbies
    show debbies 34 at Position(xpos=474,ypos=768)
    with dissolve
    if randomizer() <= 50:
        debbie "That was fun but I should really get back downstairs and start dinner."

        debbie "We'll do this again, okay?"

        debbie "Make sure {b}[jen_name]{/b} doesn't see you leave the bathroom, okay?"

    else:
        debbie "I hope {b}[jen_name]{/b} didn't hear us..."

        show debbies 35
        player_name "I doubt it. Not with the shower running..."

        show debbies 34
        debbie "... Yeah, I suppose I'm worrying too much."

        debbie "I should get downstairs and start cooking dinner..."

        debbie "Fetch me a towel?"

        show debbies 35
        player_name "Sure thing, {b}[deb_name]{/b}!"

    hide old_debbie_shower
    hide old_debbie
    hide debbies
    hide player
    with dissolve
    return

label mom_shower_end:
    call expression game.dialog_select("mom_shower_end_dialogue")
    $ renpy.end_replay()
    $ game.timer.tick()
    $ playSound()
    jump expression game.dialog_select("hallway_dialogue")

label shower_mom_sex_leave:
    player_name "I probably shouldn't."

    player_name "I don't want her to be upset."

    return

label shower_jenny_shower_spy_repeat:
    call scene_shower_with_vfx_peep
    $ M_jenny.set('rng', randomizer())
    if M_jenny.get('rng') > 66:
        show jenny b_shower_scene_a1_blurred
    elif 66 > M_jenny.get('rng') > 33:
        show jenny b_shower_scene_b1_blurred
    else:
        show jenny b_shower_scene_c1_blurred
    with dissolve
    pause
    anon "( Hmm, it's so steamy... )"

    anon "( I can't quite make out- )"

    if M_jenny.get('rng') > 66:
        show jenny b_shower_scene_a1
    elif 66 > M_jenny.get('rng') > 33:
        show jenny b_shower_scene_b1
    else:
        show jenny b_shower_scene_c1
    show bathroom_door_left at Position (xoffset=-50)
    show bathroom_door_right at Position (xoffset=50)
    with dissolve
    if M_jenny.finished_state(S_jenny_perv_on_tammy) and not M_jenny.get("first_shower_time"):
        anon "( Hello, {b}[jen_name]{/b}... )"

    elif M_jenny.finished_state(S_jenny_pissed_at_handjob) or store._in_replay is not None:
        anon "( Oh, here we go. )"

        anon "( I hope I haven't missed the show! )"

    elif M_jenny.finished_state(S_jenny_talked_to_cedric):
        anon "( Hehe, it's {b}[jen_name]{/b} again! )"

    else:
        anon "( Whoa!! )"

        anon "( It's {b}[jen_name]{/b}! )"

    pause

    if M_jenny.get('rng') > 66:
        show jenny b_shower_scene_a2
    elif 66 > M_jenny.get('rng') > 33:
        show jenny b_shower_scene_b2
    else:
        show jenny b_shower_scene_c2
    with dissolve

    if M_jenny.finished_state(S_jenny_perv_on_tammy) and not M_jenny.get("first_shower_time"):
        anon "( I can't believe how much has happened between us! )"

        anon "( A few weeks ago she would have freaked out about this, but now... )"

    elif M_jenny.finished_state(S_jenny_pissed_at_handjob) or store._in_replay is not None:
        pause
    elif M_jenny.finished_state(S_jenny_talked_to_cedric):
        anon "( She should take her webcam in there with her, she'd probably make a fortune... )"

        pause
    else:
        anon "( Oh man, she would be so pissed if she knew I was spying on her! )"

        pause

    if M_jenny.get('rng') > 75:
        show jenny b_shower_scene_a3
    elif 75 > M_jenny.get('rng') > 50:
        show jenny b_shower_scene_b3
    elif 50 > M_jenny.get('rng') > 25:
        show jenny b_shower_scene_c3
    else:
        show jenny b_shower_scene_e3
    with dissolve

    if M_jenny.finished_state(S_jenny_perv_on_tammy) and not M_jenny.get("first_shower_time"):
        anon "( I can just walk in there and join her, whenever I want! )"

    elif M_jenny.finished_state(S_jenny_pissed_at_handjob) or store._in_replay is not None:
        anon "( C'mon {b}[jen_name]{/b}, you know you want to... )"

    elif M_jenny.finished_state(S_jenny_talked_to_cedric):
        anon "( Mmm, I could watch her scrub that body all- )"

    else:
        anon "( It's a shame she's such a bitch all the time... )"

        anon "( With a body like that, she could probably get any guy she wants. )"

        pause
        anon "( I should get out of here before she catches me. )"

        pause
        scene black with dissolve
        jump jenny_shower_peep_end

    if M_jenny.get('rng') > 50:
        show jenny b_shower_scene_d1
    else:
        show jenny b_shower_scene_e_rub

    if M_jenny.finished_state(S_jenny_perv_on_tammy) and not M_jenny.get("first_shower_time"):
        pause
    elif M_jenny.finished_state(S_jenny_pissed_at_handjob) or store._in_replay is not None:
        anon "( Bingo! )"

    else:
        anon "( !!! )" with hpunch

    if M_jenny.get('rng') > 50:
        show jenny b_shower_scene_d_rub with dissolve
    return

label shower_jenny_shower_spy:
    call scene_shower_with_vfx_peep
    $ M_jenny.set('rng', randomizer())
    if M_jenny.get('rng') > 66:
        show jenny b_shower_scene_a1_blurred
    elif 66 > M_jenny.get('rng') > 33:
        show jenny b_shower_scene_b1_blurred
    else:
        show jenny b_shower_scene_c1_blurred
    with dissolve
    pause
    anon "( Hmm, it's so steamy... )"

    anon "( I can't quite make out- )"

    if M_jenny.get('rng') > 66:
        show jenny b_shower_scene_a1
    elif 66 > M_jenny.get('rng') > 33:
        show jenny b_shower_scene_b1
    else:
        show jenny b_shower_scene_c1
    show bathroom_door_left at Position (xoffset=-50)
    show bathroom_door_right at Position (xoffset=50)
    with dissolve
    anon "( Whoa!! )"

    anon "( It's {b}[jen_name]{/b}! )"

    pause
    if M_jenny.get('rng') > 66:
        show jenny b_shower_scene_a2
    elif 66 > M_jenny.get('rng') > 33:
        show jenny b_shower_scene_b2
    else:
        show jenny b_shower_scene_c2
    with dissolve
    anon "( Oh man, she would be so pissed if she knew I was spying on her! )"

    pause
    if M_jenny.get('rng') > 66:
        show jenny b_shower_scene_a3
    elif 66 > M_jenny.get('rng') > 33:
        show jenny b_shower_scene_b3
    else:
        show jenny b_shower_scene_c3
    with dissolve
    anon "( Just look at that body though! )"

    anon "( She's like a perfect- )"

    show jenny b_shower_caught_front_surprised
    anon "( !!! )" with hpunch
    jenny "What the fuck, {b}[firstname]{/b}!!!"

    anon "( Uh oh... )"


    $ player.go_to(L_home_hallway)
    scene expression player.location.background_blur with None
    show anon b_dressed_blocking
    show jenny b_towel a_hit f_angry:
        xoffset -50
    with dissolve
    jenny "You!"

    show jenny a_hit2 with dissolve
    anon "Aduh!"

    show jenny a_hit with dissolve
    jenny "Little!"

    show jenny a_hit2 with dissolve
    anon "Ow!!"

    show jenny a_hit with dissolve
    jenny "PERVERT!!!"

    show jenny a_hit2 with dissolve
    anon "Ouch!!"

    show anon f_skeptical b_dressed
    show jenny a_hit
    with dissolve
    anon "Stop hitting me!!!"

    hide jenny
    show jenny b_towel f_angry a_hips with dissolve
    jenny "What the hell is the matter with you?!"

    anon f_worried "Nothing, I just saw the door cracked and I-"

    show anon f_sad_down
    jenny "... And you what?!"

    jenny "Thought it was alright to peep on people in the shower?!"

    anon f_tired "It's not like that..."

    show jenny f_gross
    pause
    show anon f_sad_down
    pause
    anon "Well, okay. It's a little like that but..."

    show jenny f_angry
    jenny "It's exactly like that, you pathetic little-"

    anon f_worried "I'm sorry, alright?!"

    pause
    jenny "{i}*Sigh*{/i} Just get outta here or I'm telling {b}[deb_name]{/b}!"

    anon f_shock "No, no, please don't tell {b}[deb_name]{/b}!"

    anon "I'm leaving right now!"

    hide anon with fastdissolve
    pause
    show jenny f_gross
    jenny "( Grr, he's such a freaking loser! )"

    jenny "( I just wanna wring his stupid neck! )"

    hide jenny with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
