label iwa01_init_iwanka:
    show anon f_normal with dissolve
    iwanka "{b}[firstname]{/b}?"
    anon "Hey."
    iwanka "Oh em gee, how did you get passed the guards?"
    anon @ f_laugh "Your plan worked!"
    iwanka f_concerned "Plan?"
    anon "Yeah, you remember?"
    anon f_shy "The other night... You suggested I tell them I'm your new assistant."
    iwanka "I did?"
    anon f_worried "You don't remember?"
    iwanka f_normal @ f_laugh "Heh, I don't remember anything from the other night if I'm being honest..."
    anon "Nothing at all?"
    iwanka f_thinking "Hmm, I remember arriving... And that weird lady shoving a popsicle in my hand..."
    pause
    iwanka f_annoyed "... Then she called my dress whorish."
    show anon f_hurt
    pause .5
    anon f_worried "Yeah."
    show iwanka f_thinking
    pause
    iwanka f_suspicious a_hip @ f_laugh a_finger "Oh, I remember your friend made some really yummy Screwdrivers!"
    iwanka "What was his name again?"
    anon f_unimpressed "{b}Erik{/b}."
    iwanka f_disgusted "No, that wasn't it."
    show anon f_worried
    pause
    iwanka f_smirk "Anyways, the drinks were good and there was dancing..."
    iwanka "... I think."
    anon f_worried_low "Yes, there was dancing."
    iwanka "I remember your little friend was talking about a bunch of stuff I didn't understand..."
    show iwanka f_thinking
    show anon f_worried
    pause
    iwanka "... And something about..."
    pause
    iwanka f_suspicious "... An octopus?"
    anon f_surprised a_sides @ a_surprised_up "Uhh?"
    iwanka @ a_crossed "I can't remember."
    iwanka f_smirk "It's all murky."
    anon f_shy a_idle @ a_point "Well, you did drink a lot."
    iwanka f_suspicious "Did your friend have a pet octopus or something?"
    anon f_worried "N-no."
    iwanka f_concerned "Hmm, maybe it was just a dream..."
    iwanka "... It's like, stuck in my head, for some reason."
    anon "Huh."
    show anon f_surprised_teeth
    pause
    anon f_worried "Umm, weird."
    iwanka f_normal @ f_laugh "Right?!"
    pause
    iwanka "So what are you doing here?"
    anon f_normal "Well, umm... You know, we had so much fun the other night..."
    anon f_shy "... And you wanted to hang out more, so..."
    iwanka "Aren't you worried about getting caught?"
    iwanka @ f_laugh "The guards totally tase people in the nuts, you know?"
    anon f_worried "Ehh, I thought you were joking about that..."
    iwanka f_suspicious "Why would I joke about that?"
    anon "I don't know."
    iwanka f_normal @ f_eyeroll "It happens like, all the time!"
    anon f_surprised "You're serious?"
    iwanka "Oh, totally."
    show anon f_hurt a_cover_boner with dissolve
    iwanka f_smirk "They say it's like, the most effective deterrent or something..."
    show anon f_worried
    iwanka "... I think they're just bored."
    anon "That's really messed up!"
    iwanka f_normal @ f_laugh "Hehe, yeah."
    iwanka "It must work though, because nobody has ever been caught trying to break in twice."
    anon a_badge "{i}*Gulp*{/i} I'm probably safe with this {b}staff badge{/b} though, right?"
    iwanka f_surprised "Whoa, where did you get that?!"
    anon "{b}Melonia{/b} gave it to me."
    iwanka f_suspicious "My mother gave you a {b}staff badge{/b}?"
    anon f_normal a_idle "She thinks I'm the new pool boy."
    iwanka "For real?"
    anon "Yeah."
    iwanka "Are you two fucking?"

    if M_melonia.finished_state(S_mel05_init):
        anon f_surprised @ f_shy "Ehh."
        pause
        anon f_worried "I dunno, maybe..."
        show iwanka a_crossed f_smirk with dissolve
        pause
        anon @ a_fingers_small "... Just a little bit."
        iwanka @ f_laugh "Oh em gee, that's hilarious!"
        iwanka a_hip "How was it?"
        anon f_confused "Huh?"
        iwanka "I bet it was like doing push-ups over an open manhole!"
        anon f_shy "Wait, so... You're not mad?"
        iwanka @ f_eyeroll "Please, {b}[firstname]{/b}."
        iwanka "If I got upset every time my parents fucked the help, I'd never get anything accomplished."
        anon f_surprised @ -m_talk "..."
        iwanka "So not only did you trick her into giving you free access to the mansion..."
        show anon f_shy
        iwanka "... But she's also giving you free access to her vagina?"
        anon "Actually, she's paying me."
        iwanka f_normal @ f_laugh "Pfft, hahahaha!"
        show anon f_normal
        iwanka "That's so sad!"
        anon @ -m_talk "..."
        iwanka "You just totally made my day!"
    else:

        anon f_surprised "N-no!"
        show anon f_shy m_talk
        show anon of_blush with {'master': dissolve}
        anon -m_talk "Of course not!"
        iwanka a_crossed f_annoyed "{b}[firstname]{/b}, tell me the truth!"
        anon f_worried a_up -of_blush "{b}Iwanka{/b}, I swear!"
        anon "I'm not doing anything with your mother."
        show anon a_idle with dissolve
        pause
        iwanka f_suspicious "For real?"
        anon "I'm dead serious."
        iwanka f_concerned "Wow, she's slipping in her old age."
        anon f_confused "Wait, so... You just assumed I would?"
        iwanka @ f_eyeroll "Umm, duh."
        iwanka f_smirk "Tell me this..."
        iwanka "... Has she picked a name for you yet?"
        show anon f_worried_low
        pause
        anon "... {b}Hector{/b}."
        iwanka @ f_laugh "Pfft, haha!"
        iwanka a_idle "You are definitely in her crosshairs."
        anon f_worried "I am?"
        iwanka "Just remember to bag it."
        iwanka "My mother's vagina has seen more dicks than a hardware store urinal."
        anon f_shock "!!!"
        iwanka "I'm pretty sure her spit would be accepted at one of those sperm donation clinics."
        anon f_worried "I'm not really sure how to respond to that..."
        iwanka f_normal @ f_laugh "Hehe!"

    anon "So, have any other boys snuck into your father's estate to see you before?"
    iwanka @ f_surprised "Oh, hell no!"
    iwanka "They've all been too terrified of my father."
    anon f_normal @ f_laugh "Does that mean you're impressed?"
    iwanka f_smirk "Mmm, maybe..."
    anon "Impressed enough to give me a tour?"
    iwanka f_suspicious "What, like, of the mansion?"
    anon "Yeah."
    iwanka "That's a weird thing to ask for."
    anon "Is it?"
    anon "I've just never been inside a house this big before."
    iwanka f_bored "Ugh, can't we do something else, {b}[firstname]{/b}?"
    iwanka f_smirk @ f_laugh "You know, something fun!"
    anon @ f_confused "Umm, sure... I guess."
    anon "What do you have in mind?"
    iwanka "I dunno."
    iwanka @ f_laugh "Let's sneak out and get our party on again!"
    anon f_skeptical "You wanna throw another party at {b}Erik{/b}'s house?"
    iwanka @ f_concerned "Uhh, not exactly..."
    show anon f_worried
    iwanka f_bored "Look, no offense, {b}[firstname]{/b}... But your friend's house was kinda lame..."
    anon "Oh."
    iwanka f_normal "So, I was thinking I should probably choose the venue this time."
    anon "Y-yeah, okay."
    anon f_normal "Just name the place and I'll meet you there."
    iwanka f_concerned "Well, there's a bit of a catch..."
    anon @ f_confused "Hmm?"
    iwanka @ f_eyeroll "So, my dad was like, all kinds of pissed off about me sneaking out the other night..."
    iwanka f_annoyed "... And he kinda put me under house arrest."
    anon f_worried "You're serious?"
    iwanka @ -m_talk "Mhmm."
    anon f_confused "Didn't you say that you're twenty-seven years old?"
    iwanka f_suspicious "Where are you going with this, {b}[firstname]{/b}?"
    anon "Don't you think that's a little old to be getting grounded by your daddy?"
    iwanka f_annoyed @ f_eyeroll "Umm, duh."
    iwanka "Do you wanna explain that to him?!"
    anon f_sad_down "{i}*Sigh*{/i} No, I really don't."
    iwanka "Yeah, I didn't think so!"
    iwanka f_concerned "The guards aren't just gonna let me walk out this time..."
    show anon f_worried
    iwanka f_smirk "... You'll have to sneak me out."
    anon f_surprised a_point_self "Me?!"
    anon a_up "I can't do that!"
    show anon a_idle with dissolve
    iwanka f_suspicious "Why not?"
    iwanka "You snuck in here, didn't you?"
    anon f_shy "Y-yeah, but-"
    iwanka f_smirk "So just do it again, but in reverse!"
    anon f_hurt a_cover_boner @ f_worried_low -m_talk "..."
    pause
    iwanka f_concerned "{b}[firstname]{/b}?"
    anon f_worried "Yeah, sorry... I'm just thinking about how much I don't want to get tased in my nuts..."
    iwanka f_smirk @ f_eyeroll "Oh, c'mon... It'll be worth it!"
    iwanka "Do this and I'll give you whatever you want!"
    anon f_shy a_idle "Anything?"
    iwanka @ -m_talk "Mhmm."
    anon f_normal "A tour of the entire mansion?"
    iwanka f_annoyed "That's what you-"
    show iwanka f_bored
    pause
    iwanka a_crossed f_eyeroll "Yeah, sure."
    iwanka "Whatever."
    show iwanka f_normal
    anon @ f_laugh a_cheering "Alright, I'll figure something out."
    iwanka @ f_laugh "Excellent!"
    iwanka "Just come and find me when you have a plan."

    scene expression background(640, 240, 9., l=L_rump_lobby) as stage with fade
    show anon f_worried_low with dissolve:
        flip
        xoffset -100
    anon @ -m_talk "( It's never simple, is it? )"
    anon f_thinking @ a_thinking -m_talk "( How am I going to sneak {b}Iwanka{/b} past the guards? )"
    pause
    anon @ -m_talk "( What we need is a good {b}disguise{/b}. )"
    anon f_normal @ -m_talk "( There's probably something {b}here in the estate{/b} that'll work... )"
    anon @ -m_talk "( {b}I should look around{/b}. )"
    hide anon with dissolve
    return


label iwa01_find_iwanka:
    show anon with dissolve
    iwanka "Did you find a way to sneak me out yet?"
    anon f_worried "No, I'm still working on it."
    iwanka f_disgusted "Ugh, seriously?"
    anon @ a_up "Try and relax, okay?"
    anon f_normal "I'll find something, I promise."
    iwanka f_concerned a_crossed "I'm so bored, you have no idea!"

    scene expression background(640, 240, 9., l=L_rump_lobby) as stage with fade
    show anon f_thinking a_thinking with dissolve:
        flip
        xoffset -100
    anon @ -m_talk "( Hmm. )"
    anon @ -m_talk "( How am I going to sneak {b}Iwanka{/b} past the guards? )"
    pause
    anon @ -m_talk "( What we need is a good {b}disguise{/b}. )"
    anon f_normal @ -m_talk "( There's probably something {b}here in the estate{/b} that'll work... )"
    anon @ -m_talk "( {b}I should look around{/b}. )"
    hide anon with dissolve
    return


label iwa01_give_iwanka:
    show anon with dissolve
    iwanka "Did you find a way to sneak me out yet?"
    anon "Yeah, I think I've found a way for you to walk right past the guards."
    iwanka f_excited "Heh, really?"
    iwanka "How am I gonna do that?"
    show anon a_backpack f_looking_down with dissolve
    pause
    anon f_laugh a_maid_outfit "By wearing this!"
    show anon f_normal a_idle
    show iwanka a_maid_uniform f_suspicious_down
    with dissolve
    pause
    iwanka f_suspicious "You want me to dress up as a maid?"
    anon "Yeah."
    show iwanka f_suspicious_down
    pause
    anon "What?"
    iwanka "I dunno, it's just... Kinda..."
    pause
    iwanka f_disgusted "... Eww."
    anon f_unimpressed "Do you want out of this house or not?"
    iwanka f_concerned "Yes."
    pause
    iwanka "But I'm just saying, it would be nice if you could find something a little less-"
    anon "{b}Iwanka{/b}, shut up and put the uniform on!"
    iwanka @ f_surprised "!!!"
    iwanka "Alright, alright... Sheesh!"
    iwanka "You don't have to get all grumpy."
    show iwanka a_maid_uniform_smell f_disgusted with dissolve
    show anon f_worried
    pause
    iwanka a_maid_uniform "Ugh, what is that smell?"
    anon "I dunno."
    anon @ f_confused "Lemon Pledge?"
    iwanka "It's disgusting!"

    label iwa01_give_iwanka.retry:
    anon f_worried "Are we going or not?"

    if game.timer.is_evening():
        jump iwa01_give_iwanka.evening

    iwanka f_normal @ f_eyeroll "Well, not right this instant... Obviously."
    anon f_surprised "Obviously?"
    iwanka f_content_closed a_idle @ a_finger "Good parties happen after the sun goes down, duh."
    anon f_sad_down "..."
    show anon f_worried
    iwanka f_normal "Come back this evening and we'll go, alright?"
    anon "{i}*Sigh*{/i} Yeah, okay."
    anon a_sides @ a_wave "I'll see you tonight."
    hide anon with dissolve
    return False


label iwa01_give_iwanka.evening:
    iwanka f_annoyed "Yeah, yeah."
    show anon f_surprised
    show iwanka b_dressed_back_unzip1 with dissolve
    pause
    show iwanka b_dressed_back_unzip2 with dissolve
    show anon f_surprised_low
    iwanka "I can't believe you're making me wear this ugly thing..."
    show iwanka b_dressed_back_unzip3 with dissolve
    pause
    show iwanka b_dressed_back_unzip4 with dissolve
    show anon f_flirt_low
    anon "W-wait, why don't you just put it on over your clothes?"
    show iwanka b_dressed_back_unzip5 with dissolve
    iwanka "Umm, I'm not getting this stink all over my nice clothes!"
    anon f_surprised @ f_unimpressed a_frustrated "It smells fine, {b}Iwanka{/b}!"
    show iwanka b_naked a_maid_uniform f_disgusted with dissolve
    iwanka "That's your opinion!"
    show anon f_flirt_low
    iwanka @ f_eyeroll "Besides, why are you complaining?"
    anon @ f_flirt "{i}*Gulp*{/i} Good point."
    show iwanka f_suspicious_down
    pause
    iwanka @ -m_talk "..."
    show iwanka b_naked_dressing_maid with dissolve
    pause
    iwanka "Eww.{w} Eww.{w} Eww."
    show iwanka b_maid_scarfless f_disgusted a_out_gross with dissolve
    show anon f_normal
    iwanka "This is so gross!"
    show iwanka a_hips with dissolve
    anon f_worried @ f_eyeroll "Yeah, whatever..."
    anon "Do you have something to hide your hair?"
    iwanka f_surprised_up @ -m_talk "Hmm?"
    anon f_normal "Like a scarf or something?"
    iwanka f_normal @ f_laugh "Oh, right!"
    hide iwanka with dissolve
    pause
    anon "You might wanna wear some sunglasses or something too."
    iwanka "At night?"
    iwanka "Umm, that's like a major fashion faux pas!"
    anon f_worried "Yeah, well... So is getting tased in the nuts!"
    iwanka "What?"
    iwanka "Do you even know what a faux pas is?"
    anon "{b}Iwanka{/b}, just please find something..."
    iwanka "Ugh, fine!"
    anon f_looking_down a_phone @ f_eyeroll a_facepalm "Jesus."
    pause
    pause
    show iwanka b_maid f_annoyed o_glasses with dissolve
    iwanka "There."
    show anon f_normal a_idle with dissolve
    iwanka "Happy?"
    anon f_worried "I'll be happy when my nuts are safely past the guards."
    anon "C'mon, let's get this over with."
    hide anon with dissolve
    iwanka @ f_eyeroll a_dust "Oh, don't be such a pussy!"
    hide iwanka with dissolve
    return True


label iwa01_wait_iwanka:
    show anon with dissolve

    jump iwa01_give_iwanka.retry
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
