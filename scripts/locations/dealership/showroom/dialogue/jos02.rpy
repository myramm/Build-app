label jos02_init_dealership_showroom:
    call josie_button_stage
    show anon with dissolve
    anon "Hey, {b}Josephine{/b}!"
    josephine @ -m_talk "Hmm?"
    show josephine b_dressed f_sexy a_sides m_talk with dissolve
    josephine -m_talk "Oh, hey!"
    josephine "What's up, {b}[firstname]{/b}?"
    anon "I didn't know if you'd still be here or not..."
    josephine f_concerned "Huh?"
    josephine "Why wouldn't I be here?"
    anon f_worried "You know, because last time I was here we-"
    josephine a_idle f_sexy "What, because my dad caught us fucking in his office?"
    anon f_surprised "!!!"
    anon f_shy "Y-yeah?"
    josephine @ f_laugh "Hehe!"
    josephine "He was pretty mad, wasn't he?"
    anon "I thought you were gonna get fired for sure this time..."
    josephine "I told you he wouldn't do it."
    josephine "He just yelled and then told me I need to start looking for a new place to live."
    anon f_surprised "Wait, he's kicking you out?!"
    josephine @ f_eyeroll "Pfft, no."
    josephine "He told me I had six months to find a place."
    anon f_worried "That sounds like he's kicking you out, {b}Josephine{/b}."
    josephine "It's just idle threats, he'd never actually do it..."
    anon "Are you sure?"
    pause
    josephine "Pretty sure."
    josephine "Why?"
    josephine "Do you know a place where I could stay?"

    menu:
        "Not really.":
            pass

    anon "If I think of something-"
    josephine f_normal "Don't worry about it."
    pause
    josephine f_normal_down a_phone "Seriously, he'll never do it."
    anon "Oh kay..."
    pause
    show josephine f_sexy_down
    pause
    if game.timer.is_day():
        josephine f_sexy "So, you wanna go up to the break room and bang one out?"
    else:
        josephine f_sexy "So, you wanna go up to my dad's office and bang one out?"
    anon f_shock "!!!"
    anon f_surprised "You're serious?"
    josephine "Dead serious."
    josephine "I didn't even get to finish last time."

    menu:
        "Definitely!":
            anon f_normal "Definitely!"
            jump jos02_init_dealership_showroom.sex
        "Bad idea.":

            pass

    anon f_worried "What if your father catches us again?"
    josephine @ f_concerned "So what if he does?"
    josephine "I don't give a shit."
    anon a_thinking f_thinking @ -m_talk "..."
    josephine f_concerned "C'mon, please!"

    menu:
        "Alright, fine.":
            anon f_normal a_idle "Alright, fine."
            jump jos02_init_dealership_showroom.sex
        "No way!":

            pass

    anon f_worried a_idle "If he catches us again, he'll kick you out for sure."
    josephine @ f_laugh "Hah!"
    josephine @ f_eyeroll "Yeah, right."
    josephine f_normal_down a_phone "Whatever."
    josephine "Suit yourself."
    hide anon with dissolve
    return


label jos02_init_dealership_showroom.sex:
    josephine f_sexy @ f_laugh "Hell yeah!"
    josephine "Let's do it!"
    hide josephine with dissolve
    anon @ f_laugh a_cheering "( This girl is the best kind of crazy! )"
    hide anon with dissolve
    return True
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
