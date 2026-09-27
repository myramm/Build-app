label ano28_dink_dink:
    scene expression background(160, 616, 6) as stage
    show erik_overlay_o_boat as boat:
        xzoom -1
    show erik_overlay_o_boat_tarp as tarp:
        xzoom -1
    show erik_overlay_o_boat_bird1 as bird:
        xzoom -1
    anon "Hey, beat it birds!"

    show anon a_shoo f_surprised_low with {'master': fastdissolve}:
        xzoom -1
    anon "Shoo!"

    show erik_overlay_o_boat_bird2 as bird
    with fastdissolve
    show anon f_unimpressed
    show erik_overlay_o_boat_bird3 as bird
    with dissolve
    show anon a_surprised f_thinking
    hide bird
    with {'master': dissolve}
    anon "This boat isn't for you!"

    show anon a_sides with {'master': dissolve}
    erik "Heeeey!!"

    anon f_surprised @ -m_talk "Hmm?"

    show erik a_proud f_angry o_binos with {'master': dissolve}:
        xzoom -1
    erik "What are you doing, dude?!"

    erik f_sad "I was watching those!"

    anon "Huh, watching what?"

    show erik a_sides f_worried with {'master': dissolve}
    erik "The boobies!"

    anon f_confused "B-boobies?"

    erik "The two birds you just chased off!"

    erik "They were a beautiful pair of blue-footed boobies... majestic, really."

    show anon f_surprised
    pause
    anon f_skeptical "Apakah kamu serius saat ini?"

    anon "I can't tell with you sometimes..."

    show erik a_proud f_smug with {'master': dissolve}
    erik "I'm always serious when it comes to boobies, dude."

    anon f_confused "So you really do bird watch?"

    show erik a_sides f_worried with {'master': dissolve}
    erik "Yeah, I told you that..."

    anon "Okay, but I thought that was a euphemism for perving on girls."

    erik f_sad "What? No."

    erik "I really bird watch."

    pause
    erik "Sheesh, man... you make it seem like I'm some aggressive, socially incompetent loser or something..."

    anon f_thinking "aku um..."

    pause
    anon f_worried @ f_confused "... Sorry?"

    erik f_angry "Yeah, you should be sorry."

    erik "Boobies like that don't come along every day, you know?"

    pause
    erik f_normal "What are you doing out here anyways?"

    anon "I found a message from my dad and I think he might have left something here."

    erik f_worried "Seperti apa?"

    anon f_normal "Heh, I don't know... I was just about to check before you started yelling about boobies."

    erik "Oh benar."

    pause
    erik f_normal "Well, don't let me stop you."


    scene location_treehouse_cutscene05 with fade
    anon "It's probably just another dead end... my father wasn't the best at planning-"


    scene
    show screen ano28_dink_dink()
    with fade
    erik "Wah!"

    erik "Apakah itu-"

    call screen empty()
    anon "!!!" with hpunch
    anon "That looks like money!!"

    call screen empty()

    scene expression background(160, 616, 6) as stage
    show erik_overlay_o_boat as boat:
        xzoom -1
    show erik f_surprised_down m_talk o_binos:
        xoffset -175
        xzoom -1
    show anon a_stashed_bag f_shock_down:
        xoffset -175
        xzoom -1
    with fade
    pause
    anon f_surprised "A lot of money!"

    erik f_surprised -m_talk "Is it real?!"

    show anon f_surprised_down
    erik f_surprised_down "Lemme see!"

    show anon a_stashed_bag_show f_surprised_low
    with dissolve
    show anon a_stashed_bag_inside_erik
    show erik a_empty
    with dissolve
    pause
    show anon a_stashed_bag
    show erik a_money
    with dissolve
    erik "Holy crap, dude!!"

    show anon a_stashed_bag_inside f_surprised_down
    show erik f_surprised
    with {'master': dissolve}
    erik "It is real!"

    show anon a_stashed_bag_money
    with {'master': dissolve}
    erik "How much do you think is in there?!"

    anon f_surprised "Entahlah..."

    show anon a_stashed_bag_inside f_surprised_down
    show erik f_surprised_down
    with {'master': dissolve}
    anon "... But these are hundreds, so it's gotta be a lot, right?"

    pause
    show anon a_stashed_bag_show f_surprised_low with {'master': dissolve}
    erik f_normal "I mean, yeah..."

    show anon a_stashed_bag_inside_erik
    show erik a_empty f_normal_down
    with dissolve
    show anon a_stashed_bag_show
    show erik a_sides
    with dissolve
    show anon a_stashed_bag f_surprised
    with {'master': dissolve}
    erik "... I'd say half a million, at least."

    show anon a_stashed_bag_inside f_surprised_down
    with dissolve
    pause
    erik f_normal "You're rich, dude!"

    anon "Hey, there's a note here too."

    show anon b_dressed_pickup
    show erik f_normal_down
    with dissolve
    pause .4
    show anon a_letter_dad b_dressed f_worried_low
    show erik f_nervous
    with dissolve
    pause
    anon "\"{b}[firstname]{/b},\""

    anon "\"I'm so sorry, my son... For everything.\""

    anon "\"There's nothing I can say or do to make up for the mistakes I've made over these last few months.\""

    anon f_sad_down "\"I've put not only my life, but the lives of you and those closest to us at risk\"..."

    anon "... \"And all because I had the poor judgement of entering into a partnership with the wrong people.\""

    show erik f_sad
    pause
    anon f_worried_low "\"I won't ask for your forgiveness because I know I don't deserve it\"..."

    anon "... \"But I hope that one day you'll at least understand why I had to keep all of this from you.\""

    anon f_sad_down "\"There's nothing in this world more important than family, son.\""

    anon "\"My biggest regret in all of this is that I won't be around to see you start one of your own\"..."

    anon "... \"Or walk {b}[jen_name]{/b} down the aisle.\""

    anon @ f_sad_smile_down -m_talk "{i}*Mengendus*{/i}"

    anon "... \"Or grow old with {b}[deb_name]{/b}.\""

    anon "\"They're your responsibility now.\""

    anon f_worried_low "\"I believe you'll do a better job than I ever could\"..."

    anon "... \"And hopefully this money will help.\""

    pause
    anon f_sad_down "\"You are my legacy, son.\""

    anon @ f_sad_smile_down -m_talk "{i}*Mengendus*{/i}"

    anon "\"My greatest gift.\""

    anon "\"I'm so very proud of the man you've become.\""

    anon @ f_sad_smile_down -m_talk "{i}*Mengendus*{/i}"

    anon "\"I will always be there, watching over you.\""

    pause
    anon "\"With all the love in my heart, {b}Dad{/b}.\""

    show anon a_letter_dad_wipe
    show erik f_surprised
    with {'master': dissolve}
    anon @ -m_talk "{i}*Mengendus*{/i}"

    show erik a_shoulder_anon:
        xoffset 1
    with {'master': dissolve}
    erik "Jesus, dude..."

    show anon f_sad a_letter_dad
    show erik f_sad
    with {'master': dissolve}
    anon "Y-ya."

    erik "I know that wasn't exactly the goodbye you wanted..."

    erik "... But it was pretty good."

    show anon a_letter_dad_wipe with {'master': dissolve}
    anon "{i}*Sniff*{/i} Yeah, it was."

    show anon a_letter_dad f_sad_down
    show erik f_sad_down
    with {'master': dissolve}
    erik f_sad_down "I mean, I'd kill to hear something like that from my dad..."

    pause
    erik f_nervous "... Should I like, hug you or-"

    anon f_worried "Heh, no... that's alright."

    show anon a_sides f_shy
    with {'master': dissolve}
    anon "Thanks, though... I appreciate the sentiment."

    erik f_shy "No problem, dude."

    show erik a_sides:
        xoffset -175
    with dissolve
    pause
    erik "So, ehh... what are you gonna do with the money?"

    show anon b_dressed_pickup
    show erik f_normal_down
    with dissolve
    show anon a_stashed_bag b_dressed f_normal
    show erik f_normal
    with dissolve
    anon "Well, I'll probably start by paying off {b}[deb_name]{/b}'s debt at the bank."

    show anon a_backpack f_looking_down
    show erik f_normal_down
    with dissolve
    pause
    show anon a_sides f_thinking
    show erik f_normal
    with {'master': dissolve}
    anon "And I should probably give some to {b}Liu{/b}."

    anon "She definitely needs it now that she's on her own."

    show anon f_confused
    erik f_nervous "Who's {b}Liu{/b}?"

    anon f_worried "She's the teller who's been helping me."

    anon "My dad and her were close, before he died."

    erik f_normal "Oh."

    erik "Well, yeah... that sounds llke a nice thing to do."

    show anon f_shy
    pause
    erik "Just make sure you keep enough for tuition next year."

    anon f_normal "Man, did you see how much is in here?!"

    anon "I'll have plenty left over."

    show anon behind erik:
        xoffset 400
        xzoom 1
    show erik:
        xoffset 0
    with {'master': dissolve}
    erik "You should buy a boat."

    show anon f_confused_back:
        xoffset 450
    show erik:
        xoffset 75
    with {'master': dissolve}
    anon "I have The Dink."

    show anon:
        xoffset 500
    show erik f_smug:
        xoffset 150
    with {'master': dissolve}
    erik "No, I mean like a yacht!"

    show anon:
        xoffset 550
    show erik:
        xoffset 225
    with {'master': dissolve}
    erik "You know, one of those big luxury ones."

    show anon f_thinking:
        xoffset 600
    show erik f_smile_dumb:
        xoffset 300
    with {'master': dissolve}
    anon "I can just go hang out on {b}Mayor Rump{/b}'s."

    hide anon
    show erik:
        xoffset 375
    with dissolve
    pause .4
    erik f_surprised "Wait, what?!" with hpunch
    erik "You've been on {b}Mayor Rump{/b}'s yacht?!"

    anon "Heh, {b}Iwanka{/b} took me there."

    erik "Diam!"

    anon "aku serius."

    hide erik with {'master': fastdissolve}
    erik "Tell me everything, immediately!"

    anon "Haha!"


    scene expression background(o=1) as stage with longfade
    show anon f_surprised with dissolve
    anon @ -m_talk "( Wow, {b}Dad{/b} really did take money off the Russian Mafia. )"

    pause
    anon f_normal @ -m_talk "( {b}I should take it to Liu{/b} and surprise her with her portion. )"

    anon @ -m_talk "( She can probably sort out {b}[deb_name]{/b}'s debt and deposit the rest in my bank account for me too. )"

    hide anon with dissolve
    return


label ano28_dink_dink.late:
    scene expression background() as stage
    show anon f_worried with dissolve
    anon @ -m_talk "( Nah, it'll be dark soon. )"

    anon @ -m_talk "( {b}Better to come back tomorrow{/b} when I can actually see what I'm meant to be searching for. )"

    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
