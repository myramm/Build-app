label melonia_button_recovery:
    show anon f_worried with dissolve
    melonia "You're back!"
    show anon with dissolve:
        xoffset 200
    anon "Yeah, I just wanted to check and make sure you're both doing okay."
    melonia a_baby_give "Here!"
    anon "Wait a second, I-"
    show anon a_melonia_baby
    show melonia a_crossed
    with dissolve
    anon "{b}Melonia{/b}, I can't stay."
    melonia "Too late!"
    show melonia b_gown_bed_back with dissolve
    pause
    anon f_sad_down "Aww, man..."
    pause
    show anon f_frown_down
    anon "Your daddy walked right into that, didn't he, little one?"
    anon f_shy_down "Yes, he did."
    if M_melonia.pregnancy.baby_gender == "boy":
        anon @ f_laugh "Heh, you{#male} are so cute!"
    else:
        anon @ f_laugh "Heh, you{#female} are so cute!"

    scene black with slowdissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
