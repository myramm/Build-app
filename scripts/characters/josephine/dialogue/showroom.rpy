label josie_button_showroom:
    show josephine b_dressed_bored
    show anon f_worried_low with dissolve

    if M_anon.finished_state(S_ano09_blow):
        anon "{b}Josephine{/b}?"
        show josephine b_dressed f_sexy
        show anon f_normal
        with dissolve
        josephine "Hey, {b}[firstname]{/b}."
        josephine "You here to keep me company?"
    else:
        anon "Excuse me?"
        josephine "..."
        anon "{b}Josephine{/b}?"
        josephine "..."
        anon "HELLO?!"
        show josephine b_dressed f_bored a_phone
        show anon f_skeptical
        with dissolve
        josephine @ -m_talk "Hmm?"
        josephine "Oh, it's you."
        josephine f_normal_down "What's up?"

    label josie_button_showroom.choice:
    menu:
        "Buy a vehicle." if M_anon.is_state(S_ano05_sale):
            jump ano05_sale_josie.anon

        "Private photos." if M_anon.between_states(S_ano07_mech, S_ano07_give):
            jump ano07_hint_josie

        "Buy a vehicle." if M_anon.is_state(S_ano07_sale):
            jump ano07_sale_josie.anon

        "Buy a vehicle." if M_anon.is_state(S_ano09_sale):
            jump ano09_sale_josie.anon

        "How's work going?" if M_anon.finished_state(S_ano05_sale):
            jump josie_button_showroom.work

        "Naked selfies?" if M_anon.finished_state(S_ano07_perk):
            jump josie_button_showroom.nudes

        "Russians?" if M_anon.finished_state(S_ano09_brat) and not M_josie.finished_state(S_jos01_find):
            jump josie_button_showroom.russians

        "Don't you have any passions?" if not M_anon.finished_state(S_ano09_blow):
            jump josie_button_showroom.passion
        "You wanna make out?":

            if M_anon.finished_state(S_ano09_blow):
                jump josie_button_showroom.kiss
            jump josie_button_showroom.flirt

        "Blowjob?" if M_anon.finished_state(S_ano09_blow):
            jump josie_button_showroom.blowjob

        "Sex." if M_josie.finished_state(S_jos02_init):
            jump josie_button_showroom.sex

        "{b}Kim{/b}." if M_kim.state is None:
            jump josie_button_showroom.kim

        "{b}Kim{/b}." if M_kim.state is not None:
            jump josie_button_showroom.yoyo
        "Never mind.":

            pass

    if M_anon.finished_state(S_ano09_blow):
        anon f_normal @ a_wave "I'll catch you later, {b}Josephine{/b}."
        josephine f_normal "Later, {b}[firstname]{/b}."
    else:
        anon f_normal @ a_wave "I'll catch you later, {b}Josephine{/b}."
        josephine "Later, bowl cut."
        show anon f_unimpressed
        pause

    hide anon with dissolve
    return


label josie_button_showroom.blowjob:
    anon f_flirt @ -m_talk "..."
    josephine f_concerned @ -m_talk "..."
    pause
    josephine f_sexy @ f_eyeroll "Alright, fine."
    anon @ f_laugh "Sweet!"
    pause
    josephine "You still have that vest?"
    anon "I do."
    josephine "Well, put it on and come behind the desk."
    anon f_worried "Wait a second, can't we go to the bathroom or something?"
    josephine "Where's the fun in that?"
    anon @ -m_talk "..."
    josephine "C'mon, hurry up."
    anon "Okay, okay..."

    call scene_josie_blowjob.repeat from josie_button_showroom.blowjob_resume
    $ unlock_scene('josie', '01_unlocked')

    call josie_button_stage
    show anon b_jacket f_flirt_low behind josephine:
        flip
    show josephine b_dressed:
        flip
        offset (400, 300)
    with fade
    anon "Phew."
    anon "That was awesome!"
    show anon f_flirt with dissolve:
        xoffset 100
    show josephine f_sexy o_cum with dissolve:
        offset (350, 0)
    pause
    josephine @ a_fingerlick "Salty."
    josephine "Well, that was a fun diversion."
    anon @ f_laugh "Heh, yeah."
    anon f_worried @ a_schmutz "You know, you've got a little something..."
    josephine "Yeah, no shit."
    josephine "Dude, you always cum like a crazy amount!"
    anon f_flirt "Sorry."
    pause
    anon f_worried "Do you want me to get you a towel or something?"
    josephine "No, I'm gonna leave it for a while."
    anon f_surprised "Really?"
    josephine "Yeah, it's funny to see the customer's reaction."
    anon @ -m_talk "..."
    anon f_worried "You're a weird girl, you know that?"
    josephine @ f_laugh "Haha!"
    hide anon with dissolve
    return 'blowjob'


label josie_button_showroom.flirt:
    anon f_flirt "You wanna make out?"
    josephine f_pouting "Eww, no."
    anon f_worried "What?"
    anon "We did it earlier, didn't we?"
    josephine f_normal "Yeah, but that was for a purpose..."
    josephine "I was trying to get fired, remember?"
    anon f_flirt @ f_laugh "So, we can try again!"
    anon "What do you say?"
    josephine f_normal_down "How about no."
    anon f_worried "Aww, c'mon... Nobody ever got fired just sitting around looking at their phone all day."
    show josephine f_concerned
    pause
    anon f_shy "Alright, so maybe lots of people have gotten fired by doing exactly that."
    anon @ f_laugh "But I think you can do so much better!"
    show josephine f_normal_down
    pause
    anon f_worried "Maybe just a little bit?"
    josephine @ f_angry_down "Dream on, bowl cut."
    anon f_unimpressed "Ugh, fine."
    jump josie_button_showroom.choice


label josie_button_showroom.kim:
    anon f_worried "What's up with that {b}Kim{/b} guy?"
    josephine "He's a fucking douche canoe."
    josephine "That's what's up with him."
    anon "How does he keep his job?"
    josephine @ f_eyeroll "He has a bunch of repeat customers who buy a surprising amount of expensive cars."
    anon f_surprised "Really?"
    josephine "Including {b}Mayor Rump{/b}."
    anon f_surprised @ f_shock "The mayor buys his cars here?"
    josephine "Yup."
    josephine "And he specifically asks for {b}Kim{/b}, every time."
    anon f_confused "Why?"
    josephine f_normal "Oh, you haven't seen what he's like around his preferred customers."
    josephine "He turns into the biggest brown noser on the planet."
    show anon f_worried
    josephine f_normal_down "It's disgusting."
    anon "I can imagine."
    pause
    anon f_unimpressed "Ugh, I hate that guy."
    jump josie_button_showroom.choice


label josie_button_showroom.kiss:
    anon f_flirt "You wanna make out?"
    josephine f_concerned "Make out?"
    pause
    josephine "Wouldn't you rather do something more fun?"
    anon @ f_laugh "You don't think kissing is fun?"
    josephine @ f_eyeroll "I mean, I guess..."
    anon "More fun then sitting here bored all day, right?"
    josephine "True."
    pause
    josephine f_sexy "Alright, fuck it."
    anon "Awesome!"
    anon "I knew yo-"
    show josephine b_dressed_kiss_lips:
        xoffset -300
    hide anon
    anon "!!!" with hpunch
    pause
    show anon f_surprised behind josephine
    show josephine b_dressed f_angry a_gimme
    with dissolve
    josephine "C'mon, dude, more tongue!"
    anon f_worried "S-sorry."
    show josephine b_dressed_kiss:
        xoffset -300
    hide anon
    with dissolve
    pause
    show anon f_shy
    show josephine b_dressed f_laugh -a_gimme:
        xoffset 0
    with dissolve
    josephine "Not bad, bowl cut."
    anon f_unimpressed a_sides "Seriously, you're still calling me bowl cut?!"
    josephine f_sexy "Heh, get a haircut and I'll stop."
    anon a_idle "Very funny."
    jump josie_button_showroom.choice


label josie_button_showroom.nudes:
    anon f_normal @ f_confused "What were those naked selfies doing on your phone anyway?"
    josephine f_bored "{i}*Sigh*{/i} I'd rather not say."
    anon "Aww, c'mon... It's nothing to be embarrassed about."
    josephine @ f_eyeroll "Ugh, fine."
    josephine "I was trying to get into a video game."
    anon f_confused "Huh?"
    josephine "Yeah, there's this guy who creates crowdfunded video games and streams himself drawing the artwork."
    josephine "His name is {b}DarkCookie{/b}."
    josephine "I watch him all the time during my lunch break."
    anon "Oh kay?"
    anon "What does that have to do with naked selfies?"
    josephine "Well, he was running a contest where he offered to put people in his game if they sent him pictures of their boobs or dicks with the words, \"I Love Summertime Saga.\" written on them."
    anon f_surprised "For real?"
    josephine "Yeah."
    josephine "He's a weird dude."
    anon f_sad_down a_facepalm "Sounds like it."
    pause
    anon f_worried a_idle "So you sent those photos to him?"
    josephine "No, I couldn't do it."
    anon "Why not?"
    josephine "I chickened out, okay?!"
    anon f_normal @ f_laugh "You chickened out?!"
    josephine "Shut up, you would have chickened out too!"
    anon "Yeah, maybe..."
    anon "I'm just surprised is all."
    josephine "Why is that?"
    anon f_flirt "Well, speaking as someone who has glimpsed what you're hiding under those clothes..."
    josephine "Don't be creepy."
    anon "Heh, I'm just saying... You have nothing to be embarrassed about."
    josephine @ -m_talk "..."
    anon "You're beautiful."
    josephine "Yeah, well..."
    josephine "Thanks, I guess."
    anon @ a_point "You're welcome."
    josephine "Can I get back to not working now?"
    jump josie_button_showroom.choice


label josie_button_showroom.passion:
    anon f_normal "Don't you have any passions?"
    josephine "What kinda question is that?"
    anon "I dunno."
    anon "I'm just trying to figure out what kind of work you'd be better suited for..."
    josephine @ f_eyeroll "Umm, try literally anything?"
    anon "C'mon, seriously... What are your passions?"
    josephine @ f_angry "Ugh, I don't know."
    josephine "I guess I like clothes..."
    anon "Okay, that's a start."
    josephine "And shoes."
    anon "What else?"
    josephine f_sexy "Oh, I like watching videos on the internet and trolling people in the comment sections."
    anon f_skeptical @ -m_talk "..."
    anon "Yeah, I'm not sure that's a marketable skill..."
    show anon f_normal
    josephine f_normal_down "Well, it should be!"
    josephine "It takes a lot of hard work to get on my trolling level."
    anon "I'm sure."
    jump josie_button_showroom.choice


label josie_button_showroom.russians:
    anon f_worried "By the way, have you ever had any Russian customers in here?"
    josephine f_normal "Yes, quite a lot actually..."
    josephine "How did you know about that?"
    anon "Ehh, let's just call it a hunch..."
    josephine f_concerned "Oh kay."
    pause
    anon "Can you tell me anything about them?"
    josephine f_normal "They buy a lot of cars from us..."
    josephine @ f_surprised "Like, a crap ton!"
    anon @ f_confused "Really?"
    josephine "Yeah."
    josephine @ a_feigning "Always black too."
    josephine "Except for this last time, they had a young girl with them who wanted a Baudi B5 in gunmetal and then threw a tantrum when we didn't have one."
    josephine f_bored "Spoiled little shit."
    anon "Do you have like, a name or an address for them?"
    josephine "I dunno, probably."
    josephine f_normal "{b}Kim{/b}'s the one who always deals with them, they're his customers."
    $ M_kim.set('russians', True)
    anon f_unimpressed "Oh, great."
    josephine "You could try speaking with him about it?"
    anon "Yeah, that'll go great, I'm sure..."
    josephine f_sexy @ f_laugh "Heh."
    jump josie_button_showroom.choice


label josie_button_showroom.sex:
    if game.timer.is_day():
        anon f_shy "Want to have sex?"
        josephine f_sexy "Hell yeah!"
        josephine "{b}Meet me in the break room{/b} in five minutes."
        hide josephine with {'master': dissolve}
        anon f_laugh "Alright."
    else:
        anon f_shy "Want to have sex?"
        josephine f_sexy "Hell yeah!"
        josephine "{b}Meet me in my dad's office{/b} in five minutes."
        anon f_worried "Wait a second."
        anon "You really think that's a good idea?"
        josephine "Don't worry, he's busy down here closing up."
        josephine "He won't bother us."
        anon "I dunno..."
        josephine "C'mon, it gets me really hot!"
        josephine "Please?!"
        pause
        anon "Alright, just try not to make too much noise, okay?"
        josephine "Stop worrying!"
        josephine "C'mon."
        hide josephine with {'master': dissolve}
        anon @ a_point "I-"
        anon "Never mind."
    hide anon with dissolve
    return 'sex'


label josie_button_showroom.work:
    anon f_normal "How's work going?"
    josephine @ f_eyeroll "Ugh, how do you think it's going?"
    anon "Same as usual, huh?"
    josephine "This job's about as exciting as a trip to the dentist's office."
    anon "You know, it really doesn't seem that bad to me."
    josephine "At least I have my phone back now."
    anon "Yeah, you're welcome for that by the way..."
    josephine "Hey, I seem to recall you being properly rewarded!"
    anon f_flirt "Well, the discount WAS nice."
    show josephine f_surprised m_talk
    pause
    josephine f_angry "Heeeeey!"
    show josephine a_crossed -m_talk with dissolve
    anon f_normal @ f_laugh "Hahahaah!"
    anon "I'm just kidding."
    josephine "Well, it's not funny."
    show josephine f_normal_down a_phone with dissolve
    jump josie_button_showroom.choice


label josie_button_showroom.yoyo:
    anon f_worried "What's up with that new {b}Kim{/b}?"
    josephine f_normal "Oh, you met her, huh?"
    anon "Yeah."
    anon f_confused "How can there be two of them?"
    josephine f_laugh "Hehehe!"
    anon "I mean, seriously..."
    anon "... They're exactly alike."
    josephine f_normal "At least the new one doesn't smell as bad."
    anon f_happy "Heh, yeah... That's something I guess."
    pause
    anon f_confused "Just be careful around her, yeah?"
    anon f_worried "She seems more capable than her brother."
    josephine @ f_eyeroll "That's not saying much."
    jump josie_button_showroom.choice
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
