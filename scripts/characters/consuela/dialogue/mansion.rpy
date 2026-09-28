label consuela_button_mansion:
    show consuela b_dressed_mop f_normal_down
    show anon with dissolve
    anon "{b}Consuela{/b}?"
    consuela b_dressed a_work3 f_sad "Ay no..."
    consuela f_annoyed "What are you still doing here?" (show_native="¿Que sigues haciendo aqui?")
    anon f_worried @ f_confused "Eh?"
    consuela "You cannot be here!" (show_native="¡No puedes estar aquí!")
    consuela "Mr. Rump will kill you!" (show_native="¡El {b}Señor Rump{/b} te matará!")
    anon "{b}Consuela{/b}, please... Listen to me."
    show consuela f_sad
    anon "I'm going to help you, okay?"
    consuela "{i}*Sigh*{/i} I don't know what you're saying..." (show_native="{i}*Sigh*{/i} No sé lo que dices...")
    anon "I'll figure something out, I promise!"
    pause
    anon @ a_wave "Just hang in there."
    hide anon with dissolve
    pause 1
    consuela b_dressed_mop f_sad_down @ f_sad "He's a brave boy, I'll give him that." (show_native="Es un chico valiente, se lo daré.")
    pause 2
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
