label liu_button_recovery:
    show anon with dissolve:
        xoffset 200
    anon "Hey, how are you feeling?"
    liu f_nervous "A bit stir crazy from being stuck in this bed but otherwise good."
    show anon f_confused

    if M_liu.pregnancy.baby_gender == 'boy':
        anon "Any improvement with him latching on?"
    else:
        anon "Any improvement with her latching on?"

    show anon f_normal_low
    show liu f_happy_baby

    if M_liu.pregnancy.baby_gender == 'boy':
        liu "Yes, he's a greedy guy too."
        liu "Aren't you{#boy}, little one?"
    else:
        liu "Yes, she's a greedy girl too."
        liu "Aren't you{#girl}, little one?"

    anon f_laugh "Hehe."
    pause
    show liu f_happy
    anon f_normal "Well, you'll both be home before you know it."
    anon "You should enjoy the bed rest and the army of nurses while you can."
    liu "Yeah, your probably right about that."
    anon "Call me if you need anything, yeah?"
    liu f_happy "I will."
    liu "Thank you, {b}[firstname]{/b}."
    show anon a_wave f_happy with dissolve
    pause
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
