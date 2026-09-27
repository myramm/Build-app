label cafeteria_eve_cafeteria_troubles:
    scene expression player.location.background_blur
    show annie a_note_write f_annoyed_down at flip
    show annie:
        xoffset 150
    show eve f_angry a_chips:
        xoffset -100
    show kevin b_apron f_sorry:
        xoffset 100
    with fade
    eve "You can't be serious!"

    annie "I warned you both about this last time!"

    annie "Now I'll have to give you both detention."

    kevin "Aww, c'mon bro..."

    show annie a_note with dissolve
    annie f_annoyed "Do I look like a \"bro\" to you?!"

    show anon f_skeptical with dissolve:
        xoffset -100
    kevin "{i}*Huh*{/i} Tidak."

    pause
    show annie a_note_write f_annoyed_down with dissolve
    anon "Apa yang terjadi?"

    annie "I just caught {b}Kevin{/b} giving this one cafeteria food for free and I'm writing them up."

    eve "This is bullshit, {b}Annie{/b}!"

    eve "It's one little bag of chips..."

    show annie a_note with dissolve
    annie f_annoyed "Oh, I'm sorry."

    annie f_eyeroll "I forgot that stealing is okay, so long as it's just {i}something little{/i}!"

    show annie a_note_write f_annoyed_down with dissolve
    eve "I'll pay for it tomorrow, I just-"

    show eve f_sad_down
    pause
    eve "My sister forgot to put money in my lunch account this week, okay?"

    show anon f_worried
    annie "Not my problem!"

    anon "C'mon {b}Annie{/b}, can't you just let this slide?"

    hide annie
    show annie f_annoyed a_hips:
        xoffset -325
    with dissolve
    annie "Keep talking {b}[firstname]{/b} and I'll write you up as well!"

    anon f_shock "I-itu bukan-"

    eve f_surprised "APA?!"

    show anon f_surprised_teeth with None
    hide annie
    show annie a_hips f_angry at flip
    show annie:
        xoffset 200
    with dissolve
    eve f_angry "{b}[firstname]{/b} didn't even do anything!"

    annie "He's arguing with me!"

    show anon f_worried
    eve "So what?!"

    eve "You can't write him up for that!"

    show annie zorder 0
    show kevin zorder 2
    show eve a_point zorder 1 with dissolve
    eve "You're just a hall monitor, {b}Annie{/b}!"

    show eve a_hip_angry with dissolve
    eve "You don't have any real authority..."

    show kevin f_skeptical with None
    show annie f_angry:
        xoffset 225
    with dissolve
    annie "Ah, benarkah?"

    annie "Well, why don't I go get {b}Mrs. Smith{/b} right now, and we'll see what she has to say about my authority?!"

    show eve:
        xoffset -125
    with dissolve
    eve "Do it then, you little brown noser!"

    eve "I'm not scared of you or that tyrannical bit-"

    show eve:
        xoffset 0
    show annie:
        xoffset 150
    show kevin:
        xoffset -200
    with dissolve
    show kevin a_up with dissolve
    kevin f_sorry "Whoa, whoa, whoa!!"

    show kevin a_sides with dissolve
    kevin "She doesn't mean that..."

    eve "Yes, I do!!"

    show eve zorder 3
    show kevin:
        flip
        xoffset 400
    with dissolve
    kevin f_sorry "Bro, you need to chill out... Are you trying to get expelled or something?!"

    show eve a_rossed with dissolve
    eve "Hmph!"

    hide kevin
    show kevin b_apron f_sorry:
        xoffset -200
    with dissolve
    kevin "We're sorry about the potato chips."

    kevin "I-it won't happen again."

    show annie a_note_write zorder 3 with dissolve
    annie f_annoyed_down "Eh ya..."

    annie "See that it doesn't!"

    pause
    show annie a_point2 with dissolve
    annie f_annoyed "... And you'd better watch your mouth!"

    show annie a_note with dissolve
    annie "I know you think you're a special little snowflake or something; but in this school, everyone follows the rules!"

    pause
    hide annie
    show annie f_angry a_hips:
        xoffset -400
    with dissolve
    annie "Move it!" with hpunch
    show kevin f_surprised
    show anon f_surprised_teeth
    hide annie with dissolve
    anon "!!!"
    show kevin f_normal
    pause
    anon f_worried "Wow, that was intense..."

    eve "People like her are the worst!"

    eve "They get a little bit of power and then use it to make everyone else miserable!"

    show anon f_normal
    kevin @ f_laugh "True that, haha!"

    pause
    eve "Sorry I got you in trouble, {b}Kevin{/b}..."

    show kevin:
        flip
        xoffset 400
    with dissolve
    kevin "Nah, it's cool."

    kevin @ f_laugh "I'm already on {b}Mrs. Smith{/b}'s shit list."

    eve @ f_eyeroll "I dunno how that woman keeps her job..."

    pause
    kevin f_sorry "What's up with your sister forgetting your money again?"

    eve f_sad_down "It's not her fault, she's got a lot on her plate at the moment."

    kevin "Okay, but what are you going to do for food?"

    eve "Entahlah..."

    anon "She can share my lunch!"

    show anon f_grin with None
    show kevin b_apron f_normal:
        unflip
        xoffset -200
    with dissolve
    eve f_surprised "B-benarkah?"

    anon f_normal "Yeah, I'm not all that hungry anyways..."

    eve f_nervous "Apa kamu yakin?"

    anon "Y-yeah, it's no problem."

    show anon f_grin
    show eve f_happy
    kevin @ f_laugh "Heh, {b}[firstname]{/b} to the rescue!"

    show anon f_normal
    eve "For real, I'm starving!"

    anon "C'mon, you can pick out whatever you want."

    show eve f_nervous a_crossed with dissolve
    eve "Wow, you're so nice, {b}[firstname]{/b}!"

    kevin @ f_laugh "Langsung saja, kawan!"

    pause
    kevin "I should probably get back to the kitchen."

    eve "See ya, {b}Kevin{/b}."

    show anon a_wave
    show eve a_wave
    with dissolve
    kevin "Later, guys."

    hide kevin
    show anon a_idle
    hide eve
    show eve f_nervous a_crossed
    with dissolve
    eve f_nervous_down "I'll just eat a little bit-"

    anon "Don't be silly, get as much as you want."

    show eve f_happy
    pause
    eve "Terima kasih, {b}[firstname]{/b}."

    hide anon
    hide eve
    with dissolve
    return

label cafeteria_diane_delivery_3_drop_off_goods:
    scene cafeteria_b
    show player 164 at left with dissolve
    show old_annie 1 at right with dissolve
    player_name "All done!"

    show old_annie 9
    show player 163
    annie "..."
    show old_annie 3
    annie "{b}Mrs. Smith{/b} took the invoice?"

    show old_annie 1
    show player 164
    player_name "Yeah, she was... Kind of... Busy. But she said I should give it to you."

    show old_annie 5
    show player 163
    annie "begitu..."

    show old_annie 15
    show player 1
    annie "I'll take these from you, then."

    show old_annie 14
    show player 17
    player_name "Thanks, {b}Annie{/b}!"

    hide player
    hide old_annie
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
