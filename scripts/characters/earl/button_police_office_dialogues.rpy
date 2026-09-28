label earl_police_office_dialogue_roxxy_ask_earl_release:
    show earl
    show old_roxxy 1of at Position (xpos=400)
    show player 10 at left
    with dissolve
    player_name "Excuse me, sir?"
    show player 5
    earl "Huh?"
    earl "What are you kids doing here?"
    show earl f_eat a_donut_eat with dissolve
    show player 10
    player_name "We're just trying to get some information about an arrest you guys made earlier today."
    show player 5
    show earl f_normal a_idle with dissolve
    earl "Hmm, you're {b}Crystal{/b}'s daughter, aren't you?"
    show old_roxxy 1jf
    roxxy "..."
    show player 10
    player_name "Yes, she is, sir."
    player_name "Could you tell us what's happening?"
    show player 5
    earl "I'm afraid I'm not allowed to discuss these matters with anyone other than her family."
    earl "If you want to come with me, miss. I'll fill you in on how this all works."
    show player 10
    player_name "... Yeah, alright. I'll just wait over-"
    show player 11
    show old_roxxy 2c at Position (xpos=500) with dissolve
    roxxy "No!"
    show old_roxxy 2cf at Position (xpos=434)
    with dissolve
    roxxy "... I mean."
    show old_roxxy 33f at Position (xpos=400) with dissolve
    roxxy "I want him to stay. It's alright."
    show old_roxxy 32f
    show player 13
    earl @ -m_talk "..."
    earl "You're sure?"
    show old_roxxy 33f
    roxxy "Yeah."
    show old_roxxy 32f
    earl "Suit yourself."
    earl "We got an anonymous tip this morning regarding a large stash of drugs at your residence."
    earl "So we drove on over to have a look."
    earl "Were you aware that your mother had over a pound of crystal methamphetamine stashed under the couch?"
    show old_roxxy 1if
    show player 23
    player_name "A pound?!"
    show player 22
    show old_roxxy 27f at Position (xoffset=67)
    roxxy "..."
    earl "I'm afraid so."
    earl "That's a felony drug charge."
    earl "We're holding your mother for possession with intention to sell."
    show old_roxxy 33bf at Position (xoffset=34) with dissolve
    roxxy "..."
    show player 10
    player_name "That's not good."
    show player 5
    show old_roxxy 1jf with dissolve
    earl "No, son. It certainly isn't."
    earl "... Now, I've known {b}Crystal{/b} for a long time."
    earl "We went to school together back in the day."
    earl "She's always been good at getting herself into trouble..."
    earl "... But after questioning her this morning, I can tell you without a doubt that she doesn't know the first thing about cooking meth."
    earl "Now, she claims she made it all herself and was looking to move it..."
    earl "... But I'd bet good money that she was just holding it for somebody else!"
    roxxy "..."
    earl "Unfortunately, unless I get proof. She's going to wind up in prison for a very long time."
    show old_roxxy 33bf at Position (xoffset=34) with dissolve
    roxxy "{i}*Sniff*{/i}"
    show player 10
    player_name "Okay, well, what about my friend's home?"
    show old_roxxy 1jf with dissolve
    show player 5
    earl "Oh, the trailer?"
    earl "... Well, if {b}Crystal{/b} gets convicted, it'll be repossessed by the state and sold off."
    show player 25
    player_name "Sheesh..."
    show player 12
    player_name "Is there anything we can do to prevent that?"
    show player 5
    earl "Not unless you can convince {b}Crystal{/b} to give up whoever she's protecting..."
    roxxy "..."
    show player 11
    player_name "..."
    show player 5
    earl "I'm real sorry about how this all went down, miss."
    roxxy "{i}*Sniff*{/i}"
    earl "You all can {b}go down to the cells and visit her{/b} if you'd like."
    earl "They should be done questioning her by now."
    show player 14
    player_name "Alright, thanks for the information, Officer."
    show player 13
    hide earl with dissolve
    pause
    show player 5
    show old_roxxy 33bf
    roxxy "... {i}*Sniff*{/i} All of this for that inbred idiot..."
    show old_roxxy 1j with dissolve
    show player 10
    player_name "C'mon, let's go and talk to your mom."
    hide player
    hide old_roxxy
    with dissolve
    return

label earl_police_office_dialogue_first_visit:
    show earl
    show player 11 at left
    with dissolve
    earl "Whatchu doing in here?!"
    earl @ f_eat a_donut_eat "Is it another one of those \"bring your kids to work\" days?"
    show player 14
    player_name "Oh, no, I'm just passing by, sir."
    player_name "I wanted to speak with {b}Harold{/b}."
    show player 1
    earl "Wait a minute... Don't you go to school with my daughter?"
    show earl f_eat a_donut_eat with dissolve
    show player 14
    player_name "Oh, right! You're {b}Ronda{/b}'s dad!"
    show earl a_idle f_normal
    show player 1
    earl "Shiiiiiiiiiiieeeeeet!"
    show player 11
    earl "You better watch yourself around my baby girl, or I'll have to put surveillance on {b}you{/b}."
    show earl f_annoyed
    earl "Got it?!"
    show player 29
    player_name "Uhh... Of course, sir!"
    player_name "I would never-"
    show player 13 at left
    earl f_normal @ f_laugh "Relax, I'm just messing with ya! Move along now."
    return

label earl_police_office_dialogue_pre:
    show earl
    show player 1 at left
    with dissolve
    earl "Hey, what's up?"
    return

label earl_police_office_dialogue_donuts:
    show earl
    show player 14
    player_name "This might seem like a silly question, but what kind of donuts does {b}Harold{/b} like?"
    show player 1
    earl @ f_laugh "Hah!"
    earl "{b}Harold{/b} only eats them if they're {b}[harold_glaze]{/b}..."
    earl @ f_eat a_donut_eat "... But I ain't sure what else he puts on them."
    show player 14
    player_name "I see."
    show player 11
    earl "Why do you ask?"
    show player 17
    player_name "Oh, no reason."
    show player 11
    earl f_annoyed "Wait, shouldn't you be at school? What are you doing here-"
    show player 14
    player_name "Errr..."
    show player 17
    player_name "Thanks, bye!"
    return

label earl_police_office_dialogue_harold:
    show player 10
    player_name "Do you know where {b}Harold{/b} could be?"
    player_name "I need to err... Return something to him!"
    show player 11
    show earl f_normal
    earl "I'm not sure where he went, but I saw him yesterday in the office..."
    earl "He looked in a bad shape, that's for sure!"
    earl "For a second I thought he was quitting..."
    earl "... So I told him to take some time off."
    show player 12
    player_name "Did he mention where he would be while off duty?"
    show player 5
    earl "I didn't want to ask too many questions, you know?"
    earl "Sometimes guys just need some alone time..."
    show player 14
    player_name "Alright, thanks."
    return

label earl_police_office_dialogue_roxxys_mom:
    show earl
    show player 12
    player_name "Where can we speak with my {b}friend's mom{/b} again?"
    show player 5
    earl "She's {b}downstairs in a cell{/b}."
    earl "Officer {b}Yumi{/b} is down there, but she'll give you all some privacy to talk."
    show player 14
    player_name "Alright, thanks."
    return

label earl_police_office_dialogue_leave:
    show player 14
    player_name "Just passing by, sir."
    show player 1
    earl "Alright then."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
