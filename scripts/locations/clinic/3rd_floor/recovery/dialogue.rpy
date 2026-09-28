label hospital_recovery_poster:
    scene location_hospital_poster
    pause
    $ game.main()
    return

label hospital_recovery_consuela_first:
    scene expression game.timer.image('location_hospital_baby_bed{}')
    show martinez:
        crop (0, 0, 1024, 650)
        flip
        xoffset 300
        zoom .9
    show consuela b_gown_bed f_normal_down
    with fade
    show anon f_worried with dissolve
    anon "{b}Consuela{/b}?"
    martinez f_angry @ f_eyeroll "Oh, great..."
    consuela f_normal "Hola, papi."
    anon "Hey."
    anon "How are you feeling?"
    if M_consuela.pregnancy.baby_gender == "boy":
        consuela "Come meet your son." (show_native="Ven a conocer a tu hijo.")
    elif M_consuela.pregnancy.baby_gender == "twins":
        consuela "Come meet your children." (show_native="Ven a conocer a tus hijos.")
    else:
        consuela "Come meet your daughter." (show_native="Ven a conocer a tu hija.")
    anon f_normal @ f_worried -m_talk "Hmm?"
    if M_consuela.pregnancy.baby_gender == "boy":
        anon "{i}*Gasp*{/i} It's a boy?"
        consuela "Si, boy."
        anon "Wow, you were right!"
    elif M_consuela.pregnancy.baby_gender == "twins":
        anon "{i}*Gasp*{/i} You had twins?"
        consuela "Si, twins."
        anon "Heh, I guess you were wrong about the boobs thing..."
    else:
        anon "{i}*Gasp*{/i} It's a girl?"
        consuela "Si, girl."
    pause
    show consuela f_normal_down
    if M_consuela.pregnancy.baby_gender == "boy":
        anon "He's so beautiful."
        consuela "Si, beautiful!"
        consuela "He has also been silent like a mouse." (show_native="También ha estado callado como un ratón.")
    elif M_consuela.pregnancy.baby_gender == "twins":
        anon "They're so beautiful."
        consuela "Si, beautiful!"
        consuela "They have also kept silent as mice." (show_native="También han guardado silencio como ratones.")
    else:
        anon "She's so beautiful."
        consuela "Si, beautiful!"
        consuela "She has also been silent like a mouse." (show_native="Ella también ha estado en silencio como un ratón.")
    consuela "{b}Camila{/b} cried nonstop when she was born." (show_native="Camila lloró sin parar cuando nació.")
    martinez "Tsk, he can't understand you, {b}Mom{/b}..." (show_native="Tsk, Él no puede entenderte, {b}Mamá{/b}...")
    consuela "So why don't you make yourself useful and translate?" (show_native="Entonces, ¿por qué no haces algo útil y traduces?")
    show martinez with dissolve:
        unflip
        xoffset -250
    if M_consuela.pregnancy.baby_gender == "boy":
        martinez @ f_eyeroll "My mother says that your son is strong and dispassionate."
        martinez "That means he's going to grow up and become a very important person one day."
    elif M_consuela.pregnancy.baby_gender == "twins":
        martinez @ f_eyeroll "My mother says that your children are strong and dispassionate."
        martinez "That means they're going to grow up and become very important people one day."
    else:
        martinez @ f_eyeroll "My mother says that your daughter is strong and dispassionate."
        martinez "That means she's going to grow up and become a very important person one day."
    anon f_surprised "Really?"
    martinez "Yeah."
    martinez "Of course, she also glues bread to our ceiling to keep evil spirits away and stuffs pennies under all our rugs to bring good fortune..."
    anon "Wait, what?"
    martinez "I'm not joking."
    consuela f_angry "What are you saying?" (show_native="¿Que le estas diciendo?")
    martinez @ f_eyeroll "Nothing, {b}Mom{/b}." (show_native="Nada, {b}Mamá{/b}.")
    martinez "Oh, and don't go thinking just because you're fucking my mom that we're gonna become friends now or something..."
    martinez "Because frankly, it's disgusting."
    anon f_worried "I wouldn't-"
    if M_consuela.pregnancy.baby_gender == "boy":
        martinez "I'll love the kid because he's family, but you're a pendejo loser and I want nothing to do with you!"
    elif M_consuela.pregnancy.baby_gender == "twins":
        martinez "I'll love the kids because they're family, but you're a pendejo loser and I want nothing to do with you!"
    else:
        martinez "I'll love the kid because she's family, but you're a pendejo loser and I want nothing to do with you!"
    show anon f_sad_down
    consuela "{b}Camila{/b}!!"
    anon @ -m_talk "..."
    if M_consuela.pregnancy.baby_gender == "boy":
        consuela "He's the father of your little brother!" (show_native="¡Es el padre de tu hermano pequeño!")
    elif M_consuela.pregnancy.baby_gender == "twins":
        consuela "He's the father of your little brother and sister!" (show_native="¡Es el padre de tu hermano y hermana pequeños!")
    else:
        consuela "He's the father of your little sister!" (show_native="¡Es el padre de tu hermana pequeña!")
    consuela "Don't talk to him like that!" (show_native="¡No le hables así!")
    martinez a_crossed @ f_eyeroll "Can I go now?" (show_native="¿Puedo ir ahora?")
    consuela "Tell him you're sorry!" (show_native="¡Dile que lo sientes!")
    show martinez with dissolve:
        flip
        xoffset 300
    martinez "No, {b}Mom{/b}!" (show_native="¡No, {b}Mamá{/b}!")
    consuela "{b}Camila{/b}, he's never going to marry you if you're mean to him all the time." (show_native="{b}Camila{/b}, él nunca se va a casar contigo si eres malo con él todo el tiempo.")
    martinez "Why don't you marry him then?" (show_native="¿Por qué no te casas con él entonces?")
    consuela "Don't be ridiculous!" (show_native="¡No seas ridículo!")
    consuela f_sad "I'm too old for him." (show_native="Soy demasiado viejo para él.")
    consuela "It should be you." (show_native="Deberías ser tú.")
    martinez f_disgusted "Eww, gross!"
    martinez "I'm leaving."
    hide martinez with dissolve
    consuela "{b}Camila{/b}!"
    pause
    consuela "{i}*Sigh*{/i} Sorry, papi."
    anon f_sad "N-no, it's okay."
    anon "Guess she isn't going to warm up to me anytime soon, huh?"
    consuela "No, she do."
    consuela "I teach."
    anon @ -m_talk "..."
    consuela "You see, I teach."
    anon "No, it's alright."
    anon f_normal @ f_laugh "I've got you."
    show anon with dissolve:
        xoffset 300
    if M_consuela.pregnancy.baby_gender == "boy":
        anon "And now this little guy."
    elif M_consuela.pregnancy.baby_gender == "twins":
        anon "And now these little ones."
    else:
        anon "And now this little girl."
    consuela f_normal "You're such a good man, {b}[firstname]{/b}." (show_native="Eres un buen hombre, {b}[firstname]{/b}.")
    anon @ -m_talk "Hmm?"
    consuela "Si, me you have."
    consuela "I do for you."
    anon "Thanks, {b}Consuela{/b}."
    hide anon with dissolve
    return

label hospital_recovery_diane_first:
    scene expression game.timer.image("location_hospital_baby_bed{}")
    show diane a_baby b_gown_bed
    with fade
    show player 5 at left with dissolve
    diane "There he is!"
    pause
    show diane f_teasing_look
    diane "There's your daddy!"
    show diane f_down_front
    show player 3 with dissolve
    player_name "{i}*Gulp*{/i}"
    show diane f_normal
    diane "Come on, handsome."
    if M_diane.pregnancy.baby_gender == "boy":
        diane "I want you to meet your new son."
        show diane f_down_front
        show player 10 with dissolve
        player_name "{b}M-my son{/b}?"
    elif M_diane.pregnancy.baby_gender == "twins":
        diane "I want you to meet your children."
        show diane f_down_front
        show player 10 with dissolve
        player_name "{b}C-children{/b}?"
    else:
        diane "I want you to meet your new daughter."
        show diane f_down_front
        show player 10 with dissolve
        player_name "{b}M-my daughter{/b}?"
    show player 13
    diane @ -m_talk "Mmhmmm."
    show player 426 at center with dissolve
    pause
    show player 14
    player_name "Wow..."
    if M_diane.pregnancy.baby_gender == "boy":
        player_name "... He's so cute!"
    elif M_diane.pregnancy.baby_gender == "twins":
        player_name "... They're so cute!"
    else:
        player_name "... She's so beautiful!"
    show player 426
    show diane f_laugh
    diane "Hehe, yup."
    if M_diane.pregnancy.baby_gender == "boy":
        diane "Just like his daddy."
        show diane f_cheese
        if M_diane.pregnancy.number_of_babies == 1:
            show player 17
            player_name "I can't believe I actually have a son!"
    elif M_diane.pregnancy.baby_gender == "twins":
        diane "Just like their daddy."
        show diane f_cheese
        if M_diane.pregnancy.number_of_babies == 1:
            show player 17
            player_name "I can't believe I actually have kids!"
    else:
        diane "Just like her mommy."
        show diane f_cheese
        if M_diane.pregnancy.number_of_babies == 1:
            show player 17
            player_name "I can't believe I actually have a daughter!"
    if M_diane.pregnancy.number_of_babies == 1:
        show player 18
        show diane f_teasing_look
        diane "I know, me neither."
        show player 426
        diane "I never thought I'd have a child..."
    show diane f_down_front
    pause
    show player 14
    player_name "So when are you all coming home?"
    show player 13
    show diane f_normal
    diane "Oh, they wanna keep us here for a couple more days."
    diane "We'll be home soon though."
    pause
    diane "Make sure my garden doesn't wilt away!"
    show player 14
    player_name "Don't worry, I'll take care of everything."
    show player 13
    diane "Thanks, {b}[firstname]{/b}."
    show diane f_laugh
    diane "Say bye to Daddy!"
    show diane f_cheese
    pause
    show player 429
    show diane f_normal
    if M_diane.pregnancy.baby_gender == "twins":
        player_name "I'll see you soon, little ones."
    else:
        player_name "I'll see you soon, little one."
    hide player with dissolve
    return

label hospital_recovery_eve_first:
    scene expression game.timer.image('location_hospital_baby_bed{}')
    show grace f_happy:
        crop (0, 0, 1024, 650)
        flip
        xoffset 200
        zoom .9
    show eve b_gown_bed
    with fade
    show anon f_worried with dissolve
    anon "Did I miss it?"
    show grace:
        unflip
        xoffset -100
    with dissolve
    eve "{i}*Gasp*{/i} There's your daddy now."
    grace "Hey, {b}[firstname]{/b}."
    grace "No worries, everything went great."
    anon "Oh, thank goodness."
    if M_eve.pregnancy.baby_gender == "boy":
        eve "You wanna meet your son?"
        anon "{b}M-my son{/b}?"
    else:
        eve "You wanna meet your daughter?"
        anon "{b}M-my daughter{/b}?"
    eve "Mmhmmm."
    show anon f_shy_low:
        xoffset 200
    show grace f_happy_down:
        flip
        xoffset 400
    with dissolve
    pause
    anon "Wow..."
    anon "... I can't believe we actually have a kid!"
    eve "I know, right?"
    if M_eve.pregnancy.baby_gender == "boy":
        grace "He's beautiful."
    else:
        grace "She's beautiful."
    grace f_happy "I'm so proud of you, {b}Eve{/b}."
    eve "I couldn't have done it without you, {b}Sis{/b}."
    pause
    anon f_normal "So when are you two coming home?"
    show grace:
        unflip
        xoffset -100
    with dissolve
    grace "Oh, it'll be a few days, at least."
    grace "They like to make sure both {b}the mother{/b} and child are fully recuperated, before sending them home."
    anon "That makes sense."
    pause
    anon "Is there anything I can do for you?"
    eve "No, I'm alright."
    eve f_tired "{i}*Yawn*{/i} Just sleepy..."
    show grace:
        flip
        xoffset 400
    with dissolve
    if M_eve.pregnancy.baby_gender == "boy":
        grace "Why don't you let me take him for a while?"
    else:
        grace "Why don't you let me take her for a while?"
    eve "Y-yeah, okay."
    show grace:
        unflip
        xoffset -100
    with dissolve
    grace "You can head on out if you want, {b}[firstname]{/b}."
    grace "I've got this."
    anon "Thanks, {b}Grace{/b}."
    show grace:
        flip
        xoffset 200
    hide anon
    with dissolve
    return

label hospital_recovery_grace_first:
    scene expression game.timer.image("location_hospital_baby_bed{}")
    show grace b_gown_bed
    with fade
    show anon with dissolve
    grace "Hey, {b}[firstname]{/b}!"
    pause
    grace "You come to check on us?"
    anon "I did."
    if M_grace.pregnancy.baby_gender == "boy":
        grace "Come meet your son."
        anon "{b}M-my son{/b}?"
    elif M_grace.pregnancy.baby_gender == "twins":
        grace "Come meet your children."
        anon "{b}M-my children{/b}?"
    else:
        grace "Come meet your daughter."
        anon "{b}M-my daughter{/b}?"
    grace f_happy_down @ -m_talk "Mmhmmm."
    show anon f_shy_low:
        xoffset 200
    with dissolve
    pause
    anon "Wow..."
    if M_grace.pregnancy.baby_gender == "boy":
        anon "... He's so cute!"
        grace "Isn't he?"
        grace "He has your eyes, I think."
    elif M_grace.pregnancy.baby_gender == "twins":
        anon "... They're so cute!"
        grace "Aren't they?"
        grace "They have your eyes, I think."
    else:
        anon "... She's so cute!"
        grace "Isn't she?"
        grace "She has your eyes, I think."
    anon "Hmm, I dunno..."
    anon "Those might be yours."
    grace @ f_laugh "Hehe!"
    pause
    anon f_normal "So when are you two coming home?"
    grace f_happy "Oh, I dunno."
    grace "They're saying it will be at least a couple days."
    anon "Well, you just make sure you get plenty of rest, okay?"
    grace "Yeah, I will."
    pause
    grace "I wonder if you could do me a favor, {b}[firstname]{/b}?"
    anon "Sure, anything!"
    grace "Peek in on {b}Odette{/b} and make sure she's doing okay while I'm stuck in here, yeah?"
    anon "I can do that."
    grace "Thanks, {b}[firstname]{/b}."
    pause
    if M_grace.pregnancy.baby_gender == "twins":
        anon f_shy_low "I'll see you soon, little ones."
    else:
        anon f_shy_low "I'll see you soon, little one."
    grace @ f_laugh "Hehe!"
    hide anon with dissolve
    return

label hospital_recovery_jenny_first:
    scene expression game.timer.image("location_hospital_baby_bed{}")
    show jenny b_gown_bed_sleep a_bed
    $ player.last_baby_gender = M_jenny.pregnancy.baby_gender
    show debbie b_casual a_baby
    with fade
    show anon with dissolve
    debbie "Hey, sweetie!"
    show anon f_worried
    anon "{b}[deb_name]{/b}?"
    pause
    if M_jenny.pregnancy.first_baby:
        anon f_normal "I-is that?"
        if M_jenny.pregnancy.baby_gender == "twins":
            debbie "This is {b}[jen_name]{/b}'s twins."
        elif M_jenny.pregnancy.baby_gender == "boy":
            debbie "This is {b}[jen_name]{/b}'s little boy."
        else:
            debbie "This is {b}[jen_name]{/b}'s little girl."
        debbie "You wanna say hi?"
        anon "Y-yeah!"
        debbie "Just don't be too loud, okay?"
        debbie "{b}[jen_name]{/b} had a long night."
    else:
        anon "Everything okay?"
        debbie @ f_laugh "Everything is wonderful!"
        show anon f_normal
        debbie "Ten fingers and ten toes!"
        if M_jenny.pregnancy.baby_gender == "twins":
            debbie "This is {b}[jen_name]{/b}'s twins."
            anon "{b}[jen_name]{/b} had twins?!"
        elif M_jenny.pregnancy.baby_gender == "boy":
            anon "{b}[jen_name]{/b} had a little boy?!"
        else:
            anon "{b}[jen_name]{/b} had a little girl?!"
        debbie @ f_laugh "Yup!"
    show anon f_shy_low with dissolve:
        xoffset 200
    pause
    anon "Wow..."
    if M_jenny.pregnancy.baby_gender == "twins":
        debbie "Aren't they just wonderful?"
        anon "They are."
        if M_jenny.pregnancy.first_baby:
            anon "I can't believe {b}[jen_name]{/b} has kids!"
        else:
            anon "I can't believe {b}[jen_name]{/b} had more kids!"
    elif M_jenny.pregnancy.baby_gender == "boy":
        debbie "Isn't he just wonderful?"
        anon "He is."
        if M_jenny.pregnancy.first_baby:
            anon "I can't believe {b}[jen_name]{/b} has a kid!"
        else:
            anon "I can't believe {b}[jen_name]{/b} has another kid!"
    else:
        debbie "Isn't she just wonderful?"
        anon "She is."
        if M_jenny.pregnancy.first_baby:
            anon "I can't believe {b}[jen_name]{/b} has a kid!"
        else:
            anon "I can't believe {b}[jen_name]{/b} has another kid!"
    show anon f_normal
    debbie "I know, me neither."
    debbie f_normal_down @ f_laugh "I'm so excited!"
    pause
    if M_jenny.pregnancy.first_baby:
        if M_jenny.pregnancy.baby_gender == "twins":
            debbie "I'm gonna spoil these little ones rotten..."
        elif M_jenny.pregnancy.baby_gender == "boy":
            debbie "I'm gonna spoil this little guy rotten..."
        else:
            debbie "I'm gonna spoil this little girl rotten..."
        debbie "Aren't I?"
        pause
        debbie @ f_laugh "Yes, I am!"
        pause
        if M_jenny.pregnancy.baby_gender == "twins":
            anon "C-can I hold them?"
        elif M_jenny.pregnancy.baby_gender == "boy":
            anon "C-can I hold him?"
        else:
            anon "C-can I hold her?"
        debbie f_normal "Of course!"
        show debbie a_front
        show anon a_baby f_shy_down
        with dissolve
        debbie "Just be careful, okay?"
        anon "Y-yeah."
        pause
        if M_jenny.pregnancy.baby_gender == "twins":
            debbie "You should have seen {b}[jen_name]{/b} with them."
            debbie "I had to practically pry them out of {b}[jen_name]{/b}'s arms so she could get some sleep!"
        elif M_jenny.pregnancy.baby_gender == "boy":
            debbie "You should have seen {b}[jen_name]{/b} with him."
            debbie "I had to practically pry him out of {b}[jen_name]{/b}'s arms so she could get some sleep!"
        else:
            debbie "You should have seen {b}[jen_name]{/b} with her."
            debbie "I had to practically pry her out of {b}[jen_name]{/b}'s arms so she could get some sleep!"
        anon f_normal "R-really?"
        if M_jenny.pregnancy.baby_gender == "twins":
            debbie "Mmhmm, she just didn't wanna let them go."
        elif M_jenny.pregnancy.baby_gender == "boy":
            debbie "Mmhmm, she just didn't wanna let him go."
        else:
            debbie "Mmhmm, she just didn't wanna let her go."
        anon "I'm surprised..."
        anon "She hasn't been very enthusiastic about this whole thing."
        debbie "Yeah well, you know {b}[jen_name]{/b}..."
        debbie "... She's always been like that."
        debbie "You'd be surprised how much a person's perspective can change the instant they hold their child in their arms for the first time."
        anon f_shy_down "Yeah, I think I know what you mean..."
        pause
        if M_jenny.pregnancy.baby_gender == "twins":
            anon @ f_normal "Heh, they're so adorable!"
            debbie "Aww, they really like you {b}[firstname]{/b}!"
            pause
            anon "Hi there, little ones!"
        elif M_jenny.pregnancy.baby_gender == "boy":
            anon @ f_normal "Heh, he's so adorable!"
            debbie "Aww, he really likes you {b}[firstname]{/b}!"
            pause
            anon "Hi there, little guy!"
        else:
            anon @ f_normal "Heh, she's so adorable!"
            debbie "Aww, she really likes you {b}[firstname]{/b}!"
            pause
            anon "Hi there, little gal!"
        debbie @ f_laugh "Hehehe!"
        pause
        show debbie f_normal_down a_baby
        show anon a_idle
        with dissolve
        if M_jenny.pregnancy.baby_gender == "twins":
            anon "So when can we take them home?"
        elif M_jenny.pregnancy.baby_gender == "boy":
            anon "So when can we take him home?"
        else:
            anon "So when can we take her home?"
        debbie f_normal "Not for a few days, I'm afraid."
        debbie "You can head on back if you'd like, {b}[firstname]{/b}."
        debbie "I'll stay with {b}[jen_name]{/b} and the little one for a while longer."
        anon "O-okay."
    else:
        anon "Are you gonna stay here with them for a while?"
        debbie f_normal_down @ f_normal "Yeah, just a little while longer."
        if M_jenny.pregnancy.baby_gender == "twins":
            debbie "I just can't get enough of these cute little ones!"
        if M_jenny.pregnancy.baby_gender == "boy":
            debbie "I just can't get enough of this cute little guy!"
        else:
            debbie "I just can't get enough of this cute little girl!"
        anon "Heh, okay."
    anon "I'll see you at home later than, {b}[deb_name]{/b}."
    hide anon with dissolve
    return

label hospital_recovery_odette_first:
    scene expression game.timer.image("location_hospital_baby_bed{}")
    show odette b_gown_bed f_smirk
    with fade
    show anon with dissolve
    odette "Hey, big fella!"
    pause
    odette "You come to check on us?"
    anon "{i}*Gulp*{/i} Y-yeah."
    if M_odette.pregnancy.baby_gender == "boy":
        odette "Come meet your son."
        anon "{b}M-my son{/b}?"
    elif M_odette.pregnancy.baby_gender == "twins":
        odette "Come meet your children."
        anon "{b}M-my children{/b}?"
    else:
        odette "Come meet your daughter."
        anon "{b}M-my daughter{/b}?"
    odette f_happy_down @ -m_talk "Mmhmmm."
    show anon f_shy_low:
        xoffset 200
    with dissolve
    pause
    anon "Wow..."
    if M_odette.pregnancy.baby_gender == "boy":
        anon "... He's so cute!"
        odette "Well, of course he is!"
        odette "He takes after me."
    elif M_odette.pregnancy.baby_gender == "twins":
        anon "... They're so cute!"
        odette "Well, of course they are!"
        odette "They take after me."
    else:
        anon "... She's so cute!"
        odette "Well, of course she is!"
        odette "She takes after me."
    anon @ f_laugh "Hehe!"
    pause
    anon f_normal "So when are you all coming home?"
    odette f_normal "Soon, I hope."
    odette "They're talking like they wanna keep us here for a couple more days."
    anon "Well, they probably know best."
    anon "They are doctors after all."
    odette @ f_eyeroll "{i}*Sigh*{/i} Yeah, I guess."
    odette "Peek in on {b}Grace{/b} and make sure she's doing okay while I'm stuck in here, yeah?"
    anon "I can do that."
    odette "Thanks, {b}[firstname]{/b}."
    pause
    show anon f_shy_low
    if M_odette.pregnancy.baby_gender == "twins":
        anon "I'll see you soon, little ones."
    else:
        anon "I'll see you soon, little one."
    odette @ f_laugh "Hehehe!"
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
