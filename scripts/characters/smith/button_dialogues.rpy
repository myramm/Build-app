label smith_button_teachers_lounge:
    show player 22 at left
    show principal 33 at right
    with dissolve
    player_name "( Oh crap! {b}Mrs. Smith{/b} is in here! )"
    show player 11
    show principal 31 with dissolve
    player_name "( ... )"
    show principal 32
    smith "{b}[firstname]{/b}?"
    smith "What in the world are you doing in the teachers' lounge?!"
    show player 10
    show principal 31
    player_name "I was just-"
    show player 11
    show principal 32
    smith "Students are not allowed to be in here!"
    smith "Get back to your class immediately or I'll have you expelled!"
    show player 10
    show principal 31
    player_name "Y-yes, ma'am!"
    return

label smith_button_eve_school_dress_code:
    show smith
    show anon f_worried
    with dissolve
    anon "E-excuse me, {b}Mrs. Smith{/b}?"
    smith "What are you doing in here?!"
    anon "I really need to speak with you."
    smith "About what?!"
    smith "I'm a very busy woman, you know?!"
    anon "Y-yes, I know."
    pause
    smith "Well, hurry up then, out with it!"
    anon "It's about the new dress code policy..."
    smith f_confused "Dress code policy?!"
    pause
    anon "Yes, {b}Annie{/b} said you were instituting a new policy and-"
    smith f_normal "Oh, that."
    smith "I put the girl in charge of that, it's her project."
    anon "B-but she told me to come talk to you!"
    anon "The new policy prohibits hair dye, you see... And one of my friends is-"
    smith @ f_eyeroll "Tsk, I don't wanna hear about it!"
    smith "I told {b}Annie{/b} that she could do as she pleases so long as it doesn't cause me a hassle..."
    smith f_angry "Are you in here to cause a hassle?!"
    anon "I-"
    smith "Because I'm more than happy to give you detention for pestering me with these minuscule problems!"
    anon f_surprised "N-no, ma'am!"
    anon "I wasn't-"
    smith "Good!"
    smith f_scream "Now get out!"
    anon f_sad_down @ -m_talk "..."
    hide anon with dissolve
    $ player.go_to_previous()
    scene expression player.location.background_blur
    show anon f_sad_down
    with fade
    anon @ -m_talk "( {i}*Sigh*{/i} Well, that could have gone better. )"
    anon @ -m_talk "( How am I supposed to fix this now? )"
    anon @ -m_talk "( There's no way I'll get {b}Annie{/b} to change it and {b}Mrs. Smith{/b} doesn't seem to care... )"
    show anon f_thinking a_thinking with dissolve
    pause
    anon @ -m_talk "( Hmm, I wonder if any of the teachers would help me? )"
    anon f_grin a_idle "( I should {b}ask them{/b}! )"
    hide anon with dissolve
    return

label smith_button_intro:
    show anon f_worried
    show smith:
        xoffset -100
    show annie:
        xoffset 100
    with {'master': dissolve}
    anon "You wanted to see me, {b}Mrs. Smith{/b}?"
    smith "Indeed, {b}[firstname]{/b}."
    smith "We need to discuss your grades and whether or not you intend to graduate."
    anon f_surprised "It's really that bad?"
    smith a_grades "Have a look for yourself..."
    show screen school_locker_report()
    anon a_surprised f_shock "( !!! )" with hpunch
    pause
    hide screen school_locker_report with {'master': dissolve}
    show smith a_idle with {'master': dissolve}
    anon a_rub f_worried "Oh man, I'm failing everything?!"
    smith "I told you..."
    annie f_annoyed "That's what happens when you skip school for a month!"
    anon a_sides "I wasn't skipping! My dad died!"
    smith a_hips @ f_eyeroll "Be silent, {b}Annie{/b}!"
    annie @ f_curious "S-sorry, ma'am."
    show annie f_normal
    smith "... Regardless of the circumstances."
    smith "You'll need to {b}find a way to raise these grades{/b} if you don't want to repeat next year."
    smith "I'd suggest you {b}speak to your teachers{/b} about making up the work you've missed."
    smith "Perhaps they can come up with some extra credit assignments or something?"
    anon a_idle "Y-yeah, okay."
    smith "Do whatever it takes!"
    anon "Yes, ma'am."
    smith "Good, now get to class."
    anon f_shy "... Actually, ma'am?"
    smith "Yes?"
    anon "I forgot the combination to my locker. Can you help me get it open?"
    show smith f_confused
    annie f_angry "What do you mean you forgot?!"
    show anon f_surprised
    annie "Everyone was told at the beginning of the year to write down their combinations!"
    anon f_shy "I umm..."
    anon "I lost it!"
    annie f_normal @ f_gross "Pfft, typical."
    smith f_normal "That's very disappointing, {b}[firstname]{/b}."
    smith "We'll have to get you a new lock."
    anon @ -m_talk "..."
    smith "I'll send {b}Annie{/b} down with her master key momentarily..."
    smith "I suggest you get everything that you need out now."
    smith "It could be a while before the new lock arrives."
    anon f_normal "Yes, ma'am."
    smith "Head there now and then get your butt to class after you're finished!"
    return

label smith_button_go_to_locker:
    show anon f_surprised
    show smith:
        xoffset -100
    show annie f_angry:
        xoffset 100
    with {'master': dissolve}
    annie "Didn't {b}Mrs. Smith{/b} tell you to beat it?!"
    annie f_normal "{b}Head down to your locker{/b} and I'll meet you momentarily!"
    return

label smith_button_get_out:
    show player 11 at left
    show principal 1 zorder 0 at Position(xpos=0.65, ypos=1.0)
    with dissolve
    smith "What are you doing?"
    show principal 2
    smith "Get the hell out of my office!" with hpunch
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
