label con01_idea_ivy:
    anon f_worried "Would you be interested in doing a bit of maid work for {b}the mayor{/b}?"
    ivy f_confused "Maid work?"
    ivy "Is that a euphemism for something?"
    anon f_normal @ f_shy a_behind_head "N-no."
    anon "He needs someone to clean his house."
    ivy f_normal "Heh, do I look like a maid to you?"
    anon f_worried "You do not."
    ivy "Well, there ya go."
    anon @ f_sad_down "{i}*Sigh*{/i} Crap."
    ivy "Maybe try a maid service or something?"
    anon "No, that won't work."
    ivy "Why not?"
    anon "{b}The mayor{/b} has some, eh, \"special needs.\""
    ivy "You mean-"
    pause
    ivy f_shy @ f_eww "Eww."
    anon "Yeah."
    ivy f_normal "You know what?"
    show ivy b_naked_pickup with dissolve
    ivy "I might just have the answer to your problem."
    anon f_surprised "Really?"
    ivy "Yup, just give me one-"
    show anon f_normal
    ivy "Ah hah!"
    show ivy b_dressed a_thotbot with dissolve
    ivy "Here we go."
    pause

    scene expression player.location.background_closeup
    show closeup_thotbot
    with fade
    pause
    anon "{b}Thotbot{/b}?"
    anon "The cleaning solution for lonely men."
    anon "With realistic genitalia?"

    call ivy_button_stage
    show anon f_skeptical a_thotbot
    with fade
    anon "Is this for real?"
    ivy "Yup."
    ivy "I used to have one here in the shop but some lady in a lab coat bought it."
    anon f_thinking a_thinking "Hmm, this could actually work."
    anon f_normal "Could you get me one?"
    ivy "If you've got the money, I could have it here in a few days."
    anon "How much?"
    ivy "With shipping, let's say... One thousand dollars?"
    anon f_shock a_surprised_up_both "One thousand dollars?!"
    return


label con01_deal_ivy:
    anon "Are you still willing to order that robot maid for me?"
    ivy "Sure, so long as you have the money?"

    menu con01_deal_ivy.choice:
        "Fine, here you go." if player.has_money(1000):
            jump con01_deal_ivy.purchase
        "I can't afford that!":

            pass

    anon f_worried a_idle @ f_sad_down "I don't have that!"
    ivy "Well, come back and see me when you do."
    anon "Sheesh, alright."
    anon "I'll be back."
    hide anon with dissolve
    return


label con01_deal_ivy.purchase:
    anon f_normal a_money "Fine, here you go."
    show anon a_idle
    show ivy a_money
    with dissolve
    ivy "Perfect!"
    ivy a_idle "I'll order it right away."
    ivy "Come back and pick it up in a few days, okay?"
    anon "Alright, thanks!"
    hide anon with dissolve

    $ player.spend_money(1000)
    $ M_consuela.trigger(T_con01_deal)
    return


label con01_take_ivy:
    anon "Has my package arrived yet?"
    ivy "It sure has!"
    show anon f_normal
    ivy "One second."
    hide ivy with dissolve
    pause
    ivy "You know, when they said, \"realistic genitalia\" they weren't kidding!"
    ivy "This thing is incredible!"
    show ivy f_laugh
    show thotbot:
        flip
        xoffset -100
    with dissolve
    show anon f_surprised
    ivy "I can't vouch for its cleaning abilities, but that pussy is primo!"
    show ivy f_normal
    anon f_confused "Eh, you tried it?"
    ivy f_sexy "Of course!"
    ivy "I perform quality assurance testing on all of my products here at {b}Pink{/b}."
    anon "... Right."
    ivy @ f_laugh "Hehe!"
    show anon f_flirt_grin
    pause
    ivy "Anything else I can help you with?"
    anon f_flirt_low "N-no, I'm good."
    anon "I just hope {b}the mayor{/b} likes it."
    ivy "I'm sure he will."
    ivy f_normal "Have a good day!"
    anon @ f_flirt a_wave "Thanks!"
    show anon a_backpack_robot
    hide thotbot
    with dissolve
    pause

    scene expression player.location.background_blur
    show anon f_worried
    with fade
    anon @ -m_talk "( Man, I hope I don't run into anybody I know while I'm carrying this thing around... )"
    anon @ -m_talk "( I should {b}hurry to the mayor's wife{/b} and see if it's enough to free {b}Consuela{/b}. )"
    hide anon with dissolve
    return


label con01_take_ivy.check:
    anon "Has my package arrived yet?"
    ivy "I'm afraid not."
    ivy "It usually takes two or three days for deliveries here."
    anon f_sad_down "{i}*Sigh*{/i} Alright, thanks."
    hide anon with dissolve
    return


label con01_skip_ivy:
    if player.has_item('thotbot'):
        show anon a_backpack f_looking_down with dissolve
        pause
        anon a_backpack_robot f_normal "I'd like to return this please."
        show anon a_sides f_normal
        show thotbot:
            flip
            xoffset -100
        with dissolve
        ivy "Of course!"
        ivy "You haven't used it have you? We can't accept used items, you understand."
        show anon f_surprised
        show anon of_blush with {'master': dissolve}
        anon "I-- N-- No! It's been in my bag the entire time!"
        ivy "Excellent, that definitely helps matters."
    else:
        anon "I'd like to cancel the {b}Thotbot{/b} I ordered, please."
        ivy "No problem!"

    ivy f_surprised_down "Hmm, less shipping and handling, you're eligble for an eighty percent refund."
    show ivy f_normal
    anon -of_blush f_shock "!!!" with hpunch
    anon f_surprised "Only eighty percent?!"
    ivy "It was a special order. I'm very sorry."
    anon f_sad "Well better than nothing, I guess."
    if player.has_item('thotbot'):
        hide ivy with dissolve
        pause .6
        show ivy behind thotbot with dissolve:
            xoffset -50
        pause
        hide thotbot
        hide ivy
        with dissolve
        pause .6
        show ivy behind counter with dissolve
    ivy a_money "Here you are, sorry your purchase didn't work out."
    show anon a_money
    show ivy a_idle
    with dissolve
    anon "Thanks."
    show anon a_idle with dissolve
    ivy "Will there be anything else?"
    anon "Not at the moment."
    ivy f_normal "Well hope your day improves!"
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
