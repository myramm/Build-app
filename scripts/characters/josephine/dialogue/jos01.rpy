label jos01_find_josie:
    scene expression background(776, 464, 3.) as stage
    show josephine a_sides:
        offset (-175, 200)
    show anon f_shy_low with dissolve
    josephine f_surprised a_frustrated "{b}[firstname]{/b}?!"
    josephine "What are you doing here?"
    show josephine f_concerned a_sides
    show anon b_dressed_pickup
    with {'master': fastdissolve}
    anon "Looking for you."
    show anon b_onbed_sit f_normal with {'master': vpunch}:
        yoffset 250
    josephine "{i}*Gasp*{/i} Did you come to rescue me?"
    anon f_confused "Huh?"
    anon "Rescue you?!"
    josephine "My stupid father took my phone again and refuses to return it until all the paperwork in this filing cabinet is sorted."
    anon f_normal "What's so hard about that?"
    josephine "He wants it organized by date, manufacturer, model number, color, and customer information!"
    anon "Oh kay, that's a lot but still doable..."
    josephine @ f_eyeroll a_point_back "Yeah, but look at the size of this thing!"
    josephine f_angry_down a_sides @ f_angry_closed a_paper_angry "I'm gonna be stuck here forever!!!"
    anon @ f_laugh "Heh, no you won't..."
    josephine f_concerned "Hmm?"
    anon "C'mon, I'll help you."
    josephine f_normal "Really?"
    anon "Yeah, why not."
    anon "You saved me a ton of money on those cars I needed, and maybe I'll find some useful information..."
    show anon b_dressed_pickup with dissolve:
        yoffset 0
    pause .3
    hide anon with dissolve
    josephine @ f_eyeroll "I doubt it..."
    show josephine with slowdissolve:
        flip
        xoffset 150
    josephine "... It's just a bunch of dumb car paperwork."
    show anon b_dressed_pickup with dissolve:
        flip
    pause .3
    show anon b_onbed_sit with {'master': dissolve}:
        yoffset 250
    anon @ f_surprised "I bet the receipts from the cars the Russians' purchased are in there!"
    anon @ f_laugh "There might even be an address or some banking information..."
    josephine f_concerned "Why do you care so much about these Russians?"
    anon f_worried "Ehh, it's a long story."
    josephine f_normal "Well, it's not like I have anything else to do..."
    pause
    josephine "Spill it."
    anon "{i}*Sigh*{/i} Alright... But work and listen at the same time, yeah?"
    josephine f_angry "Ugh, fine."

    scene location_dealership_office_cutscene03
    show text _ ("I spent the next few hours organizing the dealership's receipts as {b}Josephine{/b} sat nearby, doing everything she could think of to avoid work...") as caption
    with fade
    pause
    hide caption with dissolve
    show text _ ("... It didn't really bother me though.\nShe may have been a terrible work partner but she was a surprisingly attentive audience.") as caption with dissolve
    pause
    hide caption with dissolve
    show text _ ("Offering condolences at my father's death and gasping when I told her about the constant harassment from the Russian Mafia.") as caption with dissolve
    pause

    scene expression background(776, 464, 3.) as stage
    show josephine a_sides:
        flip
        offset (150, 200)
    show anon a_receipts f_worried_low:
        flip
        yoffset 200
    with fade
    josephine "So this {b}Tony{/b} guy is just helping you out of the goodness of his heart?"
    anon "Yeah, so far."
    josephine "Hmm, sounds fishy to me..."
    josephine "He wants something from you, I bet."

    if M_anon.finished_state(S_ano11_init):
        anon f_worried "N-no, he doesn't..."
        anon f_worried_low "I mean-"
        josephine f_surprised "{i}*Gasp*{/i} He DID ask you for something!"
        anon f_hurt @ -m_talk "..."
        josephine f_sexy "What was it?!"
        anon f_worried_low "N-nothing."
        josephine "Oh, c'mon... I wanna know!"
        anon "I can't tell you."
        josephine f_concerned "Please?!"
        anon f_worried "No."
        josephine a_crossed f_bored @ f_eyeroll "Ugh, laaaaame!"
    else:
        anon f_worried "No, I don't think he wants anything from me..."
        anon "... {b}Tony{/b}'s just a nice guy."
        josephine f_concerned "Yeah, a nice ex-convict with mafia connections..."
        josephine f_normal @ f_eyeroll "I'm sure that's totally the case."
        anon @ f_laugh "Heh, it's true!"
        josephine f_bored "You are so naive..."

    show anon f_worried_low
    pause
    show josephine f_surprised
    pause .2
    hide josephine with dissolve
    anon "Hey, wait a second..."
    show anon b_dressed_pickup with dissolve
    pause
    anon b_dressed f_surprised_low a_receipts2 "!!!" with hpunch
    anon "This receipt has my dad's name on it!"
    show anon b_dressed_pickup with dissolve:
        unflip
        xoffset 500
    pause
    anon b_dressed f_surprised_low a_receipts_point "And so does this one!"
    pause
    anon "!!!"
    anon "All of these receipts have his name on them!"
    anon a_receipts2 "This one is dated just a few weeks before he died!"
    pause
    anon "He bought five black Abraham Town Cars..."
    anon f_surprised_down "... For three hundred and seventy-five thousand dollars?!?!"

    if M_rump.state is None:
        josephine "That's gotta be one of the Russian receipts."
        josephine "They always buy fancy black cars in bulk like that."
        anon f_worried_left "B-but, that doesn't make any sense..."
    else:
        josephine "Does that really surprise you?"
        josephine "You said he was laundering money for the mob, right?"
        anon f_worried_left "Y-yeah, I just wasn't prepared to find so much..."

    show anon f_worried a_receipts with {'master': dissolve}:
        flip
        xoffset -50

    if M_rump.state is None:
        anon "Why would my dad be-"
    else:
        anon "I mean, this is-"

    scene josephine b_chair f_sexy
    anon "!!!" with hpunch
    anon "What are you doing?!"
    josephine f_confused "Umm, getting comfortable?"
    josephine "Duh."
    anon "Y-you're naked..."
    josephine f_sexy @ f_laugh "Hehe!"
    josephine "See something you like?"
    anon "..."
    josephine "You can come and take a closer look, you know?"
    anon "{i}*Gulp*{/i} R-really?"
    josephine @ -m_talk "Mhmm."

    scene expression background(712, 400, 3.) as stage
    show josephine b_naked_sexy f_sexy:
        flip
        xoffset 150
    show anon f_flirt_low a_receipts:
        flip
        xoffset -50
    with fade
    josephine "Why don't you put those down and get your pants off?"
    anon f_worried "W-what, here in the office?"
    josephine @ -m_talk "Mhmm."
    josephine "I think we've earned a little break, don't you?"
    pause
    anon f_thinking_down "Do you think, maybe, I could make a copy of these first?"
    show anon f_surprised
    show josephine f_angry a_hips b_naked m_talk
    with fastdissolve
    josephine -m_talk "Dude, seriously?"
    josephine "I'm throwing myself at you here!!"
    anon f_worried "Y-yeah, I know... It's just-"
    josephine a_crossed @ -m_talk "..."

    if M_rump.state is None:
        anon "These might help me figure out what happened with my dad, you know?"
    else:
        anon "The police could probably use these in building my dad's case!"

    show josephine f_concerned
    pause
    josephine a_hips "Yeah, you're right."
    josephine "I'm sorry."
    anon "No, you don't have to-"
    josephine "You should just take them, {b}[firstname]{/b}."
    anon "Really?"
    josephine "Yeah."
    anon "Won't your father be mad?"
    josephine f_sexy @ a_gimme "He probably won't even notice..."
    josephine @ f_laugh "... And if he does, what's the worst that could happen?"
    josephine "We already know he won't fire me."
    show anon a_receipts_pocket f_flirt_low behind josephine with dissolve
    pause
    anon a_idle "Thanks, {b}Josephine{/b}."
    josephine "Yeah, yeah..."
    show josephine b_naked_jerk a_idle f_sexy_down with dissolve:
        xoffset -50
    josephine "... Can we screw now?"
    show josephine a_unzip2
    show anon a_surprised b_shirt
    with dissolve
    anon "!!!"
    josephine "All this paperwork has got me feeling very irritated and I need to blow off some steam."
    show josephine b_naked a_sides:
        xoffset 340
    show anon b_shirt od_dick3 f_flirt
    with dissolve
    show anon od_dick4
    anon "A-aren't you worried someone might come up here?"
    show anon od_empty f_flirt_low a_sides
    show josephine b_naked_jerk a_jerk:
        xoffset -50
    with dissolve
    josephine "They're not gonna come up here."

    if M_rump.state is None:
        josephine "Not with the mayor visiting."
    else:
        josephine "Not with the regional manager visiting."

    anon "I guess that's true."
    josephine "And even if they did..."
    josephine "... It's not like you have anything to be self-conscious about."
    show josephine b_naked_grab f_sexy:
        xoffset -450
    hide anon
    with {'master': dissolve}
    josephine "C'mon, bowl cut."
    anon "Please, stop calling me that..."
    hide josephine with {'master': dissolve}
    josephine "Hehehe!"

    call scene_josie_sex

    scene location_dealership_office_cutscene01
    sato "{b}Josephine?{/b}" with hpunch
    josephine "{b}Daddy{/b}?"
    anon "!!!"

    scene location_dealership_office_cutscene02 with fastfade
    anon "This isn't-"
    anon "I mean, we weren't-"
    sato "GET YOUR COCK OUT OF MY DAUGHTER!!!"
    pause

    scene expression background(712, 400, 3.) as stage
    show anon b_shirt f_worried a_empty od_dick1:
        flip
        xoffset 120
    show anon_arms_dressed_a_cover_boner:
        flip
        xoffset 120
    show josephine b_naked a_crossed f_angry:
        xoffset -100
    show sato f_angry:
        flip
        xoffset -70
    with fade
    josephine "What the fuck, {b}Dad{/b}?!"
    josephine "Haven't you ever heard of knocking?"
    sato "Not in my own office!"
    sato "What are you thinking?!"
    josephine "Umm, I was thinking this job is boring as fuck and my new boyfriend has an amazing dick!"
    sato @ f_surprised "W-what?!"
    josephine "You asked, {b}Daddy{/b}!"
    sato "That's not-"
    sato "Grr, you know what I meant!"
    anon "I should probably get going..."
    sato "You stay right there!"
    josephine @ f_angry_back "Stay there!"
    anon f_sad_down @ f_surprised "Oh kay..."
    sato a_crossed "This is unacceptable behavior young lady!"
    josephine "Pfft, what are you gonna do, fire me?!"
    sato "Oh, I bet you'd like that, wouldn't you?!"
    pause
    josephine f_angry_closed a_frustrated "You're the one who shut me away up here without my phone!"
    josephine "What did you think was gonna happen?!"
    show josephine f_angry
    sato "I thought you would do your job!"
    sato "Not to screw a customer on MY desk!!!"
    josephine "He's not just a customer, daddy!"
    josephine a_idle @ a_gimme "He's my boyfriend!"
    anon @ f_confused "Umm, boyfriend?"
    anon f_worried "I wasn't aware we were labeling-"
    josephine f_angry_back "Shut up, {b}[firstname]{/b}!!"
    anon f_sad_down @ f_surprised "Right, sorry."
    show josephine f_angry
    sato "I don't care if he's the King of England, you can't be doing stuff like this at work..."
    josephine "Hah!"
    josephine "Well, then you better fire me now, Daddy..."
    josephine "Because my boyfriend and I are gonna FUCK ALL OVER this stupid dealership!"
    josephine f_angry_back "Isn't that right, {b}[firstname]{/b}?"
    anon f_worried "Uhh..."
    pause
    anon "... I have no idea what you want me to say right now."
    show josephine f_eyeroll

    if M_kim.state is None:
        kim "{b}Mr. Sato{/b}?"
    else:
        yoyo "{b}Mr. Sato{/b}?"

    show josephine f_angry
    sato "Not now, {b}Kim{/b}!"
    sato "I'm dealing with a situation up here!"

    if M_kim.state is None:
        kim "Oh, ehh..."
    else:
        yoyo "Oh, ehh..."

    pause

    if M_rump.state is None:
        kim "... {b}Mayor Rump{/b} is leaving."
    elif M_kim.state is None:
        kim "... Regionar manager is leaving."
    else:
        yoyo "... Regionar manager is leaving."

    sato @ f_angry_closed a_facepalm "{i}*Sigh*{/i} Of course he is..."

    if M_rump.state is None:
        sato f_normal "Would you please just put some clothes on while I see the mayor out?"
    else:
        sato f_normal "Would you please just put some clothes on while I see my boss out?"

    sato "We'll discuss this when I return."
    josephine @ f_eyeroll "Yeah, whatever..."
    josephine a_gimme "... Give me my phone."
    show sato a_phone_pocket f_sad_down with dissolve
    pause .5
    sato a_phone_give f_normal "Here."
    show josephine a_phone f_normal_down
    show sato a_idle
    with dissolve
    pause
    sato "Please, don't do anything else until I get back."
    josephine "Yeah, we'll see."
    show sato f_sad_down with {'master': dissolve}:
        xoffset -600
        xzoom 1
    sato "{i}*Sigh*{/i}"
    hide sato with dissolve
    pause
    josephine @ -m_talk "..."
    hide anon_arms_dressed_a_cover_boner
    show anon a_sides:
        unflip
        xoffset 0
    with dissolve
    anon "{i}*Ahem*{/i}"
    anon "That was awkward..."
    josephine f_sexy "Heh, yeah."
    josephine "Sorry about that."
    show anon b_flour f_looking_down with dissolve:
        yoffset 110
    pause
    show anon b_dressed f_confused a_idle with dissolve:
        yoffset 0
    anon "So, I'm your boyfriend now?"
    josephine "As far as he's concerned, you are."
    anon "Right."
    anon "Okay."
    anon f_worried_left a_behind_head @ -m_talk "..."
    pause
    josephine f_bored "You should probably go."
    anon f_shy "Phew, yeah... I was gonna say..."
    josephine "Thanks again for helping me today."
    anon f_normal @ f_laugh a_wave "You're welcome."
    josephine "Sorry we didn't finish... You know..."
    anon "No worries."
    anon "I'll see you again soon."
    josephine f_normal_down "Okay."
    pause
    show josephine b_naked_mc_kiss_cheek f_surprised
    hide anon
    with dissolve
    pause
    show anon f_worried:
        xoffset 100
    show josephine b_naked
    with dissolve
    josephine f_concerned "What are you doing?"
    anon "I don't know."
    anon "I'm new at this..."
    show josephine f_eyeroll
    pause
    show josephine b_naked_kiss:
        xoffset -150
    hide anon
    with dissolve
    anon "!!!"
    pause
    show josephine b_naked a_idle f_sexy:
        xoffset -100
    show anon:
        xoffset 100
    with dissolve
    josephine "Now seriously, go."
    anon "Alright."
    hide anon with dissolve
    pause
    josephine @ -m_talk "..."
    show josephine f_normal_down a_phone with dissolve
    pause

    $ player.go_to(L_dealership_showroom)
    scene expression player.location.background_blur as stage with fade
    show anon f_worried with dissolve
    anon @ -m_talk "( Looks like the coast is clear. )"
    anon @ -m_talk "( I should hurry out of here before {b}Mr. Sato{/b} comes back. )"
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
