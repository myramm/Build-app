label con03_door_condo_lounge:
    scene expression player.location.background_blur
    show anon with dissolve
    anon "H-hello?"

    martinez "Open the door, puta!"

    anon f_thinking a_thinking @ f_skeptical a_idle "{b}Martinez{/b}?"

    pause
    consuela "{b}Camila{/b}, be polite!" (show_native="¡{b}Camila{/b}, sé educada!")
    martinez "{i}*Sigh*{/i} Sorry, {b}Mom{/b}..." (show_native="{i}*Sigh*{/i} Lo siento, {b}Mamá{/b}...")
    show anon f_worried a_idle
    show martinez f_angry behind anon:
        xoffset -100
    show consuela b_casual a_enchiladas:
        xoffset 100
    with dissolve
    anon "Apa yang terjadi?"

    martinez f_normal "My mother wants to repay you for all your help."

    martinez "So she made you some enchiladas."

    anon f_normal "Oh?"

    show anon f_flirt_low:
        xoffset 200
    show martinez f_eyeroll
    show consuela:
        xoffset 50
    with dissolve
    consuela "Gracias, {b}Mister [firstname]{/b}."

    consuela "I make for you."

    show anon a_lasagna
    show consuela -a_enchiladas
    with dissolve
    anon f_normal "Wow, these look delicious!"

    consuela "Si, delicious."

    martinez f_normal @ f_surprised_up "Fuck me..."

    show anon f_worried
    martinez "You seriously live here?"

    anon f_normal "Ya."

    martinez "Man, your parents must be loaded, huh?"

    anon f_sad_down "T-tidak."

    anon "My dad is dead, remember?"

    martinez "Oh benar."

    martinez "Saya buruk."

    anon "... I'll just put these in the kitchen..."

    hide anon with dissolve
    consuela f_angry @ -m_talk "Hmm?"

    consuela "What did you say to him?" (show_native="¿Qué le dijiste?")
    show consuela behind martinez
    show martinez:
        flip
        xoffset 450
    with dissolve
    martinez "Nothing, his dad is dead..." (show_native="Nada, su papá está muerto...")
    martinez "I forgot." (show_native="Lo olvidé.")
    consuela "Tsk, {b}Camila{/b}!"

    consuela "Tell him you're sorry!" (show_native="¡Dile que lo sientes!")
    martinez @ f_eyeroll "Ugh."

    show martinez behind consuela:
        unflip
        xoffset -100
    show anon f_sad_down behind consuela
    with dissolve
    martinez "My mother says she's sorry for your loss..."

    anon f_worried "Oh?"

    anon f_normal "Terima kasih, {b}Consuela{/b}."

    consuela f_normal "Ya, {b}Pak [firstname]{/b}."

    consuela "Mm, I like him." (show_native="Mm, me gusta el.")
    consuela "He's a good boy." (show_native="El es un buen chico.")
    pause
    show consuela a_whisper behind martinez
    show martinez:
        flip
        xoffset 450
    with dissolve
    consuela a_idle @ a_whisper "You should flirt with him." (show_native="Deberías coquetear con él.")
    martinez "Eww, {b}Mom{/b} don't be disgusting!" (show_native="¡Eww, {b}Mamá{/b} no seas asquerosa!")
    show anon f_skeptical
    consuela "What?" (show_native="¿Que?")
    consuela "He's cute and obviously earns good money..." (show_native="Es lindo y obviamente gana buen dinero...")
    martinez "Tidak."

    consuela "Why not?" (show_native="¿Por qué no?")
    show martinez a_crossed f_angry
    consuela "You need a man who can provide for you!" (show_native="¡Necesitas un hombre que pueda proveer para ti!")
    martinez @ -m_talk "..."
    consuela f_sad "You don't want to end up like me, do you?" (show_native="No quieres terminar como yo, ¿verdad?")
    martinez "Drop it, {b}Mom{/b}!" (show_native="¡Déjalo, {b}Mamá{/b}!")
    anon "What is happening?"

    show martinez behind consuela with dissolve:
        unflip
        xoffset -100
    martinez "Tidak ada apa-apa."

    anon f_worried @ -m_talk "..."
    martinez f_surprised @ f_surprised_up "So you bought this place yourself?"

    anon "Ya."

    martinez f_angry "How the hell did you afford it?"

    anon f_normal "I got a job and saved up my money."

    martinez "Ya benar."

    consuela "Where's his mother?" (show_native="¿Dónde está su madre?")
    martinez f_normal "I don't know." (show_native="No lo sé.")
    martinez "I think he lives here alone." (show_native="Creo que vive aquí solo.")
    consuela "{i}*Gasp*{/i} Who cleans for him?" (show_native="{i}*Gasp*{/i} ¿Quién limpia para él?")
    martinez "You got somebody cleaning this place?"

    anon "Tidak Memangnya kenapa?"

    martinez "He says no one." (show_native="Él dice que nadie.")
    consuela f_normal @ f_laugh "Aku membersihkannya untukmu!"

    anon "Hah?"

    anon "N-no, you don't have to do that..."

    consuela "Ya, benar."

    consuela "Kamu orang baik."

    consuela "Cari pekerjaan."

    consuela "I clean for you."

    martinez @ f_eyeroll "Just say yes, idiot."

    martinez "She's not going to take no for an answer."

    anon "Baiklah, jika kamu bersikeras..."

    show anon b_empty f_surprised_down:
        xoffset 0
    show consuela b_dressed_hug behind anon:
        xoffset 0
    with dissolve
    show martinez f_disgusted
    anon "!!!"
    martinez "Bruto."

    martinez "Can we go now?" (show_native="¿Podemos ir ahora?")
    show anon b_dressed f_normal behind consuela
    show consuela b_casual f_angry:
        flip
        xoffset 300
    with dissolve
    consuela "Stop being rude!" (show_native="¡Deja de ser grosera!")
    consuela "He will never go out with you if you act like this..." (show_native="Él nunca va a salir contigo si actúas así...")
    martinez f_angry @ f_eyeroll "Ugh, for fuck's sake..."

    martinez "I'm out of here."

    hide martinez with dissolve
    pause
    anon @ f_confused -m_talk "..."
    show consuela f_sad with dissolve:
        unflip
        xoffset -100
    consuela "Eh."

    consuela a_belly "{b}Camila{/b} stomach..."

    consuela "No feel good."

    show consuela a_idle with dissolve
    anon f_worried "O-oh."

    anon "Oke."

    pause
    consuela f_smirk "I come back."

    consuela "Clean good, okay?"

    anon f_normal "Oke, tentu saja."

    consuela "Adios, {b}Mister [firstname]{/b}."

    hide consuela with dissolve
    pause
    anon "Yeah, adios."

    pause
    anon f_thinking a_thinking @ -m_talk "( Hmm, is she seriously going to clean this place free of charge? )"

    anon a_idle f_grin "( {b}Consuela{/b} is such a nice lady. )"

    anon "( I'm really glad I helped her! )"

    hide anon with dissolve
    return

label con03_sing_condo_lounge:
    scene expression player.location.background_blur
    show anon with dissolve
    consuela "♪ The guy from apartment 512 ♪" (show_native="♪ El chico del apartamento 512 ♪")
    consuela "♪ The one who makes my poor heart jumps ♪" (show_native="♪ Él que hace a mi pobre corazón saltar ♪")
    anon "Is that {b}Consuela{/b}?"

    consuela "♪ To whom I write letters day and night ♪" (show_native="♪ Es a quien le hago cartas noche y día ♪")
    consuela "♪ Which I can't deliver ♪" (show_native="♪ Que no puedo entregar ♪")
    anon "She's singing."

    consuela "♪ The guy from apartment 512 ♪" (show_native="♪ El chico del apartamento 512 ♪")
    consuela "♪ Who causes me to stutter and worse ♪" (show_native="♪ Es él quien me hace tartamuda y más ♪")
    anon "Sounds like she's in the kitchen..."

    consuela "♪ He is the one I dream about all day ♪" (show_native="♪ Es en quien yo pienso y sueño noche y día ♪")
    consuela "♪ Him, only him ♪" (show_native="♪ Él, solo él ♪")
    anon @ f_laugh "I should peek in and see how she's doing."

    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
