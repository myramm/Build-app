label ano16_init_erik:
    show erik
    show anon with dissolve
    anon "Alright, {b}Erik{/b}, we're at our old treehouse..."
    anon "... Can you explain what we're doing now?"
    erik @ f_laugh "It would be my pleasure!"
    erik "But first, we need to climb up."
    anon f_confused "{b}Erik{/b}, can't you just tell me down here?"
    erik f_woozy "Trust me, dude!"
    erik "You're going to love this!"
    hide erik
    show anon f_unimpressed:
        flip
        xoffset -500
    with dissolve
    anon @ -m_talk "..."
    anon f_sad_down a_rub "{i}*Sigh*{/i}"
    hide anon with dissolve
    return


label ano16_tree_erik:
    show erik b_knees a_sonar oh_headset:
        xoffset 120
    show anon f_surprised_low b_onbed_back with dissolve
    erik @ f_laugh "Check it out!"
    anon f_confused "What the heck is that thing?"
    erik "It's a listening device."
    anon "Listening device?"
    erik "Yeah, it amplifies sounds that are far away."
    erik "We can use it to eavesdrop on conversations happening at the mayor's estate."
    anon f_normal @ f_surprised "Whoa, really?"
    erik f_woozy "Pretty cool, huh?"
    anon "It's very cool!"
    pause
    anon "But, umm... How exactly does it work?"
    erik f_normal "It's really simple, dude."
    erik "You just point the gun at whatever you want to listen to..."
    erik a_sonar_point "... And the device will amplify it and then play it back through this headset."
    anon f_shy "Okay, but I just have one question..."
    erik a_sonar "Shoot."
    anon "Why do you have that thing?"
    erik f_worried "Oh."
    erik f_worried_down "Ehh, because..."
    pause
    anon f_snarky "Because?"
    erik @ f_worried "... Because I needed it..."
    pause
    erik "... For umm..."
    erik f_surprised "... Bird watching!"
    anon f_skeptical "Bird watching, huh?"
    erik @ f_normal "Yup."
    anon f_snarky @ f_laugh "Liar."
    erik f_nervous "No, I'm serious!"
    anon @ -m_talk "Mhmm."
    anon "What kind of birds do you watch, {b}Erik{/b}?"
    erik "I don't know..."
    erik "... The ones with feathers?"
    anon @ -m_talk "..."
    erik f_worried "Are we gonna do this thing or not?"
    anon "{i}*Sigh*{/i} Yes..."
    anon "... But we're circling back to this later!"
    pause
    anon f_normal "Now, how do we know where to point that thing?"
    erik "Well, the {b}Rump estate{/b} is too far away to spot conversations without binoculars, so..."
    erik "... We'll have to work as a team."
    erik "Grab that pair of binoculars in the suitcase over there and we'll use them to pinpoint people who are having conversations."
    anon a_binoculars @ f_brag_closed "You mean these?"
    erik "Oh, you've already got them."
    anon a_idle "Yup."
    erik f_worried_down "Now if I can just get this stupid thing working..."
    anon f_worried "It's not working?"
    erik @ f_worried "Not at the moment."
    pause
    erik "It doesn't make any sense, it was working fine the other day!"
    anon "The other day?"
    erik f_normal @ f_laugh "Yeah, I was observing a nice pair of boobies down at the beach."
    anon f_grin @ f_laugh "See, I knew you got that thing to perv on girls!"
    erik f_worried "N-no!"
    pause
    erik "Blue-footed boobies are seafaring birds found along the coastlines of North, South, and Central America!"
    anon f_unimpressed @ -m_talk "..."
    show erik f_woozy
    pause
    anon "I honestly can't tell if you're joking or not."
    erik "What can I say, I like them..."
    pause
    erik f_normal @ f_laugh "... And they're what inspired my highly successful {i}World of Orcette{/i} fanfics."
    anon f_worried "Fanfics?"
    erik f_normal @ f_woozy "Yeah, they chronicle my character's erotic adventures in the harpy-infested mountains of Kol'gath!"
    show anon f_shock
    erik "Harpies are a race of birdlike females that must seek out human men to procreate and fertilize their eggs..."
    erik f_woozy "... And I'm sure I don't have to tell you, they are crazy sexy!"
    pause
    anon f_normal @ f_laugh "I don't even know how to respond to that..."
    erik f_worried_down @ f_angry "Grr, what's wrong with this thing?!"
    anon "Are the batteries dead?"
    erik f_bored "Of course the batteries aren't dead, that's the first thing I checked."
    erik "How stupid do you think I am?"
    anon @ -m_talk "..."
    pause
    anon a_take "Let me have a look."
    erik "No, I've got it..."
    anon f_unimpressed "Dude, give it to me!"
    show anon behind erik
    erik a_sonar_give f_angry "Fine, take it!"
    show erik a_idle
    show anon a_sonar f_disgusted_low
    with dissolve
    pause
    anon "What the-"
    anon f_unimpressed "Why is it all sticky?!"
    erik f_worried_down "I don't know."
    pause
    erik "It's probably just some cheese puff residue..."
    pause
    erik "... Or lubricant."
    anon f_disgusted_low a_sonar_drop1 "Eugh!{p=1}{nw}"
    show anon f_surprised_low a_sonar_drop2
    show erik behind anon
    with dissolve
    erik f_surprised "!!!"
    erik f_angry "What the hell, {b}[firstname]{/b}!"
    show anon f_worried a_idle behind erik
    show erik a_sonar_broken f_worried_down
    with dissolve
    pause
    erik f_sad_down "I paid seventy bucks for this."
    anon "I'm sorry, {b}Erik{/b}..."
    erik "{i}*Sigh*{/i} I guess that's the end of my bird-watching phase..."
    anon "I didn't mean to-"
    erik a_idle f_sad "It's fine."
    erik f_normal @ f_laugh "I was thinking it's time to switch to horses anyways."
    show anon f_unimpressed
    erik "Have I told you about the tribe of centaur warriors they're adding in the next patch?"
    anon "{b}Erik{/b}, let's just use the binoculars and see what we can deduce, yeah?"
    erik "Yeah, okay..."

    scene location_treehouse_window_behind
    show erik f_normal:
        flip
        xoffset 125
        yoffset -100
    show anon a_binocular:
        flip
        xoffset -115
        yoffset -75
    show location_treehouse_window
    with fade
    erik "You want me to go first?"
    anon "No, I'm going first."
    pause
    erik f_bored "Just try not to break these too."
    anon f_unimpressed "Har... Har... Very funny."
    show erik f_normal:
        unflip
        xoffset -280
    show anon f_normal_out a_binocular_look
    with dissolve
    pause
    anon f_worried "What the-"
    erik "You see something?"
    anon "Uhh... Yes."
    pause
    erik f_surprised "Is it the mayor?!"

    scene location_rump_backyard_spy02 with fade
    pause
    anon "God, I hope not..."
    pause
    erik "What do you see, {b}[firstname]{/b}?"
    anon "A gross misuse of the American flag, for starters..."
    pause
    erik "Can you be more specific?"
    anon "Hold on."

    scene location_rump_backyard_spy01 with fade
    pause
    anon "It's a muscular Hispanic fellow in his underpants."
    erik "Huh?"
    anon "And he's talking to a lady in a bikini."
    erik "Oh, nice!"
    erik "Is she hot?!"
    anon "Ehh, she definitely isn't ugly."
    erik "I bet it's the mayor's daughter."
    erik "She's like, super-duper hot!"

    scene location_rump_backyard_spy03 with fade
    pause
    anon "Hmm, it might be."
    pause
    anon "She seems really interested in this guy's underpants."
    erik "What do you mean?"
    anon "She's just staring right at them."
    erik "Aww, man... Now I hope it's not his daughter."

    scene location_treehouse_window_behind
    show erik f_worried:
        xoffset -280
        yoffset -100
    show anon a_binocular f_confused:
        flip
        xoffset -115
        yoffset -75
    show location_treehouse_window
    with fade
    anon "Huh?"
    erik f_worried_right "Was that lady blonde?"
    anon "No."
    erik f_normal @ f_laugh "Phew, okay."
    erik "His daughter is blonde."
    pause
    erik f_woozy "And hopefully single!"
    show anon f_eyeroll
    pause
    show anon f_normal_out a_binocular_look with dissolve
    pause
    anon f_shock "!!!"

    scene location_rump_backyard_spy05 with fade
    erik "What do you see?"
    anon "A young, beautiful, blonde girl."
    erik "{i}*Gasp*{/i} You found her!"
    anon "I think so."
    erik "What's she doing?!"
    anon "She appears to be sunbathing."
    erik "Whoa, really?!"

    scene location_treehouse_window_behind
    show erik f_surprised:
        flip
        xoffset 125
        yoffset -100
    show anon f_flirt a_binocular_look:
        flip
        xoffset -115
        yoffset -75
    show location_treehouse_window
    with fade
    erik "Lemme see!!"
    anon "Hold on."
    erik f_bored "No way, dude!"
    anon f_angry "Stop it, {b}Erik{/b}!"
    erik "It's my turn!"
    show anon a_idle f_unimpressed behind erik
    show erik a_binocular f_normal
    with dissolve
    anon "Alright, calm down!"
    show erik f_woozy a_binocular_look with dissolve:
        unflip
        xoffset -225
    anon "Sheesh."
    erik "Oh, yeah!"
    pause
    erik "There's my future wife!"
    anon f_snarky @ f_laugh "Pfft, in your dreams!"
    anon "You should know by now that girls like that have no interest in guys like us..."
    show erik f_worried a_binocular with dissolve:
        flip
        xoffset 125
    erik "Aww, don't say that."
    anon f_normal "Look at the facts, man."
    anon "She's incredibly gorgeous, built like a runway model, filthy rich, highly educated..."
    erik f_worried_down "Yeah, okay... But-"
    anon "Girls like that only date athletes or famous musicians."
    erik f_woozy "I could be a musician."
    anon @ f_skeptical "Man, be serious."
    erik "I am being serious!"
    show erik a_binocular_look with dissolve:
        unflip
        xoffset -225
    erik "It's a simple thing to respec my character and become a bard."
    anon f_unimpressed @ -m_talk "..."
    show erik f_normal a_binocular with dissolve:
        flip
        xoffset 125
    erik "Bards don't have the raw masculine sex appeal that paladins have but they do get higher charisma scores..."
    erik f_thinking "Do you think I'd have a better chance of seducing her with a lute, or a harp?"
    pause
    show anon a_binocular
    show erik a_idle behind anon
    with dissolve
    anon "Give me those!"
    erik f_worried "Hey!!"
    anon a_binocular_look f_normal_out "You really have to stop talking about video games..."
    erik f_angry "Maybe she likes video games... You ever consider that?!"
    anon "No."

    scene location_rump_backyard_spy06 with fade
    pause
    anon "Huh."
    erik "What now?!"
    anon "Nothing, just a maid bringing her a beverage."
    pause
    anon "Hmm, I wonder if that uniform is mandatory?"
    erik "Uniform?"
    anon "Yeah, she's wearing a pretty skimpy maid uniform."
    erik "Oh, man... Really?!"
    erik "Because I have this thing for sexy maids, dude!"

    scene location_treehouse_window_behind
    show erik:
        xoffset -280
        yoffset -100
    show anon a_binocular f_snarky:
        flip
        xoffset -115
        yoffset -75
    show location_treehouse_window
    with fade
    anon "What don't you have a \"thing\" for?"
    erik @ f_laugh "Heh, true."
    show anon a_binocular_look f_normal_out with dissolve
    pause
    erik "What kind of drink did she bring her?"
    anon "I have no idea."
    anon "Why does that matter?"
    erik f_thinking "Because, if I'm going to win her heart, it's important that I know her likes and dislikes..."
    anon @ -m_talk "Mhmm."
    pause
    erik f_normal "What's she doing now?"
    anon "I don't know."
    erik f_worried "How can you not know?"
    anon "Because I've moved on!"
    anon "We're trying to snoop on the mayor, here... Remember?"
    erik f_sad_down "Aww."
    pause
    anon f_shock "!!!"

    scene location_rump_backyard_spy04 with fade
    anon "There he is!"
    erik "You found him?"
    erik "What's he doing?"
    pause
    anon "Aww, man... That poor girl."
    erik "Huh?"
    anon "He's soaking in a hot tub with this girl I recently became acquainted with and her EXTREMELY annoying husband..."
    erik "Oh."
    pause
    erik "Is she hot?"

    scene location_treehouse_window_behind
    show erik f_woozy:
        xoffset -280
        yoffset -100
    show anon a_binocular f_confused:
        flip
        xoffset -115
        yoffset -75
    show location_treehouse_window
    with fade
    anon "What does that matter?"
    erik "It doesn't, I suppose..."
    show anon a_binocular_look f_normal_out with dissolve
    pause
    erik @ f_laugh "For real though, is she hot?"
    anon f_worried "... She looks miserable!"
    show erik f_worried with dissolve:
        flip
        xoffset 125
    erik "Really?"
    anon a_binocular "Yeah, man... I feel so bad for her."
    erik "Can I see?"
    show erik a_binocular
    show anon a_idle behind erik
    with dissolve
    erik f_normal "Thank you."
    show erik a_binocular_look with dissolve:
        unflip
        xoffset -225
    pause
    erik @ -m_talk "Hmm."
    pause
    anon "You see her?"
    erik f_woozy "Oh, I see her!"
    pause
    erik "Dude, I'd give my anything for a chance to motorboat that booty..."
    anon f_confused "Huh?"
    show erik f_normal_right a_binocular with dissolve
    erik "They say that's how you get pink eye; but for her, I'd totally risk it!"
    show erik f_woozy a_binocular_look with dissolve
    anon f_unimpressed "Are you perving the mayor's daughter again?!"
    erik "No."
    anon f_angry "Alright, give them back."
    erik "Hold on."
    anon "{b}Erik{/b}, I'm serious!"
    erik "Mmm, it's like a work of art..."
    pause
    erik "... Just give me three and a half minutes... Maybe even four--OH CRAP!"
    show erik f_surprised a_idle with dissolve:
        xoffset -315
        yoffset 225
    anon f_surprised_low "What the-"
    erik "Oh crap, oh crap, oh crap!"
    anon f_worried_low "Why are you on the floor?"
    erik "I think she saw me!"
    anon f_shy_low "What do you mean she saw you?!"
    erik "I mean, she looked directly at me!"
    erik "With her eyes!!"
    anon @ f_eyeroll "Nuh uh."
    erik "Dude, I'm not joking!"
    anon a_binocular_look f_normal_out "We're like one hundred yards away from-"

    scene location_rump_backyard_spy07 with fade
    anon "Huh."
    pause
    anon "You're right, she's looking right at us."
    erik "I told you!!"
    pause

    scene location_treehouse_window_behind
    show anon a_binocular f_surprised_low:
        flip
        xoffset -115
        yoffset -75
    show erik f_surprised:
        xoffset -315
        yoffset 225
    show location_treehouse_window
    with fade
    erik "What do we do?"
    anon f_surprised "I don't know!"
    pause
    anon a_binocular_look f_worried "Now she's getting up."
    erik "Does she look mad?"
    anon "She looks really mad."
    erik "Oh my god!"
    pause
    anon "Umm, she's coming this way..."
    erik "Should we run?"
    erik "I feel like we should run!"
    hide erik
    show anon f_worried_low a_binocular
    with {'master': dissolve}
    anon "Where are we gonna run?!"
    show anon a_sides with {'master': dissolve}:
        unflip
        xoffset 230
    anon "We're in a tree..."
    hide anon with {'master': dissolve}
    anon "... And it took you like fifteen minutes to climb up here."

    scene location_treehouse_floor_day
    show erik b_knees f_worried:
        flip
        xoffset -150
    show anon b_onbed_back f_worried behind erik:
        flip
    erik "Hey, don't poke fun!" with fade
    erik "You know I have cardiac arrhythmia!"
    anon "No you don't!"
    erik "Well, I could have... You don't know!"
    anon "Your landlady made that story up to get you out of gym class!"
    erik "Are you sure she's coming this way?!"
    erik "Maybe she forgot about us?"
    anon "I doubt it."
    anon "Poke your head up and look!"
    erik "No way, dude!"

    scene location_treehouse_cutscene01
    show text _ ("She had, indeed, not forgotten about us.") as caption
    with fade
    pause
    hide caption with dissolve
    show text _ ("The mayor's daughter was marching her way over and she was none too pleased that we'd been spying.") as caption with dissolve
    pause
    hide caption with dissolve
    show text _ ("My mind was racing, trying to come up with some way to get out of this...") as caption with dissolve
    pause
    hide caption with dissolve
    show text _ ("... Meanwhile, Erik was having a panic attack.") as caption with dissolve
    pause

    scene location_treehouse_floor_day
    show anon b_onbed_back f_worried:
        flip
    show erik b_knees f_worried:
        flip
        xoffset -100
    with fade
    erik "Aww, man... Why didn't I bring my inhaler!"
    anon "Just calm down."
    erik f_surprised "Calm down?!"
    erik "She's the mayor's daughter, dude!"
    erik f_worried "We're gonna end up in a bunker somewhere, getting waterboarded by Secret Service!"
    anon @ f_laugh "No, we're not."
    anon "Just hunker down and keep quiet."
    anon "Maybe she'll think we ran away."
    erik "You mean hide?!"
    anon "Yes, hide."
    erik "But I suck at hiding!"
    anon @ f_confused "Huh?"
    erik "My dexterity score is minus four!"
    show anon f_unimpressed
    erik "And my armor is infused with holy light!"
    anon "Shh!!"
    erik f_surprised "I glow in the dark, dude!"
    erik f_worried_down "Oh, man."
    erik f_worried a_cover_face "I'm invisible, I'm invisible, I'm invisible!"
    anon f_angry "{b}Erik{/b}, shut up!"
    erik "Stop yelling at me!"
    anon f_unimpressed @ -m_talk "..."
    erik a_idle "{i}*Sigh*{/i} I should have been a wizard..."
    erik "... A wizard could just teleport us out of this mess."
    iwanka "I know you're up there, pervert!"
    show erik f_surprised
    show anon f_surprised
    iwanka "I can hear you whispering to yourself!"
    erik a_cover_face "Eeep!"
    anon f_worried "Damnit, {b}Erik{/b}..."
    iwanka "C'mon, show yourself!"
    pause
    anon "Should we say something?"
    erik "Dude, no!"
    erik "Just ignore her and hopefully she'll go away."
    pause
    iwanka "I'm not leaving until you show yourself!"
    anon f_unimpressed "Any other bright ideas?"
    erik a_idle f_worried_down "Maybe this is just a bad dream?"

    scene location_treehouse_cutscene02
    show text _ ("It was not.") as caption
    with fade
    pause
    hide caption with dissolve
    show text _ ("As we tentatively crept to the edge of the hatch, the mayor's daughter came into view.") as caption with dissolve
    pause
    hide caption with dissolve
    show text _ ("Looking quite livid in her skimpy teal swimsuit.") as caption with dissolve
    pause

    scene location_treehouse_floor_day
    show anon b_onbed_back f_worried:
        flip
    show erik b_knees f_worried_down a_cover_face:
        flip
        xoffset -100
    with fade
    erik "Ugh, I'm gonna throw up."
    anon f_surprised "Don't throw up!"
    erik "Dude, I can't help it... It's a defense mechanism!"
    anon f_worried "I'm sure we can just apologize and everything will be fine..."
    iwanka "Get your butt down here, right now!"
    erik a_idle f_worried "Okay, new plan."
    erik "You go down and apologize..."
    erik "... I'll stay here and keep a look out."
    anon f_unimpressed @ -m_talk "..."
    erik f_surprised "What?!"
    erik "There's no reason both of us have to die!"
    iwanka "Alright, that's it asshole..."
    iwanka "... I'm coming up!"
    anon f_surprised "!!!"
    erik "!!!"
    pause
    erik f_worried a_cover_face "S-she's joking, right?"

    scene location_treehouse_cutscene03
    show text _ ("She was not.") as caption
    with fade
    pause
    hide caption with dissolve
    show text _ ("In fact, she was ascending our makeshift ladder with surprising speed.") as caption with dissolve
    pause

    scene location_treehouse_cutscene04
    show text _ ("I swallowed hard and looked at my friend, wondering exactly what it felt like to be waterboarded...") as caption
    with fade
    pause
    hide caption with dissolve
    show text _ ("Surely, it wouldn't come to that... Right?") as caption with dissolve
    pause

    scene location_treehouse_floor_day
    show anon b_onbed_sit f_worried:
        xoffset 200
    show erik b_knees f_surprised m_talk:
        flip
        xoffset -100
    with fade
    show iwanka b_knees_standing:
        xoffset 100
    show erik f_thinking
    show anon f_worried_high
    with dissolve
    iwanka "Oh, so there's two of you, huh?"
    anon "Look, I don't know what you think you saw, but we-"
    show iwanka b_knees f_annoyed:
        xoffset 200
    show erik f_surprised
    show anon f_worried
    with dissolve
    iwanka "I know exactly what I saw!"
    iwanka @ a_point "You were spying on me with binoculars!"
    anon "Y-yeah, okay... I was using binoculars but I wasn't spying on you, I swear!"
    iwanka "Uh huh."
    iwanka "Is this the part where you tell me you were just bird-watching?"
    anon "N-no."
    iwanka "Because I've heard that bullcrap line before!"
    anon "I was trying to spy on the mayor!"
    iwanka f_disgusted "Eugh, you have some kind of old man fetish or something?"
    anon f_surprised "What?!"
    anon f_disgusted @ a_scared "Eww, no!"
    anon "It's not a sexual thing!"
    iwanka f_thinking "Uh huh."
    anon f_worried "Actually, it's kinda complicated."
    anon "You see, I think my father might have been working for yours and-"
    iwanka "Do these lights work?"
    anon @ f_confused "Huh?"
    iwanka f_annoyed "The Christmas lights, do they work?"
    anon "Yeah, why?"
    iwanka f_normal "I just wasn't expecting this place to be so..."
    anon "Dorky?"
    iwanka @ f_laugh "Farmhouse chic!"
    anon "I don't know what that means."
    iwanka "It's like, charming... But in a rustic, simpleton kind of way."
    anon "Oh?"
    iwanka "Yeah, I kinda dig it."
    anon "T-that's nice, I guess..."
    iwanka f_suspicious "Who are you guys?"
    anon @ -m_talk "Hmm?"
    iwanka "Like, what are your names?"
    anon f_normal @ f_surprised "Oh!"
    anon @ a_wave "Ehh, my name is {b}[firstname]{/b}."
    show iwanka f_normal
    anon @ f_normal_left a_nudge "And this is my best friend {b}Erik{/b}."
    pause
    iwanka f_suspicious "Is he okay?"
    anon f_worried_left "Y-yeah, he just kinda, locks up sometimes..."
    anon f_shy "... When he's around pretty girls."
    iwanka "Weird."
    anon f_worried "Yeah."
    pause
    anon "Umm, what's your name?"
    iwanka f_surprised "You mean, you don't know?"
    anon "N-no, sorry."
    iwanka "That's surprising."
    iwanka f_normal "Usually when I meet new people, they know more about me than my freaking parents..."
    anon "Ehh, yeah... You'll have to forgive me, I'm not much into politics."
    iwanka a_hand "I'm {b}Iwanka{/b}."


    show iwanka a_hand_shake
    show anon a_empty f_normal
    with dissolve
    anon "{b}Iwanka{/b}, huh?"
    anon "That's a unique name."
    show iwanka a_idle
    show anon a_idle
    with dissolve
    iwanka @ f_bored "Yeah, I guess."
    anon "And you're the mayor's daughter?"
    iwanka @ f_snob "His one and only."
    pause
    iwanka "So what do you guys do for fun around here?"
    anon @ -m_talk "Hmm?"
    iwanka @ f_eyeroll "I've been stuck here for a few weeks now and I'm like, literally dying from boredom!"
    anon "Oh?"
    iwanka @ f_eyeroll "There is absolutely nothing here!"
    iwanka "Just a tiny mall with one movie theater and no decent shopping..."
    anon @ -m_talk "..."
    iwanka "There's no dance clubs, no bars... Not even a strip joint!"
    anon f_shy "Yeah, the last one is surprising, isn't it?"
    iwanka "Seriously, there has to be something fun to do in this town!"
    iwanka "And please don't say cow tipping."
    anon f_normal "Well, I suppose most people our age throw parties."
    iwanka f_surprised "Yes!"
    iwanka f_normal @ f_laugh "Parties!"
    iwanka "Now we're getting somewhere!"
    iwanka @ f_suspicious "Where can I find one of these parties?"
    anon @ f_thinking "Ehh, I'm not sure..."
    iwanka "You're not sure, like, you're worried they won't want me there or something?"
    anon f_worried "N-no."
    anon f_sad_down "I just don't get invited to many parties... Is all."
    iwanka f_pouting "Oh."
    iwanka f_annoyed "Well, crap!"
    iwanka f_normal "You're the only people around my age I've met since I've been here..."
    anon f_normal @ f_surprised "Oh?"
    iwanka f_pouting "Yeah, my father doesn't let me go out much."
    iwanka @ f_eyeroll "He's super pissy because I flunked out of college and he like, wants me to go into politics and maybe become the first female president or something..."
    iwanka "... But I'm all like, \"What about my dreams, daddy?!\""
    iwanka @ f_suspicious "Aren't parents the worst?"
    anon "Uhh."
    iwanka a_mime "He's all, \"You can't just let loose, {b}Iwanka{/b}...\""
    iwanka "And, \"Stop being such a slut in public!\""
    iwanka @ f_eyeroll "Blah, blah, blah..."
    iwanka f_annoyed a_idle "Meanwhile, he and {b}Mom{/b} are banging all the help and throwing orgy parties..."
    anon f_surprised "O-orgy parties?"
    iwanka f_disgusted "Eugh, you don't wanna know, trust me."
    iwanka "It's really gross!"
    iwanka "A bunch of old, rich men swapping their trophy wives."
    iwanka "Half of which don't even speak English!"
    anon @ -m_talk "..."
    iwanka "You should have seen this Russian guy he had at the last one..."
    iwanka "... He looked like a goblin!"
    anon @ f_surprised_teeth "!!!"
    anon "You don't say!"
    anon "What else can you tell me about him?"
    iwanka f_normal "What, the goblin guy?"
    anon "Was his name {b}Raz Chernyshevsky{/b}?"
    iwanka f_disgusted b_knees_back @ f_eyeroll a_wave "Umm, who cares?!"
    iwanka "He was disgusting!"
    anon f_worried "Yeah, but-"
    iwanka "He tried to put his hand up my skirt and I told him I'd sooner fuck a donkey than him!"
    anon "Are you're sure he was Russian?"
    iwanka f_normal "No."
    pause
    iwanka @ f_eyeroll "Can we talk about something else, please?"
    anon @ -m_talk "..."
    iwanka f_suspicious "You seriously don't know of any parties?"
    show anon f_thinking
    pause
    anon f_normal "You know, I think I might know of one after all..."
    iwanka f_surprised "Really?"
    anon f_normal_left "What do you think {b}Erik{/b}?"
    erik "..."
    show iwanka f_suspicious
    anon f_worried_left "{b}Erik{/b}?"
    show anon a_nudge with dissolve
    erik -m_talk @ -m_talk "!!!"
    show anon a_idle with dissolve
    erik "H-huh?"
    erik f_worried "Where am I?"
    anon "Can we throw a party for the mayor's daughter in your basement?"
    erik f_surprised m_talk "T-the mayor's... Daughter..."
    show iwanka f_laugh a_wave with dissolve
    iwanka "Hello!"
    show iwanka f_normal a_idle with dissolve
    erik "..."
    anon f_normal @ f_laugh "Pretty sure that's a yes."
    iwanka @ f_laugh "Awesome!"
    anon "It might not be the kind of parties you're used to but-"
    iwanka @ f_eyeroll "Don't worry, anything is better than sitting around with my parents!"
    pause
    iwanka f_suspicious "Unless..."
    iwanka "... There's gonna be alcohol at your party, right?"
    anon "Of course."
    iwanka f_normal @ f_laugh "Okay, good!"
    anon "His house is the green one, just over there."
    iwanka "God, it's gonna feel good to let loose again!"
    iwanka "... I am really going stir crazy shut up in that mansion."
    anon "We'll see you tonight then?"
    iwanka f_smirk "Yeah, I'll sneak over around ten."
    show iwanka b_knees_standing:
        xoffset 100
    show anon f_normal_high
    with dissolve
    pause
    iwanka "Oh!"
    show iwanka b_knees_back_pull f_normal:
        xoffset 150
    show anon f_normal
    with dissolve
    iwanka "What's the dress code?"
    anon f_worried "Dress code?"
    iwanka f_smirk "Yeah, are you thinking like, cocktail dress?"
    anon f_shy "Ehh, just come in whatever makes you feel comfortable."
    iwanka "Interesting..."
    show iwanka b_knees_back with dissolve
    iwanka f_normal "Okay, I'll figure something out."
    iwanka @ a_wave "See you tonight!"
    anon f_normal "Later, {b}Iwanka{/b}."
    hide iwanka with dissolve
    pause
    anon f_normal_left "Phew, that was unexpected!"
    anon "She ended up being pretty cool."
    anon "A little overly chatty but... It sounds like she might have information on the Russian mob boss."
    anon "Don't you think?"
    erik "..."
    anon f_worried_left "Dude, seriously?!"
    show anon a_nudge with dissolve
    erik -m_talk @ -m_talk "!!!"
    show anon a_idle with dissolve
    erik "H-huh?"
    erik f_worried "Where am I?"
    anon f_sad_down "{i}*Sigh*{/i}"

    $ player.go_to(L_treehouse)
    scene expression background(512, 576, 7.) as stage
    show anon
    show erik f_surprised
    with slowfade
    erik "So the mayor's ridiculously hot daughter is coming to my house tonight?!"
    anon "Yes."
    erik "... For a party?"
    anon "Yes."
    erik f_worried "But I've never thrown a party before..."
    anon "Relax, it doesn't have to be a good party."
    anon "We'll just put some music on and dance or something... Try to show her a good time, you know?"
    erik f_surprised "Dance?"
    erik "I don't dance, {b}[firstname]{/b}."
    anon "That's fine."
    anon "Just make sure there's lots of alcohol, yeah?"
    erik f_normal @ f_laugh "Oh, I could have {b}Mrs. Johnson{/b} make some knish!"
    anon "No!"
    erik f_worried "No knish?"
    anon "That'll just weird her out."
    anon "Normal food, like potato chips or cookies or something..."
    erik f_normal @ f_laugh "Oh, okay!"
    anon "Awesome."
    erik f_worried "Umm, you're gonna be there before she shows up, right?"
    anon "Heh, yes {b}Erik{/b}."
    erik "G-good."
    erik "Because I'm not sure I can talk to her."
    anon "What happened to the \"She's my future wife!\" talk?"
    erik "Yeah..."
    erik @ f_normal "... I meant like, in the {i}far{/i} future."
    erik "Not tonight."
    anon "Just try not to lock up again."
    anon "I might need help extracting information from her."
    erik f_worried_down @ -m_talk "..."
    anon "I'll see you {b}tonight{/b}, okay?"
    erik f_worried "Yeah, okay."
    hide erik with dissolve
    pause
    anon @ f_thinking -m_talk "( Hmm, I hope this works... )"
    anon a_thinking @ -m_talk "( I'll never get inside {b}Rump{/b}'s mansion by myself and {b}Iwanka{/b} is the only lead I have... )"
    anon a_idle f_worried @ -m_talk "( ... {b}Tonight{/b} at {b}Erik's house{/b} might be my only chance! )"
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
