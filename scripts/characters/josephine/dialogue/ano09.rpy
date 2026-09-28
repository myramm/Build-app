label ano09_deal_josie:
    show anon with dissolve
    pause
    anon "Hey, {b}Josephine{/b}."
    josephine f_normal @ -m_talk "Hmm?"
    show josephine b_dressed a_phone with dissolve:
        xoffset 0
    josephine "Oh."
    josephine f_angry_down "Hey, bowl cut."
    josephine "I hope you're not here to buy another vehicle..."
    josephine @ f_eyeroll "My stupid father gave me a raise after you bought the last one."
    anon @ f_laugh "Really?"
    anon "Congratulations!"
    josephine "Yeah, whatever."
    anon @ f_skeptical "Still trying to get fired, huh?"
    josephine f_bored "{i}*Sigh*{/i} \"Trying\" being the operative word..."
    josephine "I've gotten thirty-six bad customer reviews!"
    anon f_worried @ f_shock "!!!"
    josephine "Infected every computer in the building with adware..."
    josephine "... Taken naps in the back of showroom cars during work hours."
    anon @ -m_talk "..."
    josephine "Yesterday, I set a small desk fire and the sprinkler system went off!"
    anon f_surprised "Holy crap."
    josephine @ f_normal "Heh, yeah, I know!"
    josephine "Didn't matter."
    josephine "He just took away my lighter and told me to get back to work."
    anon "That's crazy!"
    josephine f_normal_down @ f_concerned "Frankly, I'm running out of ideas."
    pause
    anon f_normal "You know, it really doesn't seem like a bad job to me..."
    anon "I mean, you mostly just sit around all day and play on your phone."
    josephine @ -m_talk "..."
    anon f_worried "What are you doing on that thing anyways?"
    josephine @ f_normal -m_talk "Hmm?"
    josephine "Oh, I'm watching fail compilations."
    anon f_confused "Fail compilations?"
    josephine "You know, one of those collections of clips wherein people hurt themselves attempting to do really stupid things."
    anon f_worried @ -m_talk "..."
    anon "And you enjoy watching that?"
    josephine "Of course."
    pause
    josephine f_concerned "Don't you?"
    anon "I don't know, I've never seen one."
    josephine "Seriously?"
    josephine f_normal "What, do you live under a rock or something?"
    anon "No."
    josephine "Well, come over here behind the desk and I'll show you."
    anon "Won't your dad get mad?"
    josephine f_normal @ f_eyeroll "Pfft, like I give a damn!"
    pause
    josephine "Oh, actually, we should get you a dealership vest!"
    josephine "Then you can answer the phone and deal with customers while I focus on more important things..."
    show josephine f_normal_down
    anon f_surprised @ f_confused "Wha-"
    josephine "... Like this autotuned cat remix."
    anon f_worried "I can't do that!"
    josephine "Sure you can."
    josephine "It's easy!"
    josephine "All you have to do is ignore them until they get pissed and go away..."
    josephine "... That's what I do."
    anon "Why would I ever agree to that?"
    josephine "C'mon, just humor me for a couple hours."
    anon "No way!"
    josephine f_sexy "I'll give you another car discount..."
    pause
    anon f_unimpressed "A nice car?"
    josephine f_normal_down "Sure, whatever."
    anon f_normal @ a_thinking f_thinking -m_talk "..."
    anon "Alright, fine."
    anon "Where's the vest?"
    josephine "{b}Just go up to my dad's office and grab one{/b}."
    anon "What if he's in there?"
    josephine "Tell him it's for me."
    anon "Yeah, okay."
    hide anon with dissolve
    return


label ano09_vest_josie:
    show anon with dissolve
    show josephine b_dressed a_phone with {'master': dissolve}:
        xoffset 0
    josephine "Dude, hurry up!"
    show anon f_worried
    josephine "If I have to do one more customer service call I swear I'm going to puke!"
    anon "Where did you say the vest was again?"
    josephine "{b}Just go up to my dad's office and grab one{/b}."
    anon "What if he's in there?"
    josephine "Tell him it's for me."
    show anon f_thinking a_thinking with dissolve
    pause
    anon f_laugh a_idle "Yeah, okay."
    hide anon with dissolve
    return


label ano09_blow_josie:
    show anon b_jacket with dissolve
    anon "Alright, I got the vest."
    show josephine b_dressed a_phone:
        xoffset 0
    show anon a_surprised f_grin
    with {'master': dissolve}
    anon "How does it look?"
    josephine "You look like a mindless worker drone, waiting to be crushed by the consumer culture of corporate America."
    anon f_worried a_idle @ -m_talk "..."
    josephine f_sexy "It's perfect!"
    josephine f_normal_down "Now come stand over here and watch funny videos with me."
    anon f_sad_down "{i}*Sigh*{/i} Okay..."
    show anon behind josephine:
        xoffset 350
    show josephine:
        xoffset 100
    with dissolve
    pause
    josephine a_phone_show_left "This one is called, \"Hold My Beer.\""
    anon f_worried_low "Oh kay."
    pause
    anon "Who's TurdBurglar93?"
    josephine f_sexy "That's my account name."
    anon f_skeptical "So you're a turd burglar?"
    josephine f_bored "No."
    josephine "This is just my troll account."
    josephine f_normal_down "Pay attention to the video"
    anon f_worried_low "Fair enough."
    pause
    show josephine f_sexy_down
    anon "Why is that guy standing on top of a moving car?"
    anon "And where are his pants-"
    anon f_surprised_low a_cover_boner3 @ a_up "OH MY GOD!"
    josephine @ f_laugh "Hahahaah!"
    anon f_disgusted_low "Eugh!"
    anon "I didn't know a penis could bend that way..."
    pause
    anon a_idle f_unimpressed "That's disgusting!"
    josephine "I think it's funny."
    anon f_disgusted "You gotta turn that off before I puke!"
    josephine a_phone f_normal "Alright, you big baby..."
    josephine "Hold on."
    pause
    josephine a_phone_show_left f_sexy_down "This one is called, \"What could go wrong?\""
    show anon f_worried_low
    pause
    anon "Okay, it's some old lady feeding bread to a bunch of geese?"
    josephine "Just wait for it..."
    pause
    anon f_shy_low @ f_laugh "Heh, one of them stole her sandwich."
    pause
    anon "Aww, he's cute!"
    anon f_surprised_low "Whoa, don't swat at it!"
    anon "What is she-"
    pause
    josephine @ f_laugh "Pfft, haha!"
    anon "Oh my god, the whole gaggle is attacking her..."
    anon "Run lady, run!"
    pause
    anon a_cover_boner3 "Not towards the pond!"
    josephine @ f_laugh "Hahahaah!!!"
    anon a_idle f_surprised_teeth_low @ -m_talk "!!!"
    anon @ f_laugh "Pfft, haha!"
    anon f_shy_low "She fell in!"
    josephine "Serves her right for hitting the goose."
    josephine "Never mess with geese, they'll fuck you up!"
    anon f_normal "Okay, that one was pretty funny."
    josephine "I told you."
    josephine a_phone "Here, I'll show you another..."
    anon "Alright."
    show josephine a_phone_show_left
    show anon f_shy_low
    with dissolve

    $ game.timer.tick(2)
    scene expression background(608, 512, 3.8) as stage
    show anon b_jacket f_worried_low:
        xoffset 350
    show josephine f_sexy_down a_phone_show_left:
        xoffset 100
    show xtra3 as counter at right
    with slowfade
    josephine "No, people only come here to argue about comic books and anime..."
    anon "And you just post things to annoy them?"
    josephine "Pretty much."
    anon "Uh huh."
    pause
    anon f_confused "Why?"
    josephine f_normal_down @ f_normal "Because..."
    pause
    josephine f_concerned "I dunno, actually..."
    pause
    josephine "Boredom, I guess?"
    show anon f_worried
    josephine "It's fun to see them get all pissed off over nerdy stuff."
    anon "You think comic books and anime are nerdy?"
    josephine @ f_eyeroll "Well, duh."
    anon "Oh."
    anon f_unimpressed "Whatever, I still enjoy them."
    josephine f_sexy "Yeah, I do too."
    show anon f_normal
    pause
    josephine a_idle "You know what, this was fun!"
    anon f_confused "What was?"
    josephine "Hanging out with you today."
    josephine "Pretty sure this is the first time I actually enjoyed being stuck at work."
    anon f_normal "Yeah, I had fun too."
    josephine "You should come back tomorrow and do it again!"
    anon f_worried a_behind_head "Oh, ehh, I dunno..."
    anon "I think there might be a limit to how many stupid internet videos I can watch on a cell phone in one week..."
    anon "Plus, I've got school and my job at {b}Tony's{/b}."
    josephine "I thought I smelled pizza."
    anon f_normal a_idle "Yeah."
    pause
    josephine "You know, there's other things we can do besides funny videos..."
    anon @ f_confused "What do you mean?"
    josephine "Hehe, lemme show you..."
    show josephine with MoveTransition(2):
        yoffset 100
    anon f_worried_low "Where are you going?"
    show josephine with MoveTransition(2):
        yoffset 300
    anon "{b}Josephine{/b}?"
    "{i}*Ziiiip*{/i}"
    anon f_surprised_low "W-what are you doing?"
    josephine "Whoa, Bowl cut..."

    scene location_dealership_indoor_sex_bj
    show josephine b_sex_bj_talk
    show josephine_office_bj_mc as overlay
    with fade
    josephine "You've been holding out on me!"
    josephine "Look at this big dick!"
    anon "Are you crazy?!"
    anon "We can't do this here!"
    josephine "Why not, it's nearly closing time and there's nobody around..."
    anon "But-"
    hide josephine
    $ M_josie.set('sex speed', .12)
    show josie_blowjob as animation behind overlay
    with dissolve
    pause
    anon "!!!"
    josephine "Mmm."
    pause
    anon "Oh my god."
    josephine "{i}*Sluuuuuuurp*{/i}"
    pause
    anon "I can't believe this is happening..."
    josephine "Hehehe!"
    pause

    scene expression background(608, 512, 3.8) as stage
    show anon b_jacket f_brag_closed:
        flip
    show josephine f_sexy_down a_phone_show_left:
        flip
        offset (400, 300)
        subpixel True
        block:
            ease .5 offset (425, 320)
            ease .5 offset (400, 300)
            repeat
    show xtra3 as counter at right
    with fade
    anon "Oh, don't stop."
    pause
    sato "{b}Josie{/b}?!"
    anon f_surprised a_up "!!!"
    anon f_surprised_low "I changed my mind, stop!"
    anon "Stop right now!"
    pause
    show josephine with MoveTransition(.2):
        reset
        flip
        offset (400, 300)
    josephine "But you haven't cum yet..."
    anon "Your dad is-"
    show josephine f_sexy_down a_phone_show_left with hpunch:
        offset (425, 320)
    josephine "Nom!{w=.4}{nw}"
    show josephine:
        subpixel True
        block:
            ease .5 offset (400, 300)
            ease .5 offset (425, 320)
            repeat
    show anon f_brag_closed
    josephine "Nom!{fast}"
    anon "Oh, god."
    pause
    show sato f_confused:
        flip
        xoffset -100
    with dissolve
    sato "Who are you and where's my daughter?{w=.25}{nw}"
    show anon f_surprised_teeth:
        subpixel True
        xoffset -100
    show josephine:
        subpixel True
        offset (300, 400)
    with {'master': MoveTransition(.6)}
    sato "Who are you and where's my daughter?{fast}"
    josephine "{i}*Glllcck*{/i}"
    anon f_worried_left a_behind_head "Oh, umm... H-hi, there."
    anon f_worried "I'm your daughter's friend, {b}[firstname]{/b}."
    sato a_hips f_angry "I told her not to leave this desk unattended."
    sato "Why isn't she here?"
    anon f_worried_low "Uhh..."
    anon f_worried "S-she just stepped away to use-"

    scene location_dealership_indoor_sex_bj:
        align (1., .2)
        zoom 3
    $ M_josie.set('sex speed', .09)
    show josie_blowjob as animation
    show josephine_office_bj_mc as overlay
    with fade
    anon "Haah!"
    sato "To use?"
    anon "Hmm?"
    anon "Oh, sorry."
    anon "I think she's in the bathroom, sir."
    sato "Did she put you in that vest?"
    anon "Y-yes, sir."
    sato "Well, take it off."
    sato "I could get in trouble if someone mistakes you for an employee."
    anon "Will do."
    pause
    josephine "{i}*Glllcck*{/i}"
    sato "Did you hear something?"
    anon "N-no, sir."
    pause

    scene expression background(608, 512, 3.8) as stage
    show anon b_jacket f_worried:
        flip
        xoffset -100
    show josephine:
        flip
        offset (300, 400)
    show xtra3 as counter at right
    show sato a_hips:
        flip
        xoffset -100
    with fade
    sato "I hope she's not going to take long, I need her help closing down."
    anon "Heh, yeah."
    pause
    anon @ f_brag_closed "This is crazy..."
    sato "What did you say?"
    anon "Uhh, I said, she's probably just being lazy..."
    anon f_hurt a_up "Ouch!!" with vpunch
    anon f_worried_low "Watch the teeth-"
    sato f_confused "Are you alright, son?"
    anon a_idle f_worried "Hmm?"
    anon "Oh, Y-yeah... I just stubbed my toe is all."
    sato @ -m_talk "..."
    anon "Now that you mention it, she has been gone a while..."
    anon "You should probably go check on her."
    sato "She'd better not be in there masturbating again!"
    sato @ a_point "Don't touch anything, alright?"
    anon f_normal "Of course not, sir."
    hide sato with dissolve
    pause
    show anon f_surprised_low:
        subpixel True
        xoffset 0
    show josephine:
        subpixel True
        offset (400, 300)
        block:
            ease .5 offset (425, 320)
            ease .5 offset (400, 300)
            repeat
    with {'master': MoveTransition(.8)}
    anon "Okay, seriously, you have to sto-"

    call scene_josie_blowjob from ano09_blow_josie.resume
    $ unlock_scene('josie', '01_unlocked')

    scene expression background(608, 512, 3.8) as stage
    show anon b_jacket f_brag_closed:
        flip
    show josephine:
        flip
        offset (400, 300)
    show xtra3 as counter at right
    with fade
    anon "Phew."
    anon "I can't believe you did that..."
    show anon f_flirt with dissolve:
        xoffset 100
    show josephine f_sexy o_cum with dissolve:
        offset (350, 0)
    pause
    josephine "I can't believe you're so well equipped!"
    josephine "We are definitely gonna hang out more often."
    anon "Yeah, okay."
    pause
    anon f_worried @ a_schmutz "You know, you've got a little something..."
    josephine @ f_laugh "Yeah, no shit."
    josephine "Dude, you came a lot!"
    anon "Your dad is going to be back any second."
    josephine "Hehe, I know."
    sato "There you are!"
    josephine "Speak of the devil..."
    show anon f_worried
    show sato f_angry a_hips with dissolve:
        flip
    sato "I thought you said she was in the bathroom?"
    show josephine f_normal with dissolve:
        unflip
        xoffset -150
    josephine @ f_eyeroll "Relax, dad..."
    josephine "I had to get my phone out of the break room."
    sato "What's that all over your face?"
    show anon f_hurt
    josephine f_sexy "It's just lotion."
    josephine "My face has been really dry recently."
    show anon f_worried
    sato "Well, clean yourself up a bit."
    sato "You look ridiculous."
    anon @ -m_talk "..."
    josephine f_bored "Real nice, dad!"
    sato "And send your little friend home so we can close up."
    josephine @ f_eyeroll "Ugh, whatever."
    hide sato with dissolve
    show josephine with dissolve:
        flip
        xoffset 350
    josephine f_sexy "So you'll come back tomorrow?"
    anon f_normal "Yeah, I suppose."
    anon "I still need that new car, you know?"
    josephine "No worries, I'll hook you up."
    anon @ f_laugh "Awesome!"
    hide anon with dissolve
    return


label ano09_sale_josie:
    show anon with dissolve
    label ano09_sale_josie.anon:
    anon f_normal "New car time! What did you have in mind?"
    josephine f_normal "This is our most popular mid-range sport vehicle."
    josephine "The Overcompensator."
    anon @ f_skeptical "Why do they call it that?"
    josephine f_bored @ -m_talk "..."
    josephine "Do you seriously not know the answer to that question?"
    anon f_shy @ a_behind_head "Ehh, heh... N-no, I'm just joking."
    josephine @ f_eyeroll "Very funny."
    pause
    josephine "It has a retail value of thirty-two thousand."
    anon f_shock "Thirty-two thousand?!"
    anon "I can't afford that!"
    show anon f_surprised_teeth
    josephine f_sexy "You're lucky I like you..."
    josephine "I can take it as low as fifteen thousand."
    josephine "And with your trade in, we could call it an even ten thousand."
    anon a_thinking f_thinking "Ten thousand, huh?"
    anon f_worried a_idle "I might be able to swing that..."
    josephine f_normal "So, you want it or not?"
    show anon f_thinking a_thinking with dissolve

    menu:
        "Yes. ($10,000)":
            jump ano09_sale_josie.deal
        "Maybe later.":

            pass

    anon a_thinking f_worried "I'll have to think about it."
    josephine @ f_eyeroll "Great."
    hide josephine
    show josephine b_dressed_sleeping behind anon
    show anon f_worried_low
    with {'master': dissolve}
    josephine "Take your time, bowl cut."
    josephine "It's not like I'm going anywhere..."
    hide anon with dissolve
    return


label ano09_sale_josie.deal:
    if player.has_money(10000):
        anon f_normal @ f_laugh "I'll take it!"
        josephine @ f_eyeroll "Super."
        show anon a_money with dissolve
        pause
        anon a_idle "You think your dad will give you another raise for this?"
        josephine @ f_eyeroll "I dunno, probably."
        pause
        josephine "I'd rather he give me more vacation days so I can get the hell out of this place..."
        show josephine a_phone f_normal_down with dissolve
        anon "Alright."
        anon "Well, thanks again!"
        hide anon with dissolve
        return 'coupe_key'
    else:
        anon f_worried "I'll be back to get it as soon as I have the money."
        josephine @ f_eyeroll "Great."
        show josephine f_normal_down a_phone
        show anon f_worried_low
        with {'master': dissolve}
        josephine "It's not like I'm going anywhere..."
        hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
