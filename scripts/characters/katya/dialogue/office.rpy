label katya_button_office:
    $ renpy.dynamic(had_sex=M_katya.finished_state(S_kat01_init))

    if had_sex:
        show anon a_wave with {'master': dissolve}
        anon "Hey, {b}Katya{/b}!"
        katya f_happy "Hello, {b}[firstname]{/b}."
        show anon a_sides
        with {'master': dissolve}
        katya "You come to see {b}Nadya{/b}?"

    elif not M_katya.once('chat'):
        jump katya_button_office.first
    else:

        show anon f_worried with dissolve
        pause
        anon "Hello again."
        katya f_confused @ -m_talk "Hmm?"
        katya f_normal "Oh, hello."
        show anon f_shy

    menu katya_button_office.choice:
        "So what are you doing there?" if not had_sex:
            jump katya_button_office.what

        "You remember me?" if not had_sex:
            jump katya_button_office.anon

        "How are you holding up?" if not had_sex:
            jump katya_button_office.okay

        "How's work?" if had_sex:
            jump katya_button_office.work

        "Your English is getting pretty good." if had_sex:
            jump katya_button_office.language

        "Sex." if had_sex:
            jump katya_button_office.sex
        "See you later.":

            pass

    anon "I should probably leave you to your work."
    katya f_normal "Da, much to do."
    katya "Vodka bring lots of monies!"
    show katya f_normal_down
    hide anon
    with dissolve
    return


label katya_button_office.anon:
    anon "So do you remember me?"
    show katya f_normal
    pause
    anon "That day, when all the bad men got killed..."
    anon "... I was with the guys who-"
    katya f_happy "Da, you save me!"
    katya "This I remember always."
    show anon f_happy
    katya "You are good man!"
    katya "Brave man!"
    show anon a_rub f_shy_left with {'master': dissolve}
    anon "Ahh, geez."
    katya "I would kiss you..."
    show anon f_surprised
    show katya a_up f_shy with {'master': dissolve}
    katya "... But I'm not wanting make {b}Nadya{/b} angry with me."
    show anon a_sides f_shy
    show katya a_writing
    with {'master': dissolve}
    anon "Oh, no... really, it's fine!"
    anon "I'm just glad you girls are safe now."
    katya f_happy "Da, America is nice place."
    katya "I like very much."
    anon "That's good to hear."
    show katya f_happy_down
    anon "I'm happy everything worked out."
    jump katya_button_office.choice


label katya_button_office.cool:
    anon "Cool."
    pause
    show katya f_normal_down
    jump katya_button_office.choice


label katya_button_office.first:
    show anon f_worried with dissolve
    anon "Hey, umm..."
    katya @ -m_talk "Hmm?"
    show anon a_wave f_shy with {'master': dissolve}
    anon "... Hi, there."
    katya f_confused "Oh, uhh..."
    katya "... Hello?"
    show anon a_sides with {'master': dissolve}
    anon "You're {b}Katya{/b}, right?"
    katya f_normal @ -m_talk "Mmm."
    katya "Da?"
    anon f_worried "Cool."
    show katya f_confused
    pause
    show anon f_worried_surprised
    pause
    show anon f_surprised_left_low
    pause
    show anon a_shy_neck f_shy_high with {'master': dissolve}
    anon "Cool, cool, cool."
    pause
    katya "Ehh, I help you?"
    anon f_confused @ -m_talk "Hmm?"
    show anon a_sides f_worried with {'master': fastdissolve}
    anon "Oh, no... No."
    anon f_shy "I'm just, getting the lay of the land."
    show katya f_concerned
    pause
    anon f_worried "You know, checking things out?"
    katya @ -m_talk "..."
    anon f_shy "Trying to be friendly."
    katya @ f_confused "Do {b}Nadya{/b} say is okay you be here?"
    anon f_confused "{b}Nadya{/b}?"
    anon f_brag "Oh, yeah..."
    anon "... Totally."
    anon f_brag_closed "She's pretty much given me free rein of the place."
    show katya f_confused
    anon f_flirt_left "We're on good terms with one another."
    anon f_flirt "Like, really, {i}really{/i} good terms... if you know what I mean?"
    show anon f_flirt_grin
    show katya f_confused
    pause
    anon f_shy "We uhh..."
    pause
    anon f_worried "... You know what?"
    anon "Never mind."
    pause
    katya f_normal_down "Okay."
    jump katya_button_office.choice


label katya_button_office.language:
    anon f_normal "Your English has really improved."
    katya "Thanks, {b}[firstname]{/b}."
    katya "I have much more time to study now that you're giving {b}Nadya{/b} such good sexy times."
    show anon a_idle f_shy of_blush
    with {'master': dissolve}
    anon "O-oh?"
    katya @ -m_talk "Mhmm."
    katya "Is also nice to give my jaw a break."
    katya f_concerned_down "She has insatiable appetites."
    anon f_sad_down "Yeah, tell me something I don't know..."
    show katya f_confused
    pause
    show katya f_thinking_up
    pause
    katya f_happy "Okay!"
    show anon f_confused -of_blush
    with {'master': dissolve}
    katya "Did you know my country invents the Tetris?"
    show anon a_surprised_up_both f_worried_surprised
    with {'master': dissolve}
    anon "That was just a figure of speech, {b}Katya{/b}... You're not actually supposed to-"
    show anon f_confused
    pause
    anon f_skeptical "Wait, seriously?!"
    show anon a_sides
    with {'master': dissolve}
    anon "Tetris was invented in Russia?"
    katya "Is true."
    anon f_happy_surprised "I did not know that!"
    katya f_proud "Heh, you continue to learn new things from {b}Katya{/b}!"
    anon f_normal @ f_happy "Yeah, I guess so."
    jump katya_button_office.choice


label katya_button_office.okay:
    anon "So you're getting along okay?"
    katya f_happy "Better than okay!"
    katya "{b}Nayda{/b} makes me personal assistant."
    anon f_happy "Oh, really?"
    katya "For first time in life I have monies that is mine..."
    katya "... {b}Nadya{/b} takes me buy nice clothes and gets me apartment."
    anon "That's wonderful."
    katya "And the food in this country..."
    katya "... I eat like queen!"
    anon "Yeah, that's America for you."
    katya "Like the ehh, chili cheese dog!"
    anon @ f_happy_closed "Aww, yeah..."
    anon "... That's a good one!"
    katya "Oh, with the onion and little pickles on top..."
    katya "... Delicious!" (show_native="... Pal'chiki oblizhesh!")
    katya "And the bottomless french fried potatoes..."
    katya f_surprised "... No person can eat so much!"
    show katya a_wide
    with {'master': dissolve}
    katya "They explode for certain!"
    anon "Heh, yeah... chili dogs and french fries can have some {i}explosive{/i} repercussions, that's for sure."
    show katya a_writing f_happy
    with {'master': dissolve}
    katya "What is cushions?"
    anon f_shy "You know, because they make you..."
    anon "... Ehh..."
    anon f_shy_left "... {size=-2}Fart{/size}."
    katya f_confused @ -m_talk "Hmm?"
    show anon a_behind_head f_shy_down
    with {'master': dissolve}
    anon "Heh, uhh... nevermind."
    anon f_shy "It's not important."
    katya "But I could not hear you."
    show anon a_sides f_normal
    with {'master': dissolve}
    anon "Oh, good."
    pause
    anon "Trust me, that's for the best."
    katya f_happy @ f_laugh "Hehe!"
    katya "You are sometimes strange man!"
    show katya f_happy_down
    jump katya_button_office.choice


label katya_button_office.sex:
    anon "So, you think we could ehh... you know?"
    katya f_happy "Sex?" (show_native="Seks?")
    katya "Of course."
    show anon a_surprised_up f_surprised
    with {'master': dissolve}
    anon "Really?!"
    katya "Heh, I would welcome the break."
    show anon a_sides f_happy
    show katya a_front b_dressed
    with {'master': dissolve}
    katya "And my mistress did say I am to be yours whenever you wish it."
    show anon a_surprised f_surprised
    with {'master': dissolve}
    anon "She did?!"
    show katya f_confused
    show anon f_surprised_teeth
    pause
    show anon a_shy_neck f_worried
    with {'master': dissolve}
    anon f_worried "I mean, yes..."
    show anon a_sides
    with {'master': dissolve}
    anon f_shy "... S-she did."
    show katya a_undress1 f_happy
    with {'master': dissolve}
    katya "Good."
    show anon f_shy_low
    show katya a_undress2 b_dressed_boobs
    with {'master': dissolve}
    pause
    show anon f_flirt_grin
    show katya a_pull1 b_dressed_boobs
    with {'master': dissolve}
    katya "Come."
    show katya a_pull2 b_dressed_boobs_pulled
    with {'master': dissolve}
    katya "We make fuck on desk."
    anon f_flirt "Sweet!"

    call scene_katya_sex_desk_side.repeat
    $ unlock_scene('katya', '01_unlocked', variant='repeat')

    call katya_button_stage
    show katya a_pull2 b_dressed_disheveled_boobs_pulled f_happy_down
    show anon b_dressed_changing2
    with fade
    anon "Phew, that was a work out."
    show anon b_dressed_changing
    show katya a_pull1 b_dressed_disheveled_boobs
    with {'master': dissolve}
    katya @ -m_talk "Mhmm."
    show anon b_dressed a_sides
    show katya a_undress1 b_dressed_disheveled f_happy
    with {'master': dissolve}
    katya "The perfect break."
    show katya a_fix_hair1 b_dressed_sit
    with {'master': dissolve}
    katya "But now I must get back to it."
    show katya a_fix_hair2 f_normal_down
    with {'master': dissolve}
    anon f_worried "Yeah, okay."
    show katya a_writing
    with {'master': dissolve}
    pause
    anon f_shy "Don't work too hard, okay?"
    katya f_confused @ -m_talk "Hmm?"
    katya "This work is not hard."
    anon @ f_worried "Ehh..."
    anon "Nevermind."
    show katya f_concerned
    pause
    show anon a_wave
    with {'master': dissolve}
    anon "See ya, {b}Katya{/b}."
    hide anon
    with {'master': dissolve}
    katya f_normal "Farewell, {b}[firstname]{/b}." (show_native="Do svidaniya, {b}[firstname]{/b}.")
    show katya f_normal_down
    pause
    return 'afterglow'


label katya_button_office.what:
    anon "So what are you writing?"
    katya "Accounting work." (show_native="Bukhgalterskaya rabota.")
    katya "For vodka business." (show_native="Dlya vodochnogo biznesa.")
    anon f_confused @ -m_talk "Hmm?"
    anon "I don't understand."
    katya f_normal "Ehh, we... sell, vodka..."
    show anon f_confused_low
    show katya a_paper
    with {'master': dissolve}
    katya @ f_normal_low "... And keep numbers for counting."
    anon f_normal "Oh, so you're keeping track of all the money?"
    show katya a_writing f_happy
    with {'master': dissolve}
    katya "Da, monies."
    katya "Since I was little girl, I am good with numbers."
    katya "In Russia I help papa with monies also."
    anon "No kidding?"

    menu:
        "Cool beans.":
            jump katya_button_office.cool
        "What did he do?":

            pass

    anon "What did he do?"
    katya f_confused @ -m_talk "Hmm?"
    anon "Your father's business."
    anon "You sell vodka but what did he sell?"
    katya f_shy "Oh, umm... mushrooms." (show_native="Oh, umm... griby.")
    anon f_confused "Griby?"
    katya f_happy "Heh, da." (show_native="Heh, yes.")
    katya f_thinking_up "Ehh, what is word?"
    pause
    katya "Marsh..."
    show anon a_thinking
    with {'master': dissolve}
    pause
    show anon a_point2 f_happy
    with {'master': dissolve}
    anon "Marshmallows?"
    show katya f_confused
    pause
    show anon a_sides f_sad
    with {'master': dissolve}
    katya "Nyet." (show_native="No.")
    katya f_thinking_up "Not marsh... it's ehh..."
    katya "... M-mush..."
    show anon a_point2 f_happy
    with {'master': dissolve}
    anon "Mushrooms?!"
    show anon a_fist f_grin
    with {'master': dissolve}
    katya f_happy "Da, mushrooms!"
    show anon a_sides f_normal
    with {'master': dissolve}
    anon "So your father sold mushrooms?"
    katya f_proud "Well, he sells many things he take from wilderness..."
    katya "... Honey, berry, animals for eating or selling the skins..."
    katya "... Sometimes medicine."
    anon "No kidding?"
    katya "But mushroom is best seller."
    katya "People in Russia like salty mushroom very much!"
    anon f_confused "I had no idea."
    katya "Is making for wonderful snack times when mix with vodka."
    anon f_normal "Well how about that?"
    show katya f_happy_down
    anon "Guess it's true you learn something new every day."
    jump katya_button_office.choice


label katya_button_office.work:
    anon "How's it going?"
    katya "Good!" (show_native="Khorosho!")
    katya "{b}Nadya{/b} promote me to head of sales!"
    anon @ f_happy "You don't say?!"
    katya "No, is true!"
    katya "She says, \"{b}Katya{/b} you have gift for selling to fat American business man.\""
    show katya a_squeeze f_happy_down
    show anon f_surprised_low
    with {'master': dissolve}
    katya "But truth is, I just smile and wear bra that smash breasts together like angry siblings in meal ticket line."
    show anon o_boner
    with {'master': dissolve}
    anon @ -m_talk "..."
    katya a_writing f_proud "Then they triple order."
    pause
    show katya f_proud_teeth_low
    pause
    show anon f_surprised_down
    pause .4
    show anon a_cover_boner f_shy
    show katya f_laugh
    with {'master': dissolve}
    anon "I'm sorry, I didn't hear anything after the word breasts."
    katya f_proud "Maybe I sell you vodka too, eh?"
    anon "Heh, nah... That's alright."
    anon "I'm good."
    katya f_laugh "Hehe!"
    show anon a_idle -o_boner
    show katya f_happy
    with {'master': dissolve}
    jump katya_button_office.choice
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
