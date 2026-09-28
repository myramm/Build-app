label nadya_button_baby:
    if L_warehouse_depot.is_here(M_nadya):
        jump nadya_button_baby_depot
    jump nadya_button_baby_office


label nadya_button_baby_depot:
    pause .1
    show nadya f_surprised
    show svetlana f_surprised
    "{i}*Workers chattering*{/i}"
    show svetlana a_crossed
    show nadya f_angry:
        xoffset 675
        xzoom -1
    with {'master': dissolve}
    nadya "Hey, stop loitering about!"
    show svetlana:
        xoffset 450
    with {'master': dissolve}
    nadya "Back to work, all of you!"
    show anon f_worried behind nadya with dissolve:
        xoffset -100
    nadya "What, you think because I have baby I will not walk over and make example of you?!"
    show anon f_worried_surprised
    nadya "I stuff you in potato sack and ship you back Russia!"
    show anon f_worried
    anon "Ehh, {b}Nadya{/b}?"
    show anon a_surprised_up_both f_worried_surprised
    show nadya f_frowning:
        xoffset 100
        xzoom 1
    show svetlana a_sides f_curious:
        xoffset -100
        xzoom 1
    with {'master': dissolve}
    nadya "What?!"
    show svetlana f_normal
    nadya f_normal "Oh."
    show anon a_sides f_worried
    with {'master': dissolve}
    nadya "Sorry, {b}[firstname]{/b}." (show_native="Izvinite, {b}[firstname]{/b}.")
    nadya "The hormones are running crazy inside me..."
    show anon f_shy
    nadya f_annoyed_down "... And my tits won't stop leaking..."
    nadya "... Is like monsoon."
    show nadya f_normal

    menu nadya_button_baby_depot.choice:
        "How's our little one?":
            if not M_nadya.once('baby_vodka'):
                jump nadya_button_baby_depot.vodka
            jump nadya_button_baby_depot.sleep
        "I should go.":

            pass

    anon "Let me know if you need anything, okay?"
    show svetlana f_happy
    nadya f_happy "Do not worry."
    nadya "Everything is under control."
    svetlana "Da."
    svetlana "Is no problem."
    hide anon with dissolve
    return


label nadya_button_baby_depot.vodka:
    anon "How's our little one?"
    nadya "Is good."
    show anon f_normal
    nadya "A little trouble sleeping but nothing a few drop vodka can't fix."
    anon f_surprised "Vodka?!"
    anon "You can't give babies vodka!!"
    show svetlana f_curious
    nadya f_frowning @ -m_talk "Hmm?"
    nadya "Why not?!"
    anon f_worried_surprised "Because... it's bad for them!"
    show nadya f_normal
    svetlana f_smirk "Is not bad for Russian baby."
    show svetlana a_hips
    with {'master': dissolve}
    svetlana "Vodka make them strong."
    nadya "See, it is known!"
    svetlana "It is known."
    anon f_annoyed "No, it is not known!"
    show nadya f_angry
    show svetlana f_glaring
    pause
    anon "Don't give me the glaring thing, it's not going to work!"
    anon "I'm putting my foot down!"
    anon "No vodka for our baby!"
    nadya f_pouting "Is just tiny bit to help sleep."
    nadya "It will not harm-"
    anon "I said no!"
    pause
    anon "I'm serious, {b}Nadya{/b}."
    pause
    nadya f_frowning "Hmph, very well."
    show svetlana a_surprised f_surprised with {'master': dissolve}:
        xoffset 450
        xzoom -1
    svetlana "You're conceding to him?" (show_native="Vy yemu ustupayete?")
    show svetlana a_sides
    with {'master': dissolve}
    nadya f_worried "He is good father." (show_native="On khoroshiy otets.")
    show svetlana f_timid
    nadya "I owe him a lot." (show_native="Ya yemu mnogim obyazan.")
    anon f_unimpressed "English, please."
    nadya "I say you win."
    show svetlana f_timid:
        xoffset -100
        xzoom 1
    with {'master': dissolve}
    nadya "No vodka for babies."
    anon "And you?"
    svetlana f_normal "{b}Miss Chernyshevsky{/b} pays me to follow orders."
    svetlana "If she say no vodka for babies, then no vodka for babies."
    anon f_shy "Thank goodness for that!"
    jump nadya_button_baby_depot.choice


label nadya_button_baby_depot.sleep:
    anon "How's the little one?"
    nadya f_normal "Is good."
    show svetlana f_normal
    nadya f_worried "Still trouble sleeping through night, but we'll soon be past the worst of it."
    svetlana "Da, there is improvement each day."
    pause
    show svetlana f_smirk_back
    nadya "I'm glad to have {b}Svetlana{/b}, she is very good with baby."
    show svetlana a_crossed f_normal with {'master': dissolve}
    svetlana "Babies are nothing new to me."
    svetlana "I've taken care of many."
    anon "Well, I'm thankful we have you as well."
    show svetlana a_sides f_happy with {'master': dissolve}
    svetlana "Heh, is nice to be appreciated."
    svetlana "Thank you." (show_native="Spasibo.")
    jump nadya_button_baby_depot.choice


label nadya_button_baby_office:
    nadya "Shh, baby is finally sleeping."
    show anon b_sit with dissolve:
        xoffset -250
    pause
    show anon f_shy_low

    if M_nadya.pregnancy.baby_gender:
        anon "He's so beautiful."
    else:
        anon "She's so beautiful."

    nadya f_sexy_down "Da."
    pause
    nadya "Especially when sleeping."

    menu nadya_button_baby_office.choice:
        "Need anything?":
            jump nadya_button_baby_office.anything
        "Take care.":

            pass

    anon f_shy "Take care."
    nadya f_normal "Tell {b}Svetlana{/b} to fetch new swaddling blanket on your way out."
    anon "Can do."
    nadya f_happy "Thank you." (show_native="Spasibo.")
    pause
    anon "Good night, {b}Nadya{/b}."
    anon f_shy_low "Good night, little one."
    nadya "Good night, {b}[firstname]{/b}." (show_native="Spokoynoy nochi, {b}[firstname]{/b}.")
    hide anon with dissolve
    return


label nadya_button_baby_office.anything:
    anon f_normal "Need anything?"
    nadya f_normal "No." (show_native="Nyet.")
    nadya "Baby will sleep thirty minutes..."
    nadya "... Then I will feed."
    nadya "After that, {b}Svetlana{/b} will read baby story while I rest."
    anon f_shy "Sounds like you two have everything well in hand."
    nadya f_happy "Da."
    jump nadya_button_baby_office.choice
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
