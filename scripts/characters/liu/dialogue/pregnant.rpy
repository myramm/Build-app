label liu_button_pregnant:
    $ renpy.dynamic(bank=L_bank_lobby.is_here(M_liu))

    show anon with dissolve

    if bank:
        liu "Welcome to {b}Saga Financial{/b}."
        liu f_normal "How can I help-"
        show liu a_mouth_cover f_surprised
        with {'master': dissolve}
        liu "{b}[firstname]{/b}!!"
        anon "Hey, Liu."
        show liu a_idle f_nervous with {'master': dissolve}
        liu "Did you come to check up on us?"
    else:

        anon "Hey, {b}Liu{/b}."
        liu "Hey, {b}[firstname]{/b}."

    menu liu_button_pregnant.choice:
        "How are you feeling?":
            jump liu_button_pregnant.feeling

        "Is Tina around?" if bank and M_tina.is_state(S_tin02_init):
            if L_bank_cubicle.is_here(M_tina):
                jump tin02_init_liu
            jump liu_button_pregnant.tina

        "Did you inform {b}Tina{/b}?" if bank:
            jump liu_button_pregnant.lonely

        "Can I get you anything?" if not bank:
            jump liu_button_pregnant.anything
        "Let me know if you need anything.":

            pass

    show liu f_happy

    if bank:
        anon "Call me if you need anything."
        anon "I'll be here in an instant, I promise."
        liu "You're such a good man, {b}[firstname]{/b}."
        liu "Thank you."
        anon f_shy "You're welcome, {b}Liu{/b}."
    else:

        anon "Let me know if you need anything."
        liu "Okay, {b}[firstname]{/b}."
        liu "Thanks for checking on me."
        anon f_shy "Of course, {b}Liu{/b}."
        anon "I'll always be around if you need something."

    hide anon with dissolve
    return


label liu_button_pregnant.anything:
    show liu f_happy
    anon "Is there anything I can get you?"
    liu f_curious @ -m_talk "Hmm?"
    anon f_thinking "A comfort food maybe?"
    show anon f_normal
    liu f_nervous_down "No, that's very sweet of you to offer but I'm sticking to a strict diet for the sake of our child."
    anon f_confused "Oh?"
    liu f_happy "Since it's summer, I got some goji berries, walnuts, and wild caught salmon from the chinese market in the big city."
    anon f_normal "Well, that sounds good."
    liu "I remember my mother used to saute spinach and eggs in some butter and soy sauce every morning when she was pregnant with my younger brother."
    anon "I guess you have the food under control then..."
    anon f_thinking "... Maybe I could give you a back rub or something?"
    show anon f_normal
    liu f_nervous_lipbite_back @ -m_talk "Mmm."
    liu f_sexy "I might take you up on that later, {b}[firstname]{/b}."
    anon f_shy "Heh, I'm at your beck and call, m'lady."
    liu f_laugh "Hehe!"
    pause
    show liu f_happy
    jump liu_button_pregnant.choice


label liu_button_pregnant.feeling:
    show liu f_happy
    anon f_confused "How are you feeling?"
    liu f_curious @ -m_talk "Hmm?"
    liu f_normal "Oh, I'm fine."
    show anon f_shy
    liu f_nervous_back "Having children is a woman's main profession back where I come from, so..."
    liu f_nervous "... My mother taught me quite a lot as child."
    anon f_normal "Really?"
    liu f_normal @ -m_talk "Mhmm."
    liu "Her home remedies to ward off morning sickness are particularly effective."
    anon "Wow, that's amazing!"
    show anon a_thinking f_thinking with dissolve
    pause
    show anon a_point f_normal with {'master': dissolve}
    anon "You know, I bet there's a huge market for home remedies like that!"
    liu f_curious "Oh?"
    show anon a_sides f_normal_high with {'master': dissolve}
    anon f_normal_high "Particularly in Summerville..."
    anon f_normal "... Pregnancies are a big thing around here."
    liu f_surprised "I had no idea."
    jump liu_button_pregnant.choice


label liu_button_pregnant.lonely:
    show liu f_happy
    anon f_normal "Did you let {b}Tina{/b} know about the baby yet?"
    liu "Oh, yes!"
    liu "She was very excited for me."
    anon "I'll bet."
    pause
    liu f_surprised "Did you know women get six weeks paid maternity leave in this country?"
    anon f_confused "Yeah, I've heard about that."
    show anon f_normal
    liu f_curious "When {b}Tina{/b} told me that, I couldn't believe it!"
    show liu f_worried
    pause
    liu "Is it really okay for me to take so much time?"
    anon f_happy "Heh, of course {b}Liu{/b}."
    show liu f_curious
    anon f_normal "They give you that much time for a reason..."
    anon "... It's important to both your physical and mental well being."
    liu f_normal "Yeah, I guess that makes sense."
    show liu f_ashamed_down
    pause
    liu f_worried_down "I still feel bad leaving {b}Tina{/b} here all by herself."
    show liu f_normal_down
    pause
    liu f_happy "Maybe you can stop in and keep her company while I'm away?"
    anon f_confused "Keep her company?"
    liu "Yeah, just to make sure she doesn't get too lonely with me at home."
    show anon a_behind_head f_worried with {'master': dissolve}
    anon "Ehh..."
    liu f_nervous "Please?"
    show anon a_sides with {'master': dissolve}
    anon "... If that's what you want."
    show anon f_normal
    liu f_happy_excited_closed "Yay!!"
    liu f_happy "Thank you, {b}[firstname]{/b}!"
    anon "Heh, no problem."
    jump liu_button_pregnant.choice


label liu_button_pregnant.tina:
    anon f_normal "Is Tina around?"
    if game.timer.is_weekend():
        liu f_worried "No, she only works on {b}weekdays{/b}."
    else:
        liu f_worried "No, She won't be in until later {b}this afternoon{/b}."
    show anon f_worried
    liu f_curious "Can I help?"
    anon f_normal "No, no, that's okay, it can wait."
    show liu f_nervous
    jump liu_button_pregnant.choice
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
