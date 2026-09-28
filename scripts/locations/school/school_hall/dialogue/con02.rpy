label con02_job2_school_hall:
    scene expression player.location.background_blur with None
    show anon:
        xoffset 100
    show consuela b_casual:
        flip
        xoffset -100
    with dissolve
    anon "Hmm, I guess we should head upstairs and talk with {b}Mrs. Smith{/b}?"
    anon "I have no idea what service they use at the moment..."
    consuela f_surprised "This place is huge!" (show_native="¡Este lugar es enorme!")
    consuela "Am I going to clean all of this?" (show_native="¿Voy a limpiar todo esto?")
    anon "Or maybe {b}Annie{/b} can help us?"
    martinez "{b}Mamá{/b}?!!"
    show anon f_skeptical
    consuela @ -m_talk "!!!"
    anon "Mama?"
    show lopez f_angry:
        xoffset 100
    show martinez f_angry:
        xoffset -100
    with dissolve
    show consuela f_normal
    martinez "What the hell?" (show_native="¿Que demonios?")
    anon f_surprised "Wait a second..."
    anon "{b}Consuela{/b} is your mom?"
    martinez "Shut up, puta!"
    consuela f_annoyed @ f_angry "{b}Camila{/b}, no cursing!" (show_native="¡{b}Camila{/b}, no maldigas!")
    martinez f_concerned "Oh, sorry {b}Mom{/b}..." (show_native="Ay, lo siento {b}Mamá{/b}...")
    martinez f_normal "What are you doing here?" (show_native="¿Qué estás haciendo aquí?")
    consuela f_normal "This boy brought me here to find work..." (show_native="Este chico me trajo aquí para encontrar trabajo...")
    martinez f_surprised "What?!"
    martinez "What happened to your job at the mayor's house?" (show_native="¿Qué pasó con tu trabajo en la casa del alcalde?")
    consuela f_sad "I was fired." (show_native="Me despidieron.")
    martinez "Huh, why?" (show_native="¿¡Que!?, ¿por qué?")
    consuela "It's not important..." (show_native="No importa...")
    martinez f_concerned "No, please... You can't work here!" (show_native="No por favor... ¡No puedes trabajar aquí!")
    consuela f_annoyed "Why not?" (show_native="Por qué no?")
    martinez "Because it's embarrassing!" (show_native="¡Porque es vergonzoso!")
    consuela @ f_eyeroll "Tsk!"
    anon f_worried "What is happening?"
    martinez f_angry "Shut the fuck up!"
    martinez "She is not working here!"
    anon "Huh?"
    anon "Why not?"
    lopez "You are so dead, {b}[firstname]{/b}..."
    anon f_surprised @ f_shock "!!!"
    anon "What did I do?"
    martinez f_concerned "Please, {b}Mom{/b}!" (show_native="¡Por favor {b}Mamá{/b}!")
    martinez "Everyone will laugh at me!" (show_native="¡Todos se reirán de mí!")
    consuela "You worry too much, {b}Camila{/b}..." (show_native="Te preocupas demasiado, {b}Camila{/b}...")
    martinez "Please, {b}Mom{/b}... I beg you!" (show_native="Por favor, {b}Mamá{/b}... ¡Te lo ruego!")
    consuela f_sad "{i}*Sigh*{/i} Very well." (show_native="{i}*Sigh*{/i} Muy bien.")
    consuela "I'll look for something else." (show_native="Buscaré otra cosa.")
    martinez f_normal "Phew, thank you, {b}Mom{/b}!" (show_native="Phew, ¡gracias {b}Mamá{/b}!")
    anon @ -m_talk "..."
    consuela "We go."
    anon f_worried_left "Huh?"
    consuela "I no clean!"
    consuela "We go."
    hide consuela with dissolve
    anon "Aww, man..."
    martinez f_angry "What the fuck were you thinking, estúpido?!"
    show anon f_surprised_teeth
    lopez "Yeah, you realize we're going to kill you now, right?"
    anon f_surprised "Hey, c'mon ladies... I'm just trying to help!"
    martinez "You're dead."
    show anon f_sad_down
    hide martinez with dissolve
    pause
    lopez f_normal "See you soon, puta!"
    anon @ -m_talk "..."
    hide lopez with dissolve
    anon f_worried a_behind_head "Sheesh."
    anon @ -m_talk "( Those girls are crazy! )"
    anon f_worried_left @ -m_talk "( I should hurry and catch {b}Consuela{/b} before she ends up begging at the {b}mall{/b} again... )"
    hide anon with dissolve

    $ player.go_to(L_school_front)
    scene expression player.location.background_blur with fade
    show consuela b_casual f_sad with dissolve
    pause
    anon "{b}Consuela{/b}, stop!!"
    show consuela a_hips f_annoyed
    pause
    show anon b_dressed_catch_breath with dissolve
    anon "Would you hold on just a second?"
    consuela "This is not going well..." (show_native="Esto no va bien...")
    show anon b_dressed f_worried with dissolve
    anon "Huh?"
    consuela "No job."
    consuela "I go."
    anon @ a_wave "Just wait, please!"
    anon "I'll find you something, I promise!"
    consuela a_crossed @ -m_talk "Hmph!"
    pause
    anon f_thinking @ -m_talk "( There has to be some place that will hire her... )"
    anon a_thinking @ -m_talk "( The library, maybe? )"
    pause
    anon @ -m_talk "( No, that place runs on donations... They won't be able to afford a cleaning lady. )"
    pause
    anon f_hurt @ -m_talk "( C'mon, {b}[firstname]{/b}... Think! )"
    anon f_normal a_idle @ a_point "We could try the {b}clinic{/b}."
    consuela "{b}Clínica{/b}?"
    consuela "I clean {b}clínica{/b}?"
    anon "Yeah, maybe."
    anon "{b}Let's go find out{/b}."
    consuela f_annoyed_down "Okay."
    consuela "We go."
    anon "C'mon."
    hide anon with dissolve
    hide consuela with dissolve

    scene black with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
