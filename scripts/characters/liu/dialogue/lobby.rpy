label liu_button_lobby:
    show anon with dissolve
    liu "Welcome to {b}Saga Financial{/b}."
    liu f_happy "How can I help-"

    if M_anon.finished_state(S_ano28_clue):
        show liu a_mouth_cover f_surprised
        with {'master': dissolve}
        liu "{b}[firstname]{/b}!!"
        anon a_wave "Hey, Liu."
        show anon a_sides
        show liu a_point_self
        with {'master': dissolve}
        liu "Did you come to see me?"
        show liu a_sides
        with {'master': dissolve}
    else:

        show liu a_sides f_nervous
        with {'master': dissolve}
        liu "O-oh, you're back..."
        anon "Hello again, Liu."

    menu liu_button_lobby.choice:

        "Apartment number?" if M_anon.is_state(S_ano23_done, S_ano24_init):
            jump liu_button_lobby.apartment

        "Dad's money." if M_anon.is_state(S_ano28_cash):
            jump ano28_cash_liu_money

        "Is Tina around?" if M_tina.is_state(S_tin02_init):
            if L_bank_cubicle.is_here(M_tina):
                jump tin02_init_liu
            jump liu_button_lobby.tina
        "My account.":

            jump liu_button_lobby.account

        "About my dad..." if not M_anon.finished_state(S_ano28_clue):
            jump liu_button_lobby.father

        "How are you?" if M_anon.finished_state(S_ano14_find):
            if M_anon.finished_state(S_ano28_clue):
                jump liu_button_lobby.upbeat
            jump liu_button_lobby.unsure

        "Sex." if M_anon.finished_state(S_ano28_clue):
            jump liu_button_lobby.suggest
        "I should go.":

            pass

    if M_anon.finished_state(S_ano28_clue):
        anon f_worried "I gotta go."
        liu f_sexy a_sides "Remember, to come by my apartment later, okay?"
        anon f_flirt "Don't worry, I will."
        liu f_happy "See you later then, {b}[firstname]{/b}."
        anon f_normal "Bye, {b}Liu{/b}."
    else:

        anon f_normal "Have a good day."
        liu "Yes, you too."

    hide anon with dissolve
    return


label liu_button_lobby.account:
    anon f_normal "Where can I access my account?"
    liu f_normal "The easiest way is by using one of our ATM machines."
    liu @ a_point_away "In fact, there's one right behind you."
    show anon f_normal_left
    liu "Just there, on the opposite wall."
    anon f_normal "Alright, thanks."
    liu f_worried "No problem."
    jump liu_button_lobby.choice


label liu_button_lobby.anything:
    anon f_confused "Anything?"
    liu "Yes, anything you want!"
    show liu f_sexy o_blush
    with {'master': dissolve}
    liu "I'm yours."
    show anon a_thinking f_thinking
    show liu f_nervous_lipbite
    with {'master': dissolve}
    anon @ -m_talk "Hmm."
    anon "I'll get back to you on that."
    show anon a_idle f_normal
    show liu f_worried -o_blush
    with dissolve
    jump liu_button_lobby.choice


label liu_button_lobby.apartment:
    anon f_worried @ f_confused "Where is your apartment again?"
    liu f_normal "We live over in the {b}Beachside Heights Apartment Complex, room 204{/b}."
    anon f_normal "Oh, right."
    anon "I remember now."
    liu "{b}Kim{/b} usually works late so if you come by in the evening, we'll have plenty of time to snoop around."
    anon "Perfect."
    jump liu_button_lobby.choice


label liu_button_lobby.boss:
    show liu f_nervous_back o_blush with {'master': dissolve}
    liu "Shhhhh, {b}[firstname]{/b}!!!"
    show anon f_normal
    show liu a_cover f_nervous
    with {'master': dissolve}
    liu "We can't do that now!"
    anon "How come?"
    liu "My boss is here..."
    show liu -o_blush
    with {'master': dissolve}
    liu "... she could-"
    anon f_confused "You mean {b}Tina{/b}?"
    liu "Yes!"
    show anon f_normal

    menu:
        "I'm sure she wouldn't mind.":
            jump liu_button_lobby.risky
        "We could ask her to join us?":

            jump liu_button_lobby.threesome
        "Another time then.":

            pass

    anon "It's fine, we can meet up later at your place."
    liu f_worried "Yeah..."
    show liu a_nervous f_worried_down with {'master': dissolve}
    liu "... Except, now the afternoon is going to feel like an eternity!"
    anon f_flirt "Anticipation just makes it better, you know?"
    show liu a_sides f_nervous_lipbite with {'master': dissolve}
    liu @ -m_talk "Ngh."
    pause
    liu f_nervous "Stop teasing me, {b}[firstname]{/b}!"
    anon f_normal "Heh, sorry."
    pause
    anon @ f_thinking -m_talk "( Didn't {b}Liu{/b} mention before that {b}Tina comes in late on Tuesdays{/b}? )"
    jump liu_button_lobby.choice


label liu_button_lobby.father:
    anon f_confused "Are you sure there's nothing else you can tell me?"
    liu f_nervous @ f_nervous_back "I uhh-"
    pause

    if M_anon.finished_state(S_ano14_find):
        jump liu_button_lobby.rump

    anon "Did you know him well?"
    liu "Y-yes, we were-"
    show liu f_worried_down
    pause
    liu f_worried "I mean, no... We were just coworkers."
    liu @ a_holdup "Look, {b}[firstname]{/b}..."
    liu "Your father was a really nice man and I mourn his passing, but I-"
    anon @ -m_talk "..."
    liu "I really don't know anything."
    anon f_worried @ -m_talk "( She's lying. )"
    liu f_worried_down "I wish I did..."
    anon @ -m_talk "( Why won't she tell me? )"
    liu f_worried "It sounds like you and your friend are going through a really rough time right now, and I sympathize, I do."
    liu "I wish there was more I could do for you..."
    anon @ -m_talk "( There has to be something I can do to get her to open up to me... )"
    pause
    anon @ a_thinking f_thinking -m_talk "( ... Maybe I just need to find the right moment? )"
    jump liu_button_lobby.choice


label liu_button_lobby.risky:
    anon "She'd be cool with it."
    show liu a_nervous f_worried_down with {'master': dissolve}
    liu "Yeah, right."
    liu f_worried "I'm finally getting all the perks of this job and you want me risk losing it?"
    anon "{b}Tina{/b} wouldn't fire you over something like that."
    liu f_curious "How can you be sure?"
    show anon a_behind_head f_worried_surprised with {'master': dissolve}
    anon "I uhh..."
    show anon f_worried_left
    pause
    show anon a_sides f_worried with {'master': dissolve}
    liu "See, you don't know for sure!"
    anon f_normal "Well, if you did get fired, it would give us more free time together..."
    show liu a_sides f_happy with {'master': dissolve}
    liu "Haha, very funny."
    liu f_nervous "We really shouldn't, {b}[firstname]{/b}..."
    liu f_worried "... I'm sorry."
    anon "Oh, it's fine."
    anon "I understand."
    liu f_nervous "Why don't you just come over to my place tonight after work?"
    liu f_sexy "I'll make it up to you then."
    anon "Sounds good."
    jump liu_button_lobby.choice


label liu_button_lobby.rump:
    anon f_worried "Please, {b}Liu{/b}... I'm worried what will happen to my friends if this all continues..."
    show liu f_worried
    anon "... Any information is helpful, no matter how small."
    liu "W-well, I know {b}Frank{/b} was contracting some work with {b}Mayor Rump{/b}..."
    anon f_normal "Yeah, I figured that much out myself."
    pause
    anon "Did he ever mention what kind of work it was?"
    show liu f_nervous_back a_cover with dissolve
    anon "Or maybe who else was involved?"
    liu f_nervous "Umm... N-no, I don't think so..."
    anon "Are you sure?"
    liu "It was a while back... A-and my memory isn't so good..."
    anon f_worried @ -m_talk "( She's lying again. )"
    liu a_sides " I'm really sorry, {b}[firstname]{/b}..."
    liu "... I wish I could be more helpful."
    anon f_thinking_down @ -m_talk "( I guess she still doesn't trust me. )"
    anon f_normal "That's okay, {b}Liu{/b}."
    anon "I understand."
    liu f_normal "I'm sure the police will keep your friends safe."
    anon "Yeah, I hope so."
    anon @ -m_talk "( I'll just have to keep playing the waiting game for now... )"
    anon @ -m_talk "( ... And hopefully, another opportunity will present itself. )"
    jump liu_button_lobby.choice


label liu_button_lobby.sex:
    show liu a_mouth_cover f_surprised o_blush with {'master': dissolve}
    liu "What, now?!"
    anon f_happy "Yeah."
    liu a_nervous f_worried "We can't do that, I'm working!"
    show anon f_skeptical with dissolve:
        xoffset -500
        xzoom -1
    pause
    show anon a_point_back f_confused with {'master': dissolve}:
        xoffset 0
        xzoom 1
    anon "Aww, c'mon, there's hardly anyone in here..."
    show liu f_ashamed_down
    pause
    show anon a_sides f_brag with {'master': dissolve}
    anon "... And your boss won't be in until this afternoon, right?"
    liu a_behind f_nervous "Y-yeah."
    anon f_normal "Let's just sneak in the back for a moment..."
    show liu f_nervous_lipbite
    anon "... It'll be worth it, I promise."
    liu f_nervous_lipbite_back @ -m_talk "Ngh."
    pause
    liu f_worried "Okay, but we have to be quick!"
    hide liu with {'master': dissolve}
    anon f_brag "Heh, yeah."
    anon f_happy "\"Quick.\""
    anon f_flirt "Totally."
    hide anon with dissolve

    scene location_bank_office_printer
    show liu b_dressed_kiss_2:
        xoffset 250
    with fade
    liu "Mmm."
    pause
    show anon a_sides f_shy behind liu:
        xoffset 200
    show liu a_close_blouse b_dressed_disheveled f_nervous o_blush:
        xoffset 0
    with {'master': dissolve}
    liu "This is so naughty, {b}[firstname]{/b}!"
    anon f_flirt "Heh, it's about to get a whole lot naughtier."
    anon f_shy_down "Why don't you hop up on that copier?"
    show anon f_flirt
    show liu a_sides f_nervous_down:
        xoffset 475
        xzoom -1
    with {'master': dissolve}
    liu @ -m_talk "Hmm?"
    show liu a_behind f_sexy:
        xoffset 0
        xzoom 1
    with {'master': dissolve}
    liu "Y-yeah, okay."
    show anon f_flirt_low
    show liu a_sides f_nervous_down
    with dissolve
    show liu a_skirt_up_pull2 b_dressed_disheveled_skirt_up f_nervous_lipbite_back with {'master': dissolve}
    anon "Oh my god, you are so sexy!"
    show liu b_dressed_disheveled_skirt_pull_down_panties f_nervous_down with dissolve
    pause
    show anon f_flirt
    show liu a_shy b_dressed_disheveled_skirt_up f_sexy_lipbite
    with {'master': dissolve}
    liu f_sexy "Yeah?"
    anon f_flirt "Go on, get up there."
    show anon a_remove_shorts f_shy_down
    show liu b_dressed_disheveled_jump1 f_nervous_down
    with dissolve
    show anon b_shirt_undress_bottom
    show liu b_dressed_disheveled_jump2 f_nervous_laugh
    with dissolve
    show anon a_sides b_shirt f_flirt od_dick1
    show liu b_dressed_disheveled_printer f_sexy_lipbite
    with dissolve
    pause
    show anon f_surprised_low
    show liu b_dressed_disheveled_printer_open
    with dissolve
    pause
    anon f_flirt_low "That is a beautiful sight!"
    show anon od_dick2
    show liu f_surprised_down
    with dissolve
    show anon od_dick3 with dissolve
    show anon od_dick4 with dissolve
    pause
    liu f_laugh "Hehe!"
    show liu f_sexy_lipbite
    anon f_flirt "Now lay back."

    call scene_liu_sex_office.repeat
    $ unlock_scene('liu', '02_unlocked')

    scene location_bank_office_printer
    show anon a_sides b_shirt f_shy:
        xoffset 200
    show liu a_sides b_dressed_disheveled_after_sex f_ashamed_down

    if _return == 'inside':
        show liu f_sexy

    with fade

    if _return == 'inside':
        liu "My panties are gonna be full of your cum for the rest of the day now..."
        show anon f_shy_low
        show liu f_sexy_lipbite
        anon "Heh, sorry."
        liu f_nervous_down "It's trickling down my thigh..."
        anon f_worried "... You want me to get you some paper towels?"
        liu f_nervous "N-no, I'll take care of it."
    else:

        liu "Is it really noticable?"
        show liu f_nervous_lipbite
        anon f_worried_low "No, not really."
        show anon f_shy
        liu f_nervous "Okay, good."

    show liu a_close_blouse b_dressed_disheveled_skirt_up f_nervous_lipbite
    with dissolve
    pause
    show anon b_shirt_undress_bottom f_looking_down
    show liu b_dressed_disheveled_skirt_pull_down_panties f_nervous_down
    with dissolve
    pause
    show anon a_remove_shorts b_dressed
    show liu a_skirt_up_pull2 b_dressed_disheveled_skirt_up
    with dissolve
    pause
    show anon a_sides f_shy_low
    show liu b_dressed_disheveled_skirt_pull1
    with dissolve
    pause
    show anon f_shy
    show liu a_sides b_dressed_disheveled f_happy
    with {'master': dissolve}
    liu f_happy "Heh, I can barely stand up!"
    show anon a_handshake f_worried
    show liu f_nervous_down
    with {'master': dissolve}
    anon "Are you going to be okay?"
    liu f_happy "Y-yeah, I'll be fine."
    show anon a_sides f_shy
    with {'master': dissolve}
    liu f_sexy "Phew, that was so hot, {b}[firstname]{/b}..."
    liu "... I'm still tingling."
    anon "Heh."
    show anon b_empty f_surprised:
        xoffset 175
    show liu b_dressed_disheveled_hug_surprised behind anon:
        xoffset 175
    with dissolve
    pause .4
    show anon b_empty f_happy_closed
    show liu b_dressed_disheveled_hug
    with dissolve
    pause
    liu "You should probably leave first, so nobody gets suspicious."
    anon @ f_normal_closed "Alright."
    pause
    liu "I'll see you later?"
    anon f_normal_low "Of course."
    show anon b_dressed f_normal behind liu
    show liu a_close_blouse b_dressed_disheveled f_nervous_down:
        xoffset -75
    with dissolve
    pause
    show anon a_wave:
        xoffset 200
    show liu f_nervous o_blush:
        align (0, 0)
        crop (0, 0, 1024, 353)
    show liu a_sides b_dressed as body behind anon:
        align (0, 1.)
        crop (0, 353, 1024, 415)
        xoffset -75
    with {'master': dissolve}
    anon "Have a good day, {b}Liu{/b}."
    liu f_happy "I definitely will."
    hide anon
    show liu f_happy_closed
    show liu a_cover as body
    with dissolve
    pause
    return 'afterglow'


label liu_button_lobby.suggest:
    anon f_flirt "Got a little time for some \"fun\"?"

    if M_tina.where in L_bank.get_all_children_inclusive():
        jump liu_button_lobby.boss

    if game.timer.is_dow(1) and game.timer.is_morning():
        jump liu_button_lobby.sex

    show liu f_worried o_blush with {'master': dissolve}
    liu "Shhhhh, {b}[firstname]{/b}!!!"
    show anon f_normal
    show liu a_hold_arm
    with {'master': dissolve}
    liu "We can't do that now!"
    anon f_confused "How come?"
    show liu -o_blush
    with {'master': dissolve}
    liu "Look around, there are people everywhere, even the security guard is watching!"
    show anon a_surprised f_surprised_left
    with {'master': dissolve}
    liu f_ashamed_down "I'm the only teller on duty right now, so I'd be missed."
    show anon a_sides f_confused_back
    with {'master': dissolve}
    anon @ -m_talk "( When did I see that sleepy guard on duty? {b}Tuesday mornings{/b}? )"
    show anon f_worried
    liu f_worried "Sorry, {b}[firstname]{/b}."
    anon f_shy "Don't worry."
    show liu a_sides f_nervous
    with {'master': dissolve}
    anon "I understand."
    liu "Maybe if we weren't so busy I could-"
    show anon a_wave f_normal with {'master': dissolve}
    anon f_normal "It's okay, {b}Liu{/b}. I can call on you later."
    show anon a_sides with {'master': dissolve}
    liu f_happy "Really?!"
    liu f_sexy "I'd be sure to make it up to you."
    anon f_normal "Sounds good."
    jump liu_button_lobby.choice


label liu_button_lobby.threesome:
    anon f_thinking "Perhaps she could join in?"
    show liu a_mouth_cover f_surprised with {'master': dissolve}
    liu "Oh my gosh, could you imagine?!"
    pause
    show anon f_normal
    show liu a_hold_arm f_nervous o_blush
    with {'master': dissolve}
    liu "I bet she's like a total man eater behind closed doors!"
    show liu f_nervous_lipbite_back
    anon f_happy "Y-yeah, maybe..."
    show liu f_nervous_lipbite
    anon f_normal "... You wanna find out?"
    show liu a_sides f_happy with {'master': dissolve}
    liu "Heh, stop teasing me!"
    show liu f_nervous -o_blush
    with {'master': dissolve}
    liu "{b}Tina{/b} isn't that type of girl."
    anon "If you say so."
    jump liu_button_lobby.choice


label liu_button_lobby.tina:
    anon f_normal "Is Tina around?"
    if game.timer.is_weekend():
        liu f_worried "Sorry, no. She only works on {b}weekdays{/b}."
    else:
        liu f_worried "Sorry, no. She won't be in until later {b}this afternoon{/b}."
    show anon f_worried
    liu f_curious "Is it something I can assist you with?"
    anon "No, no, that's okay."
    liu f_normal "Very well, is there anything else I can do for you today?"
    anon @ f_thinking "Umm..."
    jump liu_button_lobby.choice


label liu_button_lobby.upbeat:
    anon "How are you?"
    liu f_happy "I'm wonderful!"
    show anon f_brag
    liu "Every day seems brighter now that {b}Kim{/b} is gone and you are in my life."
    liu "I'll do anything to make you as happy as you've made me, {b}[firstname]{/b}!"

    menu:
        "Anything?":
            jump liu_button_lobby.anything
        "Your smile is enough.":

            pass

    anon f_happy "Just seeing your beautiful smile is enough to make me happy, {b}Liu{/b}."
    anon "You're a wonderful person and you deserve happiness."
    liu f_nervous "Aww, {b}[firstname]{/b}... You're too good to me."
    show liu f_nervous_back
    pause
    liu f_nervous "Come closer."
    show anon f_confused_low
    show liu b_dressed_lean_whisper f_sexy
    with dissolve
    pause
    show anon b_spook f_confused:
        xoffset 150
    with dissolve
    liu "Why don't you come by my apartment tonight?"
    anon f_surprised "Oh?"
    liu "I'll do a lot more than smile for you..."
    anon f_flirt "{i}*Gulp*{/i} Y-yeah, okay."
    show anon f_shy_high
    show liu a_mouth_cover b_dressed f_laugh
    with {'master': dissolve}
    liu "Hehe!"
    show anon a_sides b_dressed f_shy:
        xoffset 0
    show liu a_idle f_happy
    with dissolve
    jump liu_button_lobby.choice


label liu_button_lobby.unsure:
    anon f_shy "How are you?"
    show liu a_point_self f_surprised o_blush with {'master': dissolve}
    liu "M-me?"
    anon f_normal "Yeah."
    anon "You having a good day?"
    show liu a_cover f_nervous_back with {'master': dissolve}
    liu "Oh, my... I uhh..."
    liu "... Y-yes, I think so."
    anon f_confused "You're not certain?"
    liu f_nervous "N-no, I am, it's just..."
    liu "... I'm not really used to people asking me about my day."
    anon f_surprised "No?"
    pause
    anon f_confused "Not even your husband?"
    show liu a_sides f_ashamed_down -o_blush with {'master': dissolve}
    liu "Oh, definitely not."
    liu "{b}Kim{/b}'s never been much for small talk."
    anon f_thinking_down "Hmm, I see."
    anon a_thinking @ -m_talk "( I guess that shouldn't come as a surprise. )"
    show anon a_sides f_worried
    with {'master': dissolve}
    anon @ -m_talk "( This girl really does deserve much better. )"
    jump liu_button_lobby.choice
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
