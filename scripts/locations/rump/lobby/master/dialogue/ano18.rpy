label ano18_trap_rump_master:
    scene expression player.location.background_blur
    show anon f_surprised with dissolve
    anon @ -m_talk "( Whoa, this is by far the most lavish bedroom I have ever seen! )"
    anon @ -m_talk "( Look at all that gold... )"
    anon @ -m_talk "( Is this {b}Mayor Rump{/b}'s room? )"
    hide anon with dissolve
    return

label ano18_hide_bed:
    scene expression background(400, 392, 4.) as stage
    show anon f_worried with dissolve
    anon @ -m_talk "( Under the bed seems like my only option. )"
    anon @ -m_talk "( I hope they don't see me! )"
    show anon b_dressed_pickup with dissolve
    hide anon with dissolve

    scene location_rump_bedroom_cutscene01
    show text _ ("My heart was in my throat as I scrambled to get under the bed.") as caption
    with fade
    pause
    hide caption with dissolve
    show text _ ("I couldn't imagine what the mayor would do if he caught me sneaking around his estate and I certainly wasn't eager to find out.") as caption with dissolve
    pause

    scene location_rump_bedroom_under_bed
    show melonia b_feet01
    with fade
    anon "( !!! )"
    iwanka "What do you want, {b}Mother{/b}?"
    show melonia b_feet02 with dissolve
    melonia "Shut the door and get in here."
    melonia "I'm changing."
    show melonia b_feet03 with dissolve
    iwanka "{i}*Sigh*{/i}"
    pause
    show melonia b_feet04
    show iwanka b_feet01
    with dissolve
    melonia "Your father has another meeting with {b}you-know-who{/b} today."
    iwanka "Eugh, again?"
    show melonia b_feet05 with dissolve
    anon "( !!! )"
    melonia "Yes and I want you put on something nice."
    iwanka "I don't wanna go!"
    iwanka "Those guys are so gross!"
    melonia "I didn't ask if you wanted to go..."
    iwanka "C'mon, {b}Mom{/b}... Please, don't make me go!"
    iwanka "R. Smelly invited me out on his yacht today and-"
    melonia "I don't want to hear it!"
    melonia "He's already pissed off that you let that guard into his office..."
    melonia "... You have a responsibility to this family."
    iwanka "Grr, this is so unfair!"
    show melonia b_feet06 with dissolve
    iwanka "Why do I have to be involved in {b}Daddy{/b}'s stupid business dealings?!"
    show melonia b_feet07 with dissolve
    anon "( Is she naked right now? )"
    melonia "Look, I don't want to go either!"
    melonia "But this arrangement has been very beneficial, and they're expecting us to make an appearance."
    iwanka "..."
    melonia "Tsk, don't start pouting!"
    anon "( Maybe I could take a little peek? )"

    scene expression background(288, 400, 4.)
    show iwanka a_crossed f_pouting:
        flip
    show melonia b_naked
    with fade
    iwanka "I'm not pouting!"
    melonia @ -m_talk "Mmhmm."
    iwanka "I just hate being paraded around like {b}Daddy{/b}'s little princess..."
    melonia "Well, I guess you shouldn't have flunked out of college then, huh?"
    iwanka @ f_eyeroll "Ugh, you know that professor had it out for me!"
    melonia "Yeah, right."
    show melonia a_pull_panties with dissolve
    pause
    show melonia b_panties_blank a_idle with dissolve
    iwanka f_suspicious "..."
    iwanka "Is {b}Daddy{/b} going to go to jail?"
    melonia a_pull_bra2 "Only if he's stupid enough to get himself caught."
    show melonia b_undies a_idle with dissolve
    iwanka "What will happen to us if he does?"
    melonia f_smirk "Hmph, we should be so lucky..."
    melonia "My sex life would improve, that's for sure."
    iwanka f_annoyed a_hip @ f_eyeroll "Eww, {b}Mom{/b}!"
    iwanka "I don't wanna hear about your sex life!"
    melonia @ f_laugh "Hahaha!"
    pause
    melonia "Your father isn't going to get caught..."
    melonia "... And even if he did, it would have no effect you and me."
    melonia "We can just claim ignorance to the entire thing."
    iwanka f_suspicious "Y-you're sure?"
    melonia f_normal "Positive."
    pause
    iwanka f_normal "Okay, but if he does get caught... Can I start having boys over?"
    melonia "Sure, sweetie."
    iwanka @ f_laugh "Hehe, yay!"
    melonia "I want you to wear that dress your father bought you."
    melonia "You know, the slutty one."
    iwanka "Umm, I can't."
    melonia "Why not?"
    iwanka "The maid took for dry cleaning."
    melonia "Ugh, the chubby Latin one?"
    iwanka @ f_eyeroll "Duh."
    iwanka "She's {b}Daddy{/b}'s new favorite."
    melonia f_annoyed @ f_eyeroll "Tsk, hiring her was a bad idea."
    melonia "Your father already has three separate lawsuits pending."
    melonia "The last thing we need is another scandal."
    iwanka "Well, good luck stopping it."
    melonia f_normal @ f_eyeroll "Yeah, I know."
    melonia "I wish I could just call Immigration and have them come deal with her."
    iwanka @ f_suspicious "You wanna get her deported?"
    melonia "Why not?"
    melonia "It's what your father did with the pool boy..."
    iwanka "Yeah, because he caught you fucking him!"
    melonia f_smirk "Technically, he was fucking me..."
    iwanka "We don't even have a pool!"
    melonia @ f_laugh "Hahaha!"
    iwanka "{b}Daddy{/b} will throw a fit if you call Immigration about his favorite toy."
    melonia f_normal @ f_eyeroll "Yeah, I know."
    melonia "{i}*Sigh*{/i} I'll just have to figure out some other way to get rid of her..."
    iwanka @ -m_talk "..."
    iwanka "So, can I go now?"
    melonia "Yes, yes... Go and get ready."
    melonia "Make sure you wear something low-cut!"
    iwanka f_annoyed "Grr, fine!"
    hide iwanka with dissolve
    melonia @ f_eyeroll "Spoiled brat."
    pause
    melonia f_annoyed "Eugh, I hope the one with the neck tattoo isn't there again today..."
    pause .5

    scene black with slowdissolve
    pause 2

    $ game.timer.tick()
    scene expression background(400, 392, 4.) as stage with slowdissolve
    show anon b_dressed_pickup with dissolve
    show anon -b_dressed_pickup f_worried with dissolve
    anon @ -m_talk "( Finally! )"
    anon @ -m_talk "( I was starting to worry I'd be stuck under that bed all day... )"
    pause
    anon f_flirt @ -m_talk "( The mayor's wife sure is pretty! )"
    anon @ -m_talk "( It's a shame she's such a snob... )"
    show anon f_thinking a_thinking
    pause
    anon @ -m_talk "( I wonder if {b}she'd be willing to help me{/b}? )"
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
