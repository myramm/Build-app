label kim_button_showroom:
    show anon f_worried with dissolve
    kim "What you want, poor boy?"
    kim f_normal "I no have time for you..."

    menu kim_button_showroom.choice:

        "Can I see your phone?" if M_anon.between_states(S_ano07_mech, S_ano07_give):
            jump ano07_hint_kim
        "You're very rude, you know that?":

            jump kim_button_showroom.rude

        "Employee of the month?" if M_kim.eotm:
            jump kim_button_showroom.employee

        "Russians?" if M_kim.russians:
            jump kim_button_showroom.russians
        "You suck. I'm leaving.":

            pass

    anon "You suck. I'm leaving."
    kim "Yes, you go home to poor famiry."
    kim "Come back when you have money."
    kim @ f_laugh "Hue hue hue!!"
    hide anon with {'master': dissolve}
    kim @ a_wave "Bye poor boy!"
    return


label kim_button_showroom.employee:
    anon f_worried @ f_skeptical "Employee of the month?"
    kim @ a_counter_raised "Yes, {b}Kim{/b} is number one, best car saresman!"
    kim "Soon, I own this prace."
    anon "I doubt that."
    kim @ f_curious "Oh, prease... What you know, poor boy?!"
    anon @ f_skeptical "I know that you're an asshole and people don't like that..."
    kim @ f_laugh "Hue hue hue!"
    kim "{b}Kim{/b} conquer car dearership!"
    kim "Wait and see."
    anon f_surprised "Conquer?"
    kim a_counter_raised "Yes, {b}Kim{/b} become boss."
    show anon f_unimpressed
    kim "Then {b}Kim{/b} expand into nationar chain!"
    kim "Cover entire nation with dearerships!!"
    anon @ -m_talk "..."
    kim "First nation, then pranet!"
    kim a_idle @ f_laugh "Hue hue hue hue!"
    kim @ a_rub "{b}Kim{/b} become a dearership GOD!!!"
    anon "What the fu-"
    kim @ f_laugh "HUE HUE HUE!!!"
    jump kim_button_showroom.choice


label kim_button_showroom.rude:
    anon f_worried "You're very rude, you know that?"
    kim f_curious "Aww, you gonna cry, poor boy?"
    anon "N-no."
    kim f_baby_cry a_cry "Boo hoo, me so poor..."
    anon f_sad "Shut up!"
    kim f_normal a_idle @ f_laugh "Hue hue hue!"
    show anon a_thinking f_thinking with dissolve
    pause
    anon f_skeptical a_idle "I'm gonna tell your boss about the way you're treating me!"
    kim "Go ahead."
    kim "They no risten to you."
    show anon f_worried
    kim @ a_counter_raised "{b}Kim{/b} is best salesman!"
    kim "Emproyee of month, for five months in row."
    $ M_kim.set('eotm', True)
    kim "I make dearership rots of money."
    kim "You just stupid poor boy."
    anon "We'll see about that..."
    kim @ f_curious "{i}*Yawn*{/i}"
    kim "You stirr tarking?"
    kim @ a_wave "Go away, poor boy."
    kim "You make {b}Kim{/b} very sreepy."
    jump kim_button_showroom.choice


label kim_button_showroom.russians:
    anon f_worried "I hear you have some Russian regulars that buy a lot of cars?"
    kim f_curious "Where you hear this, poor boy?!"
    anon "{b}Josephine{/b}."
    kim @ -m_talk "Hmm."
    kim "So what if I do?"
    kim f_normal "It's no business of yours!"
    anon "Well, I was hoping you might be able to give me some information about them?"
    kim "Pfft!"
    kim f_angry @ a_point "You hope in one hand and shit in other, see which one firrs up first."
    anon f_unimpressed "C'mon, man."
    anon "This is really important..."
    kim "{b}Kim{/b} terr you nothing!"
    kim "You go away now!"
    anon @ -m_talk "..."
    hide anon with {'master': dissolve}
    kim f_smirk a_wave "Bye bye, poor boy!"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
