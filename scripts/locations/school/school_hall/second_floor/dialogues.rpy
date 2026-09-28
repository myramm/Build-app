label second_floor_first_visit:
    scene expression player.location.background_blur with None
    show anon
    show kevin b_apron a_pot
    with {'master': dissolve}
    kevin "Whoa, {b}[firstname]{/b}?!"
    kevin "When did you get back?"
    anon @ a_wave "Hey, {b}Kevin{/b}."
    anon "Today's my first day."
    kevin "Right on, bro."
    kevin f_bro a_pot_brofist "Good to see you!"
    show anon f_surprised a_handshake with {'master': dissolve}
    pause
    show anon f_shy a_behind_head
    show kevin f_skeptical a_pot_head
    with {'master': dissolve}
    kevin "Sorry about your dad by the way..."
    anon a_idle f_worried "Yeah, thanks."
    pause
    anon f_normal "What's with the apron?"
    kevin a_pot f_sad "Ugh, {b}Mrs. Smith{/b} put me on cafeteria duty until I raise my grade in {b}Miss Okita{/b}'s class..."
    anon f_surprised "You're failing science?"
    kevin "Well, I'm not failing yet but it definitely isn't looking good, bro."
    anon f_worried "That sucks man."
    kevin "Tell me about it!"
    kevin "I haven't had a good workout in weeks!"
    anon f_normal "Oh, yeah?"
    anon "Still hanging out down at that gym?"
    kevin @ f_laugh "You know it, bro!"
    kevin a_pot_flex f_normal "I can't let these guns go unpolished, can I?"
    anon "Heh, no, I guess not..."
    kevin a_pot "Oh, that reminds me!"
    kevin "We got that new Muay Thai trainer there."
    kevin "His name is {b}Master Somrak{/b}."
    kevin "He's like a grandmaster or something, with all his ancient teachings..."
    kevin "It's pretty awesome!"
    anon f_confused "Muay Thai?"
    kevin "Yeah, bro!"
    kevin "You know, like, kickboxing and stuff."
    anon f_normal "Really?"
    kevin "You should go in there and check it out!"
    anon f_shy a_behind_head "Oh, I dunno..."
    kevin "C'mon, bro!"
    kevin "You gotta get that body in shape."
    kevin "The people demand beefcake, not sweet cake!"
    anon f_worried a_idle "Eh?"
    anon "I guess I could check it out..."
    show anon f_normal with {'master': dissolve}
    kevin @ f_laugh "That's the spirit, bro!"
    kevin "Who knows, you might even be able to whoop {b}Dexter{/b}'s ass once you've got a few classes under your belt."
    anon "Psh, yeah right."
    pause
    anon "I should get going, man."
    anon "{b}Mrs. Smith{/b} is waiting on me upstairs {b}in her office{/b}."
    kevin "Oh shit, bro... I didn't know that!"
    kevin "You better hurry on then before you end up in the cafeteria with me."
    anon @ a_wave "See ya, {b}Kevin{/b}."
    kevin "{b}Come by the cafeteria later{/b}, and we can hang."
    anon "Alright."
    hide anon
    hide kevin
    with {'master': dissolve}
    return

label second_floor_okita_dose_smith:
    scene expression game.timer.image("backgrounds/location_school_second{}_blur.jpg")
    show player 35
    player_name "Hmm, I think {b}Mrs. Smith{/b} goes into the {b}teachers' lounge to drink coffee in the afternoons{/b}."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
