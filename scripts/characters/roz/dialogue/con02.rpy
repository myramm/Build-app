label con02_job3_roz:
    scene hospital_desk
    show roz:
        flip
        xoffset -200
    show roz_desk as desk at left
    show consuela b_casual:
        xoffset 100
    show anon:
        flip
        xoffset -100
    with dissolve
    anon "E-excuse me?"
    roz "What do you want, kiddo?"
    anon "My friend here is looking for work..."
    anon "You wouldn't happen to be hiring, would you?"
    roz @ -m_talk "..."
    roz "She doesn't look like a doctor to me..."
    anon @ f_surprised "Doctor?!"
    anon @ f_laugh "No, no, she's not a doctor."
    anon "Umm, we were hoping you might have an opening on your janitorial staff?"
    roz @ -m_talk "Hmm."
    roz "Well, it just so happens that we do."
    anon @ f_surprised "Really?"
    roz "Yeah, one of our night janitors stumbled into an isolation room by accident last week..."
    roz "Got himself a bad case of yellow fever."
    anon f_shock "!!!"
    roz "And I'm not talking about an Asian fetish thing..."
    anon f_worried "O-oh?"
    roz "Does your friend speak English?"
    show anon with dissolve:
        unflip
        xoffset 400
    anon "Ehh..."
    consuela f_annoyed "What is she asking?" (show_native="¿Qué está preguntando ella?")
    show anon with dissolve:
        flip
        xoffset -100
    anon "Not really."
    roz @ -m_talk "..."
    anon "She's a real hard worker though, and she desperately needs the job!"
    roz "Can't help ya."
    anon "Aww, c'mon!"
    roz "We can't just hire anybody off the street that walks in here, you know?"
    roz "How am I supposed to give her direction if she can't speak English?!"
    anon @ f_normal "She's pretty good with simple commands and hand gestures..."
    roz "Pfft, I hope you're joking!"
    pause
    anon f_sad "Have a heart, please!"
    roz "I don't have time for this."
    anon "Look, it's my fault she got fired from her last job and she's got a family to support..."
    roz @ -m_talk "..."
    anon "Please, I'll do anything!"
    show roz f_smirk
    pause
    roz "Anything?"
    anon f_normal "Yes."
    pause
    roz "Spin around for me real quick."
    anon f_worried @ -m_talk "Hmm?"
    roz "Go on, I wanna get a good look at you."
    show anon f_worried_left a_up with dissolve:
        unflip
        xoffset 400
    anon "Like this?"
    pause
    roz "Yeah, just like that."
    consuela "This is getting weird..." (show_native="Esto está raro...")
    roz @ -m_talk "Hmm."
    roz "Alright, I think we can work something out."
    show anon f_worried -a_up with dissolve:
        flip
        xoffset -100
    anon "Yeah?"
    roz "{b}We'll have to head upstairs to the second floor storage room{/b} and grab her a uniform and a badge."
    show anon f_normal a_idle with dissolve:
        unflip
        xoffset 400
    anon "You hear that?"
    consuela "I clean?"
    anon @ f_laugh "Yes, you clean!"
    show consuela f_normal
    anon "Follow her upstairs and get your uniform."
    consuela "Uniform?"
    anon "Yes."
    consuela "Okay, I go."
    roz @ a_stop "Ah, ah, ah!"
    roz "You follow, kiddo."
    show consuela f_annoyed
    show anon f_worried with dissolve:
        flip
        xoffset -100
    anon "Huh?"
    roz "She stays here."
    anon @ -m_talk "..."
    roz "C'mon."
    hide roz with dissolve
    consuela "I go?"
    show anon f_worried with dissolve:
        unflip
        xoffset 400
    anon "Uhh, n-no..."
    anon @ a_point_self "I go."
    anon "You stay."
    consuela "I stay?"
    anon "Y-yeah."
    anon f_thinking @ -m_talk "( I wonder what she wants me to do? )"
    roz "You coming or what?"
    anon f_surprised "!!!"
    show consuela f_sad a_cross with dissolve
    anon f_worried_left "Y-yes, ma'am."
    anon f_normal "I'll be right back, okay?"
    consuela "O-okay."
    hide anon with dissolve
    consuela f_sad_down @ -m_talk "..."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
