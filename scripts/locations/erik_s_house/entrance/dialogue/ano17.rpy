label ano17_init_erikhouse_entrance:
    scene expression background(400, 312, 1.5) as stage
    show anon with dissolve:
        flip
    anon "Halo?"

    pause
    show anon with dissolve:
        unflip
        xoffset 500
    anon "Anyone home?"

    tammy "{b}[firstname]{/b}?"

    show tammy:
        flip
    show anon:
        flip
        xoffset 0
    with {'master': dissolve}
    anon -a_wave @ a_wave "Hey, {b}Mrs. Johnson{/b}."


    if M_mrsj.finished_state(S_mrsj_cupid_report):
        tammy "Hey there, bubbeleh!"

        tammy "You lookin' for me?"

        anon f_shy "Ehh, no... Sorry."

        tammy "Well, that's a let down."

        tammy f_sexy "I just got back from yoga and I thought maybe you could help me relax a little?"

        anon "Aww, man... {i}*Gulp*{/i} Umm, is {b}Erik{/b} around?"

    else:
        tammy "Apa yang kamu lakukan di sini selarut ini?"

        tammy "You here to see {b}Erik{/b}?"

        anon "Y-ya, Bu."


    tammy "{b}Erik{/b}, your little friend, {b}[firstname]{/b} is here!"

    show anon f_normal
    erik "Apa?!"

    tammy f_annoyed "I said, {b}[firstname]{/b} is here!"

    pause
    erik "I'm in the basement, {b}Tam{/b}... I can't hear you!"

    tammy f_normal @ f_eyeroll a_sides "Oy vey."

    tammy "Why don't you head on down, dear."

    anon "Oh baiklah."

    pause
    anon "Did {b}Erik{/b} tell you we were expecting company?"

    tammy f_suspicious "Company?"

    tammy "What kind of company?"

    anon "Just a new friend we made."

    anon @ f_laugh "Her name is {b}Iwanka{/b}."

    tammy f_surprised "You boys invited a girl over here?"

    anon "Ya, Bu."

    tammy f_suspicious "At this ungodly hour?"

    tammy "Is she Jewish?"

    anon @ f_thinking "N-no, I don't think so..."

    tammy @ -m_talk "Hmph."

    tammy f_normal "Well, this is a surprise!"

    pause
    tammy "I suppose I should be glad you boys are becoming more sociable..."

    anon "Yeah, we're trying."

    tammy "Do you want me to fix something to eat?"

    tammy "I think I have a pot roast in the freezer I could heat up."

    anon @ f_brag_closed a_surprised_up_both "Tidak, tidak, tidak apa-apa."

    tammy "Apa kamu yakin?"

    tammy "It's no bother."

    anon "Could you just send her downstairs when she arrives?"

    tammy "Yeah, of course dear."

    show anon with dissolve:
        xoffset 100
    tammy "You boys want something to snack on?"

    anon f_shy @ a_wave "No really, I'm good."

    tammy @ f_eyeroll "Tsk, come now!"

    tammy f_sexy "We've got popsicles!"

    anon "Maybe later, {b}Mrs. Johnson{/b}..."

    tammy @ f_eyeroll "Baiklah, sesuaikan dirimu."

    hide anon with dissolve
    pause
    tammy f_suspicious "I wonder if they'd eat some kreplach if I made it?"

    tammy f_laugh "{b}Erik{/b} loves my kreplach."


    scene expression background(360, 440, 3.5, l=L_erikhouse_basement) as stage with fade
    show anon with dissolve
    anon "{b}Erik{/b}?"

    erik "I'm in the den, {b}[firstname]{/b}!"

    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
