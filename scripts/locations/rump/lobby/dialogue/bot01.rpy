label bot01_init_rump_lobby:
    return


label bot01_init_rump_lobby.melonia:
    scene expression background(800, 472, 2.5) as stage
    show thotbot
    show anon f_surprised at flip with dissolve
    thotbot "Greetings, sir." (show_native="Hola señor!")
    anon f_skeptical "What the-"
    anon f_surprised_low "Is that a robot?"
    thotbot "My designation is Rosita."
    show anon f_skeptical
    thotbot "How may I serve you?"
    anon "Rosita?"
    melonia "I see you've met the new maid."
    show melonia f_smirk at flip with dissolve:
        xoffset -100
    anon f_worried "New maid?"
    melonia "It's a big improvement over that hideous one my husband hired, don't you think?"
    anon "Ehh..."
    melonia "And it comes with a wide array of functions and attachments!"
    melonia "Some of them more... Intriguing, than others..."
    anon "Attachments?"
    melonia "Well, I need some way of entertaining myself when your not around, don't I?"
    pause
    melonia "Maybe I'll even let you watch..."
    anon f_surprised "W-watch?"
    melonia @ f_laugh "Hehe!"
    hide melonia with dissolve
    anon f_skeptical @ -m_talk "( Does that mean she's- )"
    show anon f_thinking
    pause
    anon f_surprised_low a_up @ -m_talk "( !!! )"
    thotbot "Are you alright, sir?"
    thotbot "You look like you've seen a ghost."
    anon f_worried a_sides "{i}*Gulp*{/i} N-no, I'm fine."
    pause
    anon @ -m_talk "( Holy crap! )"
    hide anon with dissolve
    return


label bot01_init_rump_lobby.ronald:
    scene expression background(800, 472, 2.5) as stage
    show rump b_dressed_bending:
        xoffset -200
    show thotbot:
        xoffset -200
    with dissolve
    rump "{b}Melonia{/b}, get down here!"
    pause
    melonia "Ugh, what do you want?!"
    rump "I want you to tell me what I'm looking at right now..."
    pause
    show melonia f_annoyed with dissolve
    melonia "How the hell should I-"
    pause
    melonia f_normal @ f_eyeroll "Oh, you found the new maid."
    rump f_suspicious "New maid?!"
    thotbot "Greetings, master."
    thotbot "My designation is, {b}Rosie{/b}."
    rump @ -m_talk "!!!"
    rump "{b}Rosie{/b}?"
    rump "What happened to {b}Consuela{/b}?"
    melonia f_smirk "I let her go, dear."
    rump "What?!"
    rump "You can't just fire my maid, {b}Melonia{/b}!"
    melonia "Why not?"
    melonia "I got you an upgrade, you should be thanking me."
    rump "Thanking you?!"
    thotbot "I am equipped with latest in germ fighting technology."
    melonia "See, germ fighting technology!"
    melonia "It also won't cause a scandal when you inevitably put your pecker inside it."
    rump "You expect me to fuck this thing?"
    melonia "I believe it has a special port, made for just that..."
    rump "It does?"
    show thotbot b_dressed_bend with dissolve
    show rump f_smirk_down
    pause
    show rump b_dressed_bending_robot with dissolve
    pause
    thotbot "Oh my, are we going to fuck now, Master?"
    rump @ -m_talk "Hmm."
    rump "That does feel pretty nice."
    show melonia f_eyeroll
    pause
    show melonia f_normal with None
    show thotbot b_dressed
    show rump b_dressed f_normal
    with dissolve
    rump "I dunno, this just isn't doing it for me."
    melonia f_annoyed "You'd rather fuck that skanky old lady?"
    rump @ f_lips a_finger "You know I like to hear them squeal in Spanish..."
    melonia f_normal "It has language settings."
    rump "It does?"
    melonia "{b}Rosie{/b}, switch to Spanish mode."
    thotbot "Sí, señora."
    show rump f_smirk
    thotbot "My new designation is, {b}Rosita{/b}." (show_native="Mi nueva designación es, {b}Rosita{/b}.")
    rump "{b}Rosita{/b}?"
    thotbot "Sí señor."
    thotbot "Are we going to have sex now?" (show_native="¿Vamos a tener sexo ahora?")
    rump "Mmm, this could work..."
    show thotbot behind rump
    show rump f_smirk_down a_grope_robot
    with dissolve
    thotbot "¡Ay, {b}Señor Rump{/b}!"
    thotbot "Squeeze them harder!" (show_native="¡Exprimirlos más fuerte!")
    rump "Who's a bad little maid?"
    thotbot "I am!" (show_native="¡Soy!")
    pause
    hide thotbot
    show rump a_hold_robot f_normal:
        xoffset -300
    with dissolve
    rump "I'll be in my office..."
    hide rump with dissolve
    melonia @ -m_talk "Mmhmm."
    melonia f_eyeroll a_heart "Try not to hurt yourself, dear."
    hide melonia with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
