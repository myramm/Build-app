label con01_give_rump_lobby:
    scene expression background(800, 472, 2.5) as stage with None
    show anon a_backpack f_looking_down with dissolve:
        flip
        xoffset 100
    pause
    show anon a_backpack_robot f_normal_low with dissolve
    pause .5
    show anon a_idle f_normal
    show thotbot behind anon at flip
    with dissolve
    pause
    show melonia f_surprised at flip with dissolve
    melonia "What in the world is that?"
    anon @ f_laugh "Your new maid."
    melonia f_annoyed "You can't be serious..."
    anon f_normal @ f_skeptical "Why not?"
    anon "This thing will clean your house for free and won't even bat an eye when your husband harasses it."
    melonia "It's a robot, though."
    anon @ f_brag_closed a_wave "A robot with realistic genitalia."
    pause
    melonia f_happy a_heart @ f_laugh "Pfft, HAHAHAHAHAAAH!!!"
    anon f_worried @ -m_talk "..."
    anon "You don't like it?"
    melonia "No, it's perfect!"
    melonia "I'm just picturing my idiot husband sticking his cock in this thing!"
    melonia @ f_laugh "Hahahaah!"
    anon "So you'll let me take {b}Consuela{/b} out of here?"
    melonia a_idle "Sure."
    show melonia f_yell with dissolve:
        unflip
        xoffset -250
    melonia "Hey, bitch!"
    show anon f_surprised
    melonia "Get your fat ass in here!"
    show melonia f_happy
    anon f_skeptical @ -m_talk "..."
    pause
    consuela "Coming, {b}Missus Rump{/b}!"
    show anon f_worried
    pause
    show consuela with dissolve:
        flip
        xoffset -100
    consuela "You call?"
    melonia "I did and I've gotta say, it's just an absolute pleasure to tell you this..."
    melonia f_happy @ f_yell a_fired "You're fired!"
    consuela f_surprised "¡¿Qué?!"
    show melonia f_laugh with dissolve:
        flip
        xoffset 230
    melonia "I've always wanted to say that..."
    consuela f_sad a_beg "No, no, please... {b}Missus Rump{/b}!"
    show melonia f_annoyed with dissolve:
        unflip
        xoffset -340
    consuela "I clean."
    consuela "No fire."
    consuela "I clean good!"
    melonia "Eugh, don't start begging..."
    consuela "Please, no fire!"
    show consuela b_lift with dissolve
    consuela "I clean naked!"
    show consuela b_lift_back3 with dissolve
    anon f_surprised "!!!"
    show consuela b_undies a_idle with dissolve
    consuela "See, I do."
    melonia "Put those disgusting things away!"
    melonia "Nobody wants to see that!"
    consuela a_uniform_hide "Please, {b}Missus Rump{/b}..."
    melonia "Enough."
    melonia "You're his problem now."
    consuela f_annoyed "¿Qué?"
    melonia "YOU. GO. WITH. HIM!"
    consuela f_sad @ a_uniform_point "I go?"
    melonia "{i}*Sigh*{/i} YES!!"
    melonia @ f_eyeroll "Jesus, I'm done."
    hide melonia
    show consuela:
        unflip
        xoffset -660
    with dissolve
    melonia "Get her out of my house!"
    anon "Y-yeah, okay."
    show consuela with dissolve:
        flip
        xoffset -100
    consuela "What am I supposed to do now?" (show_native="¿Qué se supone que debo hacer ahora?")
    anon "C'mon, {b}Consuela{/b}."
    anon "Let's get you out of here."
    consuela "Okay, {b}Mister [firstname]{/b}..."
    hide consuela
    show anon:
        unflip
        xoffset 600
    with dissolve
    anon @ -m_talk "( Wow, I can't believe this plan worked. )"
    anon @ -m_talk "( I wonder how the mayor will react when he sees his new maid? )"
    anon @ -m_talk "( No time to think about that now, {b}I should make sure Consuela{/b} is going to be alright. )"
    hide anon with dissolve

    label con01_give_rump_lobby.resume:
    scene expression background(776, 432, 2.1, l=L_rump_front) as stage
    show consuela f_sad b_undies a_uniform_hide:
        flip
        xoffset 450
    with fade
    show anon f_worried with dissolve:
        xoffset -50
    anon "You know, you really shouldn't be walking around half-naked out here..."
    show consuela with dissolve:
        unflip
        xoffset -100
    consuela @ -m_talk "Hmm?"
    anon @ a_point "Your clothes."
    show consuela f_sad_down
    pause
    consuela "Oh, si."
    show consuela b_lift_back3 with dissolve
    pause
    show consuela b_lift_back with dissolve
    pause
    show consuela f_sad b_dressed a_idle with dissolve
    ricky "Hey, wait up!"
    show anon:
        flip
        xoffset 120
    with dissolve
    anon "{b}Ricky{/b}?"
    show ricky f_sad at flip with dissolve
    ricky "What's going on?"
    consuela "Oh Ricky, they fired me!" (show_native="¡Ay {b}Ricky{/b}, me despidieron!")
    ricky "They fired you?!"
    ricky "What happened?"

    if M_consuela.is_state(S_con01_give):
        anon "{b}Melonia{/b} has a replacement maid."
        ricky "Oh shit, for real?"
        anon @ f_normal "Yeah!"
        anon "Well, sort of..."
        anon "It's a robot, that cleans."
        ricky f_confused "A robot?"
    else:
        anon "I kinda got {b}Mayor Rump{/b} arrested..."
        ricky "Oh shit, for real?"
        anon @ f_normal "Yeah."
        anon "And {b}Melonia{/b} has wanted {b}Consuela{/b} gone for a while..."

    consuela "What am I supposed to do now?" (show_native="¿Qué se supone que debo hacer ahora?")
    consuela "How will I feed my family?" (show_native="¿Cómo voy a alimentar a mi familia?")
    ricky "You work for him now, right?" (show_native="Trabajas para él ahora, ¿verdad?")
    consuela f_surprised "I do?" (show_native="¿Hago?")
    show ricky behind consuela
    show consuela with dissolve:
        flip
        xoffset 300
    consuela f_normal "I clean, for you?"
    anon f_surprised "Uh?"
    show anon b_empty f_surprised_down
    show consuela b_hug_mc:
        xoffset 120
    show ricky f_normal
    with dissolve
    consuela "Oh {b}Mister [firstname]{/b}, this is wonderful news!" (show_native="¡Oh {b}Mister [firstname]{/b}, esta es una noticia maravillosa!")
    pause
    show anon f_shy b_dressed
    show consuela b_dressed:
        xoffset 300
    with dissolve
    consuela "How much will you pay?" (show_native="¿Cuánto pagarás?")
    consuela "Will I get any benefits?" (show_native="¿Recibiré algún beneficio?")
    ricky "She wants to know how much you plan to pay her?"
    anon f_worried "P-pay?"
    anon "Umm, I can't really afford to pay her right now..."
    ricky f_sad "He says he can't pay..." (show_native="Dice que no puede pagar...")
    consuela f_sad "¡¿Qué?!"
    consuela f_angry "I'm going to kill him!" (show_native="¡Lo voy a matar!")
    show consuela a_smack
    show anon b_dressed_blocking
    with dissolve
    show ricky f_surprised
    anon "Whoa!"
    show anon b_dressed a_behind_head
    show consuela a_idle
    with dissolve
    consuela "How am I going to feed my daughter, you idiot?!" (show_native="¿Cómo voy a alimentar a mi hija, idiota?")
    anon "Cut it out!"
    show ricky a_hold_consuela f_sad:
        xoffset 25
    show consuela b_empty:
        offset (330, 10)
    with dissolve
    ricky "{b}Consuela{/b}, calm down!" (show_native="{b}Consuela{/b}, cálmate!")
    consuela "Moron!" (show_native="¡Pendejo!")
    anon "I'm sorry, I didn't know!"
    ricky "I warned you this would happen..."
    ricky "What is she supposed to do for money now?"
    ricky "She has two kids at home, how will she feed them?"
    anon f_surprised "She has two kids?!"
    ricky "A daughter and a niece."
    anon f_sad_down "Ehh, I'll figure it out."
    ricky "How?"
    anon f_worried "I dunno, I'll find her a job."
    ricky @ -m_talk "..."
    show ricky a_idle:
        xoffset 0
    show consuela b_dressed f_annoyed:
        unflip
        offset (-300, 0)
    with dissolve
    consuela "What is the idiot saying?" (show_native="¿Qué dice el idiota?")
    ricky "He says, he will find you a job." (show_native="Dice que te encontrará un trabajo.")
    consuela f_unsure "Truly?" (show_native="¿De verdad?")
    show consuela f_annoyed with dissolve:
        flip
        xoffset 300
    ricky "Are you being serious, {b}[firstname]{/b}?"
    ricky "Because this is no joking matter."
    ricky "You have put her family at risk by doing all this..."
    anon "I will find her a good job, I promise."
    show consuela with dissolve:
        unflip
        xoffset -300
    ricky "He says yes." (show_native="El dice que si.")
    ricky "A good job." (show_native="Un buen trabajo.")
    show consuela with dissolve:
        flip
        xoffset 300
    consuela "When?" (show_native="¿Cuándo?")
    ricky "When?"
    anon "Uhh, very soon."
    ricky "Muy pronto."
    consuela "Where?" (show_native="¿Dónde?")
    ricky "Where?"
    anon "I don't know."
    show consuela f_annoyed
    ricky "If I tell her this, she's going to start hitting you again..."
    anon f_surprised "N-no, no!"
    show anon f_thinking a_thinking with dissolve
    pause
    anon f_normal a_idle "Umm... Oh, I've got it!"
    anon "She's Catholic, right?"
    ricky f_confused "What makes you think that?"
    anon @ f_skeptical "She's wearing a cross..."
    pause
    show consuela with dissolve:
        unflip
        xoffset -300
    ricky f_sad "Are you Catholic?" (show_native="¿Eres Catolico?")
    show consuela a_cross f_sad
    with dissolve
    consuela "I'm Catholic, yes." (show_native="Católica si.")
    anon "I'll bet you the church could use someone to clean!"
    ricky "He thinks you should work at the church." (show_native="Él piensa que deberías trabajar en la iglesia.")
    consuela @ f_surprised "Do I look like a nun?" (show_native="¿Me veo como una monja?")
    ricky "It wouldn't hurt to try, right?" (show_native="No estaría de más intentarlo, ¿verdad?")
    consuela f_sad_down "I suppose not." (show_native="{i}*Sigh*{/i} Supongo que no.")
    ricky "Okay, she'll do it."
    consuela f_sad "I'll have to beg at the mall for work again..." (show_native="Tendré que rogar en el centro comercial por trabajo otra vez...")
    hide consuela
    show anon f_worried:
        unflip
        xoffset 620
    with dissolve
    pause
    show anon with dissolve:
        flip
        xoffset 100
    anon f_worried "Where is she going?"
    ricky "I'm not sure."
    ricky "Something about begging for work at the mall."
    anon "She doesn't need to do that."
    ricky "Look, {b}go and ask about that job at the church{/b} and if you get good news, you'll probably find her there {b}during the week{/b}."
    anon "She's just gonna stand around at the mall all day, begging for work?"
    ricky "Don't act so surprised... It's not that uncommon for our people."
    ricky "We aren't the type to sit on our hands and lament."
    anon "Y-yeah, okay."
    hide ricky with dissolve
    anon @ -m_talk "( Man, I feel really bad about this whole thing now... )"
    anon @ -m_talk "( {b}I should head to the church and ask the priest about a job for Consuela{/b}. )"
    hide anon with dissolve
    return


label con01_skip_rump_lobby:
    scene expression background(800, 472, 2.5) as stage
    show consuela f_sad at flip
    show anon at flip with dissolve
    consuela "Oh, {b}mister [firstname]{/b}!"
    anon @ -m_talk "Hmm?"
    anon "Oh, hello {b}Consuela{/b}."
    consuela "Ehh... Where {b}mister Rump{/b}?"
    consuela "I no see him."
    anon "You didn't hear?"
    anon "{b}Mr. Rump{/b} was arrested."
    consuela f_surprised a_shock "{i}*Gasp*{/i} Arrested?!"
    anon "Yeah, he's probably in prison by now."
    consuela "Really?" (show_native="¿En serio?")
    consuela f_sad a_cross "What will happen to me?" (show_native="¿Lo que me va a pasar?")
    anon f_worried @ -m_talk "Hmm?"
    consuela a_beg "Ehh, I stay?"
    anon "Yeah, of course."
    show consuela b_hug_mc:
        xoffset 50
    show anon b_empty f_surprised:
        xoffset 50
    anon "!!!" with hpunch
    consuela "Oh, gracias {b}mister [firstname]{/b}!"
    anon "Whoa, that's uhh..."
    consuela "You're a good man!" (show_native="¡Eres un buen hombre!")
    anon "You're welcome."
    pause
    melonia "What in the hell do you think you're doing?"
    show melonia f_annoyed:
        flip
        xoffset -70
    show anon b_dressed f_worried
    show consuela b_dressed a_idle f_sad behind anon:
        unflip
        xoffset -200
    with dissolve
    consuela @ -m_talk "Hmm?"
    melonia "{b}[firstname]{/b} is mine and I don't want your disgusting hands on him!"
    consuela "Sorry, {b}Missus Rump{/b}... I-"
    melonia "In fact, I don't want you near him at all!"
    melonia f_happy @ f_yell a_fired "You're fired!"
    consuela f_surprised "¡¿Qué?!"
    anon "Wait a second, you don't have to-"
    show melonia f_laugh
    melonia "I've always wanted to say that..."
    consuela f_sad a_beg "No, no, please... {b}Missus Rump{/b}!"
    show melonia f_annoyed behind consuela
    consuela "I clean."
    consuela "No fire."
    consuela "I clean good!"
    melonia "Eugh, don't start begging..."
    consuela "Please, no fire!"
    show consuela b_lift with dissolve
    consuela "I clean naked!"
    show consuela b_lift_back3 with dissolve
    anon f_surprised_low "!!!"
    show consuela b_undies a_idle with dissolve
    consuela "See, I do."
    melonia "Put those disgusting things away!"
    melonia "Nobody wants to see that!"
    show anon f_flirt_low
    consuela a_uniform_hide "Please, {b}Missus Rump{/b}..."
    melonia "Enough."
    melonia "I want you out of here!"
    consuela f_annoyed "¿Qué?"
    show anon f_surprised
    melonia "YOU. GO. NOW."
    consuela f_sad "I go?"
    melonia "{i}*Sigh*{/i} YES!!"
    melonia @ f_eyeroll "Jesus, I'm done."
    hide melonia with dissolve
    melonia "Get her out of my house!"
    pause
    show consuela:
        flip
        xoffset 300
    show anon f_worried
    with dissolve
    consuela "What am I supposed to do now?" (show_native="¿Qué se supone que debo hacer ahora?")
    anon "I'm sorry, {b}Consuela{/b}."
    anon "We'd better get you out of here before she calls security..."
    consuela "Okay, {b}Mister [firstname]{/b}..."
    hide consuela
    show anon:
        unflip
        xoffset 550
    with dissolve
    anon @ -m_talk "( Aww, man... That's not how I wanted this to go down. )"
    anon @ -m_talk "( Poor, {b}Consuela{/b}. )"
    pause
    anon @ -m_talk "( I need to make sure she's going to be alright. )"
    hide anon with dissolve
    jump con01_give_rump_lobby.resume
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
