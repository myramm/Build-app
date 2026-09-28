label bec01_talk_becca:
    pause
    show anon b_dressed_tall:
        offset (-110, 35)
    with dissolve
    show anon f_surprised
    show becca a_front b_home_bed f_surprised
    with {'master': fastdissolve}
    becca "{b}[firstname]{/b}?!"
    show anon a_wave
    with {'master': dissolve}
    pause
    becca "What the hell are you doing here?!"
    show anon a_behind_head f_shy
    with {'master': dissolve}
    anon "H-hey, {b}Becca{/b}."
    show becca a_crossed f_annoyed
    with {'master': dissolve}
    becca "No, lemme guess..."
    becca "... You're here to fuck my mother again."
    anon f_surprised @ -m_talk "!!!"
    show anon a_surprised_up_both
    with {'master': dissolve}
    anon "Wha- No!!"
    pause
    anon f_worried "Hey, c'mon..."
    show anon a_sides
    with {'master': dissolve}
    anon "... That wasn't anything-"
    show becca b_home_bed_back
    with {'master': dissolve}
    becca "Save it, I saw you!"
    pause
    becca f_eyeroll "Eugh, and what's worse... {b}Missy{/b} saw you!"
    show becca b_home_bed
    with {'master': dissolve}
    becca f_annoyed "That bitch is never gonna let me forget it."
    anon f_shy "Look, I'm really sorry... I didn't intend to have sex with your mother, really..."
    show becca a_hips f_disgusted
    with {'master': dissolve}
    becca "Oh, so it was just an accident then?!"
    anon f_worried "Well, ehh... N-no, it wasn't an accident exactly..."
    anon "... I was actually just supposed to deliver a pizza and then-"
    becca f_annoyed "And then what, {b}[firstname]{/b}?!"
    becca "You tripped and fell penis first into my mom's vagina?!"
    anon f_confused "Err..."
    anon "... No?"
    show anon f_worried
    show becca f_confused
    pause
    anon "You see, my boss, {b}Tony{/b}..."
    anon "... He said your mother was a very special customer and that her satisfaction should be my number one priority."
    show becca f_shocked
    pause
    show anon a_shy_neck f_shy_down
    with {'master': dissolve}
    anon "So, I uhh... w-we sorta-"
    show anon a_surprised_up f_surprised
    show becca a_angry f_disgusted
    becca "EWWWW!!!" with hpunch
    show anon f_worried
    becca "My uncle {b}Tony{/b} set this whole thing up?!"
    show anon a_facepalm f_disgusted_wince
    with {'master': dissolve}
    pause
    show anon a_sides f_worried
    show becca a_front f_sad_down
    with {'master': dissolve}
    becca @ f_exhausted_closed -m_talk "{i}*Sigh*{/i} Please, just stop talking."
    anon f_sad_down "Right, sorry."
    pause
    show anon a_point_back f_worried
    with {'master': dissolve}
    anon "I'll just go..."
    show anon a_sides
    with {'master': dissolve}
    anon "... And uhh..."
    pause
    anon f_confused "... Hopefully, see you this weekend at the beach?"
    show becca a_crossed b_home_bed_back f_annoyed
    with {'master': dissolve}
    becca "Pfft, why should I?"
    becca f_upset "So you can all poke fun at me over this whole fucked up situation?"
    anon f_sad "{b}Becca{/b}..."
    pause
    show anon a_liu_shoulder f_worried:
        xoffset -50
    show becca f_glaring_back
    with dissolve
    anon "... I would never do that to you."
    show becca b_home_bed f_sad
    with {'master': dissolve}
    pause
    show anon a_sides
    with {'master': dissolve}
    becca "Do you really even care if I come?"
    anon f_confused "Huh?"
    show becca a_front b_home_bed_back f_shy_low
    with {'master': dissolve}
    becca "I mean, I'm pretty sure {b}Roxxy{/b} is in love with you..."
    show anon a_surprised_up_both f_surprised
    with {'master': dissolve}
    anon -m_talk "!!!"
    show anon a_up f_shock
    with {'master': fastdissolve}
    becca f_shy_down "... And {b}Missy{/b}'s had a crush on you since, like, the third grade."
    anon f_surprised "S-she has?"
    show anon a_point_self
    show becca b_home_bed f_confused
    with {'master': dissolve}
    becca @ -m_talk "..."
    show becca f_eyeroll
    pause
    show becca a_hips f_annoyed
    with {'master': dissolve}
    becca "So what do you need me for, huh?!"
    show anon a_sides f_confused
    with {'master': dissolve}
    becca "They aren't enough for you?"

    menu:
        "You don't like spending time with me?":
            call bec01_talk_becca.like
        "No, I want you.":

            call bec01_talk_becca.want

    show anon a_up f_worried -of_blush
    with {'master': dissolve}
    anon "Of course, anything... just name them."
    show anon a_sides
    show becca f_annoyed a_finger01
    with {'master': dissolve}
    becca "First off..."
    becca "... I don't ever wanna walk in on you and my mother, ever again!"
    anon f_normal "Not a problem."
    show becca a_hips f_upset
    with {'master': dissolve}
    becca "I mean it, {b}[firstname]{/b}!"
    show anon a_salute
    show becca f_glaring
    with {'master': dissolve}
    anon "Consider it done."
    show anon f_worried
    pause
    show anon a_sides f_normal
    show becca f_annoyed a_finger02
    with {'master': dissolve}
    becca "Secondly..."
    becca "... You gotta talk to {b}Missy{/b} and tell her she's not allowed to bring it up or rub my face in it anymore!"
    show becca a_front
    with {'master': dissolve}
    anon f_worried "That's-"
    anon @ f_skeptical "How am I supposed to manage that?"
    becca f_annoyed "Don't be dumb!"

    if M_missy.taken_dick:
        becca "That skank will do anything you tell her... so long as you promise to keep throwing her a bone now and again."
        anon f_confused "Throwing her a bone?"
    else:

        becca "That skank will do anything you tell her... so long as you promise to throw her a bone now and again."
        anon f_confused "Throw her a bone?"

    becca f_normal "Yeah, you know..."
    show becca a_finger_sex
    with {'master': dissolve}
    pause
    anon f_confused "Ehh?"
    show becca a_hips f_annoyed
    with {'master': dissolve}
    becca "Sex, dummy!"
    show anon f_thinking_down
    with {'master': dissolve}
    anon "Oh."
    show anon a_surprised_up f_surprised
    anon "OH!" with hpunch
    show anon a_sides f_shy_low
    with {'master': dissolve}
    anon "Right."
    anon f_shy "Got it."
    becca @ f_eyeroll "Wow."
    pause
    show becca a_finger03 f_normal
    with {'master': dissolve}
    becca "And lastly..."
    becca "... I want you to tell me the truth."
    anon f_confused "The truth about what?"
    show becca a_hips f_annoyed
    with {'master': dissolve}
    becca "Which of us is better?"
    show anon f_confused
    pause
    anon "Better?"
    show becca a_front
    with {'master': dissolve}
    becca "Yeah."

    if M_missy.taken_dick:
        becca "Like, who do you enjoy having sex with the most?"
    else:
        becca "Like, who are you looking forward to having sex with the most?"

    anon f_worried "Oh, uhh..."

    $ renpy.dynamic(choice=set())

    menu bec01_talk_becca.choice:
        set choice
        "{b}Roxxy{/b} is best.":

            $ choice.add("{b}Tina{/b} is best.")
            jump bec01_talk_becca.roxxy
        "{b}Becca{/b} is best.":

            call bec01_talk_becca.becca
        "{b}Missy{/b} is best.":

            call bec01_talk_becca.missy
        "{b}Tina{/b} is best.":

            jump bec01_talk_becca.tina

    anon f_confused "Hmm?"
    becca f_sexy "Hold on."
    show anon a_surprised_shoulders f_surprised_down behind becca:
        xoffset -150
    show becca b_home_bed_reach
    hide books
    with {'master': dissolve}
    pause
    show anon a_sides f_surprised
    show becca a_phone b_home_bed f_sexy_low:
        xoffset 100
        xzoom -1
    with {'master': dissolve}
    anon "What are you doing?"
    show anon f_confused
    becca "Getting my phone so we can call {b}Roxxy{/b}."
    anon f_normal "Oh, okay."
    anon f_surprised "Wait, what?!"
    anon f_worried "Why do we need to call {b}Roxxy{/b}?"
    show becca a_phone b_home_bed_back f_sexy
    with {'master': dissolve}
    becca "Because you and I are about to have sex and {b}Roxxy{/b} wants to watch..."
    anon a_surprised_up_both f_surprised "!!!"
    show becca b_home_bed f_sexy_low
    with {'master': dissolve}
    becca "... She was very clear about that."
    show anon a_down b_dressed_floor_barefeet f_worried:
        offset (-85, -35)
    show becca a_phone_talk b_home_bed f_sexy as becca_head behind anon:
        crop (0, 0, 1024, 250)
        xoffset 100
        xzoom -1
    show becca a_phone_talk f_sexy:
        align (0., 1.)
        crop (0, 250, 1024, 768 - 250)
    with {'master': dissolve}
    "{i}*Ring* *Ring*{/i}"
    anon "Y-yeah, okay... but-"
    show becca a_phone b_home_bed_back f_annoyed m_talk as becca_head
    show becca a_phone b_home_bed_back f_annoyed
    with {'master': dissolve}
    becca "Shh!"
    show anon f_surprised
    show becca f_surprised -m_talk as becca_head
    show becca f_surprised
    with {'master': fastdissolve}
    "{i}*Ring* *Ring*{/i}"
    show anon f_surprised_left_low of_blush
    show becca f_shy_back_low o_blush
    show becca f_shy_back_low o_blush as becca_head
    with {'master': dissolve}
    pause
    show anon f_worried_low
    show becca b_home_bed f_shy_down:
        crop None
    hide becca_head
    with {'master': dissolve}
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
    show anon f_worried
    show becca a_phone_talk f_shy
    with {'master': dissolve}
    becca "Hey, it's me."
    roxxy "Oh, hey... what's up?"
    becca f_shy_happy "You remember what we talked about the other day?"
    roxxy f_disgusted_out "Ugh, not the bleached asshole thing again..."
    show anon f_surprised -of_blush
    show becca f_disgusted -o_blush
    with {'master': dissolve}
    roxxy f_eyeroll "... {b}Missy{/b} is so disgusting!"
    becca "Eww, no!"
    show anon f_confused
    show roxxy f_bored
    becca f_normal "The other thing..."
    show becca f_shy_down o_blush
    with {'master': dissolve}
    becca "You know, about us having sex with your boyfriend and you watching?"
    show anon f_shock
    roxxy f_smug "Oh, yeah."
    show anon f_worried
    show roxxy b_nails_phone f_horny_down
    with {'master': dissolve}
    roxxy "What about it?"
    show becca f_shy_back
    pause
    becca "Hold on."
    show becca a_phone f_normal_down -o_blush
    with {'master': dissolve}
    roxxy f_suspicious "... Umm, okay?"
    show becca a_phone_facetime f_normal
    show roxxy f_bored_down
    with {'master': dissolve}
    becca "There."
    becca "Can you see us?"
    show roxxy b_hangup f_suspicious
    with {'master': dissolve}
    roxxy "Huh?"
    show anon f_grin
    becca f_laugh "Heh, look at your phone you dumb hooker!"
    show anon f_normal
    show becca f_happy
    show roxxy b_facetime
    with {'master': dissolve}
    roxxy "Oh."
    show anon f_worried_surprised
    roxxy f_annoyed "Hey, what the fuck is {b}[firstname]{/b} doing over there?!"
    becca f_happy "Relax, he's working for my uncle {b}Tony{/b}..."
    show anon f_worried
    becca "... You know, the one who lives across the hall from me?"
    roxxy f_suspicious "The fat guy with the mustache?"
    show becca f_annoyed
    pause
    becca "{b}Tony{/b} isn't fat, he's just big boned."
    roxxy f_smug "Yeah, right."
    roxxy "That's just something fat people say to make themselves feel better."
    show anon f_surprised
    show becca f_upset
    pause
    becca f_annoyed "Ugh, whatever... it's not important."
    show anon f_worried
    becca f_normal "You see, {b}Tony{/b} sent him over to help my mom with something."
    roxxy f_suspicious @ -m_talk "Mhmm?"
    becca f_shy_down "But he's finished with that now and I was sorta thinking... you know... since he's here and all..."
    roxxy f_horny @ f_smug "Oh, you thirsty bitch!"
    show anon f_brag
    becca f_shy_happy "I mean, why waste the opportunity?"
    show roxxy f_horny_lipbite
    pause
    roxxy f_eyeroll "Alright, fine."
    roxxy f_horny "But you have to say it!"
    show becca f_concerned
    anon f_confused "What is happening right now?"
    becca "Aww, you were serious about that?"
    show anon f_surprised
    show becca a_phone_facetime b_home_bed_back f_concerned_lipbite as becca_head behind anon:
        crop (0, 0, 1024, 250)
        xoffset 100 + 300
        xzoom -1
    show becca a_phone_facetime b_home_bed_back f_concerned_lipbite:
        align (0., 1.)
        crop (0, 250, 1024, 768 - 250)
    with {'master': dissolve}
    pause
    show becca o_blush as becca_head
    show becca o_blush
    with {'master': dissolve}
    roxxy @ f_annoyed "{b}Becca{/b} say it!"
    show anon f_confused
    show becca b_home_bed f_shy_low:
        crop None
    hide becca_head
    with {'master': dissolve}
    pause
    becca f_shy_down "I'm a horny beta bitch..."
    show anon f_surprised
    show roxxy f_horny_lipbite
    becca "... And you're my alpha..."
    pause
    show roxxy b_rub
    with {'master': dissolve}
    becca "... Will you please allow your boyfriend have his way with me?"
    show roxxy f_horny_lipbite_close
    anon f_shock "..."
    roxxy f_smug "Hehehe!"
    show anon f_surprised
    roxxy f_horny "Fuck that was hot!"
    show roxxy b_facetime
    with {'master': dissolve}
    roxxy "Alright, go ahead."
    becca f_shy_happy "Thank you!"
    show anon f_brag
    roxxy "But you'd better find a good spot for the phone!"
    roxxy "I wanna be able to see everything."
    becca "Yeah, I will... hold on."
    hide becca
    with {'master': dissolve}
    anon f_worried "Is this seriously happening?"

    scene location_tina_becca_bedroom_evening:
        anchor (712, 400)
        pos (.5, .5)
        transform_anchor True
        zoom 2.5
    show anon b_onbed_back:
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
    roxxy "Yes, this is happening."
    roxxy "Proving once again that I am the world's greatest girlfriend {i}and{/i} best friend!"
    show anon f_shy
    show becca b_home_bed f_concerned_lipbite o_blush behind cam:
        offset (175, 170)
        zoom .9
    show roxxy b_nails f_bored_down
    with {'master': dissolve}
    roxxy "Plus, I'm kinda stuck in my room right now and bored as fuck."
    show becca b_home_bed_undress a_remove_top01
    with {'master': dissolve}
    pause
    show anon f_flirt_low
    show becca a_remove_top02 -o_blush
    show roxxy b_facetime f_annoyed_right
    with {'master': dissolve}
    roxxy "My mom invited my stupid cousin over again and they're sitting outside drinking and cleaning his guns."
    show becca a_remove_top03
    with dissolve
    show becca a_remove_top04
    with {'master': dissolve}
    anon "Ehh, {b}Roxxy{/b}?"
    show anon a_side
    show becca a_sides b_pants_bed
    show roxxy b_nails f_bored_down
    with {'master': dissolve}
    roxxy "I swear, I cannot wait to get my own place..."
    show anon f_surprised_low
    show becca b_home_bed_remove_bottom01
    with {'master': dissolve}
    roxxy "... Anywhere has gotta be better than this dumpy trailer, like even-"
    show becca b_home_bed_remove_bottom02
    with {'master': dissolve}
    anon "{b}Roxxy{/b}?!!"
    show anon f_surprised
    show becca b_naked_bed a_front f_shy_happy_down o_blush
    show roxxy b_lolipop f_horny_lolipop
    with {'master': dissolve}
    roxxy @ -m_talk "Hmm?"
    show roxxy f_curious_lolipop_out
    with {'master': dissolve}
    anon f_flirt "A-am I suppose to-"
    show roxxy b_facetime f_happy_out
    with {'master': dissolve}
    roxxy "Oh, she is REAL eager for that dick, haha..."
    anon "{i}*Gulp*{/i} Y-you want me to-"
    roxxy f_horny_out "... Fuck her, {b}[firstname]{/b}."
    roxxy "And I'll watch."
    show roxxy f_horny_lipbite_out
    anon f_surprised "For real?"
    roxxy @ f_horny_out -m_talk "Mhmm."
    show anon f_flirt of_blush
    with {'master': dissolve}
    anon "That's what you want, {b}Becca{/b}?"
    show becca f_concerned_lipbite_low
    pause
    becca f_shy_happy "Yes."
    roxxy f_curious_out "C'mon, babe... what are you waiting for?!"
    roxxy f_horny_out "Get those clothes off and ravage her!"
    show becca f_concerned_lipbite
    show roxxy f_horny_lipbite_out
    anon "Y-yeah, okay."
    show anon b_onbed_sit_changing3 -of_blush:
        offset (-330, 28)
        yalign 1.
        xzoom -1
    with {'master': dissolve}
    pause
    show anon a_towel b_shorts f_flirt_down:
        reset
        offset (-500, 0)
        xzoom -1
        yalign 1.
        zoom .95
    show becca a_sides
    with {'master': dissolve}
    pause
    show anon b_dressed_changing2:
        offset (0, 0)
        xzoom 1
        yalign 1.
    show anon_overlay_o_underwear_boner1 as boner behind cam:
        offset (30, 75)
        zoom .95
    show becca f_concerned_lipbite_low
    with {'master': dissolve}
    pause
    hide boner
    show anon b_naked_undress_bottom o_boner
    show becca f_shocked_down
    show roxxy f_happy_out m_talk
    with {'master': dissolve}
    pause
    show anon a_sides b_naked f_shy od_naked_dick3 -o_boner
    show becca a_front f_concerned_low m_talk
    show roxxy f_horny_lipbite_close -m_talk
    with {'master': dissolve}
    roxxy @ -m_talk "Mmm."
    show anon a_behind f_shy_left
    with {'master': dissolve}
    roxxy f_horny_out "Yeah, you want that dick, don't you {b}Becca{/b}?"
    show anon of_blush
    show becca f_sexy_low -m_talk
    with {'master': dissolve}
    pause
    becca f_sexy_low "Y-yes."
    roxxy "Who's dick is it?"
    show becca b_naked_bed_back f_annoyed
    with {'master': dissolve}
    becca "Yours."
    roxxy f_smug_out "Louder!"
    becca @ f_annoyed_surprised "It's your dick, {b}Roxxy{/b}!"
    show anon f_surprised
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
    becca @ -m_talk "*Mumbles unintelligibly*"
    show becca b_naked_disheveled_bed_belly behind anon
    roxxy "!!!" with hpunch
    roxxy "Umm, is she okay?"
    anon @ -m_talk "Hmm?"
    show anon b_sit_naked f_shock_low od_dick1:
        offset (-250, 15)
    with {'master': dissolve}
    anon "!!!"
    show anon b_sit_naked_check f_surprised_teeth_low od_naked_dick1 behind becca:
        offset (0, -30)
    with {'master': dissolve}
    roxxy "Oh my god, you killed her with your penis!"
    anon f_worried "N-no..."
    anon f_worried_low "... She's still twitching..."
    roxxy "Hahahaah!"
    anon f_confused_low "... I think?"
    pause
    anon "... {b}Becca{/b}?"
    show anon f_surprised_down
    show becca a_shoo
    with {'master': dissolve}
    becca @ -m_talk "{i}*Whimpers*{/i}"
    show anon f_worried_low
    show becca -a_shoo
    with {'master': dissolve}
    pause
    show anon b_liu_naked f_confused_low -od_naked_dick1:
        offset (-300, -50)
    with dissolve
    roxxy "That was so fucking hot, {b}[firstname]{/b}..."
    roxxy "... I love watching you fuck my friends!"
    anon "Umm, yeah... okay..."
    anon f_worried "... Should we be more worried about her?"
    roxxy "No, she's fine..."
    show anon f_worried_low
    roxxy "... Aren't you, ya dumb skank?!"
    becca f_thinking "Ugh... shut up, {b}Roxxy{/b}..."
    show anon f_worried
    roxxy "See!"
    show becca a_reach f_upset with {'master': dissolve}
    anon f_flirt_low "I thought we lost you for a second."
    becca f_shy_back_low "N-no."
    becca "That was just, really..."
    show anon f_grin
    show becca f_shy_back_down o_blush
    with {'master': dissolve}
    becca "... {i}really{/i}, intense."
    show becca a_phone f_shy
    with dissolve
    show expression stage as stage at local with {'master': local.show}
    roxxy "Hehe!"
    roxxy "{b}Becca{/b}, it so freaking funny watching you try and take my boyfriend's big dick..."
    show anon f_surprised_low of_blush
    show roxxy f_horny_lipbite
    with {'master': dissolve}
    becca f_surprised @ -m_talk "..."
    roxxy f_happy "He literally fucks you senseless with it!"
    show anon f_flirt_low
    becca f_annoyed "No, he doesn't!"
    roxxy f_smug "Yes, he does!"
    roxxy "Heh, you just collapsed into a stuttering mess..."
    show anon f_worried_low -of_blush
    with {'master': dissolve}
    becca f_upset "Grr!"
    roxxy f_laugh m_talk "Hahahaah!"
    anon "Alright, that's enough."
    show becca f_shy_back_low
    anon "There's no reason to-"
    roxxy f_horny -m_talk "{i}*Snort*{/i} I'm sorry but it's funny..."
    show becca f_upset
    if M_missy.taken_dick:
        show anon f_surprised_teeth_low
        roxxy f_smug "... Even {b}Missy{/b} takes it better than her!"
    show roxxy f_laugh m_talk
    becca "Screw you, {b}Roxxy{/b}!!"
    crystal "{b}Roxanne{/b}, yer cousin's leavin'!!"
    show anon f_surprised_low
    show becca f_surprised
    roxxy f_annoyed_right -m_talk @ f_bored "Oh, no... not now."
    pause
    show anon f_worried_low
    show becca f_concerned
    crystal "Ya hear me?"
    roxxy "Yeah, I heard you!"
    crystal "Well, c'mon then... get up off yer keister and say bye to him before he leaves!"
    show anon f_confused_low
    show becca f_confused
    roxxy f_eyeroll "Eugh, no thanks."
    crystal "Who ya in here yappin' with anyways?"
    roxxy f_annoyed_right "None of your fucking business, Mom..."
    show anon f_surprised_low
    show becca f_surprised
    crystal "Now don't you go mouthin' off to me young lady!"
    show becca f_smug
    roxxy b_hangup c_hangup f_annoyed "Go away!!"
    crystal "I swear, I'll pick me a switch and beat the dickens outta you!"
    show anon f_surprised_teeth_low
    show becca f_laugh
    roxxy f_angry "Grr!!"
    hide roxxy
    with {'master': fastdissolve}
    roxxy "Why do you always have to embarrass me in front of my friends, you-"
    show expression stage as stage with {'master': local.hide}
    "{i}*Beep*{/i}"
    show becca f_smug
    anon f_surprised_low "Oh kay..."
    show becca a_reach with {'master': dissolve}
    becca "Heh, serves her right!"
    show anon a_surprised b_sit_naked_up f_normal_low od_naked_dick1 behind becca:
        offset (-30, -30)
    show becca a_down
    with {'master': dissolve}
    anon "... I guess, I should probably get going too."
    show anon f_surprised_low
    show becca b_naked_disheveled_bed_up f_thinking
    with {'master': dissolve}
    becca "Yeah, okay."
    anon f_shy_low "You're gonna be at the beach this weekend, right?"
    becca f_shy_happy_up @ -m_talk "Mhmm."
    becca "I'll be there."
    anon f_flirt_low "Cool."
    hide anon
    show becca f_concerned
    with {'master': dissolve}
    anon "Later, {b}Becca{/b}."
    show becca f_concerned_lipbite
    with {'master': dissolve}
    pause

    scene expression background(512, 368, 2) as stage
    show anon a_towel b_shorts f_looking_down:
        xoffset -250
        xzoom -1
    with fade
    pause
    show anon b_dressed_changing
    show becca b_naked_disheveled f_concerned
    with {'master': dissolve}
    becca "Wait!"
    show anon a_sides b_dressed f_surprised:
        xoffset 250
        xzoom 1
    with {'master': dissolve}
    anon @ -m_talk "Hmm?"
    hide anon
    show becca b_naked_disheveled_kiss:
        xoffset 150
    with {'master': dissolve}
    anon "Mmmm!"
    pause
    show anon a_sides f_surprised behind becca:
        xoffset 75
    show becca b_naked_disheveled f_shy o_blush:
        xoffset -225
    with dissolve
    anon "W-what was that for?"
    becca @ f_shy_down "No reason, I just-"
    becca f_shy_happy "This was fun."
    show anon a_handshake f_shy
    with {'master': dissolve}
    anon "Yeah, it was."
    becca "We should do it again sometime."
    anon "Really?"
    becca "Yeah."
    becca f_shy_down "Just, umm..."
    becca "... Don't tell anybody, okay?"
    anon @ f_happy "Heh, you mean other than {b}Roxxy{/b} and {b}Missy{/b}."
    becca f_concerned @ f_annoyed "Well, yeah... obviously."
    anon "Alright."
    show becca f_shy_happy
    anon "No problem."
    becca "Thanks, {b}[firstname]{/b}."
    show anon a_sides with {'master': dissolve}
    anon "See ya soon."
    hide anon
    with {'master': dissolve}
    becca "Later."
    show becca f_sexy_low
    with {'master': dissolve}
    pause
    show becca a_squeeze f_sexy_lipbite
    with dissolve
    pause

    scene expression background(l=L_apt_hall3) as stage with fade
    show anon f_happy with dissolve:
        xoffset 250
    anon @ -m_talk "( Well, I guess this means I can stop by {b}Tina{/b}'s and hang out with {b}Becca{/b} whenever I want now... )"
    anon f_grin @ -m_talk "( ... How awesome is that?! )"
    pause
    anon f_thinking @ -m_talk "( I'll just have to be careful around her mom. )"
    anon f_thinking_down @ -m_talk "( Who knows how {b}Tina{/b} would react if she learned about what we're doing... )"
    hide anon with dissolve
    return 'afterglow'


label bec01_talk_becca.like:
    anon f_worried "You don't like spending time with me?"
    becca f_concerned "I dunno..."
    show becca a_crossed b_home_bed_back f_shy_low
    with {'master': dissolve}
    pause
    show anon f_shy
    becca "... Maybe a little..."
    pause
    show anon a_surprised_up_both f_surprised_teeth
    show becca b_home_bed f_glaring
    becca @ f_upset "... Before you started boning my mom, you jerk!" with hpunch
    anon f_surprised "I said I was sorry, didn't I?"
    show anon a_sides
    with {'master': dissolve}
    pause
    anon f_worried "Seriously, {b}Becca{/b}... if I'd known she was your mom, I would never have-"
    becca f_eyeroll "Yeah, whatever."
    show becca a_front f_sad_down
    with {'master': dissolve}
    becca @ -m_talk "{i}*Sigh*{/i}"
    pause
    becca f_annoyed "I suppose... I'll consider continuing to show up for our little games at the beach..."
    show becca a_hips
    with {'master': dissolve}
    becca "... But only if you agree to three conditions!"
    return


label bec01_talk_becca.want:
    anon "No."
    anon f_shy "I come to the beach for you."
    show becca a_angry f_surprised
    with {'master': fastdissolve}
    becca @ -m_talk "!!!"
    show becca a_front f_shy_down
    with {'master': dissolve}
    becca "Y-you're just messing with me..."
    anon f_worried "No, I'm serious!"
    anon "Look, {b}Roxxy{/b} and I have our own special thing... which is great..."
    anon "... And {b}Missy{/b} is nice and all..."
    show anon a_liu_shoulder f_shy
    with {'master': dissolve}
    anon "... But you're the one I look forward to seeing most on those nights."
    show becca f_shy o_blush
    with {'master': dissolve}
    becca "You do?"
    anon "Yeah."
    pause
    show anon a_behind_head of_blush
    with {'master': dissolve}
    anon "You're really sexy, you know?"
    show becca a_crossed b_home_bed_back f_shy_down
    with {'master': dissolve}
    becca "That's-"
    show becca f_shy_low
    pause
    show anon a_sides
    with {'master': dissolve}
    becca "I uhh-"
    show becca b_home_bed f_shy_happy_down
    with {'master': dissolve}
    pause
    show becca a_front f_exhausted_closed
    with {'master': dissolve}
    becca @ -m_talk "{i}*Sigh*{/i}"
    becca f_shy "I suppose... I could continue to show up for our little games at the beach..."
    show becca -o_blush
    with {'master': dissolve}
    becca "... B-but only if you agree to three conditions!"
    return


label bec01_talk_becca.becca:
    anon f_normal "You're the best, of course."
    show becca a_front f_shy_happy o_blush
    with {'master': dissolve}
    becca "I am?"
    anon "Oh, yeah... no contest."
    becca f_happy @ f_laugh -m_talk "Hehe, I knew it!"
    becca "I knew I was better than that skinny little skank!"
    anon f_shy "There, see..."
    anon "... you feel better now, right?"
    show anon f_happy
    becca @ f_laugh -m_talk "Yes, much better."
    anon @ f_laugh -m_talk "Happy {b}Becca{/b} is best {b}Becca{/b}."
    becca @ f_laugh -m_talk "Hehe!"
    anon f_normal "So we're good now?"
    anon "You'll be at the beach this weekend with the others?"
    becca f_shy_happy "Yeah, I suppose."
    show becca f_shy_happy_up -o_blush
    with {'master': dissolve}
    becca "Although..."
    becca f_sexy "... Now that you've said I'm the best, I kinda wanna celebrate!"
    return


label bec01_talk_becca.missy:
    show anon a_fists f_normal
    with {'master': dissolve}
    anon "I'd have to go with {b}Missy{/b}."
    becca f_concerned "W-what?!"
    anon "Yeah."
    show anon a_sides f_worried
    show becca a_front f_sad_down
    with {'master': dissolve}
    pause
    anon "I mean, don't get me wrong... you and {b}Roxxy{/b} are really hot..."
    anon f_shy "... Like {i}super duper{/i} hot!"
    becca f_confused "Super duper?"
    show anon f_normal

    if M_missy.taken_dick:
        anon "But {b}Missy{/b} really puts in the extra effort while we're having sex..."
    else:
        anon "But {b}Missy{/b}'s so enthusiastic about it..."

    anon f_happy "... And she makes me laugh...."
    becca @ f_eyeroll "Eugh."
    show anon a_shy_neck f_shy_high
    with {'master': dissolve}
    anon "... And oh my god, those legs..."
    show anon a_cold of_blush
    show becca f_disgusted
    with {'master': dissolve}
    anon "... Sometimes I just want her to wrap them around my head and squeeze the life right out of me."
    becca "Alright, alright, I get it..."
    show anon a_shy_neck f_worried
    show becca a_crossed
    with {'master': dissolve}
    becca f_annoyed "... Shut up already, sheesh!"
    show becca f_thinking
    pause
    show anon a_sides f_confused -of_blush
    show becca a_front f_normal
    with {'master': dissolve}
    becca "Maybe I just need to try harder?"
    return


label bec01_talk_becca.roxxy:
    anon f_normal "I'd have to go with {b}Roxxy{/b}."
    becca f_annoyed @ f_eyeroll "Well, yeah... Obviously, {b}Roxxy{/b}..."
    show anon a_behind_head f_shy
    with {'master': dissolve}
    anon "That's not to say you aren't great... b-because you totally are!!"
    anon "... It's just, {b}Roxxy{/b} and I just have this connection, you know?"
    show becca a_hips
    with {'master': dissolve}
    becca "... I meant between {b}Missy{/b} and I!!"
    show anon a_sides f_worried
    with {'master': dissolve}
    anon "Oh."
    pause
    anon f_thinking "Well, in that case..."
    jump bec01_talk_becca.choice


label bec01_talk_becca.tina:
    show anon a_thinking f_thinking
    with {'master': dissolve}
    pause
    anon "Your mom, maybe?"
    becca f_surprised m_talk "!!!"
    anon f_shy_high "She was really aggressive at first, which was a little scary..."
    show anon a_sides f_brag
    with {'master': dissolve}
    anon "... But in like, a fantastic and super hot way... You know?"
    show becca a_crossed f_glaring -m_talk
    with {'master': dissolve}
    anon f_happy "... And those breasts... I mean, my god... they're like a couple of bean bag chairs..."
    anon "... How does she even find bras big enough to-"
    show anon a_surprised_up_both f_surprised_teeth
    show becca a_angry f_upset_yelling
    becca "Okay, you're a fucking asshole!!!" with hpunch
    show becca a_hips f_glaring
    with {'master': dissolve}
    pause
    show anon a_sides f_worried
    with {'master': dissolve}
    anon "Whoa, relax..."
    anon f_shy "... I was only kidding."
    show becca a_crossed f_annoyed
    becca "Yeah, not funny, {b}[firstname]{/b}."
    show anon a_frustrated f_normal
    with {'master': dissolve}
    anon "Oh, c'mon... It was a little funny..."
    show becca f_glaring
    pause
    anon f_shy "No?"
    pause
    show anon a_sides f_worried_low
    with {'master': dissolve}
    anon "Okay, okay... I'm sorry."
    anon f_worried "For real, the best one is..."
    jump bec01_talk_becca.choice
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
