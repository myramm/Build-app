label button_eve_sexy_time:
    scene expression player.location.background_blur with None
    show anon with dissolve
    anon "Hey, you."
    eve "!!!"
    show eve b_undies f_happy
    with dissolve
    eve "I've been waiting for you!"
    anon "Oh?"
    anon "What's goin-"
    hide anon
    show eve b_undies_kiss
    with dissolve
    anon "!!!"
    pause
    show anon
    show eve b_undies f_happy
    with dissolve
    anon "Heh, you just wanna get right into it, huh?"
    eve f_sexy "Yes!"
    pause
    eve "Get on the bed."
    anon @ a_behind_head "O-okay."
    scene expression player.location.background_closeup with None
    show anon b_onbed_sit f_flirt
    show eve f_sexy b_onbed_top_remove3 with dissolve
    with dissolve
    pause
    show eve b_onbed_top_remove4 with dissolve
    pause
    show eve f_sexy b_onbed_nude with dissolve
    pause
    show anon b_onbed_sit_changing3 with fastdissolve
    pause
    hide anon
    show eve b_onbed_cuddle_naked_kiss o_dick
    with dissolve
    eve "Mmm."
    show eve b_onbed_cuddle_naked f_happy
    show anon b_empty_eve_onbed_cuddle f_flirt_low zorder 1
    with dissolve
    pause
    anon "Wow, you are really aggressive tonight!"
    eve "Hehe, sorry."
    pause
    eve "You know, {b}[firstname]{/b}, I've been thinking..."
    pause
    eve "... You're like, the most amazing person in the world."
    anon "I dunno about that..."
    eve "No, I'm serious!"
    eve "You're smart, funny, kind, thoughtful..."
    pause
    eve "And really, REALLY, hot!"
    anon "Haha, you think I'm hot?"
    eve "Duh!"
    pause
    eve "A-and I want you to be my first..."
    anon f_worried_low "Your first?"
    pause
    anon "Your first what?"
    eve @ f_thinking_down "Tch."
    eve "I'm asking if you wanna have sex with me, {b}[firstname]{/b}..."
    anon @ f_surprised "!!!" with hpunch
    anon "Really?!"
    eve f_thinking_down "I mean, we don't have to... I just thought-"
    anon f_flirt_low "Of course I do!"
    eve f_happy "Yeah?"
    anon "Definitely."
    eve "Hehe, good!"
    $ M_eve.set('sex speed', .4)
    show eve a_jerk o_empty with dissolve
    pause
    anon "Right now?"
    eve "Right now."
    anon "{i}*Gulp*{/i} Okay."
    jump eve_sex_back_first_intro

label button_eve_maybe_another_time:
    anon f_worried "I'd love to but I'm so far behind in my classes... It's probably a bad idea."
    eve f_sad_down "Yeah, I understand."
    pause
    eve f_happy "We'll do it another time."
    anon f_normal "For sure."
    return

label button_eve_nevermind_roof:
    anon f_worried "I should probably get home."
    eve f_normal "It was nice seeing you, {b}[firstname]{/b}."
    anon "Yeah, you too."
    eve "Later."
    anon @ a_wave "Bye, {b}Eve{/b}."
    hide anon with dissolve
    return

label button_eve_ill_be_there:
    anon "I'll be there."
    eve @ f_laugh "Yay, hehe!"
    eve f_sexy "We can go into my room and have some {i}alone time{/i}, if you know what I mean?"
    anon f_flirt "Alone time, huh?"
    eve @ -m_talk "Mmhmm."
    anon "I like the sound of that."
    eve "I thought you might."
    return

label button_eve_how_are_odette_and_grace:
    anon "How are {b}Odette{/b} and {b}Grace{/b}?"
    eve "Oh, they're doing great!"
    eve "{b}Grace{/b} has a lot more free time since {b}Odette{/b} started helping out, and we've actually been spending time together {b}in the evenings{/b}."
    anon @ f_laugh "That's wonderful!"
    eve "Yeah, it is."
    eve @ f_eyeroll "Now if I could just get them to stop having sex all over the house, things would be perfect."
    anon f_surprised "S-sex?"
    eve @ f_eyeroll "Yeah, I mean, literally everywhere... And they have no shame!"
    eve f_angry "Yesterday I walked in on my sister licking {b}Odette{/b}'s dirty snatch in our kitchen!"
    anon f_flirt "R-really?"
    eve "She had her bare ass up on the counter and everything!"
    anon "{i}*Gulp*{/i} That sounds... Umm... Annoying?"
    eve "It's super annoying."
    eve "I used to eat my pop-tarts there!"
    eve f_sad "{i}*Sigh*{/i}"
    eve "Not anymore..."
    show anon f_flirt_grin
    pause .5
    show anon f_normal
    return

label button_eve_nah_i_like_to_watch_you:
    anon f_worried "Nah, I like to watch you."
    eve f_surprised "You like to watch me, huh?"
    anon f_normal "It's fun."
    eve f_sexy "You know, out of context, that sounds really dirty..."
    anon f_confused @ -m_talk "Hmm?"
    eve @ f_laugh "Hehe, never mind."
    eve "Come sit down."
    show anon f_normal
    eve "I'm about to rank up my {b}Cindel{/b}."
    anon @ f_confused "Is that the girl with the four arms?"
    eve "No, it's the one who screams and has hair like {b}Odette{/b}."
    anon "Oh, right."
    anon @ f_laugh "Cool!"

    scene location_tattoo_bedroom_cutscene06
    show text _ ("It was fun watching {b}Eve{/b} beat up on someone else for a change...\nShe almost never lost a match.") as caption
    with fade
    pause
    hide caption with dissolve
    show text _ ("Those online players didn't stand a chance against her!") as caption with dissolve
    pause

    scene expression player.location.background_blur
    show anon
    show eve b_undies f_happy
    with fade
    eve "What am I at now?"
    anon "Fifty-three wins and two loses..."
    eve f_surprised "Fifty-three?!"
    eve f_normal "Oh my god, what time is it?"
    anon "It's half past ten."
    eve f_happy @ f_eyeroll "Aww, man... I completely lost track of time!"
    anon "Yeah, I should probably start heading home."
    eve f_sad_down "I'm sorry we didn't do anything naughty..."
    anon "That's okay."
    anon "I had fun watching you beat up people online!"
    eve f_sad "I'll make it up to you next time, okay?"
    anon @ f_laugh "Sure, can't wait!"
    eve f_happy @ f_laugh "Hehe!"
    hide anon
    show eve b_undies_kiss1
    with dissolve
    pause
    show eve b_undies
    show anon
    with dissolve
    eve "I'll see you tomorrow?"
    anon "Of course."
    eve "Goodnight, {b}[firstname]{/b}."
    anon @ a_wave "Goodnight, {b}Eve{/b}."
    hide anon with dissolve
    return

label button_eve_i_should_go:
    anon f_worried "Crap, I just remembered."
    eve @ -m_talk "Hmm?"
    anon "I'm supposed to be somewhere."
    eve f_sad "You're leaving?"
    anon "Yeah, sorry."
    anon "Rain check on the alone time?"
    eve f_sad_down "Y-yeah, okay."
    anon "Thanks."
    hide anon
    show eve b_undies_kiss1
    with dissolve
    pause
    show eve b_undies
    show anon
    with dissolve
    anon "You look amazing by the way!"
    eve f_happy @ f_laugh "Hehe, thanks!"
    anon @ a_wave "I'll catch you later, okay?"
    eve "See ya, {b}[firstname]{/b}."
    hide anon with dissolve
    return

label button_eve_how_come_not_at_the_park:
    anon "How come you're not at the park?"
    eve f_sad_down @ f_eyeroll "{b}Grace{/b} doesn't want me there after dark anymore."
    anon f_worried "Oh."
    anon "The drug thing?"
    eve "Yeah."
    pause
    eve f_normal @ a_point "On the bright side, I don't have to worry about {b}Tyrone{/b} and his douchebag friends annoying me here."
    anon @ f_laugh "Heh, that's true."
    eve "Maybe I can actually get some drawings done."
    return

label button_eve_business_doing_any_better:
    anon "Business doing any better?"
    eve f_happy "Yeah, those flyers were a huge hit!"
    eve "We've had a lot more customers coming in since you handed them out."
    anon "That's wonderful!"
    return

label eve_dialogue_intro_roof:
    scene expression player.location.background_closeup with None
    show anon
    show eve
    with dissolve
    anon "{b}Eve{/b}?"
    eve @ f_laugh "Hey, {b}[firstname]{/b}!"
    hide eve
    show anon b_hug_eve f_shy_down
    with dissolve
    pause
    show anon b_dressed f_normal
    show eve f_happy
    with dissolve
    anon "What are you doing up here?"
    eve "Oh, just people watching..."
    anon "Find anything interesting?"
    eve f_normal @ f_eyeroll "No, not really."
    eve "Ugh, this town is so boring sometimes..."
    return

label button_eve_art_project:
    anon "So {b}Miss Ross{/b} was happy with the drawing we made together?"
    eve f_happy @ f_laugh "Yup, she loved it!"
    eve "Gave me this long speech about how proud she was to have helped me find my inner beauty..."
    anon @ f_confused "That's umm... Great?"
    eve "I'm just glad it's finally over and I can draw something other than self-portraits for a while!"
    eve @ f_eyeroll "I swear, that woman is nuttier than squirrel poop!"
    anon @ f_laugh "{i}*Snort*{/i} Haha!"
    return

label button_eve_hows_everyone_at_home:
    anon "How's everyone at home?"
    eve f_normal "Oh, you know... Same old, same old."
    eve "{b}Grace{/b} is working herself too hard and freaking out about bills."
    eve "{b}Tuuku{/b} is doing his best to make sure all the pot heads in Summerville are getting their fix."
    eve "And {b}Odette{/b} bought the entire series of {i}False Blood{/i}, and has been binge-watching it in the shop every day."
    anon f_surprised "{i}False Blood{/i}?"
    eve @ f_eyeroll "Yeah, it's some show about sexy vampires."
    eve "TONS of nudity so, of course, she loves it."
    anon f_flirt "Yeah, that makes sense."
    show anon f_normal
    return

label button_eve_something_simple:
    anon @ f_confused "Something simple?"
    eve "Last time she made us paint a picture using only our feet."
    anon f_surprised "Seriously?"
    eve @ f_eyeroll "Yeah, she said it would open our chakras and bring balance to our souls or some nonsense..."
    eve "I think she just has a foot fetish."
    anon f_normal @ f_laugh "Haha!"
    return

label button_eve_you_look_nice_today:
    anon f_flirt "You look nice today!"
    eve @ f_eyeroll "Shut up."
    anon f_normal "I'm serious!"
    eve "But I'm wearing the exact same thing I always wear..."
    anon "Yeah, and you always look nice!"
    eve f_nervous_down "Come on, stop it..."
    anon "It's the truth!"
    return

label button_eve_nevermind_park:
    anon f_worried "I should probably get home."
    eve f_normal "Yeah, I'll be doing the same myself, shortly."
    anon "Be careful out here, okay?"
    eve "I will be."
    anon @ a_wave "Later."
    hide anon with dissolve
    return

label button_eve_should_find_a_new_spot:
    anon f_confused "Have you considered finding a new spot to hang out?"
    eve f_angry "Why should I be the one that leaves?"
    eve f_angry_right "I was here first!"
    show anon f_worried
    chico "Now she all mad..."
    chad "Haha!"
    tyrone "Why don't you bring your fine ass over here and split a doobie with us?"
    eve "Fuck you!"
    tyrone "Yeah, I bet you'd like that, huh?"
    tyrone "We can run a train on you all night long."
    show anon f_shock
    eve @ f_disgusted_wince_down "Eugh."
    eve "You're disgusting!"
    show eve f_angry
    anon @ -m_talk "..."
    show anon f_worried
    return

label button_eve_hallway_really:
    anon f_worried "Really?"
    eve "Yeah, I'd like to but my sister will kill me if she finds out, so..."
    eve f_nervous "... Probably not a good idea."
    anon f_normal @ a_behind_head "Hehe, yeah... Probably not."
    return

label button_eve_nevermind_school:
    anon f_normal "I should probably get ready for class."
    eve f_normal "Yeah, me too."
    anon "I'll talk to you later, okay?"
    eve "Yup, later."
    hide anon with dissolve
    return

label button_eve_how_are_things_at_the_shop:
    anon f_normal "How are things at the shop?"
    eve "Mm, things are good, I guess..."
    pause
    eve f_nervous_down "I wish {b}Grace{/b} didn't have to work so much but there's nothing to be done."
    show anon f_worried
    eve "We can't afford to hire anybody, and she refuses to let me help out!"
    anon "Yeah, that sucks."
    return

label button_eve_street_kombat_rematch:
    anon f_snarky "I still want that rematch!"
    eve f_normal "Hey, I'm down to kick your butt anytime you want..."
    anon "Nah, I'll definitely get you next time!"
    eve @ f_laugh "Hehe, sure you will."
    return

label button_eve_you_still_drawing:
    anon f_normal "You still drawing?"
    eve @ f_eyeroll "Ugh, I've mostly been focusing on this stupid project for {b}Miss Ross{/b}..."
    anon "Oh, yeah?"
    eve "I've turned in like six different drawings, and she keeps making me redo it!"
    anon f_surprised "Seriously?"
    eve "Yeah, that woman is nuts!"
    pause
    anon f_normal "Is there anything I could do to help?"
    eve "Nah, I appreciate the offer but there's nothing to be done."
    eve f_sad_down "I might just drop her class..."
    anon f_shock "What?!"
    anon f_worried "But I thought you loved drawing?"
    eve "I do, but she's taking all the fun out of it..."
    anon @ -m_talk "..."
    return

label button_eve_love_the_hair:
    anon f_normal "Have I mentioned I love your new hair?"
    eve a_hair f_nervous_down "Hehe, yes... Yes, you have."
    anon "It looks so good on you!"
    eve "Thanks, {b}[firstname]{/b}."
    eve f_normal a_idle @ f_happy_right "It feels really good to hear that!"
    return

label eve_dialogue_intro_bedroom:
    scene expression player.location.background_closeup with None
    show anon
    with dissolve
    anon "{b}Eve{/b}?"
    show eve b_undies f_happy
    with dissolve
    eve "{i}*Gasp*{/i} You're here!"
    hide anon
    show eve b_undies_kiss
    with dissolve
    pause
    show eve b_undies
    show anon
    with dissolve
    anon "Heh, I'm here."
    anon "You playing games?"
    eve @ -m_talk "Hmm?"
    eve "Oh, I was just doing some {i}Street Kombat{/i} online matches."
    anon "Can I watch?"
    eve @ f_eyeroll "Umm, yeah... I guess."
    eve f_sexy "Wouldn't you rather do something else?"
    return

label eve_dialogue_intro_classroom_e1e12:
    scene expression player.location.background_closeup with None
    show eve b_desk_look_left:
        xoffset 500
    show anon b_desk
    with dissolve
    anon "Morning, {b}Eve{/b}."
    eve "Hey, {b}[firstname]{/b}."
    anon "Working hard?"
    eve "Heh, yea right..."
    eve @ f_eyeroll "This class is SO boring!"
    return

label eve_dialogue_intro_classroom_e13e20:
    scene expression player.location.background_closeup with None
    show eve b_desk_look_left:
        xoffset 500
    show anon b_desk
    with dissolve
    anon "Morning, {b}Eve{/b}."
    eve "Hey, {b}[firstname]{/b}!"
    anon "Ready for another fun day of school?"
    eve @ f_eyeroll "Heh, yeah... \"Fun.\""
    eve "I wish we could just skip and hang out at my place."
    anon "Yeah, me too."
    return

label eve_dialogue_intro_classroom_e21:
    scene expression player.location.background_closeup with None
    show eve b_desk_look_left:
        xoffset 500
    show anon b_desk
    with dissolve
    anon "Morning, {b}Eve{/b}."
    eve "Hey, {b}[firstname]{/b}!"
    hide anon
    show eve b_dressed_kiss:
        xoffset -300
    show expression "characters/eve/eve_overlay_o_chair.png" zorder 1:
        xpos 450
    show expression "characters/eve/eve_overlay_o_desk.png" zorder 2:
        xpos 500
    show expression "characters/eve/eve_overlay_o_chair.png" as anon_chair zorder 1:
        xpos -50
    show expression "characters/eve/eve_overlay_o_desk.png" as anon_desk zorder 3:
        xpos 0
    with dissolve
    pause
    eve "Mmm."
    hide eve
    hide anon_desk
    hide anon_chair
    hide expression "characters/eve/eve_overlay_o_desk.png"
    hide expression "characters/eve/eve_overlay_o_chair.png"
    show eve b_desk_look_left f_happy:
        xoffset 500
    show anon b_desk f_flirt
    with dissolve
    anon "Mmm, that was nice."
    eve @ f_laugh "Hehe!"
    eve @ f_eyeroll "Ugh, I'm so not in the mood for class today."
    eve "You wanna skip with me?"
    anon f_worried "I dunno, maybe."
    eve "Aww, c'mon... Please?"
    eve "It's so boring when you're not around!"
    return

label eve_dialogue_intro_hallway_e1e12:
    scene expression player.location.background_closeup with None
    show anon
    show eve
    with dissolve
    anon @ a_wave "Afternoon, {b}Eve{/b}."
    eve @ a_wave "Hey, {b}[firstname]{/b}."
    anon "What's going on?"
    eve f_nervous_down "Ehh, not much."
    eve "Just thinking about skipping {b}Miss Ross{/b}' class..."
    return

label eve_dialogue_intro_hallway_e13e20:
    scene expression player.location.background_closeup with None
    show anon
    show eve
    with dissolve
    anon @ a_wave "Afternoon, {b}Eve{/b}."
    eve "Hey, {b}[firstname]{/b}!"
    hide eve
    show anon b_hug_eve f_shy_down
    with dissolve
    pause
    show anon b_dressed f_normal
    show eve f_happy
    with dissolve
    anon "You heading to {b}Miss Ross{/b}' class?"
    eve f_normal "Unfortunately, yes."
    eve "Man, I hope she has something simple planned today..."
    return

label eve_dialogue_intro_hallway_e21:
    scene expression player.location.background_closeup with None
    show anon
    show eve f_happy
    with dissolve
    anon @ a_wave "Afternoon, {b}Eve{/b}."
    eve "Hey, {b}[firstname]{/b}!"
    hide anon
    show eve b_dressed_kiss:
        xoffset -400
    with dissolve
    pause
    show eve b_dressed:
        xoffset 0
    show anon
    with dissolve
    anon "Mmm, that was nice."
    eve @ f_laugh "Hehe!"
    eve "Are you coming over tonight?"
    anon "I dunno, maybe."
    eve @ f_eyeroll "Aww, c'mon... Please?"
    eve "It's so boring when you're not around!"
    return

label eve_dialogue_intro_park_e1e12:
    scene expression player.location.background_closeup with None
    show anon f_worried with dissolve
    anon "{b}Eve{/b}?"
    pause
    anon f_angry "Can you hear me?!"
    eve "Hmm?"
    eve "Oh, hey {b}[firstname]{/b}!"
    show anon f_shock
    show eve b_dressed_headphones_up with dissolve
    show anon f_normal
    pause
    show eve b_dressed_hoodless a_hoodless_remove_headphones with dissolve
    eve "Sorry."
    show eve b_dressed_headphones_down a_idle with dissolve
    anon "Am I interrupting you?"
    eve "No, not at all."
    eve @ f_eyeroll "I'm just trying to drown out this shitty rap music!"
    tyrone "Psh, don't play girl... You know you love it!"
    eve f_angry_right "Fucking assholes..."
    eve f_normal "So, what's up?"
    return

label eve_button_eve_six6nine9_time:
    scene expression player.location.background_closeup with None
    show anon with dissolve
    anon "Hey, you."
    eve "!!!"
    show eve b_undies f_happy
    with dissolve
    eve "Hey, {b}[firstname]{/b}!"
    anon "You playing games?"
    eve "Yeah."
    pause
    eve f_sexy "But now that you're here..."
    hide anon
    show eve b_undies_kiss
    with dissolve
    anon "!!!"
    pause
    show anon
    show eve b_undies f_happy
    with dissolve
    eve "Do you remember that night in the tent... When you, umm-"
    eve "... Made me cum?"
    anon f_flirt "Yeah?"
    eve "Could we, maybe... Do that again?"
    menu:
        "Sure, I guess.":
            anon a_thinking f_thinking "Hmm, let me think about it."
            eve f_nervous @ -m_talk "..."
            show anon f_flirt_grin a_idle with dissolve
            pause
            anon f_flirt @ a_point "Of course we can!"
            eve f_sexy @ f_laugh "Hehe!"
            eve "Get on the bed, {b}[firstname]{/b}."
        "HELL YES!":

            anon @ f_laugh "Oh, we can do whatever you want {b}Eve{/b}!"
            eve "Hehe, alright."
            eve f_thinking_down "Hmm."
            pause
            eve f_sexy "Why don't I grab some of my sister's massage oil, and we'll see how much stuff we can fit up your butt?"
            anon f_shock "!!!"
            anon f_worried "T-that's not-"
            anon "I didn't mean-"
            eve @ f_laugh "Hahaha!!"
            eve "I was just joking... Man, you should have seen your face!"
            anon f_shy @ a_behind_head "Very funny."
            eve "Get on the bed, {b}[firstname]{/b}."

    anon "Alright."
    scene expression player.location.background_closeup with None
    show anon b_onbed_sit f_flirt
    show eve b_onbed_tanktop f_sexy
    with dissolve
    eve "I don't think I need these clothes anymore, do you?"
    anon "Nuh uh."
    eve @ f_laugh "Hehe."
    show eve b_onbed_top_remove3 with dissolve
    pause
    show eve b_onbed_top_remove4 with dissolve
    pause
    show eve f_sexy b_onbed_nude with dissolve
    eve "There."
    eve "Your turn."
    show anon b_onbed_sit_changing3 with fastdissolve
    pause
    hide anon
    show eve b_onbed_cuddle_naked_kiss o_dick
    with dissolve
    pause
    show eve b_onbed_cuddle_naked f_happy
    show anon b_empty_eve_onbed_cuddle f_flirt_low zorder 1
    with dissolve
    eve "Mmm, I love kissing you!"
    anon "Y-yeah, likewise."
    pause
    $ M_eve.set('sex speed', .4)
    show eve a_jerk o_empty with dissolve
    eve f_thinking_down "I can't even get my fingers all the way around your dick!"
    anon "I'm telling you, it's just your small hands."
    eve f_happy "Hehehe, I dunno about that..."
    pause
    eve "Can we try something?"
    anon "Umm, I dunno..."
    anon "I guess it depends on what it is?"
    show eve a_jerk1
    eve "Don't worry, it's nothing weird..."
    anon "A-aright?"
    eve "Have you ever heard of the sixty-nine position?"
    if M_eve.get("biggus_dickus"):
        eve "I'll get on top of you and we'll both use our mouths."
        anon "You wanna put your dick in my mouth?"
    else:
        eve "I would get on top of you and take you in my mouth, while you use your tongue on me."
        anon "You want me to lick your pussy?"
    eve "Well, only if you want to?"
    anon @ -m_talk "..."
    eve "If it freaks you out, I can just go down on you like normal?"
    return

label eve_button_party_start:
    scene expression player.location.background_closeup with None
    if player.location != L_school_frenchclassroom:
        show eve f_happy
        show anon
    else:
        show eve b_desk_look_left f_happy:
            xoffset 500
        show anon b_desk
    with dissolve
    eve "You're still coming to the party {b}this Saturday evening{/b}, right?"
    anon "Yeah, I'll be there."
    eve "It's going to be so awesome!"
    eve "My sister and {b}Odette{/b} throw the best parties!"
    anon @ f_laugh "Hehe, can't wait!"
    return

label eve_button_talked_to_eve:
    scene expression player.location.background_closeup with None
    show anon a_beer
    show eve a_beer_hold
    with dissolve
    eve "I wonder what's taking {b}Odette{/b} so long?"
    anon "She said she was closing up shop, right?"
    show anon a_beer_drink f_smoke with dissolve
    eve "Yeah, but {b}Grace{/b} only had like two customers today..."
    show anon a_beer f_normal with dissolve
    eve "It shouldn't take her this long."
    hide anon with dissolve
    return

label eve_button_eve_talked_to_both_girls:
    odette "Alright, bitches..."
    scene expression player.location.background_blur
    show odette a_whiskey_yay f_laugh zorder 1:
        xoffset 100
    with fade
    odette "Who's ready to party?!"
    show anon a_beer zorder 1:
        xoffset -150
    show eve f_happy a_beer_hold zorder 0:
        flip
        xoffset 100
    show grace a_beer f_normal_back zorder 0:
        xoffset -150
    with dissolve
    odette f_moo "WOOOOO!!!"
    eve f_happy @ f_moo "WOOOOO!!!"
    show odette f_smirk a_whiskey with dissolve
    grace "Just don't go too crazy, please..."
    odette "Uh oh, sounds like somebody needs a shot of fireball!"
    grace f_sad @ f_surprised_back "Absolutely not!"
    eve f_sad "Aww, c'mon {b}Grace{/b}..."
    show grace f_sad_back
    odette "Yeah, c'mon {b}Grace{/b}!"
    odette "Don't be a party pooper!"
    grace "{i}*Sigh*{/i} Fine, give it here..."
    show eve f_happy
    show odette a_whiskey_pour with dissolve
    odette "That's my girl!"
    show odette a_whiskey
    show grace a_shot_drink f_proud m_talk
    with dissolve
    odette "Drink your medicine."
    show grace a_shot f_disgusted_wince -m_talk with dissolve
    grace "Eugh, god..."
    grace "{i}*Cough* *Cough*{/i}"
    grace f_happy "Been a while since I've had any of that!"
    odette "Good shit, huh?"
    eve "Can I try some?!"
    grace f_normal "No, I think you had better stick to beer-"
    odette "Of course, you can have some!"
    grace f_sad_back @ f_surprised_back "{b}Odette{/b}!"
    show odette a_whiskey_pour with dissolve
    odette "What?!"
    show eve a_shot
    show odette a_whiskey
    with dissolve
    odette "We were younger than her when we started drinking this stuff..."
    odette "... And it's just us here."
    show eve a_shot_drink f_drink with dissolve
    odette "What's the worse that can happen?"
    show eve a_shot f_disgusted with dissolve
    show grace f_surprised
    eve "{i}*Cough* *Cough*{/i}"
    show grace f_sad
    show eve f_sexy
    eve "H-holy shit..."
    eve "That stuff really burns!"
    odette "Mmhmm, that's how you know it's working."
    odette "You want some, stud?"
    show anon f_worried
    eve f_happy_right "Oh, he wants some!"
    anon "Ehh, s-sure... I guess."
    show odette a_whiskey_pour with dissolve
    show eve f_happy
    show grace f_sad_back
    odette "Coming right up, fine sir!"
    show grace f_sad
    show anon a_shot
    show odette a_whiskey
    with dissolve
    eve f_happy_right @ f_laugh "Haha!"
    show anon a_shot_drink f_smoke with dissolve
    pause
    anon a_shot f_disgusted_down @ f_cough "!!!"
    grace "You alright, {b}[firstname]{/b}?"
    anon "Eugh, good lord!"
    anon "What is that?"
    show anon f_worried
    show eve f_happy
    odette "Cinnamon whiskey."
    show eve f_happy_right
    anon "It's awful!"
    show eve f_happy
    odette @ f_laugh "Haha!"
    grace @ f_sad_back "Did you get everything locked up downstairs?"
    eve f_sad "Would you stop worrying and have some fun?!"
    grace f_sad "I just want to make sure-"
    show grace f_sad_back
    odette "Yes, everything is locked up... Relax."
    odette "Why don't we play a game or something?"
    show eve f_happy
    grace f_sad @ f_surprised_back "A game?"
    show anon f_normal
    eve "Yes, yes, yes!"
    eve @ f_confused "Truth or Dare?"
    show grace f_sad_back
    odette @ f_eyeroll "No, not Truth or Dare... That's kiddie shit!"
    show grace f_sad
    eve @ f_nervous_down "Uhh, I don't know many drinking games..."
    grace f_normal "Never Have I Ever?"
    odette @ f_laugh a_whiskey_yay "Bingo!"
    anon @ f_confused "Huh?"
    grace f_happy "Hehe, it's a drinking game."
    eve "How does it work?"
    show grace f_happy_back
    odette "It's really easy."
    odette "All you have to do is admit to something that you've never done."
    odette "For instance:"
    odette "{i}*Ahem*{/i} Never have I ever..."
    odette @ f_laugh a_whiskey_yay "Masturbated with a hairbrush!"
    show grace f_weary
    anon f_worried @ f_shock "!!!"
    eve @ f_laugh "WHAT?!"
    odette "Now, anyone here that HAS masturbated with a hairbrush, drinks a shot."
    grace f_tired_back "You're a bitch, you know that?"
    odette @ f_laugh "Hahaha!"
    grace "You just love bringing this shit up..."
    show grace a_shot_drink f_proud m_talk with dissolve
    eve @ f_surprised "So wait a second, that means-"
    show grace a_shot f_eyeroll -m_talk with dissolve
    grace "{i}*Sigh*{/i} Yes, I masturbated with a hairbrush a couple times, back when I lived at home with {b}Mom{/b} and {b}Dad{/b}."
    show grace f_normal
    anon f_surprised_teeth "!!!"
    eve @ f_laugh "Haha, why?!"
    grace f_sad @ f_eyeroll "Uhh, because I was horny and didn't have anything else?"
    show anon f_flirt_grin
    show grace f_normal_back
    odette @ f_confused "Why didn't you just buy yourself a dildo?"
    show anon f_normal
    grace "Umm, you did meet our parents, right?"
    odette "Yes."
    grace f_sad_down "{b}Dad{/b} wouldn't let us work, so I had no money to buy one..."
    grace "... And if that wasn't enough, {b}Mom{/b} was always snooping around in our rooms."
    show grace f_normal
    eve "Oh my god, could you imagine if she had found a dildo in your room?"
    grace f_happy "She would have shit a brick!"
    eve @ f_laugh "Totally!"
    pause
    show grace f_normal_back
    odette "Still though, a hairbrush?"
    grace @ f_eyeroll "Just the handle..."
    show anon f_laugh
    odette @ f_laugh "Pfft, hahaha!"
    show anon f_normal
    grace f_tired_back "Alright then, bitch... My turn!"
    grace "Never have I ever had a three-way on a pool table in front of a room full of people."
    show eve f_surprised
    show anon f_shock
    odette @ f_eyeroll "..."
    anon f_normal "Wow, that is really specific..."
    show odette f_yawn a_whiskey_drink with dissolve
    show anon f_surprised
    show grace f_happy
    eve f_disgusted @ f_surprised "Y-you really did that?"
    show grace f_happy_back
    odette f_smirk a_whiskey "It was a long time ago."
    show anon f_grin
    eve "Ewww!"
    show anon f_normal
    odette "You only live once, {b}Evie{/b}..."
    grace "That's when people started calling you the Chinese finger trap, you know?"
    show anon f_confused
    show eve f_confused
    odette "Ugh, don't bring that up."
    grace f_happy @ f_laugh "Hahaha!"
    anon "I don't get it..."
    eve "Me neither."
    grace a_fingers "Think about it."
    anon f_thinking a_thinking "..."
    eve f_thinking_down "..."
    grace a_shot @ f_eyeroll "Ehh, never mind."
    show eve f_happy
    show grace f_normal_back
    odette "Alright, can we ask questions that aren't specifically targeting each other now?"
    show anon f_normal a_shot with dissolve
    grace "Hey, you started it!"
    odette "Yeah, yeah..."
    pause
    odette "Why don't you go, {b}[firstname]{/b}?"
    show grace f_normal
    show eve f_happy_right
    anon f_worried "M-me?"
    eve "Do you understand the rules?"
    anon "I think so."
    anon f_thinking "Mmm, let's see..."
    anon "Never have I ever..."
    anon f_snarky "Shoplifted."
    show eve f_happy
    grace @ f_uneasy "You've never stolen anything in your entire life?!"
    show eve f_happy_right
    anon "Nope."
    show odette f_yawn a_whiskey_drink
    show grace a_shot_drink f_proud m_talk
    with dissolve
    show eve a_shot_drink f_drink with dissolve
    pause
    show eve a_shot f_disgusted_wince_down
    show odette f_smirk a_whiskey
    show grace a_shot f_happy -m_talk
    with dissolve
    eve "Eugh!"
    eve "I think you're supposed to ask naughty questions, {b}[firstname]{/b}..."
    show anon f_depressed
    show eve f_happy
    show grace f_normal_back
    odette "No, that question was perfect!"
    show grace f_normal
    show anon f_worried
    eve f_confused @ -m_talk "Hmm?"
    show grace f_normal_back
    odette "It got us all drinking, didn't it?"
    eve "Well, yeah?"
    odette "That's the entire purpose of the game, {b}Evie{/b}!"
    odette "Nice job, {b}[firstname]{/b}."
    show eve f_happy_right
    show grace f_normal
    anon f_normal @ f_laugh "Thanks."
    grace "Your turn, {b}Sis{/b}."
    show eve f_happy
    eve "Okay."
    eve "I've got one that will get all three of you for sure!"
    odette "Alright, let's hear it."
    eve "Never have I ever..."
    eve "Kissed a girl."
    odette "Ugh, too easy!"
    show grace a_shot_drink f_proud m_talk
    show odette f_yawn a_whiskey_drink
    show anon a_shot_drink f_smoke
    with dissolve
    pause
    show anon f_disgusted_wince a_shot
    show grace a_shot f_normal -m_talk
    show odette f_smirk a_whiskey
    with dissolve
    anon "Gaah!"
    show anon f_worried
    eve "How many girls have you kissed, {b}Odette{/b}?"
    show grace f_normal_back
    odette "I don't know, four or five?"
    show grace f_normal
    show anon f_normal
    eve "{b}Grace{/b}?"
    grace "Two."
    eve "I thought for sure it would be more, {b}Sis{/b}..."
    grace "Nope, just {b}Odette{/b} and one random girl at a party in high school."
    odette "I can't believe you never kissed a girl, {b}Evie{/b}."
    show eve f_nervous_down
    eve "I hadn't ever kissed anybody, before {b}[firstname]{/b}..."
    grace "Aww, I didn't know that..."
    grace @ f_laugh "You two are so sweet!"
    odette "Sweet?"
    show grace f_normal_back
    odette @ f_laugh "It's tragic is what it is!"
    odette a_shrug "Here."
    show grace f_surprised
    eve f_surprised "W-what are you-"
    show odette b_kiss_eve:
        xoffset -400
    hide eve
    with dissolve
    show anon f_surprised
    eve "!!!"
    grace f_angry "{b}Odette{/b}!"
    anon "!!!"
    show anon f_flirt_grin
    pause
    odette "Muuah!"
    hide odette
    show odette a_whiskey f_smirk zorder 1:
        xoffset 100
    show eve f_angry a_shot zorder 0:
        flip
        xoffset 100
    with dissolve
    eve "W-what the hell was that?!"
    show grace f_tired_back
    odette "Now you can say you've kissed a girl!"
    grace "I told you not to get too crazy..."
    grace "We've barely even started and-"
    odette "Would you relax?!"
    odette "It was just a kiss..."
    grace @ -m_talk "Hmph."
    show eve f_normal
    odette "Who's turn is it?"
    show grace f_normal
    anon f_normal "Yours, I think."
    show grace f_normal_back
    odette "Alright."
    show odette f_thinking
    pause
    odette "Never have I ever..."
    odette f_smirk "Snuck out of my parent's house."
    show grace f_normal
    eve @ f_eyeroll "I find that hard to believe."
    show grace f_normal_back
    odette "Why do you say that?"
    grace "Her dad lets her do whatever she wants, remember?"
    show grace f_normal
    eve f_happy "Oh, right..."
    show grace a_shot_drink f_proud m_talk
    show eve a_shot_drink f_drink
    show anon a_shot_drink f_smoke
    with dissolve
    pause
    show anon f_disgusted_wince a_shot
    show eve a_shot f_disgusted_wince_down
    show grace a_shot f_disgusted_wince -m_talk
    with dissolve
    eve "Phew!"
    show grace f_normal
    eve "Okay, this stuff is really kicking my ass..."
    anon f_worried "Yeah, totally."
    odette @ f_laugh "Haha!"
    grace "Maybe we should slow down a bit..."
    eve f_surprised "No!"
    show grace f_normal_back
    odette "We're not slowing down."
    show eve f_happy
    odette "It's your turn!"
    grace f_sad_back "{i}*Sigh*{/i} Fine."
    grace f_thinking @ -m_talk "Hmm."
    pause
    show grace f_happy
    grace "Never have I ever..."
    grace "Done anal."
    show odette f_surprised
    show eve f_surprised
    show anon f_surprised_teeth
    show grace f_normal_back
    odette "Whoa, really?"
    show anon f_flirt_grin
    show eve f_nervous_right
    odette f_smirk "All these years and you've never let anyone park it in your rear garage?"
    show eve f_nervous_down
    grace "Nope."
    grace "Plenty have tried but I never let them."
    grace f_happy_back "Gotta save something for marriage, you know?"
    odette "Psh, yeah right..."
    show odette f_yawn a_whiskey_drink with dissolve
    show grace f_normal
    show eve a_shot_drink f_drink with dissolve
    pause
    show eve a_shot f_disgusted_wince_down
    show odette f_smirk a_whiskey
    with dissolve
    show grace f_surprised
    anon f_shock "!!!"
    grace "{b}Eve{/b} what the fuck?!"
    show eve f_nervous
    show anon f_surprised_teeth
    grace "You've never had sex before!"
    eve "You didn't say sex, you just said anal."
    eve f_nervous_down "I've stuck stuff up there before..."
    show anon f_disgusted_wince
    show grace f_surprised_back
    show eve f_nervous_right
    odette "Oh shit, she's right!"
    show eve f_nervous_down
    show anon f_flirt_grin
    odette "You didn't say sex."
    show grace f_sad_down
    grace "Y-yeah, but..."
    odette "Who would have guessed, little {b}Evie{/b}'s done something you haven't!"
    odette "Haha!"
    grace f_sad "Why would you-"
    eve "I was curious and... It actually feels really nice..."
    odette "I've never been so proud!"
    grace "Ugh, the whole reason I went there was so you wouldn't have to drink!"
    show grace f_tired_back
    odette "I can give you some pointers later, if you want?"
    grace "Shut up, {b}Odette{/b}!"
    odette @ f_laugh "Hahaha!"
    show grace f_sad
    eve f_sad_right "S-sorry, {b}[firstname]{/b}..."
    eve "I hope you don't think I'm gross?"
    anon f_normal @ f_laugh "Of course not."
    show eve f_nervous
    show grace f_sad_back
    odette "Oh, good grief!"
    odette "There's nothing to be sorry about {b}Evie{/b}!"
    odette "Just because your sister is a prude-"
    show eve f_happy
    grace f_tired_back "I am not a prude!"
    odette @ f_laugh "Hahaha!"
    pause
    show grace f_sad_back
    odette "Seriously though, it's perfectly natural to experiment with that sort of stuff..."
    odette "... And for the record, she's right... It does feel really nice!"
    grace f_normal @ f_eyeroll "Ugh, next!"
    show grace f_sad
    eve f_happy_right "I think it's {b}[firstname]{/b}'s turn."
    anon "Is it?"
    eve @ -m_talk "Mmhmm."
    anon "O-okay."
    anon f_thinking "Umm."
    pause
    anon "Never have I ever..."
    anon f_snarky "Masturbated in public."
    show eve f_happy
    show grace f_surprised
    odette @ f_laugh "Hah, he's got me..."
    show grace f_sad_back
    show odette f_yawn a_whiskey_drink with dissolve
    pause
    show odette f_smirk a_whiskey with dissolve
    grace f_sad_down "{i}*Sigh*{/i}"
    show grace a_shot_drink f_proud m_talk with dissolve
    show anon f_flirt_grin
    pause
    show grace a_shot f_sad_back -m_talk with dissolve
    odette f_surprised "Really, when?!"
    grace f_sad_down "None of your business..."
    odette "Hey, it's the rules of the game!"
    odette "You gotta spill!"
    show odette f_smirk
    grace @ f_eyeroll "..."
    eve @ f_laugh "C'mon, sis..."
    grace f_normal "Ugh, fine."
    show anon f_normal
    grace f_normal_back "You remember Mr. Frampton?"
    odette "Our social studies teacher in high school?"
    grace "Yeah."
    grace "Well, I always thought he was hot and one day in class... I kinda..."
    odette "You masturbated in class?!"
    grace "Yeah, a little... Under my desk."
    odette @ f_laugh "Oh my god!"
    grace "Nobody knew, I was really discreet!"
    show anon f_laugh
    odette "You naughty girl..."
    show anon f_normal
    grace f_sad_down @ f_tired_back "Shut up!"
    odette @ f_laugh "Hahaha!"
    show eve a_shot_drink f_drink with dissolve
    show grace f_surprised
    pause
    show eve a_shot f_disgusted_wince_down with dissolve
    anon f_surprised "!!!"
    grace "Seriously, you too?!"
    show anon f_normal
    show eve f_happy
    eve "Y-yeah, one time..."
    show grace f_sad
    eve "In the bathroom at school."
    odette "What set that off?"
    show eve f_nervous_right
    eve "Uhh... N-nothing."
    show eve f_nervous_down
    odette @ -m_talk "Hmm?"
    eve "I don't remember."
    odette "Psh, c'mon!"
    odette "Did it involve {b}[firstname]{/b} or something?"
    show eve f_hood_remove
    grace f_tired_back "{b}Odette{/b}!"
    grace f_sad "She doesn't have to say if she doesn't want to..."
    show eve f_nervous_down
    odette "{i}*Sigh*{/i} Yeah, okay."
    grace "I think we'd better stop the game here, I don't want anyone getting sick..."
    show grace f_surprised
    show anon f_grumpy
    eve f_surprised "NO!"
    show anon f_surprised
    pause
    eve f_nervous "I mean, just one more..."
    show grace f_sad
    show anon f_normal
    eve "It's my turn."
    grace f_thinking @ -m_talk "..."
    grace f_normal @ f_eyeroll "Alright, one more."
    eve f_nervous_right "Never have I ever had sex."
    show anon f_surprised_teeth
    show grace f_eyeroll
    show eve f_nervous
    odette "Well, that's an easy one."
    show odette f_yawn a_whiskey_drink
    show grace a_shot_drink f_proud m_talk
    with dissolve
    pause
    show grace a_shot f_normal -m_talk
    show odette f_smirk a_whiskey
    with dissolve
    if not M_player.is_virgin:
        show anon a_shot_drink f_smoke with dissolve
        show eve f_sad_right
        pause
        show anon f_disgusted_wince a_shot with dissolve
        show eve f_sad_down
        show grace f_sad
        odette "Really?"
        show anon f_worried
        odette "Who was the lucky gal?"
        grace @ f_sad_back "{b}Odette{/b}..."
        anon "Ehh, I'd rather not say... If that's alright?"
        eve "Yeah, it's fine."
        odette "Aww, but I wanted to-"
    else:
        show anon f_grin
        show eve f_nervous_right
        pause
        show eve f_happy_right
        show grace f_happy
        odette f_tired "Really?"
        odette "You're a virgin?"
        show anon f_surprised
        grace @ f_tired_back "{b}Odette{/b}..."
        anon f_worried "Y-yeah."
        anon "I was waiting to find the right person."
        eve "That's so sweet, {b}[firstname]{/b}!"
        show anon f_normal
        grace @ f_laugh "It really is!"
        odette f_smirk @ f_eyeroll "Laaaaame."
    show eve f_normal
    grace f_tired_back "{b}Odette{/b}!"
    odette f_tired "What?!"
    show grace f_surprised
    pause
    show grace f_surprised_back
    pause
    odette f_smirk @ f_surprised "Oh."
    show grace f_normal
    pause
    grace "Alright, I think that's enough games for the night."
    odette "Well, I'm going to keep drinking..."
    show odette f_yawn a_whiskey_drink
    anon @ f_surprised "!!!" with hpunch
    show odette f_smirk a_whiskey with dissolve
    show grace f_normal_back
    pause
    odette @ f_burp "{i}*Buuuurp*{/i}"
    odette "If that's alright with you three?"
    show eve f_happy
    grace "Knock yourself out."
    odette "So..."
    show grace f_surprised_back
    odette f_shy "Are you two dating now or what?"
    show eve f_surprised_right
    show grace f_surprised
    anon f_worried "Uhh..."
    eve "I don't think we're ready to label it yet."
    odette "But you like him, right?"
    eve f_nervous_down @ -m_talk "Mmhmm."
    odette f_smirk "I know he likes you..."
    show grace f_normal
    anon f_flirt "Yes."
    if M_eve.biggus_dickus:
        odette "... And you've seen the girldick."
        show anon f_surprised
    else:
        odette "... And you've seen the scar."
    show grace f_tired
    show odette f_laugh
    eve f_surprised "!!!"
    show odette f_smirk
    grace f_angry_back "{b}Odette{/b}!"
    show anon f_worried
    odette "What?!"
    odette "He has, hasn't he?"
    show eve f_nervous_right
    anon f_normal "I have."
    odette "Can we be done with all the secrecy then, please?"
    show eve f_nervous
    grace f_sad @ -m_talk "..."
    odette "{b}Evie{/b} has nothing to be ashamed of... She should be proud!"
    eve f_sad_down "I dunno about proud..."
    if M_eve.biggus_dickus:
        odette "You're a hot girl with a dick... It's awesome!"
        eve f_sad "Ehh-"
        odette "For real!"
    else:
        odette "Scars are wicked sexy, girl."
        eve f_sad "Ehh-"
        odette "I'm serious!"
    odette "Don't you think it's sexy, {b}[firstname]{/b}?"
    anon f_grin @ f_normal "I do."
    eve f_surprised_right "Y-you do?"
    grace f_normal @ f_uneasy "Aww."
    eve f_nervous_down "B-but what about the rest of me?"
    show anon f_normal
    odette f_shy "What are you talking about?!"
    eve "Y-you know, my tiny tits..."
    show anon f_worried
    eve "... And my flat butt."
    odette f_normal @ f_eyeroll "Oh, for fuck's sake!"
    show grace f_normal_back
    odette "That's what has you so shy all the time?!"
    eve @ -m_talk "..."
    odette "You've got to wake up, girl!"
    odette "Tell her {b}[firstname]{/b}..."
    show grace f_normal
    show eve f_nervous_right
    anon f_normal "I like your body."
    show eve f_happy_right
    odette f_shy "SEE!"
    show grace f_normal_back
    show eve f_happy
    odette f_smirk "I bet you've got delicious little perky buds under there and guys love that shit... Trust me!"
    show grace f_eyeroll
    eve "R-really?"
    show grace f_normal_back
    odette @ f_laugh "Hell yeah!"
    odette @ f_eyeroll "I mean, look at your sister... Her tits aren't anything to write home about."
    show anon f_worried
    grace f_sad_down @ f_eyeroll "Jeez, thanks..."
    odette f_surprised "What-"
    odette f_confused "That's not-"
    pause
    odette f_sad "You know, I think yours are beautiful, but they aren't..."
    odette f_tired "Goddamnit, you know what I mean!"
    grace f_happy @ f_laugh "Haha!"
    show anon f_normal
    eve "You mean, she isn't stacked like you..."
    show grace f_happy_back
    odette f_normal "Yes, exactly!"
    odette f_shy "She's not stacked like me, and she still gets plenty of attention, right?"
    eve "Yeah."
    odette f_smirk "Men like all shapes and sizes..."
    odette "... And you're cute as hell!"
    pause
    odette "I'd fuck you in an instant."
    show eve f_eyeroll
    show anon f_flirt
    grace f_surprised_back "{b}Odette{/b}!!!"
    show eve f_happy
    odette f_confused "What?!"
    odette "I would."
    grace f_sad_back @ f_eyeroll "Jesus."
    odette "Why don't you take that hoodie off and let us see you?"
    show anon f_surprised
    show grace f_sad
    eve f_nervous "Really?"
    show anon f_flirt_grin
    odette "Yeah!"
    grace "You don't have to do that {b}Eve{/b}..."
    odette f_normal "Shush, prude!"
    grace f_angry_back "Stop calling me that!"
    show odette f_laugh
    show eve f_nervous_right
    show grace f_sad
    eve @ -m_talk "..."
    show odette f_normal
    pause
    show eve f_nervous_down
    show grace f_sad_back
    odette @ f_eyeroll "Oh my god with this shyness stuff..."
    show odette f_yawn a_whiskey_drink with dissolve
    show eve f_nervous
    pause
    show odette b_skirt f_tired_down a_remove1 with dissolve
    pause
    show odette b_skirtblank a_remove2 with dissolve
    pause
    show odette a_remove3 with dissolve
    show odette a_remove4 with dissolve
    pause
    show odette f_smirk b_skirt a_whiskey
    show grace f_surprised_back
    show eve f_surprised
    anon f_shock "!!!" with hpunch
    show anon f_flirt_grin
    show grace f_weary a_facepalm with dissolve
    odette "There, see..."
    odette "It's not that scary."
    show eve f_nervous_down a_hoodless_remove2 with dissolve
    show grace f_normal_back a_shot with dissolve
    pause
    show odette b_skirtblank a_idle with dissolve
    show eve f_nervous a_shot with dissolve
    odette f_tired_down "These damn things are a pain in the ass, more than anything..."
    grace @ f_tired_back "You're full of shit."
    odette f_normal "I'm serious!"
    show odette b_skirt a_whiskey with dissolve
    odette "They weigh a ton!"
    odette @ f_eyeroll "My back is always hurting!"
    odette "They are constantly getting in my way..."
    odette "... And have you seen me try and run?"
    grace @ f_weary "Ehh."
    odette "Remember that concert we snuck into a few years back?"
    odette "Where we had to sprint past security?"
    grace "Oh yeah!"
    odette "My tit bounced up and nailed me right in the face!"
    grace f_happy_back @ f_laugh "Haha, that shit was funny!"
    odette f_shy "No it wasn't!"
    odette "I practically gave myself a black eye!"
    show grace f_laugh
    show odette f_laugh
    show anon f_laugh
    eve f_laugh "Haha!"
    anon "Haha!"
    show grace f_happy_back
    show eve f_happy
    show anon f_flirt_grin
    odette f_smirk "So you see, big tits aren't all they're cracked up to be..."
    eve "Y-yeah, I guess."
    odette "Take off the hoodie, I wanna see what you're working with!"
    show grace f_normal
    eve f_nervous_down "{i}*Sigh*{/i} Alright."
    show eve b_topless a_remove with dissolve
    pause .25
    show eve b_pants a_dressup with dissolve
    pause
    show eve a_shot with dissolve
    odette f_smirk @ f_moo a_whiskey_yay "Woooo!!!"
    eve f_nervous @ f_eyeroll "Shut up..."
    odette "See, I was right!"
    odette "Those are adorable!"
    show eve f_nervous_right
    eve @ -m_talk "..."
    show eve f_nervous
    show grace f_normal_back
    odette "You're a lucky guy, {b}[firstname]{/b}!"
    odette @ f_laugh "I would eat her right up!"
    show grace f_normal
    show eve f_nervous_right
    show odette f_tired_down a_remove5 with dissolve
    pause
    show odette b_remove6 with dissolve
    pause
    show odette b_panties f_smirk a_whiskey with dissolve
    show anon f_surprised
    show eve f_surprised
    grace f_surprised_back "Would you stop?!"
    show anon f_grin
    show eve f_nervous
    grace "You've gone far enough!"
    show anon f_flirt
    show grace f_tired_back
    odette f_tired "Oh my god, what is your deal, {b}Grace{/b}?!"
    odette "When did you become such a prude?"
    grace f_angry_back "I'm not a prude!"
    odette @ f_eyeroll "Yeah, right."
    odette "When's the last time you got laid?"
    grace f_sad_down "That's not-"
    odette "'Cause I haven't seen you with anyone in... I dunno... What do you think, {b}Evie{/b}?"
    eve "Not since {b}Mom{/b} and {b}Dad{/b}'s accident."
    grace f_sad "That has nothing to do with it."
    odette @ -m_talk "Mmhmm."
    odette f_normal "You used to be fun, you know?"
    grace f_sad_back "I'm still fun!"
    odette f_smirk @ f_laugh "Then prove it, let's see some skin!"
    show eve f_happy
    grace f_sad_down @ f_eyeroll "{i}*Sigh*{/i}"
    pause
    grace f_normal_down "Fine. Fuck it!"
    show grace a_remove1 with dissolve
    pause
    show grace b_shorts a_remove2 with dissolve
    pause
    show grace f_normal a_hip with dissolve
    show anon f_flirt
    eve @ f_moo a_shot_yay "Woooo!!!"
    odette @ f_laugh "Haha, that's the spirit!"
    show grace f_proud a_remove3 with dissolve
    pause
    show grace b_remove4 with dissolve
    pause
    show grace f_normal_back b_underwear a_shot with dissolve
    grace "There."
    grace "Satisfied?"
    odette "No, but it's a start."
    grace @ -m_talk "..."
    odette "Here, you need more of this!"
    show odette a_idle
    show grace a_whiskey
    with dissolve
    grace f_sad_down "{i}*Sigh*{/i}"
    show grace a_whiskey_drink f_proud m_talk with dissolve
    pause
    show grace a_whiskey f_normal -m_talk with dissolve
    odette "What do you think, {b}[firstname]{/b}?"
    odette "Are these some sexy bitches or what?!"
    show eve f_happy_right
    anon "Very sexy."
    pause
    show odette f_surprised
    pause
    show grace f_happy_back
    show eve f_happy
    odette f_smirk_back @ f_laugh "Oh shit, this is my jam!"
    show grace b_lead f_happy zorder 2
    show odette b_empty zorder 3:
        xoffset -545
    with dissolve
    odette "Come dance with me!"
    grace @ f_laugh "Hehe!"
    hide grace
    hide odette
    with dissolve
    eve f_happy_right "You wanna dance?"
    anon f_worried "Ehh, maybe in a bit."
    anon f_flirt "I'll just watch for now."
    eve f_laugh "Hehe, okay!"
    hide eve with dissolve
    show anon f_flirt_grin
    pause
    eve "Wait for me!"

    scene location_tattoo_rooftop_cutscene01
    show text _ ("The moment had me completely frozen in place.\nMesmerized by beautiful bodies of the girls dancing before me in the firelight.") as caption
    with fade
    hide caption with dissolve
    show text _ ("It was hard to fathom how I had ended up in this situation...\nWas I just the luckiest guy on the planet or what?") as caption with dissolve
    pause

    scene expression background(800, 400, 2.4) as stage
    show anon f_flirt_grin at flip
    with fade
    anon @ -m_talk "..."
    show eve b_pants f_laugh a_hip at flip with {'master': dissolve}
    eve "Hehe!"
    show eve b_empty:
        xoffset -530
        xzoom 1
    show anon b_pulling4 f_grin
    with {'master': dissolve}
    eve f_happy_right "C'mon, {b}[firstname]{/b}... Come dance with me!"
    anon f_flirt "O-okay."
    show anon:
        xoffset -188
    show eve f_happy:
        xoffset -718
    with dissolve
    pause
    anon f_surprised "Whoa..."
    eve f_happy_right @ -m_talk "Hmm?"

    scene expression background(512, 400, 2.4) as stage
    show odette b_kiss_grace:
        xoffset -400
    with fade
    pause
    show anon f_flirt:
        xzoom -1
        xoffset 100
    show eve f_happy b_pants a_hip:
        xoffset -100
    with dissolve
    anon "Looks like {b}Odette{/b} is finally getting somewhere with your sister..."
    eve "Y-yeah, maybe."
    pause
    show eve a_belly_sick f_disgusted_wince_down:
        xoffset 450
        xzoom -1
    with {'master': dissolve}
    eve "Eugh."
    anon f_worried "You alright?"
    eve "Yeah, I just-"
    pause
    eve "Feel a little dizzy... All of a sudden..."
    anon "Can I get you some-"
    eve f_surprised a_puke "Oh shit!"
    hide eve
    show anon a_surprised f_surprised:
        xzoom 1
        xoffset 600
    with dissolve
    anon "{b}Eve{/b}?!"
    show anon a_surprised_up f_surprised_teeth
    with {'master': dissolve}
    eve "{i}*BLLEEAARRGHHH*{/i}"
    show anon a_sides f_worried
    show odette b_panties f_confused:
        xoffset 100
        xzoom -1
    show grace b_underwear f_sad:
        xoffset -100
        xzoom -1
    with dissolve
    grace "Is she puking?"
    show anon:
        xoffset 50
        xzoom -1
    with {'master': dissolve}
    anon "Y-yeah, I think so..."
    grace "Shit!"
    grace f_angry "I told you this was going too far!"
    show odette f_sad
    hide grace
    show anon:
        xzoom 1
        xoffset 550
    with dissolve
    grace "Come on, {b}Sis{/b}. Let's get you downstairs and drinking some water..."
    odette @ -m_talk "..."
    odette "Fuck!"
    show anon f_worried:
        xoffset 0
        xzoom -1
    with dissolve
    odette "Talk about bad timing!"
    anon "Is {b}Eve{/b} going to be alright?"
    odette f_tired "Oh, she'll be fine..."
    show anon:
        xoffset 500
        xzoom 1
    with {'master': dissolve}
    odette "Just a bit too much too quickly."
    pause
    odette f_smirk "Quite the night, huh?"
    anon "Yeah, pretty crazy."
    odette "I bet it was all pretty exciting for you?"
    show anon a_behind_head f_surprised:
        xoffset 0
        xzoom -1
    with dissolve
    pause
    anon f_worried "Ehh, y-yes..."
    odette @ f_laugh "Hehe, what's the matter?"
    odette "You seem a little embarrassed..."
    anon @ -m_talk "..."
    show odette b_pantiesblank with dissolve
    odette "You like my tits, {b}[firstname]{/b}?"
    show odette f_smirk_down
    anon f_surprised_teeth_down o_boner "!!!" with hpunch
    anon f_depressed "S-sorry, I didn't mean-"
    odette f_smirk @ f_laugh "Haha!"
    odette "It's fine, {b}[firstname]{/b}... You can look."
    anon a_sides f_flirt @ -m_talk "..."
    odette "You wanna touch them?"
    anon f_worried "Oh, uhh..."
    anon "... I don't think that's a good idea."
    show odette b_panties
    with {'master': dissolve}
    odette "Why not?"
    odette "{b}Evie{/b} won't mind if we have a little fun..."
    anon @ -m_talk "..."
    show anon f_surprised behind odette
    show odette a_grope:
        xoffset 250
    with {'master': dissolve}
    odette "... I promise!"
    show anon f_surprised_down
    with {'master': dissolve}
    anon @ -m_talk "!!!"
    odette a_idle f_surprised_down "Wow, {b}Tuuku{/b} wasn't joking!"
    show anon a_sides f_surprised
    with {'master': dissolve}
    odette f_smirk "You are big!"
    anon f_worried "I don't think we should be-"
    odette "Aww, don't be shy big fella."
    show anon a_up f_surprised_low -o_boner
    show odette a_anon_pants1 f_smirk_lip_down:
        offset (237, 207)
    with {'master': dissolve}
    anon "W-whoa, {b}Odette{/b}!!"
    pause
    odette f_smirk_up "You must be horny as hell after the night you just had..."
    odette "... Heh, I know I certainly am!"

    menu:
        "I can't do this!":
            show odette a_anon_pants2 f_confused
            show anon a_cover_boner o_boner f_worried_low
            with {'master': dissolve}
            anon "Cut it out, {b}Odette{/b}."
            odette f_thinking @ -m_talk "Hmm?"
            show odette a_sides
            with {'master': dissolve}
            anon "{b}Eve{/b} and {b}Grace{/b} are right downstairs!"
            show anon a_sides
            show odette f_smirk_up
            with {'master': dissolve}
            odette "Oh, relax... they're going to be busy for a while."
            show anon -o_boner
            show odette a_anon_pants1 f_smirk_lip_down
            with {'master': dissolve}
            anon "That's not the point, I-"
            show odette a_anon_pants2 f_sad
            show anon a_cover_boner o_boner f_surprised_low
            with {'master': dissolve}
            anon "{b}Odette{/b}, stop!"
            show odette a_sides f_annoyed_up
            with {'master': dissolve}
            odette "Wait, seriously?"
            anon "Yes!"
            odette f_thinking "Umm, you understand I'm offering to suck your dick right now... right?"
            anon f_worried_low "Yeah, I kinda figured that... it's just-"
            show anon a_sides -o_boner
            with {'master': dissolve}
            anon "{i}*Sigh*{/i} Could you stand up, please?"
            pause
            show odette b_remove6:
                offset (200, 50)
            with {'master': dissolve}
            anon "Look, you're like, super hot and all..."
            show anon f_worried of_blush
            show odette b_panties f_confused:
                offset (200, 0)
            with {'master': dissolve}
            anon "... And very, VERY naked..."
            show odette f_laugh
            with {'master': dissolve}
            odette "Hehe!"
            show odette f_smirk
            with {'master': dissolve}
            odette "Uh huh?"
            show anon f_shy_left
            with {'master': dissolve}
            anon "... But {b}Eve{/b} and I are... well, I'm exactly sure what we are yet."
            show anon f_shy
            show odette f_confused
            with {'master': dissolve}
            anon "B-but I'm eager to find out!"
            odette "Oh kay?"
            anon f_worried "And I really don't want to risk screwing things up... ya know?"
            anon "So, much as I would enjoy the... uhh..."
            odette f_smirk "Blowjob?"
            anon "... Y-yes, that!"
            odette f_laugh "{i}*Snort*{/i}"
            show anon a_cover_boner
            with {'master': dissolve}
            anon "I'm afraid I must respectfully, decline."
            odette f_smirk "Wow, I don't think anybody has ever turned me down before..."
            show anon f_surprised_low
            show odette a_excited f_shy:
                xoffset 275
            with {'master': dissolve}
            odette "... it's kinda turning me on even more."
            anon f_shy "{i}*Gulp*{/i} R-really?"
            odette @ -m_talk "Mhmm."
            grace "{b}Odette{/b}!"
            show anon a_sides f_worried_left -of_blush
            show odette f_confused
            with {'master': dissolve}
            grace "I need your help!"
            odette f_sad "Tsk, looks like our fun's getting cut short..."
            show anon f_worried
            show odette a_sides:
                xoffset 200
            with {'master': dissolve}
            odette f_smirk "You should head on home... We'll take good care of {b}Evie{/b}."
        "Now what?":

            show odette a_sides f_smirk_lip_down
            show anon b_shirt od_dick2
            with dissolve
            show anon od_dick3
            with fastdissolve
            show odette a_excited f_smirk_down
            show anon od_dick4
            with fastdissolve
            odette "Hell-O!"
            show odette a_anon_pants2 f_smirk_lip_down
            with {'master': dissolve}
            anon "Uhh, what exactly are you-"

            call scene_odette_blowjob
            $ unlock_scene('Odette', '04_unlocked', variant='roof')

            scene expression background(512, 400, 2.4) as stage
            show anon a_sides b_shirt od_dick4_wet f_surprised:
                xzoom -1
            show odette a_wipe b_panties:
                xoffset 200
                xzoom -1
            with fade
            pause
            show odette a_sides
            with {'master': dissolve}
            odette "Shit, I'd better go..."
            anon f_confused "Wait, you're leaving?!"
            odette f_smirk "Duty calls I'm afraid..."
            odette "... But don't worry, big fella..."

    show anon f_surprised
    show odette a_kiss f_moo
    with dissolve
    pause
    odette a_idle f_smirk "To be continued."
    anon @ -m_talk "{i}*Gulp*{/i}"
    show anon f_shy:
        xoffset 500
        xzoom 1
    hide odette
    with {'master': dissolve}
    odette "Hehe!"
    pause
    anon f_flirt_grin @ -m_talk "( Holy crap! )"
    anon @ -m_talk "( That girl is big trouble... )"
    pause
    anon @ f_laugh -m_talk "( ... What a night though! )"
    anon @ -m_talk "( I think {b}Eve{/b} and I might really be building towards something really special here! )"
    anon @ -m_talk "( I'll have to be sure and {b}check on her tomorrow{/b}. )"
    hide anon with dissolve
    return

label eve_button_eve_talk_to_girls:
    scene expression player.location.background_closeup with None
    show anon a_beer
    show eve f_happy a_ipod
    with dissolve
    anon "Here you go."
    show eve a_beer_ipod
    show anon b_dressed_pickup
    with dissolve
    eve "Thanks, {b}[firstname]{/b}!"
    show anon b_dressed f_worried a_beer with dissolve
    anon "Sorry, I couldn't find any warm, skunky ones; past their expiration date..."
    show eve f_confused
    anon f_snarky "You know, since that's the way you usually drink them?"
    eve f_happy @ f_laugh "Oh, hah hah, very funny."
    anon f_normal @ f_laugh "Hahaha!"
    eve f_normal_down "You got any music preference?"
    anon "Nah, anything is fine."
    eve "I think I'll start us off with some classic rock."
    eve "That's {b}Grace{/b}'s favorite."
    anon "Works for me!"
    pause
    eve f_sad a_beer_hold "{i}*Sigh*{/i} I really hope {b}Grace{/b} cuts it loose tonight."
    eve "You wouldn't believe how much fun she used to be!"
    anon f_worried "I think she's pretty fun now, {b}Eve{/b}."
    eve "Y-yeah, but nothing like before the accident..."
    anon "You really think the accident is to blame?"
    eve "I hope so."
    eve f_sad_down "Otherwise, it's my fault."
    anon f_skeptical "How could it be your fault?"
    eve "Y-you know, because she's stuck taking care of me..."
    anon "Isn't it possible she just grew out of the whole party scene?"
    anon "I mean, people do that..."
    anon "They get older and their priorities change."
    eve "Yeah, I guess."
    anon "Don't worry about it so much."
    anon f_worried "Let's just focus on having fun tonight, huh?"
    eve "You're right."
    show anon b_hug_eve f_shy_down
    hide eve
    with dissolve
    eve "You always make me feel better, {b}[firstname]{/b}."
    eve "Thank you!"
    return


label eve_button_bike_breakdown_started:
    scene expression player.location.background_closeup with None
    if player.location != L_school_frenchclassroom:
        show eve f_happy
        show anon
    else:
        show eve b_desk_look_left f_happy:
            xoffset 500
        show anon b_desk
    with dissolve
    eve "Hey, {b}[firstname]{/b}!"
    if player.location != L_school_frenchclassroom:
        hide eve
        show anon b_hug_eve f_shy_down
        with dissolve
    anon "Hello."
    if player.location != L_school_frenchclassroom:
        show anon b_dressed f_normal
        show eve f_happy
        with dissolve
    eve "Are you still {b}coming over this weekend{/b}?"
    anon "Of course."
    eve "I really hope {b}Grace{/b} gets the bike fixed and lets us take her for a spin!"
    anon "Yeah, that would be awesome!"
    return

label eve_button_bike_breakdown_start:
    scene expression player.location.background_closeup with None
    if player.location != L_school_frenchclassroom:
        show eve f_happy
        show anon
    else:
        show eve b_desk_look_left f_happy:
            xoffset 500
        show anon b_desk
    with dissolve
    eve "Hey, {b}[firstname]{/b}!"
    if player.location != L_school_frenchclassroom:
        hide eve
        show anon b_hug_eve f_shy_down
        with dissolve
    anon "Hello."
    if player.location != L_school_frenchclassroom:
        show anon b_dressed f_normal
        show eve f_happy
        with dissolve
    anon "You wanna hang out after school?"
    eve f_sad "Aww, I wish I could..."
    eve "I've got detention, remember?"
    anon f_worried "Oh, right."
    eve "Sorry."
    anon "It's no problem."
    eve f_happy "You should {b}come over to my house this weekend{/b}!"
    show anon f_normal
    eve "{b}Grace{/b} got the replacement part for her bike, so she'll be trying to fix it."
    anon "Oh, yeah?"
    eve "Who knows, if she gets it working, she might even let us take it for a spin."
    anon @ f_laugh "That would be so awesome!"
    eve "So you'll be there?"
    anon "You bet I will."
    eve @ f_laugh "Hehe, I can't wait!"
    hide anon with dissolve
    return

label eve_button_detention:
    scene expression player.location.background_closeup with None
    show anon
    show eve f_happy
    with dissolve
    eve "{b}[firstname]{/b}!"
    hide eve
    show anon b_hug_eve f_laugh
    with dissolve
    anon "Heh, hey {b}Eve{/b}."
    anon f_shy_down "How are you?"
    show anon b_dressed f_normal
    show eve f_happy
    with dissolve
    eve "Fantastic, thanks to you!"
    anon "What do you mean?"
    eve "I handed in your sketch to {b}Miss Ross{/b}, and she loved it!"
    anon "Really?"
    eve "Yeah!"
    eve "You really saved me a lot of trouble."
    anon "Aww, c'mon... It was nothing."
    hide anon
    show eve b_dressed_kiss:
        xoffset -400
    with dissolve
    anon "!!!"
    pause
    show eve b_dressed f_surprised a_cover_mouth:
        xoffset 0
    show anon f_flirt
    with dissolve
    eve "Oops!"
    show eve f_nervous a_rossed
    eve "S-sorry, I forgot where we are..."
    anon "N-no, it's okay."
    anon "I like kissing you."
    eve @ f_surprised "You do?"
    anon "Of course."
    eve a_idle "Hehe, I like kissing you too."
    show anon f_grin
    show eve f_nervous_down
    pause
    eve "But I did... Kinda... Promise {b}Grace{/b} that we'd take it slow..."
    anon f_worried "Oh?"
    eve "Y-yeah."
    eve f_nervous "She's playing the role of the concerned big sister again."
    anon f_grin @ f_unimpressed "Heh, that's okay."
    eve "Yeah?"
    anon f_normal "We can take it slow, it's no problem."
    hide eve
    show anon b_hug_eve f_shy_down
    with dissolve
    eve "Oh my god, you are the best, {b}[firstname]{/b}!"
    eve "Thank you!"
    anon "You're welcome."
    pause
    show anon b_dressed f_normal
    show eve f_happy
    with dissolve
    anon "So, how did things go between your sister and {b}Odette{/b} the other night?"
    eve @ -m_talk "Hmm?"
    anon f_flirt "Did they, you know?"
    eve "Oh, you're asking if they hooked up?"
    anon f_flirt_grin @ -m_talk "Mmhmm."
    eve "No, they didn't."
    eve @ f_eyeroll "Apparently, my sister fell asleep shortly after they put the movie in."
    anon f_normal @ f_laugh "She fell asleep?"
    eve "Yeah."
    anon "During a horror movie?"
    eve @ f_laugh "Haha!"
    eve "I know, crazy right?!"
    eve "It's because she's overworking herself."
    eve "She's exhausted, like, all the time!"
    anon "Yeah, I can imagine."
    eve f_sad_down "I wish she would let me help her."
    pause
    anon "Why doesn't {b}Odette{/b} help her?"
    eve f_normal "What?"
    anon "I mean, she's at your place all the time anyways..."
    anon "If she offered to help {b}Grace{/b} with work in the shop, maybe {b}Grace{/b} would be more receptive to her advances?"
    eve f_thinking_down @ -m_talk "Hmm."
    anon "You don't think so?"
    eve f_normal "No, it's actually a good idea."
    eve a_hip @ f_eyeroll "It might even work... IF {b}Odette{/b} wasn't so freaking lazy!"
    anon @ f_laugh "Haha!"
    eve "That girl hasn't worked a day in her entire life."
    anon "You should tell her."
    eve "Yeaaah, no."
    anon "Why not?"
    eve "Because, I'm not going to help {b}Odette{/b} seduce my sister!"
    eve "That would be weird."
    anon "Why is that weird?"
    anon "You want {b}Grace{/b} to be happy, don't you?"
    eve "Of course I do!"
    eve "But, it's {b}Odette{/b}... And my sister..."
    anon "So?"
    eve f_sad_down a_idle "{i}*Sigh*{/i} I dunno, maybe you're right."
    pause
    eve f_normal "I guess it wouldn't hurt to try."
    anon @ f_laugh "Exactly."
    pause
    eve f_happy "You should come over tonight, and we'll talk to {b}Odette{/b} about it."
    anon @ f_flirt "I can do that."
    eve @ f_laugh "Awesome!"
    eve "Afterwards, I'll whoop your butt in {i}Street Kombat{/i} again!"
    anon @ f_snarky a_point "Oh, you're so going down this time!"
    eve @ f_laugh "Haha!"
    roxxy "Hey, freak!" with hpunch
    show eve f_surprised:
        flip
        xoffset 100
    show becca f_upset:
        xoffset 100
    show missy f_angry:
        xoffset -50
    show roxxy f_angry:
        xoffset -200
    show anon f_surprised:
        xoffset -175
    with dissolve
    anon "{b}Roxxy{/b}?"
    show roxxy m_talk
    if M_roxxy.finished_state(S_roxxy_picnic_done):
        roxxy "Out of my way, {b}[firstname]{/b}!"
    else:
        roxxy "Out of my way, loser!"
    show anon f_surprised_teeth
    show roxxy b_dressed_toes with dissolve
    roxxy "You think it's funny, pulling pranks on people?!"
    show roxxy b_dressed -m_talk with dissolve
    eve f_confused "Huh?"
    roxxy "I know you're the one who fucked up my hair!"
    becca "And my skin!"
    eve a_hip f_normal @ f_eyeroll "I dunno what you're talking about..."
    roxxy "Don't try and deny it!"
    missy "You drew a dick on my forehead!"
    eve f_happy @ f_laugh "Hahaha!"
    missy @ -m_talk "..."
    becca "We know it was you!"
    show anon f_surprised_left
    eve "Can you prove it?"
    show anon f_surprised
    roxxy "I don't need to prove it!"
    if M_roxxy.finished_state(S_roxxy_picnic_done):
        show roxxy b_empty zorder 2:
            xoffset -125
            yoffset 6
        show anon f_surprised_teeth b_pulling1 zorder 1:
            xoffset -120
        show becca:
            xoffset 150
        show missy:
            xoffset 20
        with dissolve
        show eve f_surprised
        roxxy "C'mon, {b}[firstname]{/b}!"
        roxxy "I don't want you hanging out with this fugly bitch anymore!"
        eve f_angry "H-hey!"
        show eve b_empty zorder 2:
            xoffset -118
        show anon b_pulling2 f_surprised_left
        with dissolve
        eve "You don't get to control him!"
        show anon f_surprised b_pulling3 with dissolve
        roxxy "Let go!"
        show anon b_pulling2 f_surprised_left with dissolve
        eve "NO!"
        show anon b_pulling3 f_surprised with dissolve
        pause
        anon "Okay, you two need to calm down..."
        show missy f_normal
        show anon b_pulling2 with dissolve
        eve "He can hang out with whoever he wants!"
        show anon f_hurt
        missy "This is kinda hot."
        becca @ f_eyeroll "Shut up, {b}Missy{/b}..."
        show anon b_pulling3 with dissolve
        roxxy "You better back the fuck off, bitch!"
        show anon b_pulling2 with dissolve
        eve "Or what?!"
        show anon b_pulling3 with dissolve
        roxxy "Grr!"
        show anon b_pulling2 with dissolve
        eve "I'm not scared of you!"
        show anon b_dressed a_up f_angry:
            xoffset 100
        show eve b_dressed f_surprised
        show roxxy b_dressed
        with dissolve
        anon "That's enough!"
        show anon a_surprised
        roxxy "You are so dead..."
    else:
        roxxy "Do you know how long it took me to wash that shit out?!"
        eve "A long time, I hope!"
        roxxy "So you admit it?!"
        show anon f_surprised_left
        eve "No, I'm not admitting shit..."
        eve @ f_laugh "... But you definitely deserved it!"
        show anon f_worried
        anon "Okay, everybody needs to calm down..."
        roxxy "Shut up, {b}[firstname]{/b}!"
        eve "Hey, don't talk to him like that!"
        roxxy "Or what?!"
        pause
        show anon f_surprised
        roxxy "Maybe I should fuck up YOUR hair?"
        show anon f_surprised_left
        eve "I'm not scared of you!"
        anon f_angry "That's enough!"
        roxxy "You better listen to your friend, freak!"
    eve f_angry "Fuck you, trailer trash Barbie!"
    roxxy f_glaring @ -m_talk "!!!"
    show roxxy b_jump with dissolve
    show missy f_surprised
    show becca f_surprised
    show anon f_shock
    show eve f_surprised a_arrest
    roxxy "Raaaah!"
    show anon f_surprised_left
    hide eve
    hide roxxy
    eve "!!!" with hpunch
    becca "Holy shit!"
    anon "{b}Roxxy{/b} stop!"

    scene location_school_right_hall_cutscene_02
    with fade
    eve "Aaahh!!"
    roxxy "This is what happens!"
    eve "Get off of me!"
    roxxy "When you mess with me!"
    eve "Aaahh!!"

    scene location_school_right_hall_cutscene_03
    with fade
    eve "{i}*Chomp*{/i}" with hpunch
    roxxy "!!!"
    roxxy "OOOWWWW!!!"
    anon "{b}Eve{/b}!"
    roxxy "You fucking bitch!"
    roxxy "AAAHHHH!!!"

    scene expression player.location.background_closeup
    show anon f_surprised
    show eve b_dressed_disheveled f_angry:
        flip
        xoffset -100
    show roxxy a_ouch f_glaring
    with fade
    roxxy "You bit me!"
    eve "Damn right!"
    smith "What is going on in here?!"
    show anon f_sad_down
    anon "Oh, crap..."
    show smith f_angry
    show roxxy:
        flip
        xoffset 250
    with dissolve
    show anon f_hurt
    smith "Have you girls lost your minds?"
    roxxy f_angry "She started it!"
    show anon f_tired
    eve "WHAT?!"
    eve "You're the one who started it!"
    smith "That's enough!" with hpunch
    smith "I will not tolerate this type of behavior in my school!"
    smith "Detention for all of you!"
    show anon f_depressed
    roxxy f_glaring "Seriously?"
    eve "Aww, come on!"
    missy "That's not fair!"
    becca "Yeah, we didn't even do anything!"
    smith "Silence!" with hpunch
    smith "I'm not about to argue with a bunch of snot nosed brats!"
    smith "That's {b}Annie{/b}'s job."
    pause
    smith "Now, let's go!"
    roxxy f_angry_right "Nice going, bitch..."
    eve "{i}*Sigh*{/i} Shut up, {b}Roxxy{/b}."
    show roxxy f_surprised
    show anon f_surprised_teeth
    show eve f_surprised
    smith @ f_scream "I SAID MOVE IT!" with hpunch
    scene black with fade
    pause
    $ player.go_to(L_school_frenchclassroom)
    scene expression player.location.background_blur with None
    show anon f_worried
    show eve a_hip:
        flip
        xoffset -100
    show roxxy:
        flip
        xoffset 250
    show annie f_annoyed
    with dissolve
    annie "Alright trouble makers, you know the drill."
    annie "No talking, no cell phones, no food or drinks-"
    roxxy @ f_eyeroll a_cross "Oh great, we get to spend the next four hours with this stupid suck up..."
    eve f_happy @ f_laugh "Heh, yeah... She's the only person in this school I hate more than you..."
    roxxy @ f_laugh "Hahaha!"
    annie @ f_angry "Hey, I said no talking!"
    roxxy @ f_pouting_hair "Psh."
    eve f_disgusted "Freaking brown noser."
    annie "What did you say?"
    eve f_sexy "Shouldn't you be off kissing {b}Mrs. Smith{/b}'s feet or something?"
    roxxy @ f_laugh "Hahaha!"
    annie f_angry a_note @ a_note_write "You two just bought yourselves another detention!"
    eve @ f_eyeroll "Ugh, we're crushed..."
    annie @ a_note_write "You just bought one more, right there!"
    show anon f_depressed
    roxxy "Well, I'm free the day after too."
    roxxy "Beyond that, I'm going to have to check my calendar!"
    eve @ f_laugh "Hahaha!"
    annie "Good, because it's going to be filled with detentions!"
    show eve f_angry
    roxxy f_pouting @ -m_talk "..."
    annie "Are you through?"
    roxxy f_normal "No."
    show eve f_sexy
    annie @ a_note_write "That's another one!"
    pause
    annie "I can do this all day."
    show anon f_worried
    eve "So?"
    annie @ a_note_write "That's another one!"
    eve @ -m_talk "..."
    annie f_annoyed "We'll keep going..."
    annie "Just say the word."
    roxxy "Go."
    eve @ f_laugh "Hahaha!"
    annie @ a_note_write "You just bought one more!"
    annie "You think I've got something better to do?"
    eve "We know you don't have anything better to do..."
    roxxy @ f_laugh "Haha!"
    annie "What was that?"
    eve @ -m_talk "..."
    anon "Guys, cut it out!"
    annie "I'll see you both in here every day for the rest of your natural-born lives if you aren't careful!"
    roxxy f_pouting @ -m_talk "..."
    eve f_angry @ -m_talk "..."
    annie "That's what I thought..."
    annie f_angry a_idle @ a_point1 "Now, take your seats!"
    hide eve
    hide roxxy
    with dissolve
    anon f_tired "Sheesh."
    scene black with fade
    pause
    scene expression player.location.background_blur
    show anon b_desk f_sad_down:
        xoffset 600
    show eve b_desk_look_left f_sad_down:
        xoffset 300
    show roxxy b_desk_bored f_pouting:
        xoffset -50
    with fade
    pause
    anon @ -m_talk "..."
    pause
    show eve f_nervous_right
    pause
    eve "Hey, {b}Roxxy{/b}."
    show anon f_worried_left
    eve "Psst."
    roxxy f_worried "What?"
    eve f_happy_right "It would be a shame if that prankster who got you went after {b}Annie{/b} next, don't you think?"
    show roxxy b_desk_normal with dissolve
    roxxy f_normal "Huh?"
    pause
    roxxy @ f_surprised "Oh."
    roxxy f_sexy @ f_laugh "Haha, yeah!"
    roxxy "That bitch totally has it coming!"
    eve @ f_laugh "Haha!"
    show anon f_normal_left
    roxxy "Just make sure it's something really humiliating..."
    eve "Totally."
    pause
    anon f_thinking @ -m_talk "( Huh. )"
    anon @ -m_talk "( They're acting pretty friendly all of a sudden... )"
    anon f_normal_left @ -m_talk "( Did they actually bond over a shared hatred of {b}Annie{/b}? )"
    pause

    scene location_school_french_cutscene16
    show text _ ("I wasn't sure what {b}Eve{/b} was plotting but it was nice to see her and {b}Roxxy{/b} getting along for once.\nEven if it did spell trouble for {b}Annie{/b}...") as caption
    with fade
    pause
    hide caption with dissolve
    show text _ ("I just hope it doesn't land {b}Eve{/b} more detention!\nI can't imagine doing this every night for a week straight!") as caption with dissolve
    pause

    $ game.timer.tick(3)
    $ player.go_to(L_school_front)
    scene expression player.location.background_blur
    show eve f_eyeroll
    show anon f_depressed
    with fade
    eve "Ugh, longest four hours, EVER!"
    show eve f_normal
    anon f_tired "Yeah, tell me about it..."
    pause
    eve @ f_sad_down "Sorry I got you detention."
    anon f_worried "It's okay."
    show eve f_nervous
    pause
    anon "Sorry {b}Roxxy{/b} tried to rip your head off."
    eve "Yeah."
    pause
    anon f_normal @ f_laugh "I can't believe you bit her boob!"
    eve f_laugh "Well, I had to do something..."
    eve "She was trying to smother me with those giant things!"
    anon @ f_laugh "Hahaha!"
    eve @ f_laugh "Hahaha!"
    show eve f_normal
    pause
    eve f_sad_down "Man, {b}Grace{/b} is going to flip out when she hears I got detention for a week straight!"
    anon "At least you and {b}Roxxy{/b} left things on good terms..."
    eve "Yeah, I guess."
    pause
    eve f_sad "{i}*Sigh*{/i} I should probably get home."
    anon "Yeah, me too."
    eve "It sucks our plans got ruined..."
    anon "Heh, no worries."
    anon f_snarky "I'll just have to kick your butt in {i}Street Kombat{/i} another day."
    eve f_happy @ f_laugh "Hehe, yeah right!"
    eve "In your dreams."
    anon f_normal @ f_laugh "Hehe!"
    hide eve
    show anon b_hug_eve f_shy_down
    with dissolve
    pause
    eve "See you tomorrow?"
    anon "Of course."
    pause
    show eve f_happy
    show anon b_dressed f_normal
    with dissolve
    eve "Okay."
    pause
    eve @ a_wave "See ya."
    anon @ a_wave "Later, {b}Eve{/b}."
    hide anon with dissolve
    return

label eve_button_voyeurism_follow_roof:
    scene expression player.location.background_closeup with None
    show anon
    show eve
    with dissolve
    anon "Wow, this is awesome!"
    eve f_happy "Hehe, you think so?"
    anon "Definitely!"
    pause
    anon "This all belongs to {b}Tuuku{/b}?"
    eve "Most of it, yeah."
    eve "He occasionally needs a place to crash or hideout and {b}Grace{/b} won't let him in the apartment."
    eve "So he built all of this."
    anon "Do those speakers work?"
    eve "If we plug them in, sure."
    eve "{b}Tuuku{/b} likes to play music for his plants sometimes."
    anon f_worried "He plays music for his marijuana plants?"
    eve @ f_laugh "Hehe, yeah."
    eve "He says it helps them grow."
    anon f_normal @ f_confused "Does that really work?"
    eve @ f_eyeroll "No idea."
    pause
    anon @ f_laugh "It's so cool!"
    eve "Why don't you go sit down over there and I'll grab us some beers."
    anon f_worried "Y-you mean on the edge of the roof?"
    eve "Yeah."
    pause
    eve "You're not afraid of heights, are you?"
    anon "N-no, I'm not scared of heights..."
    hide eve with dissolve
    eve "Hehe!"
    anon f_sad_down "I'm scared of falling."
    hide anon with dissolve
    scene expression "backgrounds/location_tattoo_rooftop_ledge.jpg" with None
    show eve b_sidebed f_disgusted a_beer_hold
    show anon b_sit:
        yoffset 20
    with dissolve
    eve "Aww man, they're hot."
    pause
    eve f_happy "You want one?"
    anon f_unimpressed "You're asking me if I want hot beer?"
    eve @ f_laugh "Hehe, yeah."
    pause
    anon "How long has it been up here again?"
    eve "No idea."
    pause
    anon "I think I'll pass."
    show anon f_normal
    eve "Probably a smart move..."
    show eve f_drink a_beer_drink with dissolve
    pause
    eve a_beer_hold f_disgusted_wince_down "EUGH!!"
    eve f_disgusted "Okay, definitely a smart move."
    eve "That's awful!"
    anon @ f_laugh "Haha!"
    pause
    eve f_happy "Quite the view, isn't it?"
    anon "Yeah, you can pretty much see the entire town from up here..."
    eve "Yeah, pretty much."
    pause
    anon "So tell me more about {b}Odette{/b} and {b}Grace{/b}."
    eve @ f_confused -m_talk "Hmm?"
    eve f_nervous "Oh, right."
    eve "There really isn't much to talk about."
    eve @ f_eyeroll "{b}Odette{/b} has had a crush on {b}Grace{/b} like, forever."
    anon @ f_confused "I thought they were just friends?"
    eve "Well, that's kinda what I'm saying."
    eve "They are just friends and have been since they were little kids but..."
    eve "... {b}Odette{/b} wants to be more."
    anon "And your sister doesn't?"
    eve @ f_eyeroll "My sister has no idea {b}Odette{/b} likes her..."
    anon @ f_surprised "Really?"
    eve "Yeah."
    eve "It's the weirdest thing."
    eve "{b}Odette{/b} has always been able to seduce any guy she wants at the drop of a hat..."
    anon "Uh huh."
    eve "It's like, easy as pie for her."
    eve "... But when it comes to my sister, she turns into a totally different person."
    eve "She gets super awkward and clumsy, always saying the wrong thing..."
    eve "It's kinda hilarious, if I'm being honest."
    anon "Sounds like she's in love."
    eve f_laugh "Haha, yeah right!"
    eve "{b}Odette{/b} in love."
    eve f_happy "Good one."
    show eve f_drink a_beer_drink with dissolve
    pause
    eve a_beer_hold f_disgusted_wince_down "Eugh."
    anon @ f_confused "Why are you still drinking that stuff?"
    eve @ f_burp "{i}*Burp*{/i}"
    eve f_nervous_down "I have a feeling before the night is over, I'm going to need it..."
    anon f_worried "What does that mean?"
    eve f_nervous @ f_laugh "Hehe, never mind."
    show anon f_thinking
    pause
    anon f_normal @ f_confused "So, {b}Odette{/b} is bi?"
    eve "Guess so."
    anon "And your sister isn't?"
    eve "As far as I know, she isn't."
    anon @ -m_talk "Mmhmm."
    pause
    anon f_skeptical "What about you?"
    eve f_nervous_down "M-me?"
    anon f_flirt "Yeah, you."
    show eve f_drink a_beer_drink with dissolve
    pause
    eve a_beer_hold f_disgusted_wince_down "Eugh."
    eve f_nervous_down "I dunno..."
    anon f_normal "You don't know?"
    eve "I've never really thought about it."
    pause
    anon @ f_laugh "Heh, well, think about it!"
    pause
    eve "I guess I could be."
    anon @ f_surprised "Really?"
    eve f_nervous "I mean, yeah, with the right girl..."
    eve "Gender isn't as important as personality... At least, that's what I think."
    anon f_flirt "Interesting."
    show eve f_nervous_down
    pause
    eve f_nervous "What about you?"
    anon f_surprised @ -m_talk "Hmm?"
    eve "Could you see yourself being with another guy?"
    show anon f_thinking
    menu:
        "No way.":
            anon f_unimpressed "Guys are gross!"
            eve f_happy @ f_disgusted "So, you're saying... You're gross?"
            anon f_normal @ f_laugh "Oh, totally!"
            anon "I don't know how you put up with me..."
            anon "... I'm disgusting!"
            eve @ f_laugh "Hahaha!"
            eve "You always know how to make me laugh!"
            anon "That's a good thing, yeah?"
            eve "Yes, very good."
            $ M_eve.set("biggus_dickus", "")
        "Maybe.":

            anon f_shy "I don't know."
            anon "I've never thought about it."
            pause
            eve f_happy @ f_laugh "Hahaha!"
            anon f_normal "What?"
            eve "Well, think about it!"
            anon "Hehe, alright."
            show anon f_thinking
            show eve f_drink a_beer_drink with dissolve
            pause
            show eve f_disgusted a_beer_hold with dissolve
            anon @ -m_talk "Hmm."
            pause
            eve f_happy "Well?!"
            anon "I'm thinking!"
            eve @ f_laugh "Hahaha!"
            pause
            anon f_shy "I suppose I agree with you..."
            anon f_normal @ f_brag_closed "Personality is more important than gender."
            eve f_surprised "Really?"
            anon "Yup."
            eve f_nervous_down "I wasn't expecting that."

    show eve f_drink a_beer_drink with dissolve
    pause
    eve a_beer_hold f_disgusted_wince_down "Eugh, I'm never gonna get used to this stuff."
    anon "Stop drinking it!"
    eve f_disgusted "No, no, no... Trust me, I need it."
    anon f_confused "For what?"
    eve "Just-"
    pause
    eve f_nervous "Just shut up!"
    anon f_normal "Okay..."
    eve f_nervous_down a_idle "Here."
    show eve f_nervous a_paper
    show expression "characters/eve/eve_arms_sidebed_a_paper.png"
    with dissolve
    anon "What's this?"
    eve "It's for you."
    eve f_nervous_down "I uhh... Kinda... Made it for you."
    hide expression "characters/eve/eve_arms_sidebed_a_paper.png"
    show eve a_idle
    show anon f_surprised a_paper
    with dissolve
    anon "Really?"
    scene expression player.location.background_blur
    show expression "objects/closeup_drawing_02.png" as drawing with fade
    anon "Whoa!"
    pause
    anon "You drew this?"
    eve "Y-yeah."
    pause
    eve "You like it?"
    anon "I love it!"
    pause
    hide drawing
    scene expression "backgrounds/location_tattoo_rooftop_ledge.jpg"
    show eve b_sidebed f_happy
    show anon b_sit a_paper zorder 1:
        yoffset 20
    with fade
    anon "I can't believe you made this for me!"
    eve "W-well, the other day you said you liked the whole Bonnie and Clyde thing..."
    anon "Yeah, I remember!"
    eve f_nervous_down "... And I was thinking of you and doodling, and... It just... Sorta, happened."
    anon "This is really cool, {b}Eve{/b}!"
    anon "Thank you!"
    eve f_happy @ f_laugh "Hehe, you're welcome."
    pause
    anon @ f_laugh "Wow, look at you in that dress!"
    eve f_nervous_down "Y-you like that?"
    anon "Of course!"
    anon f_flirt "You look hot!"
    eve f_happy @ f_laugh "Shut up!"
    anon "What?!"
    anon f_normal "You do!"
    pause
    show anon a_idle with dissolve
    pause
    show eve f_nervous_down
    pause
    eve "Thank you, by the way..."
    anon @ -m_talk "Hmm?"
    eve f_nervous "For cheering me up the other day!"
    anon "Of course."
    pause
    show eve f_nervous_down
    pause
    anon f_flirt "So, you were thinking about me, huh?"
    eve f_surprised @ -m_talk "!!!"
    eve "Heh, uhh..."
    eve f_nervous @ f_laugh "New subject!"
    anon f_normal "Aww, c'mon!"
    eve "Oh, I've got an idea!"
    hide eve with dissolve
    anon @ f_worried "Where are you going?"
    eve "Just hold on."
    pause
    eve "I know they're here somewhere..."
    pause
    anon "Do you need help?"
    eve "No, I've got it."
    pause
    eve "Ah hah!"
    pause
    show eve b_sidebed f_happy a_binocular zorder 0 with dissolve
    eve "Found em."
    anon @ f_confused "Binoculars?"
    eve "Yeah."
    eve "Like you said, we can pretty much see the entire town from up here."
    eve @ f_laugh "So, let's do some people watching!"
    anon "You wanna spy on people?"
    eve f_confused "You've never done that, before?"
    anon f_worried_low "N-no..."
    eve f_happy @ f_eyeroll "Yeah, right."
    anon "Okay, maybe a little..."
    eve "Liar!"
    show eve f_normal_out a_binocular_look with dissolve
    show anon f_normal
    pause
    eve @ -m_talk "Hmm."
    anon "You see anything?"
    eve "Not yet."
    pause
    eve "Looks like {b}Tyrone{/b} and his goons aren't in the park tonight."
    anon @ f_laugh "Heh, yeah... They're probably at home still trying to scrub those stink bombs off!"
    show eve a_binocular with dissolve
    eve @ f_laugh "Hahaha!"
    pause
    show eve f_normal_out a_binocular_look with dissolve
    pause
    eve "Oh my god..."
    anon @ -m_talk "Hmm?"
    eve "There's two topless ladies jogging in the park!"
    show anon f_shock:
        flip
        xoffset -350
    with fastdissolve
    anon "T-topless?"
    anon f_normal_out "You're lying."
    show eve a_binocular_give
    show expression "characters/eve/eve_arms_sidebed_a_binocular_give.png" zorder 2
    with dissolve
    eve "No seriously!"
    show anon a_binocular
    show eve f_normal_out a_point
    hide expression "characters/eve/eve_arms_sidebed_a_binocular_give.png"
    show expression "characters/eve/eve_arms_sidebed_a_point.png" zorder 2
    with dissolve
    eve "Check it out!"
    show eve a_idle
    hide expression "characters/eve/eve_arms_sidebed_a_point.png"
    show anon a_binocular_look
    with dissolve
    pause
    anon "!!!"
    scene expression "backgrounds/location_tattoo_rooftop_spy01.jpg" with fade
    pause
    anon "{b}M-Mrs. Johnson{/b}?"
    eve "Do you know them?"
    anon "Ehh, yeah..."
    anon "The redhead is my friend's landlady."
    eve "Whoa, really?"
    scene expression "backgrounds/location_tattoo_rooftop_ledge.jpg"
    show eve b_sidebed
    show anon b_sit a_binocular_give:
        flip
        xoffset -350
        yoffset 20
    with fade
    anon "You know {b}Erik{/b}?"
    show anon a_idle
    show eve a_binocular f_confused
    with dissolve
    eve "The fat kid with all the freckles?"
    anon "Y-yeah."
    show eve f_normal_out a_binocular_look with dissolve
    eve "That's his landlady?!"
    anon "Yeah."
    eve "Wow, she's really hot..."
    anon f_flirt "... Yeah."
    pause
    eve "I wonder who the other girl is?"
    anon f_normal @ f_skeptical "One of her friends from yoga class, I think..."
    pause
    eve "Why are they topless?"
    anon "No idea."
    pause
    eve "Hmm, kinky."
    pause
    eve "!!!"
    pause
    eve "Heh, again?"
    show eve f_sexy a_binocular_give
    show expression "characters/eve/eve_arms_sidebed_a_binocular_give.png"
    with dissolve
    eve "You're going to like this one..."
    anon f_normal_left @ -m_talk "Hmm?"
    show anon a_binocular
    show eve f_normal_out a_point
    hide expression "characters/eve/eve_arms_sidebed_a_binocular_give.png"
    show expression "characters/eve/eve_arms_sidebed_a_point.png"
    with dissolve
    eve "The apartment building over there, second floor, left most window."
    hide expression "characters/eve/eve_arms_sidebed_a_point.png"
    show eve a_idle f_sexy
    show anon f_normal_out a_binocular_look
    with dissolve
    anon "O-okay."
    pause
    anon "!!!"
    scene expression "backgrounds/location_tattoo_rooftop_spy02.jpg" with fade
    anon "Is that-"
    eve "That's {b}Mrs. Kim{/b}."
    eve "She works the counter down at the bank..."
    anon "Y-yeah, I've seen her there before."
    pause
    anon "She's masturbating..."
    pause
    scene expression "backgrounds/location_tattoo_rooftop_ledge.jpg"
    show eve b_sidebed f_sexy
    show anon b_sit f_normal_out a_binocular_look:
        flip
        xoffset -350
        yoffset 20
    with fade
    anon "Is that her husband lying next to her?"
    eve "Yeah, the fat ugly one."
    pause
    show anon f_normal_left a_binocular with dissolve
    eve "She does this a lot."
    show eve a_binocular
    show anon a_idle
    with dissolve
    anon "You mean, you've spied on her before?"
    eve "Yeah, {b}Tuuku{/b} found her one day when we were all up here."
    show eve f_normal_out a_binocular_look with dissolve
    eve "He watches her all the time."
    anon "That's kinda creepy, isn't it?"
    eve "Well, she's the one masturbating in front of a window..."
    eve "If she doesn't want people to see, she should buy some curtains!"
    pause
    anon "Yeah, I suppose that's true."
    eve "I just feel sorry for her."
    eve "You know her husband probably can't satisfy her needs..."
    anon f_surprised_left @ -m_talk "..."
    pause
    eve "Hmm, nothing going on at the library tonight."
    show anon f_normal_out
    eve "That's unusual."
    anon "Is it?"
    show eve f_happy a_binocular with dissolve
    eve "Totally."
    eve "Ever since they started holding sex addicts meetings there, people have been fucking all over the place."
    show eve f_normal_out a_binocular_look with dissolve
    anon f_normal @ f_normal_left "Really?"
    eve "Hehe, yup."
    pause
    eve "!!!"
    pause
    eve "Aww."
    anon f_normal_left "Did you find something?"
    eve "Yeah."
    show eve a_binocular_give f_happy
    show expression "characters/eve/eve_arms_sidebed_a_binocular_give.png"
    with dissolve
    eve "You wanna look along the shoreline for a pier."
    show anon f_normal_out a_binocular
    show eve a_point f_normal_out
    hide expression "characters/eve/eve_arms_sidebed_a_binocular_give.png"
    show expression "characters/eve/eve_arms_sidebed_a_point.png"
    with dissolve
    eve "Right over there."
    show anon a_binocular_look
    hide expression "characters/eve/eve_arms_sidebed_a_point.png"
    show eve a_idle
    with dissolve
    anon "Okay."
    pause
    anon "!!!"
    scene expression "backgrounds/location_tattoo_rooftop_spy03.jpg" with fade
    anon "I see them."
    eve "They're watching the sunset together."
    eve "Isn't it romantic?"
    anon "Y-yeah, I suppose."
    pause
    anon "I think she's naked."
    pause
    scene expression "backgrounds/location_tattoo_rooftop_ledge.jpg"
    show eve b_sidebed f_eyeroll
    show anon b_sit f_normal_out a_binocular_look:
        flip
        xoffset -350
        yoffset 20
    with fade
    eve "Typical guy..."
    eve f_happy "Two people sharing a beautiful moment together and all you care about is that she's naked."
    show anon f_normal_left a_binocular with dissolve
    pause
    show anon a_idle
    show eve a_binocular
    with dissolve
    anon "Heh, sorry."
    show eve f_normal_out a_binocular_look with dissolve
    eve "No, it's okay... I get it."
    pause
    eve "She is really pretty."
    pause
    eve @ -m_talk "Hmm."
    pause
    eve "I guess that's it."
    show eve a_idle f_happy
    hide anon
    show anon b_sit:
        yoffset 20
    with dissolve
    pause
    anon "So..."
    pause
    anon "Now what?"
    eve f_nervous_down a_cover "It's kinda cold out here, don't you think?"
    anon "A little bit."
    eve "Why don't we go check out the tent?"
    eve "It might be warmer in there."
    anon "Are you sure {b}Tuuku{/b} won't mind?"
    eve f_happy @ f_laugh "Yeah, so long as we don't break any of his stuff."
    eve "C'mon, I'll race you!"
    hide eve with dissolve
    anon f_unimpressed @ f_worried "Hey, no fair!"
    eve "Hahaha!"
    anon "Cheater."
    return

label eve_button_voyeurism_meetup:
    scene expression player.location.background_closeup with None
    show anon
    show eve f_happy
    with dissolve
    anon "Hi."
    eve "Hey, {b}[firstname]{/b}."
    eve "You still {b}coming over tonight{/b}?"
    anon @ f_laugh "Yup, I'll be there."
    eve "I'm going to find us something REALLY scary to watch!"
    anon "Heh, can't wait."
    eve "Yeah, me neither!"
    hide anon with dissolve
    return

label eve_button_voyeurism_start:
    scene expression player.location.background_closeup with None
    show anon
    show eve f_happy
    with dissolve
    anon @ a_wave "H-hey."
    eve "{b}[firstname]{/b}!"
    hide eve
    show anon b_hug_eve f_shy_down
    with dissolve
    eve "It's good to see you!"
    anon "Heh, you're in a good mood today..."
    eve "Thanks to you!"
    show anon b_dressed f_normal a_behind_head
    show eve f_happy
    with dissolve
    anon "I'm just glad you're feeling better."
    eve @ f_laugh "Yes, much better."
    pause
    eve "Say, are you busy this evening?"
    anon a_idle @ -m_talk "Hmm?"
    anon "I'm not sure yet, why?"
    eve "You wanna come over and hang out?"
    anon "Yeah, okay."
    eve "{b}Grace{/b} and {b}Odette{/b} are heading into the city to pick up some second hand tattoo gun that {b}Grace{/b} found online."
    eve "So, we should have the house to ourselves for a while."
    anon "Oh?"
    eve "Yeah, I figured we could sneak a couple of {b}Odette{/b}'s beers out of the fridge and watch a scary movie or something?"
    anon @ f_laugh "I'm down for that!"
    eve @ f_laugh "Awesome!"
    eve "I'm super excited!"
    anon @ a_wave "{b}I'll see you tonight then{/b}."
    eve @ a_wave "See you, {b}[firstname]{/b}."
    hide anon with dissolve
    return

label eve_button_police_trouble:
    scene expression player.location.background_closeup
    show grace f_angry a_hips_mad
    show eve f_sad_down:
        flip
    with fade
    grace "Yeah, that's great... Can I use your sorries to pay this fine?!"
    eve @ -m_talk "..."
    grace "Three thousand dollars, {b}Eve{/b}!"
    grace "You know, we're barely getting by as it is!"
    eve f_sad_down @ a_wipe_tears "{i}*Sniff*{/i} I know..."
    grace f_weary a_facepalm "I can't believe you did this..."
    pause
    eve f_sad "It's not fair, everyone does it!"
    grace f_angry a_hips_mad "No, they don't."
    eve f_sad_down "{i}*Sniff*{/i} You and {b}Odette{/b} do..."
    grace @ a_idea "{b}Eve{/b}, there's a big fucking difference between smoking the occasional joint in our home and walking around in public with half a pound of weed in your pocket!"
    eve @ -m_talk "..."
    grace "What did you think was going to happen?!"
    eve "{i}*Sniff*{/i} I'm sorry..."
    grace @ f_angry_yelling_closed a_upset "I'm going to kill {b}Tuuku{/b} when we get home!"
    eve f_surprised "He wasn't involved in this!"
    grace "Pfft, yeah right... I don't believe that for a second."
    eve "He wasn't!"
    show grace f_eyeroll
    pause
    show eve f_cry_down a_wipe_tears with dissolve
    grace f_weary a_facepalm "Just get on the bike and let's get out of here..."
    hide eve with dissolve
    grace f_angry_yelling_closed a_upset "Grr, I dunno what the hell we're gonna do!"
    hide grace with dissolve
    scene expression player.location.background_blur
    show anon f_worried
    with fade
    anon @ -m_talk "( That sounded bad. )"
    anon @ -m_talk "( Poor {b}Eve{/b}... )"
    hide anon with dissolve
    return

label eve_button_prank_douches_park:
    scene expression player.location.background_closeup with None
    show eve f_happy_right:
        flip
        xoffset 250
    show anon f_worried:
        xoffset -100
    show tuuku:
        xoffset 50
    with dissolve
    anon "{b}Eve{/b}?"
    show anon f_normal
    eve f_happy a_hip "See, I told you he would come."
    eve f_happy_right "Hey, {b}[firstname]{/b}!"
    anon "What's going on?"
    eve "Not much."
    show eve f_happy
    tuuku "Ahh, I remember this guy..."
    tuuku "You were at the tattoo shop the other day!"
    anon "Yup, that was me."
    tuuku f_happy "You two banging then?"
    anon f_surprised "!!!"
    eve f_surprised a_rossed "WHAT?!"
    anon f_worried a_behind_head "Uhh..."
    eve f_angry "Don't answer that {b}[firstname]{/b}!"
    eve "He's just being an asshole..."
    tuuku "An asshole?!"
    tuuku f_laugh @ f_confused "For asking little a question?"
    eve "That is not a little question!"
    show tuuku f_happy
    eve @ f_eyeroll "... And besides, I already told you, {b}[firstname]{/b} isn't interested in me!"
    menu:
        "Yes, I am!":
            anon a_rub f_shy_left "Umm, actually..."
            show tuuku f_laugh
            eve f_surprised "!!!"
            eve f_nervous_down "That's not funny, {b}[firstname]{/b}!"
            anon a_idle f_worried "I'm not joking."
            tuuku f_happy @ a_thumb "I knew it!"
            tuuku "You are so clueless when it comes to this stuff..."
            eve "T-that's not-"
            eve a_idle "I mean, he doesn't-"
            pause
            tuuku @ f_eyeroll a_point "Tsk, would you chill out... It's a good thing, {b}Evie{/b}!"
            eve f_angry @ -m_talk "..."
            tuuku @ f_laugh "Isn't she adorable when she's embarrassed?"
            show eve a_flip with dissolve
            pause
            tuuku @ f_laugh "Hahaha!"
            show eve a_idle with dissolve
        "...":

            anon a_rub f_worried_left "..."
            tuuku f_confused "Yeah, but {b}Odette{/b} said-"
            eve f_angry "I don't wanna hear it!"
            eve "It's none of her fucking business..."
            tuuku f_annoyed @ a_point "You don't have to get all defensive, I'm just-"
            eve "... And you should butt out too!"
            show anon f_worried a_idle with dissolve

    tuuku a_arrest "Alright, alright... Sheesh!"
    tuuku f_happy "I'm just saying you two are cute together..."
    show tuuku a_idle with dissolve
    eve "OH MY GOD, DROP IT!!!"
    tuuku @ f_laugh "Hahaha!"
    pause
    tuuku @ a_thumb "I'm {b}Tuuku{/b}, by the way."
    anon f_confused "You're what?"
    tuuku f_normal @ a_thumb "{b}Tuuku{/b}."
    anon @ -m_talk "..."
    anon "What does that mean?"
    eve f_normal_right "It's his name..."
    anon f_worried @ f_surprised a_behind_head "Oh."
    show eve f_normal
    tuuku f_happy "Nickname, actually..."
    tuuku "A bit strange, I know, but the ladies love it!"
    eve @ f_eyeroll a_facepalm "{i}*Snort*{/i} You wish."
    anon "Is there a story behind it?"
    tuuku @ f_wink "Yup, but I can't tell you."
    anon "How come?"
    tuuku f_angry @ a_point "... Because then I'd have to kill you."
    show anon f_surprised_teeth
    eve f_normal_right @ f_laugh "Pfft, yeah right!"
    eve "Don't listen to him, {b}[firstname]{/b}... He's just trying to act cool."
    show anon f_worried
    show eve f_normal
    tuuku f_happy @ a_thumb "Hey, I am cool!"
    eve @ f_eyeroll "Heh, with that hair?"
    eve "It looks like someone gave up halfway through cutting it!"
    show anon f_normal
    tuuku "Aww, not cool {b}Evie{/b}."
    tuuku a_rub "Never make fun of the doo!"
    eve @ f_laugh "Hahahaah!"
    tuuku @ f_laugh "Hehe!"
    show tuuku a_idle
    pause
    tuuku "So, did you fill him in on the plan yet?"
    show eve f_normal_right
    anon "All I know is that we're pulling a prank on {b}Tyrone{/b} and his buddies..."
    show eve f_normal
    tuuku f_normal @ a_point "That's right, we're going to teach those assholes a lesson tonight!"
    tuuku "Nobody messes with {b}Evie{/b} and gets away with it!"
    anon @ f_laugh "Heh, alright... So how do we do that?"
    eve f_normal_right "We're gonna sabotage their stuff!"
    anon f_worried @ f_confused "What do you mean?"
    eve f_normal "Did you bring the goodies?"
    tuuku f_happy "Of course."
    show tuuku a_vials with dissolve
    show eve f_nervous_down
    anon f_worried_low "What are those things?"
    eve f_happy_right "Stink bombs."
    anon @ f_surprised "Stink bombs?!"
    eve @ f_laugh "Hehe, yup!"
    eve "Basically, {b}Tuuku{/b} is going to distract them while you and I sneak these into their bags."
    anon f_confused "How do they work?"
    show eve f_normal
    tuuku "Oh, it's really simple... All you have to do is drop it in there, seal it up, and give it a whack."
    show tuuku a_hips
    show anon a_vials f_worried_low
    with dissolve
    tuuku "These vials shatter super easy and the stinky stuff soaks into everything!"
    eve f_normal_right "Just be really careful, {b}[firstname]{/b}... These things are SUPER powerful."
    anon f_worried "Y-yeah, okay."
    show eve f_happy
    tuuku "If we're lucky, they won't even realize what's happened until they get home."
    eve "Oh, that would be awesome!"
    tuuku "Hehe, the second they open those backpacks, it's going to unleash smellageddon!"
    eve @ f_laugh "Haha!"
    anon "B-but how are you going to distract them?"
    tuuku "Oh, that's the easy part."
    tuuku @ f_laugh a_thumb "I'm their dealer."
    anon f_confused "Huh?"
    eve @ f_laugh "He sells them drugs all the time."
    anon f_surprised "You do?"
    tuuku @ a_shrug "Hey, a man's gotta make a living, right?"
    eve f_confused "I still don't understand why it's okay to sell to them and not me?!"
    eve "We're the exact same age!"
    tuuku f_normal "Umm, because they don't have an {b}older sister{/b} threatening to smash my balls if they get caught with my stuff!"
    show eve f_normal
    anon f_worried @ f_skeptical "Eww..."
    tuuku "Right?!"
    tuuku f_happy @ a_point "See, {b}[firstname]{/b} gets it!"
    eve @ f_eyeroll "Ugh, whatever... Let's just get on with this!"
    show anon f_normal
    tuuku "Heh, gladly."
    tuuku "I'll signal you when I've got their attention."
    tuuku @ a_thumb "Just give me a few minutes to work my magic!"
    hide tuuku with dissolve
    pause
    tuuku "Heeey, what's up my homies?!"
    pause
    anon "He seems nice."
    anon f_worried "Y-you know, for a drug dealer."
    eve @ f_laugh "It's just pot, {b}[firstname]{/b}..."
    eve f_happy_right "He's not an actual drug dealer."
    anon f_shy @ a_behind_head "Heh, I know."
    pause
    anon f_normal a_idle "How do you two know each other?"
    eve @ -m_talk "Hmm?"
    eve "Oh, my sister dated him for a little while back in middle school."
    eve "He's been palling around with her and {b}Odette{/b} ever since."
    anon f_surprised "He dated {b}Grace{/b}?"
    eve @ f_eyeroll "Yeah, for like a month..."
    anon "So are they like, friends with benefits or something?"
    eve f_surprised "What?!"
    eve f_happy_right @ f_laugh "Haha, of course not!"
    eve "{b}Tuuku{/b}'s become more like a brother to us..."
    show eve f_happy
    show anon f_brag_closed a_facepalm with dissolve
    pause
    show anon f_normal a_idle
    show eve f_sad_thinking
    with dissolve
    pause
    eve f_happy "... Or maybe like a dorky cousin, heh."
    eve f_happy_right "Either way, I'm pretty sure they never even kissed."
    anon "Oh."
    pause
    eve @ f_eyeroll "I think {b}Odette{/b} fucked him a couple times, but she pretty much sleeps with everybody, so..."
    anon f_surprised "!!!"
    anon f_flirt "S-she does?"
    eve f_happy "Totally."
    anon f_surprised_down a_cover_boner "{i}*Gulp*{/i}"
    pause
    eve "There's the signal."
    show anon f_surprised
    eve "You ready?"
    anon f_worried "As ready as I'll ever be..."
    eve "Hehe, c'mon!"
    hide eve with dissolve
    anon f_worried_low a_vials "{i}*Sigh*{/i} Here goes nothing..."
    hide anon with dissolve
    return

label eve_button_prank_douches_school:
    scene expression player.location.background_closeup with None
    if player.location != L_school_frenchclassroom:
        show eve f_happy
        show anon
    else:
        show eve b_desk_look_left f_happy:
            xoffset 500
        show anon b_desk zorder 3
    with dissolve
    eve "Don't forget, {b}we're meeting at the park tonight{/b} to get back at those assholes for spraying me!"
    anon f_worried "Will you just tell me what you're planning?"
    eve "No way!"
    eve "I don't wanna ruin the surprise!"
    anon f_tired "Ugh, fine."
    anon "I'll be there."
    eve "It'll be fun, I promise."
    if player.location == L_school_frenchclassroom:
        show expression "characters/eve/eve_overlay_o_chair.png" zorder 1:
            xpos 450
        show expression "characters/eve/eve_overlay_o_desk.png" zorder 2:
            xpos 500
    hide eve
    with dissolve
    pause
    anon f_surprised_teeth "( Man, I really don't wanna start a prank war with {b}Tyrone{/b} and his friends... )"
    anon @ -m_talk "( ... But I can't just leave {b}Eve{/b} to do this on her own. )"
    if player.location != L_school_frenchclassroom:
        show anon f_tired a_facepalm with dissolve
    anon "( I hope she isn't planning anything too crazy. )"
    hide anon
    if player.location == L_school_frenchclassroom:
        show expression "characters/eve/eve_overlay_o_chair.png" as anon_chair zorder 1:
            xpos -50
        show expression "characters/eve/eve_overlay_o_desk.png" as anon_desk zorder 3:
            xpos 0
    with dissolve
    return

label eve_button_prank_roxxy:
    scene expression player.location.background_closeup with None
    show anon f_worried
    show eve f_happy
    with dissolve
    anon "{b}Eve{/b}?"
    eve "Oh, hey {b}[firstname]{/b}!"
    anon f_confused "Why are you hanging out near the locker rooms?"
    eve "I'm waiting..."
    anon "Waiting?"
    anon "Waiting for what?"
    show anon f_worried
    eve "Stick around and you'll find out..."
    anon @ -m_talk "..."
    anon "Umm, okay..."
    pause
    anon @ f_sad_down "I feel like I should apologize to you again for what happened at your house..."
    eve @ f_laugh "Heh, you mean when you burst in on me changing with a raging python in your pants?"
    anon f_tired a_behind_head "Uhh, y-yeah."
    eve "Relax, {b}[firstname]{/b}... It's not that big a deal."
    anon f_worried a_idle "You're not mad?"
    eve f_happy a_hip_angry @ f_laugh "Do I look mad?"
    anon "No."
    pause
    anon f_skeptical "You look really happy."
    eve "Very happy!"
    anon f_worried "Why are you-"
    roxxy "AHHHH!!" with hpunch
    eve @ f_laugh "Hehehe!"
    anon "What the-"
    hide anon with dissolve
    eve "This is going to be good!"
    scene black with fade
    pause
    $ player.go_to(L_school_boysroom)
    scene expression player.location.background_blur
    show roxxy b_undies a_hair f_surprised:
        flip
        xoffset 400
    with None
    show anon f_worried:
        xoffset -200
    with dissolve
    pause
    roxxy f_angry "OH MY GOD!!"
    anon f_shock "!!!"
    show anon f_surprised_teeth
    roxxy "IT'S SPRAY PAINT!"
    roxxy f_worried "NO NO NONONONO!!"
    show missy o_doodles f_yawn a_yawn zorder 1:
        xoffset 50
    with dissolve
    missy "{i}*Yawn*{/i}"
    show missy f_tired a_idle
    missy "What are you yelling about?!"
    roxxy f_angry "LOOK AT MY FUCKING HAIR, YOU IDIOT!!!"
    missy f_normal "Whoa, how did that happen?!"
    roxxy "Somebody replaced my hairspray with paint!"
    show roxxy f_pouting_hair with None
    show becca b_towel:
        flip
        xoffset 200
    with dissolve
    becca "Who is screaming?!"
    missy a_point f_surprised "Holy crap!"
    missy f_laugh "Hahahaha!"
    show missy a_idle
    becca "What?!"
    missy f_normal @ f_laugh "You are orange!"
    becca f_confused "Orange?"
    show becca a_look f_shocked_down
    becca "!!!" with hpunch
    becca f_upset "OH, WHAT THE HELL?!"
    hide becca with dissolve
    missy f_laugh "Hahahaah!"
    missy "Why are you orange?"
    becca "I DON'T KNOW!!"
    missy f_normal @ f_laugh "Hahahaah!"
    pause
    becca "Oh, shit!"
    pause
    show becca b_towel a_bottle f_upset zorder 1:
        flip
        xoffset 200
    becca "Somebody put sunless tanner in my body wash!"
    missy "Seriously?!"
    show becca a_hip
    hide roxxy
    show roxxy b_undies a_hair f_angry zorder 0:
        xoffset -200
    with dissolve
    roxxy "Would you guys shut up?!"
    roxxy "What am I gonna do about my hair?"
    becca "Who cares about your stupid hair?!"
    becca "I'm ORANGE!"
    missy @ f_laugh "PFFFT, HAHAHAHA!!!"
    show roxxy b_undies a_hair f_glaring:
        flip
        xoffset 400
    with dissolve
    show becca f_glaring
    missy "You guys look so ridiculous!"
    roxxy @ -m_talk "..."
    becca @ -m_talk "..."
    missy "W-what?"
    show becca f_upset a_mirror with dissolve
    pause
    missy f_surprised "!!!"
    show becca a_hip
    show missy a_mirror f_confused
    with dissolve
    show roxxy f_angry
    missy "Oh, wow..."
    pause
    missy "There's a dick on my face!"
    becca "No shit?"
    pause
    missy f_surprised "Oh, man... It's so veiny..."
    becca "How did that even happen?"
    missy f_normal a_idle @ a_yawn f_yawn "I don't know... I was sleeping."
    becca "You were sleeping... In the locker room?"
    missy "Yeah?"
    becca @ -m_talk "..."
    missy "I was bored!"
    missy "You two take forever to get ready..."
    becca "Who do you think did this?"
    show missy a_think f_thinking with dissolve
    roxxy "I don't know but whoever it was, they're fucking dead!"
    show anon f_surprised_teeth:
        xoffset -250
    with dissolve
    hide anon with dissolve
    roxxy "I'm serious!"
    show roxxy f_pouting_hair
    missy a_idle f_normal @ a_point "I bet it was those skanky cheerleaders from the B squad..."
    becca "Those sophomore sluts?"
    missy "Yeah, you know they're super jealous of us, right?"
    becca @ f_eyeroll "They don't have the balls to pull something like this!"
    roxxy @ -m_talk "..."
    show missy a_yawn f_yawn with dissolve
    scene black with fade
    pause

    $ player.go_to(L_school_lefthallway)
    scene expression player.location.background_blur with None
    show anon f_surprised
    show eve f_happy
    eve "Hmm, it sounds like {b}Roxxy{/b} and the moron twins are having a rough day..."
    anon "You did that?"
    eve @ f_laugh "Hahahaha!"
    if M_roxxy.finished_inclusive(S_roxxy_end):
        anon f_worried a_rub "Don't you think that was a little extreme?"
        eve @ a_wtf "Psh, relax {b}[firstname]{/b}..."
        eve "It'll all wash out."
        anon "Y-yeah, but-"
        eve f_eyeroll @ a_up "Honestly, I don't know what you see in that bitch..."
        anon a_idle "C'mon, she's not that bad."
        eve f_angry @ a_wtf "She bullies me like, all the time!"
        anon "Yeah, I know..."
        anon "She's just lashing out because her home life sucks."
        eve "Yeah well, regardless... She had this coming."
    else:
        anon f_normal "How did you manage to do all of that?!"
        eve @ a_wtf "Oh, I've got my ways..."
        eve "Pretty good, huh?"
        anon "Heh, yeah..."
        eve @ f_laugh "Hahahaha!"
        anon "I think you may have overreacted a little bit..."
        eve f_eyeroll "Oh, please."
        eve "That's what they get for bullying me!"
    eve f_happy @ f_laugh a_point "And they aren't my only targets!"
    anon f_worried @ -m_talk "Hmm?"
    eve "I'm getting back at {b}Tyrone{/b} and his douchebag friends too!"
    anon a_behind_head "Oh, man... Are you serious?"
    eve "You wanna help?"
    anon a_idle "Ehh, I dunno... What exactly are you planning?"
    eve @ f_laugh "Hehe, you'll see."
    eve "Just {b}meet me in the park tonight{/b}, alright?"
    anon "Y-yeah, okay."
    eve "Don't forget!"
    hide eve with dissolve
    anon "I won't..."
    pause
    anon f_surprised_teeth "( Man, I really don't wanna start a prank war with {b}Tyrone{/b} and his friends... )"
    anon @ -m_talk "( ... But I can't just leave {b}Eve{/b} to do this on her own. )"
    show anon f_tired a_facepalm with dissolve
    anon "( I hope she isn't planning anything too crazy. )"
    hide anon with dissolve
    return

label eve_button_bridgets_help:
    scene expression player.location.background_closeup with None
    if player.location != L_school_frenchclassroom:
        show eve f_sad_down
        show anon
    else:
        show eve b_desk_look_left f_sad_down:
            xoffset 500
        show anon b_desk
    with dissolve
    anon "{b}Eve{/b}!"
    eve f_sad "Hey, {b}[firstname]{/b}."
    anon "You're not going to believe what happened!"
    eve @ -m_talk "Hmm?"
    anon "I asked {b}Coach Bridget{/b} to speak with {b}Mrs. Smith{/b} about the dress code, and she got the entire thing thrown out!"
    eve f_surprised "!!!"
    eve f_nervous "Really?!"
    anon "Yeah, isn't that great?"
    anon "You can keep your blue hair just the way you like it!"
    eve @ f_laugh "That's so awesome, {b}[firstname]{/b}!"
    if player.location == L_school_frenchclassroom:
        show expression "characters/eve/eve_overlay_o_chair.png" zorder 2:
            xpos 450
        show expression "characters/eve/eve_overlay_o_chair.png" as anon_chair zorder 1:
            xpos -50
        show expression "characters/eve/eve_overlay_o_desk.png" zorder 3:
            xpos 500
        show expression "characters/eve/eve_overlay_o_desk.png" as anon_desk zorder 4:
            xpos 0
    hide eve
    show anon b_hug_eve f_surprised_low zorder 2
    with dissolve
    anon "!!!"
    eve "You're the best!"
    anon f_shy_low "Heh, thanks!"
    show eve b_dressed f_nervous_down
    show anon f_shy b_dressed
    with dissolve
    eve "Oh, ehh... Sorry."
    eve f_nervous "I didn't mean to-"
    anon "It's alright."
    anon "That was nice."
    eve "Y-yeah, it was-"
    tyrone "What up, bitches?!"
    if player.location == L_school_frenchclassroom:
        show expression "characters/eve/eve_overlay_o_chair.png" zorder 0
        show anon f_worried zorder 1:
            xoffset -100
    else:
        show anon f_worried zorder 1:
            xoffset -100
    show chad
    show chico a_gun_up:
        xoffset 100
    show tyrone f_smirk:
        xoffset -125
    show eve f_surprised zorder 1:
        flip
        xoffset 200
    with dissolve
    eve "!!!"
    chad "What are you two lovebirds talking about?"
    anon "Nothing, we're just chatting."
    eve f_angry "What the fuck do you cumstains want?"
    tyrone "Again with all that attitude..."
    tyrone "You know you catch more flies with honey, right?"
    eve @ f_eyeroll "Psh, as if..."
    eve "Though it is fitting, that in this metaphor of yours, you guys are shit sipping insects!"
    chad @ f_angry "Meta-huh?"
    tyrone "Tsk, damn girl... Why you gotta be like that?!"
    anon "Can we help you guys with something?"
    tyrone "Heh, yeah actually, I think you can!"
    tyrone "You see, my boy {b}Chico{/b} here was looking to get in some target practice..."
    show eve f_confused
    anon f_confused "Target practice?"
    show chico f_cocky a_gun_down zorder 2 with dissolve
    chico "Say hello to my little friend!"
    show chico a_gun_shoot
    show eve f_surprised a_wtf
    show anon b_dressed_blocking
    anon "!!!" with hpunch
    show anon b_dressed f_surprised
    show chico a_gun_down
    show eve f_sad_down b_dressed_wet
    with dissolve
    eve "Ahh!!!"
    show eve f_angry
    anon f_angry "Dude, what the hell?!"
    tyrone f_laugh "Hahaha!"
    chad @ f_laugh "Hahaha!"
    eve "You fucking assholes!!!"
    tyrone f_smirk "Damn, you got her good yo!"
    eve "Eugh, is this beer?!"
    eve "You sprayed me with fucking beer?!"
    tyrone "Daww, don't get all upset baby..."
    tyrone "Why don't you have your boyfriend there get you a towel while we help you outta those wet clothes, eh?"
    show eve a_sides:
        xoffset 0
    show anon a_point zorder 3:
        xoffset 150
    with dissolve
    anon "You guys need to leave."
    show anon a_sides with dissolve
    chad "Psh, look at him, actin' all tough now."
    chico @ f_laugh "Haha!"
    tyrone "For real, chill out, Opie..."
    tyrone "We're just messing with ya."
    anon "Well, it's not funny!"
    eve f_sad_down "My sister is gonna kill me!"
    tyrone "Sister?"
    show eve f_angry
    tyrone "Mm, I bet she's fine as hell, just like you."
    eve "Fuck off!"
    anon "Seriously guys, go!"
    tyrone "Yeah, yeah... We're leaving."
    tyrone f_laugh "Tell your sister we said hi!"
    show eve zorder 3
    eve @ a_flip -m_talk "..."
    hide chico
    hide chad
    hide tyrone
    with dissolve
    pause
    hide eve
    show eve b_dressed_wet a_wtf f_sad
    show anon f_worried
    eve "{i}*Sigh*{/i} What the hell am I going to do?"
    eve "If I go home reeking of beer, my sister will freak out."
    show eve a_idle
    anon "Can't you sneak in?"
    eve "Mmm, probably not..."
    eve "She usually times her break so she can ask me about my day."
    anon "Hmm, you could come to my place and have a shower if you want."
    anon "My roommate could loan you a set of clean clothes..."
    eve f_sad_down "N-no, I don't think that's a good idea."
    pause
    eve f_sad "Maybe you could come with me and distract {b}Grace{/b} while I change?"
    anon f_confused @ a_thinking "Distract her?"
    eve "Yeah, just ask her some questions or something..."
    anon "Ehh, I mean... I can try."
    eve "Please?!"
    anon f_worried "Y-yeah, okay."
    eve "Thanks, {b}[firstname]{/b}!"
    anon "Here, I'll take your bag."
    eve f_sad_down a_wtf "Eugh, this is disgusting!"
    hide anon
    hide eve
    with dissolve
    return

label eve_button_dress_code_ask_teachers:
    scene expression player.location.background_closeup with None
    show anon
    show eve f_sad_down
    with dissolve
    anon @ a_wave "Hey, {b}Eve{/b}."
    eve f_sad "Hey, {b}[firstname]{/b}."
    anon "You wanna hang out later?"
    eve "Nah, maybe some other time..."
    eve "I just wanna be alone today."
    anon f_worried "Oh, okay... Sure."
    eve "I'll see you around."
    anon "See ya."
    hide eve with dissolve
    pause
    anon @ -m_talk "( Poor {b}Eve{/b}, she just can't catch a break. )"
    anon f_angry @ -m_talk "( {b}I should speak with the teachers{/b} around school about changing this new dress code. )"
    hide anon with dissolve
    return

label eve_button_school_dress_code:
    scene expression player.location.background_closeup with None
    if player.location != L_school_frenchclassroom:
        show eve f_sad_down
        show anon f_worried
    else:
        show eve b_desk_look_left f_sad_down:
            xoffset 500
        show anon b_desk f_worried
    with dissolve
    anon "Hey, {b}Eve{/b}."
    eve "Hey, {b}[firstname]{/b}."
    anon "You wanna hang out later?"
    eve f_sad "Nah, maybe some other time..."
    if player.location != L_school_frenchclassroom:
        show eve a_rossed with dissolve
    eve f_sad_down "I just wanna be alone today."
    anon f_tired "Oh, okay... Sure."
    eve "I'll see you around."
    anon "See ya."
    hide eve with dissolve
    pause
    anon @ -m_talk "( Poor {b}Eve{/b}, she just can't catch a break. )"
    anon f_angry @ -m_talk "( {b}I should speak with Mrs. Smith{/b} about changing this new dress code. )"
    hide anon with dissolve
    return

label eve_button_roxxy_bullying_upset:
    scene school_assembly_hall_closeup_floor
    show eve b_sidebed f_sad_down
    show anon b_sit f_worried with dissolve
    anon "H-hey."
    eve "Hey."
    pause
    anon "What happened?"
    eve "Nothing out of the ordinary."
    eve "Just {b}Roxxy and her idiot friends{/b} being bitches..."
    anon "Oh."
    pause
    anon "Are you alright?"
    eve "Yeah, I'll be fine."
    eve "{i}*Sigh*{/i} S.S.D.D."
    anon f_confused "S.S.D.D.?"
    eve f_nervous "You've never heard of that?"
    anon f_worried "No?"
    eve @ f_laugh "Hehe, it means, \"Same shit, different day\"."
    anon f_laugh "Oh, I get it!"
    anon "Heh."
    show anon f_normal
    show eve f_sad_down
    pause
    anon f_worried "Do they bother you a lot?"
    eve "Nah, I usually just stay out of their way, and they ignore me."
    pause
    eve f_nervous a_hair "{b}[firstname]{/b}, can I ask you something?"
    anon f_normal "Sure!"
    eve "Should I change my hair?"
    anon f_worried "What?!"
    eve "It was {b}Grace{/b}'s idea to dye it blue."
    eve "I wasn't so sure but now that it's done, I really like it."
    pause
    anon "Is that what {b}Roxxy{/b} was teasing you about?"
    eve a_down f_sad_down "Y-yeah, they called me gross..."
    anon f_skeptical "That's ridiculous!"
    eve @ -m_talk "..."
    anon "You're like, the opposite of gross!"
    eve f_confused "The opposite?"
    show anon f_normal
    eve f_nervous "Heh, I'm not sure what that-"
    anon "You're beautiful!"
    eve f_surprised "!!!"
    show eve f_nervous_down
    anon "... And the hair really suits you!"
    eve @ f_eyeroll "Tch, you're just being nice..."
    anon "No, I'm serious!"
    anon "You're beautiful, {b}Eve{/b}."
    eve f_happy "Heh, you sound just like my sister and {b}Odette{/b}."
    show eve f_sad_down
    pause
    eve "If you really got to know me, you wouldn't think that..."
    anon f_worried "What do you mean?"
    eve @ -m_talk "..."
    eve "Never mind."
    pause
    eve f_nervous "We should probably get to class, huh?"
    anon f_shy "Yeah, probably..."
    eve "Thanks for making me feel better, {b}[firstname]{/b}."
    anon "It's no prob-"
    annie "Ah hah!"
    show anon f_surprised_left
    eve f_surprised @ -m_talk "!!!"
    annie "I knew I'd find you two up to no good!"
    show eve b_dressed f_sad a_idle
    show anon b_dressed f_surprised behind eve:
        flip
        xoffset -150
    with dissolve
    show annie at flip with dissolve
    annie "Skipping class, are we?!"
    anon f_worried "N-no, we were just heading there now..."
    annie "Yeah, right."
    annie a_note "I'm writing both of you up for this."
    eve "Are you kidding me?!"
    annie "No, I am not."
    pause
    annie a_note_write @ f_smirk a_note "Hmm, looks like one more strike for you trouble maker and you're getting detention!"
    eve f_angry @ a_wtf "For fuck's sake..."
    eve "Don't you have anything better to do than hassle me all day?!"
    annie f_angry a_note "Hey, watch your mouth!"
    pause
    annie "I'm simply doing my job and enforcing school policy."
    annie f_smirk "Oh, that reminds me..."
    annie "{b}Mrs. Smith{/b} is instituting some new dress codes here in the school."
    annie "Hair dye is now prohibited, so enjoy that blue color while it lasts..."
    eve f_surprised @ -m_talk "!!!"
    annie "Once it's gone, it's gone for good."
    annie "Otherwise, it's expulsion!"
    anon "She can't do that, this is a public school..."
    anon "Public schools don't have dress codes!"
    annie "It's already done."
    show eve f_sad_down a_rossed with dissolve
    annie "Feel free to take it up with her if you have a problem."
    eve @ -m_talk "..."
    annie f_angry a_point1 "Now get your butts to class!!"
    hide annie with dissolve
    eve "This day can't get any worse..."
    hide anon
    show anon f_worried
    with dissolve
    anon "Seriously, she can't do that."
    anon "Let's go and talk to {b}Mrs. Smith{/b}."
    eve "{i}*Sigh*{/i} What's the point?"
    eve "She's just gonna say no and with my luck I'll just make things worse..."
    hide eve with dissolve
    anon @ -m_talk "( Poor {b}Eve{/b}, she just can't catch a break. )"
    anon f_angry @ -m_talk "( {b}I should speak with Mrs. Smith{/b} about changing this new dress code. )"
    hide anon with dissolve
    return

label eve_button_auditorium_bummed:
    scene school_assembly_hall_closeup_floor
    show eve b_sidebed f_sad_down
    pause
    show anon f_worried with dissolve
    anon "{b}Eve{/b}?"
    show eve a_startled f_surprised with hpunch
    eve "!!!"
    eve "What the-"
    eve "{b}[firstname]{/b}?!"
    show eve a_down with dissolve
    eve "Sheesh, you scared the crap out of me!"
    anon "Sorry."
    eve f_nervous "Phew, my heart's pounding!"
    pause
    eve "What are you doing in here anyways?!"
    anon "Well, I saw you arguing with {b}Miss Ross{/b} and then you snuck in here..."
    eve f_confused "Keeping tabs on me, huh?"
    anon "N-no, nothing like that."
    anon "Just making sure you're okay, is all..."
    eve f_nervous "You're worried about me?"
    anon f_normal "Well, we're friends, right?"
    eve "Yeah, I suppose so."
    anon "Friends look after one another."
    eve f_laugh "Heh, that's sappy as hell..."
    anon f_worried "..."
    eve f_wink "... But I kinda like it."
    show anon f_normal
    eve f_happy "Thanks, {b}[firstname]{/b}."
    anon "You're welcome."
    pause
    show eve f_nervous_down
    pause
    anon f_worried "So..."
    anon "You wanna talk about it?"
    eve "Nah, it's stupid."
    anon "Okay, fair enough."
    anon "We'll just talk about something else."
    show eve f_nervous
    anon f_normal "For instance, why you're hanging out in a dark auditorium, all by yourself?"
    eve f_laugh "Heh, I just wanted to blow off some steam."
    show eve f_nervous_down
    anon "Oh?"
    show eve a_idle with dissolve
    pause
    show eve f_nervous a_joint_show with dissolve
    anon f_shock "!!!"
    anon "Where did you get that?!"
    show anon f_worried
    show eve f_nervous_down a_joint with dissolve
    eve "My sister."
    anon f_skeptical "Your sister gave you a joint?"
    eve f_laugh "Oh, god no!"
    eve f_happy "I swiped it from her stash this morning."
    anon "Really?"
    anon f_worried "Won't she be mad?"
    eve @ f_eyeroll "Psh, she probably won't even notice..."
    show eve f_nervous_down a_idle with dissolve
    pause
    show eve a_down with dissolve
    eve @ f_nervous "... And even if she does, she'll just assume one of her friends smoked it."
    anon f_normal "Oh, I see."
    pause
    anon "You two get along pretty good?"
    eve f_confused @ -m_talk "Hmm?"
    anon "You and your sister."
    eve f_nervous "Oh."
    pause
    eve "Yeah, for the most part."
    eve @ f_laugh "Heh, when she's not doing her {i}mom impression{/i}."
    anon f_confused "{i}Mom impression{/i}?"
    eve "Yeah, she's like, trying to set a good example for me or something..."
    pause
    anon f_worried "... And that's a bad thing?"
    eve @ f_eyeroll "It's annoying!"
    eve f_happy "I mean, she used to be so much fun!"
    eve "I'm talking parties, every night!"
    eve "Like, totally living the wild life..."
    eve f_disgusted "... And now, she pretends she doesn't want anything to do with that stuff."
    eve "Even though, everyone can tell, she totally misses it!"
    eve f_sad "It just makes me feel like I'm in the way and-"
    eve f_laugh "Heh."
    show eve f_nervous
    eve "Sorry, I'm being dumb."
    anon "Nah, you're not."
    anon "I get it."
    eve "My sister is actually really awesome!"
    eve "I'm lucky to have her."
    show eve f_normal_up
    pause
    eve f_happy "You know what?!"
    anon f_normal @ -m_talk "Hmm?"
    eve "You should come over and meet her sometime!"
    anon f_worried "T-to your house?"
    eve "Yeah!"
    eve f_nervous "I mean, if you want..."
    anon f_confused "Ehh."
    eve "I can introduce you two."
    anon "S-sure, I guess."
    show anon f_surprised_forward
    show eve f_normal_up
    "{i}*Bell rings*{/i}"
    show anon f_unimpressed a_behind_head with dissolve
    anon "Oh, crap."
    anon "Was that the bell?"
    show anon a_idle with dissolve
    eve f_nervous_down "Heh, I guess the fun is over..."
    eve f_nervous "You can {b}swing by my place tonight{/b}, if you want..."
    show anon f_normal
    eve "... Or {b}any other evening{/b}, for that matter."
    anon "Okay."
    anon "I'll come by soon."
    eve f_laugh "Awesome!"
    show eve a_wave with dissolve
    eve f_happy "Later, {b}[firstname]{/b}!"
    anon "See ya, {b}Eve{/b}."
    hide eve
    hide anon
    with dissolve
    return

label eve_button_ross_argument:
    scene expression player.location.background_blur with None
    show eve f_nervous_down:
        xoffset -50
    show ross f_sad:
        flip
        xoffset 220
    with dissolve
    ross "You have to try, sweetie..."
    eve @ f_eyeroll "..."
    show eve f_sad
    ross "A great artist should be able to spot beauty in anything, especially themselves."
    eve "{i}*Sigh*{/i} I'm trying, it's just..."
    eve f_sad_down "... Complicated."
    ross "I just don't understand why this project is giving you so much trouble..."
    show ross a_touch_comfort with dissolve
    ross "Perhaps you should come by the art room after school, and we'll work on it together?"
    show ross a_sides
    show eve f_sad a_up
    with dissolve
    pause
    eve "N-no, that's okay."
    show eve a_cover f_sad_down with dissolve
    eve "I'd prefer to do this alone."
    ross "Alright."
    pause
    eve f_nervous "I should really get to class, {b}Miss Bissette{/b} will get angry if I'm late again..."
    show ross a_hip with dissolve
    ross f_normal "Oh, pish posh!"
    show eve f_sad_down
    ross "I've never seen {b}Vivienne{/b} get angry with anyone."
    ross "Much less one of her best students!"
    eve @ -m_talk "..."
    show ross f_confused a_hip_angry with dissolve
    ross "Tsk, fine."
    ross "You can go, just as soon as you promise me you'll keep working at it."
    eve "Y-yeah, I will."
    ross f_normal "Good girl."
    ross "We're going to conquer this thing by the end of the semester, okay sweetie?"
    eve f_eyeroll "Uh huh."
    hide eve with dissolve
    pause
    show ross a_yell with dissolve:
        xoffset 600
    ross "Come and see me after school if you need any help!"
    show ross f_sad a_hip with dissolve
    pause
    ross "Poor thing..."
    hide ross
    show anon
    show ross f_sad
    with dissolve
    ross "Oh!"
    if not M_ross.is_state(S_ross_end):
        ross f_normal "Hey there, {b}[firstname]{/b}."
        anon f_normal "Hello, {b}Miss Ross{/b}."
        ross "Shouldn't you be in class?"
        anon "Y-yes, ma'am."
        anon "I'm on my way there now."
        ross "Good, good."
        ross "Remember to come and {b}speak with me{/b} in the {b}art room{/b} soon, okay?"
        ross "If we're going to get those grades of yours up, we'll nee-"
    else:
        ross f_sexy "Hey there, handsome!"
        anon f_flirt "Heh, hi {b}Miss Ross{/b}."
        show ross a_touch_sexy:
            xoffset -200
        with dissolve
        ross "What are you doing out here wandering the halls?"
        anon "Heh, I was just... Uhh..."
        ross "You're not planning on skipping {b}Miss Bissette{/b}'s class are you, naughty boy?"
        ross "Because I was just about to head up to my office and I wouldn't mind a litt-"

    scene location_school_right_hall_cutscene_01
    with fade
    anon "( Hmm? )"
    anon "( Where's {b}Eve{/b} going?! )"
    anon "( That's not {b}Bissette's classroom{/b}. )"
    pause

    scene expression player.location.background_blur
    show anon f_worried
    show ross f_confused:
        xoffset -200
    with fade
    ross "{b}[firstname]{/b}?"
    ross "Did you hear what I said?"
    anon "Oh, I umm... S-sorry, what were you saying?"
    ross "You feeling alright?"
    anon "Y-yeah, totally... I uhh... I mean, no... I-"
    anon "Actually, I am feeling a bit under the weather today..."
    ross "Oh?"
    anon "Yeah, I just need to go sit down, I think..."
    ross f_sad "Alright, well, feel better."
    anon f_normal "Yup, will do!"
    anon "Thanks, {b}Miss Ross{/b}."
    hide ross with dissolve
    anon f_worried @ -m_talk "( Hmm, that was a bit awkward... )"
    anon @ -m_talk "( Oh well, at least I'm free to {b}check up on Eve{/b} now. )"
    anon @ -m_talk "( What could she be doing {b}in the Auditorium{/b}? )"
    hide anon with dissolve
    return

label eve_button_park_hangout:
    show expression player.location.background_closeup with None
    show eve a_artpad f_happy
    show anon
    with dissolve
    eve "Hey, you showed up!"
    anon f_snarky "I said I would, didn't I?"
    anon f_normal "Is this the spot you were talking about?"
    eve @ f_laugh "Yup!"
    show anon f_normal_left
    pause
    anon f_normal "Hmm, this is nice..."
    eve "Hehe, right?!"
    eve "I love it here!"
    eve "I dunno why, but the fountain totally relaxes me."
    anon "Yeah, it makes sense."
    anon @ f_brag_closed "The sound of flowing water, it's soothing."
    eve @ f_laugh "Exactly!"
    anon "You know, if you have a thing for water, we have some great beaches around here."
    anon "You can stick your toes in the sand and listen to the waves lapping against the shoreline."
    eve "Y-yeah?"
    anon "Some really beautiful sunsets too."
    eve f_nervous "Sounds great but isn't there loads of people there?"
    anon "Well, there can be... Especially this time of year."
    eve @ f_laugh "Heh, thanks but I'll just stick to my nice, quiet, secluded fountain..."
    anon @ f_laugh "Heh, fair enough."
    pause
    show eve f_nervous_down
    pause
    anon f_shy "S-so, you got the town figured out yet?"
    eve f_nervous "Yeah, I think so."
    eve "I mean, there's not much to it, really..."
    anon "Heh, true."
    anon "Do you miss the big city?"
    eve f_nervous_down "Mm, not really the city so much..."
    pause
    eve f_nervous "I miss the food."
    anon f_confused "The food?"
    eve "Yeah, there were so many restaurants, and they stayed open like, twenty-four seven."
    eve "There was this great Chinese place near our house."
    eve "I swear, I would kill for an order of their lo-mein!"
    anon f_normal "Hah, I don't even know what that is..."
    eve f_surprised "Seriously?"
    eve f_sad "That's tragic, {b}[firstname]{/b}..."
    anon f_snarky "Tragic, huh?"
    show anon f_grin
    eve f_laugh "Haha, totally."
    show eve f_happy
    pause
    show anon f_normal
    show eve f_nervous_down
    pause
    show anon a_point with dissolve
    anon "So, what are you drawing?"
    show anon a_idle with dissolve
    eve f_confused "Hmm?"
    eve f_normal "Oh, it's nothing... Just doodles."
    anon "Can I see?"
    eve f_nervous_down "Ehh, yeah... I guess."
    show eve a_artpad_show
    pause
    show eve a_crossed f_nervous
    show anon a_artpad_catch
    with dissolve
    pause

    scene location_park_cutscene_02
    show text _ ("I was really surprised when {b}Eve{/b} agreed to let me see her art pad.\nShe was always so protective and secretive with it at school.") as caption
    with fade
    pause
    hide caption with dissolve
    show text _ ("It felt good to know that she trusted me enough to share.\nShe was one of the few people who actually treated me with kindness after all and I was eager to return the favor.") as caption with dissolve
    pause

    scene location_park_cutscene_01
    show text _ ("She was an amazing artist!") as caption
    with fade
    pause
    hide caption with dissolve
    show text _ ("Her style and use of vibrant colors made the character on the page look almost real.") as caption with dissolve
    pause
    hide caption with dissolve
    show text _ ("Like she could spring to life at any moment and fly away into the night.") as caption with dissolve
    pause
    scene expression player.location.background_closeup
    show eve f_nervous:
        xoffset -250
    show anon a_artpad_catch
    with fade
    anon "Whoa, this isn't a doodle..."
    anon "This is awesome!"
    eve "Y-you think?"
    anon "Definitely!"
    anon "Who is it?"
    eve "It's umm... My sister..."
    anon f_shock "Really?"
    eve f_nervous_down "Y-yeah."
    anon f_normal "It's so good!"
    anon "This is like, the kinda stuff people pay good money for, you know?!"
    eve f_eyeroll "Psh, yeah right..."
    show eve f_nervous
    anon "I'm serious!"
    anon "You should do this for a liv-"
    show anon f_surprised_forward
    show expression "characters/anon/anon_overlay_o_can_hit.png":
        flip
        xoffset -500
    with dissolve
    "Tink!"
    show anon a_artpad_rub
    hide expression "characters/anon/anon_overlay_o_can_hit.png"
    with dissolve
    anon f_skeptical "Ow!"
    show eve f_surprised
    anon "What the-"
    chico "Pfft, haHAAH!!"
    show anon f_surprised_teeth a_artpad_catch:
        xoffset -100
    show eve f_disgusted:
        flip
        xoffset 150
    show chad
    show chico:
        xoffset 100
    show tyrone f_smirk:
        xoffset -125
    with dissolve
    tyrone @ f_laugh "Yo, did you see that thing bounce off his head?!"
    show anon f_depressed
    chad "Hahaha!"
    chico "Yeah, it smacked him right in his dumb ass haircut..."
    tyrone @ f_laugh "Hahahaah!!"
    show anon a_artpad_catch with dissolve
    anon f_worried "Why are you guys throwing stuff at me?!"
    eve "Ugh, not this again..."
    eve "How many times do I have to tell you ASSHOLES to leave me alone?!"
    chico "Tch, damn dawg... She's feisty tonight!"
    tyrone "What are you two lovebirds over here lookin' at?"
    eve "None of your business!"
    show anon f_surprised a_surprised_up_both
    show tyrone a_artpad_steal
    with dissolve
    pause
    show anon f_angry a_sides
    show eve a_hip_angry f_angry
    with dissolve
    eve "Hey!!"
    show tyrone a_artpad f_surprised_down with dissolve
    pause
    show tyrone f_uneasy_down
    pause
    show tyrone a_artpad with dissolve
    tyrone f_smirk "Ohoho, DAYUM!!"
    tyrone "Who's this bitch supposed to be? She's fine as hell!"
    anon "Give that back!"
    tyrone "Yo, chill out Opie..."
    tyrone "It ain't like I'm gonna steal it..."
    show tyrone a_artpad_throw with dissolve
    tyrone "Here."
    show anon a_artpad_catch
    show tyrone a_sides
    pause
    show anon a_artpad_sides
    eve "Fuck you, {b}Tyrone{/b}!"
    tyrone "C'mon girl, don't get all bent outta shape..."
    show tyrone a_hands_rub with dissolve
    tyrone "You know you're my main bitch!"
    chad "Haha!"
    eve f_eyeroll "Eugh, in your fucking dreams..."
    tyrone "Why don't you come spit rhymes with us tonight?"
    show eve f_angry
    tyrone "I'll hook you up with more of that kine bud, you like."
    eve "No fucking way!"
    show tyrone a_sides with dissolve
    tyrone "Tch, fine... Be that way."
    pause
    show tyrone a_point with dissolve
    tyrone "What about you?"
    show tyrone a_sides with dissolve
    anon f_worried @ -m_talk "Hmm?"
    tyrone "You wanna come have some fun or you just gonna sit here with little miss flat-ass all night?"
    show eve f_surprised
    pause
    show eve a_cover f_sad_down with dissolve
    eve @ -m_talk "..."
    anon f_angry "Nah, I'm good right here."
    tyrone "Tch, suit yourself."
    tyrone "{b}We'll be right over there if you come to your senses{/b}..."
    show tyrone f_kiss_drink
    pause
    tyrone f_smirk "Bye, Boo..."
    show eve f_angry a_flip with dissolve
    tyrone f_laugh "Hahahaah!"
    hide tyrone
    hide chico
    hide chad
    with dissolve
    pause
    hide eve
    hide anon
    show anon a_artpad_catch f_worried
    show eve f_sad_down
    with dissolve
    pause
    show anon a_artpad_give with dissolve
    anon "You alright?"
    show anon a_idle
    show eve a_artpad
    with dissolve
    eve f_sad_down "Y-yeah."
    anon "You sure?"
    show eve a_crossed with dissolve
    eve f_sad "Yeah, I'm fine..."
    pause
    eve "I should probably be getting home, before my sister gets worried."
    anon "Yeah, okay..."
    eve "Sorry about them."
    anon "It's not your fault."
    show eve:
        flip
        xoffset 650
    with dissolve
    pause
    anon "Hey, {b}Eve{/b}..."
    hide eve
    show eve f_sad with dissolve
    eve @ -m_talk "Hmm?"
    anon "Seriously, don't listen to those guys... They're idiots."
    eve f_nervous "Heh, I know..."
    show eve f_nervous_down
    pause
    eve f_nervous "Thanks, {b}[firstname]{/b}."
    show anon f_grin
    pause
    anon f_shy "Anytime."
    hide eve
    hide anon
    with dissolve
    return

label eve_button_heisenberg:
    scene expression player.location.background_blur
    show player 90
    show player_outfit bb 638e
    with dissolve
    anon "( I better not. Don't want to blow my cover! )"
    hide player
    hide player_outfit
    with dissolve
    return

label eve_button_crypt:
    anon f_worried "I was thinking of {b}visiting Odette in the crypt next full moon{/b}..."
    show eve f_sad
    anon "... Would you maybe... Wanna... Come with me?"
    eve "Are you being serious?"
    anon "Yeah, I think it would really help me figure this whole thing out."
    eve "I don't... Think that's a good idea."
    anon @ -m_talk "Hmm?"
    eve "With my luck, some ghost will follow me home."
    eve "Or a demon will possess me or something."
    anon f_shy "That won't happen."
    anon @ f_laugh "I'll protect you!"
    eve f_normal "You will?"
    anon "Of course."
    anon "You're my girl, remember?"
    show eve f_happy
    pause
    eve "It makes me really happy when you say things like that..."
    anon f_normal "So you'll go?"
    eve f_nervous "Umm..."
    pause
    eve f_sad "... No."
    eve "I can't do it."
    anon f_worried "No?"
    eve "I'm sorry, {b}[firstname]{/b}..."
    eve "Maybe another time."
    anon f_normal "It's alright, {b}Eve{/b}."
    anon "If you're not ready, then you're not ready."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
