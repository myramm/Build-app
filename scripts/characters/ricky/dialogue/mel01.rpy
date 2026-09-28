label mel01_hint_ricky:
    show ricky f_laugh
    show anon f_sad with dissolve:
        flip
    ricky "Phew, that was hard to watch, amigo..."
    anon "You saw that, huh?"
    ricky f_normal "She really laid into you."
    anon "Yeah."
    ricky a_finger "Do not worry, amigo."
    ricky "I will help you!"
    show ricky a_idle with dissolve
    anon f_shy "I'd really appreciate it."
    anon "I don't know the first thing about hot tub maintenance."
    ricky "It's very simple."
    ricky "Come, {b}grab the leaf skimmer{/b} just there and I'll show you."
    hide ricky
    show anon f_confused:
        unflip
        xoffset 500
    with {'master': dissolve}
    anon "{b}Leaf skimmer{/b}?"
    anon f_worried "Y-yeah, okay."
    hide anon with dissolve
    return


label mel01_find_ricky:
    show anon f_worried with dissolve
    ricky "Problem, amigo?"
    anon "Umm, what's a {b}leaf skimmer{/b} exactly?"
    ricky @ f_laugh "Heh, you serious?"
    ricky "It's the little net on a stick."
    ricky @ a_finger_down "On the ground, there."
    show anon f_worried_low
    pause .5
    anon f_normal_low "Oh, I see."
    anon "I'll grab it."
    ricky f_laugh "Go on, friend!" (show_native="Andale, amigo!")
    ricky "{b}Mrs. Rump{/b} will be returning soon."
    hide anon with dissolve
    return


label mel01_help_ricky:
    show anon a_net with dissolve:
        xoffset -150
    anon "Alright, I've got the {b}leaf skimmer{/b}."
    ricky "Very good, amigo."
    ricky "Now, you just need to fish out all of this nastiness."
    show anon f_disgusted_low
    anon "Eugh, what the hell..."
    ricky "Si, the mayor must have enjoyed himself thoroughly last night..."
    anon "{b}Mayor Rump{/b} did this?"
    ricky "He likes to unwind at night."
    anon "It's so disgusting!"
    ricky @ f_laugh "Heh, this is nothing..."
    ricky f_smirk "... You should see it after he has company over!"
    anon f_sad_down "Aww, man."
    ricky "Look on the bright side, eh?"
    ricky "At least the pay is terrible."
    anon @ -m_talk "..."
    ricky f_laugh "Hahahaah!"
    ricky "Hey, nobody said that the job would be easy, amigo."
    anon f_disgusted_low "Yeah, but this is just gross."
    ricky "Once you're done with the skimming, I'll teach you how to check the levels and filter the water."
    anon f_tired "{i}*Sigh*{/i} Okay."
    ricky f_normal "You'll be fine."
    ricky "Just don't think about it."
    hide ricky with dissolve
    pause
    show anon b_dressed_back_cleaning a_net2 with dissolve:
        yoffset 155
    anon "Don't think about it..."
    anon "... Find your happy place."

    call minigame_hottub (1, 5)

    scene expression background(768, 368, 4.) as stage
    show location_rump_backyard_jacuzzi_overlay as hottubback:
        yoffset 140
    show location_rump_backyard_jacuzzi_overlay as hottub:
        yoffset 155
    show anon a_net_wipe f_tired:
        xoffset -150
    show ricky:
        xoffset 150
    with fade
    ricky "Hey, it's looking pretty good!"
    show anon a_net with dissolve
    pause
    ricky f_smirk "Ehh, you missed a spot."
    anon @ -m_talk "Hmm?"
    ricky @ a_finger_tub "Just there."
    show anon b_dressed_back_cleaning a_idle with dissolve:
        yoffset 155
    pause
    show anon b_dressed f_shock a_net_condom:
        yoffset 0
    anon "!!!" with hpunch
    show anon a_net_condom_fling with dissolve
    anon "EUGH!!!"
    show anon a_net f_surprised_teeth
    show ricky f_thinking:
        flip
        xoffset 600
    with dissolve
    pause
    ricky f_smirk @ -m_talk "Hmm."
    show ricky f_laugh with dissolve:
        xoffset 150
        unflip
    ricky "Nice distance!"
    show ricky f_smirk
    anon f_unimpressed a_net_sides "Yeah, thanks."
    anon f_disgusted "You know, I've done some pretty messed-up stuff in my life..."
    anon "... But fishing used condoms out of the mayor's hot tub is like, a whole new level."
    ricky f_sad "It could be worse, amigo."
    anon "I don't see how."
    ricky f_smirk "You could have been here when he used it."
    anon "Eugh..."
    ricky @ f_laugh "Hahahaah!"
    anon "... I did not need that image in my head, {b}Ricky{/b}!"
    ricky f_normal "C'mon, I show you the next step."
    anon f_worried "Okay."
    show ricky b_pull_pants with dissolve:
        yoffset 50
    pause
    show ricky b_dressed a_chlorine with dissolve:
        yoffset 0
    ricky "Okay, here is where the magic happens..."
    anon @ f_confused "What is that?"
    ricky "Chlorine, amigo."
    show ricky a_chlorine_pour1 with dissolve
    pause
    anon f_disgusted_wince "Wow, it's really strong!"
    ricky "Si."
    show anon f_worried_low
    ricky "It's five times stronger than usual."
    ricky "{b}Mrs. Rump{/b} has it special-ordered from Mexico."
    anon f_worried "It's burning my eyes..."
    ricky "Heh, yeah... Be careful you do not inhale too much."
    ricky "It will turn your insides to paste."
    anon f_surprised "!!!"
    anon "Are you serious?!"
    ricky @ f_laugh "Of course not!"
    ricky "You are so gullible, amigo!"
    anon f_unimpressed @ -m_talk "..."
    pause
    anon "Sheesh, how much are you going to pour in there?"
    ricky "All of it, of course."
    ricky "There's no such thing as too much, trust me."
    ricky a_chlorine_pour2 "You'll thank me later."
    anon "Hmm?"
    ricky a_hips @ a_chlorine_throw "Alright, it's time for the last step."
    anon "Okay."
    show ricky b_dressed_back_jacuzzi with dissolve:
        yoffset 155
    ricky "We just turn on the jets and give it about ten minutes to filter the water."
    anon "That's it?"
    show ricky b_dressed with dissolve:
        yoffset 0
    ricky @ f_laugh "That's it!"
    ricky "Piece of cake, eh?"
    anon "Yeah, I guess."
    melonia "{i}*Ahem*{/i}"
    show anon f_shock with dissolve:
        flip
        xoffset -250
    anon "!!!"
    show anon f_worried
    show melonia b_swimsuit f_normal with dissolve:
        flip
        xoffset -100
    melonia "How's it going out here, {b}Ricky{/b}?"
    ricky @ f_laugh "Si, es very good, señora."
    ricky "The new kid learns quickly."
    melonia @ f_annoyed -m_talk "Mhmm."
    melonia "I trust he can learn to be on time from now on then?"
    anon "Y-yes, ma'am."
    melonia "See to it that he gets a proper uniform."
    ricky "It would be my pleasure, ma'am."
    melonia "And I want you to know, {b}Hector{/b}, that your money for the day is going to {b}Ricky{/b}..."
    anon f_surprised @ -m_talk "Hmm?"
    melonia "... Since he had to take time out of his day to teach you how to do your job."
    ricky f_confused a_up "N-no, it's okay..."
    ricky "... He did most of the work."
    show ricky a_idle with dissolve
    melonia f_annoyed "Nonsense!"
    melonia "I will not reward one of my employees for tardiness and ineptitude!"
    anon f_worried_left "It's fine, {b}Ricky{/b}."
    anon "I don't care."
    ricky "Ehh."
    show anon f_worried
    melonia "Come back and see me once you're finished with him."
    melonia a_shoulder "I'd like you to work on my shoulders again."
    ricky f_normal "Si, señora."
    show melonia a_idle with dissolve
    show anon f_worried_left
    ricky a_finger "Come along, amigo."
    ricky @ f_laugh "It's time for you to hammock up!"
    hide ricky with dissolve
    show melonia f_smirk
    anon f_worried "H-hammock up?"
    hide anon with dissolve
    show melonia f_smirk_down
    pause

    scene expression background(304, 448, 3.) as stage
    show anon f_worried:
        flip
    show ricky a_finger:
        flip
    with fade
    ricky "Now, we must find the perfect hammock for you!"
    anon "{b}Ricky{/b}, I really don't think-"
    ricky "Trust me, my friend!"
    ricky "You're going to look fabulous!"
    show ricky f_laugh a_pocket with dissolve
    anon f_worried_low "Ehh, what are you-"
    ricky a_hammock_bunch f_smirk "Feast your eyes, amigo!"
    anon f_surprised_low a_up "!!!"
    anon f_worried a_sides "Do you just carry those around with you all day?"
    ricky f_confused "Si?"
    pause
    ricky f_smirk "I like to keep my options open."
    ricky @ f_smirk_wink "My little Aztec warrior likes to accessorize!"
    anon @ a_facepalm f_sad_down -m_talk "..."
    ricky "So which one shall it be?!"
    anon f_worried_low "Man, I don't know..."
    ricky "Personally, I think the pink one would look very nice."
    ricky @ f_laugh "And the lace will feel good against your package."
    anon f_worried "No pink."
    ricky f_confused "The purple then?"
    show anon f_tired
    ricky f_smirk @ f_smirk_wink "{b}Mrs. Rump{/b} will not be able to resist the fuzzy balls, eh?"
    anon f_unimpressed @ -m_talk "..."
    ricky @ f_laugh "They will hypnotize her as you work."
    anon f_worried_low "Ehh, I think those are... A bit too..."
    ricky "Fabulous?"
    anon "... Flamboyant..."
    show ricky f_sad
    anon f_worried "... For me."
    ricky "Let's agree to disagree about that."
    anon f_worried_low "Maybe the green one?"
    ricky f_confused "You want the green?"
    ricky "But it's so plain and boring?"
    ricky "I've never worn it even once..."
    anon f_surprised @ f_laugh "PERFECT!"
    show ricky f_sad
    anon "Err, I mean..."
    anon f_worried "{i}*Ahem*{/i} I think I'll ehh... Give that one a try."
    ricky @ -m_talk "..."
    ricky a_hammock_bunch_shrug "Suit yourself."
    show ricky a_idle
    show anon a_hammock
    with dissolve
    anon f_worried_low "Thanks."
    anon "I guess..."
    ricky f_smirk "Now, let's see if it fits."
    anon f_surprised "What, right now?"
    ricky "No time like the present."
    anon f_disgusted "Ehh... N-no, that's okay."
    show anon a_backpack f_looking_down with dissolve
    pause
    anon f_worried a_idle "I think I'll save that for next time."
    ricky f_sad "Aww, you're quite the tease, amigo."
    anon @ -m_talk "..."
    melonia "{b}Ricky{/b}!!"
    show anon f_surprised
    melonia "It's unwise to keep me waiting!!"
    ricky a_whisper f_normal "Si, señora!"
    ricky a_idle "Next time then."
    ricky "Take care, amigo."
    anon f_normal "Y-yeah, see ya, {b}Ricky{/b}."
    hide ricky
    show anon a_wave:
        unflip
        xoffset 500
    with {'master': dissolve}
    ricky "Here I come, señora!"
    show anon a_backpack2 f_looking_down with dissolve:
        flip
        xoffset 0
    pause
    anon a_hammock f_worried_low @ -m_talk "..."
    anon f_sad_down "{i}*Sigh*{/i} What have I gotten myself into?"
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
