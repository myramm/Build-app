label ricky_button_garden:
    show ricky f_smirk
    show anon f_worried at flip with dissolve
    ricky "Hola, amigo."
    ricky "Why don't you pop that shirt off and come help me with the gardening?"
    anon "Uhh, I'm not sure that's a good idea..."
    ricky "Hmm, no?"
    ricky "Just pop the shirt off and supervise then."
    ricky "I could use the motivation."

    menu ricky_button_garden.choice:
        "{b}Consuela{/b}." if M_consuela.is_state(S_con01_init):
            if M_ricky.once('con02_dialogue_consuela'):
                jump con01_init_ricky.repeat
            else:
                jump con01_init_ricky

        "Replacement for {b}Consuela{/b}." if M_consuela.is_state(S_con01_plan):
            jump con01_plan_ricky
        "Motivation?":

            jump ricky_button_garden.motivation
        "Are you gay?":

            jump ricky_button_garden.gay
        "I should go.":

            pass

    show ricky f_smirk
    anon f_normal "See ya around, {b}Ricky{/b}."
    ricky @ f_sad "Aww, I hate to see you go, amigo..."
    pause
    ricky "... But I love to watch you leave."
    anon f_grumpy @ -m_talk "..."
    hide anon with dissolve
    return


label ricky_button_garden.motivation:
    show ricky f_smirk
    anon @ f_confused "Motivation?"
    ricky "That's right!"
    ricky "Nothing motivates me more than a spicy little taquito barking orders at me."
    anon f_grumpy "Eh."
    ricky "Really let me have it though, yeah?"
    ricky "I've been a naughty boy..."

    menu:
        "Pass.":
            anon "Yeeeeeah, no."
            ricky f_sad "Aww."
            pause
            ricky f_smirk "You're no fun, amigo."
            show anon f_worried
        "Maybe later.":

            anon f_worried "Maybe some other time..."
            ricky "Ah, if you wish, amigo..."
            ricky "... I hold you to it though, eh?"
            anon @ -m_talk "..."
            ricky @ f_laugh "Hehehe!"

    jump ricky_button_garden.choice


label ricky_button_garden.gay:
    show ricky f_smirk
    anon f_skeptical "Are you gay?"
    ricky "What gave it away?"
    ricky @ f_laugh "Hehe!"
    anon f_worried "I thought you and {b}Mrs. Rump{/b} were uhh... You know?"
    ricky f_confused "You think I would let that old broad have her way with me?!"
    ricky f_smirk @ f_laugh "Hahahaha!!"
    anon f_confused @ -m_talk "..."
    anon "I saw her all over you earlier!"
    ricky "Oh, she wants it, that's for sure!"
    ricky "She pays me a little extra on the side to entertain her..."
    ricky "... And yeah, I flirt with her a bit, but only to increase my earnings!"
    ricky "A girl's gotta get paid, you know?"
    anon f_worried @ -m_talk "..."
    ricky "I wouldn't sex her for all the money in world!"
    anon "You wouldn't?"
    ricky "Hell no!"
    ricky "My little Aztec warrior only likes the boys, eh?"
    anon f_skeptical "Your little wha-"
    ricky f_laugh "My Aztec warrior, amigo!"
    anon @ -m_talk "..."
    ricky f_smirk "Look at you blush!"
    ricky "You're too adorable!"
    anon f_worried "Y-yeah, thanks."
    jump ricky_button_garden.choice
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
