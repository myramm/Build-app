label pizzeria_kitchen_intro:
    scene expression background(720, 400, 3.2) as stage
    show maria b_dressed_behind:
        yoffset 40
    with fade
    maria @ -m_talk "{i}*Sluuuuurp*{/i}"

    pause
    show maria b_dressed a_spoon_taste f_taste with dissolve:
        flip
        offset (500, 0)
    maria @ -m_talk "Hmm!"

    show maria a_spoon_point f_normal with dissolve
    show anon behind maria with dissolve:
        xoffset 100
    maria "Magnifico!"

    pause
    maria "Those roasted red peppers were a great idea!"

    pause
    anon "Halo."

    show maria a_spoon_startled f_surprised with {'master': fastdissolve}
    maria "!!!"
    show maria a_spoon_heart with dissolve:
        unflip
        xoffset 100
    maria f_angry "W-who the hell are you?!"

    show anon f_worried
    show maria a_spoon_hips with dissolve
    anon @ a_behind_head "Oh, I'm uhh-"

    maria "{b}TONY{/b}!!!"

    maria "There's some weirdo back here in the kitchen!"

    anon a_up "N-no, no, no... I'm not-"

    tony "What are you screamin' about?"

    show tony f_suspicious behind anon with dissolve:
        flip
        xoffset -100
    show anon a_idle with dissolve
    maria "You let this kid sneak right past you!"

    tony "Nobody snuck past me..."

    maria "Well then, what's he doin' back here?!"

    tony f_normal "He's our new delivery boy."

    show maria f_confused
    pause
    maria @ a_spoon_point "What? Him?!"

    tony "Yeah, what's the matter with that?"

    maria "He's a little young, don'tcha think?"

    tony "Nah, he's eighteen."

    pause
    tony f_suspicious "Ain't ya?"

    anon @ f_worried_left "Ya, tuan."

    tony f_normal @ f_laugh "There, ya see?"

    tony "He's eighteen..."

    tony "... And a good kid too."

    tony @ f_suspicious "Way better than that egghead, Gino."

    maria f_annoyed @ a_crossed "Yeah, like that's a high hurdle to climb..."

    maria "Gino was more useless than the pope's cock!"

    show anon f_surprised_teeth
    show maria f_normal
    tony a_belly f_laugh "Hahahahaah!"

    show anon f_surprised_left
    tony a_point_under "What'd I tell ya?"

    tony "She's a firecracker, my {b}Maria{/b}!"

    show tony f_normal a_idle with dissolve
    show anon f_normal
    pause
    maria "What's ya name then, kid?"

    anon @ -m_talk "Hmm?"

    anon "Oh, it's {b}[firstname]{/b}."

    maria "Is this your first job, {b}[firstname]{/b}?"

    anon f_worried "Ya, Bu."

    maria f_confused "Well, don't look so concerned."

    maria "It's all pretty straight forward."

    maria "I cook, he sells, you deliver."

    maria "Just show up on time, double check your orders, maybe mop the floors every once in a while..."

    anon f_normal "I can do all of that."

    maria f_angry @ a_spoon_point "... And most importantly, keep my husband out of trouble!"

    show anon f_normal_left
    tony @ a_frustrated "What trouble?!"

    pause
    tony @ a_finger_up "I think you're forgettin'..."

    tony @ f_smirk_closed a_heart "I solve problems, I don't make em."

    show anon f_normal
    maria @ a_spoon_point "Yeah well, you have a bad habit of tryin' to solve problems that aren't yours."

    pause
    maria "Don't act like you dunno what I'm talkin' about."

    show anon f_normal_left
    tony f_suspicious @ a_wave "Ahh, lay off it, {b}Maria{/b}!"

    tony "I'm goin' back to the counter."

    hide tony with dissolve
    show anon f_normal
    maria "I mean it, {b}Tony{/b}!!"

    tony "Ya, ya..."

    maria f_shy a_spoon_sides "{i}*Huh*{/i}"

    anon @ -m_talk "..."
    maria a_spoon_hips "So, you have any questions?"

    anon "N-no, I don't think so."

    maria f_normal "Baiklah."

    pause
    maria @ a_spoon_point "If you think of anything, don't be scared to come and ask."

    anon "Ya, Bu."

    maria "Ride safe out there."

    anon "Saya akan."

    hide anon with dissolve
    pause
    show maria f_shy with dissolve:
        flip
        xoffset 500
    maria "Tsk, I hope you know what you're doing, {b}Tony{/b}..."

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
