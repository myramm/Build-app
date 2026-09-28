label iwanka_button_bedroom:
    show iwanka f_excited
    show anon with dissolve
    iwanka "Oh em gee!!"
    hide anon
    show iwanka b_dressed_kiss:
        xoffset -200
    with dissolve
    anon "!!!"
    show anon
    show iwanka b_dressed:
        xoffset 0
    with dissolve
    anon "Wow, okay."
    iwanka "I am so glad you're here!"
    iwanka "Being stuck in this house is the absolute worst!"
    anon @ -m_talk "..."
    iwanka "So what's going on?"

    menu iwanka_button_bedroom.choice:
        "{b}Consuela{/b}." if M_consuela.between_states(S_con01_init, S_con01_give) and not M_consuela.finished_state(S_con01_skip):
            jump con01_init_iwanka
        "Working for your dad?":

            jump iwanka_button_bedroom.work
        "The Yacht":

            jump iwanka_button_bedroom.yacht
        "Blowjob.":

            jump iwanka_button_bedroom.blowjob

        "Sex." if M_iwanka.finished_state(S_iwa01_pier):
            jump iwanka_button_bedroom.sex
        "I should go.":

            pass

    anon f_normal @ a_wave "I should go."
    iwanka f_normal "Yeah, okay."
    iwanka f_smirk "Meet me on the yacht later and we'll party, okay?"
    anon "Yeah, maybe."
    iwanka @ f_laugh "See ya, {b}[firstname]{/b}."
    hide anon with dissolve
    return


label iwanka_button_bedroom.blowjob:
    anon f_normal "Mind giving me a blowjob?"
    iwanka f_smirk "Heh, really?"
    anon "Yeah, why not?"
    iwanka "Umm, you realize my father will ship you off to a third world country if he catches us, right?"
    anon f_worried "Wait, what?"
    iwanka "Yeah."
    pause
    anon "You're serious?"
    iwanka "Dead serious."
    iwanka "And that's after he has you castrated."
    anon f_surprised "!!!"
    iwanka @ -m_talk "Mhmm."
    show anon f_surprised_down
    pause
    iwanka "You still want that blowjob?"
    anon f_worried "I-"
    anon f_shy a_behind_head "Umm, you know... On second thought..."
    iwanka @ f_laugh "Haha!"
    iwanka "I didn't think so."
    show anon a_idle with dissolve
    jump iwanka_button_bedroom.choice


label iwanka_button_bedroom.sex:
    anon f_flirt "Want to do it?"
    iwanka f_smirk "Heh, really?"
    anon "Yeah, why not?"
    iwanka f_excited "Umm, you realize my father will ship you off to a third world country if he catches us, right?"
    anon f_worried a_behind_head "Wait, what?"
    iwanka f_smirk "Yeah."
    show anon f_surprised_teeth
    pause
    anon f_worried "You're serious?"
    iwanka "Dead serious."
    iwanka "And that's after he has you castrated."
    anon "!!!"
    iwanka @ -m_talk "Mhmm."
    pause
    iwanka "You still want sex?"
    anon "I-"
    anon "Umm, you know... On second thought..."
    iwanka "Haha!"
    iwanka "I didn't think so."
    show anon a_idle with dissolve
    jump iwanka_button_bedroom.choice


label iwanka_button_bedroom.work:
    anon f_worried "Aren't you supposed to be helping your dad with his work?"
    iwanka f_normal "No, I'm on strike."
    anon "Strike?"
    iwanka f_annoyed "That's right."
    iwanka "I demand shorter hours and longer breaks!"
    iwanka @ a_finger "I want my own office with a plasma TV and one of those massage chairs!"
    anon @ -m_talk "..."
    iwanka "An extra five thousand dollars a week in allowance!"
    iwanka "Fresh lemon wedges for my bottled water!"
    pause
    iwanka "And last but not least, I want this house arrest bullshit to be over!"
    iwanka f_smirk "Then, and only then will I get back to work."
    anon "Wow."
    anon @ a_behind_head "Umm, okay."
    iwanka f_annoyed "I'm not going to be treated like some prisoner in my own home."
    iwanka @ a_finger "This is America, not communist China!"
    jump iwanka_button_bedroom.choice


label iwanka_button_bedroom.yacht:
    anon f_normal "At least you can still sneak out to the yacht, right?"
    iwanka f_smirk "Yes, and thank god for that!"
    iwanka "I'd be climbing the walls if you hadn't shown me how to do that."
    anon "It was nothing, I'm just happy I could help."
    iwanka "No, I owe you big time."
    show iwanka a_touch_sexy:
        xoffset -200
    show anon f_shy behind iwanka
    with dissolve
    iwanka "And I'm looking forward to repaying you... Many, many times."
    anon "{i}*Gulp*{/i} Y-yeah, I'm looking forward to that too."
    show iwanka a_idle behind anon with dissolve:
        xoffset 0
    iwanka "But not here."
    iwanka "My father would kill you if he caught us."
    jump iwanka_button_bedroom.choice
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
