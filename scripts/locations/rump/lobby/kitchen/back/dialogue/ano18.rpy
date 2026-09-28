label ano18_yard_rump_back:
    scene expression background(672, 368, 4., l=L_rump_back)
    show ricky b_speedo a_shovel:
        flip
        xoffset -100
    show melonia b_swimsuit f_pouting:
        xoffset 100
    melonia "Aww, just one more dance?"
    ricky f_smirk @ a_thumb "No, I should really get back to the hedges."
    melonia "You know, the hedges aren't paying your bills, {b}Ricardo{/b}."
    ricky "Heh, your husband is the one who pays my bills, señora."
    ricky "I'm not so sure he would like these dancing sessions."
    melonia @ f_eyeroll "My husband's wants do not concern me..."
    melonia f_annoyed "... And they certainly shouldn't concern you."
    show ricky b_pull_pants with dissolve
    ricky "All the same, I have much work to do."
    ricky b_dressed a_idle @ a_pull_up "If I don't get back to it, I'll be here all night."
    melonia f_smirk "Or you could skip the yardwork all together..."
    melonia "There's a few things I could use your help with inside the house."
    ricky f_confused "In the house?"
    melonia "Specifically, in my bedroom..."
    ricky "Ehh, you know I can't be doing this, señora."
    ricky "Your husband would cut my balls off and ship me back to El Salvador!"
    melonia f_annoyed "Ugh, fine!"
    melonia "Whatever, do your stupid yardwork..."
    show consuela:
        xoffset -300
    with dissolve
    melonia "See if I care."
    consuela "{b}Ricky{/b}, {b}Mister Rump{/b} wants you to wash the-" (show_native="{b}Ricky{/b}, {b}El señor Rump{/b} quiere que laves el-")
    show consuela:
        flip
        xoffset 200
    with dissolve
    pause
    melonia "Out of my way, bitch!"
    show ricky m_talk f_sad
    show melonia b_swimsuit_push
    hide consuela
    consuela "!!!" with hpunch

    scene location_rump_backyard_cutscene01
    show text _ ("I was starting to feel really sorry for this maid.") as caption
    with fade
    pause
    hide caption with dissolve
    show text _ ("Even the mayor's wife was cruel to her.") as caption with dissolve
    pause
    hide caption with dissolve
    show text _ ("It just wasn't right, nobody deserved to be treated that way.") as caption with dissolve
    pause

    scene expression background(600, 368, 4., l=L_rump_back)
    show ricky f_sad
    show consuela f_wincing b_lift:
        flip
    with fade
    ricky "Are you alright, {b}Consuela{/b}?" (show_native="¿Estás bien, {b}Consuela{/b}?")
    consuela f_sad_down "{i}*Sigh*{/i} Si."
    show consuela b_dressed f_angry with dissolve
    consuela "I hate working for these terrible people!" (show_native="¡Odio trabajar para estas personas terribles!")
    ricky "I know..." (show_native="Lo sé...")
    ricky "... But there is nothing we can do." (show_native="... Pero no tenemos otra opción.")
    anon "Excuse me?"
    consuela f_sad @ -m_talk "Hmm?"
    show anon f_worried behind consuela:
        xoffset -100
    show consuela:
        unflip
        xoffset -300
    with dissolve
    consuela "Who is this?" (show_native="¿Quien es este?")
    ricky f_smirk "Dayum, I don't know, but he's cuuuuute!"
    pause
    anon f_skeptical "Whaa-"
    ricky "I think I'd better put my gloves on, you're too hot to handle!"
    anon @ -m_talk "..."
    ricky "What's your name, baby?"
    anon f_worried @ a_point_self "Uhh, are you talking to me?"
    ricky "I'm {b}Ricky{/b}."
    anon @ a_wave "{b}[firstname]{/b}."
    ricky f_confused "{b}[firstname]{/b}?"
    consuela "What kind of a name is that?" (show_native="¿Qué tipo de nombre es ése?")
    ricky f_smirk "Are you sure your name isn't Coca-Cola?"
    ricky "Because you are so-da-licious!"
    anon @ -m_talk "..."
    consuela f_annoyed "{b}Ricky{/b}, stop it!" (show_native="¡{b}Ricky{/b}, para!")
    consuela "You're making the poor boy uncomfortable..." (show_native="Estás incomodando al pobre chico...")
    ricky @ f_eyeroll "Tsk, it's just a little innocent flirting..."
    ricky "This wet blanket is named {b}Consuela{/b}."
    anon f_normal "H-hi, {b}Consuela{/b}."
    consuela f_normal "Hola, {b}Señor [firstname]{/b}."
    anon f_worried "Are you doing okay?"
    anon "That lady pushed you awfully hard..."
    consuela f_sad "Huh?" (show_native="¿Qué?")
    ricky "Oh, sweetie, she doesn't speak English."
    ricky f_normal "He's asking if you're alright?" (show_native="¿Él pregunta si estás bien?")
    ricky "He probably saw that bitch push you." (show_native="Probablemente vio a esa perra empujarte.")
    consuela "Ahh, that's surprising..." (show_native="Ahh, eso es sorprendente...")
    ricky "Heh, I told you they weren't all assholes."
    show consuela:
        flip
        xoffset 300
    with dissolve
    consuela "Who is he?" (show_native="¿Quién es él?")
    ricky "That's a good question."
    show consuela:
        unflip
        xoffset -300
    with dissolve
    ricky f_smirk @ f_confused "Who are you?"
    ricky "Other than the man of my dreams..."
    anon f_normal @ f_sad_down "Ehh."
    anon "I'm {b}Iwanka{/b}'s new assistant..."
    show anon f_grin
    ricky "He says he works for the mayor's daughter." (show_native="Dice que trabaja para la hija del alcalde.")
    consuela "Pfft, he's lying..." (show_native="Pfft, él está mintiendo...")
    ricky "Try again, hot stuff."
    show anon f_worried
    ricky "That bullshit might fool those tontos at the gate but you'll have to do better with us."
    anon @ a_behind_head "R-right, sorry."
    anon "I kinda... Umm, snuck in here."
    ricky f_confused "Snuck in?"
    anon "I'm looking for dirt on the mayor."
    ricky f_smirk "Well, you won't have to look very hard to find that..."
    show consuela:
        flip
        xoffset 300
    with dissolve
    consuela "What did he say?" (show_native="¿Que dijo el?")
    ricky f_normal "He says he is investigating a scandal surrounding the mayor." (show_native="Dice que está investigando los escándalos que involucran al alcalde.")
    consuela "Scandal?" (show_native="¿Escándalo?")
    consuela "The mayor will go to jail!" (show_native="¡Lo van a meter al bote!")
    ricky "Yes, that is likely." (show_native="Si, eso es probable.")
    consuela "No, this is bad!" (show_native="¡No, esto es malo!")
    consuela "They will deport us!" (show_native="¡Nos deportarán!")
    show consuela:
        unflip
        xoffset -300
    with dissolve
    ricky f_sad "We cannot let you do this..."
    anon @ f_surprised "!!!"
    anon "Why not?"
    ricky "Believe me, we would love to see {b}Mayor Rump{/b} get the justice he deserves."
    ricky "But if he goes to jail, I fear they will deport her."
    anon "Deport her?"
    ricky "Si, she is an illegal immigrant in your country."
    anon @ f_sad_down "Crap."
    ricky "We just need to keep our heads down and our mouths shut."
    pause
    anon "You really want to let them get away with all this?"
    anon "They seem so awful..."
    ricky "Si, that is true."
    ricky "They work us like dogs and treat us even worse!"
    ricky "{b}Consuela{/b} has it the hardest though."
    ricky "At least I make okay money off {b}Missus Rump{/b}..."
    ricky "They pay her next to nothing."
    consuela f_angry "{b}Rump{/b} is a pig!" (show_native="¡{b}Rump{/b} es un cerdo!")
    ricky "And {b}Mister Rump{/b} is always staring..."
    show consuela f_sad_down
    ricky "He likes the thick booty."
    anon "Why doesn't she quit?"
    show consuela f_sad
    ricky f_normal @ f_smirk "Hah!"
    ricky "He asks why you don't quit?" (show_native="¿Él pregunta por qué no renuncias?")
    consuela f_sad_down "I wish I could..." (show_native="Ojalá pudiera...")
    ricky f_sad "{b}Mister Rump{/b} does not allow quitting."
    anon @ -m_talk "..."
    ricky "{i}*Sigh*{/i} Even if she could quit."
    show consuela f_sad
    ricky "How is she supposed to get another job?"
    ricky "She has no education, no skills... She can't even speak English!"
    anon "No, this isn't right."
    anon "There has to be some way I can help her?"
    ricky f_normal "He says he wants to help you..." (show_native="Él dice que quiere ayudarte...")
    show consuela:
        flip
        xoffset 300
    with dissolve
    consuela "Help me?" (show_native="¿Ayudarme?")
    consuela "Why would he do that?" (show_native="¿Por qué?")
    ricky "I think he's just a good guy." (show_native="Creo que solo es un buen tipo.")
    consuela "Pfft, the good ones no longer exist..." (show_native="Pfft, ya no existen de esos...")
    show consuela:
        unflip
        xoffset -300
    with dissolve
    ricky "This is very sweet of you to say, señor... But I do not think it is possible."
    anon @ -m_talk "..."
    rump "{b}CONSUELA{/b}, ISN'T SOMEONE SUPPOSED TO BE WASHING MY CAR?!"
    show consuela f_surprised
    show ricky f_sad
    anon f_surprised "!!!" with hpunch
    consuela f_sad @ a_point "The cunning child should leave now." (show_native="El niño astuto debería irse ahora.")
    ricky "You must go señor!"
    ricky "You do not want {b}Mister Rump{/b} to find you inside his estate..."
    anon f_worried "Y-yeah, alright."
    anon "I'm coming back though!"
    consuela "Go!"
    hide anon with dissolve
    pause
    ricky f_smirk "Mmm, watch that boy go..." (show_native="Mm, mira a ese chico ir...")
    show consuela f_angry:
        flip
        xoffset 300
    with dissolve
    consuela "Go wash the car, idiot!" (show_native="Ve a lavar el auto, ¡idiota!")
    ricky f_eyeroll "Yeah, yeah..."

    scene expression background(l=L_rump_kitchen) with fade
    show anon f_worried with dissolve
    anon @ -m_talk "( There has to be some way I can help that poor lady... )"
    anon @ -m_talk "( I should {b}look around this place some more{/b}. )"
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
