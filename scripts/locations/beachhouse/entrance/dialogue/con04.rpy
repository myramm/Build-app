label con04_wake_condo_lounge:
    scene expression background(200, 400, 4.) at flip
    show layer master at flip
    show lopez f_angry:
        flip
        xoffset 350
    show martinez f_angry
    martinez "It doesn't make sense, she had the best voice on the show!"

    lopez "It doesn't matter, she looked like a camel."

    martinez "Ck."

    lopez "You know the ugly ones never win."

    show anon f_worried with dissolve:
        xoffset -100
    martinez "That's stupid..."

    lopez "Yeah, well, it's true."

    anon "Umm, what's going on?"

    show lopez:
        unflip
        xoffset -200
    with dissolve
    lopez "Ugh, nice job... You woke him up!"

    martinez "Go back to bed, puta."

    martinez "We're watching television."

    anon f_skeptical "Yeah, you're watching MY television..."

    anon "What the hell are you two even doing here?"

    lopez "Her mom said we could watch TV 'til the bus comes."

    anon "Ah, benarkah?"

    martinez "Yeah, you got a problem with that?!"

    anon f_worried "T-tidak."

    consuela "Could you girls please stop yelling?" (show_native="¿Podrían dejar de gritar niñas?")
    consuela "You're going to wake up {b}Mister [firstname]{/b}." (show_native="Van a despertar a {b}Mister [firstname]{/b}.")
    show consuela f_angry behind anon with dissolve:
        flip
        xoffset 150
    martinez "He's already awake, {b}Mom{/b}." (show_native="Él ya está despierto, {b}Mamá{/b}.")
    martinez "And interrupting our show!"

    anon @ -m_talk "..."
    consuela "{b}Camila{/b}!"

    consuela "Have a little respect for your future husband!" (show_native="¡Ten un poco de respeto por tu futuro esposo!")
    martinez @ f_disgusted "He is not my future husband!" (show_native="¡Él no es mi futuro esposo!")
    consuela "Not if you keep acting like this..." (show_native="No si sigues actuando así ...")
    show consuela f_sad with dissolve:
        unflip
        xoffset -400
    consuela "Sorry, papi."

    consuela "I tell them, be quiet!"

    consuela "But they no listen!"

    martinez @ f_eyeroll "What the fuck are you calling him \"papi\" for?"

    lopez f_normal @ a_cover_mouth f_laugh "{i}*Mendengus*{/i}"

    show consuela f_angry with dissolve:
        flip
        xoffset 150
    consuela "They go now!"

    anon "T-tidak, tidak apa-apa."

    anon "They can watch TV, I don't care."

    show consuela f_sad with dissolve:
        unflip
        xoffset -400
    consuela @ -m_talk "..."
    consuela "They stay?"

    anon f_normal "Tentu."

    consuela f_normal @ f_laugh "Thank you, {b}Mister [firstname]{/b}!" (show_native="¡Oh, gracias {b}Mister [firstname]{/b}!")
    show consuela b_kiss5:
        xoffset -100
    show anon b_empty
    with dissolve
    pause
    show consuela b_dressed:
        xoffset -400
    show anon b_dressed
    with dissolve
    consuela "Thank you, thank you, thank you!" (show_native="¡Gracias, gracias, gracias!")
    martinez "{b}Mom{/b}, why did you call him \"daddy\"?" (show_native="{b}Mamá{/b}, ¿por qué lo llamaste \"papi\"?")
    lopez @ f_laugh "Is your mother fucking {b}[firstname]{/b}?" (show_native="¿Tu mamá se está cogiendo a {b}[firstname]{/b}?")
    martinez f_angry "Shut up!" (show_native="¡Cállate!")
    show consuela f_angry with dissolve:
        flip
        xoffset 150
    consuela "Be silent, both of you!" (show_native="¡Cállense las dos!")
    martinez a_crossed "Hmph!"

    pause
    show consuela f_normal with dissolve:
        unflip
        xoffset -400
    consuela "Come, I cook for you."

    anon "Oh, that sounds good!"

    consuela "Si, very good."

    hide anon with dissolve
    lopez "I'm hungry too." (show_native="Yo también tengo hambre.")
    show consuela f_angry with dissolve:
        flip
        xoffset 150
    consuela "There is no breakfast for disrespectful brats!" (show_native="¡No hay desayuno para chamacas irrespetuosas!")
    lopez f_angry "Ugh, what did I do?" (show_native="Ugh, ¿que hice?")
    consuela "Shut up!" (show_native="¡Cállate!")
    lopez f_sad @ f_surprised "!!!"
    consuela "He's a good boy!" (show_native="¡El es un buen chico!")
    consuela "You girls would be lucky to marry someone like him!" (show_native="Ustedes chicas tendrían suerte de casarse con alguien como él.")
    martinez f_disgusted "He is disgusting, {b}Mom{/b}!" (show_native="¡Él es asqueroso, {b}Mamá{/b}!")
    consuela "You don't know what you're talking about..." (show_native="No sabes de qué estás hablando ...")
    consuela "He's clean, generous, and handsome." (show_native="Es limpio, generoso y guapo.")
    consuela "You should be thinking about your future!" (show_native="¡Deberías estar pensando en tu futuro!")
    consuela "He could provide for you." (show_native="Él podría proveer para ti.")
    consuela "He could provide for all of us." (show_native="Él podría proveer para todos nosotros.")
    martinez @ f_eyeroll "Yeah, right." (show_native="Sí, ¿verdad?")
    consuela "{i}*Sigh*{/i} Just keep silent and watch TV." (show_native="{i}*Sigh*{/i} Solo guarda silencio y mira la televisión.")
    consuela "I'll do everything, like always." (show_native="Haré todo, como siempre hago.")
    hide consuela with dissolve
    pause
    show lopez with dissolve:
        flip
        xoffset 350
    lopez "Damn, your mom is seriously pissed..."

    martinez f_angry "She's being a bitch!"

    pause
    show lopez f_smirk
    pause
    lopez "So, you think he's fucking her?"

    martinez f_disgusted "EWW!"

    martinez "Shut the fuck up!"

    lopez f_normal @ f_laugh "Ha ha ha!"

    martinez @ f_eyeroll "Screw this, I'd rather wait at the bus stop..."

    hide martinez with dissolve
    lopez "Hey, wait up!"

    hide lopez with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
