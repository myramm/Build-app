label girls_lockerroom_judith_in_girls_bathroom:
    scene girl_lockerroom
    show player 106 at left with dissolve
    player_name "Woah! There's a big hole in the ground in here..."
    player_name "( No wonder they had to close this locker room! )"
    show player 90
    player_name "..."
    show player 10
    player_name "( I can still hear sobbing. )"
    player_name "( There's definitely {b}someone in here{/b}... )"
    hide player 10 with dissolve
    return

label girls_lockerroom_judith_toilet_first_intro:
    scene expression game.timer.image("backgrounds/location_school_locker_room_broken_stall{}.jpg")
    show old_judith 11 zorder 1 at Position( xpos = 310, ypos = 768) with dissolve
    window hide
    pause
    show player 106f zorder 0 at Position (xpos = 639, ypos = 768) with dissolve
    player_name "!!!"
    judith "{i}*Sobbing*{/i}"
    show player 108
    player_name "{b}Judith{/b}?!"
    show old_judith 13
    show player 109
    judith "... Hey, {b}[firstname]{/b}."
    show old_judith 12
    show player 108
    player_name "Are you okay?"
    show old_judith 13
    show player 109
    judith "I just wanted to stay away, from everyone."
    show old_judith 12
    show player 108
    player_name "What do you mean?"
    show old_judith 13
    show player 109
    judith "No one likes me... And everyone makes fun of my body..."
    judith "... So at least in here I won't be made fun of."
    show old_judith 12
    show player 108
    player_name "You can't let these people get to you that way!"
    show old_judith 13
    show player 109
    judith "They're right, though. I am ugly..."
    return

label girls_lockerroom_judith_toilet_first_not_ugly:
    show player 111
    show old_judith 12
    player_name "I don't think you're ugly at all!!"
    show old_judith 15
    show player 110
    judith "... Really?"
    show old_judith 14
    show player 111
    player_name "Yeah!"
    player_name "I think you look good!"
    show old_judith 15
    show player 110
    judith "That's... The nicest thing anyone has said to me..."
    show old_judith 14
    show player 111
    player_name "Well, I'm just being honest... And I'm sure I'm not the only one!"
    player_name "You just have to ignore all the negative stuff at school."
    show old_judith 15
    show player 110
    judith "I guess you're right..."
    show old_judith 14
    show player 111
    player_name "Anyway, we should get out of here and get back to class."
    show old_judith 17
    show player 106f
    judith "Wait!!"
    judith "Stay here a little longer... With {b}me{/b}..."
    return

label girls_lockerroom_judith_toilet_first_ok:
    show old_judith 16
    show player 111
    player_name "Oh... Okay."
    show old_judith 17
    show player 110
    judith "Do you remember the other day when..."
    judith "... We were both in the locker room? In front of {b}Annie{/b}?"
    show old_judith 16
    show player 111
    player_name "Yeah?"
    show old_judith 17
    show player 110
    judith "Well, I... I liked the way you looked at me."
    show old_judith 16
    show player 106f
    player_name "!!!"
    show old_judith 17
    judith "It wasn't just your eyes... Your body was also reacting."
    show old_judith 16
    player_name "..."
    show old_judith 17
    judith "Was it my breasts that made you... So happy... {i}Down there{/i}?"
    show old_judith 16
    show player 111
    player_name "I... I'm sorry!"
    show old_judith 17
    show player 106f
    judith "Don't be sorry!!"
    judith "... I really liked it and..."
    judith "... I was wondering If I could, you know, see it again?"
    return

label girls_lockerroom_judith_toilet_first_sure:
    show old_judith 16
    show player 111
    player_name "I guess so..."
    show old_judith 17
    show player 106f
    judith "Let me do it."
    hide player
    show old_judith 18 at Position(xpos = 447, ypos = 768)
    player_name "!!!"
    show old_judith 19
    window hide
    pause
    show old_judith 20
    window hide
    pause
    show old_judith 21
    window hide
    pause
    show old_judith 22
    window hide
    pause
    show old_judith 24
    judith "It's so... Nice..."
    judith "... And thick."
    show old_judith 23
    player_name "{i}*Gasp*{/i}"
    show old_judith 24
    judith "I just love how it feels in my hand..."
    show old_judith 25_23
    pause 4
    judith "..."
    show old_judith 23
    judith "Would you like to touch my breasts?"
    return

label girls_lockerroom_judith_toilet_first_yes:
    player_name "Yeah! I'd love to..."
    show old_judith 33
    player_name "..."
    show old_judith 34
    player_name "Wow..."
    show old_judith 35
    judith "Go ahead!"
    judith "Touch them... But be gentle! They're really sensitive..."
    show old_judith 36_37_38
    pause 4
    show old_judith 39 with hpunch
    judith "{i}*Moan*{/i}"
    player_name "!!!"
    show old_judith 33
    judith "It's just too much. My body gets all fuzzy when you touch my nipples..."
    show old_judith 4f zorder 1 at Position( xpos = 310, ypos = 768)
    show player 112 zorder 0 at Position (xpos = 639, ypos = 768)
    player_name "I didn't mean to hurt you."
    show player 13f
    show old_judith 5f
    judith "No, it's fine! It felt really good... I'm just sensitive..."
    show old_judith 4f
    show player 10f
    player_name "Maybe we should stop..."
    show player 13f
    show old_judith 5f
    judith "Yeah... Thanks for staying with me, I feel much better..."
    show old_judith 2f
    judith "... And if you want, we could do this again, some time..."
    show old_judith 4f
    show player 17f
    player_name "I'd like that!"
    show old_judith 5f
    show player 13f
    judith "I'll see you later then."
    hide player
    hide old_judith
    with dissolve
    return

label girls_lockerroom_judith_toilet_first_should_stop:
    show old_judith 24
    player_name "I think we should stop..."
    show old_judith 6f zorder 1 at Position( xpos = 310, ypos = 768)
    show player 112 zorder 0 at Position (xpos = 639, ypos = 768)
    player_name "We can't be late for class and {b}Annie{/b} could see us in here..."
    show player 13f
    show old_judith 2f
    judith "I understand. Thanks for staying with me..."
    show old_judith 3f
    judith "... And if you want, we could do this again, some time..."
    show old_judith 4f
    show player 17f
    player_name "I'd like that!"
    show player 13f
    show old_judith 5f
    judith "I'll see you later then."
    return

label girls_lockerroom_judith_toilet_first_cant:
    show old_judith 16
    show player 108
    player_name "I can't do that right now, {b}Judith{/b}..."
    player_name "Also, we should really go... I don't want to be late and {b}Annie{/b} could see us in here..."
    show old_judith 13
    show player 109
    judith "Oh..."
    judith "You can go, then. I'll stay here a little bit longer I think..."
    show player 111
    show old_judith 14
    player_name "Alright, I'll see you later then."
    return

label girls_lockerroom_judith_toilet_should_leave:
    show old_judith 16
    show player 108
    player_name "We should really go... I don't want to be late and {b}Annie{/b} is already on my case..."
    show old_judith 13
    show player 109
    judith "Oh..."
    judith "You can go, then. I'll stay here a little bit longer I think..."
    show old_judith 14
    show player 111
    player_name "Alright, I'll see you later then."
    return

label girls_lockerroom_judith_toilet_first_ugly:
    show old_judith 12
    show player 108
    player_name "I know, but you have to learn to deal with it!"
    show player 109
    judith "..."
    show old_judith 11
    judith "{i}*Sobbing*{/i}"
    show player 108
    player_name "I'm sorry..."
    show player 106f
    judith "I just want to be alone right now."
    show player 108
    player_name "I'll see you later, then..."
    return

label girls_lockerroom_judith_toilet_not_here:
    scene expression game.timer.image("backgrounds/location_school_locker_room_broken_stall{}.jpg")
    show player 11 with dissolve
    player_name "..."
    show player 10
    player_name "( {b}Judith{/b} is not here. )"
    player_name "( She must be in the hallway or at home. )"
    show player 108f
    player_name "( I should ask her to come in for {b}some fun{/b}. )"
    hide player 108f
    return

label judith_toilet_replay:
    scene expression game.timer.image("toilet_stall{}")
    show old_judith 14 zorder 1 at Position( xpos = 310, ypos = 768)
    show player 111 zorder 0 at Position (xpos = 639, ypos = 768) with dissolve
    player_name "Hey!"
    show old_judith 15
    show player 110
    judith "I was hoping you'd come see me..."
    judith "Did anyone see you come in here?"
    show old_judith 14
    show player 108
    player_name "I don't think so?"
    show old_judith 14
    show player 110
    judith "Oh, good..."
    judith "Emm... So? What do you feel like doing?"
    call screen judith_stage01

label judith_kiss:
    show player 108
    show old_judith 14
    player_name "Hmm... Have you ever kissed someone?"
    show old_judith 15
    show player 110
    judith "You mean, like a... Kiss, kiss?"
    show old_judith 14
    show player 17f
    player_name "Well, yeah!"
    show old_judith 13
    show player 110
    judith "Not really..."
    show old_judith 14
    show player 17f
    player_name "Let's try it!"
    show old_judith 4f
    show player 110
    judith "..."
    hide player
    show old_judith 31_32 at Position ( xpos = 380, ypos = 768)
    with dissolve
    pause 4
    show old_judith 5f zorder 1 at Position( xpos = 320, ypos = 768)
    show player 13f zorder 0 at Position (xpos = 640, ypos = 768)
    with dissolve
    judith "That... Was good..."
    show old_judith 4f
    show player 17f
    player_name "Feels a bit strange I guess. Haha."
    show old_judith 5f
    show player 11f
    judith "Let's do something else!"
    show old_judith 4f
    show player 14f
    player_name "Okay..."
    call screen judith_stage02

label judith_handjob:
    show player 111
    show old_judith 16
    player_name "We could do like last time, I guess?"
    show old_judith 17
    show player 106f
    judith "Let me do it."
    hide player
    show old_judith 18 at Position(xpos = 465, ypos = 768)
    player_name "!!!"
    show old_judith 19
    window hide
    pause
    show old_judith 20
    window hide
    pause
    show old_judith 21
    window hide
    pause
    show old_judith 22
    window hide
    pause
    show old_judith 24
    judith "It's so... Nice..."
    judith "... And thick."
    show old_judith 23
    player_name "{i}*Gasp*{/i}"
    show old_judith 24
    judith "I just love how it feels in my hand..."
    show old_judith 25_23
    pause 4
    player_name "That feels sooo... Good!"
    show old_judith 24
    judith "You want me to stop?"
    call screen judith_stage03

label judith_keepgoing:
    show old_judith 25_23
    pause 4
    player_name "That feels sooo... Good!"
    show old_judith 24
    judith "You want me to stop?"
    call screen judith_stage03

label judith_playwithtits:
    show old_judith 33
    judith "..."
    show old_judith 35
    judith "You like feeling them?"
    show old_judith 34
    player_name "Yeah..."
    show old_judith 36
    player_name "Your breasts are so nice and soft..."
    show old_judith 36_37_38
    pause 4
    show old_judith 39 with hpunch
    judith "{i}*Moan*{/i}"
    player_name "!!!"
    show old_judith 35
    judith "You want to try something else?"
    call screen judith_stage03

label judith_cum:
    show old_judith 25_23
    pause 4
    show old_judith 26
    pause .3
    show old_judith 27
    judith "..."
    show old_judith 28
    judith "Wow, that's a lot of cum!"
    show old_judith 29
    player_name "Sorry! I didn't mean to make a mess..."
    show old_judith 28
    judith "It's fine..."
    judith "I always wanted to know how that feels!"
    show old_judith 30
    player_name "Oh. Haha!"
    show old_judith 5f zorder 1 at Position( xpos = 300, ypos = 768)
    show player 13f zorder 0 at Position (xpos = 623, ypos = 768)
    judith "We could do this again..."
    show player 17f
    show old_judith 4f
    player_name "I'd like that!"
    show player 13f
    show old_judith 5f
    judith "Me too..."
    show player 2f
    show old_judith 4f
    player_name "We should get out of here..."
    show player 1f
    show old_judith 5f
    judith "Okay!"
    $ renpy.end_replay()
    $ M_judith.set("in bathroom", False)
    $ M_judith.unforce()
    $ persistent.cookie_jar["Judith"]["unlocked"] = True
    $ persistent.cookie_jar["Judith"]["gallery"]["02_unlocked"] = True
    $ game.timer.tick()
    $ player.go_to(L_school_lefthallway)
    $ game.main()

label judith_pullpants:
    show old_judith 24
    judith "I'm not... Ready for that yet."
    show old_judith 23
    player_name "Oh... It's okay! We don't have to."
    show old_judith 24
    judith "Maybe another time..."
    judith "... When I feel a bit more comfortable."
    show old_judith 23
    player_name "I'm okay with that."
    show old_judith 24
    judith "Can we do something else?"
    call screen judith_stage03

label girls_lockerroom_roxxy_lockerroom_event:
    scene expression game.timer.image("location_school_locker_room_broken{}_blur")
    show old_missy 1 at Position (xpos=400)
    show old_becca 1 at left
    show old_roxxy 3 at right
    with dissolve
    roxxy "It's total bullshit!"
    show old_roxxy 3d
    show old_becca 2
    becca "I can't believe {b}Coach Bridget{/b} really suspended you from the team!"
    show old_becca 1
    show old_missy 2
    missy "Yeah, doesn't she realize that the team is going to suck hardcore without you?"
    show old_missy 1
    show old_becca 6
    becca "Well, we aren't THAT bad."
    show old_becca 1
    show old_missy 1bf with dissolve
    missy "... Please. You can't even do a proper toe touch!"
    show old_missy 2bf
    show old_becca 2
    becca "Hey, I can too!"
    show old_becca 6
    becca "I just don't like to do them 'cause it makes my tits sore!"
    show old_becca 8
    becca "You'd understand if you weren't such a stick!"
    show old_becca 7
    show old_missy 4f
    missy "Screw you, skank! {b}Roxxy{/b} does them just fine, and she's got bigger tits than you do!"
    show old_missy 4bf
    show old_becca 8
    becca "Pfft, yeah, well... EVERYONE has bigger tits than you!"
    show old_becca 7
    show old_missy 4f
    missy "Oh, that's it! I'm gonna-"
    show old_roxxy 31
    roxxy "Would you two cut it out?"
    show old_missy 3 with dissolve
    show old_roxxy 3
    roxxy "Focus on me and my problems!"
    show old_roxxy 3d
    show old_missy 1b
    missy "Sorry, {b}Roxxy{/b}."
    show old_missy 1
    show old_becca 2
    becca "I just don't know what to tell you..."
    show old_becca 1
    show old_roxxy 3
    roxxy "Well, I can't steal homework from that four-eyed cow anymore."
    roxxy "If I get caught again, they're going to expel me."
    show old_roxxy 3d
    show old_missy 3
    missy "..."
    show old_becca 2
    becca "What about {b}Dexter{/b}?"
    show old_becca 1
    show old_missy 1
    roxxy "..."
    show old_roxxy 2
    roxxy "What about him?"
    show old_roxxy 1
    show old_becca 2
    becca "He's your boyfriend, isn't he?"
    show old_becca 1
    show old_roxxy 3c
    roxxy "... Yeah, so?"
    roxxy "He's too stupid to help me with my homework if that's where you're going with this..."
    roxxy "... He can barely read."
    show old_roxxy 3d
    show old_missy 6
    missy "Hahaha!"
    show old_roxxy 31
    roxxy "Shut up, {b}Missy{/b}!"
    show old_roxxy 3b
    show old_missy 1b
    missy "... Sorry."
    show old_missy 1
    show old_becca 2
    becca "You don't need him to help you do the homework. Just have him steal someone else's homework for you!"
    show old_becca 1
    show old_roxxy 29
    roxxy "... Hmm."
    show old_roxxy 30
    roxxy "That's not bad."
    roxxy "I can continue on the same way but without any of the risk."
    show old_roxxy 29
    show old_missy 2
    missy "... So {b}Dexter{/b} really can't read?"
    show old_missy 1
    show old_roxxy 3
    roxxy "... {b}Missy{/b} drop it."
    show old_roxxy 3d
    show old_missy 1b
    missy "Hehe, I'm sorry it's just kind of funny is all."
    show old_missy 1
    show old_becca 2
    becca "Who cares if he can read?"
    becca "He's the most popular guy in school AND he has a car!"
    show old_becca 1
    show old_roxxy 2
    roxxy "Yeah."
    roxxy "... And he's old enough to buy us alcohol!"
    show old_roxxy 1
    show old_missy 8
    missy "You're right, that's definitely a perk!"
    show old_missy 7
    show old_becca 2
    becca "So you're all set then?"
    show old_becca 1
    show old_missy 1
    show old_roxxy 1b
    roxxy "Not quite."
    roxxy "{b}Dexter{/b} can steal work for the {i}French bitch{/i} and {b}Miss Ross{/b} is easy enough to please."
    roxxy "I just need to tell her she's pretty and pretend I'm interested in her stupid art."
    show old_roxxy 3c
    roxxy "... But what am I going to do for {b}Miss Dewitt{/b}'s class?"
    show old_roxxy 1
    becca "..."
    show old_missy 1b
    missy "Just pick up the flute like {b}Becca{/b} and I did."
    show old_missy 1
    show old_roxxy 3c
    roxxy "Ugh, seriously?"
    show old_roxxy 1
    show old_missy 1b
    missy "Yeah, it's not that hard."
    missy "... And it's good practice, you know..."
    show old_missy 8
    missy "... For blowjobs!"
    show old_missy 7
    show old_roxxy 2
    roxxy "Pfft, yeah right!"
    show old_roxxy 1
    show old_missy 2
    missy "I'm serious!"
    show old_missy 5
    missy "... Or well, that's what my sister says..."
    show old_missy 1
    show old_roxxy 2
    roxxy "Playing a musical instrument and sucking dick are two completely different things, you dumb slut."
    show old_roxxy 1
    show old_missy 3
    missy "..."
    show old_becca 2
    becca "Yeah, and didn't your sister get fired from her job at Consum-R because she couldn't count the register properly?"
    show old_becca 1
    show old_missy 2f with dissolve
    missy "Huh?"
    show old_missy 4f
    missy "... No!"
    show old_missy 2f
    missy "I mean..."
    show old_missy 4f
    missy "... Shut up, {b}Becca{/b}!"
    show old_missy 2bf
    show old_becca 4
    becca "Pffftt!!!"
    show old_becca 8
    becca "\"My sister says...\""
    show old_becca 4
    becca "Hahaha!"
    show old_missy 2 with dissolve
    missy "Look, I'm just saying go with the flute, and we can help you practice."
    show old_missy 1
    becca "Hahaha!"
    show old_becca 1
    show old_missy 4f with dissolve
    missy "I said shut up, {b}Becca{/b}!!"
    show old_missy 2bf
    show old_roxxy 2
    roxxy "Ugh, both of you shut up..."
    show old_missy 1 with dissolve
    show old_roxxy 1b
    roxxy "C'mon, we better get going or the {i}French bitch{/i} is gonna lecture us with her mush mouth again."
    show old_roxxy 1
    show old_becca 4
    becca "Haha!"
    hide old_becca
    hide old_missy
    hide old_roxxy
    with dissolve

    scene expression game.timer.image("lefthall{}")
    show player 23 at left with dissolve
    player_name "( Oh crap! They're coming this way! )"
    show player 22
    show old_roxxy 1 at Position (xpos=500)
    show old_missy 1f at Position (xpos=700)
    show old_becca 2f at right
    with dissolve
    becca "Hey, were you spying on us?!"
    show old_becca 1f
    show old_roxxy 3c
    roxxy "What the hell you perv!"
    show old_roxxy 3b
    show old_missy 8f
    missy "Hi, {b}[firstname]{/b}."
    show old_missy 7f
    show old_roxxy 3cf at Position (xoffset=-50) with dissolve
    becca "..."
    show old_missy 3f
    roxxy "..."
    show old_missy 2f
    missy "I mean... Yeah, what the fuck, nerd?!"
    show old_roxxy 3c with dissolve
    show old_missy 1f
    show player 12
    player_name "I wasn't-"
    show player 22
    show old_roxxy 3
    roxxy "Don't lie!"
    show old_roxxy 3d
    show old_becca 2f
    becca "Yeah, it's obvious you were listening!"
    show old_becca 1f
    show player 24
    player_name "... Fine."
    show player 12
    player_name "I was listening, you happy?"
    show player 24
    show old_roxxy 3
    roxxy "Eugh, you're such a loser..."
    show old_roxxy 3d
    show player 12
    player_name "You know, having {b}Dexter{/b} steal people's homework isn't going to work..."
    player_name "The teachers are going to know you didn't write it."
    show player 16
    show old_becca 8f
    becca "Pfft, what do you know?!"
    show old_becca 7f
    show old_roxxy 3c
    roxxy "... And why do you care?"
    show old_roxxy 3d
    show player 12
    player_name "I don't care!"
    player_name "Flunk out and prove everybody right about you."
    player_name "It won't bother me one bit..."
    hide player with dissolve
    show old_roxxy 29
    roxxy "..."
    show old_missy 8f
    missy "Bye, {b}[firstname]{/b}!"
    show old_missy 7f
    show old_roxxy 3cf at Position (xoffset=-50) with dissolve
    show old_becca 2f
    becca "What the hell, {b}Missy{/b}?"
    show old_becca 1f
    show old_missy 2 with dissolve
    missy "... What?"
    scene black
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
