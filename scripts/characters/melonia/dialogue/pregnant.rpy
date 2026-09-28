label melonia_button_pregnant:
    show melonia f_annoyed
    show anon with dissolve
    anon "How's everything going?"
    melonia "Tch, I'm pregnant with your idiot child..."
    show anon f_worried
    melonia "... How do you think it's going?"

    menu melonia_button_pregnant.choice:
        "Are you feeling okay?":

            if M_melonia.pregnancy.stage == 1:
                jump melonia_button_pregnant.annoyed
            elif M_melonia.pregnancy.stage == 2:
                jump melonia_button_pregnant.vain
            else:
                jump melonia_button_pregnant.nauseous
        "Staying out of the hot tub?":

            jump melonia_button_pregnant.hottub
        "I should go.":

            pass

    anon f_worried "I should go."
    anon "Let me know if you need anything, okay?"
    melonia f_annoyed "Yeah, how about a pool boy who knows how to pull out?"
    anon f_thinking @ -m_talk "..."
    anon f_normal @ f_laugh "Very funny."
    melonia "Just beat it and let me relax, would you?!"
    anon f_sad_down "Fine."
    hide anon with dissolve
    return


label melonia_button_pregnant.annoyed:
    anon f_worried "Are you feeling okay?"
    melonia f_annoyed "No."
    melonia "I'm feeling very, very annoyed with you right now for talking me into this!"
    anon "Okay..."
    anon "... But otherwise, you're feeling good?"
    melonia @ f_pouting "{i}*Sigh*{/i} I feel pregnant."
    melonia "Any more questions?!"
    jump melonia_button_pregnant.choice


label melonia_button_pregnant.hottub:
    anon f_shy "Staying out of the hot tub?"
    melonia f_glaring "Do you want me to punch you?"
    anon f_brag_closed "It's important that you stay out of the hot tub while you're pregnant, {b}Melonia{/b}..."
    anon "... You know that."
    show anon f_shy
    melonia "Yes, {b}[firstname]{/b}."
    melonia "I'm staying out of the hot tub; I'm not a monster!"
    anon a_point "And no alcohol?"
    melonia a_fists @ -m_talk "..."
    anon a_idle f_worried @ f_surprised a_surprised_up_both "Oh kay, I'll take that as a yes..."
    show melonia a_idle with dissolve
    jump melonia_button_pregnant.choice


label melonia_button_pregnant.nauseous:
    anon f_worried "Are you feeling okay?"
    melonia f_annoyed "No, I am not feeling okay!"
    melonia "My back hurts, I'm nauseous, my feet are swollen, and my tits are leaking all over the place!"
    anon "That's, umm-"
    melonia @ f_pouting "And to top it all off, everytime I sneeze I pee a little!"
    anon f_surprised @ -m_talk "!!!"
    melonia "Yeah."
    melonia "That's a lovely little tidbit, isn't it?!"
    anon f_worried "Can I do something to make you feel better?"
    melonia "You could punch yourself in the face, like, REALLY hard."
    anon @ f_hurt -m_talk "..."
    anon "Anything less violent?"
    melonia "{i}*Sigh*{/i} No."
    melonia "I just want this demon child out of me..."
    anon "You're almost there, just a few more days."
    jump melonia_button_pregnant.choice


label melonia_button_pregnant.vain:
    anon f_worried "Are you feeling okay?"
    melonia f_annoyed "Eugh, look at me..."
    anon "Huh?"
    melonia "Do you have any idea how much work it took to bounce back after I had {b}Iwanka{/b}?"
    anon @ f_thinking "Umm."
    melonia @ f_yell "Too much!"
    melonia "And now I'm going to have to do it all over again, thanks to you!"
    anon "You're being ridiculous."
    anon "I think you look great!"
    melonia @ f_eyeroll "Well, you're an idiot."
    jump melonia_button_pregnant.choice
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
