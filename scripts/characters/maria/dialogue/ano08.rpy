label ano08_late_maria:
    show anon with dissolve
    anon "Hi, {b}Maria{/b}, I'm here to {b}move the flour{/b}."

    show maria b_dressed f_confused with dissolve
    maria "{b}[firstname]{/b}?"

    maria "Isn't it past your bedtime?"

    maria "It's too late to move the flour now. I won't need it until tomorrow."

    anon f_worried "Oh..."

    anon "Sorry, {b}Maria{/b}."

    maria f_sad "Never mind, I'll see you tomorrow, OK?"

    anon @ a_wave "Yes... Have a good night."

    hide anon with dissolve
    return


label ano08_sack_maria:
    show anon with dissolve
    anon "Hi, {b}Maria{/b}."

    show maria a_spoon_hips f_normal with dissolve:
        unflip
        xoffset 0
    maria "Did you {b}bring me that flour out of the back{/b} like I asked you?"

    anon "Belum."

    anon "I'm getting it now."

    maria f_confused "Do ya need {b}Tony{/b} to help ya?"

    anon f_worried "N-no, I've got it."

    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
