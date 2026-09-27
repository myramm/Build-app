label pizzeria_interior_job_complete:
    call tony_button_stage

    if M_anon.is_state(S_ano04_test):
        jump pizzeria_interior_job_complete.audition
    else:
        jump pizzeria_interior_job_complete.repeat


label pizzeria_interior_job_complete.audition:
    if res.pay == 0:
        show tony f_suspicious
        with fade
        show anon f_sad_down with dissolve:
            flip
        tony "You didn't get a single one right?"

        anon f_worried "Sorry, {b}Tony{/b}... I don't know what happened."

        tony @ f_laugh "Ugh, you're killin' me smalls."

        tony "Get back out there and try again!"

        anon "Y-ya, tuan!"

        hide anon with {'master': dissolve}
        tony f_angry "And this time get it right!"

        jump pizzeria_interior_job

    with fade
    show anon with dissolve:
        flip

    if res.perfect:
        tony "Hey, it wasn't in a flash but you were pretty dang close."

        anon @ f_laugh "So I'm hired?"

        tony a_money "Heh, not only are you hired but I'm throwing in a bonus for the perfect run!"

    else:
        tony "Hey, not bad buddy!"

        anon @ f_thinking "Meh, I could have done better..."

        tony "Oh, you'll get the hang of it."

        pause
        tony "The important thing is you've earned yourself a job."

        anon "So I'm hired?"

        tony a_money "Anda yakin."


    show anon a_money
    show tony a_idle
    with dissolve
    show anon a_idle with dissolve
    tony "Now I want you to take this money and {b}put it in the bank{/b}."

    tony "You're gonna save up everything you earn with that bike and turn it into somethin' better, capisce?"

    anon "Alright, I can do that."

    tony "Atta' boy, {b}[firstname]{/b}!"

    tony "You stick with me and you'll go far, you hear?"

    anon "Ya, tuan!"

    hide anon with dissolve
    return


label pizzeria_interior_job_complete.repeat:
    if res.pay == 0:
        show tony f_suspicious
        with fade
        show anon f_sad_down with dissolve:
            flip
        tony "You didn't get a single one right?"

        anon "Sorry, {b}Tony{/b}... I don't know what happened."

        tony "Ugh, you're killin' me smalls."

        tony "I'm trying to run a business here!"

        anon f_worried "I'll do better next time, I promise."

        tony "Yah, aku harap begitu!"

        hide anon with dissolve
        return

    with fade
    show anon with dissolve:
        flip

    if res.perfect:
        tony "Man, you are killin' it out there!"

        tony a_money "I threw in a little extra for the perfect run."

        show anon a_money
        show tony a_idle
        with dissolve
        anon "Terima kasih, {b}Tony{/b}."

        show anon a_idle with dissolve
        tony "My pleasure, buddy."

    else:
        tony "Nice work out there, buddy."

        anon @ f_thinking "Meh, I could have done better..."

        tony "Yeah, you coulda but you still done good."

        show anon a_money
        show tony a_idle
        with dissolve
        tony "You'll get the hang of it."

        show anon a_idle with dissolve
        anon "Terima kasih, {b}Tony{/b}."


    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
