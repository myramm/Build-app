label ano07_mech_jiang:
    show anon with dissolve
    anon "Excuse me, sir?"
    show jiang with dissolve:
        unflip
        xoffset 0
    jiang @ -m_talk "Hmm?"
    jiang "You talkin' to me?"
    anon "Are you {b}Jiang{/b}?"
    jiang "I might be."
    jiang "Who's askin'?"
    anon @ a_wave "Hi there, I'm {b}[firstname]{/b}."
    jiang @ -m_talk "..."
    jiang "Oh kay."
    anon "{b}Josephine{/b} sent me out here to ask you something."
    jiang f_suspicious "{b}Josephine{/b}?"
    jiang "Man, I don't know nobody named {b}Josephine{/b}!"
    anon "She's the girl working the reception desk inside..."
    jiang f_smirk "Ah snap!"
    jiang "For real?"
    pause
    jiang "That girl is fiiiine!"
    anon "Y-yeah, okay."
    anon "I was hoping you could-"
    jiang "She tryin' to get with a playa?"
    anon f_confused "Huh?"
    jiang "I mean, I usually don't mess with them Asian girls..."
    jiang "... 'Cause they got no booty and they high-maintenance as fuck!"
    jiang "Know what I'm sayin'?"
    anon f_worried "Eh, not really."
    jiang "I might make an exception for your girl though, 'cause she's got them DSLs, like damn!"
    anon f_confused "DSLs?"
    jiang "Yeah, dick-sucking lips."
    anon f_surprised "!!!"
    jiang "She's got a great set on her!"
    jiang "Know what I'm sayin'?"
    anon f_worried @ -m_talk "..."
    anon "Umm, sorry but that's not why I'm here."
    jiang f_suspicious "Tsk, man... What the fuck you want then?"
    anon "I heard you're friends {b}Kim{/b}?"
    jiang f_annoyed "Pfft, hell no!"
    jiang "I ain't friends with that angry little midget!"
    jiang "Motherfucker owes me two hundred bucks!"
    anon f_normal "Oh, really?"
    jiang "Damn straight."
    jiang "Had me jailbreak his phone and install a bunch of security programs..."
    jiang "... Then he stiffed me when it came time to pay up!"
    jiang "Talkin' 'bout rewarding me once he's in charge and shit."
    anon "Yeah, that definitely sounds like him."
    anon "Listen, umm... I'm trying to get my hands on that phone of his, and it seems like you're the only person capable of making that happen."
    jiang f_smirk "Heh, yeah... Okay."
    jiang "I could probably feed him some bullshit and get you some one-on-one time with it."
    jiang "The question is... How much you payin'?"
    anon f_worried "Eh, I don't know."
    jiang f_suspicious "What do you mean, you don't know?"
    anon "I'm kinda saving up for a car right now."
    jiang f_annoyed "Yeah well, I ain't workin' for free."
    jiang "I want cash money, upfront this time."
    jiang "No more freebies!"
    jiang "{b}Jiang{/b} don't play that shit."
    jiang "Know what I'm sayin'?"
    anon "Y-yeah..."
    anon "Is there something else we can work out?"
    jiang f_suspicious "Like what?"
    anon "I dunno, something I can assist you with?"
    jiang a_up f_eyeroll "Whoa, hold up."
    jiang "I ain't into no gay shit, now..."
    anon f_surprised "!!!"
    show jiang f_annoyed a_idle with dissolve
    anon f_worried "That's not-"
    anon "I wasn't implying that!"
    jiang f_suspicious "Uh huh."
    anon "Is there like, work you need done or help with something?"
    jiang "Do I look like a man who can't handle his own work?"
    anon "No."
    jiang f_normal @ f_thinking "I mean, I guess you could help me out with {b}my lucky tool bag{/b}..."
    anon "Your lucky tool bag?"
    jiang "Yeah, I misplaced it somewhere and haven't had time to look for it."
    anon f_normal "Oh?"
    jiang "If you can find it and bring it here... I guess I'll help you out."
    anon @ f_laugh "I can definitely do that."
    anon "Any idea where I should start the search?"
    jiang @ f_thinking "It's probably layin' around at one of my side jobs."
    anon "Side jobs?"
    jiang "Yeah, I do repairs on the side."
    jiang "You know, pretty much anything that pays."
    anon "Go on."
    jiang "Over the weekend, I was doing repairs on the ice machine {b}at that big apartment building{/b} in town."
    anon "Okay."
    jiang f_thinking "Then I fixed a broken toilet {b}at the mall{/b}..."
    jiang "... And there's the water filtration unit {b}at the public pool{/b}."
    pause
    jiang "Damn thing is always breakin' down."
    show jiang f_normal
    anon "Alright, so {b}the big apartment building{/b}, {b}the mall bathroom{/b}, and {b}the public pool{/b}?"
    anon "I'll take a look."
    jiang f_suspicious "Be careful with my {b}lucky tool bag{/b}, will ya?"
    jiang f_annoyed "You break anything and the deal is off."
    jiang "You know what I'm sayin'?"
    anon "Yeah, I'll be careful."
    anon "Just have that phone ready when I get back."
    jiang f_normal "Yeah, yeah..."
    hide anon with dissolve
    return


label ano07_find_jiang:
    show anon with dissolve
    anon "Any luck getting {b}Kim{/b}'s phone?"
    show jiang with dissolve:
        unflip
        xoffset 0
    jiang "Maybe."
    jiang "Any luck finding my {b}tool bag{/b}?"
    anon f_worried "Not yet."
    jiang @ f_suspicious "Well, you ain't gettin' the phone without it."
    jiang "You know what I'm sayin'?"
    anon "{i}*Sigh*{/i} Yeah, I get it."
    anon "Where do you think you left it again?"
    jiang f_annoyed "Man, I don't know!"
    jiang "Over the weekend, I was doing repairs on the ice machine {b}at that big apartment building{/b} in town."
    anon "Okay."
    jiang f_thinking "Then I fixed a broken toilet {b}at the mall{/b}..."
    jiang "... And there's the water filtration unit {b}at the public pool{/b}."
    pause
    jiang f_annoyed "Damn thing is always breakin' down."
    anon f_normal "Alright, so {b}the big apartment building{/b}, {b}the mall bathroom{/b}, and {b}the public pool{/b}?"
    anon "I'll check it out."
    hide anon with dissolve
    return


label ano07_give_jiang:
    show anon with dissolve
    anon "Hey, {b}Jiang{/b}!"
    show anon f_shy_down a_backpack
    show jiang:
        unflip
        xoffset 0
    with dissolve
    anon "Look what I got!"
    show anon a_toolbag f_normal with dissolve
    pause
    jiang "Yo, you found it!"
    show anon a_idle
    show jiang a_toolbag f_happy_down
    with dissolve
    pause
    jiang f_normal "Hmm, everything looks good."
    anon "Were you able to get {b}Kim{/b}'s phone?"
    jiang "Psh, you know it!"
    show jiang a_phone_kim with dissolve
    jiang "Told him there was a new version of that security software and he handed it right over."
    show anon a_phone_kim
    show jiang a_sides
    with dissolve
    anon "Nice!"
    show anon f_shy_down
    pause
    jiang "What do you want with it anyways?"
    anon f_normal @ -m_talk "Hmm?"
    anon "Oh, it's just some pics he stole from {b}Josephine{/b} that I promised to delete for her."
    jiang f_suspicious "What kinda pics?"
    anon f_shy_down "No idea."
    anon "She just said they were private."
    jiang f_normal "Oh."
    pause
    jiang f_suspicious "Wait a second..."
    jiang f_smirk "Are we talking naked pics?"
    anon f_worried "I don't know."
    anon "I promised her I wouldn't look."
    jiang @ f_suspicious "Are you fuckin' crazy?!"
    jiang "You got naked pics of a beautiful woman in your hand right now and you ain't even gonna look?!"
    anon @ -m_talk "..."
    jiang "C'mon man, let's peep that shit!"
    show anon f_thinking

    menu:
        "Nah, I promised not to look.":
            anon f_worried "Sorry."
            jiang f_annoyed @ f_eyeroll a_head "Aww, seriously man..."
            anon "It's not like she sent them to me."
            anon "They were stolen from her."
            jiang "So?"
            anon "So, what's the matter with you?"
            jiang "Pfft, nothin' is the matter with me!"
            jiang f_suspicious "I'm just a man who loves boobs, that's all."
            anon "It wouldn't be right."
            jiang f_normal "If lovin' boobs is wrong, then I don't want to be right!"
        "One peek wouldn't hurt.":

            $ M_josie.set('peeked', True)
            anon f_flirt "I suppose one peek wouldn't hurt."
            jiang "Nah, it wouldn't hurt one little bit!"
            jiang "Know what I'm sayin'?"
            hide anon
            hide jiang
            show closeup_josephine_nude as phone
            with dissolve
            anon "!!!"
            anon "I guess they were naked pics..."
            jiang "Hell to the yeah, man!"
            jiang "Those are small but nice."
            pause
            jiang "Is there more?"
            anon "Yeah, I think so."
            show closeup_josephine_nude2 as phone with dissolve
            anon "!!!"
            jiang "Oh snap!"
            jiang "I see some pussy peekin'!"
            anon "I wonder what she took these for?"
            jiang "Who cares?"
            jiang "This is awesome!"
            pause
            anon "I think that's enough."
            pause
            hide phone
            show anon a_phone_kim f_worried
            show jiang f_annoyed
            with dissolve
            jiang "Aww, man... C'mon!"
            anon "No, it doesn't feel right; looking at these."
            jiang "If lookin' at naked women is wrong, then I don't want to be right!"

    show anon a_idle
    show jiang a_phone_kim
    with dissolve
    anon "Thanks again, for your help today."
    jiang a_sides f_annoyed @ f_eyeroll "Yeah, whatever man..."
    show jiang with dissolve:
        flip
        xoffset 500
    jiang "Fuckin' crazy white boy, comin' up in here and deletin' naked pics."
    hide jiang with dissolve
    jiang "I dunno why I keep gettin' involved with these crazy motherfuckers..."
    pause
    anon @ -m_talk "( Well, that settles that. )"
    anon @ -m_talk "( I should check in with {b}Josephine{/b} and tell her she can stop freaking out now. )"
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
