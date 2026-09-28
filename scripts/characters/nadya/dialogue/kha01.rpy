label kha01_init_nadya:
    show anon a_wave behind nadya with dissolve:
        xoffset -100
    show nadya a_sides
    with {'master': dissolve}
    nadya "Oh good, you're here!"
    show svetlana a_sides:
        xoffset -100 xzoom 1
    with {'master': dissolve}
    nadya "I have job for you."
    show anon a_sides
    with {'master': dissolve}
    anon f_worried "Uhh, I'm still need some more time to think your offer over if you-"
    show svetlana f_curious_back
    nadya "No, no, no... Not that job!"
    show anon f_confused
    nadya "Something else."
    nadya "Something small."
    anon "Oh?"
    show svetlana a_hips f_concerned:
        xoffset 450 xzoom -1
    with {'master': dissolve}
    svetlana "That was not a small mess that I had to clean up." (show_native="Eto byl ne malen'kiy besporyadok, kotoryy mne prishlos' ubrat'.")
    show nadya a_dismiss
    with {'master': dissolve}
    nadya @ f_eyeroll "Oh, stop exaggerating!"
    nadya "It was just a teeny-tiny, little explosion."
    show anon f_surprised
    show nadya a_sides
    show svetlana a_crossed f_bored:
        xoffset -100 xzoom 1
    with {'master': dissolve}
    svetlana @ f_eyeroll -m_talk "Pfft!"
    anon f_worried_surprised "Explosion?"
    anon f_worried "Y-you mean the other day... When {b}Katya{/b} and I-"
    nadya f_bored "Da."
    nadya "One of our stills in lab."
    nadya "It seems our master distiller fell asleep and failed in her duties."
    show anon f_confused

    if M_khadne.get('chat', False):
        anon "You mean {b}Khadne{/b}?"
        nadya f_normal "Da."
    else:

        anon "Master distiller?"
        nadya f_normal "Da."
        nadya "Her name is {b}Khadne{/b}."

    show nadya a_hips
    with {'master': dissolve}
    nadya "Once a lowly slave of Papa, I intuit that her talents lie elsewhere."
    nadya f_happy "Her vodka is not only delicious, but highly profitable."
    svetlana @ f_eyeroll "She makes more trouble than she does vodka."
    nadya f_frowning "Have you tried her recipe?" (show_native="Vy poprobovali yeye retsept?")
    show svetlana a_sides f_bored:
        xoffset 450 xzoom -1
    with {'master': dissolve}
    svetlana "{i}*Sigh*{/i} Yes, it is quite good." (show_native="Da, eto ochen' khorosho.")
    nadya f_happy "It's exquisite!" (show_native="Eto izyskanno!")
    svetlana f_concerned @ f_annoyed "But it's not worth dying in warehouse inferno."
    nadya f_normal "Agreed."
    show nadya a_point
    with {'master': dissolve}
    nadya "That is why I ask for his help."
    show anon a_point_self f_surprised
    show svetlana:
        xoffset -100 xzoom 1
    with {'master': dissolve}
    anon "M-me?"
    show nadya a_sides
    with {'master': dissolve}
    anon "What can I do?"
    show anon a_sides f_confused
    with {'master': dissolve}
    nadya "{b}Khadne{/b}'s problem is not one of negligence."
    svetlana f_concerned_back "Stupidity more like..." (show_native="Glupost' bol'she pokhozha...")
    nadya f_frowning "Nyet." (show_native="No.")
    nadya "She is simply depressed."
    show svetlana a_confused f_curious:
        xoffset 450 xzoom -1
    with {'master': dissolve}
    svetlana "What she has to be depressed about?!"
    nadya f_normal "She's alone, in a strange country... doing a job she's been told she's unsuited for since she was child."
    show svetlana a_hips
    with {'master': dissolve}
    svetlana "All of us are alone in this place."
    svetlana "You should not baby her." (show_native="Vy ne dolzhny yeye detka.")
    nadya "Not everyone is as strong as you, {b}Svetlana{/b}." (show_native="Ne vse takiye sil'nyye, kak ty, {b}Svetlana{/b}.")
    show svetlana a_crossed f_bored
    with {'master': dissolve}
    svetlana @ -m_talk "Hmph."
    show anon a_wave f_shy
    with {'master': dissolve}
    anon "Excuse me, ladies?"
    show svetlana:
        xoffset -100 xzoom 1
    with {'master': dissolve}
    nadya @ -m_talk "Hmm?"
    show anon a_sides
    with {'master': dissolve}
    anon "I'm still not sure how I fit into all this."
    nadya f_happy "I hear once, that a good leader must use every tool at her disposal to solve difficult problem..."
    show anon f_confused
    show nadya f_sexy_low
    with {'master': dissolve}
    pause
    show nadya a_point
    with {'master': dissolve}
    nadya "And in you, I have a very large tool."
    show anon a_crossed f_unimpressed
    show nadya f_laugh
    with {'master': dissolve}
    svetlana f_happy_back @ f_laugh "Hah!"
    svetlana "That's an understatement." (show_native="Eto preumen'sheniye.")
    show nadya a_hips f_happy
    with {'master': dissolve}
    nadya "Hehe, right?" (show_native="Hehe, verno?")
    show svetlana f_happy
    anon f_skeptical "So what, you want me to sleep with her too?"
    nadya f_sexy "If needs be."
    show nadya a_finger f_normal
    with {'master': dissolve}
    nadya "Foremost I want you to cheer her up."
    show anon a_sides f_disgusted
    show nadya f_sexy
    with {'master': dissolve}

    if M_khadne.get('chat', False):
        nadya "From what I've been told, you already have some rapport with her."
        show nadya a_hips
        with {'master': dissolve}
        anon f_confused "I do?"
        nadya f_normal "Da."
        nadya "{b}Katya{/b} tells me the girl is quite fond of you."
        anon f_worried "Hmm, that's not the impression I got."
        show nadya a_hips_shrug f_pouting
        with {'master': dissolve}
        nadya "Yes, well... {b}Khadne{/b} is not the easiest person to read."
        show nadya a_hips f_normal
        with {'master': dissolve}
    else:

        nadya "And based on the effect you've had on my other girls..."
        show nadya a_hips
        with {'master': dissolve}
        nadya f_sexy "... I'd say you are the perfect man for task."

    anon f_unimpressed "You know, I'm beginning to feel like a bit of a man-whore around here."
    nadya f_confused "And this is bad thing?"
    nadya "I assume man enjoy this work."
    nadya "Do you not find my girls beautiful?"

    menu:
        "What about you and me?":
            anon f_shy "I just thought, maybe we..."
            show anon a_shy_neck f_shy_down
            with {'master': dissolve}
            anon "... Had something special, you know?"
            show anon a_sides f_surprised
            show nadya a_sides f_sexy:
                xoffset -398
            show svetlana a_sides f_surprised
            with {'master': dissolve}
            pause
            show anon a_surprised_up f_empty
            show nadya a_pinch_face f_pouting
            with {'master': dissolve}
            nadya "Aww, is this what upsets you?"
            show svetlana f_smirk
            nadya "You {i}are{/i} special to me, {b}[firstname]{/b}..."
            show anon a_surprised f_surprised
            show nadya a_finger f_frowning
            with {'master': dissolve}
            nadya "... But business comes first, understand?"
            show anon a_sides f_frown_down
            with {'master': dissolve}
            anon "I guess so."
            show nadya a_hips
            with {'master': dissolve}
        "Of course I do.":

            show anon a_surprised_up f_worried
            with {'master': dissolve}
            anon "N-no, it's not that!"
            anon "I think they're all gorgeous."
            show anon a_sides f_flirt
            with {'master': dissolve}
            anon "Like, crazy super duper hot."
            show anon f_flirt_grin
            show nadya f_surprised
            show svetlana a_surprised f_surprised
            with {'master': dissolve}
            pause
            show svetlana a_sides f_happy_down o_blush
            with {'master': dissolve}
            pause
            show anon a_surprised_up_both f_surprised_teeth
            show nadya a_crossed f_angry:
                xoffset -398
            with {'master': dissolve}
            anon @ -m_talk "!!!"
            anon f_worried @ f_shy "{i}*Ahem*{/i} N-not as beautiful as you, of course."
            show anon a_sides
            show svetlana f_surprised -o_blush
            with {'master': dissolve}
            nadya f_bored @ -m_talk "Mhmm."
            show svetlana f_concerned
            nadya f_confused "So what is problem?!"
            anon f_sad_down "{i}*Sigh*{/i} Nothing, I guess..."

    nadya f_normal "Then it's settled!" (show_native="Togda eto resheno!")
    nadya "Now please..."
    show nadya a_point_angry behind anon:
        xoffset 150 xzoom -1
    show svetlana f_happy
    with {'master': dissolve}
    nadya "... Work your magic."
    svetlana @ f_laugh "Heh..."
    show nadya a_sides
    with {'master': dissolve}
    svetlana "... dick magic." (show_native="... dik magiya.")
    show anon f_unimpressed
    show svetlana f_laugh
    nadya f_laugh "Hehe!"
    anon "Yeah, okay."
    hide anon
    show svetlana a_sides f_smirk:
        xoffset 450 xzoom -1
    with {'master': dissolve}
    svetlana "Go get her, tiger."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
