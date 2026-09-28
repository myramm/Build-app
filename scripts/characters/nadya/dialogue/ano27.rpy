label ano27_plan_nadya:
    scene expression game.timer.image('location_warehouse_pipe{}') as stage
    show keeves b_suit:
        xoffset 50
        xzoom -1
    show nadya b_traditional f_disgusted:
        xoffset -100
        xzoom -1
    nadya "Ugh, this smell is unbearable."
    keeves "We're standing next to a sewage drain, what were you expecting?"
    nadya f_angry "I was expecting not to be involved in this part..."
    keeves "Well, nobody is holding a gun to your head, princess."
    keeves "Why don't you head back inside and let me handle this?"
    show nadya with dissolve:
        xoffset -250
        xzoom 1
    nadya "What, you want get rid of me?!"
    keeves "No, I'm just saying, if your delicate sensibilities can't handle a little-"
    nadya "Do not speak to me like I am child!"
    nadya "I get enough of this talk from papa!"
    keeves @ -m_talk "..."
    show nadya a_crossed f_pouting with {'master': dissolve}:
        xoffset 300
        xzoom -1
    nadya @ -m_talk "Hmph."
    pause
    keeves f_happy "Your dress looks nice by the way."
    keeves "The kid's gonna love it."
    show nadya f_angry with {'master': dissolve}:
        xoffset -250
        xzoom 1
    nadya f_angry "Shut up!"
    nadya "You know father makes me to dress conservative!"
    keeves f_normal @ -m_talk "Mhmm."
    nadya @ f_eyeroll "I'm so sick of stupid men!" (show_native="YA tak ustal ot glupykh muzhchin!")
    nadya "I send you all away once papa is gone."
    nadya "Bratva take only woman after when I'm in charge!"
    keeves "Hush, they're coming."
    show nadya f_worried with {'master': dissolve}:
        xoffset -100
        xzoom -1
    nadya @ -m_talk "Hmm?"
    tony "I think I see 'em over there!"
    harold "Shh!!"
    tony "What?!"
    harold "Can you take it down a notch?!"
    harold "You're gonna bring the whole damn place down on our heads!"
    tony "Good."
    tony "Then we can take 'em all out quick and be home in time to catch the last few innings of the game."
    harold "You can't seriously be that stupid..."
    tony "Hey, who you callin' stupid?!"
    show nadya f_eyeroll
    harold "You realize there's dozens of armed goons in there, right?!"
    show nadya f_worried
    anon "Would you two please stop arguing?"
    tony "Tell that to fuckin' cupcake over there..."
    tony "... She's the one gettin' her panties all in a bunch!"
    show keeves f_happy
    harold "Grr, you're gonna get us all killed!"
    keeves @ f_laugh "Heh, they sound like a colorful bunch."
    anon "Enough, both of you!!"
    show keeves f_normal
    pause
    anon "Jesus!"
    show anon f_worried behind nadya with dissolve:
        xoffset 150
        xzoom -1
    anon "{i}*Sigh*{/i} We're here."
    nadya "Da, we hear you from mile away!"
    show anon f_tired
    show tony a_pipe_hold_shoulder b_casual f_glaring behind anon:
        xoffset 40
    show harold a_gun_side b_tanktop f_angry behind tony:
        xoffset 340
        xzoom -1
    with {'master': dissolve}
    harold "See, I told you!"
    show anon f_eyeroll
    tony f_angry "Aww, shaddup."
    show anon f_worried
    show harold f_angry_right_up:
        xoffset -160
        xzoom 1
    with {'master': dissolve}
    pause
    show anon f_hurt
    show harold f_worried_down
    show tony a_pipe_point_forward f_suspicious
    with {'master': dissolve}
    tony "Why's the gal wearing a potato sack?"
    show anon a_facepalm
    show harold f_worried
    show nadya a_showoff f_surprised_down
    show tony a_pipe_hold_shoulder
    with {'master': dissolve}
    nadya "Wha-"
    show anon a_sides f_annoyed
    show nadya a_crossed f_angry
    with {'master': dissolve}
    nadya "Is traditional dress in my country!!"
    tony "They make you wear potato sacks as a tradition?"
    show anon f_worried
    show keeves f_surprised
    tony "No wonder you Ruskie broads are so vindictive..."
    keeves f_happy @ f_laugh "Pfft, haha!"
    nadya "Go to hell, old man!" (show_native="Poshyel k chyertu, starik!")
    nadya "Is not potato sack!"
    show harold f_worried_right_up
    show tony f_eyeroll
    anon "I think it looks nice."
    show harold f_worried
    show tony f_question
    keeves "See, I was right."
    keeves "The kid likes it."
    anon f_surprised "Wait a second, {b}Father Keeves{/b}?!"
    show harold f_surprised
    show tony f_surprised
    anon "What the heck are you doing here?"
    show harold f_suspicious
    show tony f_suspicious
    anon f_confused "And what's with the traveling salesman getup?"
    nadya f_normal @ f_sexy "You ask me for help, yes?"
    show anon f_worried
    show harold f_worried
    tony f_sad "Ehh, no offense Father... but I'm kinda hopin' nobody will be needin' a priest tonight."
    nadya @ f_laugh "Hah, they think you are real priest!"
    anon f_confused @ -m_talk "Hmm?"
    show harold f_suspicious
    keeves @ f_laugh "Relax fellas."
    show tony f_question
    keeves "My work with the church is just a cover."
    harold "A cover for what?"
    show anon f_surprised
    nadya "He is hired gun."
    nadya "{b}Johnny Silverdick{/b}."
    show anon f_confused
    show harold f_concerned
    tony f_surprised "{b}Silverdick{/b}?!"
    tony f_suspicious "As in THE {b}Johnny Silverdick{/b}?"
    tony "... Who took down the Gogolak Gang up in Chicago?"
    keeves "That was a long time ago."
    tony f_surprised "Holy shit!"
    tony f_normal_right "This guy's a fuckin' legend!"
    tony f_normal "I can't believe you're here in the flesh!"
    show tony a_pipe_handshake
    show keeves a_empty
    with {'master': dissolve}
    tony "This is an honor to be meetin' ya."
    show nadya f_eyeroll
    keeves f_laugh "Please, you're making me blush."
    show nadya f_worried
    show tony a_pipe_hold_shoulder
    show keeves a_idle f_happy
    with {'master': dissolve}
    tony "Hey, is it true you killed Jimmy Tudeski and Frankie Figs with an ink pen?"
    keeves @ f_laugh "Heh, nah..."
    show anon f_worried_surprised
    keeves "... It was actually a number 2 lead pencil."
    tony @ f_laugh "Hah, this fuckin' guy!"
    anon f_worried "Ehh, {b}Tony{/b}?"
    tony f_normal_right @ -m_talk "Hmm?"
    anon "We really need to hurry this along..."
    tony "Oh, shit... you're right."
    tony "My bad."
    show tony f_normal
    pause
    show keeves f_normal
    anon "Have you seen the girls in there?"
    anon "Are they okay?"
    show tony f_sad
    nadya f_worried "{b}Dimitri{/b} has them tied up and will be taking them to interrogation room shortly."
    show anon f_surprised_teeth
    show harold f_worried
    show keeves f_sad
    nadya "They are whole for now but soon he will start removing pieces."
    anon f_worried "Then we need to hurry!"
    show keeves f_normal
    anon "Is this our way in?"
    show nadya behind harold
    show keeves behind nadya
    nadya a_hips_point f_normal "Da, is here."

    scene expression background(500, 384, 1.5, b=0, l='warehouse_pipe') as stage with fade
    anon "It's awfully small..."
    anon "... And stinky."
    tony "Yeah, there's no way I'm fittin' in there."
    pause

    scene location_warehouse_pipe_night as stage
    show keeves b_suit:
        xoffset 50
        xzoom -1
    show harold a_gun_side b_tanktop f_worried:
        xoffset -160
        xzoom 1
    show tony a_pipe_hold_shoulder b_casual f_sad:
        xoffset 40
    show anon a_sides f_worried:
        xoffset 150
        xzoom -1
    show nadya a_crossed b_traditional f_normal:
        xoffset -100
        xzoom -1
    with fade
    nadya "{b}[firstname]{/b} must go alone, I think."
    anon "Aww, man."
    harold "Now wait a second, we can't just send the kid in by himself..."
    show harold f_angry_right_up
    tony f_question "You gonna squeeze your donut eatin' ass in there, cupcake?"
    show harold f_angry with dissolve:
        xoffset 340
        xzoom -1
    pause
    harold "Obviously no... but-"
    tony "Trust me, the kid can handle himself just fine."
    tony f_normal_right "Can't ya, champ?"
    show harold f_worried
    pause
    show anon f_worried_surprised
    nadya "Is no need for concern."
    show anon f_worried
    show tony f_question
    show harold:
        xoffset -160
        xzoom 1
    with {'master': dissolve}
    nadya "I leave my minion {b}Jab{/b} on other side to meet him with bag of supplies."
    harold @ f_suspicious "Your minion?"
    show tony f_sad
    nadya "He is bodyguard."
    nadya "Together they will open path and signal for you to join them."
    nadya "Then you all clear warehouse together."
    anon "Ehh, yeah... okay..."
    pause
    anon "... H-how do I do that, exactly?"
    nadya @ f_eyeroll "Tsk, how should I know?!"
    nadya f_angry "Improvise!"
    show tony f_normal
    anon "Improvise?"
    nadya "My plan for half the men turn on papa in few days, remember?!"
    nadya @ a_hips_point "Is YOU who makes us go tonight!"
    nadya "Now this is problem and YOU must find solution!"
    show harold f_worried_right_up
    tony f_normal_right "Just pop open a door or window and we'll find ya, champ."
    anon f_confused "What about the guards on the outside?"
    show harold f_worried
    show tony f_normal
    keeves "I'll handle them."
    keeves "You just focus on finding a way inside for the others."
    show harold f_worried_right_up
    show tony f_normal_right
    anon f_worried "Y-yeah, okay."

    if M_tony.watches:
        show anon behind tony
        show tony a_mc_hip_single f_normal:
            xoffset 182
            xzoom -1
        show tony_arms_dressed_a_mc_shoulder_single as arm:
            xoffset 182
            xzoom -1
        with dissolve
        tony "Everything's gonna be alright, eh?"
        tony "Those dirty Ruskies got no idea what's about to hit 'em!"
        anon "But what if-"
        tony "You can do this, champ!"
        pause
        anon "Thanks, {b}Tony{/b}."
        hide arm
        show tony a_pipe_hold_shoulder f_normal_right behind anon:
            xoffset 40
            xzoom 1
        with dissolve
        pause

    elif M_mia.finished_state(S_mia_route_split):
        show anon behind harold
        show tony behind anon
        show harold a_gun_side_shoulder f_worried:
            xoffset 282
            xzoom -1
        with dissolve
        harold "You're gonna get through this, son."
        harold "Just keep to the shadows and stay low, yeah?"
        pause
        harold "We'll be there to have your back the second you signal us."
        anon "Thanks, {b}Harold{/b}."
        show harold a_gun_side f_worried_right_up behind tony with dissolve:
            xoffset -160
            xzoom 1
        pause

    anon "Right then."
    pause
    anon "I guess it's time."
    show harold f_concerned
    show keeves a_go
    show tony f_smirk
    show nadya behind keeves
    with {'master': dissolve}
    keeves "You two follow me."
    show keeves a_sides with {'master': dissolve}
    keeves "I'll get you in position to breach in case things go wrong."
    tony "Sounds good."
    harold "Right behind you."
    hide keeves
    hide tony
    hide harold
    show nadya:
        xoffset -650
        xzoom 1
    with dissolve
    tony "{b}Johnny{/b} fuckin' {b}Silverdick{/b}..."
    tony "... Can you believe it?!"
    harold "I've never heard of him."
    tony "... This is awesome!"
    show anon f_worried with {'master': dissolve}:
        xoffset -150
    anon "Where are you going to be for all this?"
    show nadya a_idle f_bored with {'master': dissolve}:
        xoffset -50
        xzoom -1
    nadya "With papa in upstairs office..."
    pause
    show anon a_surprised f_surprised_down behind nadya
    show nadya a_hips_point f_sexy
    with {'master': dissolve}
    nadya "... Waiting for you."
    show anon a_sides f_shy
    show nadya a_idle
    with {'master': dissolve}

    menu:
        "Don't worry, I'll be there.":
            anon f_normal "Don't worry, I'll be there."
            nadya "Confidence is good."
            nadya "You will need it."
            pause
            show nadya b_traditional_kiss_cheek behind anon:
                xoffset -150
            show anon b_empty f_surprised
            with {'master': dissolve}
            anon @ -m_talk "!!!"
            show anon b_dressed
            show nadya b_traditional f_normal:
                xoffset 100
            with {'master': dissolve}
            anon f_shy "What was that for?"
            nadya "For luck."
            nadya "You will need that too."
            pause
            nadya "And for saying you like dress."
            anon "Oh, I do like it."
            anon "You look very pretty."
            pause
            nadya "Then perhaps I wear it for you another time?"
            anon "{i}*Gulp*{/i} I'd like that..."
        "Kiss for luck?":

            anon f_normal "Kiss for luck?"
            nadya f_angry @ -m_talk "Hmph."
            nadya "Mission first."
            nadya "Kisses later."
            anon f_worried "Yeah, okay."
            pause
            anon "I meant what I said by the way..."
            nadya f_worried @ -m_talk "Hmm?"
            anon f_normal "You look very pretty in that dress."
            nadya f_normal @ -m_talk "..."
            nadya @ f_eyeroll "Okay, you convince me!"
            show nadya b_traditional_kiss_cheek behind anon:
                xoffset -150
            show anon b_empty f_surprised
            with {'master': dissolve}
            anon @ -m_talk "!!!"
            show anon b_dressed f_shy
            show nadya b_traditional f_sexy:
                xoffset 100
            with {'master': dissolve}
            nadya "For luck."
            anon f_normal "Oh, it's definitely working..."
            anon "... I can feel it."
            nadya @ f_laugh "Hehe!"

    pause
    nadya f_angry "You go now."
    anon "Y-yeah, okay."
    hide nadya with dissolve
    show anon f_disgusted with dissolve
    pause
    anon @ -m_talk "( Eugh, this is gonna suck... )"
    show anon b_climb_pipe with dissolve:
        xoffset 0
        xzoom 1
    pause

    scene location_warehouse_sewers_cutscene_01
    show text _ ("The interior of the tunnel was dark, slippery, and cramped.") as caption
    with fade
    pause
    hide caption with dissolve
    show text _ ("I thought to use my phone as a flashlight at first but immediately regretted it.") as caption with dissolve
    pause
    hide caption with dissolve
    show text _ ("The muck I was crawling through was better left unseen... And the smell was indescribable!") as caption with dissolve
    pause
    hide caption with dissolve
    show text _ ("My every instinct was screaming to turn back, but that wasn't an option.") as caption with dissolve
    pause
    hide caption with dissolve
    show text _ ("The girls were somewhere on the other side of this abomination and they needed me!") as caption with dissolve
    pause

    show screen minigame_sewer() with fade
    call screen empty()

    scene location_warehouse_sewers_cutscene_02
    show text _ ("It had been pure hell in that sewage drain.") as caption
    with fade
    pause
    hide caption with dissolve
    show text _ ("The horrors I beheld within will haunt me until the end of my days...") as caption with dissolve
    pause
    hide caption with dissolve
    show text _ ("... I will never feel clean again.") as caption with dissolve
    pause

    scene expression background(312, 360, 2.5, l=L_warehouse_sewer) with fade
    show anon f_disgusted_low o_sewage with dissolve:
        xoffset -250
        xzoom -1
    anon @ -m_talk "( Hell, thy name is sewage drain. )"
    anon @ -m_talk "( No way I'm going back in there! )"
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
