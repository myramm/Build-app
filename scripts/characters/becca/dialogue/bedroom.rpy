label becca_button_bedroom:
    pause
    show anon b_dressed_tall:
        offset (-110, 35)
    with dissolve
    show becca a_front b_home_bed f_confused
    with {'master': dissolve}
    becca "{b}[firstname]{/b}?"
    show anon a_wave
    with {'master': dissolve}
    anon "Hey, {b}Becca{/b}."
    becca "What are you doing here?"
    show anon a_sides
    with {'master': dissolve}

    menu becca_button_bedroom.choice:
        "I was in the neighborhood.":
            jump becca_button_bedroom.area
        "What are you working on?":

            jump becca_button_bedroom.work
        "Sex.":

            jump becca_button_bedroom.sex
        "Just saying hi.":

            pass

    anon "You'll be at the beach this weekend, right?"
    becca f_confused "Umm, yeah?"
    becca "Why wouldn't I be there?"
    anon f_shy "I dunno, I was just making sure."
    pause
    show anon a_shy_neck f_shy_left
    show becca a_front f_surprised
    with {'master': dissolve}
    pause
    anon "I'm really looking forward to it, you know?"
    show becca a_front f_shy_down o_blush
    with {'master': dissolve}
    becca "Oh, umm..."
    show anon f_shy
    show becca b_home_bed_back f_shy_low
    with {'master': dissolve}
    pause
    show becca f_shy_down
    becca "... Y-yeah, me too."
    show anon a_cheering f_grin
    with {'master': dissolve}
    pause
    show anon a_surprised_shoulders f_surprised_teeth
    with {'master': dissolve}
    pause
    show anon a_sides f_shy
    with {'master': dissolve}
    anon "C-cool!"
    anon f_happy "I guess, I'll just see you there!"
    show becca b_home_bed f_shy_happy
    with {'master': dissolve}
    becca "See ya, {b}[firstname]{/b}."
    hide anon
    show becca f_concerned_lipbite
    with {'master': dissolve}
    pause
    return


label becca_button_bedroom.area:
    anon "Just thought I'd drop in and say hello."
    show becca a_crossed
    with {'master': dissolve}
    becca @ -m_talk "Mhmm."
    becca f_annoyed "You'd better not be doing nasty shit with my mother again."
    show anon a_behind_head f_worried
    with {'master': dissolve}
    anon "Oh, ehh..."

    menu:
        "Of course not.":
            pass
        "I wouldn't call it nasty...":

            jump becca_button_bedroom.troll

    anon f_shy "I told you, that was just a simple misunderstanding."
    becca f_eyeroll "Yeah, whatever."
    show becca a_front f_annoyed
    with {'master': dissolve}
    becca "Just... shut up."
    anon "Alright."
    show anon a_sides
    with {'master': dissolve}
    jump becca_button_bedroom.choice


label becca_button_bedroom.sex:
    show anon a_shy_neck f_shy_left
    with {'master': dissolve}
    anon "Say, remember the other day when we uhh... you know?"
    becca f_confused @ -m_talk "Hmm?"
    anon f_shy "When we facetimed {b}Roxxy{/b}..."
    show anon of_blush
    with {'master': dissolve}
    anon "... So she could watch us... uhh..."
    show becca a_front f_shy_down o_blush
    with {'master': dissolve}
    becca "Oh, that."
    show anon a_sides
    with {'master': dissolve}
    anon "Y-yeah."
    becca f_shy "You wanna, do that again?"
    anon f_worried "I mean, if you don't want to, I under-"
    becca f_concerned "N-no, I do!"
    show becca b_home_bed_back f_shy_low
    with {'master': dissolve}
    becca "Or, uhh... I mean, we can..."
    becca f_shy_happy_down @ f_shy_down "... B-because, you know, it's better than doing homework."
    anon f_shy "Right."
    show becca b_home_bed f_concerned_lipbite_low
    with {'master': dissolve}
    pause
    show anon f_normal -of_blush
    show becca f_concerned -o_blush
    with {'master': dissolve}
    becca "Let's see if {b}Roxxy{/b}'s home first."
    show anon a_surprised_shoulders f_surprised_down behind becca:
        xoffset -150
    show becca b_home_bed_reach
    hide books
    with {'master': dissolve}
    pause
    show anon a_sides f_shy
    show becca a_phone b_home_bed f_normal_down:
        xoffset 100
        xzoom -1
    with {'master': dissolve}
    pause
    show anon a_down b_dressed_floor_barefeet f_normal:
        offset (-85, -35)
    show becca a_phone_talk f_shy
    with {'master': dissolve}
    "{i}*Ring* *Ring*{/i}"
    pause
    "{i}*Ring* *Ring*{/i}"

    $ renpy.dynamic(local=ComposeTransition(phoneleft.show,
        before=MoveTransition(.7, time_warp=_warper.easein_cubic)))

    show location_tina_becca_bedroom_bed:
        xoffset 300
    show anon:
        xoffset 300 + -85
    show becca:
        xoffset 300 + 100
    show roxxy bed b_phone f_bored at Split(-15, 'left', offset=300).new:
        xoffset -300
    show expression phoneleft.core_bar as split
    with {'master': local}
    roxxy "Hello?"
    becca "Hey, it's me."
    roxxy "Oh, hey... what's up?"
    show becca f_shy_back o_blush
    with {'master': dissolve}
    becca "Umm, so... your boyfriend's here again and we were kinda thinking-"
    roxxy f_annoyed "{b}[firstname]{/b}'s over there again?!"
    show anon f_worried_surprised
    becca f_concerned "Well, yeah... I mean, he was just in the neighborhood and stopped by to say hello, you know?"
    show anon f_worried
    roxxy f_suspicious "Uh huh."
    pause
    roxxy f_smug "And let me guess, you want another taste of that delicious dick?"
    show anon f_flirt_grin
    becca f_shy_back "Umm... s-sorta..."
    show roxxy b_nails_phone f_bored_down
    with {'master': dissolve}
    roxxy "Well, that didn't sound very convincing."
    show anon f_worried
    becca f_concerned "Please, {b}Roxxy{/b}?"
    roxxy f_smug_out "C'mon, you know what I wanna hear..."
    show anon f_shy
    show becca f_shy_down
    pause
    becca "I'm a horny beta bitch..."
    show roxxy f_horny_lipbite_out
    becca "... And you're my alpha..."
    pause
    becca "... Will you please allow your boyfriend have his way with me?"
    show anon f_grin
    show roxxy f_horny_lipbite_close
    pause
    show roxxy b_phone f_smug
    with {'master': dissolve}
    roxxy "Hahaha!"
    show anon f_happy
    roxxy f_horny "Alright, fine..."
    roxxy f_smug "... But facetime me again so I can watch."
    becca f_shy "Y-yeah, okay."
    hide becca
    with {'master': dissolve}
    anon "So we're doing this?"

    scene location_tina_becca_bedroom_evening:
        anchor (712, 400)
        pos (.5, .5)
        transform_anchor True
        zoom 2.5
    show anon b_onbed_back f_happy:
        offset (105, 28)
        yalign 1.
        zoom .85
    show cam
    show roxxy bed b_facetime f_horny_out:
        align (1., 0.)
        crop (275, 90, 1 / .7 * 1024 / 4.2, 1 / .7 * 768 / 4.2)
        offset (-45, 35)
        xzoom -1
        zoom .7
    with fade
    roxxy "Yes, you can do it..."
    show anon f_shy
    show becca b_home_bed f_concerned_lipbite o_blush behind cam:
        offset (175, 170)
        zoom .9
    with {'master': dissolve}
    roxxy "... But I hope you appreciate what an amazing girlfriend you have!"
    anon f_flirt "Of course I appreciate that {b}Roxxy{/b}..."
    show becca b_home_bed_undress a_remove_top01
    with {'master': dissolve}
    anon "... You're the best!"
    show anon f_flirt_low
    show becca a_remove_top02 -o_blush
    with {'master': dissolve}
    roxxy f_smug_out "Good."
    show anon a_side
    show becca a_remove_top03
    with dissolve
    show becca a_remove_top04
    with {'master': dissolve}
    roxxy "Now hurry up and get to fuckin' because my mom will be home soon and I don't want her interrupting the show!"
    show becca a_sides b_pants_bed
    with {'master': dissolve}
    anon "{i}*Gulp*{/i} Y-yeah, okay."
    show anon b_onbed_sit_changing3 -of_blush:
        offset (-330, 28)
        yalign 1.
        xzoom -1
    show becca b_home_bed_remove_bottom01
    show roxxy f_horny_lipbite_out
    with {'master': dissolve}
    pause
    show anon a_towel b_shorts f_flirt_down:
        reset
        offset (-500, 0)
        xzoom -1
        yalign 1.
        zoom .95
    show becca b_home_bed_remove_bottom02
    show roxxy b_lolipop f_curious_lolipop_out
    with {'master': dissolve}
    pause
    show anon b_dressed_changing2:
        offset (0, 0)
        xzoom 1
        yalign 1.
    show anon_overlay_o_underwear_boner1 as boner behind cam:
        offset (30, 75)
        zoom .95
    show becca b_naked_bed a_sides f_shy_happy_down o_blush
    with {'master': dissolve}
    pause
    hide boner
    show anon b_naked_undress_bottom o_boner
    show becca f_shocked_down
    show roxxy b_facetime f_happy_out m_talk
    with {'master': dissolve}
    pause
    show anon a_sides b_naked f_shy od_naked_dick3 -o_boner
    show becca f_sexy_low
    show roxxy f_smug_out -m_talk
    with {'master': dissolve}
    roxxy "You want that dick, {b}Becca{/b}?"
    show anon a_behind f_flirt_low
    with {'master': dissolve}
    becca f_sexy_low "Y-yes."
    roxxy "I can't hear you!"
    show anon f_shy of_blush
    with {'master': dissolve}
    becca "Yes, I want it!"
    roxxy f_horny_out "Who's dick is it?"
    show anon f_brag
    becca f_thinking @ f_exhausted_closed -m_talk "Yours."
    roxxy f_smug_out "Louder!"
    show anon f_surprised
    show becca b_naked_bed_back f_annoyed
    with {'master': fastdissolve}
    becca @ f_annoyed_surprised "It's your dick, {b}Roxxy{/b}!"
    roxxy f_happy_out "Hehe, good girl..."
    show anon f_happy
    show becca b_naked_bed f_concerned_lipbite_low
    with {'master': dissolve}
    roxxy f_smug_out "... Now get on the bed, {b}[firstname]{/b}."
    roxxy "I want her to ride you."
    show anon a_sides f_shy
    with {'master': dissolve}
    anon "R-right, umm..."
    anon f_flirt "... This is awesome!"
    show anon f_grin
    roxxy f_laugh "Hehe!"

    call scene_becca_sex_bedroom.repeat
    $ unlock_scene('becca', '03_unlocked')

    scene location_trailer_bedroom_facetime as underlay:
        yoffset -90
    show roxxy bed b_stomach c_stomach f_horny o_wet:
        yoffset -90

    $ renpy.dynamic(local=Split(10.5, 'top', offset=-55),
                    stage='location_tina_becca_bedroom_bed')
    show expression stage as stage
    show anon b_naked_bed_mount
    show becca b_naked_disheveled_bed_mount f_exhausted_closed
    with fade
    roxxy "That was so fucking hot, {b}[firstname]{/b}!"
    show becca b_naked_disheveled_bed_belly behind anon
    anon "!!!" with hpunch
    show anon b_sit_naked f_surprised_low od_dick1:
        offset (-250, 15)
    with {'master': dissolve}
    roxxy "What, again?!"
    show anon b_sit_naked_check f_surprised_low od_naked_dick1 behind becca:
        offset (0, -30)
    with {'master': dissolve}
    anon "{b}Becca{/b}?"
    show anon f_surprised_down
    show becca a_shoo
    with {'master': dissolve}
    becca @ -m_talk "*Mumbles unintelligibly*"
    show anon f_worried_low
    show becca -a_shoo
    with {'master': dissolve}
    show anon b_liu_naked -od_naked_dick1:
        offset (-300, -50)
    with {'master': dissolve}
    roxxy "How can you still be struggling with my boyfriend's big dick?"
    show anon f_flirt_low of_blush
    show becca a_reach f_thinking
    with {'master': dissolve}
    becca "Ugh... shut up, {b}Roxxy{/b}!"
    show becca a_phone f_shy o_blush
    with dissolve
    show expression stage as stage at local with {'master': local.show}
    roxxy "{i}*Snort*{/i} I'm sorry but it's funny..."
    if M_missy.taken_dick:
        show anon f_surprised_low
        roxxy f_smug "... Even {b}Missy{/b} takes it better than you!"
    show anon f_worried_low -of_blush
    with {'master': dissolve}
    becca f_upset "Grr!"
    show roxxy f_annoyed_right
    with {'master': dissolve}
    crystal "{b}Roxanne{/b}, I'm home!!"
    show becca f_concerned
    roxxy f_annoyed "Oh, shit!"
    roxxy "I gotta go."
    roxxy f_suspicious "Will you come by and see me later, {b}[firstname]{/b}?"
    show becca f_shy_back_low
    anon f_confused_low @ -m_talk "Hmm?"
    roxxy f_horny_lipbite @ f_horny "Watching you two is fun and all but I'd much rather have you to myself for a while."
    show becca f_shy_back_low
    show anon f_thinking_down

    menu:
        "Sure.":
            anon f_normal_low "Yeah, totally."
            show becca f_shy_back_down
            show roxxy f_horny_lipbite_close
            anon "I'll come see you soon, okay?"
            roxxy f_horny "Good."
            show anon f_grin
            show becca f_surprised
            roxxy f_smug "I'm gonna give you the best sex of your life next time you're here, I promise!"
        "Yeah, maybe...":

            anon f_worried_low "If there's time."
            roxxy f_suspicious "C'mon, {b}[firstname]{/b}..."
            roxxy "... Can't you make time?"
            anon "I'll try, okay?"
            show becca f_shy
            roxxy f_bored_down "{i}*Sigh*{/i} Alright."
            roxxy "Just-"
            pause
            roxxy f_bored "I miss you."
            show becca f_sad
            anon "I know."

    crystal "Where the heck are ya, {b}Roxanne{/b}?!"
    show anon f_surprised_low
    show becca f_surprised
    show roxxy f_annoyed_right
    crystal "I need help!"
    show anon f_worried_low
    show becca f_concerned
    show roxxy b_hangup c_hangup
    with {'master': dissolve}
    roxxy "Ugh, I- ... Coming... just, hold on!!"
    show anon f_surprised_low
    show becca f_surprised
    roxxy f_eyeroll "Stupid, drunk, good for nothing..."
    show roxxy b_stomach c_stomach f_bored
    with {'master': dissolve}
    roxxy "... I'll talk to you guys later."
    anon f_normal_low "Y-yeah, okay."
    show roxxy f_angry_right
    becca f_happy "Later, {b}Roxxy{/b}."
    show anon f_surprised_low
    show becca f_surprised
    hide roxxy
    with {'master': dissolve}
    roxxy "You are so fucking embarrass-"
    show expression stage as stage with {'master': local.hide}
    "{i}*Beep*{/i}"
    show becca a_reach f_shy with {'master': dissolve}
    anon f_surprised_low "Oh kay..."
    show anon a_surprised b_sit_naked_up f_normal_low od_naked_dick1 behind becca:
        offset (-30, -30)
    show becca a_down
    with {'master': dissolve}
    anon "... I guess, I should probably get going too."
    show anon f_flirt_low
    show becca b_naked_disheveled_bed_up f_thinking
    with {'master': dissolve}
    becca "Yeah, okay."
    anon f_shy_low "I'll see you later?"
    becca f_shy_happy_up @ -m_talk "Mhmm,"
    becca "I'll be here."
    anon f_flirt_low "Cool."
    hide anon
    show becca f_sexy_low
    with {'master': dissolve}
    anon "See you later, {b}Becca{/b}."
    becca "Later."
    show becca f_concerned_lipbite
    with {'master': dissolve}
    pause
    return 'afterglow'


label becca_button_bedroom.troll:
    show anon f_shy_left of_blush
    with {'master': dissolve}
    anon "I wouldn't call it nasty..."
    show becca f_glaring
    anon f_flirt "... Your mom is really sexy."
    show becca a_angry f_surprised
    with {'master': dissolve}
    becca @ -m_talk "!!!"
    show becca a_hips f_disgusted
    with {'master': dissolve}
    becca "Eugh, c'mon {b}[firstname]{/b}... I don't wanna hear that shit!!"
    show anon a_cannoli_gobble f_laugh
    show becca f_glaring
    with {'master': dissolve}
    anon "{i}*Snort*{/i}"
    show anon a_sides f_happy -of_blush
    with {'master': dissolve}
    anon "Relax, I'm just messing with you {b}Becca{/b}..."
    becca f_annoyed "Yeah, not funny!"
    anon f_shy "Hehe, sorry."
    jump becca_button_bedroom.choice


label becca_button_bedroom.work:
    show anon a_point_down f_confused_low
    with {'master': dissolve}
    anon "What are you working on?"
    show becca f_normal_down
    pause
    becca f_normal "It's just a boring thing for {b}Miss Dewitt{/b}'s class."
    show anon a_sides f_normal
    show becca a_front
    with {'master': dissolve}
    anon "Oh, yeah?"
    becca "I'm supposed to explain the difference between a bass clef and a treble clef in one paragraph..."
    show anon f_confused
    becca "... Then I have to properly identify and label all the note values."
    anon "That sounds hard."
    becca f_concerned "Not really."
    becca "I've been reading sheet music since I was like, five years old."
    anon "Really?"
    becca f_normal @ f_eyeroll "Yeah, my mom forced me take piano lessons."
    anon f_surprised "You can play the piano?"
    becca @ -m_talk "Mhmm."
    anon f_happy "That's awesome!"
    becca f_shy_back_low "Ehh, not really..."
    anon f_worried "No?"
    becca f_sad "It's boring and I hated it."
    anon @ f_confused "How come?"
    becca f_annoyed "Because I was a little girl and I wanted to be outside playing games with all the other kids!"
    becca "Not cooped up in the house with my mother and that decrepit music teacher!"
    anon f_thinking_down "Oh."
    pause
    anon f_happy "Well, I think still think it's cool."
    show becca f_eyeroll
    pause
    show becca f_normal
    jump becca_button_bedroom.choice
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
