label bodyguard_button_estate:
    show bodyguard f_suspicious
    show anon with dissolve
    bodyguard "{i}*Ahem*{/i} Where do you think you're going?"
    anon f_worried @ -m_talk "Hmm?"
    bodyguard f_normal "You're not supposed to be here."
    anon "O-oh, umm..."
    anon @ f_confused "Isn't this {b}Mayor Rump{/b}'s house?"
    bodyguard "Yeah, that's right."
    bodyguard "And it's off-limits to civilians!"

    menu bodyguard_button_estate.choice:

        "I'm here to see {b}Iwanka{/b}." if M_anon.finished_state(S_ano17_done):
            jump bodyguard_button_estate.assistant
        "I'm supposed to be here.":

            jump bodyguard_button_estate.manager
        "Sorry, I didn't know.":

            pass

    anon "Sorry, I didn't know."
    bodyguard "Move along now, sir."
    bodyguard "Otherwise, I'll have to remove you by force."
    anon @ f_shock "No need for that!"
    anon @ a_wave "I'm leaving."
    hide anon with dissolve
    return


label bodyguard_button_estate.assistant:
    anon f_brag @ f_brag_closed a_point "I'm {b}Iwanka{/b}'s new assistant."
    show bodyguard a_crossed with fastdissolve
    bodyguard "You?!"
    pause
    bodyguard "I haven't heard anything about {b}Mayor Rump{/b} hiring a new assistant for his daughter..."
    anon f_worried "O-oh?"

    if player.stats.chr() < 5:
        jump bodyguard_button_estate.temporary

    anon f_normal "That's probably because the mayor didn't hire me."
    bodyguard f_suspicious @ -m_talk "Hmm?"
    anon "It was actually {b}Mrs. Rump{/b} who hired me."
    bodyguard f_normal a_defensive "Oh!"
    bodyguard a_relief "Now see, that makes sense!"
    bodyguard a_idle "I figured {b}Ricky{/b} wasn't going to be enough for her..."
    anon f_confused "{b}Ricky{/b}?"
    bodyguard "Oh, don't worry... You'll find out."
    show anon f_surprised
    pause
    bodyguard "You can head on inside."
    anon f_worried "I can?"
    anon f_brag_closed "I mean, yes, of course I can."
    anon "Thank you."
    show anon f_snarky
    bodyguard "Just make sure {b}Mrs. Rump{/b} gives you a {b}staff badge{/b}, alright?"
    bodyguard "Otherwise, we'll have to keep doing this dance."
    anon f_normal @ a_wave "Okay, thanks."
    hide anon with {'master': dissolve}
    bodyguard "Have a nice day, sir."

    $ display.toast(chr_pass)
    scene expression L_rump_lobby.background_blur with fade
    show anon with dissolve
    anon @ f_laugh -m_talk "( Alright, {b}Iwanka{/b}'s plan worked! )"
    anon f_worried @ -m_talk "( Now I just need to get my hands on a {b}staff badge{/b}. )"
    if game.timer.is_morning():
        anon f_bored @ -m_talk "( Those guards are relentless about it! )"
        anon @ -m_talk "( I've wasted my entire morning with those idiots. )"
    else:
        anon @ a_thinking f_thinking -m_talk "( It sounds like it would be pretty handy. )"
        anon @ -m_talk "( Maybe I should speak with {b}Iwanka{/b} about it? )"
        pause
        anon @ -m_talk "( I'll just need to find her first... )"
    hide anon with dissolve
    return True

label bodyguard_button_estate.temporary:
    anon f_brag @ f_brag_closed "That's probably because I'm just a temporary hire..."
    anon "... You know, until they find a woman who's more qualified."
    bodyguard f_suspicious "A temporary hire?"
    anon f_worried "{i}*Gulp*{/i} Y-yes?"
    pause
    bodyguard f_normal "One moment while I confirm that."
    bodyguard a_ear "Yeah, we have a suspicious character at the front claiming to be {b}Miss Iwanka{/b}'s new temporary assistant..."
    pause
    bodyguard @ -m_talk "Mmhmm."
    pause
    bodyguard "I see."
    bodyguard a_ear "Should I detain him then, sir?"
    anon f_shock "!!!"
    bodyguard "That's affirmative."
    show anon f_worried a_surprised_up_both with fastdissolve:
        xoffset -50
    anon "Y-you know, on second thought... I'll just come back later."
    show anon f_surprised_teeth a_sides:
        xoffset -100
    show bodyguard a_stop
    with fastdissolve
    bodyguard "Stay right where you are, sir!"
    hide anon with fastdissolve
    anon "Oh shit!!"

    scene black with dissolve
    pause 2

    $ display.toast(chr_fail)
    scene expression L_rump_front.background_blur with dissolve
    show anon b_dressed_catch_breath with dissolve
    anon "Haah... Haah..."
    anon @ -m_talk "( That was close! )"
    anon @ -m_talk "( I've really gotta be more careful going about this. )"
    hide anon with dissolve
    return


label bodyguard_button_estate.manager:
    anon @ a_behind_head "I'm supposed to be here."
    show bodyguard f_suspicious
    anon @ a_point "I'm uhh, here for the... Thing?"
    bodyguard "The thing?"
    anon @ a_behind_head "Yeah, you know... The thing... In the place..."
    show bodyguard a_crossed f_normal with dissolve
    pause
    anon "They want me to take care of it."
    bodyguard @ -m_talk "..."
    anon @ -m_talk "..."
    bodyguard a_ear "I'm going to need backup at the front gate, we have a suspicious individual seeking entry."
    anon f_shock "!!!"
    bodyguard "Bring the taser."
    show anon f_worried a_surprised_up_both with fastdissolve:
        xoffset -50
    anon "Y-you know, on second thought... I might have the wrong house."
    show bodyguard a_stop
    with fastdissolve
    bodyguard "Stay right where you are, sir!"
    hide anon with {'master': fastdissolve}
    anon "Don't tase me, bro!"

    scene black with dissolve
    pause 2

    scene expression L_rump_front.background_blur with dissolve
    show anon b_dressed_catch_breath with dissolve
    anon "Haah... Haah..."
    anon @ -m_talk "( That was close! )"
    anon @ -m_talk "( I've really gotta be more careful going about this. )"
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
