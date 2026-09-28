label mel04_init_net:
    scene expression background(768, 368, 4.) as stage
    show location_rump_backyard_jacuzzi_overlay as hottubback:
        yoffset 140
    show location_rump_backyard_jacuzzi_overlay as hottub:
        yoffset 155
    show anon f_worried_low a_backpack with dissolve:
        flip
    pause
    show anon a_hammock with dissolve
    pause
    anon @ -m_talk "( {i}*Sigh*{/i} Here we go again. )"
    show anon f_surprised
    pause
    show anon f_surprised_left
    pause
    show anon b_dressed_changing3 with dissolve
    pause
    show anon b_dressed_changing2 with dissolve
    anon "( This is so embarrassing... )"
    show anon b_naked_undress_bottom with dissolve
    pause
    show anon b_hammock_pickup with dissolve
    pause
    show anon b_hammock f_worried_low a_net with dissolve
    anon @ -m_talk "( Maybe if I hurry, nobody will see me. )"

    call minigame_hottub (5, 10)

    scene expression background(768, 368, 4.) as stage
    show location_rump_backyard_jacuzzi_overlay as hottubback:
        yoffset 140
    show location_rump_backyard_jacuzzi_overlay as hottub:
        yoffset 155
    show anon b_hammock_back_cleaning:
        yoffset 155
    with fade
    pause
    show melonia b_swimsuit f_smirk_down a_glass with dissolve:
        flip
        xoffset -210
    pause
    show melonia f_drink a_glass_drink with dissolve:
        xoffset 400
    pause
    show melonia f_smirk_down a_glass_throw with dissolve
    pause 0.25
    show melonia a_idle f_smirk_low with {'master': dissolve}:
        unflip
        xoffset 0
    "{i}*Glass shatters*{/i}"
    show melonia f_smirk
    show anon b_hammock a_net f_surprised_teeth:
        flip
        offset (-500, 0)
    with fastdissolve
    anon @ -m_talk "!!!"
    anon f_unimpressed a_net_sides @ -m_talk "..."
    show anon with dissolve:
        unflip
        xoffset 0
    anon f_surprised "{b}Mrs. Rump{/b}!"
    anon f_worried "S-sorry, I didn't see you there."
    melonia "Aren't you finished yet, {b}Hector{/b}?"
    melonia "I'm quite ready to cool off."
    anon "Just putting the finishing touches in now, ma'am."
    melonia f_annoyed "Well, enough of that."
    show anon f_flirt_low
    show melonia f_smirk_down a_remove_shall1
    with dissolve
    pause
    show melonia a_remove_shall2 with dissolve
    pause
    show melonia a_remove_shall3 with dissolve
    pause
    show melonia b_jacuzzi_climb with dissolve:
        offset (450, 155)
    melonia "It's been a stressful day and I'm eager to relax."
    show anon f_worried_low
    show melonia b_jacuzzi f_relax a_idle behind hottub:
        xoffset 0
    with dissolve
    anon "Stressful day, ma'am?"
    melonia "Yes, I woke up to my obnoxious husband pawing at me like some sex crazed baboon..."
    melonia "He's well aware of my aversion to his body and yet he insists on pestering me with it."
    melonia @ f_eyeroll "I had to get up and leave the room, I couldn't take it."
    anon @ f_surprised_low -m_talk "..."
    melonia "Our chef came in late and I had to wait almost fifteen minutes for my breakfast."
    melonia "If he wasn't in such high demand I would have fired him on the spot!"
    anon f_bored "Uh huh."
    melonia f_annoyed_up "And then, to top it all off, I had Pilates today with that evil little witch."
    anon f_worried_low "Huh?"
    melonia @ f_eyeroll "My personal trainer."
    melonia "Hannah or whatever..."

    if M_anna.finished_state(S_anna_start):
        anon f_thinking @ -m_talk "( Hannah, huh? )"
        pause
        anon @ -m_talk "( I wonder if she's talking about {b}Mrs. Johnson{/b}'s friend, {b}Anna{/b}? )"
    else:
        anon f_thinking @ -m_talk "( Pilates instructor, huh? )"
        anon @ -m_talk "( I wonder who she's talking about? )"

    show anon f_worried_low
    melonia f_relax "I swear, the woman derives some kind of sick pleasure out of torturing me!"
    anon "Yeah, that sounds... Umm, rough?"
    melonia "Rough doesn't even begin to describe it, {b}Hector{/b}."
    melonia "{i}*Sigh*{/i} But it's the price I have to pay if I want to maintain my figure."
    anon "Sure."
    melonia f_smirk_peek "You were lucky to be born a man."
    melonia f_smirk_up "Men don't need to concern themselves with such things..."
    melonia @ f_laugh "... Especially when they're as gifted as you appear to be."
    anon "Gifted, ma'am?"
    melonia @ f_annoyed_up "Don't play dumb, {b}Hector{/b}."
    melonia "That thong doesn't leave much to the imagination, you know?"
    anon f_surprised_down "T-thong?!"
    anon f_worried_low "Oh, right."
    melonia "I imagine a large cock like that gives you all sorts of advantages, hmm?"
    anon "Ehh, I dunno..."
    anon "... I guess."
    melonia @ f_laugh "You guess?!"
    melonia "Clearly, you don't understand the power you wield..."
    melonia "Why don't you come in here and join me, {b}Hector{/b}?"
    melonia "We can discuss all the ways in which your... {i}*Ahem*{/i} Gift, might benefit you here at the {b}Rump estate{/b}."
    anon "Y-you want me to-"
    show anon f_worried with dissolve:
        flip
        xoffset -500
    anon "Umm."
    show anon f_worried_low with dissolve:
        unflip
        xoffset 0
    anon "What if the mayor finds us?"
    melonia "He won't."
    melonia "I promise."
    anon "{i}*Gulp*{/i} O-okay."
    show anon b_jacuzzi_climb_hammock with dissolve:
        yoffset 155
    melonia f_smirk "That's a good boy."
    show anon b_jacuzzi_naked f_worried a_idle behind hottub with dissolve
    melonia "There, now that feels nice, doesn't it?"
    anon @ f_worried_left "Yes, ma'am."
    melonia f_relax "Mmm, I just love the way the jets caress my lower back..."
    anon "Uh huh."
    show anon f_worried_left
    pause
    melonia f_smirk @ f_smirk_peek "Why are you sitting so far away?"
    show anon f_worried
    melonia "You're not afraid of me, are you?"
    anon "N-no, ma'am."
    anon "I just-"
    anon f_surprised_down "!!!"
    show anon f_surprised with dissolve:
        xoffset -100
    anon "Is that your foot?!"
    melonia @ f_laugh "Hehe!"
    melonia "Well, it's the only thing that will reach you sitting so far away..."
    melonia "Why don't you come a little closer?"
    anon f_worried "Ehh."
    ricky "Hola, señora!"
    show ricky f_smirk_low behind hottubback with dissolve:
        offset (200, 20)
        xzoom -.95
        yzoom .95
    anon f_worried_high "{b}Ricky{/b}, thank goodness!"
    show melonia f_annoyed_up
    anon @ a_whisper_back "{i}*Whispers*{/i} Took you long enough!"
    melonia "We're kinda busy here, {b}Ricky{/b}!"
    ricky @ a_finger "Oh, apologies, señora!"
    ricky "I didn't mean to interrupt."
    ricky "It's just, are you sure he should be in there with you?"
    ricky "If your husband sees-"
    show anon f_worried
    melonia @ f_yell "Oh, screw that old pumpkin!"
    melonia "It would be exactly what he deserves after the obscene display he put on this morning!"
    show anon f_worried_high
    ricky f_confused_low "Obscene display?"
    show anon f_worried
    melonia @ f_eyeroll "Eugh, I'm not getting into it again."
    melonia f_relax "Ask {b}Hector{/b}, if you must know."
    show anon f_worried_high
    ricky f_smirk_low @ a_finger "Ehh, es okay!"
    ricky "We can just forget it."
    pause
    ricky "So, I suppose {b}Hector{/b} here will be giving you your massage today?"
    anon f_surprised_high "!!!"
    melonia f_smirk_peek @ -m_talk "Hmm?"
    ricky "It's Pilates day, si?"
    ricky "And I figure, he's in the tub already... So-"
    show anon f_worried
    melonia f_smirk "Oh, now that's a marvelous idea!"
    show anon f_worried_high
    ricky "He's quite a good masseur."
    show anon f_worried
    melonia "Oh?"
    anon "Ehh."
    show anon f_worried_high
    show melonia f_smirk_up
    ricky "I'm sure he would be more than happy to do so..."
    ricky "... For the right price, of course."
    show anon f_worried
    melonia "Of course."
    melonia "I think two hundred should cover it, don't you?"
    show anon f_worried_high
    ricky @ f_thinking "Mmm, it depends on how thorough you want him to be?"
    show anon f_worried
    melonia @ f_laugh "Oh, he'll need to be very thorough!"
    show anon f_worried_high
    ricky "Perhaps, two hundred and fifty then?"
    ricky @ f_laugh "For that price, he will leave no stone unturned, eh?"
    show anon f_worried
    melonia "Mmm, I like the sound of that."
    melonia "Very well."
    melonia a_money "I'll throw you another hundred to dance for me while he does it!"
    show anon f_worried_high
    ricky @ f_laugh a_finger "Done and done!"
    show ricky b_pull_pants
    show anon f_worried
    show melonia a_idle f_smirk
    with dissolve
    pause
    show ricky b_speedo with dissolve
    show anon f_worried_high
    ricky "Let's get it started, eh?!"
    show anon f_surprised_high
    anon @ a_whisper_back "{i}*Whispers*{/i} Uhh, I have no idea what I'm supposed to do!"
    show ricky a_whisper with dissolve:
        xoffset -250
        xzoom .95
    ricky "{i}*Whispers*{/i} Start with the feet, amigo."
    show ricky a_idle with dissolve:
        xoffset 200
        xzoom -.95
    anon f_worried "Umm, I should probably start with your feet, huh?"
    melonia "Mmm, thorough indeed..."
    show anon f_worried_low a_massage_foot1 with dissolve:
        xoffset 0
    melonia "Don't hold back."
    melonia f_relax "I like a firm touch."
    $ M_ricky.set('sex speed', 0.4)
    hide ricky
    show ricky_body_b_speedo_dance as animation behind hottubback:
        offset (200, 20)
        xzoom -.95
        yzoom .95
    show anon a_massage_foot
    with dissolve
    anon "Y-yes, ma'am."
    ricky "Huah!"
    pause
    ricky "I will bring pleasure to your eyes while {b}Hector{/b} pleasures your body, señora!"
    melonia "Mmm, that feels marvelous, {b}Hector{/b}!"
    pause
    ricky "You are like a goddess today!"
    melonia "Ahh, yes!"
    pause
    ricky "We live, only to please you!"
    show anon a_massage_calf with dissolve
    melonia "Ngh!"
    melonia "Your hands are amazing!"
    pause
    show ricky_body_b_speedo_dance as animation behind hottubback with dissolve:
        xoffset -250
        xzoom .95
    ricky "Take it all in, señora!"
    ricky "It's just for you!"
    show anon f_surprised
    melonia f_smirk_lipbite_moan "Ahh!"
    show anon f_surprised_low
    pause
    anon @ -m_talk "( Is she rubbing herself beneath the water? )"
    show anon f_flirt
    melonia "Don't stop, {b}Hector{/b}!"
    show anon f_flirt_low a_massage_foot_calf with dissolve
    melonia "That's it!"
    pause
    melonia "Oh, god!"
    melonia "Right there!"
    pause
    show ricky_body_b_speedo_dance as animation behind hottubback with dissolve:
        xoffset 200
        xzoom -.95
    ricky "You are getting close to the precipice, señora..."
    ricky "... I can hear it in your voice."
    melonia @ -m_talk "Mhmm!"
    pause
    show anon f_surprised a_idle with dissolve
    melonia f_normal "Alright, enough foreplay!"
    hide animation
    show ricky f_sad_low b_speedo behind hottubback:
        offset (200, 20)
        xzoom -.95
        yzoom .95
    show melonia a_grab_hat f_smirk_lipbite
    with dissolve
    pause
    show melonia b_jacuzzi_hatless a_throw_hat with dissolve
    anon "!!!"
    show melonia a_heart f_smirk with dissolve
    melonia "Come sit behind me {b}Hector{/b}."
    show ricky f_smirk_low
    anon f_worried_high "Ehh."
    show ricky with dissolve:
        xoffset -250
        xzoom .95
    ricky "You must do as the lady commands, my friend."
    ricky "She is paying you for the pleasure, remember?"
    show ricky with {'master': dissolve}:
        xoffset 100
        xzoom -.95
    anon f_worried "O-okay."
    show melonia f_smirk_up
    show anon b_hammock_thrust2 f_worried_low behind melonia:
        offset (250, 100)
    with dissolve
    pause
    show anon b_jacuzzi_naked f_worried:
        flip
        offset (50, 155)
    show melonia f_smirk:
        xoffset -100
    with dissolve
    anon "Like this?"
    melonia "Yes, that's perfect."
    anon "What do you want me to-"
    show anon f_worried_low
    show melonia a_remove1 f_smirk_lipbite
    with dissolve
    pause
    show melonia b_jacuzzi_topless_remove2 with dissolve
    show melonia b_jacuzzi_topless_remove3 with dissolve
    anon f_shock_low "!!!"
    show melonia b_jacuzzi_topless a_idle with dissolve
    anon f_surprised_low "What are you-"
    show melonia b_jacuzzi_topless_leaning:
        xoffset 0
    hide anon
    with dissolve
    pause
    ricky @ f_laugh "Heh, the lady is skipping a few steps..."
    melonia a_grab1 @ f_annoyed_up "Keep dancing, {b}Ricky{/b}!"
    ricky "Si, señora."
    hide ricky
    show ricky_body_b_speedo_dance as animation behind hottubback:
        offset (100, 20)
        xzoom -.95
        yzoom .95
    show melonia a_grab2 f_relax
    with dissolve
    anon "Whoa, this is-"
    melonia "Do you like them, {b}Hector{/b}?"
    pause
    show melonia f_smirk_lipbite2
    anon "Y-yes, they're very nice, ma'am."
    melonia f_smirk "Show me."
    anon "Hmm?"
    melonia @ f_annoyed "Squeeze them, {b}Hector{/b}!"
    anon "O-okay."
    show melonia a_massage with dissolve
    pause
    melonia f_smirk_lipbite2 @ f_relax "Ahh, that's it!"
    pause
    anon "( Okay, yeah... )"
    anon "( She's definitely rubbing herself! )"
    melonia @ f_smirk_lipbite_moan "Mmm!"
    pause
    melonia @ f_smirk_lipbite_moan "Ngh!"
    ricky "Es okay."
    ricky "Let him hear you, señora."
    pause
    melonia f_smirk_lipbite_moan "Oh, {b}Hector{/b}!"
    melonia "It's so good!"
    pause
    ricky "He's really pushing the right buttons, si?"
    melonia "YES!!!"
    pause
    melonia "I'm gonna-"
    show melonia f_smirk_lipbite2
    ricky "Si, señora."
    ricky "Let it out."
    melonia a_massage_nipples f_smirk_lipbite_moan "NGGHHH!!" with flash
    hide animation
    show ricky b_speedo f_smirk_low behind hottubback:
        offset (100, 20)
        xzoom -.95
        yzoom .95
    with dissolve
    pause
    ricky @ f_laugh "Hahaah!"
    show melonia f_relax_exhale m_talk a_idle with dissolve
    ricky "Bravo, amigo!"
    melonia "Oh my..."
    melonia "... I need a second to..."
    melonia "... Catch my breath."
    show melonia -m_talk f_relax
    ricky "Well worth the two hundred and fifty dollars, si?"
    melonia @ -m_talk "Mhmm."
    pause
    melonia f_smirk "You're quite skilled with your hands, {b}Hector{/b}."
    melonia "Perhaps we should retire to my bedroom and test your skill in other areas?"
    anon f_worried "Y-your bedroom?"
    show melonia f_smirk_up
    ricky f_sad_low "Ehh, actually... Señora..."
    ricky "... I think {b}Hector{/b} has another job today."
    melonia f_surprised_up "What?!"
    ricky "Isn't this right, {b}Hector{/b}?"
    anon @ f_skeptical "I do?"
    ricky "Si, you know... That important one..."
    pause
    ricky @ f_smirk_wink "... We discussed earlier?"
    anon f_worried_low @ f_brag_closed "Oh, right!"
    anon "I meant, I do... Yes."
    anon "{i}*Ahem*{/i} Another job."
    show melonia f_surprised b_jacuzzi_topless_getout with dissolve
    melonia "Wait just a sec-"
    show anon b_hammock_thrust2 behind melonia:
        flip
        offset (-360, 100)
    show melonia b_jacuzzi_topless f_pouting
    show ricky f_smirk
    with dissolve
    melonia "Oof!"
    show melonia f_curious
    hide anon
    show anon b_jacuzzi_climb_hammock:
        unflip
        yoffset 155
    with dissolve
    anon "I'm really sorry, ma'am."
    show anon b_hammock f_worried_low:
        offset (-100, 0)
    show melonia f_curious_up b_jacuzzi_topless_edge
    show ricky f_smirk_low
    with dissolve
    melonia "Can't you just cancel?!"
    melonia "I'll-"
    melonia f_pouting_up "Don't you want to take me upstairs?"
    ricky "Perhaps another time, señora?"
    melonia f_curious_up "B-but..."
    show ricky f_sad with dissolve:
        xoffset -350
        xzoom .95
    ricky "You should hurry, amigo."
    show anon f_worried
    ricky "They will get upset if you're late."
    anon "Right."
    show anon f_worried_low a_behind
    show ricky f_smirk_low:
        xoffset 100
        xzoom -.95
    show melonia f_annoyed_up
    with {'master': dissolve}
    anon "See ya, {b}Mrs. Rump{/b}!"
    melonia "This is all very upsetting, {b}Hector{/b}!!"
    hide anon with dissolve
    pause
    melonia f_annoyed @ f_yell "And call me {b}Melonia{/b}!"
    pause
    melonia f_smirk_up "I don't suppose you'd like to go upstairs and-"
    ricky f_smirk_low @ f_laugh "Heh, I'm afraid not, señora."
    show melonia f_annoyed_up
    ricky "As I've explained before..."
    ricky @ a_finger_down "... My pepe only peps for the boys, eh?"
    melonia "Grr!!"
    show melonia b_jacuzzi_topless f_annoyed with dissolve
    melonia "Just forget it!"
    ricky "As you wish, {b}Mrs. Rump{/b}."
    hide ricky with dissolve
    pause
    melonia f_yell "I WILL have that dick, no matter the cost!"

    scene expression background(280, 440, 5, l=L_rump_kitchen, o=1) as stage with fade
    show anon f_flirt_low a_money with dissolve:
        flip
        xoffset -200
    anon @ -m_talk "( Wow, that was intense! )"
    anon @ -m_talk "( The mayor's wife just had an orgasm in my lap... )"
    anon f_laugh -m_talk "( ... And she paid me three hundred dollars! )"
    show anon f_flirt a_idle with dissolve
    pause
    anon f_thinking a_thinking -m_talk "( I wonder if she'd be willing to help me yet? )"
    anon f_laugh -a_thinking -m_talk "( I'll ask her next time. )"
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
