label school_erik_intro_started:
    scene expression player.location.background_blur
    show mia
    with None
    show erik:
        flip
        xoffset 150
    show anon:
        xoffset -100
    with {'master': dissolve}
    anon @ a_wave "Hei, {b}Mia{/b}!"

    mia "Hey, {b}[firstname]{/b}! Glad to see you're back!"

    mia "Hi, {b}Erik{/b}! How was your weekend?"

    erik @ f_worried_down "I mostly stayed in my room..."

    mia @ f_laugh "That's cool. Sometimes I like alone time too!"

    mia "What about you, {b}[firstname]{/b}? What have you been up to?"

    show erik f_bored_right
    anon f_sad_down "Well, I'm not sure if you've heard or not, but my dad passed away. So I've been dealing with that..."

    show erik f_bored
    mia f_worried "Oh yeah. I heard from my mom..."

    mia "I didn't mean to bring it up. I'm sorry you had to go through that. I'm just glad you're finally back!"

    show erik f_bored_right
    anon f_normal "Thanks. I'll be fine. Don't worry."

    show erik f_bored
    mia f_normal "Listen, I was looking for someone to {b}help me get ready for the final exams{/b}, so..."

    show anon f_surprised
    mia "... If you're interested, let me know!"

    show erik f_bored_right
    anon f_shy a_behind_head "Uhh, sure... I guess?"

    anon "Where do you want to meet? The library?"

    show erik f_bored
    show anon f_normal a_pocket with {'master': dissolve}
    mia f_worried "Umm, I'd have to ask my parents, first."

    mia "They probably won't let me, though."

    mia "I'm not really allowed to stay late after school or see friends outside of my house."

    show erik f_bored_right
    anon @ f_surprised "Really?! That sucks!"

    show erik f_bored
    mia @ f_laugh "Yeah... Heh, heh."

    mia "Anyway, it'd be easier if you just came over to my house to study..."

    mia f_normal @ f_laugh "You know where I live, so just drop by whenever you want!"

    mia "I'd better get going. Science class is starting soon!"

    mia "{b}Professor Okita{/b} said today's laboratory experiment will be challenging."

    mia "That means it's probably gonna to take the entire hour to complete."

    erik f_worried "Ugh. Don't remind me..."

    mia "Talk to you later guys!"

    hide mia with dissolve
    hide anon
    hide erik
    with {'master': dissolve}
    return

label school_erik_how_you_doin:
    scene expression player.location.background_blur
    show erik with dissolve
    erik "Hai, {b}[firstname]{/b}!"

    show anon f_tired with dissolve
    anon "Oh... Hey..."

    erik "How was your first day back at school?"

    anon @ a_facepalm "Ugh... I don't even want to talk about it."

    erik f_worried "begitu..."

    erik "What are you up to now?"

    anon f_thinking "Well, I told {b}[deb_name]{/b} that I would visit her friend {b}Diane{/b}."

    anon f_normal "She's gonna pay me to do some work for her."

    erik f_sad "Man... I wish I had a job..."

    erik @ f_laugh "A job where I could just sit at my computer playing games all day, heh..."

    show erik f_normal
    anon f_worried @ a_point "Oh, speaking of computers... Mine is definitely broken."

    anon "I think I need to {b}replace some parts in it{/b}, or something..."

    anon f_normal "You know any good stores where I could buy some?"

    erik "Hmmm... I usually {b}shop for parts at Consum-R in the mall{/b}."

    erik "They sell lots of things for a reasonable price."

    anon "Alright then, I'll check it out!"

    erik @ f_laugh "Sampai jumpa lagi!"

    hide erik
    hide anon
    with dissolve
    return

label school_mrsj_cupid_ready:
    scene expression L_school_front.background_blur
    show player 17 with dissolve
    player_name "I should tell {b}Erik{/b} the good news!"

    player_name "He's going to be so excited about this!"

    show player 14
    player_name "{b}June{/b} seems like the perfect kind of girl for him!"

    hide player with dissolve
    return

label school_june_date_ready:
    scene expression L_school_front.background_blur
    show player 10 with dissolve
    player_name "I should probably tell {b}Erik{/b} that it's not going to work out with {b}June{/b}..."

    player_name "... And that I might spend time with her."

    player_name "He's going to be upset."

    hide player with dissolve
    return

label school_dewitt_glue_mission:
    scene expression L_school_front.background_blur
    show player 32f with dissolve
    player_name "( Where the heck is {b}Erik{/b}? )"

    player_name "( He should have been here by now... )"

    show player 31f
    show old_erik 5 at right with dissolve
    erik "{b}[firstname]{/b}?"

    show old_erik 52
    show player 10 at left with dissolve
    player_name "Itu dia!"

    player_name "What took you so long?"

    show player 5
    show old_erik 4
    erik "Sorry, dude! I was pillaging an Orcette village and I kinda lost track of time..."

    show old_erik 1
    show player 12
    player_name "... Hah?"

    player_name "Is that a video game thing?!"

    show player 5
    show old_erik 5
    erik "... Ya."

    show old_erik 1
    show player 37 with dissolve
    player_name "..."
    show player 38 with dissolve
    player_name "Let's just focus on the mission, {b}Erik{/b}."

    show player 5 with dissolve
    show old_erik 5
    erik "What is our mission anyways?"

    show old_erik 52
    show player 239_240 with dissolve
    pause
    show player 618 at Position (xoffset=35) with dissolve
    player_name "We gotta {b}break into Mrs. Smith's office, and apply this adhesive solution to her office chairs{/b}."

    show player 617 at Position (xoffset=35)
    show old_erik 5
    erik "Is that the same stuff we made in {b}Miss Okita{/b}'s class a while back?"

    show old_erik 52
    show player 618 at Position (xoffset=35)
    player_name "Yeah. {b}Kevin{/b} made it for me."

    show player 617 at Position (xoffset=35)
    show old_erik 5
    erik "That stuff is crazy strong!"

    erik "... And you want to put it on {b}Mrs. Smith{/b}'s chairs?"

    erik "Won't she get stuck?"

    show old_erik 52
    show player 17 with dissolve
    player_name "Heh, that's kind of the point, dude."

    show player 13
    show old_erik 3b
    erik "Oh benar."

    show old_erik 3c
    pause
    show old_erik 3b
    erik "Well, lead the way I guess..."


    scene outside_school_night02a
    show text _ ("The school was locked down tight but I was determined to find an entry point somewhere.\nPerhaps one of these main floor windows would do the trick?") as caption
    with fade
    pause

    scene outside_school_night02b
    show text _ ("{b}Erik{/b} was not the ideal partner for a stealth mission but I was still glad to have him along.\nThere's no way I could have managed this without him.") as caption
    with fade
    pause

    scene outside_school_night02c
    show text _ ("As {b}Erik{/b} helped me through the window I couldn't help but feel like this had all been too easy...\n... There was certainly something ominous about the school tonight.") as caption
    with fade
    pause

    $ playMusic()
    scene black with dissolve
    pause 0.5
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
