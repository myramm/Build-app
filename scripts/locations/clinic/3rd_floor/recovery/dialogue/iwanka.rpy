label hospital_recovery_iwanka_first:
    scene expression game.timer.image('location_hospital_baby_bed{}')
    show iwanka b_gown_bed f_drunk
    with fade
    show anon f_worried with dissolve
    anon "Did I miss it?"

    iwanka @ f_laugh "Heee!"

    iwanka "You're here!"

    show anon f_shy_low with dissolve:
        xoffset 200
    anon "Is that our-"

    iwanka "Say hi to daddy."


    if M_iwanka.pregnancy.baby_gender == "boy":
        anon "It's a boy?"

        iwanka "It's a boy!!!"

        anon "He's beautiful."

    else:

        anon "It's a girl?"

        iwanka "It's a girl!!!"

        anon "She's beautiful."


    iwanka "They're giving me some REALLY good drugs right now!"

    anon f_worried "Oh?"

    anon "I guess that explains why you seem a little loopy..."

    iwanka "You want some?"

    anon "T-tidak, tidak apa-apa."

    iwanka "Anda yakin?"

    iwanka @ f_annoyed "Nurse!!"

    show anon f_hurt
    iwanka "Can you get my boyfriend an IV full of whatever it is you're giving me?!"

    show anon f_worried a_wave with dissolve:
        flip
        xoffset -500
    anon "She's joking!"

    anon "We're good in here."

    show anon a_idle with dissolve:
        unflip
        xoffset 0
    iwanka @ f_laugh "Hehehe!"

    pause
    anon f_shy "So everything went okay?"

    iwanka @ -m_talk "Hmm?"

    iwanka "Tentu saja!"

    iwanka @ f_thinking "Well, I kinda made one of the security guys cry..."

    anon f_worried "Hah?"

    iwanka "The nurse told him to hold my hand while she gave me the epidural."

    iwanka "And there was this pop..."

    anon f_surprised "You broke his hand?!"

    iwanka "That's what they told me."

    anon "Sialan!"

    iwanka f_suspicious "Hey, do you smell cotton candy?"

    anon "Maybe I should take the baby so you can rest?"

    iwanka f_drunk "No, no... We're good!"

    iwanka "I will take some of that cotton candy though... If you can find it."

    anon f_shy a_behind_head "Heh, pretty sure that's just the drugs, {b}Iwanka{/b}..."

    iwanka "Blue please."

    show anon f_worried
    pause
    iwanka "The best foods are blue."

    anon "Benar."

    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
