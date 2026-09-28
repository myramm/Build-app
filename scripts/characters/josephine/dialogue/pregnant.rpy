label josie_button_pregnant:
    show anon with dissolve
    anon "Hey, {b}Josephine{/b}."

    if M_josie.pregnancy.stage <= 2:
        josephine @ -m_talk "Hmm?"
        josephine f_normal "Oh, hey!"
        josephine "I'm glad you're here!"
        anon "Yeah?"
        josephine "You wanna watch some Gootube videos with me?"
        show josephine f_normal_down
    else:
        josephine "Oh my god, {b}[firstname]{/b}!"
        show anon f_worried
        josephine "I am freaking out here!"
        anon "What's the matter?"
        josephine @ f_angry_closed "You put a giant fucking baby inside me, that's what's the matter!"

    menu josie_button_pregnant.choice:

        "Calm down..." if M_josie.pregnancy.stage > 2:
            jump josie_button_pregnant.calm

        "What are you watching?" if M_josie.pregnancy.stage <= 2:
            if M_josie.pregnancy.stage == 1:
                jump josie_button_pregnant.gootube
            else:
                jump josie_button_pregnant.feeding

        "The baby" if M_josie.pregnancy.stage <= 2:
            jump josie_button_pregnant.baby
        "Your dad?":

            if M_josie.pregnancy.stage == 1:
                jump josie_button_pregnant.notice
            elif M_josie.pregnancy.stage == 2:
                jump josie_button_pregnant.clueless
            else:
                jump josie_button_pregnant.grandpa

        "I can't stay." if M_josie.pregnancy.stage <= 2:
            pass

        "I have to go." if M_josie.pregnancy.stage > 2:
            pass

    if M_josie.pregnancy.stage <= 2:
        anon f_normal @ f_worried "I can't stay."
        anon "I just wanted to see how you were doing."
        josephine f_normal_down @ f_bored "Just, bored..."
        josephine "... As usual."
        anon "I'll see you later, okay?"
        josephine @ -m_talk "Mhmm."
    else:
        anon f_worried "Are you going to be okay?"
        josephine f_concerned "Ugh, yeah..."
        josephine "I wish you could stay though."
        anon "I know."
        josephine "For some reason, talking with you makes me feel better."
        anon f_normal "I'll come back soon, okay?"
        josephine "Alright."

    hide anon with dissolve
    return


label josie_button_pregnant.baby:
    anon f_worried "Are you really sure you wanna go through with this?"
    josephine f_concerned "What do you mean?"
    anon "I mean, children are a big responsibility and it's not something you can just ignore when you feel like it..."
    josephine f_bored "Umm, duh."
    josephine "I'm not stupid, {b}[firstname]{/b}."
    anon "I know that, {b}Josephine{/b}... I'm just saying that-"
    josephine f_sexy "Dude, you need to chill out."
    josephine "We're talking about a little kid with my DNA... It's going to be the coolest baby ever!"
    anon @ -m_talk "..."
    anon "{i}*Sigh*{/i} Well, at least you're thinking positive..."
    show josephine f_normal_down
    jump josie_button_pregnant.choice


label josie_button_pregnant.calm:
    anon f_worried "Everything is going to be fine, I promise."
    josephine f_bored "Yeah, real easy for you to say!"
    josephine "You're not the one who has to squeeze the damn thing out of your vagina!"
    anon "Women give birth everyday, your body knows exactly what to do..."
    josephine f_angry "No, fuck that!"
    josephine "I don't wanna!"
    anon "Ehh."
    josephine "It's just gonna have to stay in there."
    anon "{b}Josephine{/b}..."
    josephine "Why the hell did I let you talk me into this?"
    anon f_surprised "ME?!"
    anon "I'm the-"
    anon f_shock "That's-"
    anon f_hurt a_sides @ -m_talk "{i}*Sigh*{/i}"
    anon a_idle f_worried "Look at me."
    josephine f_concerned @ -m_talk "Hmm?"
    pause
    anon "Just breathe, okay?"
    josephine @ -m_talk "Mhmm."
    anon "You've watched like a hundred videos on childbirthing these past few weeks..."
    josephine @ -m_talk "..."
    anon "... I know that because you forced me watch most of them with you, remember?"
    josephine f_sexy @ f_laugh "Heh, yeah."
    show anon f_normal
    josephine "It was so funny when that one video made you throw up!"
    anon "The lady sharted diarrhea everywhere!"
    josephine @ f_laugh "Hahahaah!"
    anon "It was on the baby!"
    josephine "{i}*Snort*{/i}"
    pause
    anon "Seriously, {b}Josephine{/b}... You know everything about this stuff."
    anon "You've got this."
    pause
    josephine "Thanks, {b}[firstname]{/b}."
    jump josie_button_pregnant.choice


label josie_button_pregnant.clueless:
    anon f_worried "He still doesn't know?"
    josephine f_normal_down "Nope."
    josephine "He's absolutley clueless, just like I expected..."
    anon f_confused "How can he not know?"
    anon f_normal @ f_laugh "You're clearly showing."
    josephine f_bored "Pfft, just in my belly a bit..."
    josephine f_angry_down "My tits haven't grown at all."
    show anon f_worried
    josephine "Which is bullshit!"
    josephine f_angry "That's supposed to be one of the best parts about getting pregnant!"
    anon "Your tits are fine..."
    josephine f_normal_down @ f_eyeroll "Yeah, right."
    jump josie_button_pregnant.choice


label josie_button_pregnant.feeding:
    anon f_normal "What are you watching?"
    josephine f_normal_down "A video on breastfeeding."
    josephine "Care to join me?"
    anon f_worried "Ehh..."
    josephine "A lot of these videos suggest frequently scrubbing your nipples with a brush or loofah during pregnancy to toughen them up."
    anon "Really?"
    josephine @ -m_talk "Mhmm."
    pause
    anon @ f_disgusted "That sounds really unpleasant."
    josephine f_sexy "Yeah, I'm not doing that."
    josephine "They also say that I should have my partner rub lanolin oil on my breasts after each feeding session."
    anon f_normal "Oh?"
    josephine f_normal_down "Yeah, I thought you'd like that..."
    anon @ f_laugh "Hehe."
    jump josie_button_pregnant.choice


label josie_button_pregnant.gootube:
    anon f_normal "What are you watching?"
    josephine f_normal "Gootube."
    anon f_confused @ -m_talk "..."
    josephine f_bored "Seriously, do you live under a rock or something?"
    anon f_worried @ f_sad_down "I dunno..."
    anon "What is Gootube?"
    josephine f_normal "It's a video-sharing platform on the internet."
    josephine "People basically upload whatever they want and it's free to watch."
    anon @ f_confused "Like porn?"
    josephine @ f_eyeroll "No, not porn..."
    pause
    josephine f_surprised "Err, well... I mean, they {i}DO{/i} have porn."
    josephine f_sexy "Quite a lot actually."
    anon f_normal "I knew it."
    josephine f_surprised "But I'm not watching that!"
    josephine f_normal a_phone_show_left "This is what to expect when you're expecting videos."
    anon f_surprised "Baby stuff?"
    josephine f_sexy "Yeah, it's been really interesting so far."
    anon f_worried "Well, I'm glad to see you're finally taking this at least a little bit seriously..."
    josephine f_normal_down a_phone "Uh huh."
    pause
    josephine f_sexy "Did you know that like ninety percent of women poop themselves during delivery?"
    show anon f_disgusted
    pause
    anon "Welp, that didn't last long."
    josephine f_normal_down @ f_laugh "Hahahaah!"
    show anon f_worried
    jump josie_button_pregnant.choice


label josie_button_pregnant.grandpa:
    anon f_worried "Let's think about something else, okay?"
    josephine f_concerned "Yeah, okay."
    anon "Surely your father has figured out you're pregnant by now, right?"
    josephine "He has..."
    pause
    josephine f_bored "... And don't call me {b}Shirley{/b}."
    anon f_normal @ f_laugh "Heh, very funny."
    josephine f_sexy @ f_laugh "Hehe!"
    anon f_worried "What did he say?"
    josephine "He was annoyed that I didn't tell him and he tried to yell at me..."
    pause
    josephine @ f_eyeroll "... But it wasn't very convincing."
    josephine "He's really excited about being a grandpa."
    anon f_normal "Well, that's good news!"
    josephine "Yeah, I guess."
    jump josie_button_pregnant.choice


label josie_button_pregnant.notice:
    anon f_worried "Don't you think we should tell your dad you're pregnant?"
    josephine f_angry "No, we're not telling him yet!"
    josephine f_sexy "I want him to notice on his own."
    anon f_confused "That's-"
    pause
    anon "Why?"
    josephine "Because it'll be funnier that way!"
    anon f_worried @ -m_talk "..."
    anon "Won't he be mad?"
    anon "I don't want him to hate me or something..."
    josephine @ f_eyeroll "My dad isn't going to hate you."
    josephine "He doesn't have it in him."
    anon "He might, when he finds out I got you pregnant."
    josephine "Dude, you've been fucking his daughter on the desk in his office..."
    anon f_surprised "!!!"
    anon f_worried @ f_surprised_left "Shhh, not so loud!"
    josephine f_concerned "... He literally walked in on you balls deep inside me."
    pause
    josephine f_sexy "If he was capable of hating someone, you'd be number one on his list."
    anon f_surprised_teeth @ -m_talk "..."
    josephine "Trust me, you're good."
    show anon f_worried
    show josephine f_normal_down
    jump josie_button_pregnant.choice
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
