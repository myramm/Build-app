label jos02_init_dealership_showroom:
    call josie_button_stage
    show anon with dissolve
    anon "Hey, {b}Josephine{/b}!"

    josephine @ -m_talk "Hmm?"

    show josephine b_dressed f_sexy a_sides m_talk with dissolve
    josephine -m_talk "Oh, hei!"

    josephine "Ada apa, {b}[firstname]{/b}?"

    anon "I didn't know if you'd still be here or not..."

    josephine f_concerned "Hah?"

    josephine "Why wouldn't I be here?"

    anon f_worried "You know, because last time I was here we-"

    josephine a_idle f_sexy "What, because my dad caught us fucking in his office?"

    anon f_surprised "!!!"
    anon f_shy "Y-ya?"

    josephine @ f_laugh "hehe!"

    josephine "He was pretty mad, wasn't he?"

    anon "I thought you were gonna get fired for sure this time..."

    josephine "I told you he wouldn't do it."

    josephine "He just yelled and then told me I need to start looking for a new place to live."

    anon f_surprised "Wait, he's kicking you out?!"

    josephine @ f_eyeroll "Pfft, no."

    josephine "He told me I had six months to find a place."

    anon f_worried "That sounds like he's kicking you out, {b}Josephine{/b}."

    josephine "It's just idle threats, he'd never actually do it..."

    anon "Apa kamu yakin?"

    pause
    josephine "Cukup yakin."

    josephine "Mengapa?"

    josephine "Do you know a place where I could stay?"


    menu:
        "Tidak juga.":
            pass

    anon "If I think of something-"

    josephine f_normal "Jangan khawatir tentang hal itu."

    pause
    josephine f_normal_down a_phone "Seriously, he'll never do it."

    anon "Oh oke..."

    pause
    show josephine f_sexy_down
    pause
    if game.timer.is_day():
        josephine f_sexy "So, you wanna go up to the break room and bang one out?"

    else:
        josephine f_sexy "So, you wanna go up to my dad's office and bang one out?"

    anon f_shock "!!!"
    anon f_surprised "Kamu serius?"

    josephine "Sangat serius."

    josephine "I didn't even get to finish last time."


    menu:
        "Tentu saja!":
            anon f_normal "Tentu saja!"

            jump jos02_init_dealership_showroom.sex
        "Ide buruk.":

            pass

    anon f_worried "What if your father catches us again?"

    josephine @ f_concerned "So what if he does?"

    josephine "I don't give a shit."

    anon a_thinking f_thinking @ -m_talk "..."
    josephine f_concerned "C'mon, please!"


    menu:
        "Baiklah baiklah.":
            anon f_normal a_idle "Baiklah baiklah."

            jump jos02_init_dealership_showroom.sex
        "Mustahil!":

            pass

    anon f_worried a_idle "If he catches us again, he'll kick you out for sure."

    josephine @ f_laugh "Hah!"

    josephine @ f_eyeroll "Ya benar."

    josephine f_normal_down a_phone "Apa pun."

    josephine "Sesuaikan dirimu."

    hide anon with dissolve
    return


label jos02_init_dealership_showroom.sex:
    josephine f_sexy @ f_laugh "Ya, ya!"

    josephine "Ayo lakukan!"

    hide josephine with dissolve
    anon @ f_laugh a_cheering "( This girl is the best kind of crazy! )"

    hide anon with dissolve
    return True
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
