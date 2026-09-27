label hospital_recovery_maria_first:
    $ player.last_baby_gender = M_maria.pregnancy.baby_gender
    scene expression game.timer.image('location_hospital_baby_bed{}')
    show tony b_casual:
        crop (0, 0, 1024, 650)
        flip
        xoffset 200
        zoom .9
    show maria b_gown_bed f_normal_down
    with fade
    show anon with dissolve
    anon "Did I miss it?"

    show tony with dissolve:
        unflip
        xoffset -100
    tony @ a_frustrated f_laugh "Heh, \"did I miss it\" he says..."

    tony @ f_smirk_wink a_point "Let's just say that you missed the fuckin' fireworks show..."

    if M_maria.pregnancy.baby_gender == 'boy':
        tony "... But you're right on time to meet your godson!"

    elif M_maria.pregnancy.baby_gender == 'girl':
        tony "... But you're right on time to meet your goddaughter!"

    else:
        tony "... But you're right on time to meet your godchildren!"

    maria f_annoyed "Tsk, {b}Tony{/b}! Watch your fuckin' mouth!"

    if M_maria.pregnancy.baby_gender == 'twins':
        maria "I don't want you cursin' in front of our children!"

    else:
        maria "I don't want you cursin' in front of our child!"

    show maria f_normal_down
    show tony with dissolve:
        flip
        xoffset 200
    tony "Oh, you're right, darlin'!"

    tony "Saya minta maaf."

    if M_maria.pregnancy.baby_gender == 'boy':
        anon "D-did you say godson?"

    elif M_maria.pregnancy.baby_gender == 'girl':
        anon "D-did you say goddaughter?"

    else:
        anon "D-did you say godchildren?"

    show tony with dissolve:
        unflip
        xoffset -100
    maria @ f_normal -m_talk "Mhmm!"

    tony "That's right, champ."

    if M_maria.pregnancy.baby_gender == 'boy':
        tony "It's a baby boy, just like I wanted!"

    elif M_maria.pregnancy.baby_gender == 'girl':
        tony "It's a baby girl!"

    else:
        tony "{b}Maria{/b} had twins!"

    anon "That's wonderful, you guys!"

    show tony with dissolve:
        flip
        xoffset 200
    if M_maria.pregnancy.baby_gender == 'boy':
        tony "I told ya the visualization thing would work..."

        maria @ f_eyeroll "Ya, terserah."

        maria "You woulda been just as happy with a girl."

        tony @ f_laugh a_belly "Heh, that's true, darlin'!"

    elif M_maria.pregnancy.baby_gender == 'girl':
        maria "I told ya the visualization thing wouldn't work..."

        tony @ f_eyeroll "Ya, terserah."

        tony "I'm just as happy with a girl."

        maria "Heh, better be!"

    else:
        maria "I never, in my wildest dreams, imagined we'd get so lucky..."

        tony f_smirk @ a_fists "Yeah, it's like we hit the lottery!"

        tony "A boy and a girl!"

    tony "I'd be happy with anything, so long as it comes outta you."

    pause
    if M_maria.pregnancy.baby_gender == 'twins':
        maria "I can't believe I'm actually holding my children right now..."

    else:
        maria "I can't believe I'm actually holding my child right now..."

    maria f_normal "We aren't ever gonna be able to repay you for this, {b}[firstname]{/b}."

    anon "Nah, don't mention it."

    anon "I was happy to help."

    show maria f_normal_down
    if M_maria.pregnancy.baby_gender == 'boy':
        maria "He's just so beautiful!"

        tony f_smirk "Yeah, he is."

        tony "He's got his mama's eyes."

        maria @ f_sexy "And his father's chin."

    elif M_maria.pregnancy.baby_gender == 'girl':
        maria "She's just so beautiful!"

        tony f_smirk "Ya, benar."

        tony "She's got her mama's eyes."

        maria @ f_sexy "And her father's nose."

    else:
        maria "They're just so beautiful!"

        tony f_smirk "Yeah, they are."

        tony "They got their mama's eyes."

        maria @ f_sexy "And their father's nose."

    anon f_shy a_behind_head @ f_surprised "!!!"
    show tony with dissolve:
        unflip
        xoffset -100
    if M_maria.pregnancy.baby_gender == 'boy':
        tony "Yeah, he takes after you quite a bit, champ."

        tony "I imagine he'll grow up to be quite the lady-killer, eh?!"

    elif M_maria.pregnancy.baby_gender == 'girl':
        tony "Yeah, she takes after you quite a bit, champ."

        tony "I imagine she'll grow up to be quite the ornery one, eh?!"

    else:
        tony "Yeah, they take after you quite a bit, champ."

        tony "I imagine they'll grow up to be quite ornery, eh?!"

    anon "Heh, I dunno about that..."

    if M_maria.pregnancy.baby_gender == 'boy':
        maria f_normal "Do you wanna hold him?"

    elif M_maria.pregnancy.baby_gender == 'girl':
        maria f_normal "Do you wanna hold her?"

    else:
        maria f_normal "Do you wanna hold 'em?"

    anon a_idle "Benar-benar?"

    tony @ f_laugh a_frustrated "Well, sure!"

    if M_maria.pregnancy.baby_gender == 'boy':
        tony "You're his godfather after all, ain't ya?!"

    elif M_maria.pregnancy.baby_gender == 'girl':
        tony "You're her godfather after all, ain't ya?!"

    else:
        tony "You're their godfather after all, ain't ya?!"

    anon "Y-ya, oke."

    show maria a_down
    show anon a_baby f_shy_down:
        xoffset 100
    with dissolve
    pause
    anon "Wah..."

    pause
    if M_maria.pregnancy.baby_gender == 'boy':
        anon @ f_laugh "He's so cute and tiny!"

    elif M_maria.pregnancy.baby_gender == 'girl':
        anon @ f_laugh "She's so cute and tiny!"

    else:
        anon @ f_laugh "They're so cute and tiny!"

    if M_maria.pregnancy.baby_gender == 'twins':
        anon "Hi, little ones..."

    else:
        anon "Hi, little one..."

    anon "I'm your godfather, {b}[firstname]{/b}."

    pause
    anon f_normal "Saya sangat senang untuk kalian!"

    show anon a_idle
    show maria a_idle f_normal_down
    with dissolve
    tony "Thanks, champ."

    pause
    anon "So, how long are you gonna be here?"

    tony "Ahh, a few days..."

    tony "It shouldn't be problem."

    anon "Apakah kamu memerlukan aku untuk membelikanmu sesuatu?"

    show tony f_normal with dissolve:
        flip
        xoffset 200
    tony "You need anything, darlin'?"

    maria f_normal "No, I've got everything I need, right here."

    tony "Heh, ya, benar!"

    show tony with dissolve:
        unflip
        xoffset -100
    tony "We're good, champ."

    tony "Just make sure you take care of yourself, yeah?"

    tony "We'll be deliverin' pizza again before ya know it!"

    anon "Ya baiklah."

    anon "See ya, {b}Tony{/b}."

    anon "Bye, {b}Maria{/b}."

    tony @ a_point f_smirk_wink "Nanti, juara."

    maria "See you soon, {b}[firstname]{/b}."

    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
