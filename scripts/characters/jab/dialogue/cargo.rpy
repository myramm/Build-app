label jab_button_cargo:
    $ renpy.dynamic(queries=set())

    show thug a_bottle_drink f_drink -m_talk with dissolve
    pause
    show anon with dissolve:
        xoffset 150
        xzoom -1
    pause
    show anon:
        xoffset -300
        xzoom -1
    show thug a_bottle_throw f_surprised
    with dissolve
    pause
    show anon a_surprised f_hurt:
        xoffset -575
    show thug a_wave b_dressed
    with {'master': dissolve}
    jab "Hello, friend." (show_native="Privet, comrade {b}[firstname]{/b}.")
    show anon a_sides f_tired with dissolve
    pause
    show anon with {'master': dissolve}:
        xoffset -75
        xzoom 1
    anon "Hey, {b}Jab{/b}."
    jab a_sides "Can I ask question?"

    menu jab_button_cargo.choice:
        "Ehh, sure.":
            jump jab_button_cargo.question
        "What kind of name is {b}Jab{/b}?":

            jump jab_button_cargo.name
        "Not now.":

            pass

    if len(queries) > 8:
        show anon a_crossed f_annoyed with {'master': dissolve}
        anon "Staaahp!"
        anon f_confused "How can you possibly have more?!"
    elif queries:
        show anon a_up f_worried with {'master': dissolve}
        anon "No more please!"
    else:
        anon "Not now please."

    show thug a_defensive f_normal with {'master': dissolve}
    jab "Okay, but perhaps I could give you this document I've been working on with suggestions to make game better?"
    show anon a_sides
    show thug a_sides
    with {'master': dissolve}
    anon f_confused "Ehh..."
    jab "Is only twenty-five pages but more is coming, so don't worry."
    anon f_surprised "Twenty-five pages?!"
    anon f_confused "Wha-"
    show thug a_scratch_head f_concerned with {'master': dissolve}
    jab "Ehh, sorry... Twenty-eight."
    jab "I forgot I added my ideas for making sexy times with all the womans at beach house."
    show anon a_pocket
    show thug a_sides
    with {'master': dissolve}
    anon "We're already planning that."
    jab f_happy "Oh, good. Then my ideas have been helpful."
    anon f_skeptical @ -m_talk "..."
    show anon a_point f_confused
    with {'master': dissolve}
    anon "..."
    show anon a_sides f_sad_down
    with {'master': dissolve}
    anon @ -m_talk "..."
    show thug:
        xoffset 500
        xzoom -1
    with {'master': dissolve}
    jab "Let me just find my documents..."
    show anon a_surprised_up_both f_surprised_teeth
    hide thug
    with {'master': dissolve}
    jab "... I know they're here somewhere."
    show anon a_protect f_worried with {'master': dissolve}
    jab "You want I should give you diagrams for future map expasions?"
    show anon:
        easeout 3 xoffset -800
    jab "I made five originally but it has grown to twelve now."

    scene expression background(104, 512, 5, l=L_warehouse_depot) with fade
    show anon b_dressed_catch_breath with fastdissolve:
        xoffset -100
    anon @ -m_talk "( Haah... Haah... )"
    anon @ -m_talk "( Oh man, haah... That was terrifying! )"
    show anon a_surprised b_dressed f_worried with {'master': dissolve}
    anon "( I should keep going, he might still find me out here... )"
    hide anon with fastdissolve
    return 'escape'


label jab_button_cargo.name:
    show anon a_wave f_normal_closed with {'master': dissolve}
    anon "Let {i}me{/i} ask..."
    show anon a_sides f_skeptical
    with {'master': dissolve}
    anon "... What kind of a name is {b}Jab{/b} anyway?"
    jab f_happy "Is short for {b}Jabzap{/b}."
    show anon f_confused
    jab "Nickname."
    anon f_skeptical "So what is your real name then?"
    show thug a_finger f_smirk with {'master': dissolve}
    jab "Oh, I see what you do..."
    jab "... You no trick me, comrade!"
    anon f_confused "Huh?"
    show thug a_chest with {'master': dissolve}
    jab "Russian mind is strong!"
    jab "I will not fall victim to your sneaky mind games!"
    anon f_sad_down "You know what..."
    anon "... Never mind."
    anon "I don't wanna know."
    show thug a_sides f_laugh with {'master': dissolve}
    jab "Ah hah!"
    jab f_happy "I win!"
    show thug f_laugh
    anon f_worried "No, I seriously don't wanna know."
    jab f_happy "Too late!"
    jab "I win."
    show thug f_laugh
    show anon a_pocket
    with {'master': dissolve}
    anon "Right... Whatever."
    anon "Don't care."
    jab f_normal "Me neither."
    pause
    jab f_happy "Because I already won."
    show anon a_crossed f_annoyed
    show thug f_laugh
    with {'master': dissolve}
    anon "No you didn't!"
    jab f_happy "Yes, I did."
    pause
    show thug a_cheer1 f_smirk with dissolve
    show thug a_cheer with None
    jab "Go {b}Jab{/b}!! "
    extend "Go {b}Jab{/b}!! "
    extend "Go {b}Jab{/b}!!"
    show thug a_cheer1 with None
    anon f_eyeroll "Jesus, you are infuriating!"
    hide anon with {'master': dissolve}
    jab f_concerned "Oh come now, don't be sore loser!"
    return


label jab_button_cargo.question:
    python:
        renpy.dynamic(q=random.randint(1, 9),
                      intro=random.random(), outro=random.random())
        queries.add(q)

    if intro <= .33:
        anon "Ehh, sure."
    elif intro <= .66:
        anon "I guess..."
    elif intro <= .99:
        anon "Why not?"
    else:
        anon "Can anything prevent that now?"

    call expression 'jab_button_cargo.question{}'.format(q)

    if outro < .40:
        show anon a_thinking f_thinking
    elif outro < .80:
        show anon a_rub f_worried
    else:
        show anon a_crossed f_thinking_down

    with {'master': dissolve}
    anon @ -m_talk "( I have no idea how to respond to this... )"
    show anon a_sides f_shy -of_blush with {'master': dissolve}
    anon "Let me get back to you on that."
    show thug a_sides f_normal_down with {'master': dissolve}
    jab "{i}*Sigh*{/i} Very well..."
    pause
    jab f_normal "One more question?"
    show anon f_tired
    jump jab_button_cargo.choice


label jab_button_cargo.question1:
    show thug a_hips f_normal with {'master': dissolve}
    jab "It seems many characters in town are changing appearance."
    show anon f_confused
    jab "Most people seem think is improvement but I'm not sure..."
    jab f_confused "... Is not better to leave as they are?"
    show anon a_behind_head with {'master': dissolve}
    anon "Ehh..."
    jab "Change is for no good reason, I think."
    return


label jab_button_cargo.question2:
    jab f_normal "I hear story of woman turning house into barn for animals..."
    show anon f_worried_surprised
    show thug a_confused f_confused
    with {'master': dissolve}
    jab "... Why would someone do this?!"
    jab "Is not making sense!"
    show anon a_behind_head f_shy
    show thug a_hips
    with {'master': dissolve}
    anon "Ehh..."
    jab "I should make petition for correcting this decision..."
    jab "... Is lunacy, I think."
    return


label jab_button_cargo.question3:
    jab f_normal "You realize that house you stay in makes no sense?"
    show anon f_confused
    show thug a_finger
    with {'master': dissolve}
    jab "Rooms do not match exterior."
    show thug a_confused f_confused
    with {'master': dissolve}
    jab "... Is this intentional or oversight?"
    anon f_worried_left "Ehh..."
    show anon f_worried
    show thug a_sides f_normal
    with {'master': dissolve}
    jab "This makes artist look foolish, I think."
    return


label jab_button_cargo.question4:
    show thug a_scratch_head f_confused with {'master': dissolve}
    jab "Why is not all characters have pregnancy yet?"
    show anon a_facepalm f_worried_down
    show thug a_hips
    with {'master': dissolve}
    jab "I want make babies with everyone but no."
    jab "... Why you do this to adoring fan?"
    show anon a_sides f_worried with {'master': dissolve}
    anon "Ehh..."
    jab f_normal "At least add {b}Roxxy{/b}."
    jab f_smirk "She is best waifu..."
    show thug a_boobs with {'master': dissolve}
    jab "... with breasts like torpedoes!"
    return


label jab_button_cargo.question5:
    jab f_normal "You realize that some backgrounds still require exterior shots?"
    show anon f_eyeroll
    jab "They exist for many but not all."
    show anon f_tired
    jab f_confused "... Is this intentional or oversight?"
    anon "Ehh..."
    show thug a_crossed with {'master': dissolve}
    jab "This cookie artist is lazy, I think."
    return


label jab_button_cargo.question6:
    jab f_normal "Why is {b}Kevin{/b} on your to do list?"
    show anon f_confused
    jab f_confused "Are you gay, comrade?"
    show anon f_surprised
    jab f_normal "... I mean, is fine if you are... So long as you understand, I'm not into it."
    anon f_confused "Ehh..."
    jab f_smirk "My penis like only lady butthole."
    show anon f_worried_surprised
    pause
    return


label jab_button_cargo.question7:
    jab f_normal "Why is landlady's daughter not loving you yet?"
    show anon f_surprised
    show thug a_hips f_angry
    with {'master': dissolve}
    jab "Is infuriating!"
    jab "... You do so much, and give her big monies..."
    show anon a_shy_neck f_shy_left of_blush with {'master': dissolve}
    anon @ -m_talk "..."
    show thug a_confused with {'master': dissolve}
    jab "... Why can she not admit she loves you?!"
    jab "Is unacceptable!"
    show anon a_sides f_worried -of_blush
    show thug a_hips
    with {'master': dissolve}
    jab "I so mad!"
    return


label jab_button_cargo.question8:
    jab f_confused "What is with old lady at hospital getting so many sexy times?"
    show anon f_confused
    jab "Cookie has old lady fetish?"
    show anon f_unimpressed
    jab "... Meanwhile, better characters have only one!"
    show anon a_behind_head with {'master': dissolve}
    anon "Ehh..."
    jab f_normal "Is unacceptable!"
    show anon a_sides f_flirt_grin
    show thug a_finger
    with {'master': dissolve}
    jab "I want demand more scenes with music teacher!"
    show thug a_sides f_smirk
    with {'master': dissolve}
    jab "Her milkshake brings all the Russian boys to the yard, eh?"
    return


label jab_button_cargo.question9:
    jab f_confused "How come {b}Judith{/b} does not get more sexy time love?"
    show anon f_surprised
    jab "Yes, she is thicc and nerdy with the oversize glasses."
    jab f_smirk "... But those tiddies though!"
    show anon a_behind_head f_shy of_blush with {'master': dissolve}
    anon "Ehh..."
    show thug a_boobs with {'master': dissolve}
    jab "I want to cover them in whipped cream and chocolate sauce..."
    show anon f_shy_left
    jab "... And then tie them in knot around my penis!"
    show thug a_sides f_normal
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
