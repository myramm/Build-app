label ano25_init_pizzeria_interior:
    call tony_button_stage

    show tony a_idle f_normal
    show liu_overlay_o_pizza_rolls:
        xoffset -100
    show liu a_mouth_cover f_eating_chew:
        xoffset -100
    liu @ -m_talk "Om nom!"
    liu "Oh my god, I would get so fat if I worked here."
    tony m_talk "Heh, there ain't nothin' wrong with that... little skin and bones thing like you..."
    show liu a_pizza_roll with {'master': dissolve}
    tony -m_talk "... You could do with more meat on ya."
    liu @ f_eating a_pizza_roll_eat "Nom nom."
    liu @ -m_talk "Mmm."
    liu "What are these called again?"
    tony "Pizza rolls."
    liu a_pizza_roll "They don't look like the pizza rolls they sell in the store..."
    show liu a_pizza_roll_eat f_eating
    show tony f_question a_frustrated
    with {'master': dissolve}
    tony "Bah, you're talkin' about those little bite sized pizza pockets in the frozen section!"
    show liu a_mouth_cover f_eating_chew
    show tony a_idle
    with {'master': dissolve}
    liu "Yeah, my husband loves those."
    tony "He might as well be eatin' garbage!"
    tony "I wouldn't feed those things to a dog."
    liu f_happy @ f_laugh "You're right, these are way better!"
    show tony f_normal
    show anon behind liu:
        xoffset 150
        xzoom -1
    show liu a_pizza_roll
    with {'master': dissolve}
    tony "They're real easy to make too."
    show liu a_pizza_roll_eat f_eating with dissolve
    liu "Om nom!"
    show liu a_mouth_cover f_eating_chew
    show anon f_worried
    with dissolve
    tony "I just roll out the dough into a rectangle and slap some sliced mozzarella on it."
    tony m_talk "Then slather that bad boy with some nice marinara and throw in the toppings of your choice..."
    show liu a_idle f_happy with {'master': dissolve}
    tony -m_talk "... In this case, pepperoni, onion, green pepper, and mushroom."
    show anon f_confused
    tony "Cover it all in mozzarella before rollin' it up tight and tossin' it in the oven."
    tony "It takes about ten minutes to get it nice and crispy."
    tony "Then ya just cut it into one-inch slices and voilà!"
    show anon f_normal
    show tony a_kiss_fingers f_kiss
    show liu a_pizza_roll
    with dissolve
    pause
    show liu a_pizza_roll_eat f_eating
    show tony a_idle f_normal
    with dissolve
    liu "Nom nom."
    show liu a_idle f_eating_chew with dissolve
    tony "You got yerself a REAL pizza roll."
    liu a_mouth_cover "Mmm, they're so good!"
    tony "Yeah, I'm still tryin' to talk the missus into puttin' 'em on the menu."
    liu "You should..."
    liu "... I can't stop eating them!"
    tony f_smirk "Heh, you have as many as you want darlin'."
    liu f_worried a_cover "N-no, I'd better stop."
    liu "I don't want to look like a pig."
    tony @ f_laugh "Ahh, forghedaboudit!"
    tony "There ain't nothin' sexier than a beautiful woman with a healthy appetite."
    liu a_idle f_confused "Really?"
    tony "Mhmm."
    tony @ f_smirk_wink "You're sure makin' my dough rise... if you know what I mean?"
    show anon f_confused
    liu @ f_laugh a_mouth_cover "Heh, oh my!"
    pause
    liu "Well, maybe just one more..."
    show liu a_pizza_roll with dissolve
    tony @ f_laugh "Attagirl!"
    show liu a_pizza_roll_eat f_eating with dissolve
    liu "Om nom!"
    show liu a_idle f_eating_chew with dissolve
    pause
    show anon f_surprised
    show tony f_surprised
    liu @ f_burp m_talk "{i}*Buuuurp*{/i}" with hpunch
    show anon f_laugh
    show tony f_laugh
    liu a_mouth_cover f_nervous -m_talk "Oh, goodness!"
    tony f_laugh "Heh!"
    show anon f_normal
    show tony f_smirk
    show liu f_normal o_blush a_idle
    with {'master': dissolve}
    liu "That was embarrassing!"
    tony "Hey, I'm a chef."
    tony "Burpin' is a compliment!"
    tony "You want some of this, champ?"
    show liu o_empty f_confused with {'master': dissolve}
    liu @ -m_talk "Hmm?"
    anon @ f_laugh "Nah, I think I'm good."
    show liu o_blush f_surprised with {'master': dissolve}:
        xoffset 300
        xzoom -1
    tony "You sure?"
    tony "They're fresh outta the oven."
    anon "Thanks though, {b}Tony{/b}."
    liu f_worried "I uhh..."
    liu "... I don't normally eat like this."
    liu f_ashamed_down "{b}Kim{/b} never let me-"
    anon "Heh, don't worry about it {b}Liu{/b}."
    anon "I'm happy to see you enjoying yourself."
    show liu f_nervous
    pause
    tony "Your girl here was just tellin' me about your little spat with her soon to be ex-husband."
    anon f_shy a_behind_head "Oh, that... was nothing, really..."
    tony f_question "Oh?"
    tony "'Cause it didn't sound like nothin'."
    show tony a_sides f_smirk with dissolve:
        xoffset -550
        xzoom 1
    hide tony with dissolve
    pause .4
    show liu f_nervous_back -o_blush
    show tony a_fists:
        xoffset -100
        xzoom -1
    with {'master': dissolve}
    tony "You gave that scumbag the ole' one-two, didn't ya?"
    tony "Eh? Eh?"
    show liu f_nervous
    anon a_idle @ f_laugh "Heh, it wasn't much of a fight."
    show liu f_nervous_back
    tony f_normal a_idle "Glass jaw?"
    show liu f_nervous
    anon "Ehh, no... he was just all talk."
    show liu f_nervous_back
    tony f_smirk "Ah, so he backed down, eh?"
    show liu f_nervous
    anon "Pretty much."
    show liu f_nervous_back
    tony "Well, it still sounds like you did good."
    liu "He did."
    liu "It was very brave."
    show liu f_nervous
    show anon f_shy_low of_blush
    with dissolve
    anon "Aww, c'mon you guys..."
    tony "Heh, look at Mr. tough guy blushin'!"
    liu @ f_laugh "Hehe!"
    show anon f_shy
    tony @ f_smirk_wink "It was me that taught him, ya know?"
    show liu f_nervous with {'master': dissolve}:
        xoffset -300
        xzoom 1
    liu "Oh?"
    show anon of_empty f_worried with {'master': dissolve}
    anon "Yeah, yeah."
    anon "Are we gonna start putting together a plan here or what?"
    show liu f_happy:
        xoffset 300
        xzoom -1
    tony @ a_frustrated f_laugh "Aww, relax champ..."
    tony "... I'm just clownin' with ya."
    tony f_question "You clue her into what needs doing yet?"
    show liu f_worried with dissolve:
        xoffset -300
        xzoom 1
    liu "No, he's told me very little."
    show liu f_worried with dissolve:
        xoffset 300
        xzoom -1
    liu "B-but I wanna help!"
    liu "Especially if it gets those Russian assholes off your back."
    anon "Yeah, hopefully it will."
    anon "You see, the mob bosses' daughter has offered to help us take her father down but she wants something in exchange."
    liu f_confused "Wait a second, his own daughter?"
    show liu with dissolve:
        xoffset -300
        xzoom 1
    liu "Why would she do that?"
    tony f_sad @ f_eyeroll "Uhh, because she's a Ruskie and they're all fuckin' crazy..."
    show liu f_worried with dissolve:
        xoffset 300
        xzoom -1
    anon "No, she said she wants him out of the way so she can take over."
    tony "Yeah, and she'll probably stab you in the back the second it's done."
    anon f_worried_low "{i}*Sigh*{/i} That's a possibility..."
    anon f_worried "... But I'm willing to take the risk."
    tony f_suspicious @ -m_talk "Hmm."
    pause
    liu "So what does she want in exchange?"
    anon "Some briefcase that they stashed {b}inside the vault at Saga Financial{/b}."
    liu f_surprised "Oh."
    anon "Know anything about it?"
    liu f_worried "Yeah, actually I do."
    anon "Really?!"
    anon "Can you help us get it?"
    liu f_worried_down "Umm..."
    liu "... I mean, I can... yeah."
    tony f_question "I sense a \"but\" comin'."
    liu f_worried "Buuuut they're gonna know it's missing the second you take it."
    anon "Huh?"
    anon "How come?"
    liu "If it's the briefcase I think it is, they have it tagged."
    anon "Tagged?"
    anon "What are you talking about?"
    liu "It's one of the more expensive security precautions we offer."
    liu "Basically, they scan the item into our system where it's monitored twenty-four-seven."
    liu "If it leaves the vault without proper authorization, a security alert is sent and everything goes into lockdown."
    anon f_surprised "Holy crap, really?"
    tony f_angry "See, this is why I don't want {b}Tina{/b} involved."
    tony "They'll pull the securty camera footage and see her takin' this thing out of the vault."
    tony "It'll get back to the mob."
    tony "And next thing you know, your little friend here is tied to a chair in some dark room with a car battery attached to her nipples."
    show anon f_surprised_teeth
    show liu f_shocked:
        xoffset -300
        xzoom 1
    with {'master': fastdissolve}
    liu @ -m_talk "..."
    anon f_worried "Well, we can't have that!"
    show tony f_suspicious
    show liu f_frightened:
        xoffset 300
        xzoom -1
    with dissolve
    pause
    anon "Don't worry, {b}Liu{/b}, we're not going to let anything happen to you."
    show liu f_worried
    show anon f_thinking a_thinking
    with dissolve
    pause
    anon f_confused "How many cameras are there?"
    liu "Three."
    liu "Two in the lobby and one outside the vault."
    anon "It's outside the vault?"
    liu @ -m_talk "Mhmm."
    pause
    anon f_normal a_idle "What if we covered the cameras?"
    tony "How are you gonna do that?"
    anon "I dunno... with a towel or something?"
    liu "No, that won't work."
    liu "They're on the ceiling and you won't get near enough to cover them without walking through their field of view."
    anon f_thinking a_thinking @ -m_talk "Hmm."
    pause
    show liu f_ashamed_down a_cover
    anon f_worried a_frustrated "Okay so there's no way to get around them seeing {b}Liu{/b} in the footage..."
    show anon a_idle with {'master': dissolve}
    tony f_sad "Sounds like this goose is cooked."
    anon f_thinking a_thinking @ f_confused "No, just... gimme a second."
    tony f_sad a_crossed "Kid, we'll find another way... there's no sense-"
    anon f_worried_high @ f_skeptical "{b}Tony{/b}, let me think!"
    tony a_calm_down f_surprised "Sheesh, alright..."
    tony a_frustrated f_sad "Think until your head explodes for all I care."
    tony "I'm just sayin', you'd be better off comin' up with an entirely new plan..."
    tony a_idle @ f_eyeroll "... Maybe one that doesn't involve crazy Russian broads with daddy issues."
    anon a_crossed f_skeptical "I hear you, {b}Tony{/b}."
    anon "Feel free to pitch in your own ideas at any time..."
    tony "{i}*Sigh*{/i} Look, I ain't never been much of an idea guy."
    tony "That was Luigi's department."
    tony f_normal "I just provided the muscle and did my best to look imposing."
    pause
    tony f_smirk "Which, I'll have you know, is an important skill when you rob people for a livin'."
    show liu f_normal
    anon a_idle f_tired "Yeah, I'm sure it is {b}Tony{/b}..."
    pause
    anon f_surprised @ -m_talk "!!!"
    anon "Holy crap, that's it!"
    show tony f_question
    liu f_confused "Huh?"
    tony "What's it?"
    anon f_normal @ f_laugh "We rob the bank!"
    show liu f_surprised
    tony f_surprised @ -m_talk "..."
    tony f_question "You're serious?"
    anon "Yeah, think about it!"
    show liu f_worried
    anon "We go in and pretend to rob the place..."
    show tony f_suspicious
    anon "... And we make it look like we're forcing {b}Liu{/b} to take us down into the vault against her will."
    show liu f_worried_down
    show tony f_thinking
    anon "That way it's all on camera, and as far as the mob is concerned, {b}Liu{/b} was just a victim."
    tony f_smirk "Which should keep 'em off her back."
    anon "Right?!"
    anon "We can grab the briefcase, tie her up, and leave her in the vault for the cops to find."
    tony @ a_point "Heh, not bad kid!"
    tony "This could actually work."
    liu a_idle f_worried "But you two will be in the footage also, committing a felony."
    anon f_worried "Oh."
    anon "Crap, she's right."
    tony a_frustrated @ f_laugh "Ahh, we'll just wear masks."
    show anon f_normal
    tony a_idle "You think the worthless cops in this town are gonna figure it out?"
    tony @ f_laugh "Forghedaboudit!"
    anon "We'll need guns and masks."
    tony "Oh, that won't be a problem."
    tony @ a_finger_up "I got everything we'll need back home at our apartment."
    anon f_worried "And {b}Liu{/b}, you'll have to put on a convincing performance for the cameras..."
    anon "... You think you can do that?"
    liu f_worried_down "I-"
    pause
    liu f_worried "I think so."
    tony "We should hit the place when it's slow."
    tony "Maybe late in the evening or something?"
    tony "And I want {b}Tina{/b} out of the building too!"
    show liu f_worried with dissolve:
        xoffset -300
        xzoom 1
    liu "No, I think early in the morning would be best, we're always slow then..."
    pause
    liu "... And {b}Tina{/b} comes in extra late on Tuesdays... so you'd have a window of about three hours."
    anon "That's more than enough time."
    tony f_question "And what about the alarm situation?"
    tony "Security guards?"
    tony "That sorta thing."
    liu "Umm, we do have a security guard..."
    liu "... But he's like ninety and spends most of the day sleeping."
    anon "That shouldn't be a problem then, right {b}Tony{/b}?"
    tony "Heh, no problem at all."
    liu "... And there's the silent alarm but I'd have to manually trigger it."
    anon f_worried "She can probably just tell them she forgot, don't you think?"
    anon "I mean, that's believable... in high stress situations it's easy to forget things."
    tony f_normal "Yeah, I don't see why not."
    pause
    tony f_smirk @ f_laugh "Man, this is excitin'..."
    tony "... I always wanted to hit a bank!"
    pause
    tony @ a_arms_around "This'll be another thing crossed off my bucket list."
    liu f_worried_down "I need to get back to work."
    pause
    show liu f_worried with dissolve:
        xoffset 300
        xzoom -1
    liu "So we're really doing this?"
    anon "Yeah, I think so."
    show liu f_worried_down behind anon
    pause
    anon a_liu_shoulder "Don't worry, {b}Liu{/b}... everything will be fine, I promise."
    anon "I know you can do this."
    liu f_nervous "Y-yeah, okay."
    anon "Just be ready {b}Tuesday morning{/b}, alright?"
    anon a_idle "We'll come in about ten minutes after you open."
    liu @ -m_talk "Mhmm."
    anon "And call me if anything comes up or we need to alter the plan."
    liu "I will."
    liu f_nervous_down "Umm..."
    pause
    anon f_confused "Is there something else?"
    show liu b_dressed_kiss:
        xoffset 200
    hide anon
    show tony f_surprised
    with {'master': dissolve}
    anon "!!!"
    show tony f_smirk
    pause
    show anon a_sides f_surprised behind liu:
        xoffset 150
        xzoom -1
    show liu b_dressed f_nervous:
        xoffset 500
    with {'master': dissolve}
    liu "Just be careful, okay?"
    anon f_shy "Always."
    show liu f_happy with {'master': dissolve}:
        xoffset -100
        xzoom 1
    liu "It was nice meeting you, {b}Tony{/b}."
    tony "Hey, right back at ya, beautiful..."
    tony "... And don't you fret about a thing, eh?"
    tony "I'll keep the kid safe for ya."
    liu f_laugh "Thank you."
    hide liu
    show anon:
        xoffset 650
        xzoom 1
    with dissolve
    pause
    tony "Heh, you're just plowin' fields all over this town, huh?"
    show anon f_worried with dissolve:
        xoffset 150
        xzoom -1
    anon "N-no, it's not like that... I only wanted to-"
    tony a_point "Ahh, relax... I'm just bustin' ya balls."
    tony -a_point "It's a good thing {b}Maria{/b} went home early today..."
    tony "... I mean, she ain't exactly the jealous type but I don't think she'd have been too pleased seein' that girl smooch ya like that."
    anon f_worried "Oh yeah, I was beginning to wonder why she hadn't popped her head in yet."
    tony "She wasn't feelin' too good so I sent her home to rest."

    if M_maria.pregnancy.stage > 2:
        anon "It's not the baby is it?"
    else:
        anon "Nothing serious I hope?"

    tony "Nah, just a little head cold."
    tony "She'll be fine in a couple days."
    anon f_normal "Oh."
    tony "But it means {b}you gotta go and pick up the gear for the bank job{/b}."
    anon f_confused @ -m_talk "Hmm?"
    anon "Why?"
    tony "Because, she'll get suspicious and start askin' a million questions if I do it."
    tony "I've never been able to lie to her!"
    tony @ f_laugh "The woman reads me like a book."
    anon f_normal "Alright, I can do it."
    anon "Where do you keep it?"
    tony "{b}Look for a gray duffel bag in our bedroom closet{/b}."
    tony "It should be pretty easy to spot."
    tony a_point "And don't let her get a peek at what's inside, eh?"
    tony -a_point "Just tell her somethin' broke at your house and I sent ya over to borrow some tools."
    tony "Capiche?"
    anon "{b}Gray duffel bag, bedroom closet.{/b}"
    anon "I got it."
    tony "{b}Bring the bag with ya to the bank Tuesday morning and I'll meet ya there.{/b}"
    anon "Yeah, okay."
    tony @ a_point "Don't be late!"
    anon "I won't."
    tony "Attaboy."
    tony f_smirk "Man, I wish Luigi was still with us..."
    show tony with dissolve:
        xoffset -550
        xzoom 1
    tony "... He woulda loved this!"
    hide tony
    with dissolve
    pause
    anon f_thinking @ -m_talk "( {b}I should head over to Tony's apartment and get the gear right away.{/b} )"
    anon @ -m_talk "( Hopefully {b}Maria{/b} doesn't ask too many questions. )"
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
