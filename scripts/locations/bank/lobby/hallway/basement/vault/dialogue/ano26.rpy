label ano26_move_bank_vault:
    scene expression background(512, 512, 4.6, l=L_bank_basement) as stage
    show liu f_frightened:
        xzoom -1
    show anon of_ski_mask a_tiny_gun_down f_angry with dissolve:
        xoffset -100
        xzoom -1
    anon "Is this it?"
    liu "Y-yes, sir."
    anon "Good."
    anon a_tiny_gun "Now open it."
    hide liu with dissolve
    pause
    anon "And no funny business!"
    anon "Remember, I've got a gun pointed right at you!"
    liu "Okay!"
    pause
    anon f_worried "So you got any plans tonight?"
    liu "Mm, no... not really."
    liu "I've mostly just been throwing out {b}Kim{/b}'s old junk all week."
    liu "You wouldn't believe some of the things I found stashed away."
    show anon a_tiny_gun_down with dissolve
    pause
    anon f_normal "Heh, like what?"
    liu "Like the poetry journal he kept hidden under his pillow."
    anon f_confused "Poetry journal?"
    liu "Yeah, it's awful!"
    anon f_normal @ f_laugh "I can imagine."
    show liu with dissolve:
        xzoom -1
    liu "No, trust me... you can't."
    liu "His stuff makes Paula Nancy Millstone Jennings look like Emily Dickinson."
    anon f_worried "Wow, that's a lot of names I don't know..."
    liu m_talk "Heh, sorry."
    show liu f_nervous_down o_blush -m_talk with {'master': dissolve}
    liu "I guess, I read a lot."
    anon "No, that's cool... I wasn't poking fun."
    show liu f_nervous
    pause
    anon "Maybe you can show me sometime?"
    show anon f_normal
    liu "Y-yeah, I'd love to."
    show anon f_surprised_left
    show liu f_surprised o_empty
    with {'master': dissolve}
    tony "What the hell's takin' so long down here?"
    show liu f_worried
    show anon f_worried_left
    show tony o_ski_mask f_smirk b_casual a_gun_lower with dissolve:
        xoffset 200
    tony "You two lovebirds forget you're supposed to be puttin' on a show for the cameras?"
    anon "Oh, right."
    show anon a_tiny_gun f_worried
    show liu f_frightened a_holdup
    with {'master': dissolve}
    liu "!!!"
    anon "Uhh..."
    show tony f_question
    pause
    anon f_angry "... Get in the vault and face the wall!"
    liu "Okay!"
    hide liu with dissolve
    anon "Keep those hands where I can see them!"
    hide anon with dissolve
    pause
    tony a_gun_down f_eyeroll "Jesus..."
    hide tony with dissolve

    scene expression background(192, 400, 3.) as stage
    show anon a_tiny_gun of_ski_mask:
        xoffset -100
        xzoom -1
    show liu a_holdup f_frightened:
        xoffset -550
    show tony a_gun_lower b_casual f_question o_ski_mask:
        xoffset 200
    with fade
    tony "Any idea what this thing looks like?"
    anon f_worried_left "No, not really."
    show anon f_normal
    show liu a_sides f_nervous:
        xoffset 0
        xzoom -1
    with {'master': dissolve}
    liu "It's an all black briefcase."
    liu "Should be pretty easy to spot."
    tony "Are there cameras in here?"
    liu "No."
    show anon a_tiny_gun_down
    show tony a_baklava2 o_empty
    with {'master': dissolve}
    tony "Thank Christ!"
    show liu f_laugh
    tony a_gun_lower f_normal o_ski_mask_pulled @ f_laugh "I'm sweating like a whore in church under this thing..."
    show liu f_happy
    show anon a_baklava2 of_empty f_normal_left
    with dissolve
    anon "I thought you and Luigi used to wear these all the time?"
    show anon of_ski_mask_pulled a_tiny_gun_down with dissolve
    show liu f_worried
    tony f_sad "Yeah, well... that was years ago and I might have put on a few pounds since then, okay?!"
    tony "Thanks for pointin' it out."
    anon f_worried_left "What?!"
    anon "I didn't even say anything!"
    tony f_angry "Yeah, but you were thinkin' it!"
    show anon f_worried
    liu f_happy "I think you look great, {b}Tony{/b}."
    tony f_smirk "Aww, thanks, darlin'!"
    anon @ f_eyeroll "Can we just find the briefcase and get out of here, please?!"
    tony "No worries, I'm on it."
    hide tony with dissolve
    liu "I think I saw it up high somewhere..."
    hide liu with dissolve
    anon a_idle f_thinking "( Up high, eh? )"
    anon a_surprised f_surprised_high "( Wait, is it really that easy?! )" with hpunch
    hide anon with dissolve
    return


label ano26_take_case:
    scene expression background(400, 400, 2) as stage
    show anon a_briefcase_up of_ski_mask_pulled with dissolve
    anon "Got it!"
    show anon a_briefcase
    show liu:
        xoffset 100
    show tony a_gun_down b_casual f_question o_ski_mask_pulled:
        xoffset -50
    with dissolve
    tony "What, that little thing?"
    anon "Yeah, I think so."
    liu "Nice work, {b}[firstname]{/b}!"
    anon @ f_laugh "Thanks, {b}Liu{/b}."
    tony "Hand it here."
    anon @ -m_talk "Hmm?"
    show anon a_sides f_confused
    show liu f_nervous_down
    show tony a_briefcase f_normal_down
    with {'master': dissolve}
    anon "What are you doing?"
    tony f_normal "I gotta see what all the fuss is about..."
    show liu f_worried
    anon f_surprised "You're gonna open it here?!"
    tony "Yeah, why not?"
    tony "Gotta make sure we ain't handin' that crazy broad something we'll regret, right?"
    show liu f_worried_down
    show tony f_normal_down
    show anon f_thinking_down:
        xoffset -220
        xzoom -1
    with dissolve
    anon "I guess..."

    scene location_bank_vault_briefcase_closed with fade
    pause

    scene anon b_mcpuffin m_talk
    show tony b_mcpuffin m_talk
    show liu b_mcpuffin m_talk
    with dissolve
    "!!!"
    tony -m_talk "Holy Mother Mary and Joseph..."
    anon -m_talk "Is that what I think it is?"
    tony "Y-yeah."
    liu -m_talk "It's so pretty!"
    tony "You know, I heard stories about this... but I never believed 'em."
    anon "How in the heck did it wind up with the Russians?"
    tony "I don't even wanna know."
    liu "Can I touch it?"

    scene expression background(400, 400, 2) as stage
    show liu f_surprised:
        xoffset 100
    show anon a_sides f_surprised of_ski_mask_pulled:
        xoffset -220
        xzoom -1
    show tony a_briefcase b_casual f_angry o_ski_mask_pulled:
        xoffset -150
        xzoom -1
    with fastfade
    tony "No, ya can't touch it!"
    show anon f_worried_low
    tony f_suspicious "Don't you realize what that is?!"
    liu f_ashamed_down "You're right, sorry."
    show anon f_surprised
    tony f_sad "Here, you take it."
    show tony a_sides
    show anon a_briefcase f_worried
    with dissolve
    tony "I don't want it near me."
    anon @ -m_talk "..."
    tony "Tie your little girlfriend up and lets get out of here."
    show liu f_surprised
    tony "I'll get the door."
    hide tony
    show anon:
        xoffset 280
        xzoom 1
    show liu:
        xoffset 700
        xzoom -1
    with {'master': dissolve}
    anon "R-right, okay."
    show liu f_confused with {'master': dissolve}:
        xoffset 100
        xzoom 1
    liu "Tie me up?"
    anon "Yeah."
    anon "It's probably best that the cops find you here in the vault tied up, don't you think?"
    liu f_worried_down "Y-yeah, okay."
    pause
    show liu a_behind f_ashamed_down with dissolve:
        xoffset 700
        xzoom -1
    pause
    show anon f_worried_low a_stashed_bag_show behind liu with dissolve:
        crop (0, 0, 400, 768)
        offset (475, 10)
    pause
    liu "Are you gonna be okay with that thing?"
    anon @ f_confused -m_talk "Hmm?"
    anon "Oh, sure."
    anon "I uhh... don't plan on having it very long."
    anon "We'll set up a meeting with the mob bosses' daughter right away."
    liu f_nervous_down "You still coming over tonight?"
    anon f_normal_low "Heh, I dunno..."
    show liu f_worried_down
    pause
    anon f_worried_low "... It might not be the best idea, what with the robbery and all."
    liu "Oh."
    anon "The mob will be looking for the people who took the case..."
    anon "... I don't wanna implicate you."
    liu "Y-yeah, I suppose that's for the best."
    anon f_normal_low "But I'll definitely come by once things die down."
    show liu f_nervous_down
    pause
    show anon f_normal a_sides with {'master': dissolve}:
        reset
        offset (280, 0)
    pause
    show liu f_worried with {'master': dissolve}:
        xoffset 100
        xzoom 1
    liu f_nervous "Well, you'd better..."
    liu f_sexy "... There's a certain rain check I'd like to cash."
    liu "I hope you haven't forgotten about it?"
    show liu f_sexy_lipbite
    anon f_flirt "No, I remember."
    liu f_sexy "Good."
    show liu b_dressed_kiss_3:
        xoffset 200
    hide anon
    with dissolve
    liu "Mmm."
    pause
    show liu a_behind b_dressed:
        xoffset -150
    show anon a_sides f_flirt of_ski_mask_pulled:
        xoffset 150
    with dissolve
    liu "Stay safe."
    anon "You too."
    pause
    anon "Here, lemme help you onto the floor."
    liu "Thanks."

    scene location_bank_cutscene_01
    show text _ ("It wasn't much of a bank robbery but it hopefully looked convincing for the cameras.") as caption
    with fade
    pause
    hide caption with dissolve
    show text _ ("{b}Liu{/b} had played her role well and it seemed she'd have little trouble convincing the police.") as caption with dissolve
    pause

    scene location_bank_cutscene_02
    show text _ ("As for {b}Tony{/b} and I... we secured the prize and made our exit quickly.") as caption
    with fade
    pause
    hide caption with dissolve
    show text _ ("My heart was racing the entire way to the van but {b}Tony{/b} kept his cool.") as caption with dissolve
    pause
    hide caption with dissolve
    show text _ ("I sure was glad I had him to lean on through this whole ordeal.") as caption with dissolve
    pause

    scene expression background(288, 432, 3.5, l=L_warehouse) as underlay:
        xoffset -400
    show nadya a_phone_talk:
        xoffset -500

    $ renpy.dynamic(stage=Fixed(L_pizzeria_interior.background_closeup,
                                Transform(game.timer.image('char_xtra_12{}'), yalign=1.)))
    show expression L_pizzeria_interior.background_closeup as stage
    show expression game.timer.image('char_xtra_12{}') as counter
    show tony f_smirk a_duffel b_casual:
        xzoom -1
    show anon a_briefcase:
        xoffset 50
        xzoom -1
    with fade
    tony "Phew, thank god {b}Maria{/b} is still home nursin' that cold."
    tony "It'd be real hard explainin' that briefcase to her."
    anon f_confused "Huh?"
    anon a_briefcase_ear "I can't hear you, my ears are still ringing from the alarm!"
    tony @ f_laugh "Yeah, mine are pretty bad too."
    anon "What did you say?"
    tony @ f_eyeroll "Ugh."
    tony f_suspicious "I said-"
    show tony f_sad
    pause
    tony "Never mind."
    show tony with dissolve:
        xoffset -400
        xzoom 1
    hide tony with dissolve
    pause
    anon a_briefcase "It's a good thing {b}Maria{/b} isn't here."
    anon "We'd have a hard time explaining the briefcase to her, huh?"
    show tony b_casual f_sad behind counter with dissolve:
        xzoom -1
    tony @ -m_talk "..."
    tony "Yeah, I just said that."
    anon f_worried "Oh, you did?"
    tony f_smirk "Jesus."
    anon "Sorry it wasn't the bank heist you envisioned, {b}Tony{/b}."
    tony @ a_wave "Ahh, it's fine."
    tony @ f_laugh "I'm still crossin' it off the bucket list."
    anon @ f_laugh "Hehe!"
    tony "You did real good, kid."
    anon f_shy "Thanks."
    pause
    tony "So when you callin' this gal?"
    anon f_worried "Oh."
    anon "Umm... now, I suppose."
    tony "Good."
    tony @ a_point "The sooner that thing is gone, the better, yeah?"
    anon "Yeah."
    hide tony
    hide counter
    show expression stage as stage
    with dissolve
    tony "You want some food or something?"
    anon a_briefcase_phone f_worried_low "Nah, I'm good."
    anon "Thanks."
    pause
    show anon a_briefcase_phone_talk f_confused with dissolve:
        xoffset 550
        xzoom 1
    "{i}*Ring* *Ring*{/i}"
    show expression stage as stage at phoneleft with phoneleft.show
    nadya "Speak."
    anon f_worried "Yes, hello... {b}Nadya{/b}?"
    nadya "Da."
    anon "H-hey, it's me... {b}[firstname]{/b}."
    pause
    nadya f_angry "... Well?!"
    nadya "What do you want?!"
    anon "Right... sorry."
    anon "I have that briefcase you wanted."
    nadya f_surprised "You do?"
    anon "Yeah."
    show nadya f_normal
    anon "It wasn't easy but I got it."
    nadya "This is nice surprise."
    anon "When can we meet?"
    nadya @ f_eyeroll -m_talk "Hmm."
    nadya "We meet tomorrow."
    nadya "On hill overlooking town."
    anon "{b}Raven Hill{/b}?"
    nadya "Da."
    nadya "{b}Be there at sunset and come alone{/b}."
    nadya "Understand?"
    anon "Yeah, okay."
    nadya "Good."
    nadya "See you then."
    show anon f_sad_down a_briefcase_phone with dissolve
    show expression stage as stage with {'master': phoneleft.hide}
    "{i}*Beep*{/i}"
    anon "{i}*Sigh*{/i} I hope this was all worth it."
    pause
    show expression L_pizzeria_interior.background_closeup as stage
    show expression game.timer.image('char_xtra_12{}') as counter behind anon
    show tony a_pizza_roll behind counter with dissolve:
        xzoom -1
    tony "So, what did she say?"
    show anon a_briefcase f_worried with dissolve:
        xoffset 50
        xzoom -1
    anon "{b}I'm meeting her tomorrow evening, on Raven Hill{/b}."
    tony "You want me to tag along?"
    anon "No, she was pretty specific that I come alone."
    tony "I see."
    show tony a_pizza_roll_take with dissolve
    show tony a_pizza_roll_eat f_eat with dissolve
    pause
    tony a_pizza_roll f_chew "Well, I think it's a bad idea."
    anon "Yeah, I know you do."
    show tony a_pizza_roll_take with dissolve
    show tony a_pizza_roll_eat f_eat with dissolve
    anon "But we did the job and got the briefcase..."
    show tony a_pizza_roll f_chew with dissolve
    anon "... Seems pretty silly to give up now."
    tony "You say silly, I say smart."
    show anon f_worried_low
    pause
    tony f_normal "Just call me afterwards and lemme know you're okay, yeah?"
    anon f_shy "Will do."
    pause
    tony f_suspicious "Now do me a favor and get that briefcase outta my shop."
    tony "It's makin' my skin crawl, just knowin' it's in here..."
    show tony a_pizza_roll_take with dissolve
    show tony a_pizza_roll_eat f_eat with dissolve
    anon "Heh, okay."
    show tony a_pizza_roll f_chew with dissolve
    anon "Give {b}Maria{/b} my love."
    tony "Oh, after today's excitement... you bet I will."
    anon f_laugh "Heh, have fun!"
    hide anon with dissolve

    scene expression background(l=L_pizzeria_exterior) with fade
    show anon a_briefcase f_worried with dissolve
    anon @ -m_talk "( {b}Tony{/b}'s right, I have no idea what I'm walking into tomorrow... )"
    anon @ -m_talk "( ... {b}I should make sure all my affairs are in order before I head to Raven Hill{/b}. )"
    pause
    anon @ -m_talk "( And I should check on {b}Liu{/b} and make sure everything went okay with the police. )"
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
