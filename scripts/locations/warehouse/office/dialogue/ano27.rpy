label ano27_boss_warehouse_office:
    scene location_warehouse_attack_cutscene40
    show text _ ("I mustered my courage and pushed open the door, revealing a darkened office on the other side.") as caption
    with fade
    pause
    hide caption with dissolve
    show text _ ("The air was thick with cigar smoke and the thumping cords of Russian orchestral music playing over a worn record player.") as caption with dissolve
    pause
    hide caption with dissolve
    show text _ ("Raz sat hunched over a desk, working intently as Nadya stood close behind him, boredom written clearly on her face.") as caption with dissolve
    pause

    scene location_warehouse_attack_cutscene30
    show nadya cutscene30 f_bored
    show raz cutscene33 f_normal_down:
        offset (234, 161)
        zoom .6
    with fade
    pause
    show nadya f_smile with {'master': dissolve}
    raz @ -m_talk "Hmph."
    raz "I heard explosion and gunfire, {b}Dimitri{/b}..."
    raz "... I trust you took care of it?"
    anon "I'm afraid {b}Dimitri{/b} won't be coming back, {b}Raz{/b}."
    show nadya f_left
    raz f_confused @ -m_talk "Hmm?"

    scene location_warehouse_attack_cutscene31
    show anon cutscene31
    with fade
    anon @ f_smirking "In fact, last time I saw him, he was lying in a pool of his own blood."
    raz "Who the fuck are you?"
    anon @ f_shocked "What, you don't recognize me?"
    raz "No."
    raz "Why should I?"
    anon "You killed my father!"

    scene location_warehouse_attack_cutscene30
    show nadya cutscene30 f_left
    show raz cutscene33 f_unimpressed:
        offset (234, 161)
        zoom .6
    with fade
    raz "Heh, is that right?"
    pause
    raz f_normal_down "I have killed many fathers, little one..."
    raz "... And many sons as well."
    raz "Why should that make you special, eh?"
    show nadya f_normal
    pause
    anon "Because I'm the one who stole your briefcase."
    show raz f_normal
    show nadya f_left
    with dissolve
    pause
    raz "You?"
    pause
    raz "You are {b}Frank{/b}'s son?"

    scene location_warehouse_attack_cutscene31
    show anon cutscene31
    with fade
    anon "That's right, asshole!"
    anon f_smirking "And I'm here to see that you answer for your crimes!"

    scene location_warehouse_attack_cutscene30
    show nadya cutscene30 f_smirk
    show raz cutscene33:
        offset (234, 161)
        zoom .6
    with fade
    pause
    show nadya f_left
    raz f_smirk "Heh."
    raz "Even from afterlife, {b}Frank{/b} is pain in my ass."
    anon "..."
    raz f_normal_down "We had good thing, you know?"
    raz "Before your idiot father decide to grow conscience."
    anon "Hmm?"
    raz "I bring merchandise from Russia and sell for big monies..."
    raz f_smirk_down "... {b}Rump{/b} keeps policeman out of way..."
    pause
    raz f_normal_down "... And {b}Frank{/b} launder money through car dealership."
    pause
    raz "Is simple plan."
    raz "Very lucrative."
    anon "..."
    show nadya f_concerned
    raz f_normal "{i}*Sigh*{/i} But then {b}Rump{/b} runs his fat mouth to your father..."
    raz "... And spill beans about drugs and sex slaves."
    pause
    raz "Tsk, tsk, {b}Frank{/b} did not take news well, I'm afraid."
    pause

    scene location_warehouse_attack_cutscene32 with fade
    raz "I offer him more monies to keep working."
    pause
    raz "I offer him any two girl he wishes from warehouse."
    pause
    raz "I offer him a future of endless possibilites and in return, he gives betrayal!"

    scene location_warehouse_attack_cutscene31
    show anon cutscene31
    with fade
    anon "That's because my father was a good man!"
    raz "Hmph."
    pause

    scene location_warehouse_attack_cutscene30
    show nadya cutscene30 f_concerned
    show raz cutscene33 f_angry:
        offset (234, 161)
        zoom .6
    with fade
    raz "I say he was stupid man!"
    raz "Only a fool dies for his morals."
    raz "And in the end, what did it accomplish?!"
    raz "I will simply pack up business and begin anew elsewhere."
    raz "Your friends will work off debt your father owes."

    scene location_warehouse_attack_cutscene31
    show anon cutscene31
    with fade
    pause
    raz "Perhaps I will make them to whore themselves in Russian ghetto, eh?"
    anon "That's not going to happen."
    raz "Heh."

    scene location_warehouse_attack_cutscene30
    show nadya cutscene30
    show raz cutscene33 f_smirk:
        offset (234, 161)
        zoom .6
    with fade
    pause
    raz "And who's going to stop me?"
    show nadya f_concerned
    raz "You are soon to be joining your papa in the ground, little one."
    raz "And my enterprise will be reborn, even stronger than before."
    pause
    raz f_normal "But first..."

    scene location_warehouse_attack_cutscene33
    show raz cutscene33
    raz "... I will be needing my briefcase back!" with vpunch
    anon "!!!"
    raz "Tell me where it is and I will kill you quickly!"
    anon "I'm not telling you a damn thing!"
    raz f_smirk "Is that so?"
    pause
    raz "Let's see if you feel same way after I shoot you in kneecap..."
    nadya "Stop it!"

    scene location_warehouse_attack_cutscene34
    show nadya_face_limo_f_serious:
        offset (236, 73)
        zoom 1.1
    with fastfade
    raz "Hmm?"

    scene location_warehouse_attack_cutscene35
    show raz cutscene35 f_annoyed
    with fade
    raz "Beloved?" (show_native="Lyubimyye?")
    raz "What the hell are you doing?!"
    pause

    scene location_warehouse_attack_cutscene36
    show nadya cutscene36 f_annoyed
    with fade
    nadya "Taking what is rightfully mine!"
    pause
    raz "This is not funny, {b}Nadya{/b}... drop the fucking gun!"
    nadya f_smirk "Is no joke, papa..."
    pause
    nadya "Who do you think sent him to steal briefcase?"

    scene location_warehouse_attack_cutscene35
    show raz cutscene35 f_surprised
    with fade
    pause
    raz "Y-you?"
    raz f_annoyed "You did this?!"
    nadya "That's right."

    scene location_warehouse_attack_cutscene36
    show nadya cutscene36 f_angry
    with fade
    nadya "You have led Bratva to ruin!"
    nadya "And now you flee country with tail between your legs like beaten dog... pathetic!"
    raz "You ungrateful child..."
    pause
    raz "... You really think I will let you get away with this?!"
    nadya "It is already done!"
    nadya "Your men are dead and you will join them!"
    show nadya f_smirk
    pause
    nadya "Bye-bye, papa."

    scene location_warehouse_attack_cutscene37
    raz "Traitorous bitch!" (show_native="Predatel'skaya suka!") with hpunch
    nadya "Oof!"

    scene location_warehouse_attack_cutscene31
    show anon cutscene31 f_shocked
    with fastfade
    anon "{b}Nadya{/b}!!!"
    pause
    show anon f_normal
    raz "You're no daughter of mine!" (show_native="Ty mne ne doch'!")

    scene location_warehouse_attack_cutscene38
    anon "You bastard!" with hpunch
    raz "Ack!!"

    scene location_warehouse_attack_cutscene39a with fade
    pause

    scene location_warehouse_attack_cutscene39b with {'master': fastdissolve}
    anon "!!!"
    raz "!!!"

    scene location_warehouse_attack_cutscene39c with fastdissolve
    pause

    label ano27_boss_warehouse_office.retry:
    scene
    show screen minigame_tugofwar(player.stats._str)
    with fastfade
    call screen empty()

    if not _return:
        jump ano27_boss_warehouse_office.fail

    scene location_warehouse_attack_cutscene42
    show raz cutscene42 f_hatred
    with fade
    anon "Haah... Haah..."
    anon "It's over, {b}Raz{/b}!"
    pause
    raz "Just do it, you little shit!"
    pause
    raz "Pull the fucking trigger, if you have balls!"
    nadya "Do it, {b}[firstname]{/b}!"
    nadya "Kill him!"

    $ renpy.dynamic(rv=True)
    if M_harold.lightfingered and M_kim.wallet:
        menu:
            "Pull the trigger. {color=f77b}[[Revenge]{/color}":
                $ renpy.dynamic(rv=False)
            "Wait for the cops. {color=7ff7}[[Justice]{/color}":
                pass

    if rv:
        scene location_warehouse_attack_cutscene43a
        show anon cutscene43 f_calm
        with fade
        pause
        anon "Nah, I'm not gonna kill you, {b}Raz{/b}..."
        anon "... That would be too quick."
        pause
        anon "You're gonna spend the rest of your life suffering behind bars for what you did to my father."
        scene location_warehouse_attack_cutscene43c
        show anon cutscene43 f_calm
        with dissolve
        pause

        scene location_warehouse_attack_cutscene42_gunless
        show raz cutscene42
        with fade
        raz "Is that right?"
        raz "Heh, so you are coward after all..."
        pause
        raz "... Just like your papa."
        pause
        raz @ f_laugh "Hahahaah!"
        pause
        raz f_laugh "Ahahaahaahaaah!!"

        scene location_warehouse_attack_cutscene43d
        anon "!!!" with flashbulb

        scene location_warehouse_attack_cutscene44
        show nadya cutscene36 f_smirk_down:
            offset (337, 84)
            zoom .66
        with fade
        anon "Oh my god-"
        nadya "Burn in hell, you piece of shit!" (show_native="Gori vadu, ty kusok der'ma!")
        pause

        scene location_warehouse_attack_cutscene45_gunless
        show text _ ("It was no secret that Nadya held little love for her father...") as caption
        with fade
        pause
        hide caption with dissolve
        show text _ ("... But this...") as caption
        with dissolve
        pause
        hide caption with dissolve
        scene location_warehouse_attack_cutscene45b_gunless
        show text _ ("... This was hard to fathom.") as caption
        with dissolve
        pause
        hide caption with dissolve
        scene location_warehouse_attack_cutscene45_gunless
        show text _ ("Raznikov Putin Chernyshevsky, the man who had taken my father's life, lay dead at my feet...") as caption
        with dissolve
        pause
        hide caption with dissolve
        show text _ ("... And by his own daughter's hands.") as caption
        with dissolve
        pause
        hide caption with dissolve
        show text _ ("Some would call that poetic justice.") as caption
        with dissolve
        pause

        scene expression background(720, 360, 2.45) as stage
        show nadya a_gun_sides b_traditional f_sexy_down:
            xoffset 75
        show anon a_sides f_shock o_blood_splatter_face:
            xoffset 125
        with fade
        pause
        anon f_angry "{b}Nadya{/b}, what the hell?!"
        show nadya a_gun_what f_frowning with {'master': dissolve}
        nadya "I told you, he must die."
        show anon a_cheek f_annoyed o_blood_splatter
        show nadya a_gun_sides
        with {'master': dissolve}
        anon "He would have spent the rest of his life in prison if we'd just-"
        show anon a_sides with {'master': dissolve}
        nadya "No."
        pause
        nadya "Is too dangerous."
        anon f_worried_low @ -m_talk "..."
        show anon f_disgusted_low
        show nadya f_normal
        nadya "Better this way... you will see."
    else:

        scene location_warehouse_attack_cutscene43a
        show anon cutscene43
        with fade
        pause
        anon "For my father."
        pause

        scene location_warehouse_attack_cutscene43b with flashbulb
        pause

        scene expression background(720, 360, 2.45) as stage
        show anon a_gun_raz_down f_frown_down o_blood_splatter:
            xoffset 250
        with longfade
        pause
        nadya "My god..." (show_native="Bozhe moy...")
        pause
        nadya "... You did it!!"
        show anon a_sides f_tired with {'master': dissolve}
        anon @ -m_talk "..."
        show anon b_empty f_surprised o_empty:
            offset (250 - 30, 8)
        show nadya b_traditional_hug_anon behind anon:
            xoffset 250
        with dissolve
        nadya "You really did it!"
        anon @ -m_talk "!!!"
        hide anon
        show nadya b_traditional_kiss:
            xoffset 125
        with dissolve
        pause
        nadya "Mmm."
        pause
        show anon a_sides f_frown_down o_blood_splatter:
            xoffset 125
        show nadya b_traditional f_sexy:
            xoffset -100
        with dissolve
        pause
        nadya f_worried "Why the frown face?"
        pause
        nadya "{b}[firstname]{/b}?"
        anon f_sad "I-"
        pause
        anon "I killed him..."
        nadya "Uhh, da?"
        nadya f_sexy "That was plan, wasn't it?"
        anon f_sad_down "Y-yeah, it was... I just-"
        show anon f_disgusted_low
        pause

    anon "Eugh, I think I'm gonna be sick."
    nadya f_confused "Sick?"
    nadya f_frowning "Come now, you are being foolish."
    anon f_confused @ -m_talk "Hmm?"
    nadya "My papa was piece of shit!"
    nadya "The world is better place without him."
    anon f_worried "Y-yeah, I know."
    pause
    nadya f_normal "Come."
    show nadya with {'master': dissolve}:
        xoffset -175
    nadya "I will help you forget these feelings."
    hide anon
    show nadya b_traditional_kiss:
        xoffset 25
    with dissolve
    pause
    nadya "Mmm."
    show anon a_sides f_surprised o_blood_splatter:
        xoffset 25
    show nadya b_traditional f_sexy:
        xoffset -275
    with dissolve
    pause
    nadya "I like your lips."
    anon f_flirt "{i}*Gulp*{/i} Y-yeah, I like yours too."
    nadya "Hehe."
    hide anon
    show nadya b_traditional_kiss:
        xoffset -75
    with dissolve
    nadya "Mmm."
    pause
    show anon a_sides f_flirt_grin o_blood_splatter:
        xoffset -75
    show nadya b_traditional f_sexy:
        xoffset -375
    with dissolve
    pause
    nadya "Would you like to make sexy times with me?"
    anon f_surprised "W-what, now?!"
    nadya "Yes."
    nadya "You have made me very powerful woman and I am wet with excitement."
    anon f_shy "{i}*Gulp*{/i} I uhh-"
    pause
    anon f_shy_left "That's a really weird thing to say..."
    nadya "Come, I want you to fuck me on couch!"
    anon f_shy "N-no, I don't think that's a good idea..."
    nadya f_pouting @ -m_talk "Hmm?"
    nadya "Why not?!"

    if rv:
        anon f_worried_low "Y-you know, you just killed your father... and the police will be here any minute..."
    else:
        anon f_worried_low "Y-you know, I just killed your father... and the police will be here any minute..."

    show nadya f_surprised
    anon "... We really shouldn't-"
    show anon f_worried
    nadya f_worried "Tsk, you're right."
    nadya "I should not be here when policeman arrive."
    nadya f_laugh "Good thinking!"
    pause
    nadya f_sexy "Perhaps next time we meet, we will have the sexy times?"
    anon f_shy "Y-yeah, totally."
    anon "Next time."
    pause
    hide anon
    show nadya b_traditional_kiss:
        xoffset -150
    with dissolve
    pause
    nadya "Mmm."
    show anon a_sides f_shy o_blood_splatter:
        xoffset -150
    show nadya b_traditional f_sexy:
        xoffset -450
    with dissolve
    pause
    nadya "I will await our next meeting with much anticipation."
    anon "See ya, {b}Nadya{/b}."
    nadya "Farewell."
    show anon f_worried:
        xoffset -650
        xzoom -1
    hide nadya
    with dissolve
    pause
    anon "What a strange girl."
    pause
    show anon f_frown_down with {'master': dissolve}:
        xoffset -150
        xzoom 1
    anon "{i}*Sigh*{/i}"
    anon @ -m_talk "( Well, I guess this nightmare is finally over... )"
    pause
    show anon f_worried with {'master': dissolve}:
        xoffset -650
        xzoom -1
    anon @ -m_talk "( ... {b}I should head back to Tony and the girls{/b}. )"
    hide anon with dissolve

    scene location_warehouse_attack_cutscene46
    show text "As I descended the stairs, I saw the police were swarming all over, trying to make sense of the mess we had left in our wake." as caption
    with fade
    pause
    hide caption with dissolve
    show text "I should have felt relief at the sight, but I didn't." as caption with dissolve
    pause
    hide caption with dissolve
    show text "Perhaps I was numb after what had transpired upstairs, or maybe I was just too exhausted to care." as caption with dissolve
    pause
    hide caption with dissolve
    show text "Regardless, Harold was quick to take me aside and lead me over to where Tony and the girls were waiting." as caption with dissolve
    pause

    scene expression background(824, 480, 1.75, b=.85, l='warehouse_main_cops') as stage:
        align (0.,  .5)
        xoffset -50
        zoom 2
    show debbie a_cover f_surprised_worried:
        xoffset 0
        xzoom -1
    show tony a_point_under b_casual f_question:
        xoffset 200
    show jenny b_dressed_magic f_concerned:
        xoffset -170
        xzoom -1

    if M_player.ano27_hero == 'tony':
        show tony b_casual_bandage

    with fade
    tony "See, I told ya he'd be fine!"
    show debbie a_mouth_shock f_sad
    show harold b_tanktop f_concerned behind tony:
        xoffset 0
    show anon a_sides f_tired o_blood_splatter behind harold:
        xoffset -150
        xzoom -1
    show tony a_idle f_normal

    if M_player.ano27_hero == 'harold':
        show harold b_tanktop_bandage

    with dissolve
    pause
    show anon a_empty b_empty f_surprised o_empty
    show debbie b_robe_hug_mc:
        xoffset -150
        xzoom -1
    with dissolve
    debbie "Oh, thank goodness you're back!"
    anon "It's alright, {b}[deb_name]{/b}... it's over."
    show harold f_concerned_right_up
    tony f_question "You got the bastard?"
    show harold f_concerned
    anon f_worried_left "Yeah, it's done."
    show anon a_sides b_dressed o_blood_splatter
    show debbie a_front b_robe f_sad:
        xoffset 0
        xzoom -1
    show tony f_smirk
    with {'master': dissolve}
    harold f_suspicious "He's dead?"
    show anon f_worried with {'master': dissolve}:
        xoffset 300
        xzoom 1
    anon @ -m_talk "Mhmm."
    tony "Good."
    harold f_concerned "Let's leave it at that, alright?"
    anon f_confused @ -m_talk "Hmm?"
    harold "It's better if I don't know the details."
    show anon f_worried
    pause
    show harold f_normal with {'master': dissolve}:
        xoffset 480
        xzoom -1
    harold f_normal "Can you make sure they get home safe?"
    show debbie f_sad_back
    tony "Yeah, I can do that."
    show harold with dissolve:
        xoffset 0
        xzoom 1
    harold "I'll drop by to check on you guys as soon as we get this mess sorted out."
    show anon f_shy:
        xoffset -150
        xzoom -1
    show debbie f_sad
    with {'master': dissolve}
    debbie "Thank you, {b}Harold{/b}."
    show harold a_stop f_normal_closed with {'master': dissolve}
    harold "No need to thank me, ma'am."
    harold f_normal "Your tenant is the real hero here."
    show anon a_empty b_empty f_shy_down o_empty
    show debbie b_robe_hug_mc:
        xoffset -150
    show jenny f_eyeroll
    show harold a_sides
    with dissolve
    pause
    show jenny f_sad
    show harold:
        xoffset 480
        xzoom -1
    with {'master': dissolve}
    harold "Give me a minute to distract my unit before you head out."
    tony f_normal "Will do."
    show harold a_radio f_concerned m_talk:
        xoffset 1200
        xzoom -1
    show tony a_idle:
        xoffset 650
        xzoom -1
    with dissolve
    show layer master:
        ease 1. xpos -800
    with None
    tony "Hey, {b}Harold{/b}!"
    show harold f_suspicious -m_talk with {'master': dissolve}:
        xoffset 700
        xzoom 1
    harold @ -m_talk "Hmm?"
    show tony a_point with {'master': dissolve}
    tony "You're alright."
    show harold f_surprised with dissolve
    pause
    show tony a_arms_around f_smirk with {'master': dissolve}
    tony "For a useless cop."
    show harold a_sides f_smirk with {'master': dissolve}
    harold "Heh, yeah... thanks."
    show tony a_idle with dissolve
    pause
    tony "Maybe you come by the pizzeria sometime and we'll have a beer or somethin'?"
    harold "You know, I might just take you up on that."
    pause
    harold "Drive safe."
    hide harold
    show tony a_wave
    with dissolve
    pause
    show anon a_idle b_dressed f_shy o_blood_splatter:
        xoffset 375
        xzoom 1
    show debbie a_front b_robe f_normal:
        xoffset 50
        xzoom -1
    show layer master:
        xpos -800
        ease 1. xpos 0
    with None
    show tony a_idle:
        xoffset 150
        xzoom 1
    with dissolve
    pause
    jenny "Can we go home now?"
    show anon f_worried:
        xoffset -100
        xzoom -1
    show debbie a_front f_sad:
        xoffset -450
        xzoom 1
    show tony f_question
    with {'master': dissolve}
    debbie "Soon, sweetie."
    jenny "It smells like a bunch of unwashed assholes up in here..."
    show anon f_disgusted
    show tony f_surprised
    debbie a_mouth_shock f_surprised "{b}[jen_name]{/b}!!"
    jenny @ f_gross "... Mixed with rotten cabbage and vodka."
    tony f_laugh "Hah!"
    show debbie a_front f_sad:
        xoffset 50
        xzoom -1
    show anon f_surprised_left
    show jenny f_sexy
    show tony a_point_under f_normal
    with {'master': dissolve}
    tony "I like her, she's funny!"
    show anon a_crossed f_unimpressed with {'master': dissolve}:
        xoffset 375
        xzoom 1
    anon "Yeah, right."
    show tony a_idle f_smirk
    with {'master': dissolve}
    anon f_tired "Let's see how you feel after ten minutes stuck in a car with her."
    show debbie f_sad_back
    show jenny a_upset f_upset
    show tony f_laugh
    with {'master': dissolve}
    jenny "Hey, what's that supposed to mean?!"
    show anon a_sides:
        xoffset -100
        xzoom -1
    show debbie f_sad
    show tony f_smirk
    with {'master': dissolve}
    anon "Nothing... nevermind."
    anon "I'm too tired to argue with you right now."
    show debbie f_sad_back
    show jenny a_crossed f_upset_back
    with {'master': dissolve}
    jenny @ -m_talk "Hmph!"
    show anon f_normal
    debbie f_normal "Let's just get home and I'll fix you both some nice hot soup..."
    show debbie with {'master': dissolve}:
        xoffset -450
        xzoom 1
    debbie "... That'll be nice, won't it?"
    show jenny f_nipple3
    pause
    show jenny a_sides f_concerned with {'master': dissolve}
    jenny "That actually does sound good."
    tony f_normal_right "Hmm, they look nice and distracted now."
    show anon f_confused:
        xoffset 375
        xzoom 1
    show debbie f_curious:
        xoffset 50
        xzoom -1
    show tony a_point f_normal
    with {'master': dissolve}
    tony "Let's make like a tree and get outta here."
    show tony a_idle with {'master': dissolve}
    jenny f_happy "Yes, please!"
    show anon a_sides:
        xoffset -125
        xzoom -1
    show jenny:
        xoffset -670
        xzoom 1
    show tony a_point_under:
        xoffset -250
    with dissolve
    pause .25
    show debbie a_nervous:
        xoffset -450
        xzoom 1
    hide jenny
    hide tony
    with dissolve
    debbie "I don't think that's how the expression goes..."
    show anon f_frown_down
    hide debbie
    with dissolve
    anon @ -m_talk "..."
    debbie "C'mon, sweetheart!"
    show anon f_worried
    anon "I'm coming!"
    hide anon with dissolve

    scene location_home_entrance_frontdoor_night
    show location_home_entrance_frontdoor_night_door_overlay as door
    show anon f_tired_happy o_blood_splatter behind door:
        xoffset 15
        xzoom -1
    show jenny a_sides b_dressed_magic:
        xoffset -225
    show debbie a_sides:
        xoffset -500
    with longfade
    debbie "I'll see what kind of soup I have ingredients for in the kitchen."
    hide debbie with dissolve
    show jenny with dissolve:
        xoffset -475
    show anon with dissolve:
        xoffset -235
    show tony b_casual f_sad behind anon:
        xoffset 28

    if M_player.ano27_hero == 'tony':
        show tony b_casual_bandage

    with dissolve
    jenny f_gross "I'm getting in the shower to wash all this grime off!"
    hide jenny with dissolve
    show anon:
        xoffset 60
        xzoom 1
    with dissolve
    pause
    anon f_tired_happy "You wanna come in for soup?"

    if M_player.ano27_hero == 'tony':
        tony "Nah, I think I better head home and take care of this bullet hole."
        show tony f_grimace_down
        show anon a_surprised_up f_worried
        with {'master': dissolve}
        anon "Oh man, I'm sorry {b}Tony{/b}... I completely forgot!"
        show tony f_smirk
        anon "We should get you to the hospital."
        tony f_laugh "Nah, don't be silly... {b}Maria{/b} can patch me up, no problem."
        show anon a_sides f_confused
        show tony f_smirk
        with {'master': dissolve}
        anon "You're sure?"
        tony "Ah, yeah... I've been through worse than this, believe me."
        anon f_normal "Give her my love, will you?"
        tony f_normal "Of course, champ."
        pause
        hide anon
        show tony b_casual_hug_mc f_normal_down:
            xoffset -225
        with hpunch
        anon "!!!"
        tony f_normal_down "Ya did good tonight, champ."
        tony "Your dad woulda been proud of ya."
        pause
        tony f_smirk_closed "I'm proud of ya."
        show tony f_normal_down
        anon "Thanks, {b}Tony{/b}."
        show anon a_sides o_blood_splatter:
            xoffset 60
        show tony a_idle b_casual_bandage f_normal:
            xoffset 28
        with dissolve
        tony "And don't go thinkin' that just because this mess is over, you don't gotta come and see us no more, eh?!"
        tony "We're family now, remember?"
        anon f_shy "Heh, I remember."
    else:

        tony "Nah, I think I better get home to {b}Maria{/b} and let her know everyone's alright."
        anon f_normal "Give her my love, will you?"
        tony f_smirk "Will do."
        pause
        show anon behind tony
        show tony a_mc_shoulder_single f_normal
        with {'master': dissolve}
        tony "Ya did good tonight, champ."
        tony "Your dad woulda been proud of ya."
        show anon f_shy_down
        pause
        tony f_smirk_closed "I'm proud of ya."
        show tony f_smirk
        anon f_shy "Thanks, {b}Tony{/b}."
        show tony a_point with {'master': dissolve}
        tony "And don't go thinkin' you're gonna get outta deliverin' pizza now that your a hotshot hero, eh?!"
        tony f_laugh "I still got mouths to feed!"
        show tony a_hips f_smirk with {'master': dissolve}
        anon f_shy "Heh, I won't."

    tony "See ya soon, champ."
    anon f_normal "Later, {b}Tony{/b}."
    show anon a_wave:
        xoffset 300
    hide tony
    with dissolve
    pause
    show anon a_idle with dissolve
    pause
    show anon f_shy_high with dissolve
    pause
    debbie "Which one sounds better, vegetable beef or creamy potato soup?"
    show anon f_normal with dissolve:
        xoffset -200
        xzoom -1
    anon "Either sounds good to me, {b}[deb_name]{/b}."

    if M_debbie.finished_state(S_debbie_night_visit_three):
        debbie "Why don't you come inside and I'll help you wash up?"
        anon f_flirt "Oh?"
        debbie "Then you can keep me company while I cook dinner."
        hide anon with {'master': dissolve}
        anon "Sounds good to me!"
    else:

        debbie "Why don't you come inside and get washed up?"
        debbie "I'll have the soup done in no time."
        hide anon with {'master': dissolve}
        anon "Yeah, alright."

    pause
    pause
    show anon a_surprised f_surprised_teeth o_blood_splatter with dissolve:
        xoffset 200
    show anon a_reach f_surprised_teeth_left with fastdissolve:
        xoffset 340

    scene black with slowdissolve
    pause 2
    return rv


label ano27_boss_warehouse_office.fail:
    scene location_warehouse_attack_cutscene41a
    if player.stats._str < 10:
        $ display.toast(str_fail)
    show raz cutscene41
    with fade
    raz "Heh."
    pause
    raz "Like father, like son."

    scene location_warehouse_attack_cutscene41b with flashbulb
    pause

    $ A_game_over.unlock()
    show screen confirm(
        _('GAME OVER...'),
        _layer='master',
        background='menu_condom',
        no_action=Return(),
        no_text='Retry',
        yes_action=If(FileLoadable(restorepoint, slot=True),
                     FileLoad(restorepoint, confirm=False, slot=True),
                     ShowMenu('load')),
        yes_text=(_('Restore') if renpy.can_load(restorepoint)
                               else _('Load'))) with gameover
    call screen empty()

    jump ano27_boss_warehouse_office.retry
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
