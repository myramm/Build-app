label ano27_init_jab:
    scene location_hill_limo_closeup_evening
    show thug
    show anon f_annoyed with dissolve
    anon "Oh, great... it's you."
    thug @ f_laugh "{b}Dimitri{/b}'s little bunny!!"
    thug "You bring more money for me?"
    anon "No."
    anon "I think you have enough of my money, don't you?"
    thug "Aww, don't take it so personal..."
    thug "... Is my job to take the monies."
    show anon f_hurt a_facepalm with dissolve
    pause
    anon a_idle f_snarky "Where's your girlfriend?"
    thug f_confused "Girlfriend?"
    show anon f_flirt_grin
    thug "I don't have-"
    show thug f_surprised
    pause
    show anon f_grin
    thug f_angry "Oh, haha... very funny."
    show anon f_normal
    thug a_point "How about I put fist through your face, eh?"
    show anon f_worried
    thug f_normal "We see who laughing then."
    show thug a_idle with {'master': dissolve}
    anon f_annoyed "Yeah, whatever."
    anon "Look, I've got a meeting with {b}Nadya{/b}... you gonna let me pass?"
    show thug f_angry
    pause
    thug "Fine."
    thug a_point "But remember this..."
    thug "... I eat piece of shit like you for breakfast!"
    anon f_disgusted @ f_skeptical "Eww, you eat shit for breakfast?"
    thug "Yes, that's-"
    show thug f_confused a_thinking with dissolve
    pause 0.5
    thug a_point "Err, wait... no!"
    thug f_angry "This not what I'm saying!"
    show thug a_idle with {'master': dissolve}
    anon f_confused @ -m_talk "..."
    thug a_point "You are the shit in this scenario... so then I would be eating-"
    thug a_thinking f_confused "Ehh, no... this not right either."
    show anon f_worried_surprised
    thug f_angry a_idle "Dammit!" (show_native="Yoperesete!")
    thug "Is all jumbled now!"
    anon f_worried @ -m_talk "..."
    show anon f_confused
    thug f_confused "Usually I eat nice syrniki with bowl of kasha..."
    anon "Uh huh."
    thug "... But this is metaphor for making you into corpse."
    nadya "{b}Jab{/b}, stop talking and open door!"
    show thug f_wincing
    nadya "... Fucking asshole." (show_native="... Grebanyy mudak.")
    show anon f_snarky
    jab f_concerned "Y-yes, of course!"
    jab "Sorry, {b}Miss Chernyshevsky{/b}."
    jab "{i}*Ahem*{/i} She will see you now."
    anon @ -m_talk "Mhmm."

    scene location_hill_cutscene_limo_enter
    show text _ ("It felt like I was walking into a lions den...") as caption
    with fade
    pause
    hide caption with dissolve
    show text _ ("Could {b}Nadya{/b} really be trusted?") as caption with dissolve
    pause
    hide caption with dissolve
    show text _ ("At least I wasn't getting thrown into the vehicle this time.") as caption with dissolve
    pause

    scene location_mugging_limo_back
    show nadya b_dress_limo2
    with fade
    nadya "You must forgive my bodyguard..."
    nadya "... He is good man and loyal to me, but his head is empty."
    anon "Hmm?"
    nadya "Like untrained puppy dog, I must teach him to stop making potty on carpets."
    anon "Right."
    anon "Okay."
    pause
    anon "I really hope that's a metaphor..."
    nadya "You bring briefcase?"
    anon "It's right here."
    show nadya b_dress_limo9 with dissolve
    nadya "May I see it?"
    pause
    anon "S-sure."
    show nadya b_dress_limo5 with dissolve
    pause
    show nadya b_dress_limo6 f_normal_down with dissolve
    pause
    show nadya b_dress_limo7 f_surprised_down with dissolve
    nadya @ -m_talk "!!!"
    pause
    anon "We happy?"
    nadya f_smirk "Da, we happy."
    show nadya b_dress_limo6 with dissolve
    pause
    show nadya b_dress_limo14 with dissolve
    pause
    nadya "I must say, I'm surprised..."
    show nadya b_dress_limo15 with dissolve
    nadya "... I did not believe you truely capable."
    show nadya b_dress_limo14 with dissolve
    anon "Well, you're not the first person to underestimate me."
    nadya "Heh, this is true."
    nadya "I hear about {b}Mayor Rump{/b}'s little fuckboy from car dealership."
    anon "You mean {b}Kim{/b}?"
    nadya "Da, {b}Kim{/b}."
    nadya @ f_laugh "Hahaha, the picture on news... hilarious!"
    pause
    anon "So, does this mean you're gonna keep to your end of the bargain?"
    nadya @ -m_talk "Hmm."
    nadya f_normal "Da."
    nadya "But can I trust you will pull trigger?"
    anon "P-pull trigger?"
    nadya "If I get you in room with papa..."
    nadya f_angry "... I want him dead, not arrested!"
    pause
    nadya f_confused "You have balls to do this?"
    anon "I uhh..."
    anon "... Yes?"
    nadya f_serious "Then we must act soon."
    nadya "He is already packing up operation for return to Russia."
    anon "I'm ready to go now."
    nadya f_smirk "Heh, you're eager... this is good."
    pause
    nadya f_serious "At warehouse, there is sewage drain that leads to chemical storage room."
    nadya "That is entry point."
    anon "You want me to crawl in through a sewage drain?"
    nadya f_smirk "Da."
    pause
    nadya f_confused "Is this problem?"
    anon "N-no, I guess not."
    pause
    nadya f_smirk "Give me few days and I will use this to turn many men against him."
    pause
    nadya f_serious "I will contact you... but you must be ready!"
    nadya "We cannot let opportunity slip away!"
    anon "I'll be ready."
    nadya f_normal "Good." (show_native="Khoroshiy.")
    pause
    nadya "When papa is dead, we will be friends..."
    nadya f_smirk "... Or perhaps more?"
    anon "{i}*Gulp*{/i} M-more?"
    nadya "Heh, we will see what future brings."
    pause
    nadya f_serious "Now... leave me."
    anon "Y-yeah, okay."
    show nadya f_serious_right
    pause
    nadya f_angry_right "{b}Jab{/b}, time to go!" (show_native="{b}Jab{/b}, vremya idti!")
    nadya "We have work to do." (show_native="Nam yest' nad chem rabotat'.")
    jab "Y-yes, {b}Miss Chernyshevsky{/b}."
    show nadya f_angry
    pause
    jab "You want I should take the-"
    nadya f_angry_right "Don't start with the questions, just drive the fucking car!"

    scene expression L_pizzeria_interior.background_closeup as underlay:
        xoffset 415
    show tony a_phone_talk:
        xoffset 465
        xzoom -1
    show expression game.timer.image('char_xtra_12{}') as counter:
        xoffset 415

    $ renpy.dynamic(stage=background(824, 400, 3.2))
    show expression stage as stage
    with fade
    show anon f_laugh with dissolve:
        xoffset -500
        xzoom -1
    anon @ -m_talk "( Heh, it's nice to see that asshole sweat a little after all the problems he's caused me. )"
    anon f_grin @ -m_talk "( I think I'm going to like working with {b}Nadya{/b}. )"
    show anon a_phone f_looking_down with dissolve
    pause
    show anon f_normal a_phone_talk with dissolve
    "{i}*Ring* *Ring*{/i}"
    show expression stage as stage at phoneright with phoneright.show
    tony "{b}Tony{/b}'s pizza, go for {b}Tony{/b}."
    anon "It's me."
    tony @ f_laugh "Oh, hey champ!"
    tony "You been to see the {b}Ruskie{/b} broad yet?"
    anon "Yeah, I just finished with the meeting actually."
    tony "Well, seein' as how you're still alive and callin', I'm gonna assume it went well?"
    anon "It did."
    anon "She gave me a way inside the warehouse and asked for a couple days to turn some of her father's men against him."
    tony f_smirk "No kiddin'?"
    tony "So we can expect some back-up once shit hits the fan?"
    anon "That's what she says..."
    show tony f_sad
    pause
    tony f_suspicious "... And you're confident she ain't gonna stab us in the back the second the job's done?"
    anon f_worried "Pretty confident."
    pause
    anon "I can just go myself if you're worried... I don't wanna risk your new family if-"
    tony f_angry "No, no, no... don't start with that shit."
    tony "I promised I'd help ya get justice for your father and that's exactly what I'm gonna do."
    tony f_suspicious "Just makin' sure I got all the information."
    pause
    anon "She wants this real bad..."
    anon "... And I'm not sure what she'd stand to gain from double-crossing us."
    tony "Well we should plan a contingency for it anyways."
    show anon f_worried_surprised
    tony f_normal "It's often the bullet ya don't see comin' that gets ya."
    pause
    show anon f_worried
    tony "We'll start plannin' tomorrow, yeah?"
    anon "Yeah, okay."
    tony @ f_laugh "Good."
    tony "I'll have {b}Maria{/b} cook us up somethin' special, eh?"
    tony "One last blowout before we charge into the lions den."
    anon f_normal "Sounds good, {b}Tony{/b}!"
    tony "Just make sure ya bring your appetite!"
    anon "Heh, I will."
    pause
    anon "See you then."
    tony "Later, champ."
    show anon a_phone f_looking_down with dissolve
    show expression stage as stage with {'master': phoneright.hide}
    "{i}*Beep*{/i}"
    show anon a_idle f_normal with dissolve:
        xoffset 0
        xzoom 1
    pause
    anon @ -m_talk "( Sounds like tomorrow's gonna be a busy day. )"
    anon @ -m_talk "( I should head home and get some rest. )"
    hide anon with dissolve
    return


label ano27_jabb_jab:
    show thug a_bottle f_disgusted
    show anon a_surprised f_surprised_teeth_down o_sewage with dissolve
    jab "Eugh, you reek!"
    anon f_annoyed "Yeah, thank you, Captain Obvious."
    jab "No, seriously!"
    jab "You smell like, two hobos having the gay sex inside gym bag full of year old dirty socks."
    anon f_unimpressed @ -m_talk "..."
    jab f_normal "No, no..."
    jab "You smell like, rotten eggs dipped in public toilet of Indian restaurant and left lying in a nest of burning human hair!"
    pause
    anon "You done?"
    jab @ f_laugh "Heh, yes."
    anon f_tired "Goo-"
    show anon f_confused
    jab a_bottle_finger @ f_surprised "Err... wait, no!"
    jab "I have one more!"
    anon a_sides f_unimpressed @ -m_talk "..."
    jab a_bottle "You smell like, lutefisk cooking in crockpot with sack full of dirty pennies and blue-green algae next to a tepid pool of sulphur."
    jab @ f_laugh "That's exactly what you smell like!"
    pause
    anon "Very funny."
    anon f_worried_low a_point_down "Are those the supplies {b}Nadya{/b} left me?"
    jab "Da."
    anon a_sides "{i}*Sigh*{/i} It had better be something good."
    show anon b_dressed_pickup o_sewage_pickup with {'master': dissolve}
    jab f_normal_down m_talk "Prepare to be disappointed."
    show thug a_bottle_drink f_drink -m_talk with {'master': dissolve}
    anon "What the-"
    pause
    show thug a_bottle_empty f_confused_down with {'master': dissolve}
    anon "A bar of soap and a towel?!"
    show thug f_concerned
    show anon b_dressed f_angry a_rag o_sewage
    with {'master': dissolve}
    anon "This is all she left?!"
    jab "What were you hoping to find?"
    show thug a_bottle_throw f_normal with {'master': dissolve}
    anon f_annoyed "I dunno... something useful?!"
    show thug b_dressed a_idle with {'master': dissolve}
    jab "Trust me, soap very useful for you now."
    anon "There's not even any water!"
    jab f_confused "Oh, ehh..."
    show thug f_confused_down with {'master': dissolve}:
        xoffset 500
        xzoom -1
    jab "... Shit."
    pause
    show thug f_concerned with {'master': dissolve}:
        xoffset 0
        xzoom 1
    jab "My bad."
    pause
    anon "You're a fucking asshole, {b}Jab{/b}."
    jab f_normal "Yes, you are not the first to tell me this..."
    anon f_sad_down "{i}*Sigh*{/i} I guess, I'll just have to make do."
    show anon f_hurt a_rag_wash_face with dissolve
    jab "Perhaps you can weaponize foul odor and unleash it upon my former comrades, eh?"
    show anon o_sewage_body a_rag_wash_shirt f_looking_down with dissolve
    jab @ f_laugh "Haha!"
    show anon o_empty a_rag_throw f_normal with dissolve
    anon "Done."
    show anon a_sides with dissolve
    show thug f_surprised
    jab @ -m_talk "Hmm?"
    anon "Now we need to find a way to sneak my friends inside."
    jab f_confused "Ehh, how you do this?!"
    anon "Are there any exits nearby?"
    jab f_confused_down a_scratch_head "You were filthy but now you pristine... I don't-"
    anon f_worried @ f_annoyed "{b}Jab{/b}, focus!"
    jab f_confused a_idle "Ehh, sorry... what is question?"
    anon "How do we get my friends inside?!"
    jab f_concerned "Oh."
    jab "Umm... this is going to be problem."
    jab "Closest entrance is main warehouse floor."
    jab "Many guards there!"
    anon "Show me."
    jab f_normal @ a_defensive "Ehh, I think no."
    anon f_surprised "No?!"
    anon f_angry "What do you mean, no?!"
    jab "I'm not going..."
    jab "... Is suicide mission!"
    anon f_annoyed "{b}Nadya{/b} promised me you'd help!"
    jab "Well, {b}Miss Chernyshevsky{/b} not here... is she?"
    anon "You're seriously not going to help me?!"
    jab "I tell you go to main warehouse floor, yes?"
    pause
    jab @ a_point "It's that way."
    pause
    anon f_unimpressed "Ugh, fine."
    anon a_give_me "Just give me your gun and I'll go alone."
    jab f_angry "What, no!"
    jab "Is my gun!"
    pause
    anon f_tired "Man, c'mon!"
    jab f_concerned "No way."
    jab "I need my gun."
    anon f_skeptical "Why would you possibly need a gun cowering back here in the storage room?"
    jab "Ehh, I don't know... big rat, maybe?"
    show anon a_sides f_unimpressed with dissolve
    pause
    anon "A big rat?"
    jab "Yes, with huge claws and a taste for human blood."
    anon "You are unbelievable."
    pause
    anon f_annoyed a_frustrated "Screw you, {b}Jab{/b}!"
    show anon a_sides with {'master': dissolve}:
        xoffset -500
        xzoom -1
    jab f_laugh a_wave "Bye."
    show thug a_idle f_normal
    hide anon
    with {'master': dissolve}
    jab "Have a great time!"
    anon "You suck."
    return


label ano27_peek_jab:
    show thug a_bottle
    show anon f_worried with dissolve
    jab "Any luck, comrade?"
    anon "No."
    pause

    if not M_jab.once('water'):
        anon f_surprised_low "Wait..."
        anon f_angry "How'd you get another bottle of water?"
        jab "I uhh... I find it."
        anon "What do you mean, you found it... where?!"
        jab "Was in supplies."
    else:
        anon f_surprised_low @ -m_talk "..."
        anon f_surprised "Okay, seriously... how much water are you hiding from me?"

    jab "You want?"
    anon f_unimpressed @ -m_talk "..."
    anon f_skeptical "Well, it's no good to me now, is it?!"
    pause
    anon f_annoyed "Your gun on the other hand..."
    jab @ f_laugh "Yes, gun is very useful."
    jab "Maybe is best if you crawl back into sewage drain and go find one..."
    anon a_frustrated "Screw you, {b}Jab{/b}!"
    show anon -a_frustrated with {'master': dissolve}:
        xoffset -500
        xzoom -1
    jab @ f_laugh "Bye."
    hide anon with {'master': dissolve}
    jab "Have a great time!"
    show thug a_bottle_drink f_drink with {'master': dissolve}
    anon "You suck."
    show thug a_bottle_throw f_normal with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
