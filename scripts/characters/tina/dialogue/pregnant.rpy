label tina_button_pregnant:
    $ renpy.dynamic(local=flip if L_bank_lobby.is_here(M_tina) else reset)

    if M_tina.outfit.is_naked:
        show tina f_sad
        show anon f_worried with dissolve
        anon "Wow, it is scorching in-"
        anon f_surprised "!!!"
        anon f_flirt_low "In here..."
        tina "Hey there, {b}[firstname]{/b}."
        tina "Sorry about the heat."
        anon f_flirt "Y-you're naked!"
        tina @ f_laugh "Heh, yeah, I know."
        tina "Our A/C broke and {b}Tony{/b} is having trouble getting it fixed."
    else:
        show anon at local with dissolve
        anon "Hey, {b}Tina{/b}."
        tina "Hey there, {b}[firstname]{/b}."

    menu tina_button_pregnant.choice:

        "Can't you pay to have it fixed?" if M_tina.outfit.is_naked:
            jump tina_button_pregnant.aircon
        "How are you feeling?":

            if M_tina.pregnancy.stage == 1:
                jump tina_button_pregnant.excited
            elif M_tina.pregnancy.stage == 2:
                jump tina_button_pregnant.sick
            else:
                jump tina_button_pregnant.bloated
        "Can I get you anything?":

            if M_tina.pregnancy.stage == 1:
                jump tina_button_pregnant.obgyn
            elif M_tina.pregnancy.stage == 2:
                jump tina_button_pregnant.nutritionist
            else:
                jump tina_button_pregnant.masseuse
        "I'll see you soon.":

            pass

    anon f_normal a_wave "I'll see you soon."
    show tina f_normal
    anon "Feel free to call me, night or day..."
    anon "... Okay?"
    tina "That shouldn't be necessary but I appreciate the sentiment, {b}[firstname]{/b}."
    anon f_worried @ -m_talk "..."
    tina "Take care."
    hide anon with dissolve
    return


label tina_button_pregnant.aircon:
    anon f_worried "Can't you pay to have it fixed?"
    tina f_sad "I could, sure."
    tina "But {b}Tony{/b} insists on fixing it himself."
    anon "This can't be good for the baby..."
    tina "Oh, it's fine."
    tina "My OB/GYN says it would have to be a lot hotter than this before we needed to worry."
    anon "Still..."
    becca "Hey, Mom?"
    becca "I can't get this stupid fan to wor-"
    show becca b_panties_sweat f_surprised behind tina with dissolve:
        xoffset -300
    show anon f_surprised
    becca "!!!"

    if M_roxxy.finished_state(S_roxxy_get_oil):
        show becca b_panties_sweat_cover with fastdissolve
        becca "{b}[firstname]{/b}?!"
        anon f_normal "Hey, {b}Becca{/b}."
        becca "Wha-"
        show becca f_upset with dissolve:
            flip
            xoffset 300
        becca "Why didn't you warn me he was coming over!"
        show anon f_flirt_low
        tina "Because I didn't know..."
        becca f_concerned "I don't want him to see me like this!"
        tina "Like what, sweetie?"
        anon "Yeah, you're fine, {b}Becca{/b}."
        show becca with dissolve:
            unflip
            xoffset -300
        show anon f_flirt
        becca "No, I'm not!"
        becca "I'm all sweaty and gross and..."
        show becca with dissolve:
            flip
            xoffset 300
        becca "... A-and don't look at me, I'm hideous!"
        hide becca with dissolve
        show anon f_skeptical
        pause
        tina f_normal "Oh, don't mind her."
        show anon f_normal
        tina "She's just embarrassed."
    else:
        show becca f_upset with dissolve:
            flip
            xoffset 300
        becca "What is he doing here again?!"
        show anon f_flirt_low
        tina "He's here to check on the baby, of course..."
        becca @ f_eyeroll "Ugh!"
        becca "It is so fucked up that you two are having a baby together!"
        tina "{b}Becca{/b}, don't be rude!"
        becca "Whatever."
        becca "Come help me with this stupid fan once the nerd leaves..."
        hide becca with dissolve
        show anon f_normal
        pause
        tina "Oh, don't mind her."
        tina "She's just grumpy about the heat."

    anon @ -m_talk "..."
    jump tina_button_pregnant.choice


label tina_button_pregnant.bloated:
    anon f_worried "How are you feeling?"
    tina f_sad "Bloated."
    tina "Sore."
    tina "Not to mention I'm melting in this heat!"
    anon "Y-yeah, no doubt."
    pause
    tina "At least we're nearing the end."
    tina f_normal "I can't wait to meet our child!"
    anon f_normal "Yeah, it's quite exciting."
    jump tina_button_pregnant.choice


label tina_button_pregnant.excited:
    anon f_normal "How are you feeling?"
    tina f_normal @ f_laugh "Heh, checking up on me, huh?"
    anon "Yeah, if that's okay?"
    tina "Of course."
    tina "It's very sweet of you!"
    tina "I haven't had a man to dote on me since Luigi died..."
    anon "Well, I'm here if you need anything."
    tina "Thank you, {b}[firstname]{/b}."
    jump tina_button_pregnant.choice


label tina_button_pregnant.masseuse:
    anon f_normal "Can I get you anything?"
    anon "Back massage or a foot rub maybe?"
    tina f_normal @ f_laugh "Heh, no that's okay."
    tina "{b}Becca{/b} and I have been going to a masseuse twice a week."
    anon "A masseuse?"
    tina "Yeah."
    tina "Like I said, it's important to do everything I can to help ensure the baby is born happy and healthy."
    anon f_unimpressed "And luckily, you have plenty of money to do exactly that..."
    tina @ -m_talk "Mhmm."
    anon @ -m_talk "( I sure wish I could play a bigger role here... )"
    jump tina_button_pregnant.choice


label tina_button_pregnant.nutritionist:
    anon f_normal "Can I get you anything?"
    anon "Something to snack on or a drink maybe?"
    tina f_normal "Heh, no that's okay."
    tina "My nutritionist has me on a very strict food regiment for the baby..."
    anon @ f_skeptical "You have a nutritionist?"
    tina "Of course."
    tina "A woman my age, it's important to do everything I can to help ensure the baby is born happy and healthy."
    pause
    tina "Luckily, I have plenty of money to do exactly that."
    anon "Y-yeah, that's wonderful, {b}Tina{/b}."
    jump tina_button_pregnant.choice


label tina_button_pregnant.obgyn:
    anon f_normal "Can I get you anything?"
    anon "Nausea medication maybe?"
    tina f_normal "Heh, no that's okay."
    tina "I have a specialist making house calls three times a week..."
    anon @ f_skeptical "A specialist?"
    tina "Yeah, my OB/GYN."
    tina "Like I said, it's important to do everything I can to help ensure the baby is born happy and healthy."
    pause
    tina "Luckily, I have plenty of money to do exactly that."
    anon @ f_laugh "Y-yeah, that's wonderful, {b}Tina{/b}."
    jump tina_button_pregnant.choice


label tina_button_pregnant.sick:
    anon f_normal "How are you feeling?"
    tina f_sad "Ugh, I forgot how much I hate morning sickness..."
    anon f_worried "Pretty bad, huh?"
    tina "It's ten times worse than it was with {b}Becca{/b}!"
    tina "I guess, because I'm older now..."
    anon "Yeah, that would make sense."
    jump tina_button_pregnant.choice
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
