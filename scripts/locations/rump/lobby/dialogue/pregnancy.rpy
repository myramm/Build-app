label rump_lobby_iwanka_baby_first:
    scene expression background(800, 472, 2.5) as stage
    show iwanka a_baby:
        flip
    show anon behind iwanka with dissolve:
        flip
    anon "Hey, you two are finally home, huh?"
    iwanka "Yeah, finally!"
    if M_iwanka.pregnancy.baby_gender == "boy":
        anon "How's my little guy doing?"
    else:
        anon "How's my little girl doing?"
    show anon f_normal_low with dissolve:
        xoffset -200
    show iwanka f_smirk_down
    pause
    anon f_skeptical "Is that an earring?"
    iwanka "Yeah, doesn't it look great?"
    anon f_worried "Ehh, how did you-"
    iwanka "The guy didn't wanna do it at first but I slipped him a couple hundred bucks and he changed his mind."
    if M_iwanka.pregnancy.baby_gender == "boy":
        anon "A-and the crown?"
    else:
        anon "A-and the tiara?"
    iwanka f_smirk "Pretty awesome, huh?"
    iwanka "Only twelve grand."
    anon f_surprised @ -m_talk "!!!"
    if M_iwanka.pregnancy.baby_gender == "boy":
        anon "You spent twelve thousand dollars on a baby crown?!"
    else:
        anon "You spent twelve thousand dollars on a baby tiara?!"
    iwanka f_annoyed "Well, it's my father's money so who cares?"
    anon "I have no words..."
    show melonia b_dressed_magic f_disgusted with dissolve
    show anon f_worried with dissolve:
        unflip
        xoffset 200
    melonia "What is that smell?"
    pause
    iwanka f_bored "{i}*Sigh*{/i} Hello, {b}Mother{/b}."
    melonia @ f_confused "Is that a baby?"
    melonia "Why do you have a baby?!"
    if M_iwanka.pregnancy.baby_gender == "boy":
        anon "It's your grandson."
    else:
        anon "It's your granddaughter."
    melonia @ f_surprised "What?!"
    melonia "Oh my god, {b}Iwanka{/b}... Tell me you didn't adopt a child!"
    show anon f_shock a_sides with dissolve
    iwanka "No, I didn't adopt a child, {b}Mother{/b}..."
    show anon f_worried
    melonia f_confused "Well then how did you-"
    show melonia f_surprised
    pause
    melonia f_confused @ f_pouting "{i}*Gasp*{/i} You didn't steal it, did you?"
    show anon f_worried_left
    iwanka f_annoyed "Of course not!"
    show anon f_worried
    melonia f_annoyed "No, I don't want details!"
    melonia @ a_point "Just take it back to wherever you found it before someone realizes it's missing."
    show anon f_worried_left
    iwanka "Oh em gee, {b}Mother{/b}..."
    show anon f_worried
    hide melonia with dissolve
    melonia "I need a drink!"
    pause
    anon "Wow."
    show anon with dissolve:
        flip
        xoffset -200
    iwanka "I told you."
    iwanka f_smirk_down "Let's get you upstairs and fed, huh?"
    hide iwanka with dissolve
    if M_iwanka.pregnancy.baby_gender == "boy":
        iwanka "You're a hungry boy, aren't you?"
    else:
        iwanka "You're a hungry girl, aren't you?"
    anon @ a_frustrated -m_talk "( What the in hell is wrong with this family? )"
    hide anon with dissolve
    return


label rump_lobby_melonia_pregnancy_first:
    scene expression background(800, 472, 2.5) as stage
    show anon with dissolve:
        flip
    pause
    show anon f_worried
    show melonia f_glaring:
        flip
    with {'master': dissolve}
    melonia "YOU!"
    anon "{b}Melonia{/b}?"
    show melonia b_dressed_mad with fastdissolve
    show melonia b_dressed:
        xoffset 200
    show anon f_surprised a_surprised_up_both:
        xoffset 70
    with {'master': fastdissolve}
    anon "Ehh, what's going on?"
    melonia f_yell "What's going on?!"
    show anon a_sides with dissolve
    melonia "WHAT'S GOING ON?!!"
    melonia "I'll tell you what's going on!"
    melonia "I'm pregnant!"
    show melonia f_glaring
    anon f_shock "!!!"
    anon "You're-"
    anon f_worried "I thought you were on birth control?"
    melonia f_yell "I am on birth control!"
    melonia "The stupid doctor must have screwed something up!"
    melonia "I swear to god, I'm gonna kill her!"
    show melonia f_glaring
    anon "Okay, you really need to calm down..."
    melonia f_yell "Hmph, don't tell me to calm down!"
    melonia "This is your fault!"
    show melonia f_glaring
    anon a_sides @ a_point_self "My fault?!"
    melonia @ a_point "You and that glorious cock of yours!"
    anon "Are you even sure it's mine?"
    melonia "What the hell kind of question is that?!"
    melonia @ f_yell "Of course it's yours!"
    anon "Well, I dunno, I'm just checking."
    melonia "Now I have to go to the clinic and get it taken care of..."

    menu:
        "Do you want me to come with you?":
            jump rump_lobby_melonia_pregnancy_first.support
        "Don't do that!":

            pass

    anon f_surprised "Don't do that!"
    melonia f_confused "Huh?"
    anon f_shy "You should have it."
    melonia f_annoyed "Are you out of your mind?!"
    show anon f_worried
    melonia "I don't want a stupid baby!"
    anon "Why not?"
    melonia "Because I already had one and she's been nothing but a pain in my ass!"
    anon "Yeah, but this one is ours."
    anon "You can't just get rid of it!"
    melonia "Oh, yes I can!"
    melonia "If you think I'm going to spend nine months sober and unable to use my hot tub, you've got another thing coming!"
    anon "{b}Melonia{/b}..."
    melonia "There isn't anything you could say that's gonna make me change my mind on this, {b}[firstname]{/b}!"

    menu:
        "Fine, you win.":
            jump rump_lobby_melonia_pregnancy_first.relent
        "You wanna bet?!":

            pass

    anon f_skeptical "You wanna bet?!"
    melonia "Hmph, let's hear it then..."
    melonia f_smirk "This oughta be rich!"

    if not player.has_required_chr(10):
        jump rump_lobby_melonia_pregnancy_first.threaten

    anon "If you do this..."
    show anon f_thinking
    pause
    $ display.toast(chr_pass)
    anon f_angry @ a_point_self "... You can kiss my glorious cock goodbye!"
    melonia f_annoyed "You wouldn't."
    anon "Watch me!"
    anon "I want this baby, {b}Melonia{/b}!"
    anon "And I will absolutely stop having sex with you if you get rid of it!"
    melonia f_surprised @ -m_talk "..."
    melonia "That's not-"
    pause
    melonia @ f_glaring "Grr!!"
    melonia "Fine, you win!"
    anon f_normal "Yeah, I thought that might make you reconsider."
    melonia "... Asshole."
    pause
    melonia "{i}*Sigh*{/i} You're the only person in the world who could get away with this shit..."
    melonia @ a_point "... And you're gonna be at my beck and call during this entire pregnancy!"
    anon "Agreed."
    melonia "I'm serious."
    melonia "Anything and everything I ask for, you're doing it!"
    anon "Absolutely!"
    melonia f_annoyed "You can start by getting the hell away from me because I kinda wanna stab you right now..."
    anon f_worried "Well then, maybe I'd better do that!"
    melonia a_fists "Yeah, maybe you should!"
    anon "Fine!"
    melonia "Good!"
    show melonia f_pouting with dissolve:
        xoffset -400
    pause
    anon "I'll see you later."
    melonia @ -m_talk "Hmph!"
    hide melonia with dissolve
    anon f_normal @ -m_talk "( Holy crap, it worked! )"
    pause
    anon @ -m_talk "( I can't believe it... )"
    anon @ -m_talk "( I'm gonna be a father! )"
    anon @ f_laugh -m_talk "( This is so exciting! )"
    hide anon with dissolve
    return True


label rump_lobby_melonia_pregnancy_first.relent:
    anon f_tired "Fine, you win."
    melonia "Why don't you do us both a favor and get yourself snipped?"
    anon f_worried "Huh?"
    melonia "Then we wouldn't have to worry about this kind of thing."
    anon "Yeah, that's not happening..."
    melonia "Grr, I need a drink!"
    hide melonia with dissolve
    pause
    anon @ -m_talk "( Well, I guess that settles that... )"
    hide anon with dissolve
    return


label rump_lobby_melonia_pregnancy_first.support:
    anon "Do you want me to come with you?"
    melonia "Don't be ridiculous, I'm not some fragile teenage girl that needs her hand held."
    melonia "It's just an abortion."
    anon "Sheesh, alright."
    melonia "Why don't you do us both a favor and get yourself snipped?"
    anon "Huh?"
    melonia "Then we wouldn't have to worry about this kind of thing."
    anon "Yeah, that's not happening..."
    melonia "Grr, I need a drink!"
    hide melonia with dissolve
    pause
    anon @ -m_talk "( Well, I guess that settles that... )"
    hide anon with dissolve
    return


label rump_lobby_melonia_pregnancy_first.threaten:
    anon f_angry "If you do this..."
    anon f_thinking "... I'm gonna-"
    show anon f_worried
    pause
    anon "I'll-"
    melonia f_annoyed "You'll what?!"
    show anon f_angry
    pause
    $ display.toast(chr_fail)
    anon "... I'll be very, very angry with you!"
    melonia f_smirk @ f_laugh "Hah!"
    melonia "Like I give a shit about that."
    anon @ -m_talk "..."
    melonia f_annoyed "Why don't you do us both a favor and get yourself snipped?"
    anon f_worried "Huh?"
    melonia "Then we wouldn't have to worry about this kind of thing."
    anon "Yeah, that's not happening..."
    melonia "Grr, I need a drink!"
    hide melonia with dissolve
    pause
    anon @ -m_talk "( Well, I guess that settles that... )"
    hide anon with dissolve
    return


label rump_lobby_melonia_pregnancy:
    scene expression background(800, 472, 2.5) as stage
    show melonia f_glaring:
        flip
    show anon f_worried with dissolve:
        flip
    melonia "YOU!"
    anon "{b}Melonia{/b}?"
    show melonia b_dressed_mad with fastdissolve
    show melonia b_dressed with {'master': fastdissolve}:
        xoffset 200
    anon f_surprised a_surprised_up_both "Ehh, what's going on?"
    melonia f_yell "What's going on?!"
    show anon a_sides with dissolve
    melonia "WHAT'S GOING ON?!!"
    melonia "I'll tell you what's going on!"
    melonia "I'm pregnant again!"
    show melonia f_glaring
    anon "Again?!"
    melonia "What, do you have like, super sperm or something?!"
    anon "I don't know, I-"
    melonia "Grr!!"
    melonia "Well, I can tell you one thing!"
    melonia "There is no fucking way I'm doing this again!"

    menu:
        "You wanna bet?!":
            pass
        "No, we have plenty.":

            jump rump_lobby_melonia_pregnancy.abort

    anon f_skeptical "You wanna bet?!"
    anon f_angry "You get rid of that baby and we're done."
    melonia f_pouting "That's not-"
    pause
    melonia f_annoyed "Be reasonable, {b}[firstname]{/b}!"
    anon "If you want me to continue fulfilling your needs, you are having this baby."
    show melonia f_glaring
    melonia @ -m_talk "..."
    melonia "Fine, I'll have your stupid baby!"
    melonia "Happy?!"
    anon "Thank you."
    melonia "You know, I'm beginning to feel the urge to stab you again..."
    anon "Well then, maybe I'd better leave."
    melonia a_fists @ f_yell "Yeah, maybe you should!"
    anon "Fine."
    melonia @ f_yell "Good!"
    pause
    anon @ a_wave "I'll see you later."
    melonia "Hmph!"
    hide melonia with dissolve
    show anon f_shy
    pause
    anon @ -m_talk "( Another baby... )"
    anon @ f_laugh -m_talk "( This is so exciting! )"
    hide anon with dissolve
    return True


label rump_lobby_melonia_pregnancy.abort:
    anon f_worried "No, we have plenty."
    anon "It's your decision."
    melonia "Damn right it is!"
    melonia "And I've given you more than enough children already!"
    pause
    melonia "Why don't you do us both a favor and get yourself snipped?"
    anon "Huh?"
    melonia "Then we wouldn't have to worry about this kind of thing."
    anon "Yeah, that's not happening..."
    melonia "Grr, I need a drink!"
    hide melonia with dissolve
    pause
    anon @ -m_talk "( Well, I guess that settles that... )"
    hide anon with dissolve
    return


label rump_lobby_melonia_baby_first:
    scene expression background(800, 472, 2.5) as stage
    show iwanka f_bored with None:
        flip
        xoffset -50
    show melonia a_baby f_annoyed:
        xoffset -200
    show anon behind iwanka:
        flip
        xoffset 100
    with dissolve
    iwanka "Oh, good... You're back..."
    melonia "Don't get smart, I'm not in the mood."
    if M_melonia.pregnancy.baby_gender == "boy":
        iwanka "Is that the little brother I never wanted?"
    else:
        iwanka "Is that the little sister I never wanted?"
    melonia a_baby_give "Here."
    show melonia a_idle
    show iwanka a_melonia_baby f_surprised
    show anon f_surprised
    with dissolve
    iwanka "What the-"
    iwanka "I don't want this!"
    melonia "I need a drink."
    show anon f_tired
    hide melonia
    show iwanka:
        unflip
        xoffset -600
    with dissolve
    iwanka "Seriously?!"
    pause
    iwanka "{b}Mom{/b}!"
    pause
    if M_melonia.pregnancy.baby_gender == "boy":
        anon "Here, I'll take him."
    else:
        anon "Here, I'll take her."
    show iwanka with dissolve:
        flip
        xoffset -50
    show iwanka with dissolve:
        xoffset 350
    pause
    show anon a_melonia_baby f_shy_down
    show iwanka a_idle f_normal
    with dissolve
    iwanka "She is unbelievable."
    anon "Yeah."
    iwanka f_suspicious "You still think this was a good idea?"
    show anon f_worried
    if M_melonia.pregnancy.baby_gender == "boy":
        anon "I mean, she's bound to warm up to him eventually, don't you think?"
    else:
        anon "I mean, she's bound to warm up to her eventually, don't you think?"
    iwanka f_normal @ f_laugh "Hah!"
    iwanka "I wouldn't count on it."
    show iwanka with dissolve:
        unflip
        xoffset -200
    iwanka "It's been twenty-six years and I'm still waiting for her to warm up to me..."
    if M_melonia.pregnancy.baby_gender == "boy":
        anon "Well, at least he has a father and big sister who will love and care for him, right?"
    else:
        anon "Well, at least she has a father and big sister who will love and care for her, right?"
    show iwanka f_suspicious with dissolve:
        flip
        xoffset 350
    iwanka @ -m_talk "..."
    show anon f_shy_down
    show iwanka f_smirk_down
    pause
    if M_melonia.pregnancy.baby_gender == "boy":
        iwanka "{i}*Sigh*{/i} He is really cute."
        iwanka f_excited "Have you named him yet?"
    else:
        iwanka "{i}*Sigh*{/i} She is really cute."
        iwanka f_excited "Have you named her yet?"
    anon f_normal "Not yet."
    anon "You wanna help me pick something out?"
    iwanka @ f_laugh "Oh, totally!"
    iwanka "I'm like, super good at naming things."
    anon "Yeah?"
    if M_melonia.pregnancy.baby_gender == "boy":
        iwanka "You should name him Cash."
        anon f_skeptical "Cash?!"
    else:
        iwanka "You should name her Fortune."
        anon f_skeptical "Fortune?!"
    anon f_worried @ f_disgusted "That's terrible."
    iwanka "What, no it's not!"
    iwanka "It's refined."
    anon f_unimpressed "Try again."
    show iwanka behind anon:
        unflip
        xoffset -255
    show anon:
        xoffset 0
    with {'master': dissolve}
    iwanka "Okay."
    show iwanka:
        xoffset -455
    show anon:
        xoffset -200
    with {'master': dissolve}
    if M_melonia.pregnancy.baby_gender == "boy":
        iwanka "Jermajesty."
    else:
        iwanka "Chardonnay."
    show iwanka:
        xoffset -655
    show anon:
        xoffset -400
    with {'master': dissolve}
    anon "Eugh, I thought you were good at this?"
    show iwanka:
        xoffset -855
    show anon:
        xoffset -600
    with {'master': dissolve}
    iwanka "I AM!"
    hide anon
    hide iwanka
    with {'master': dissolve}
    anon "Just awful."

    show black with slowdissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
