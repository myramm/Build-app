label ano13_tony_pizzeria_interior:
    call tony_button_stage

    show tony a_idle
    show anon with dissolve:
        flip
    tony "'Ey, there he is!"
    anon "Hey, {b}Tony{/b}."
    tony "I'm glad you're here, champ!"
    tony "I was just gettin' ready to polish the old gal up."
    tony "Get her lookin' nice and pretty for our little adventure tonight."
    anon f_confused @ -m_talk "Hmm?"
    tony "Here, I'll show ya."
    show tony b_dressed_pickup with {'master': dissolve}:
        xoffset -300
    anon f_worried_low "Alright."
    show tony b_dressed a_pipe_brandish:
        xoffset 0
    show anon f_surprised a_sides
    with {'master': dissolve}
    tony "Here she is."
    anon @ -m_talk "!!!"
    tony f_normal_down a_pipe_hold @ -m_talk "Hmm."
    tony "She's a bit dusty but otherwise no worse for wear."
    anon f_skeptical "{b}Tony{/b}, what the heck is that?"
    tony a_pipe_touch "I call her Vera."
    anon f_surprised @ -m_talk "..."
    tony @ f_normal "She saved my life once back in the day and I been keepin' her close ever since."
    anon "A pipe saved your life?"
    tony @ f_smirk_wink "That's right."
    anon f_normal @ -m_talk "..."
    tony a_pipe_hold "Heh, maybe I'll tell you the story sometime..."
    tony @ f_normal "... If you ask real nice."
    show tony a_pipe_touch with dissolve
    pause
    anon f_shy "Right."
    pause
    anon "So uhh..."
    pause
    anon "... About tonight..."
    tony f_normal "Oh, don't worry about tonight."
    tony "We're gonna be fine."
    show tony a_pipe_swing
    show anon b_dressed_blocking
    with dissolve
    tony @ f_laugh "Any of those dirty ruskies come at us, they're gonna get their fuckin' skulls bashed in!"
    show tony a_pipe_touch
    show anon b_dressed f_worried
    with dissolve
    anon "{b}Tony{/b}..."
    tony "Vera here cracks 'em open like eggs on a fryin' pan!"
    tony @ f_laugh "We'll make ourselves an omelet, eh?"
    anon "Last night, I-"
    tony "Heh, it would probably taste like vodka..."
    anon "I went-"
    tony @ f_laugh a_pipe_brandish "... And cabbage."
    anon @ f_angry "{b}Tony{/b}, listen to me!"
    tony f_suspicious @ -m_talk "Hmm?"
    anon "I already went to the warehouse."
    tony f_surprised "Eh?"
    tony f_angry "What are ya talkin' about?"
    anon "Y-yeah, last night."
    anon "I went there to scope the place out, like we discussed."
    tony a_idle @ a_point "Are you tellin' me, that you went there by yourself?"
    anon a_surprised_up_both "{i}*Gulp*{/i} Y-yes."
    pause
    tony @ f_question "What are you, fuckin' stupid?!"
    tony "What did I tell you, eh?!"
    anon a_sides f_sad_down @ -m_talk "..."
    tony "I told you not to go by yourself!"
    anon "I just-"
    tony "You got no experience with this kinda thing..."
    tony "... And no idea what you're lookin' for!"
    tony "You can't weigh more than a buck twenty soakin' wet!"
    tony "What was your plan if one of them bastards discovered ya, eh?"
    anon @ f_sad "I-"
    anon "It wasn't-"
    maria "What's with all the yellin' out there?"
    tony @ a_point "This isn't some silly video game, {b}[firstname]{/b}!"
    anon "I know that."
    tony "These fuckin' ruskies will kill ya and they ain't gonna do it fast neither!"
    anon @ -m_talk "..."
    show maria b_dressed_magic f_sad behind counter with dissolve:
        flip
        xoffset -200
    maria "What the hell are you screamin' at him for {b}Tony{/b}?!"
    show anon f_sad
    show tony with dissolve:
        unflip
        xoffset -400
    tony "I'm screamin' at him because he's a fuckin' idiot!"
    maria f_angry "{b}Tony{/b}, don't talk to him like that!"
    maria "He's the biological father of our child for fuck's sake!"
    show tony with dissolve:
        flip
        xoffset 0

    if M_tony.watches:
        tony "Yeah, and that's why I expected more sense from him!"
    else:
        tony "Yeah, well maybe that wasn't such a good decision..."

    anon f_sad_down a_behind_head @ -m_talk "..."
    tony "Go on, tell her what you did."
    show maria f_sad
    pause
    anon f_sad a_sides "{i}*Sigh*{/i} I went to the Russian hideout last night."
    maria f_surprised "!!!"
    pause
    maria f_angry "What are you, fuckin' stupid?!"
    tony f_normal @ f_laugh "Heh, that's exactly what I said."
    anon f_worried a_surprised_up_both "Listen, I thought about what we discussed the other day, and you were right."
    anon "You and {b}Tony{/b} are finally starting a family together..."
    anon a_sides "... It's wrong for me to drag him into my mess."
    show tony f_angry
    maria "That's not-"
    tony @ f_eyeroll "What a load of fuckin' cazzate!"
    anon @ f_confused -m_talk "Hmm?"

    if M_tony.watches:
        tony f_sad "Don't you realize you're part of this family too?"
        anon f_sad @ -m_talk "..."
        tony "And family watch each other's backs, eh?"
        maria "Damn straight!"
    else:
        tony "Shieldin' me from danger and goin' alone doesn't make you heroic, champ."
        tony @ f_question "It makes you a fuckin' moron."
        maria "He's right."
        anon f_sad @ -m_talk "..."
        maria "I don't want either of ya gettin' involved with those animals but if you insist upon doin' it, it's best that {b}Tony{/b} go with ya."
        maria "He's done this kinda thing before."

    anon "I don't know what to say..."
    tony f_sad "Well, you can start by sayin' you're sorry..."
    anon f_sad_down "I am."
    pause
    anon f_sad "Sorry, that is."
    tony f_angry @ a_point "... And that you'll do what I say, from now on?!"
    anon "I will."
    pause
    anon a_surprised_up_both f_surprised "I promise."
    tony f_suspicious "Good."
    show anon f_worried a_sides with dissolve
    pause
    tony "So what happened?"
    anon @ -m_talk "Hmm?"
    tony "At the warehouse last night."
    tony "What did you find out?"
    anon f_surprised "Oh, umm..."
    anon f_worried "Well, it was actually pretty quiet."
    anon "There were a couple guards and I saw some women in their underwear..."
    maria f_confused "Women in their underwear?"
    anon @ a_behind_head "Y-yeah."
    show tony f_thinking
    anon "{b}Dimitri{/b} and {b}Igor{/b} dragged them out of the warehouse and were yelling at them."
    tony f_suspicious "What about?"
    anon "I'm not sure..."
    anon "It was too far away and I couldn't hear them."
    tony "Hmm, sex slaves maybe?"
    show anon f_thinking
    pause
    tony "What else can you tell me?"
    anon a_thinking "Mmm."
    tony "How many points of egress?"
    anon a_idle f_worried @ f_confused "Huh?"
    tony "You know, doors and windows?"
    anon "Oh, I have no idea."
    tony "Okay... Did you get a head count on their men?"
    anon "... No."
    tony "Tsk."
    tony "Anything visible that we could exploit for a distraction?"
    anon f_thinking "Uhh."
    tony f_angry @ -m_talk "Grr!"
    tony "See, this is why I told you not to go alone!"
    anon f_sad_down @ -m_talk "..."
    tony "You completely ballsed it up!"
    pause
    tony "{i}*Sigh*{/i} Frankly, I'm surprised nobody saw ya."
    anon f_worried "Uhh, yeah..."
    anon "... About that."
    tony @ -m_talk "Hmm?"
    anon f_shy @ a_behind_head "Somebody, kinda... did..."
    anon "See me, that is."
    show anon f_worried
    tony @ f_question "What do you mean?"
    anon "Well, apparently the police were scoping the place out too..."
    anon f_worried_low "... And they saw me and well..."
    pause
    anon f_surprised_teeth @ f_worried "... We had a talk."
    tony @ f_eyeroll "Oh, for fuck's sake!"
    anon f_surprised @ a_surprised_up_both "I didn't tell them anything {b}Tony{/b}, I swear!"
    anon "They just gave me a ride home and that was it."
    tony "Well, I gotta tell ya..."
    tony "... This was a world-class fuckup, champ!"
    anon f_sad_down @ -m_talk "..."
    tony "There's no way we can go back to that warehouse now without the cops gettin' all up in our asses."
    maria "We should just let them handle it, you know?"
    tony @ f_eyeroll "What, the cops?!"
    show anon f_worried
    tony @ f_laugh a_belly "You gotta be jokin'..."
    maria "{b}Tony{/b}, they're obviously bein' proactive about this..."
    show tony with dissolve:
        unflip
        xoffset -400
    tony "Why?"
    tony "'Cause they was sniffin' around the warehouse?"
    maria "Yeah."
    tony @ f_eyeroll "Psh, that don't mean nothin'!"
    pause
    show tony f_normal with dissolve:
        flip
        xoffset 0
    tony @ f_smirk_wink "They probably got lost on their way to raid the donut shop, eh?"
    anon f_normal @ f_laugh "Hehe!"
    maria "That's not funny, {b}Tony{/b}!"
    show tony with dissolve:
        unflip
        xoffset -400
    tony "Ahh, would you relax darlin'?"
    tony "You got exactly what you wanted."
    maria @ -m_talk "Hmm?"
    tony "If the cops is watchin' that place, I ain't goin' anywhere near it..."
    anon f_worried "So what's next?"
    show tony with dissolve:
        flip
        xoffset 0
    tony f_suspicious @ a_point "That's the million-dollar question, champ."
    pause
    tony @ a_frustrated "We can't strike at the mob directly..."
    tony "... So we either need to find someone else who can or a way to hit 'em indirectly."
    anon @ f_skeptical "Indirectly?"
    anon "What do you mean?"
    tony "Eddie mentioned they had some big wig throwin' funds at 'em, yeah?"
    tony "If we could just figure out who it is..."

    if M_josie.finished_state(S_jos01_find):
        anon f_thinking a_thinking "Actually, I might know!"
        tony @ -m_talk "Hmm?"
        anon f_normal a_idle "I was at the car dealership the other day and I overheard a conversation between {b}Mayor Rump{/b} and a salesman."
        anon "{b}The mayor{/b} mentioned having some new Russian associates."
        tony f_surprised "Did he?"
        maria "That isn't proof of anything."
        maria "Just because he has a Russian associate, doesn't mean it's related to the mob."
        tony f_suspicious "True but it's still worth checkin' out."
        tony "And it's not like we have anything else to go on..."
    else:
        anon "I'll keep my ear to the ground and let you know if I hear anything..."
        maria "It's not much to go on {b}Tony{/b}."
        tony "Yeah, I know..."
        tony "... But we don't have a whole lot of options right now."

    anon f_surprised @ a_point "!!!"
    anon "I just remembered something!"
    pause
    anon "The officer that drove me home last night..."
    anon "... She mentioned that the police released a {b}box of personal belongings{/b} to my landlady yesterday."
    tony f_surprised "Oh?"
    anon "Yeah, I completely forgot about it!"
    anon f_worried @ f_skeptical "Do you think the police could have missed something?"
    tony f_normal "Heh, you're damn right they could have!"
    show anon f_normal
    tony @ a_frustrated "Fuckin' numbskulls can't find their asses to wipe 'em half the time!"
    anon "I should get back home and {b}speak with [deb_name]{/b} about it."
    tony "Yeah, I agree."
    tony "In the meantime, I'll make some calls and see what I can dig up."
    anon "Thanks, {b}Tony{/b}."
    anon "I'll come back as soon as I find something."
    maria @ f_angry "Just remember to be smart, from here on out..."
    maria "You do anymore stupid things like going to that warehouse by yourself and I'm cuttin' you off, mister!"

    if M_tony.watches:
        maria "Just because {b}Tony{/b} and I love ya, doesn't give ya a free pass to be an idiot!"
    else:
        maria "I don't care how good ya cock feels!"

    tony @ f_laugh "Hah!"
    maria "I'll take this pussy right off the market!"
    maria "Ya hear me?"
    anon f_worried "Y-yes, ma'am."
    maria @ -m_talk "Hmph."
    hide maria with dissolve
    pause .2
    show tony:
        unflip
        xoffset -400
    with dissolve

    if M_tony.watches:
        tony "Don't worry, she's just blowin' off some steam..."
        show tony f_smirk_wink with {'master': dissolve}:
            flip
            xoffset 0
        tony "I'll talk with her."
    else:
        pause
        tony @ -m_talk "..."
        show tony with dissolve:
            flip
            xoffset 0

    tony f_normal "Head on home, champ."
    anon f_normal @ a_salute "Yes, sir."
    hide anon with dissolve
    return


label ano13_tina_pizzeria_interior:
    scene expression player.location.background_closeup
    show expression game.timer.image('char_xtra_12{}') as counter
    show tony:
        flip
    show maria b_dressed_magic:
        flip
        xoffset -200
    show tina:
        xoffset -200
    tina "See, I knew the kid was a sure thing."
    tina @ f_sexy "Didn't take him long neither, from the sound of it."
    tony "Yeah, he done real good for us..."
    tony @ f_laugh a_belly "... Put a pup in {b}Maria{/b} almost right away."
    tina "I'm not surprised."
    tina "He's just so young and virile!"
    tony "Bah, every guy is at that age, {b}Tina{/b}."
    tony "Hell, Luigi and I used to bag three girls a day..."
    tina @ f_sexy "Well, is it any wonder your swimmers quit swimming?!"
    maria f_disgusted "Yeah, no doubt."
    tina "You're lucky your dick hasn't fallen off..."
    tony @ f_laugh "'Ey, watch it, you!"
    show maria f_eyeroll
    tina @ f_laugh "Hehe!"
    show maria f_normal
    tony @ f_laugh a_point_back "My dick is just fine and you know it!"
    tony f_smirk "I don't recall hearin' any complaints from either of you, eh?"
    tina f_sexy "Well, at least not to your face..."
    tina @ f_laugh "... Right, {b}Maria{/b}?"
    show tony f_surprised
    maria "Nu uh, don't you go draggin' me into this!"
    show anon f_skeptical behind tony:
        flip
        xoffset 194
    with dissolve
    tina f_normal @ f_laugh "Hahaha!"
    show tony f_normal
    anon f_normal @ a_wave "Hey, everyone."
    show tina with dissolve:
        flip
        xoffset 363
    tina "... And there he is."
    tony "We were just talkin' about you, champ."
    tina "His ears must have been burning."
    anon @ -m_talk "Hmm?"
    tina a_pinch "I hear you've been putting in some overtime hours here at the pizzeria, huh?"
    show maria o_blush
    show tina a_idle
    show anon f_shy of_blush
    with {'master': dissolve}
    anon f_shy of_blush "Ehh... Heh."
    maria "Oh, lay off it, {b}Tina{/b}..."
    show anon of_empty
    show maria o_empty
    with {'master': slowdissolve}
    maria "... You're embarrassin' the poor boy."
    tina f_sexy @ f_laugh "Aww, he's not embarrassed..."
    tina "... Are you stud?"
    show tina with dissolve:
        unflip
        xoffset -200
    tina f_normal "I wanna hear some details!"
    maria f_angry "No."
    tina "Oh, c'mon!"
    tina "I vetted him for you guys, didn't I!"
    show anon f_surprised
    tina "That's gotta earn me a little something something?"
    tony @ f_laugh "I'm pretty sure the kid gave you more than a little something something already, {b}Tina{/b}..."
    show anon f_shy_low of_blush with {'master': dissolve}
    maria "{b}Tony{/b}!!"
    tina @ f_laugh "Hah, true enough."
    tony f_normal_right "It's fine {b}Maria{/b}..."
    tony "... I'm not gonna get mad."
    maria "It's not fine!"
    maria "What happens in our bedroom is private and I don't like discussin' it with nobody."
    maria "Not even with you, {b}Tina{/b}."
    show tony f_normal
    tina @ f_eyeroll "Oh, fine."
    tina "Be that way."
    show tina f_sexy with dissolve:
        flip
        xoffset 363
    tina "We'll just have some fun on our own then, won't we babyface?"
    show maria f_sad
    anon f_shy a_behind_head "Ehh, yeah... I guess."
    tina @ f_laugh "Hehe!"
    tony f_smirk "Sounds like you're gonna have your hands full for a while, champ."
    show tony a_tina_shoulder
    show tina b_empty
    show anon a_idle of_empty
    with dissolve
    tony "This one isn't easily kept satisfied."
    anon f_confused "Umm, what does \"vetted\" mean?"
    show maria f_skeptical
    tony f_suspicious @ -m_talk "Hmm?"
    anon "{b}Tina{/b} said she \"vetted\" me for you guys..."
    anon f_worried "... What does that mean?"
    tony f_normal "It means I sent you to her as a test of your baby-makin' abilites and she reported back to me."
    tina f_sexy "I thought it was obvious..."
    anon f_surprised "My what?!"
    tony @ f_eyeroll "I had to make sure you knew what went where before askin' you to pump a baby into my wife..."
    tony "... {b}Tina{/b} owed me one, so I asked her to give you a practice run."
    show tony a_idle
    show tina b_dressed f_annoyed
    with dissolve
    tina "What, you think I just jump in the sack with every guy who shows up at my door with a pizza?!"
    anon f_worried "N-no, of course not-"
    tina f_normal @ f_laugh "Hahaha!"
    tina @ a_pinch "Relax kid, you passed with flying colors."
    show anon f_shy
    tina "With the exception of my daughter walking in on us, it was the best sex of my life."
    show maria f_surprised
    tony f_smirk "Wait a second, you didn't mention that before!"
    show tina:
        unflip
        xoffset -200
    show maria f_normal
    with dissolve
    tony @ f_laugh "Little {b}Rebecca{/b} walked in on you guys?!"
    tina f_sad "{i}*Sigh*{/i} Yeah, right at the end."
    tina "The poor girl was mortified."

    if M_tina.becca_crush:
        tina f_normal "The girl has a bit of a crush on him, I'm afraid."
        tony "You don't say?"
        tina f_sexy "Apparently, her little social group has been passing him around like candy."
        tony @ f_laugh a_belly "Hah!"
        tony "You're just full of surprises, ain't ya, champ?"
    else:
        tina "Apparently, the kid here isn't very popular at school..."
        tony "You're kiddin'?"
        tina f_sexy "... My daughter has become quite the little snob, I'm afraid."
        maria @ f_surprised "That's surprising."
        maria "She was such a sweet kid..."

    tina "Regardless, we'll have to be careful going forward."
    show tina with dissolve:
        flip
        xoffset 363
    tina "{b}Come see me at the bank{/b} if you wanna set something up, okay?"
    show tina f_kiss a_blow_kiss with dissolve
    pause
    show tina f_normal a_idle with dissolve
    anon "Y-yeah, okay."
    show tina with dissolve:
        unflip
        xoffset -200
    tina "Speaking of which... I need to get back there."
    tina "Our teller can't be left on her own for too long."
    tina @ f_eyeroll "Poor girl is timid like a mouse."
    show tina b_dressed_hug_maria
    hide maria
    with dissolve
    tina "I'm so happy for you guys..."
    maria "Aww, thanks, doll."
    tony "Yeah, we got lots of work to do here ourselves."
    tony "Orders are comin' in so fast, we can barely keep up."
    show maria b_dressed_magic:
        flip
        xoffset -200
    show tina b_dressed
    with dissolve
    pause
    tony "You got time to make some deliveries, champ?"
    anon f_worried "Actually, I was hoping you could take a look at something for me?"
    show anon f_looking_down a_backpack
    show tina:
        flip
        xoffset 363
    with dissolve
    tony f_suspicious "Oh?"
    anon f_worried a_box_attic_photo "Yeah, I found this hidden amongst my father's belongings..."
    show anon a_idle
    show tony f_normal_down b_dressed_pic
    show tina f_normal_down b_empty:
        flip
        xoffset 186
    show maria b_empty f_surprised_low m_talk:
        xoffset -194
    with dissolve
    pause
    show maria f_sad -m_talk
    tony f_surprised "Holy shit, champ!"
    tina f_suspicious "Who's that shaking {b}Mayor Rump{/b}'s hand?"
    maria "That's his father, I'm sure."
    anon "It is."
    tony f_suspicious "Well, the guy on the right is {b}Raz Chernyshevsky{/b}... Ain't no doubt about it."
    maria @ f_surprised_low "The mob boss?"
    tony @ -m_talk "Mhmm."
    tony "I'd recognize his ugly mug anywhere."
    tina f_annoyed @ f_normal_down "... He looks like a goblin."
    maria f_disgusted "He really does."
    anon "Well, I guess that confirms it then..."
    anon f_sad_down "... My dad was definitely working with the Russians."
    show maria f_sad
    show tina f_sad
    tony f_sad "I'm afraid so, champ."
    pause
    tony f_suspicious "It also confirms that our beloved mayor is involved in this mess as well."
    maria "He's likely the political backing your sources were hinting at."
    tony @ f_question "What's this number at the top?"
    anon f_worried "Yeah, I'm not sure."
    anon "There was a little key attached too."
    tina f_normal @ f_surprised "I know exactly what that is!"
    tony @ -m_talk "Hmm?"
    tina "It's a lockbox code."
    anon @ f_skeptical "Lockbox?"
    show tony b_dressed
    show maria b_dressed_magic behind tony:
        xoffset -200
    show tina b_dressed behind tony:
        xoffset 300
    show anon a_box_attic_photo
    with dissolve
    tina "Yeah, we have a bunch of them down at the bank."
    tina "In fact, it's probably one of ours."
    tony "No kiddin'?"
    tina f_annoyed "Hmmm... I can't today..."
    if game.timer._dow == 4:
        tina "... And I don't work Saturdays..."
        tina f_normal "... But if you swing by after the weekend I'll take you down to our vault."
    elif game.timer._dow == 5:
        tina "... And we're closed tomorrow..."
        tina f_normal "... But if you swing by next week I'll take you down to our vault."
    else:
        tina f_normal "... But if you swing by tomorrow I'll take you down to our vault."
    tina "So long as you have the key, we can take a look."
    anon f_normal "Yeah, okay."
    tony "Now we're gettin' somewhere!"
    tina "See ya, guys."
    tony "Bye, {b}Tina{/b}."
    anon "See ya."
    hide tina with dissolve
    pause
    maria "Shouldn't he take this to the police?"
    show tony f_angry behind maria with dissolve:
        unflip
        xoffset -250
    tony "Ugh, you're still goin' on about the fuckin' police?!"
    maria f_angry "It's their job, {b}Tony{/b}!"
    tony "They ain't worth a damn, {b}Maria{/b}..."
    show anon f_worried
    maria @ f_eyeroll "Says you!"
    maria "It don't hurt to keep 'em in the loop."
    maria "They can't help if you withhold evidence from 'em!"
    tony @ f_eyeroll "Bah, whatever."
    show tony f_suspicious with dissolve:
        flip
        xoffset 200
    tony "Champ, if you wanna waste time cluin' the cops in... That's on you."
    tony "Go ahead and {b}take it down to the precinct{/b}."
    tony "{b}Chat with that detective who's workin' your pa's case{/b}."
    anon @ -m_talk "..."
    tony "But if I was you, I'd {b}meet Tina at the bank and check that lockbox{/b}."
    anon f_normal "Yeah, okay."
    maria @ -m_talk "Hmph!"
    hide maria with dissolve
    show tony with dissolve:
        unflip
        xoffset -250
    tony a_frustrated @ f_sad "Aww, c'mon darlin'..."
    show anon f_worried
    tony "... What, I'm not allowed to have my own opinion?!"
    pause
    tony a_whisper "{b}Maria{/b}?!"
    hide tony with dissolve
    pause
    anon f_thinking @ -m_talk "( Hmm, I guess I have a decision to make... )"
    anon @ -m_talk "( {b}I can take this evidence to the cops{/b} or I can {b}head down to the bank{/b} and continue investigating on my own... )"
    pause
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
