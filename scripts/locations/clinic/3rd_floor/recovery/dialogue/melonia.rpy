label hospital_recovery_melonia_first:
    scene expression game.timer.image('location_hospital_baby_bed{}')
    show melonia b_gown_bed f_annoyed
    with fade
    show anon f_worried with dissolve
    anon "Did I miss it?"

    melonia "It's about fucking time you showed up!"

    anon "Maafkan aku, aku-"

    pause
    anon f_shy "Is that?"

    show anon with dissolve:
        xoffset 200

    if M_melonia.pregnancy.baby_gender == "boy":
        melonia a_baby_give "Here, take him!"

        show melonia a_crossed
        show anon a_melonia_baby f_shy_down
        with dissolve
        anon "It's a boy?"

        melonia "Yes, it's a boy."

    else:

        melonia a_baby_give "Here, take her!"

        show melonia a_crossed
        show anon a_melonia_baby f_shy_down
        with dissolve
        anon "It's a girl?"

        melonia "Yes, it's a girl."


    melonia "The little shit has puked on me three times today!"


    if M_melonia.pregnancy.baby_gender == "boy":
        melonia "Barely born and he's already a pain in my ass."

        pause
        anon "He's so beautiful!"

        melonia "Well, of course he's beautiful, I'm his mother after all."

    else:

        melonia "Barely born and she's already a pain in my ass."

        pause
        anon "She's so beautiful!"

        melonia "Well, of course she's beautiful, I'm her mother after all."


    pause
    melonia "See if you can get that nurse back in here..."

    melonia "... She's supposed to give me information on local wetnurses."

    anon f_confused "Wetnurses?"

    anon "Why would we need a wetnurse?"

    melonia "Well, I'm certainly not going to breastfeed it!"

    anon f_worried "Kenapa?"

    melonia "Umm, have you seen what that does to a woman's breasts?!"

    melonia "No, thank you!"

    anon "{b}Melonia{/b}..."

    melonia "Look {b}[firstname]{/b}, I'm already going to need vaginal rejuvenation surgery because of this..."

    melonia "... And if you think I'm getting my tits redone too, you're out of your fucking mind!"

    anon "Breastfeeding builds up their immune system and strengthens the bond between mother and child."

    melonia "I don't need to strengthen my bond with it."

    anon "Kamu bersikap konyol."

    melonia "{b}Iwanka{/b} wasn't breastfed and she turned out fine..."

    pause
    melonia "... Or near enough anyways."

    anon @ -m_talk "..."
    melonia f_yell "Stop looking at me like that!"

    melonia "We're getting a wetnurse and that's the end of it!"

    show melonia f_annoyed
    anon @ f_eyeroll "Uh, baiklah."

    melonia "I don't want to hear another word about it!"

    anon f_angry "I said, fine!"

    melonia f_pouting @ -m_talk "Hmph!"

    pause
    melonia f_annoyed "I'm going to take a nap."

    anon f_unimpressed "Good, you obviously need it."

    melonia "Saya bersedia!"

    anon f_angry "So take one."

    melonia "Saya akan!"

    anon "Bagus."

    melonia "Bagus!"

    pause
    show melonia b_gown_bed_back with dissolve
    pause
    melonia "Wake me up when they say I'm good to return home."

    anon "Ya baiklah."

    pause
    anon f_surprised "Tunggu, apa?!"

    anon "I can't stay here that long!"

    pause
    anon f_worried "{b}Melonia{/b}?"

    pause

    if M_melonia.pregnancy.baby_gender == "boy":
        anon f_frown_down "{i}*Sigh*{/i} Your{#male} mommy is a terrible grump."

    else:
        anon f_frown_down "{i}*Sigh*{/i} Your{#female} mommy is a terrible grump."


    anon f_shy_down "Yes, she is!"


    scene black with slowdissolve

    $ game.timer.tick()
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
