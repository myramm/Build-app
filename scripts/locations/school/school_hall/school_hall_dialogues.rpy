label school_eve_lesbians_aftermath:
    scene expression player.location.background_blur with None
    show anon
    show erik:
        xoffset -100
    with dissolve
    erik "... So then we stormed the goblin nest and I took an arrow in the knee!"
    anon "That sounds bad."
    erik "Meh, it'll make guard duty a pain but I captured a goblin slave girl so it was totally worth it!"
    anon f_surprised "Goblin slave girl?"
    erik @ f_laugh "Yeah man, once you go green, your sex life's a dream!"
    anon f_snarky "... Right."
    anon f_normal "Okay."
    erik @ f_laugh "Hahaha!"
    show eve b_dress f_happy:
        xoffset 100
    with dissolve
    eve "Hey, {b}[firstname]{/b}!"
    anon @ a_wave "Hey!"
    show erik f_surprised:
        flip
        xoffset 300
    with dissolve
    erik "!!!"
    anon "Wow, you're wearing that dress from the party!"
    eve "Y-yeah."
    eve "You told me you wanted to see me in dresses more often, remember?"
    anon "I do."
    anon @ f_laugh "You look amazing!"
    eve @ f_laugh "Hehe, thanks!"
    hide anon
    show eve b_dress_kiss
    show erik:
        xoffset 0
    with dissolve
    pause
    eve "Mmm."
    hide eve
    show eve b_dress f_happy
    show anon:
        xoffset 300
    with dissolve
    pause
    eve f_confused "What's with him?"
    anon @ -m_talk "Hmm?"
    show anon f_worried:
        flip
        xoffset -200
    with dissolve
    anon "I dunno."
    anon "{b}Erik{/b}?"
    pause
    anon "You alright, buddy?"
    erik @ -m_talk "..."
    hide anon
    show anon f_flirt:
        xoffset 300
    with dissolve
    anon "I don't think he's used to seeing girls as pretty as you."
    eve "Aww."
    hide anon
    show eve b_dress_kiss
    with dissolve
    pause
    hide eve
    show eve b_dress f_happy
    show anon:
        xoffset 300
    with dissolve
    eve "You wanna walk with me to {b}Miss Ross{/b}' class?"
    anon "Of course!"
    anon f_normal_left "I'll catch you later, okay {b}Erik{/b}?"
    erik "..."
    show anon f_normal
    eve @ f_laugh "Hehe, c'mon!"
    scene black with fade
    pause

    $ player.go_to(L_school_lefthallway)
    scene expression player.location.background_blur with None
    show eve f_happy b_dress
    show anon
    with dissolve
    eve "... They've been fucking like rabbits!"
    anon f_flirt "Really?"
    eve "Yeah, all over the house!"
    eve "I'm like, terrified to come out of my bedroom..."
    eve @ f_laugh "Seriously, I could draw {b}Odette{/b}'s vag from memory at this point."
    anon f_normal @ f_laugh "Haha!"
    random_guy "Whoa, who is that?!"
    eve f_nervous "Umm, {b}[firstname]{/b}?"
    random_girl "Isn't that {b}Eve{/b}?"
    show eve f_nervous_down
    random_guy "No way!"
    random_girl "I think it is..."
    eve "P-people are staring..."
    anon f_flirt "They're just admiring how beautiful you are."
    random_girl "She's so pretty..."
    show eve f_nervous
    anon "See, I told you."
    anon f_normal "Feels good, doesn't it?"
    eve "Y-yes."
    kevin "{b}Eve{/b}?"
    show kevin f_surprised
    show eve:
        flip
        xoffset 300
    with dissolve
    kevin "Is that really you?"
    anon "Hey, {b}Kevin{/b}!"
    show kevin f_normal
    eve "H-hi."
    eve "Yeah, it's really me."
    kevin "Wow, you look awesome!"
    eve "Really?"
    kevin @ f_laugh "Yeah!"
    kevin "Where'd you get that dress?"
    eve f_happy "My sister's girlfriend bought it for me."
    kevin "You should dress like this all the time!"
    random_guy "Who knew that was hiding under all those layers?!"
    random_girl "Right?!"
    eve "Heh, uhh... I dunno."
    eve "I'm not sure I could handle this much attention all the time."
    eve "Maybe just once in a while..."
    eve f_nervous_right "... When {b}[firstname]{/b} wants me to."
    anon "Works for me!"
    eve f_happy_right @ f_laugh "Hehe!"
    pause
    kevin "You all heading to {b}Miss Ross{/b}' class?"
    show eve f_happy
    anon "Yup."
    kevin "Mind if I walk with you?"
    eve "Not at all."
    hide kevin
    hide eve
    hide anon
    with dissolve
    kevin "I wonder what crazy crap she has planned for us today?"
    eve "Oh god, who knows?"
    return

label school_eve_school_stinker:
    scene expression player.location.background_blur with None
    show annie a_stink f_gross:
        flip
        xoffset 250
    show smith a_stink f_gross:
        flip
    show chad
    with dissolve
    smith "Haven't you ever heard of a shower?!"
    chad f_angry "I did shower, twice!"
    chad f_normal_down "It won't go away..."
    annie "Eugh, it's unbearable..."
    chad f_normal "Yo, you're the one who said that if I missed another day of school, I'd be expelled!"
    smith "My eyes are watering!"
    smith "Go home!"
    chad "I can't get expelled, my folks will kill me!"
    smith "Fine, I won't expel you!"
    smith "Just get out of here before I puke!"
    annie "Yeah, don't come back until that stink is gone!"
    chad f_happy @ f_laugh "Sweet, no school!"
    annie "It's in my mouth!"
    smith "Why are you still standing there!"
    smith @ f_scream "LEAVE!" with hpunch
    chad f_surprised "!!!"
    pause
    hide chad with dissolve
    smith "Jesus, we're going to have to air this place out..."
    smith "Make sure you open all the windows."
    annie "Right away, ma'am."
    show smith f_puke
    hide annie with dissolve
    smith a_cover "{i}*Hurrrk*{/i}"
    smith f_eyeroll "Oh, god..."
    scene expression player.location.background_blur with None
    show anon f_laugh
    with fade
    anon "( Looks like {b}Tyrone{/b} and his boys are still dealing with the aftermath of {b}Eve{/b}'s prank... )"
    pause
    show ronda f_laugh with {'master': dissolve}
    ronda "Did you see that, {b}[firstname]{/b}?"
    anon f_normal "Heh, yeah."
    ronda f_normal "I can't believe they still stink!"
    ronda @ f_laugh "Hahahaah!"
    anon "{b}Eve{/b} must be loving this, huh?"
    ronda f_suspicious a_crossed "Oh, I don't know..."
    ronda "I haven't seen her today."
    anon "No?"
    ronda "I don't think she's here..."
    anon f_worried "She didn't show up for school?"
    ronda f_normal "Maybe she's grounded or something?"
    anon @ a_behind_head "Y-yeah, maybe..."
    pause
    anon "So, how did you make out?"
    ronda @ -m_talk "Hmm?"
    anon "Your dad seemed really pissed off..."
    ronda f_upset "Yeah, he was."
    ronda f_suspicious "Thankfully, my mom calmed him down and helped me convince him that I didn't do anything wrong."
    anon "Good."
    anon "I was worried we'd gotten you in big trouble."
    ronda @ -m_talk "Mmhmm."
    ronda @ f_eyeroll "Well, I can't jog in the park anymore, but otherwise, no."
    anon "That sucks!"
    ronda f_normal "Yeah, I'll have to change up my entire routine now."
    ronda a_sides "Speaking of which, I should get going..."
    ronda "{b}Coach Bridget will be waiting for me out at the track{/b}."
    anon "O-oh, okay."
    anon @ a_wave "See ya later."
    ronda "See ya."
    hide ronda with dissolve
    pause
    anon a_thinking f_thinking @ -m_talk "( I wonder why {b}Eve{/b} didn't show up today? )"
    anon @ -m_talk "( Perhaps I should {b}swing by her house and check on her{/b}? )"
    hide anon with dissolve
    return

label school_eve_apologize:
    scene expression player.location.background_blur
    show anon f_thinking a_thinking with dissolve
    anon @ -m_talk "( Hmm, I should probably find {b}Eve{/b} and apologize again. )"
    hide anon with dissolve
    return

label school_eve_big_sister_problems:
    scene expression player.location.background_blur with None
    show eve f_sad_down
    show anon f_worried with dissolve
    anon @ a_wave "Hey {b}Eve{/b}, what's up?"
    eve f_sad "Oh, hey {b}[firstname]{/b}... Not much."
    anon "Something wrong?"
    eve f_sad_down "Ugh, {b}Miss Ross{/b} is-"
    show eve a_rossed with dissolve
    pause
    eve "Never mind, I'm just having a rough day..."
    anon "You sure?"
    anon "We can talk about it, if you want?"
    eve "Nah, I think I'm just going to head home."
    anon "You're gonna cut class?"
    eve "Yeah, I think so..."
    pause
    eve f_happy a_hip "Hey, you wanna come with me?"
    anon f_skeptical "Ehh, I dunno..."
    eve "We can go back to my place and play some more {i}Street Kombat{/i}!"
    anon f_shy "Heh, that does sound fun..."
    anon f_worried "... But won't your sister get mad?"
    eve @ f_eyeroll "Oh, please... She's so busy with her shop, she probably won't even realize we're there..."
    anon "Are you sure?"
    eve "Yeah, trust me."
    anon f_thinking a_thinking @ -m_talk "Hmm."
    eve "C'mon, you really wanna sit through another one of {b}Miss Bissette{/b}'s boring lectures?"
    anon f_worried a_idle "Of course not but I am kinda behind on my grades..."
    eve "Tsk, now you're just making excuses..."
    anon "Hey, I'm not-"
    eve "You've got plenty of time to work on your grades!"
    show anon f_unimpressed
    pause
    anon f_normal @ a_up f_brag_closed "Alright, fine... Let's go."
    eve @ f_laugh "Yay!!"
    show anon a_empty b_empty f_surprised_left:
        flip
        xoffset -344
    show eve a_grab_mc
    with dissolve
    eve "{b}Let's go to my place{/b}!"
    anon @ -m_talk "!!!"
    hide anon
    hide eve
    with dissolve
    $ player.go_to(L_park)
    $ playSound()
    scene expression player.location.background_blur with None
    show eve f_happy:
        flip
        xoffset 300
    show anon
    with dissolve
    eve "They just don't make anime as good as they used to, you know?"
    eve @ f_eyeroll "All of today's stuff is packed to the brim with cliché, shallow characters, and fan service!"
    anon "Heh, I've never met a girl who was so into anime before..."
    hide eve
    show eve f_happy
    with dissolve
    eve "O-oh, yeah?"
    anon "I'm pretty sure the other girls in this town have never even heard of anime."
    eve f_nervous_down "Y-yeah, I guess I'm pretty weir-"
    anon "It's awesome!"
    eve f_surprised @ -m_talk "!!!"
    eve "I-it is?"
    anon "Yeah, really awesome!"
    show eve f_happy
    anon @ f_skeptical a_point "Have you seen, \"Attack on Colossus?\""
    eve "Oh yeah, the Colossi in that series are dope!"
    anon @ f_laugh "Right, with those creepy smiles?!"
    eve "I love it!"
    pause
    eve "The protagonist is a big, whiny pussy though..."
    anon f_laugh "Hahaha, totally!"
    eve f_laugh "Haha!"
    pause
    show anon f_normal
    eve f_happy "Alright, we're almost to the shop..."
    scene black with fade
    $ player.go_to(L_tattooparlor)
    scene expression player.location.background_blur with None
    show eve:
        flip
    show anon f_normal:
        flip
    eve "... Just be really quiet while we're going {b}through the garage{/b}, okay?"
    anon f_worried "O-okay, sure, but-"
    eve @ f_eyeroll "My sister probably won't care that I'm skipping school, but there's no reason to tell her if I don't have to..."
    anon a_salute "Umm, {b}Eve{/b}?"
    eve f_confused "What?"
    anon "Are you sure the shop is even open?"
    hide eve
    show eve:
        xoffset -500
    show anon f_worried a_idle
    with dissolve
    eve @ -m_talk "Hmm?"
    eve f_surprised a_hip_angry @ a_wtf "What the-"
    eve f_sad "There's nobody minding the shop!"
    pause
    hide eve
    show eve f_sad a_hip_angry:
        flip
    with dissolve
    eve "C'mon, I need to figure out what's going on..."
    hide eve with dissolve
    anon @ -m_talk "..."
    hide anon with dissolve
    return

label school_diane_delivery_3:
    scene expression player.location.background_blur
    show player 166 at left with dissolve
    player_name "Phew, almost there..."
    show player 168b
    annie "HOLD IT RIGHT THERE!" with hpunch
    show player 168c
    player_name "Hmm?"
    show player 168b
    show old_annie 5 at right with dissolve
    annie "Where do you think you're going with all that milk?"
    show old_annie 6
    show player 168
    player_name "Oh, hey {b}Annie{/b}."
    player_name "I'm supposed to deliver this to the cafeteria."
    show player 167
    show old_annie 5
    annie "I don't think so."
    show old_annie 6
    show player 166
    player_name "What, why?"
    show player 165
    show old_annie 5
    annie "{b}Mrs. Smith{/b} didn't say anything to me about a milk delivery today."
    show old_annie 6
    show player 166
    player_name "... So?"
    player_name "I'm sure {b}Mrs. Smith{/b} doesn't tell you about every little thing that's going on in the school..."
    show player 165
    show old_annie 3
    annie "Uhh, yes she does."
    annie "I'm her second in command."
    show old_annie 1
    player_name "..."
    show player 166
    player_name "Look {b}Annie{/b}, this is really heavy. Can you please just get out of my way?"
    player_name "I'm positive it's supposed to go to the cafeteria."
    show player 165
    show old_annie 4
    annie "I said no!"
    annie "Not until I clear it with {b}Mrs. Smith{/b}."
    show old_annie 1
    player_name "..."
    show old_annie 3
    annie "C'mon, she's in her office."
    hide old_annie with dissolve
    show player 166
    player_name "{b}Her office on the third floor{/b}?!"
    player_name "Can you at least help me carry this?"
    show player 165
    annie "Nope!"
    pause
    show player 168c
    player_name "{i}*Sigh*{/i}"
    hide player with dissolve
    return

label school_roxxy_shower_event:
    scene expression player.location.background_blur
    show anon f_worried b_jersey with dissolve
    anon @ -m_talk "( Woah! It's hard to breathe! )"
    anon @ -m_talk "( It's so damn hot outside... )"
    anon f_disgusted_down a_surprised_shoulders @ -m_talk "( ... And I'm SOAKED! )"
    anon @ -m_talk "( I should {b}take a shower{/b} before going to my next class. )"
    return

label school_roxxy_intense_gymercise:
    scene expression player.location.background_blur
    show old_erik 28 at right
    show player 1 at left
    with dissolve
    erik "Hey, {b}[firstname]{/b}."
    show old_erik 27
    show player 14
    player_name "Hey, {b}Erik{/b}."
    player_name "Why are you wearing your gym clothes?"
    show old_erik 28
    show player 11
    erik "{b}Coach Bridget{/b} wants to speak with you!"
    erik "She's waiting out by the track."
    show old_erik 27
    show player 10
    player_name "Crap, it's probably about all the training I've missed... She's gonna kill me!"
    show old_erik 28
    show player 5
    erik "You'd better hurry!"
    show old_erik 27
    show player 10
    player_name "Yeah, thanks for letting me know, man!"
    show old_erik 29
    show player 11
    erik "No problem, dude!"
    show old_erik 27
    hide player with dissolve
    pause
    show old_erik 28
    erik "Good luck!"
    hide old_erik with dissolve
    return

label school_bissette_challenge:
    scene expression player.location.background_blur
    show anon f_thinking with dissolve
    anon @ -m_talk "( I should probably {b}talk to Miss Bissette about that private tutoring{/b}. )"
    anon @ -m_talk "( I can't understand any of the material in class... )"
    anon @ -m_talk "( ... I think I'm too far behind to catch up on my own. )"
    anon @ -m_talk "( A little bit of extra help never hurt anybody... )"
    anon @ a_thinking -m_talk "( ... And I may get that reward if I do well in the final quiz! )"
    hide anon with dissolve
    return

label school_mia_glasses_favor:
    scene expression player.location.background_blur
    show player 13 at left
    show old_mia 10 at right
    with dissolve
    mia "Hey, {b}[firstname]{/b}."
    show old_mia 7
    show player 14
    player_name "Hey, {b}Mia{/b}."
    show player 12
    player_name "How's your dad doing?"
    show player 5
    show old_mia 10
    mia "He's alright. I think..."
    show old_mia 51 with dissolve
    mia "My mom was cleaning up his office last night and found these old glasses..."
    show old_mia 7
    show player 446
    with dissolve
    pause
    show player 448
    player_name "Sweet, Aviators!"
    player_name "Does he still wear them?"
    show player 13
    show old_mia 50
    with dissolve
    mia "He used to, but that was a long time ago."
    mia "I was thinking maybe he would like to use them again."
    show old_mia 50b
    show player 14
    player_name "That's nice."
    show player 13
    show old_mia 50
    mia "Actually, I was wondering if you could drop them off at his work?"
    mia "I have to be somewhere later and I won't have time to take them myself."
    show old_mia 50b
    show player 10
    player_name "Huh? You want {i}me{/i} to go?"
    show player 5
    show old_mia 50
    mia "Why not?"
    mia "You two seem to be getting along so well..."
    mia "... And he would be happy to see them again, I'm sure!"
    mia "Ever since you spoke to him, he's been doing much better."
    show old_mia 50b
    show player 12
    player_name "Ehh... Yeah, I suppose I could {b}drop them off at his work{/b}."
    show player 447
    show old_mia 10
    with dissolve
    mia "Thanks, that's really sweet of you to do this for me."
    show old_mia 7
    show player 448
    player_name "It's no problem, I don't mind visiting him."
    show player 447
    show old_mia 10
    mia "See you later, then!"
    show old_mia 7
    show player 448
    player_name "Bye."
    hide player
    hide old_mia
    with dissolve
    call popup ('give', 'aviators')
    return

label school_erik_bully_fight:
    scene expression player.location.background_blur
    show old_dexter 9 at right with dissolve
    erik "Ugh!!"
    erik "Let... Me go... {b}Dexter{/b}!"
    dexter "Not a chance, chubby."
    dexter "You still haven't given me your homework."
    dexter "I guess you didn't get the message."
    erik "I told you! I already turned it in! I don't have it anymore!"
    dexter "Well then, I guess you'll have to give me something else..."
    dexter "How much money do you got on you?"
    erik "What?!"
    dexter "I said, how much money are you going to give me before I shove your face into a locker!!"
    erik "!!!"
    erik "{b}Dexter{/b}! I... I..."
    show player 15 at left with dissolve
    show old_dexter 10
    player_name "HEY!!!"
    player_name "Leave him alone, {b}Dexter{/b}!"
    show player 16
    show old_dexter 9
    dexter "Well, if it isn't your loser friend."
    show old_dexter 10
    show player 15
    player_name "{b}Dexter{/b}, stop picking on {b}Erik{/b}."
    show player 16
    show old_dexter 9
    dexter "Why? Would you like to take his place?"
    player_name "..."
    show old_dexter 12 with dissolve
    dexter "Step up, {b}[firstname]{/b}."
    show old_dexter 13
    dexter "Let's see what you got!"
    return

label school_erik_bully_fight_pass:
    show old_dexter 14
    show player 387 with dissolve
    player_name "I'm not scared of you, {b}Dexter{/b}!"
    show player 388
    show old_dexter 15
    dexter "Well, you should be scared of... THIS!"
    hide player
    hide old_dexter
    show old_dexter 16 at left
    with dissolve
    pause
    show old_dexter 17 at right with dissolve
    player_name "Haiii!!"
    hide old_dexter
    show player 390 at left
    show old_dexter 18 at right
    with dissolve
    dexter "Arghh!!"
    dexter "You... Little... Shit..."
    show old_dexter 15 with dissolve
    show player 389
    player_name "!!!"
    show player 391
    show old_dexter 19 with hpunch
    pause
    hide player
    show old_dexter 20 at left
    with dissolve
    dexter "Not so fast this time, huh?!"
    dexter "I'll show you..."

    scene school_fight_cs1
    show text _ ("Even after all my recent training at the gym,\n{b}Dexter{/b} was still too strong for me...\n... But I knew now, that I could hurt him...") as caption
    with fade
    pause

    scene school_fight_cs2
    show text _ ("... And then, everything went dark.") as caption
    with fade
    pause

    scene expression player.location.background_blur
    show old_mia 24 at left
    show old_dexter 21 at Position (xpos=713)
    with fade
    mia "{b}[firstname]{/b}!! Are you okay?!"
    show old_mia 23
    pause
    show old_mia 28 with dissolve
    mia "What's your problem, {b}Dexter{/b}?"
    mia "You really hurt him!"
    show old_mia 27
    show old_dexter 22
    dexter "Mind your own business!"
    dexter "He had it coming!!"
    show old_dexter 23
    show old_roxxy 30 at right with dissolve
    roxxy "{b}Dexter{/b}?"
    show old_roxxy 29
    show old_dexter 24
    dexter "What?!"
    show old_dexter 23
    show old_mia 23 with dissolve
    show old_roxxy 27
    roxxy "..."
    show old_roxxy 28
    roxxy "Umm... {b}Dexter{/b}, what's going on?"
    roxxy "Did you do that?"
    show old_roxxy 29
    show old_mia 27 with dissolve
    show old_dexter 24
    dexter "Nothing's going on!!"
    show old_dexter 12
    dexter "I just finished teaching this little shit a lesson."
    show old_dexter 23
    show old_roxxy 30
    roxxy "Really? You had to do this now? In the hallway?"
    show old_roxxy 29
    show old_dexter 24
    dexter "Shut up, {b}Roxxy{/b}."
    dexter "Come on. Let's get out of here!"
    show old_roxxy 27
    dexter "I've got better things to do than watch a bunch of idiots standing around."
    hide old_dexter
    hide old_roxxy
    with dissolve
    hide old_mia
    show eve f_sad_down a_sides:
        xoffset -350
    show old_mia 23 at left
    show old_judith 40 at Position (xpos=600)
    show old_erik 50 at Position (xpos=900)
    with dissolve
    judith "Oh my gosh! What happened?!"
    show old_judith 41
    eve "{b}Dexter{/b} is such a jerk."
    eve "He went too far this time."
    hide old_erik
    show teacher 15 at Position (xpos=700)
    show old_erik 50 at Position (xpos=900)
    with dissolve
    bissette "!!!"
    bissette "What is happening over here?"
    bissette "What is wrong with {b}[firstname]{/b}?"
    show teacher 14
    show old_mia 26 with dissolve
    mia "He got into a fight with {b}Dexter{/b} and {b}Dexter{/b} slammed him into the lockers."
    mia "He's still breathing. I hope he'll be alright."
    show old_mia 25
    bissette "..."
    show teacher 15
    bissette "We should be calling the ambulance!"
    $ playSound()
    scene black with fade
    hide old_mia
    hide eve
    hide teacher
    hide old_erik
    hide old_judith
    return

label school_erik_bully_fight_fail:
    show old_dexter 14 at right with dissolve
    show player 6 at left with dissolve
    player_name "I don't want to fight you, {b}Dexter{/b}!"
    show player 23 with dissolve
    player_name "I just want you to leave {b}Erik{/b} alone..."
    show player 22
    show old_dexter 15
    dexter "Really?"
    show old_dexter 14
    show player 10
    player_name "That's all..."
    show player 22
    show old_dexter 12 with dissolve
    dexter "Hah!"
    dexter "Weak and pathetic..."
    dexter "... Just like your father!"
    hide old_dexter
    with dissolve
    show player 24
    player_name "..."
    hide player
    with dissolve
    return

label school_roxxy_intro_started:
    scene expression player.location.background_blur
    show dexter zorder 2:
        xoffset -50
    show roxxy f_laugh zorder 2:
        xoffset 50
    with None
    show erik zorder 1:
        xzoom -1
        xoffset 50
    show anon zorder 1:
        xoffset -100
    with {'master': dissolve}
    roxxy "... So then {b}Becca{/b} threw her retainer in the toilet!"
    dexter @ f_laugh "Bahahahahahah!"
    roxxy f_unimpressed @ -m_talk "..."
    roxxy "... Ugh, what are you two losers looking at?!"
    erik "I think we're looking at the combined IQ of 2."
    show erik f_laugh
    anon @ f_laugh "Hah!!"
    show erik f_normal
    roxxy f_angry "Excuse me?!"
    dexter f_angry "... Huh, I don't get it?"
    roxxy @ f_eyeroll "They're calling us stupid..."
    dexter "They are?!"
    dexter a_ball_point "Hey! You calling us stupid?!"
    show anon f_surprised
    erik f_worried "I... N-no, I didn't... I mean, I wouldn't..."
    dexter a_idle @ a_ball_fists "'Cause I'll smash your face in, you little shit!"
    roxxy f_sexy @ f_unimpressed "... And what are YOU laughing at?"
    roxxy "Didn't your deadbeat loser of a father kill himself or something?"
    show anon f_sad_down
    erik f_bored_right @ -m_talk "..."
    anon f_angry "At least I HAD a father growing up..."
    show erik f_normal
    anon "... And I don't live in a TRAILER!!"
    show dexter f_laugh
    roxxy f_surprised "!!!" with hpunch
    show dexter f_surprised
    roxxy f_angry "... You're dead!"
    show dexter f_angry
    roxxy "{b}Dexter{/b}, get 'em!!!"
    show anon f_surprised
    dexter f_normal "Hold up, {b}Roxxy{/b}. {b}Mrs. Smith{/b} is coming..."
    dexter "If I get caught fighting again, {b}Coach Bridget{/b} said she'll kick me off the team."
    hide dexter with dissolve
    roxxy @ f_eyeroll "Pfft, fine..."
    roxxy "... This isn't over, {b}[firstname]{/b}!"
    roxxy "I'll deal with you later!"
    hide roxxy with {'master': dissolve}
    pause
    show smith f_angry with {'master': dissolve}
    show anon f_worried
    show erik f_worried
    smith "You two! Get over here, RIGHT NOW!!!"
    show erik f_worried_down
    smith "What are you still doing in the damn hallway?!"
    erik @ f_worried "Sorry, {b}Mrs. Smith{/b}! We were just-"
    smith f_normal "Ah, {b}[firstname]{/b}! Finally returned to us I see..."
    anon "Y-yes, ma'am."
    smith f_angry @ f_scream "Well, it's about time! Do you have any idea how far your grades have fallen?!"
    anon f_surprised "... They have?"
    erik f_worried "That doesn't seem fair!"
    erik "Don't you know his dad-"
    smith "That's quite enough, young man!"
    smith "I suggest you get your butt to class before you find it sitting in detention!"
    erik f_worried_down @ -m_talk "..."
    smith "... And as for you, {b}[firstname]{/b}, we need to discuss your failing grades!"
    smith "I want you upstairs, in my office, right away!"
    anon f_worried "Yes, {b}Mrs. Smith{/b}."
    hide smith with {'master': dissolve}
    show anon:
        xoffset 0
    show erik f_worried:
        xzoom 1
        xoffset 0
    with {'master': dissolve}
    erik "Man, she's pure evil..."
    anon f_normal "Heh, yeah."
    erik "I'm serious! She's like the Evil Ice Queen from {i}Whorecraft{/i}!"
    show erik f_normal
    anon "Well, I'd better {b}get up to her office{/b} before her mood worsens."
    erik "Good luck, dude..."
    anon "... Thanks."
    erik @ f_laugh "Oh shoot, I almost forgot!"
    erik "I slipped a little welcome back present into your locker!"
    anon "Really?"
    erik "Glad to have you back, dude!"
    anon "Thanks, {b}Erik{/b}!"
    anon a_thinking f_thinking @ -m_talk "Hmm..."
    anon "... You know, I don't remember my locker combination."
    show anon f_worried a_idle with {'master': dissolve}
    erik f_worried "You didn't write it down?"
    anon "No, but I guess I should have, huh?"
    erik f_normal "You're probably going to have to {b}talk to Mrs. Smith about it{/b}."
    anon f_normal @ f_worried "Ugh, you're probably right..."
    anon @ a_wave "I'll see you later, {b}Erik{/b}."
    erik "Yup, see ya, {b}[firstname]{/b}."
    return

label school_hallway_dewitt_talent_show_ask_annie:
    scene expression player.location.background_blur
    show player 4f with dissolve
    player_name "( I wonder who I should talk to first? )"
    show player 9f at left with dissolve
    pause
    pause
    show player 22 at left
    show old_annie 4 at right
    with hpunch
    annie "{b}[firstname]{/b}, stop loitering in the hallway!"
    show old_annie 1
    show player 12
    player_name "{b}Annie{/b}, I just stepped into the hallway..."
    show player 5
    show old_annie 5
    annie "Whatever. Hurry to your next class before I write you up!"
    show old_annie 6
    show player 12
    player_name "Alright! Sheesh..."
    show player 10
    player_name "Oh, hey! Wait a second!"
    player_name "You don't happen to play an instrument or sing, do you?"
    show player 5
    show old_annie 3
    annie "I do. What of it?"
    show old_annie 1
    show player 10
    player_name "Well, you see, {b}Miss Dewitt{/b} is looking for people to play in the talent show."
    show player 5
    show old_annie 5
    annie "Yes, I'm well aware."
    show old_annie 6
    player_name "..."
    show player 10
    player_name "Would you maybe like to be a part of it?"
    show player 5
    show old_annie 9
    annie "Pfft, absolutely not!"
    show old_annie 5
    annie "You do realize, {b}Mrs. Smith{/b} is trying to get that stupid show canceled, right?"
    show old_annie 6
    show player 12
    player_name "Yeah, I heard."
    show player 5
    show old_annie 3
    annie "So there's no way I could participate in it!"
    show old_annie 1
    show player 12
    player_name "You don't always have to listen to {b}Mrs. Smith{/b}, {b}Annie{/b}."
    show player 5
    show old_annie 5
    annie "I am head of the disciplinary committee, official hall monitor, and {b}Mrs. Smith{/b}'s second in command!"
    show old_annie 3
    annie "It's my sworn duty to follow her orders."
    show old_annie 1
    show player 12
    player_name "This isn't the military, {b}Annie{/b}..."
    show player 11
    show old_annie 7
    annie "SILENCE!"
    show old_annie 1
    show player 10
    player_name "But-"
    show player 11
    show old_annie 5
    annie "{b}Mrs. Smith{/b} wants that show canceled and plans have been set in motion."
    show old_annie 6
    show player 12
    player_name "... Plans?"
    show player 5
    show old_annie 9
    annie "Grr, I've said too much."
    show old_annie 1
    show player 11
    player_name "..."
    show old_annie 5
    annie "I suggest you just give up on the talent show. It's not going to happen, I assure you."
    show old_annie 8
    annie "Now, get out of my way so I can finish my patrol!"
    hide old_annie with dissolve
    show player 12
    player_name "What a whack job..."
    hide player with dissolve
    return

label school_dewitt_glue_mission_cult:
    scene expression player.location.background_blur with dissolve
    player_name "!!!"
    player_name "Shh, I hear something."

    scene cult_event 1
    with Dissolve(0.3)
    erik "..."
    erik "!!!"
    scene cult_event 2
    with Dissolve(0.3)
    player_name "Shhh!"
    player_name "Stay quiet..."
    scene cult_event 3
    with Dissolve(0.3)
    window hide
    pause
    scene cult_event 4
    with Dissolve(0.3)
    scene expression player.location.background_blur
    show player 22 at left
    show old_erik 51 at right
    with dissolve
    pause
    show player 10
    player_name "What the-"
    player_name "Who was that?"
    player_name "... And where are they going?"
    show player 5
    show old_erik 53
    erik "I don't like this, {b}[firstname]{/b}!"
    erik "We should get out of here!"
    show old_erik 52
    show player 10
    player_name "Calm down, dude."
    player_name "They don't know we're here."
    show player 5
    show old_erik 53
    erik "What do you think is up with the creepy outfits?"
    show old_erik 52
    show player 10
    player_name "I dunno."
    show player 92
    player_name "I think we should follow them."
    show player 90
    show old_erik 53
    erik "Are you nuts?!"
    show old_erik 52
    show player 92
    player_name "It'll be fine, {b}Erik{/b}!"
    player_name "Just stay behind me and keep quiet!"
    show player 90
    show old_erik 2 with dissolve
    erik "{i}*Sigh*{/i}"
    show old_erik 3 with dissolve
    erik "... Fine."
    hide player
    hide old_erik
    with dissolve
    return

label school_dewitt_pre_talent_show_chat:
    scene expression player.location.background_blur
    show old_kevin 23 at Position (xpos=600)
    show eve f_happy
    with dissolve
    show player 13 at left with dissolve
    eve "There he is!"
    show old_kevin 22 with dissolve
    kevin "Finally!"
    kevin "How did everything go last night?"
    show old_kevin 23 with dissolve
    eve "We were starting to worry you got caught or something..."
    show player 14
    player_name "Nope. Everything went smoothly."
    player_name "Have you guys seen {b}Mrs. Smith{/b} and {b}Annie{/b} this morning?"
    show player 13
    show old_kevin 9b
    kevin "Not for a while."
    kevin "You think they're really stuck up in her office?!"
    show old_kevin 23
    show player 17
    player_name "I hope so."
    show player 13
    eve @ f_laugh "Haha! This is so awesome!"
    show player 14
    player_name "Where's {b}Miss Dewitt{/b}?"
    show player 13
    eve "She's in the auditorium setting up for the show."
    show old_kevin 9b
    kevin "We were just getting ready to go help her."
    show old_kevin 23
    eve "Yeah, why don't you come with us?"
    show player 14
    player_name "Hmm, I'm gonna go {b}check on Mrs. Smith's office{/b} first."
    player_name "I want to make certain there won't be any surprises."
    show player 13
    show old_kevin 9b
    kevin "Yeah, that's probably a good idea."
    show old_kevin 23
    eve f_nervous "... Just promise me you'll be careful, {b}[firstname]{/b}."
    show player 17
    player_name "I will."
    show player 13
    eve f_happy "{b}Meet us in the auditorium{/b} when you're finished."
    hide eve
    hide old_kevin
    hide player
    with dissolve
    return

label school_weekend_lock:
    scene expression L_school_front.background_blur
    show anon with dissolve
    anon @ -m_talk "( It's the weekend. )"
    anon @ -m_talk "( The school is {b}closed until Monday{/b}. )"
    hide anon with dissolve
    return

label night_closed_school:
    if getPlayingSound("<loop 8 to 179>audio/ambience_suburb_night.ogg"):
        $ playSound("<loop 8 to 179>audio/ambience_suburb_night.ogg", 1.0)
    scene expression L_school_front.background_blur
    if False:
        if M_erik.get("webcam help"):
            $ player.go_to(L_school_hall)
            call expression game.dialog_select("school_erik_webcam_quest")
            call expression game.dialog_select("school_erik_webcam_quest_sneak_in")

            $ game.main()
        else:

            call expression game.dialog_select("school_erik_webcam_quest_need_help")
    else:

        call expression game.dialog_select("school_closed")
    call expression game.dialog_select("town_map_dialogue")

label school_closed:
    show anon with dissolve
    anon @ -m_talk "( The school is closed at night... I should come back tomorrow. )"
    hide anon with dissolve
    return

label school_hallway:
    $ player.go_to(L_school_hall)
    $ game.main()

label school_locker_smith_go_to_locker:
    scene expression L_school_hall.background_blur with None
    show anon f_worried:
        xzoom -1
    show annie:
        xzoom -1
    with {'master': dissolve}
    annie "Alright, let's get this over with."
    show annie a_key_get f_normal_down with {'master': dissolve}:
        xzoom 1
        xoffset -500
    pause
    show annie f_normal a_key with {'master': dissolve}
    anon f_normal @ f_surprised "Wow, so that key opens everybody's locker?"
    show annie a_key_get f_normal_down with {'master': dissolve}
    pause
    show annie a_idle f_normal with {'master': dissolve}:
        xzoom -1
        xoffset 0
    annie "Pfft, this key opens every lock and door in the school."
    anon f_surprised "For real?!"
    annie "Duh, that's why it's called a {b}{i}master key{/i}{/b}."
    anon f_skeptical "How come you get it?"
    annie f_annoyed "Umm, because I bust my ass every day helping {b}Mrs. Smith{/b} keep all you kids in line?!"
    anon f_worried "Kids? We're the same age..."
    annie @ f_normal "... Yeah, right. Everyone around here is so immature."
    anon "So you just have that {b}master key{/b} with you all the time?"
    annie "Of course not! {b}Mrs. Smith keeps it in her office{/b}, but we like, never have to use it."
    anon "Never?"
    annie f_smirk "Nobody else is dumb enough to lose their locker combination..."
    show anon f_depressed a_sides with dissolve
    annie f_normal "Hurry up and grab what you need."
    annie "We're gonna be late for Athletics class!"
    anon f_tired "Yeah, yeah. I'm going."
    return

label school_hallway_smith_unlocked_locker:
    scene expression player.location.background_blur with None
    show anon f_thinking a_thinking with {'master': dissolve}
    anon @ -m_talk "( Hmm, so {b}Mrs. Smith has a master key in her office somewhere{/b}. )"
    anon @ -m_talk "( ... {b}that would be a useful thing to have{/b}! )"
    anon @ -m_talk "( ... )"
    anon @ -m_talk "( Something to think about. )"
    anon @ -m_talk "( For now, I should {b}head to the boys' locker room{/b} and get changed for athletics class. )"
    return

label school_erik_webcam_quest:
    show player 14 at left
    show old_erik 1 at right
    player_name "Hey!"
    show player 17
    player_name "I thought you wouldn't show up."
    show player 1
    show old_erik 4
    erik "I told {b}Mrs. Johnson{/b} I went to see a movie at the mall..."
    show player 17
    show old_erik 1
    player_name "Nice."
    show player 11
    show old_erik 5
    erik "But I can't be out too long: I have to be home before bedtime."
    show player 92
    show old_erik 1
    player_name "You have a bedtime?!"
    show player 91
    show old_erik 3
    erik "... I just don't like to upset {b}Mrs. Johnson{/b}, you know?"
    show player 113
    show old_erik 1
    player_name "Anyway, we have to be quick and quiet!"
    show player 1
    show old_erik 5
    erik "Is there an alarm, though?"
    show old_erik 1
    show player 2
    player_name "We shouldn't have to worry about that if we use the window!"
    player_name "Just follow me..."
    hide player
    hide old_erik
    hide ui
    scene black
    return

label school_erik_webcam_quest_sneak_in:
    scene outside_school_night02a
    show text _ ("After some convincing, {b}Erik{/b} followed me to the right side of the school.\nWe quickly ran through the yard towards one of the main floor windows.") as caption
    with fade
    pause

    scene outside_school_night02b
    show text _ ("I had to give {b}Erik{/b} a boost first.\nI have to say, it was a lot harder than I thought...") as caption
    with fade
    pause

    scene outside_school_night02c
    show text _ ("It was then my turn, as I jumped up and snuck inside...\nWe had finally made it in, and no one had seen us.") as caption
    with fade
    pause

    $ playMusic()
    scene expression player.location.background_blur with fade
    player_name "!!!"
    player_name "I hear someone coming..."

    scene cult_event 1 with fastdissolve
    erik "What the-"
    scene cult_event 2 with fastdissolve
    player_name "Shhh!"
    player_name "Stay quiet..."
    scene cult_event 3 with fastdissolve
    pause
    scene cult_event 4 with fastdissolve

    scene expression player.location.background_blur
    show player 22 at left
    show old_erik 5 at right
    with dissolve
    erik "I have a bad feeling about this..."
    show player 10
    show old_erik 1
    player_name "Yeah, something's going on here."
    show player 11
    show old_erik 5
    erik "What are they doing in the school this late?"
    erik "... And wearing those strange outfits?"
    show player 92
    show old_erik 1
    player_name "Let's follow them and see where they're going."
    show player 91
    show old_erik 5
    erik "Really? 'Cause I was thinking maybe we should just leave..."
    show player 26
    show old_erik 3
    player_name "Don't be a chicken!"
    player_name "Plus, we still haven't finished what we came here for..."
    show player 91
    show old_erik 2
    erik "{i}*Sigh*{/i}"
    show old_erik 3
    erik "Fine..."
    hide player 91 with dissolve
    hide old_erik 3 with dissolve
    return

label school_erik_webcam_quest_need_help:
    show player 114 with dissolve
    player_name "Hmm..."
    show player 10
    player_name "( I'm gonna need some {b}help{/b} sneaking into the school at night. )"
    hide player 10 with dissolve
    return

label school_roxxy_dexter_argument:
    scene expression player.location.background_blur
    show eve f_happy
    show old_kevin 23f at Position (xpos=500)
    with dissolve
    eve "Yeah, they are out there arguing right now!"
    show old_kevin 9bf
    kevin "Hah, they are the worst..."
    kevin "They totally deserve each other!"
    show old_kevin 23f
    eve "I know right..."
    eve "C'mon, we should go check it out before it's over."
    show old_kevin 9bf
    kevin "... I'm good. Their stupid drama doesn't do anything for me..."
    show old_kevin 23f
    show player 14 at left with dissolve
    player_name "What's going on guys?"
    show player 13
    show old_kevin 9b with dissolve
    kevin "Heya, bruh!"
    show old_kevin 23
    eve @ a_wave "Hey, {b}[firstname]{/b}."
    eve "{b}Roxxy{/b} and {b}Dexter{/b} are causing some big scene over at the basketball court."
    eve "I was just about to go check it out."
    eve "... Wanna come with?"
    show player 14
    player_name "Yeah, okay."
    player_name "Let's go."
    show player 13
    show old_kevin 9b
    kevin "See you guys later!"
    hide player
    hide old_kevin
    hide eve
    with dissolve
    return

label school_roxxy_dexter_confront:
    scene expression player.location.background_blur
    show player 5 at left
    show old_dexter 1 at right
    show old_dexter 4
    with dissolve
    dexter "{b}[firstname]{/b}!"
    show old_dexter 2 with dissolve
    show player 10
    player_name "Oh, man. Here we go..."
    player_name "What do you want, {b}Dexter{/b}?"
    show player 5
    show old_dexter 6 with dissolve
    dexter "Have you been perving on {b}Roxxy{/b} in the shower?!"
    show old_dexter 5
    show player 12
    player_name "Who told you that?"
    show player 11
    show old_dexter 8 with dissolve
    dexter "... {b}Becca{/b}!"
    show old_dexter 6 with dissolve
    dexter "Is it true?"
    show old_dexter 2 with dissolve
    show player 10
    player_name "No!"
    player_name "I just went to take a shower after my gym class."
    player_name "It's not my fault {b}Roxxy{/b} was already in there!"
    show player 5
    dexter "..."
    show old_dexter 6 with dissolve
    dexter "So you WERE perving on her!"
    show old_dexter 2 with dissolve
    show player 10
    player_name "Huh?"
    show player 12
    player_name "No!"
    player_name "Weren't you listening?!"
    player_name "Look man, I wasn't in there to perv on {b}Roxxy{/b}..."
    player_name "I needed to shower!"
    player_name "I promised her I wouldn't look."
    show player 11
    dexter "..."
    hide player
    show old_dexter 7 at left

    player_name "{i}*Gurt*{/i}" with hpunch
    show player 89 at left
    show old_dexter 1 at right
    show old_dexter 6
    with dissolve
    dexter "Leave {b}Roxxy{/b} alone!"
    show old_dexter 5
    show player 88
    player_name "{i}*Wheeze*{/i}"
    show old_dexter 6
    dexter "She's mine!"
    dexter "Understand?!"
    show old_dexter 5
    player_name "{i}*Gasp*{/i}"
    show player 89
    show old_dexter 4 with dissolve
    dexter "Go near her again and I'll bash your face in!"
    show old_dexter 2 with dissolve
    show player 88
    player_name "{i}*Cough* *Cough*{/i}"
    show player 10 with dissolve
    player_name "... I thought you two were finished?"
    show player 90
    show old_dexter 8
    dexter "... Huh?"
    dexter "Who said that?"
    show old_dexter 2
    show player 10
    player_name "You did!"
    player_name "The other day, at the basketball court."
    show player 90
    show old_dexter 6 with dissolve
    dexter "It's not over!"
    dexter "She'll apologize, and we'll get back together."
    show old_dexter 2 with dissolve
    show player 10
    player_name "... I'm not so sure."
    show player 90
    show old_dexter 15 at Position (xoffset=2) with dissolve
    dexter "You want another one?!"
    show old_dexter 14 at Position (xoffset=2)
    show player 88 with dissolve
    player_name "{i}*Cough*{/i} ... Please, no."
    show player 89
    show old_dexter 15 at Position (xoffset=2)
    dexter "Then stay away from my girl!"
    dexter "Got it?!"
    show old_dexter 14 at Position (xoffset=2)
    show player 10 with dissolve
    player_name "... Yeah, I got it."
    show player 90
    show old_dexter 15 at Position (xoffset=2)
    dexter "That's what I thought!"
    hide old_dexter with dissolve
    show player 16
    player_name "( ... )"
    player_name "( You're gonna get yours one day, {b}Dexter{/b}. )"
    hide player with dissolve
    return

label school_roxxy_assignment:
    scene expression player.location.background_blur
    show teacher 18f at left
    show old_roxxy 33 zorder 1 at right
    with dissolve
    roxxy "No, {b}Miss Bissette{/b}! I'm begging you here!"
    roxxy "Please, don't fail me!"
    show old_roxxy 32
    show teacher 19f
    bissette "I have been telling you, silly girl!"
    bissette "Turning in other student's work is inexcusable!"
    bissette "I am sick of saying these things!"
    show teacher 18f
    show old_roxxy 33
    roxxy "C'mon! There's gotta be something I can do!"
    roxxy "Just give me one more chance!"
    show old_roxxy 32
    show teacher 3f
    bissette "Hah!"
    show teacher 19f
    bissette "I have given you many chances already!"
    show teacher 18f
    show old_roxxy 33
    roxxy "I'll study and do the work myself this time."
    roxxy "I promise!"
    roxxy "Just one more chance!"
    show old_roxxy 32
    show teacher 20f
    bissette "..."
    show player 13f zorder 0 at Position (xpos=650) with dissolve
    show teacher 2f
    bissette "Oh, {b}[firstname]{/b}!"
    bissette "This is good timing, yes?!"
    show teacher 5f
    bissette "{b}Roxanne{/b} here was just caught trying to hand in your homework!"
    show teacher 19f
    bissette "... This, after I tell her, \"I fail you, if you do this again!\""
    bissette "Now she is wanting yet another chance!"
    show teacher 5f
    bissette "What say you?"
    bissette "Should I to be giving her this chance?"
    show teacher 4f
    roxxy "..."
    show player 11f
    player_name "..."
    show player 10f
    player_name "I uhh..."
    player_name "... Yes?"
    show player 5f
    show teacher 20f
    bissette "Hmm..."
    pause
    show teacher 2f
    bissette "Tsk, you are too kind-hearted, {b}[firstname]{/b}!"
    show teacher 12f
    bissette "... But you are also too cute to refuse!"
    show old_roxxy 1e
    show player 13f
    bissette "Very well."
    show teacher 19f
    bissette "This is to be your last chance {b}Roxanne{/b}!"
    show teacher 18f
    show old_roxxy 1d
    roxxy "Phew, thank you!"
    show old_roxxy 1e
    show teacher 19f
    bissette "... And to make sure you do things right..."
    show teacher 3f
    bissette "{b}[firstname]{/b} here is going to be your study partner!"
    show player 22f
    show teacher 1f
    show old_roxxy 3c with dissolve
    roxxy "What?!"
    roxxy "No freaking way that is happening!"
    show old_roxxy 3d
    show teacher 3f
    bissette "Ah ah ah!"
    show teacher 2f
    bissette "What has become of your, \"I will do anything!\", hmm?"
    show teacher 1f
    show old_roxxy 2
    roxxy "... Yeah, but..."
    show old_roxxy 3c
    roxxy "... Why him?!"
    show old_roxxy 14
    if M_bissette.is_state(S_bissette_end):
        show teacher 12f
        bissette "{b}[firstname]{/b} here is my best student!"
        bissette "Who better to help you with your studies, yes?"
        show teacher 13f
    else:
        show teacher 2f
        bissette "{b}[firstname]{/b} is trying to make up work as well."
        bissette "It seems fitting you should be helping one another to catch up, yes?"
        show teacher 1f
    show player 10f
    player_name "I really have to do this?"
    show player 5f
    show teacher 2f
    bissette "It was your idea to be giving her another chance!"
    bissette "I expect you to make sure she really does the studying!"
    show teacher 1f
    show player 24f
    player_name "{i}*Sigh*{/i}"
    player_name "Okay..."
    show teacher 3f
    bissette "Très bien!"
    show teacher 2f
    bissette "I leave you to it!"
    hide teacher with dissolve
    show player 5 at left with dissolve
    show old_roxxy 29
    roxxy "..."
    player_name "..."
    show old_roxxy 30
    roxxy "Ugh, this sucks!"
    show old_roxxy 29
    show player 10
    player_name "Just relax... It won't be that bad."
    player_name "I'll just swing by your place later, and we'll get it over with quickly..."
    show player 5
    show old_roxxy 2
    roxxy "You want to come to my place?"
    show old_roxxy 3
    roxxy "I don't want you there!"
    show old_roxxy 3d
    show player 10
    player_name "Would you rather go to the library or something?"
    show player 5
    show old_roxxy 3c
    roxxy "... And be seen in public with YOU..."
    roxxy "Eww, no."
    show old_roxxy 14
    show player 12
    player_name "Well then..."
    show player 11
    dexter "Hey, {b}Missy{/b}! You seen {b}Roxxy{/b} today?!"
    missy "Yeah, she was on her way to see {b}Miss Bissette{/b}..."
    show old_roxxy 2b
    roxxy "!!!" with hpunch
    show old_roxxy 2c
    roxxy "Oh shit!"
    roxxy "Umm..."
    roxxy "Hide!"

    scene location_school_cutscene03
    show text _ ("Before I knew what was happening {b}Roxxy{/b} had flung open my locker and shoved me inside.") as caption
    with fade
    pause

    scene expression player.location.background_blur
    show old_roxxy 7f at left
    show old_dexter 8 at right
    with fade
    dexter "There you are."
    show old_dexter 2
    show old_roxxy 11f with dissolve
    roxxy "... Yeah, I'm here. What's up?"
    show old_roxxy 9f
    show old_dexter 8
    dexter "Just thought I'd see if you were ready to apologize yet?"
    show old_dexter 2
    show old_roxxy 11f
    roxxy "Pfft, apologize for what?"
    show old_roxxy 9f
    show old_dexter 6 with dissolve
    dexter "You know what!"
    dexter "You called me names!"
    show old_dexter 2
    show old_roxxy 11f
    roxxy "You mean stupid?"
    dexter "..."
    show old_roxxy 5f with dissolve
    roxxy "Well, don't act so stupid and I won't call you stupid... Stupid."
    show old_roxxy 6f with dissolve
    dexter "Grrr..."
    show old_dexter 6
    dexter "STOP CALLING ME STUPID!" with hpunch
    show old_dexter 5
    show old_roxxy 10f with dissolve
    roxxy "... Or what?"
    show old_roxxy 7f with dissolve
    show old_dexter 2 with dissolve
    dexter "..."
    show old_dexter 8
    dexter "You're lucky you're my girlfriend!"
    dexter "If anybody else talked to me like this..."
    show old_dexter 4
    dexter "I'd smash their faces in!" with hpunch
    show old_dexter 2
    show old_roxxy 11f
    with dissolve
    roxxy "Uh huh."
    roxxy "Are you done whining?"
    show old_roxxy 9f
    show old_dexter 8
    dexter "Whatever."
    dexter "You'll apologize eventually."
    show old_dexter 6 with dissolve
    dexter "Just remember. Until you do, don't ask me for nothin'!"
    show old_dexter 2 with dissolve
    show old_roxxy 10f
    roxxy "Like I need anything from you!"
    roxxy "You'd probably just screw it up, even if I did!"
    show old_roxxy 6f with dissolve
    dexter "..."
    show old_dexter 4 with dissolve
    dexter "Rrraaaggh!!!" with hpunch
    show old_dexter 6 with dissolve
    dexter "You're such a bitch!"
    hide old_dexter with dissolve
    show old_roxxy 7f
    roxxy "..."
    show old_roxxy 1b at right with dissolve
    roxxy "Alright, come on out, {b}[firstname]{/b}."
    show old_roxxy 1
    pause
    show player 12 at left with dissolve
    player_name "Is it really a good idea to antagonize him like that?"
    show player 5
    show old_roxxy 1b
    roxxy "Huh?"
    show old_roxxy 3c
    roxxy "Whatever. Fuck him! He's a dick!"
    show old_roxxy 3d
    show player 10
    player_name "Yeah, but he's not exactly the most stable person in the world..."
    player_name "Why are you dating him anyways?"
    show player 12
    player_name "You're like, way out of his league!"
    show player 5
    show old_roxxy 2
    roxxy "Pfft, please. I'm way out of everyone's league!"
    roxxy "Dating {b}Dexter{/b} means nobody else messes with me."
    show old_roxxy 1h
    roxxy "It's just easier."
    show old_roxxy 1g
    show player 10
    player_name "Yeah, but he's so..."
    show player 5
    show old_roxxy 2
    roxxy "... Stupid?"
    show old_roxxy 1
    show player 17
    player_name "Haha, yeah!"
    show player 13
    show old_roxxy 4
    roxxy "Hahaha!"
    show old_roxxy 1
    pause
    show player 11
    player_name "..."
    roxxy "..."
    show player 10
    player_name "{i}*Ahem*{/i} So... I guess {b}I'll come around your place tonight{/b}?"
    show player 5
    show old_roxxy 30
    roxxy "{i}*Sigh*{/i} Fine."
    roxxy "Just don't expect much from me with the studying. It's not my strong suit."
    show old_roxxy 29
    show player 14
    player_name "No worries. I'll show you the ropes!"
    show player 13
    roxxy "..."
    show player 36 with dissolve
    player_name "See ya {b}tonight{/b}."
    show player 13
    show old_roxxy 30
    roxxy "... Uh huh."
    show old_roxxy 29
    hide player with dissolve
    roxxy "..."
    pause
    show old_roxxy 1g
    pause
    return

label school_roxxy_missing_outfit:
    scene expression player.location.background_blur
    show old_becca 1 at Position(xpos=315)
    show old_missy 2b at left
    show old_roxxy 3c zorder 1 at right
    with dissolve
    roxxy "... Ugh, did you two find it?"
    show old_roxxy 3b
    show old_becca 2
    becca "Nope."
    show old_becca 1
    show old_missy 2
    missy "Are you sure you didn't leave it at home?"
    show old_missy 2b
    show old_roxxy 3c
    roxxy "Of course I'm sure, {b}Missy{/b}!"
    roxxy "What, do I look like an idiot or something?"
    show old_roxxy 3b
    show old_becca 3
    show old_missy 1b
    missy "I didn't say that!"
    show old_missy 3
    show old_becca 3b
    becca "You might as well have..."
    show old_becca 3
    show old_missy 2
    missy "I'm just trying to help!"
    show old_missy 2b
    show old_becca 4
    becca "Hahaha, worst help ever!"
    show old_becca 5
    show old_roxxy 30
    roxxy "{i}*Sigh*{/i} I don't suppose one of you brought an extra uniform?"
    show old_roxxy 29
    show old_becca 2
    becca "Nope. My backup is in the wash."
    show old_becca 3
    show old_missy 1b
    missy "Yeah, I didn't bring mine either."
    show old_missy 1
    show old_becca 8
    becca "With {b}Missy{/b}'s tiny tits, her uniform wouldn't fit you anyways..."
    show old_becca 7
    show old_missy 4
    missy "Shuddup, skank!"
    show old_missy 2b
    show old_becca 4
    becca "Hahaha, don't worry. You'll hit puberty someday..."
    show old_becca 5
    show old_roxxy 3c
    roxxy "{i}*Sigh*{/i} You two are worthless, you know that?"
    show old_roxxy 3b
    show old_becca 2
    becca "Pssh, whatever."
    show old_becca 1
    show old_missy 2
    missy "It's not our fault you left your uniform at home!"
    show old_missy 2b
    show old_roxxy 30
    roxxy "I guess we'll just have to go and get it."
    show old_roxxy 3b
    show old_becca 2b with dissolve
    becca "What?!"
    becca "You want us to walk to your place right now?!"
    show old_becca 1 with dissolve
    show old_missy 2
    missy "Yeah, fuck that!"
    show old_missy 2b
    show old_roxxy 3c
    roxxy "C'mon you dumb bitches!"
    roxxy "I don't wanna walk there all by myself!"
    show old_roxxy 3b
    show old_missy 2
    missy "No way!"
    missy "If I skip another French lesson, {b}Miss Bissette{/b} is going to write my parents..."
    show old_missy 2b
    show old_becca 3b
    becca "Ooh, your mom would totally whoop your ass if that happened!"
    show old_becca 3
    show old_missy 1b
    missy "I know, right?"
    show old_missy 1
    show old_roxxy 2
    roxxy "Fine, we'll just go without you... Right, {b}Becca{/b}?"
    show old_roxxy 1
    show old_becca 2b with dissolve
    becca "..."
    show old_roxxy 3b
    roxxy "Seriously?!"
    show old_roxxy 3c
    show old_becca 2 with dissolve
    becca "It's too hot to walk all the way to your place!"
    becca "... And besides, your cousin freaks me out."
    show old_becca 1
    show old_roxxy 31
    show old_missy 2b
    roxxy "You guys suck!"
    show old_roxxy 3d
    show player 14f zorder 0 at Position (xpos=600) with dissolve
    player_name "Hey, girls!"
    player_name "What's going on?"
    show player 13f
    show old_becca 2
    becca "... Umm, why are you talking to us?"
    show old_becca 1
    show player 11f
    show old_missy 1b
    missy "Nerd alert!"
    show old_missy 1
    show old_roxxy 27 with dissolve
    roxxy "..."
    show player 5 with dissolve
    show old_roxxy 28
    roxxy "I {b}forgot my cheerleading uniform at home{/b}."
    show old_roxxy 1n
    roxxy "... And \"my friends\" here, are too good to go with me to get it."
    show old_roxxy 1m
    show player 5f with dissolve
    show old_missy 1b
    missy "Hey, I totally would if it wasn't for {b}Miss Bissette{/b}!"
    show old_missy 1
    show old_roxxy 1n
    roxxy "... Whatever."
    show old_roxxy 1m
    show player 10 with dissolve
    player_name "I'll go with you."
    show old_roxxy 1k
    player_name "... You know, if you want?"
    show player 5
    show old_roxxy 1i
    show old_becca 2b with dissolve
    becca "Eww..."
    becca "Why would she want to go anywhere with you, geek boy?!"
    show old_becca 1 with dissolve
    show old_roxxy 1j
    roxxy "..."
    pause
    show old_roxxy 1l
    roxxy "... Fine, let's go."
    show old_roxxy 1k
    show player 13
    show old_becca 2b with dissolve
    becca "WHAT?!"
    becca "You're seriously going with this loser?"
    show old_becca 1
    show old_roxxy 3
    with dissolve
    roxxy "Well, I don't wanna walk across town on my own!"
    roxxy "... And since you two slutbags won't come..."
    show old_roxxy 3c
    show player 5
    roxxy "... What choice to do I have?"
    show old_roxxy 3b
    show old_becca 2
    show player 5f with dissolve
    becca "Yeah, but I mean... Just look at him..."
    becca "... He's so..."
    show old_becca 1
    show old_missy 8
    missy "... Losery?"
    show old_missy 7
    show old_becca 4
    becca "Haha, yeah!"
    show old_becca 5
    show old_missy 3
    show player 12f
    player_name "That's not even a word!"
    show player 90f
    show old_roxxy 3c
    roxxy "Ugh, would you two shuddup already?!"
    roxxy "C'mon, {b}[firstname]{/b}. Let's get this over with."
    hide old_roxxy with dissolve
    player_name "..."
    show player 12f
    player_name "... See ya, slutbags!"
    hide player with dissolve
    show old_becca 1
    becca "..."
    show old_becca 3
    show old_missy 6
    missy "Pfft, hahaha!"
    show old_missy 7
    show old_becca 2f at Position (xpos=400) with dissolve
    becca "What are you laughing at?!"
    show old_becca 1f
    show old_missy 6
    missy "... That nerd just called you a slutbag!"
    show old_missy 7
    show old_becca 2f
    becca "Umm, he called both of us slutbags, moron."
    show old_becca 1f
    show old_missy 3
    missy "..."
    show old_missy 5
    missy "Oh, right..."
    show old_missy 4
    missy "Hey, don't call me moron, you twat!"
    scene black with fade
    return

label school_roxxy_return_to_school:
    scene expression player.location.background_blur
    show player 14 at Position (xpos=500)
    show old_roxxy 23 at right
    show old_roxxy_outfit cheer at right
    with dissolve
    player_name "Looks like we made it back in time."
    show player 13
    show old_roxxy 24
    roxxy "... Thanks for your help today."
    show old_roxxy 23
    show player 14
    player_name "Not a problem, {b}Roxxy{/b}!"
    show player 13
    show old_becca 5 at Position(xpos=315)
    show old_becca_outfit cheer at Position (xpos=315)
    show old_missy 1b at left
    show old_missy_outfit cheer at left
    with dissolve
    show player 13f at Position (xpos=600) with dissolve
    missy "Hey, you found it?!"
    show old_missy 1
    show old_becca 6
    becca "... Uhh, obviously."
    becca "She's wearing it, isn't she?"
    show old_becca 5
    show old_missy 2
    missy "Oh, shuddup!"
    show old_missy 2b
    show old_becca 8
    becca "What's the geek still doing here?"
    show old_becca 7
    show player 5f
    show old_roxxy 23b
    roxxy "... Don't call him names."
    show old_roxxy 23
    show old_becca 2
    becca "Huh?"
    show old_becca 1
    show old_roxxy 24
    roxxy "... He's a nice guy."
    show old_roxxy 23
    show old_becca 8
    becca "What, are you in love with him now or something?"
    show old_becca 7
    show old_roxxy 23c
    roxxy "Pfft, no!"
    show old_roxxy 24
    roxxy "He just helped me out of a jam today is all and I think you should be nicer to him."
    show old_roxxy 23
    show old_becca 4
    becca "Hah, whatever!"
    show old_becca 8
    becca "I think you've got a little crush on {b}[firstname]{/b}!"
    show old_becca 4
    becca "Haha!"
    show old_becca 8
    becca "What do you think, {b}Missy{/b}?"
    show old_becca 7
    show old_missy 8
    missy "... Yeah, he's kinda cute."
    show old_missy 7
    show old_becca 3
    becca "!!!" with hpunch
    show old_becca 3b
    show old_missy 3
    becca "That's not what I meant!"
    show old_becca 2
    becca "What's the matter with you two?!"
    show old_becca 1
    show old_missy 1
    roxxy "..."
    show old_becca 2
    becca "Ugh, I'm going to practice!"
    hide old_becca
    hide old_becca_outfit cheer
    with dissolve
    show old_missy 2
    missy "{b}Becca{/b}, hold up!"
    missy "... I didn't understand the question!"
    hide old_missy
    hide old_missy_outfit cheer
    with dissolve
    roxxy "..."
    show player 10 at Position (xpos=500) with dissolve
    player_name "... Thanks for saying that."
    show player 13
    show old_roxxy 23b
    roxxy "Huh?"
    show old_roxxy 24
    roxxy "Oh, right."
    roxxy "Whatever."
    roxxy "Don't let it go to your head!"
    show old_roxxy 23b
    roxxy "I don't like you or anything. I just appreciate your help is all."
    show old_roxxy 23
    show player 14
    player_name "O-okay."
    player_name "I guess I'll see you around."
    show player 13
    show old_roxxy 24
    roxxy "Yeah, we'll see..."
    hide old_roxxy
    hide old_roxxy_outfit cheer
    with dissolve
    player_name "( Well, that was a crazy day... )"
    player_name "( I think {b}Roxxy{/b} is actually starting to warm up to me! )"
    show player 18
    player_name "( I should look for more opportunities to get close with her. )"
    return

label school_roxxy_trailer_park_trouble:
    scene expression player.location.background_blur
    show old_annie 3 at right
    show old_roxxy 3df zorder 1 at left
    with dissolve
    annie "The student handbook is very clear on this matter!"
    annie "Students are not allowed to have their cell phones out while on school property."
    show old_annie 1
    show old_roxxy 3f
    roxxy "Go away, you psychotic little brown noser!"
    show old_roxxy 3df
    show player 10f zorder 0 at Position (xpos=500) with dissolve
    player_name "What's going on?"
    show player 5f
    show old_roxxy 3f
    roxxy "I'm having a crisis here!"
    show old_roxxy 3df
    show player 5 at Position (xpos=400) with dissolve
    show old_annie 5
    annie "Irrelevant!"
    annie "No cell phones on school property and this is school property!"
    show old_annie 3
    annie "You have to put it away!"
    show old_annie 1
    show old_roxxy 3f
    roxxy "Back off, {b}Annie{/b} or I swear I'm going to pop you one, right in the face!"
    show old_roxxy 3bf
    show old_annie 5
    annie "Pfft, you don't frighten me..."
    show old_annie 6
    annie "..."
    show old_annie 5
    annie "... I'm getting {b}Mrs. Smith{/b}!"
    hide old_annie with dissolve
    show old_roxxy 3df
    show player 10f at Position (xpos=600) with dissolve
    player_name "What happened?"
    show player 5f
    show old_roxxy 33f
    roxxy "Apparently, the cops just showed up and arrested my mom!"
    show old_roxxy 32f
    show player 10f
    player_name "What?!"
    player_name "Why would they do that?"
    show player 11f
    show old_roxxy 33f
    roxxy "I don't know!"
    roxxy "I've gotta get home..."
    show old_roxxy 32f
    player_name "..."
    show player 10f
    player_name "You want me to walk with you?"
    show player 5f
    show old_roxxy 32f
    roxxy "..."
    show old_roxxy 1lf
    roxxy "You'd really do that?"
    show old_roxxy 32f
    show player 10f
    player_name "... Sure, I don't mind!"
    show player 5f
    roxxy "..."
    show old_roxxy 1lf
    roxxy "Thanks, {b}[firstname]{/b}."
    roxxy "C'mon, let's get out of here before {b}Annie{/b} comes back."
    show old_roxxy 32f
    show player 12f
    player_name "Right behind you."
    hide old_roxxy
    hide player
    with dissolve
    return

label school_roxxy_selling_meth_ask_roxxy:
    scene expression player.location.background_blur
    show old_roxxy 14f at Position (xpos=500)
    show old_becca 1 at Position(xpos=315)
    show old_missy 1 at left
    show player 14f at right
    with dissolve
    player_name "Hey {b}Roxxy{/b}, I need to speak with you!"
    show player 13f
    show old_becca 2
    becca "Ugh, get lost loser!"
    show old_becca 1
    show old_missy 2
    missy "Yeah, can't you see she has enough problems?!"
    show old_missy 2b
    show player 14f
    player_name "I think I found a way to fix all of this!"
    show player 13f
    show old_missy 2
    missy "Pfft, yeah right!"
    show old_missy 2b
    show old_becca 2
    becca "What's a nerd like you going to do?"
    show old_becca 1
    show old_roxxy 29f
    show player 12f
    player_name "Can I please just talk to you for a second?"
    show player 90f
    show old_becca 2
    becca "I said get lost!"
    show old_becca 1
    show old_missy 2
    missy "Yeah, ge-"
    show old_missy 3
    show old_roxxy 30f
    roxxy "Would you two shut up already!"
    show player 11f
    roxxy "{i}*Sigh*{/i} Just go on to class, I wanna hear him out."
    show old_roxxy 29f
    show player 13f
    show old_becca 2b with dissolve
    becca "You're serious?"
    show old_becca 1
    show old_roxxy 3 at Position (xpos=600)
    with dissolve
    roxxy "Just go!"
    show old_roxxy 3b
    show old_missy 2b
    show old_becca 2
    becca "Tch, fine!"
    show old_becca 3b
    becca "C'mon {b}Missy{/b}!"
    hide old_becca
    hide old_missy
    with dissolve
    pause
    show old_roxxy 3cf at Position (xpos=500) with dissolve
    roxxy "So, how exactly are you gonna fix all this?"
    show old_roxxy 3df
    show player 14f
    player_name "Well, I convinced {b}Clyde{/b} to turn himself in!"
    show player 13f
    show old_roxxy 30f
    roxxy "... Great."
    show old_roxxy 3df
    show player 5f
    player_name "..."
    show player 10f
    player_name "That's it?"
    show player 5f
    show old_roxxy 3cf
    roxxy "Did you forget?"
    roxxy "Even if he confesses, my mom will stay in jail until her trial."
    roxxy "We'll still lose the trailer."
    show old_roxxy 3df
    show player 14f
    player_name "Well, I've got a plan for that as well!"
    player_name "{b}Clyde{/b} says he's got more than enough meth to make fifty thousand dollars!"
    show player 13f
    show old_roxxy 2f
    roxxy "Pfft, {b}Clyde{/b} says..."
    show old_roxxy 3cf
    show player 5f
    roxxy "That moron can barely tie his shoes!"
    roxxy "... And you think he can really sell all that meth?!"
    show old_roxxy 3df
    player_name "..."
    show player 10f
    player_name "Doesn't he do it all the time?"
    show player 5f
    show old_roxxy 4f
    roxxy "Hahaha! Are you kidding me?"
    show old_roxxy 3cf
    roxxy "He cooks it but my mom does all the selling!"
    show old_roxxy 3df
    show player 11f
    player_name "..."
    show old_roxxy 2bf
    roxxy "!!!"
    show old_roxxy 3cf
    roxxy "I never said that! Understand!"
    show old_roxxy 3df
    show player 10f
    player_name "Don't worry, I'm not gonna tell anybody."
    show player 5f
    show old_roxxy 30f
    roxxy "Look, I appreciate you trying to help, {b}[firstname]{/b}."
    show old_roxxy 3cf
    roxxy "... But you're better off just forgetting about me and my problems!"
    hide old_roxxy with dissolve
    player_name "..."
    show player 4f
    player_name "( Well, now what? )"
    player_name "( I guess I should head {b}back to Clyde{/b}... )"
    hide player with dissolve
    return

label school_roxxy_shut_down_lab:
    scene expression player.location.background_blur
    show old_roxxy 32f at Position (xpos=500)
    show old_becca 2 at Position(xpos=315)
    show old_missy 1 at left
    show player 13f at right
    with dissolve
    becca "Ugh, back again?"
    show old_becca 1
    show old_missy 2
    missy "What do you want now, loser?!"
    show old_missy 2b
    show player 5f
    show old_roxxy 30f at Position (xoffset=34)
    roxxy "Oh. My. God."
    show old_roxxy 3 at Position (xpos=600) with dissolve
    roxxy "Would you two just cut it out?"
    roxxy "I'm not in the mood for all of this."
    show old_roxxy 3d
    show old_missy 3
    missy "..."
    show old_becca 2
    becca "... So what? We're supposed to be nice to this nerd now?"
    show old_becca 1
    show old_roxxy 3c
    roxxy "Just let us talk."
    show old_roxxy 3d
    show player 13f
    show old_becca 2
    becca "Fine."
    show old_becca 3b
    becca "C'mon, {b}Missy{/b} let's leave {b}Roxxy{/b} and her nerdy little boy toy to chat."
    hide old_becca with dissolve
    show old_roxxy 3c
    roxxy "Ugh, quit being a bitch, {b}Becca{/b}!"
    show old_roxxy 3d
    show old_missy 1b
    missy "Hey, wait for me!"
    hide old_missy with dissolve
    pause
    show old_roxxy 3cf at Position (xpos=500) with dissolve
    roxxy "What do you want, {b}[firstname]{/b}?"
    show old_roxxy 3df
    show player 14f
    player_name "I brought you something!"
    show player 239_240f with dissolve
    pause
    show player 650f with dissolve
    pause
    show old_roxxy 68bf
    show player 13f
    with dissolve
    roxxy "..."
    show old_roxxy 68cf
    roxxy "God he's dumb."
    show old_roxxy 1f f with dissolve
    show player 14f
    player_name "Heh, yeah..."
    show player 13f
    show old_roxxy 2f
    roxxy "I thought I told you to forget about all this?"
    show old_roxxy 1f f
    show player 14f
    player_name "Yeah, you did."
    show player 13f
    show old_roxxy 2f
    roxxy "So why are you still-"
    show old_roxxy 2bf
    show player 14f
    player_name "I brought you something else too!"
    show player 239_240f with dissolve
    pause
    show player 638bf
    roxxy "!!!" with hpunch
    show old_roxxy 80f at Position (xoffset=47)
    show player 13f
    with dissolve
    pause
    show old_roxxy 82f at Position (xoffset=47)
    roxxy "Holy shit!"
    roxxy "I've never seen this much money before!"
    roxxy "How did you..."
    show old_roxxy 81f at Position (xoffset=47)
    show player 14f
    player_name "{b}Clyde{/b} and I sold the meth last night."
    show player 13f
    show old_roxxy 82f at Position (xoffset=47)
    roxxy "Are you serious?!"
    show old_roxxy 81f at Position (xoffset=47)
    show player 14f
    player_name "Yeah. We made sixty thousand dollars!"
    player_name "That should be plenty to bail your mom out... Right?"
    show player 13f
    show old_roxxy 80f at Position (xoffset=47)
    roxxy "..."
    show old_roxxy 1bf with dissolve
    roxxy "I can't believe you did all this!"
    show old_roxxy 1f f
    roxxy "..."
    show old_roxxy 1bf
    roxxy "{b}[firstname]{/b}, why are you doing all this?!"
    roxxy "You don't owe me anything and I've only ever been mean to you."
    show old_roxxy 1f f
    show player 14f
    player_name "... 'Cause it's the right thing to do."
    show player 13f
    show old_roxxy 1if at Position (xoffset=-34) with dissolve
    roxxy "..."
    show old_roxxy 1lf at Position (xoffset=-34)
    roxxy "I don't know what to say..."
    show old_roxxy 1kf
    show player 14f
    player_name "You don't have to say anything."
    player_name "Just go and get your home back."
    show player 13f
    pause
    hide player
    show old_roxxy 59f at right
    player_name "!!!" with hpunch
    roxxy "Thank you, {b}[firstname]{/b}!"
    roxxy "I'm not going to forget this!"
    hide old_roxxy
    show old_roxxy 1f f at Position (xpos=500)
    show player 14f at right
    with dissolve
    player_name "... No problem!"
    show player 13f
    show old_roxxy 1bf
    roxxy "I'd better get down to the station and get {b}Mom{/b} out!"
    roxxy "I'll talk with you soon, okay?"
    show old_roxxy 1f f
    show player 14f
    player_name "Alright. Good luck!"
    show player 13f
    hide old_roxxy with dissolve
    pause
    hide player
    show player 17f
    with dissolve
    player_name "( Wow! )"
    player_name "( {b}Roxxy{/b} just hugged me in public! )"
    show player 13f
    player_name "( Well, sorta... Nobody was around to see it... )"
    player_name "( ... But it's still progress! )"
    player_name "( I should look for more opportunities to spend time with her once things settle down! )"
    hide player with dissolve
    return

label school_roxxy_give_exams:
    $ player.go_to(L_school_hall)
    scene expression player.location.background_blur
    show player 14 at left
    show old_roxxy 1 at right
    with dissolve
    player_name "Hey, {b}Roxxy{/b}!"
    show player 17
    player_name "I've got something for you."
    show player 13
    show old_roxxy 1b
    roxxy "You mean..."
    roxxy "You have the exams?"
    show old_roxxy 1
    show player 14
    player_name "Heh, yeah!"
    player_name "She was keeping them in her bedroom, can you believe that?!"
    show player 239_240 with dissolve
    pause
    show player 643 with dissolve
    pause
    hide player
    show old_roxxy 59 at left
    with dissolve
    roxxy "Oh my god, you're the best {b}[firstname]{/b}!"
    player_name "!!!" with hpunch
    show old_roxxy 64b at right
    show player 14 at left
    with dissolve
    player_name "Err, thanks..."
    show player 13
    show old_roxxy 64c
    roxxy "You know..."
    roxxy "I really like a guy who isn't afraid to stick their neck out for their girl."
    show old_roxxy 64b
    show player 10
    player_name "... M-my girl?"
    show player 5
    show old_roxxy 2b with dissolve
    roxxy "!!!"
    show old_roxxy 2c
    roxxy "I mean, not to say... I'm your girl or anything..."
    show old_roxxy 1
    show player 3 with dissolve
    player_name "..."
    show old_roxxy 2
    roxxy "Heh, that would be crazy, right?"
    show old_roxxy 1
    show player 29
    player_name "Oh, I don't kno-"
    show player 3
    show old_roxxy 2
    roxxy "I mean, could you imagine you and I?"
    roxxy "... Dating?"
    show old_roxxy 1
    show player 24 with dissolve
    player_name "..."
    roxxy "..."
    show player 26
    player_name "I uhh..."
    show player 11
    show old_roxxy 2b
    annie "You really think one of the students is responsible?"
    smith "... Well, who else would break into my house and steal only the exams?!"
    show old_roxxy 2c
    roxxy "Oh shit!"
    roxxy "{b}Mrs. Smith{/b} is coming!"
    show old_roxxy 2b
    show player 10
    player_name "You can't let her see those exams!"
    player_name "We gotta get out of here!"
    show old_roxxy 2c at left
    show player 11f at Position (xpos=400)
    with dissolve
    roxxy "There's no time!"
    show old_roxxy 2b
    show player 10f
    player_name "What are you-"
    show player 11f
    show old_roxxy 3c
    roxxy "{b}Shut up and get over here{/b}!!!"
    show old_roxxy 3d
    show player 22f
    player_name "!!!"
    scene black with fade

    scene location_school_cutscene04
    show text _ ("... And just like that I was dragged into my locker by {b}Roxxy{/b}!") as caption
    with fade
    pause

    scene expression player.location.background_blur
    show principal 26f at left
    show principal 26f at Position (xoffset=70)
    show old_annie 3 at right
    with fade
    annie "So, what's the plan?"
    show old_annie 1
    show principal 4f with dissolve
    smith "We have to get those exams back! If the board finds out about this, it could mean the end of everything I've built here!"
    show principal 26f at Position (xoffset=70) with dissolve
    show old_annie 3
    annie "Don't worry, ma'am. That's not going to happen!"
    show old_annie 1
    show principal 27f at Position (xoffset=70)
    smith "Of course it's not going to happen! You're gonna find those exams and bring those responsible to me for punishment!"
    show principal 26f at Position (xoffset=70)
    show old_annie 3
    annie "... Yes, ma'am."
    show old_annie 1
    show principal 27f at Position (xoffset=70)
    smith "Start by searching these lockers."
    smith "The little shit might have stashed them in there."
    show principal 26f at Position (xoffset=70)
    show old_annie 3
    annie "Right away, ma'am!"
    show old_annie 1
    show principal 4f with dissolve
    smith "... And don't fail me, {b}Annie{/b}!"
    smith "You know what happens when I'm displeased..."
    show principal 26f at Position (xoffset=70) with dissolve
    show old_annie 6
    annie "..."
    show old_annie 5
    annie "I won't fail you, ma'am."
    show old_annie 6
    show principal 27f at Position (xoffset=70)
    smith "Very good."
    smith "Now get to work!"
    hide old_annie
    hide principal
    with dissolve
    scene expression "backgrounds/location_school_locker_inside01.jpg"
    show player locker 3
    show old_roxxy locker 1
    player_name "!!!"
    show player locker 1
    player_name "{b}Annie is searching the lockers{/b}!"
    player_name "We're totally screwed!"
    show player locker 2
    show old_roxxy locker 2
    roxxy "Shh!!!"
    roxxy "Be quiet!"
    show old_roxxy locker 3
    roxxy "... And stop squirming around!"
    show old_roxxy locker 1
    show player locker 1
    player_name "Sorry, I'm just freaking out!"
    player_name "We're gonna get expelled for this, you know?!"
    show player locker 2
    show old_roxxy locker 2
    roxxy "Would you just calm down!"
    show old_roxxy locker 1
    show player locker 4
    player_name "..."
    show player locker 7
    player_name "Sorry..."
    show player locker 2
    "Clang!"
    show player locker 3
    pause
    annie "Eugh, what are these crusty tissues?!"
    show player locker 1
    player_name "She's getting closer!"
    show player locker 8
    "Clang!"
    show player_boner locker 1 with dissolve
    pause
    show old_roxxy locker 2
    roxxy "Hey! You're poking-"
    show player locker 9
    show player_boner locker 2
    show old_roxxy locker 4
    roxxy "!!!" with hpunch
    show old_roxxy locker 3
    roxxy "What is that?!"
    roxxy "Don't tell me that's your-"
    show old_roxxy locker 4
    show player locker 5
    player_name "..."
    "Clang!"
    show player locker 3
    show old_roxxy locker 6
    roxxy "Is your dick hard right now?!"
    show old_roxxy locker 5
    show player locker 7
    player_name "I-I can't help it..."
    show player locker 5
    show old_roxxy locker 7
    roxxy "How can you be turned on right now?!"
    show old_roxxy locker 5
    show player locker 7
    player_name "I don't know! I can't exactly control it!"
    show player locker 5
    show old_roxxy locker 7
    roxxy "Well, try hard-"
    show old_roxxy locker 8
    hide player_boner
    roxxy "{i}*Gasp*{/i}"
    roxxy "It's touching my-"
    show old_roxxy locker 9
    show player locker 2
    player_name "Stop moving!"
    show player locker 1
    show old_roxxy locker 8
    "Clang!"
    $ M_roxxy.set('sex speed', .6)
    show old_roxxy locker 8_9
    show player locker 9
    player_name "You're making it worse!!"
    show player locker 8
    roxxy "... It's touching my pu-"
    show player locker 9
    player_name "{b}Roxxy{/b} stop moving!"
    show player locker 3
    player_name "... Oh crap."
    player_name "I think we're the next locker..."
    show player locker 9
    player_name "You have to stop grinding on me!"
    show player locker 8
    $ M_roxxy.set('sex speed', 2)
    show old_roxxy locker 8_9
    roxxy "Ahh... Fuuu..."
    pause
    judith "{b}Annie{/b}!"
    show player locker 3
    judith "I need help opening my locker..."
    annie "Ugh, seriously?"
    annie "You are such a pain in my ass."
    judith "I know, I'm sorry..."
    annie "This is the last time!"
    judith "..."
    judith "Why are you searching everyone's locker anyways?"
    show player locker 4
    annie "Just you never mind that!"
    pause
    annie "Alright, it's open. Get your stuff and-"
    annie "Your locker is a mess!"
    show player locker 8
    judith "..."
    annie "This is disgusting..."
    annie "What's the matter with you?!"
    judith "I just-"
    annie "Keeping food in your locker is strictly forbidden!"
    show player locker 3
    annie "I'm gonna have to write you up for this..."
    judith "... But-"
    annie "No excuses, c'mon!"
    annie "I'm taking you to {b}Mrs. Smith{/b} right away!"
    show player locker 9
    annie "I bet punishing you will cheer her up!"
    judith "P-punishment?"
    annie "Move it!"
    judith "... What kind of punishment?!"
    pause
    $ M_roxxy.set('sex speed', .4)
    show old_roxxy locker 8_9
    roxxy "Mmm..."
    show player locker 7
    player_name "{i}*Huff*{/i} You gotta... Stop."
    player_name "I think {b}Annie{/b} is... {i}*Puff*{/i}... {b}Annie{/b} is leaving!"
    show player locker 8
    roxxy "Ahh!"
    show player locker 7
    player_name "{b}Roxxy{/b}?"
    player_name "What are you doing?! We've gotta go!"
    show player locker 9
    roxxy "Shuddup! Shuddup! Shuddup!"
    $ M_roxxy.set('sex speed', .2)
    show old_roxxy locker 8_9
    player_name "What's gotten into-"
    show player locker 9
    show old_roxxy locker 10
    roxxy "Ngghhh!" with flash
    show player locker 8
    player_name "!!!" with hpunch
    roxxy "Haah... Haah..."
    roxxy "Holy shit!"
    roxxy "That was..."
    show player locker 5
    player_name "..."
    show player locker 6
    player_name "{b}Roxxy{/b} we gotta get out of here before {b}Annie{/b} comes back!"
    show player locker 5
    show player_boner locker 2
    show old_roxxy locker 2
    with dissolve
    roxxy "Y-yeah... Okay."
    roxxy "Just... Help me out. My legs are like jello right now..."
    scene black with fade
    scene expression player.location.background_blur
    show old_roxxy 1k at right
    show player 10 at left
    with dissolve
    player_name "That was too close!"
    show player 5
    roxxy "..."
    show old_roxxy 1l
    roxxy "Phew, that was..."
    show old_roxxy 1m
    pause
    show old_roxxy 86 at left
    hide player with hpunch
    pause
    show old_roxxy 3b at right
    show player 15 at left
    with dissolve
    player_name "Ouch!"
    show player 12
    player_name "What was that for?!"
    show player 90
    show old_roxxy 3c
    roxxy "Who the hell gets a boner at a time like that?!"
    show old_roxxy 3d
    show player 10
    player_name "I don't know?!"
    player_name "It just happened!"
    show player 12
    player_name "You're the one who wouldn't stop grinding on it!"
    show player 90
    show old_roxxy 3b
    pause
    show old_roxxy 86 at left
    hide player
    roxxy "Shut up!" with hpunch
    show old_roxxy 3b at right
    show player 15 at left
    with dissolve
    player_name "Ouch! Stop punching me!"
    show player 16
    show old_roxxy 3
    roxxy "You had better not tell anybody what happened in that locker!"
    show old_roxxy 3c
    roxxy "Do you understand me?!"
    show old_roxxy 3b
    show player 12
    player_name "Yeah, I got it!"
    player_name "Just make sure you don't get caught with those exams..."
    show player 90
    show old_roxxy 3
    roxxy "I'll worry about the exams!"
    roxxy "You just focus on keeping your mouth shut!"
    roxxy "If anybody finds out I will absolutely die!"
    show old_roxxy 29f with dissolve
    show player 12
    player_name "{i}*Sigh*{/i} You are way too concerned about other peoples opinions... You know that?"
    show player 90
    show old_roxxy 30f
    roxxy "Just shut up, {b}[firstname]{/b}..."
    show old_roxxy 29f
    show player 12
    player_name "Fine. I've gotta get to my next class anyways..."
    player_name "See ya, {b}Roxxy{/b}."
    show player 90
    roxxy "..."
    show old_roxxy 30f
    roxxy "Bye."
    hide player
    hide old_roxxy
    with dissolve
    show old_roxxy 29f
    roxxy "..."
    show old_roxxy 32 with dissolve
    pause
    show old_roxxy 33
    roxxy "That felt amazing!"
    roxxy "... And it's so..."
    roxxy "... Big!"
    show old_roxxy 1g with dissolve
    roxxy "..."
    show old_roxxy 1h
    roxxy "Who would have thought he was packing something like that?!"
    show old_roxxy 32 with dissolve
    pause
    show old_roxxy 33
    roxxy "... Maybe I am too worried about other people's opinions..."
    roxxy "I mean, would it really be so bad if I started dating {b}[firstname]{/b}?"
    show old_roxxy 1i
    roxxy "..."
    show old_roxxy 1l
    roxxy "Oh my god, I just realized..."
    roxxy "{b}Missy{/b} was right about the nerds having big dicks thing."
    show old_roxxy 84 with dissolve
    roxxy "..."
    roxxy "Ugh, if she finds out I'll never hear the end of it..."
    hide old_roxxy with dissolve
    return

label school_roxxy_dexter_flirt:
    scene expression player.location.background_blur
    show player 13f at right
    show dewitt 43 at left
    with dissolve
    dewitt "Oh, {b}[firstname]{/b}. Perfect timing!"
    show dewitt 42
    show player 14f
    player_name "Hey, {b}Miss Dewitt{/b}."
    player_name "Dang, that's a lot of records!"
    show player 13f
    show dewitt 41
    dewitt "Could you do me a favor and {b}run these down to the auditorium{/b} for me?"
    dewitt "I'm doing a lecture on acoustics later today..."
    show dewitt 42
    show player 14f
    player_name "Sure, I don't mind."
    show player 13f
    show dewitt 43
    dewitt "Aww, thank you, sugar."
    hide dewitt
    show player 642f
    with dissolve
    pause
    player_name "( Hmm, {b}the auditorium is down the right side hallway on the first floor{/b}. )"
    player_name "( I should {b}head there now{/b}. )"
    hide player with dissolve
    return

label school_roxxy_do_pushups_intro:
    scene expression player.location.background_blur
    show player 13 at left
    show old_erik 4 at right
    with dissolve
    erik "{b}[firstname]{/b}!"
    show old_erik 1
    show player 14
    player_name "Hey, {b}Erik{/b}."
    player_name "What's up, man?"
    show player 13
    show old_erik 4
    erik "Oh, you know... The usual."
    erik "I got this sick new codpiece during a raid last night!"
    show old_erik 1
    show player 12
    player_name "Codpiece?"
    show player 13
    show old_erik 4
    erik "Yeah, dude. The green ladies love a good codpiece..."
    show old_erik 1
    show player 17
    player_name "... Haha, right on, man."
    show player 13
    show old_erik 4
    erik "How did things go at the bikini contest?"
    show old_erik 1
    show player 14
    player_name "It was so awesome!"
    player_name "You should have come with me..."
    show player 13
    show old_erik 4
    erik "So you got to see {b}Roxxy{/b} in a tight bikini?"
    show old_erik 1
    show player 14
    player_name "Oh, you have no idea!"
    player_name "She looked so sexy, man!"
    show player 13
    show old_erik 4
    erik "Cool!"
    erik "You really like her, huh?"
    show old_erik 1
    show player 14
    player_name "... Yeah. She's actually a pretty nice person."
    player_name "It's just buried under a layer of bitchiness..."
    show player 13
    show old_erik 4
    erik "Hahaha!"
    erik "She actually said hi to me this morning..."
    show old_erik 1
    show player 12
    player_name "Really?"
    show player 13
    show old_erik 3b
    erik "I mean, she didn't know my name..."
    show old_erik 4
    erik "But hey, at least she didn't call me nerd or fat boy."
    show old_erik 1
    show player 14
    player_name "Heh, sorry."
    show player 13
    show old_erik 4
    erik "No, really! It was a big improvement."
    erik "She must really like you, {b}[firstname]{/b}!"
    show old_erik 1
    show player 14
    player_name "Yeah, I dunno."
    show player 13
    show old_erik 4
    erik "C'mon, dude."
    erik "Used to be, she wouldn't even talk to us."
    erik "Now she's inviting you out to party with her friends."
    show old_erik 1
    show player 5
    player_name "..."
    show player 10
    player_name "We're gonna be late for gym..."
    show player 5
    show old_erik 3b
    erik "Oh, shoot! You're right."
    show old_erik 4
    erik "C'mon, you can tell me all about the bikini contest on the way!"
    hide player
    hide old_erik
    with dissolve
    scene gym
    show player 13 at left
    show old_erik 3b zorder 1
    with dissolve
    erik "Her top snapped?!"
    show old_erik 1
    show player 14
    player_name "Heh, yeah."
    show player 13
    show old_erik 3b
    erik "Like... You saw her..."
    show old_erik 1
    show player 14
    player_name "Her breasts!"
    show player 13
    show old_erik 4
    erik "... Whoa!"
    show old_erik 1
    show player 14
    player_name "It's not that big a deal..."
    show player 13
    show old_erik 4
    erik "Yeah, right!"
    erik "That's so awesome, dude!"
    erik "I wish I could have-"
    show old_erik 1b
    show old_dexter 15 zorder 0 at right
    with dissolve
    show player 90
    dexter "Beat it, fat boy."
    show old_dexter 14
    show old_erik 5b
    erik "Huh?"
    show old_erik 5b
    show player 12
    player_name "Leave us alone, {b}Dexter{/b}..."
    show player 90
    show old_dexter 15
    dexter "I SAID BEAT IT, FAT BOY!"
    hide old_erik
    show old_dexter 21c
    with dissolve
    pause
    show old_dexter 21d with dissolve
    pause
    show old_dexter 14 with dissolve
    show player 15
    player_name "What the hell, man!"
    show player 16
    show old_dexter 15 with dissolve
    dexter "Didn't I tell you to leave {b}Roxxy{/b} alone?!"
    show old_dexter 14
    show player 5
    player_name "..."
    show old_dexter 15
    dexter "Now I hear you're bothering her at the beach?!!"
    show old_dexter 13 at Position (xoffset=-18) with dissolve
    dexter "Do I need to bash your face in?!"
    show old_dexter 14 with dissolve
    show player 12
    player_name "Back off, {b}Dexter{/b}!"
    player_name "She invited me to come."
    show player 90
    show old_dexter 12 with dissolve
    dexter "Psh, yeah right."
    dexter "Why would she want to hang around a loser like you?"
    show old_dexter 11
    show player 12
    player_name "I'm the loser?!"
    player_name "You're the one who has to force himself on girls because he can't get any action..."
    show player 90
    show old_dexter 15 with dissolve
    dexter "What the hell did you just say?!"
    show old_dexter 14
    show player 15
    player_name "... You heard me!"
    show player 12
    player_name "You're pathetic, {b}Dexter{/b}!"
    show player 90
    show old_dexter 21b at Position (xpos=950) with dissolve
    dexter "You're dead, {b}[firstname]{/b}!"
    show old_dexter 14
    show bridget a_crossed f_angry:
        xoffset -300
    with dissolve
    bridget "What in heck is going on here?!"
    show old_dexter 11
    dexter "!!!"
    show player 12
    player_name "N-nothing, ma'am."
    show player 90
    bridget "It doesn't look like nothing!"
    bridget "{b}Dexter{/b}, how many times do I have to tell you not to start fights during class?!"
    show old_dexter 22
    dexter "Yeah, but {b}Coach{/b}... This cockroach has been-"
    show old_dexter 21
    bridget f_angry_yell "I don't want to hear it!" with hpunch
    bridget "If you boys need to settle an argument, then let's do it in a non-violent way..."
    show bridget f_angry
    show player 12
    player_name "... What, like talking?"
    show player 90
    show old_dexter 22
    dexter "I don't understand-"
    show old_dexter 21
    bridget @ f_angry_yell "Push-ups!"
    show player 10
    player_name "Huh?!"
    show player 5
    bridget @ f_angry_yell "Drop and give me fifty! Both of you!" with hpunch
    show player 11
    player_name "!!!"
    dexter "!!!"
    bridget "Last person standing wins the argument!"
    show old_dexter 12
    dexter "This little twerp can't do fifty push-ups..."
    show old_dexter 11
    show player 12
    player_name "I bet I can do them faster than you."
    hide player with dissolve
    show old_dexter 12
    dexter "Psh, yeah right."
    show old_dexter 11
    dexter "..."
    hide old_dexter with dissolve
    pause
    bridget a_whistle f_angry_yell "Go!"
    return

label school_roxxy_trailer_park_romance_intro:
    scene expression player.location.background_blur
    show player 13 at left
    show old_roxxy 1b at right
    with dissolve
    roxxy "{b}[firstname]{/b}!"
    show old_roxxy 1
    show player 14
    player_name "Hey, {b}Roxxy{/b}."
    player_name "What's up?"
    show player 13
    show old_roxxy 1b
    roxxy "I was waiting up for you."
    show old_roxxy 1
    show player 10
    player_name "You were waiting for me?"
    show player 5
    show old_roxxy 1b
    roxxy "Yeah, I figured we could walk to class together."
    show old_roxxy 1
    show player 12
    player_name "Really?"
    show player 14
    player_name "I mean, sure! I'd like that!"
    show player 13
    show old_roxxy 1b
    roxxy "Cool."
    show old_roxxy 1
    player_name "..."
    roxxy "..."
    show player 14
    player_name "So, did you get your trophy home?"
    show player 13
    show old_roxxy 4
    roxxy "Yeah!"
    show old_roxxy 1b
    roxxy "I've got it in my room."
    roxxy "I still can't believe I won..."
    show old_roxxy 1
    show player 14
    player_name "Well, you did!"
    player_name "Those other girls didn't stand a chance!"
    show player 13
    show old_roxxy 1b
    roxxy "Heh, really?"
    show old_roxxy 1
    show player 14
    player_name "Of course."
    player_name "You are way out of their league!"
    show player 13
    roxxy "..."
    show old_roxxy 1b
    roxxy "... Thanks, {b}[firstname]{/b}."
    roxxy "Say, I was thinking..."
    roxxy "... If you aren't too busy..."
    show old_roxxy 1
    show player 5
    player_name "Hmm?"
    show old_roxxy 2
    roxxy "... Maybe you'd wanna hang out tonight?"
    show old_roxxy 1
    show player 10
    player_name "You wanna hang out, with me?"
    show player 5
    show old_roxxy 2
    roxxy "Only if you want to!"
    roxxy "... I just thought... Maybe... You'd come to my place?"
    show old_roxxy 1b
    roxxy "I can make you dinner!"
    roxxy "You know... As thanks for all your help!"
    show old_roxxy 1
    show player 10
    player_name "You can cook?"
    show player 5
    show old_roxxy 2
    roxxy "No, not really..."
    show old_roxxy 1b
    roxxy "... Sorry, I'm not very good at this stuff."
    show old_roxxy 1
    show player 5
    player_name "Hmm?"
    show player 10
    player_name "What do you mean?"
    show player 5
    show old_roxxy 2
    roxxy "... Never mind."
    roxxy "Just forget I said anything."
    show old_roxxy 1
    return

label school_roxxy_trailer_park_romance_no:
    show player 10
    player_name "Well, I would {b}Roxxy{/b} but I've got other plans..."
    show player 5
    show old_roxxy 1l with dissolve
    roxxy "Oh, yeah. Totally..."
    roxxy "I've got tons of other stuff to do too."
    show old_roxxy 1k
    show player 12
    player_name "... Maybe another time?"
    show player 5
    show old_roxxy 1l
    roxxy "Yeah, maybe. We'll see..."
    hide old_roxxy with dissolve
    pause
    show player 12
    player_name "She's acting weird..."
    hide player with dissolve
    return

label school_roxxy_trailer_park_romance_yes:
    show player 10
    player_name "Wait, no!"
    show player 14
    player_name "I'll come!"
    show player 13
    show old_roxxy 1b
    roxxy "You will?!"
    show old_roxxy 1
    show player 14
    player_name "Definitely! I'm just surprised you asked me is all."
    show player 13
    show old_roxxy 2
    roxxy "Heh, yeah..."
    show old_roxxy 1
    player_name "..."
    roxxy "..."
    show old_roxxy 1b
    roxxy "So I guess I'll see you this {b}afternoon{/b} at {b}my place{/b}?"
    show old_roxxy 1
    show player 14
    player_name "Sounds good."
    show player 13
    show old_roxxy 4
    roxxy "Awesome! Don't forget!"
    show old_roxxy 1
    show player 14
    player_name "Heh, I won't."
    hide old_roxxy with dissolve
    pause
    show player 17
    player_name "( Wow, {b}dinner tonight at Roxxy's place{/b}! )"
    player_name "( I guess we're really friends now! )"
    show player 13
    player_name "( Hmm, I wonder why she was acting so weird about it though? )"
    hide player with dissolve
    return

label school_roxxy_dexter_basketball:
    scene expression player.location.background_blur
    show player 5f with dissolve
    player_name "( Hmm, I don't see {b}Dexter{/b} around... )"
    player_name "( I really hope he didn't see {b}Roxxy{/b} and I making out. )"
    player_name "( He'll wanna fight for sure. )"
    show old_erik 4 at right
    erik "What's up, dud-"
    show old_erik 5
    show player 6f at left
    player_name "Whaaaa!!!" with hpunch
    show player 22 with dissolve
    erik "Whoa?!"
    show player 37 with dissolve
    erik "What the-"
    show old_erik 3b
    player_name "Phew, sorry man."
    show player 38
    player_name "You scared the crap out of me!"
    show player 5 with dissolve
    show old_erik 5
    erik "What's got you so jumpy?"
    show old_erik 3b
    show player 10
    player_name "{i}*Sigh*{/i} I think {b}Dexter{/b} saw me making out with {b}Roxxy{/b}..."
    show player 5
    show old_erik 5
    erik "!!!" with hpunch
    erik "You made out with {b}Roxxy{/b}?!"
    show old_erik 51
    show player 38 with dissolve
    player_name "Shh, keep it down man!"
    show player 3
    show old_erik 53
    erik "Sorry... Dude, this is epic news though!"
    show old_erik 4
    erik "My best friend is making out with the most popular girl in school!"
    show old_erik 1
    show player 5 with dissolve
    player_name "..."
    show player 12
    player_name "I guess you didn't hear the part where her steroid pumping, psycho of an ex-boyfriend saw us together?"
    show player 5
    show old_erik 3b
    erik "Oh, right."
    show old_erik 5
    erik "Yeah, that's not good. {b}Dexter{/b} is going to kill you, dude..."
    show old_erik 52
    show player 12
    player_name "I know! That's why I'm jumpy!"
    player_name "I keep expecting him to charge out at me every time I pass a classroom..."
    show player 5
    show old_erik 4
    erik "Well, no worries, dude. I've got your back!"
    erik "We can walk together and I'll make sure he doesn't sneak up on you."
    show old_erik 1
    show player 10
    player_name "Heh, thanks, {b}Erik{/b}..."
    show player 5
    show old_erik 5
    erik "Just be warned, if it comes down to a fight, I'm gonna be less than worthless..."
    player_name "..."
    show old_erik 3b
    erik "I'm serious, dude... Don't judge me too harshly if I pee my pants and pass out!"
    show old_erik 1
    show player 17
    player_name "Hahaha!"
    show player 13
    show old_erik 4
    erik "C'mon, we've {b}got gym out on the basketball court today{/b}. No way {b}Dexter{/b} tries to start a fight in front of {b}Coach Bridget{/b}."
    show old_erik 1
    show player 10
    player_name "Yeah, I hope you're right."
    hide player
    hide old_erik
    with dissolve
    scene basketball_b
    show old_kevin 23f at Position (xpos=500)
    show old_erik 52f at Position (xpos=300)
    show player 5 at left
    show bridget a_ball f_normal:
        xoffset 150
    with dissolve
    bridget "... Now, I know you boys have probably seen the professionals on TV..."
    bridget "... Dribbling between their legs and passing behind their backs!"
    bridget @ f_angry "It's a bunch of nonsense!" with hpunch
    bridget "Basketball is all about the fundamentals!"
    bridget "Intelligent play calling, precise execution-"
    show old_kevin 32f
    kevin "... And making it rain from the three-point line!"
    show old_kevin 23f
    player_name "..."
    erik "..."
    bridget @ f_angry "Oh, so this is all a big joke to you, huh?"
    show old_kevin 34f with dissolve
    kevin "{i}*Gulp*{/i} ... I didn't mean-"
    show old_kevin 23f with dissolve
    bridget "No, no, no. It's my fault..."
    bridget "... I didn't realize you were too good for basketball fundamentals..."
    show old_kevin 34f with dissolve
    kevin "That wasn't-"
    show old_kevin 34bf
    bridget @ f_angry "Why don't you just run laps around the court for the rest of class instead?"
    kevin "!!!"
    show old_kevin 24f with dissolve
    kevin "... But that's 57 minutes..."
    show old_kevin 24bf
    bridget "Is that not enough?"
    bridget "We can always meet here after school if you want more?"
    show old_kevin 24f
    kevin "{i}*Sigh*{/i} No, ma'am."
    show old_kevin 24bf
    bridget "Good."
    bridget "Get started!" with hpunch
    show bridget a_ball_whistle f_angry_yell
    hide old_kevin
    with dissolve
    pause
    bridget a_ball f_normal "Hmm, now where was I?"
    show player 10
    player_name "{i}*Ahem*{/i} Fundamentals, ma'am."
    show player 5
    bridget "Ahh, yes."
    bridget "So basketball is all about the fund-"
    show player 22
    dexter "There's the nerd I've been looking for!" with hpunch
    show player 23
    player_name "Oh, shit..."
    show player 22
    show old_erik 5f
    erik "Uh oh..."
    show old_erik 51f
    show old_dexter 14 at right with dissolve
    bridget "What in the world?!"
    show old_dexter 15
    dexter "You think I wasn't gonna find out, you little bitch?!"
    show old_dexter 14
    bridget @ f_angry "Excuse me?! {b}Dext{/b}-"
    show old_dexter 13 at Position (xoffset=-18) with dissolve
    dexter "Get out of my way, fat boy or I'll punch those stupid freckles right off your face!" with hpunch
    show old_erik 64f with fastdissolve
    show old_erik 65f with fastdissolve
    show old_erik 66f with fastdissolve
    hide old_erik
    show old_dexter 15
    with dissolve
    dexter "I saw you and that whore, ex-girlfriend of mine!"
    show old_dexter 14
    show player 15
    player_name "Hey, don't talk about {b}Roxxy{/b} like that!"
    show player 16
    show old_dexter 15
    dexter "I'll say whatever the hell I want!"
    dexter "What are you gonna do about it, NERD?!"
    show old_dexter 14
    show player 11 at Position (xpos=-150)
    show bridget zorder 1:
        flip
        xoffset 0
    with dissolve
    bridget "Alright, {b}Dexter{/b}, you better back up right this instant!" with hpunch
    bridget "This isn't happening in the middle of my class, mister!"
    show old_dexter 15
    dexter "... But {b}Coach{/b} you don't understand..."
    dexter "This piece of shit-"
    show old_dexter 14
    bridget "I don't wanna hear it, {b}Dexter{/b}!"
    bridget "You know the rules in my class!"
    bridget "We settle things here without violence!"
    show old_dexter 15
    dexter "Ugh, this won't be settled until that twerp gets the beating he has coming..."
    show old_dexter 14
    show bridget a_ball_throw f_normal with dissolve
    player_name "..."
    show bridget a_crossed
    show old_dexter 29
    with dissolve
    dexter "Hmm?"
    bridget "So beat him on the court."
    hide bridget
    show player 16 at left
    with dissolve
    show old_dexter 30
    dexter "I don't understand..."
    show old_dexter 29
    show player 12
    player_name "She's saying we should settle this with a game of basketball... Moron."
    show player 16
    dexter "!!!"
    show old_dexter 30
    dexter "Oh, you're so dead..."
    show old_dexter 33
    show player 647
    with dissolve
    dexter "Fine!"
    show old_dexter 15 with dissolve
    dexter "Your ball, NERD!"
    hide player
    hide old_dexter
    with dissolve
    return

label school_roxxy_fight_dexter:
    scene expression L_school_front.background_blur
    show player 12 with dissolve
    player_name "I had better make sure I'm prepared for a fight before going back to school."
    player_name "There's no doubt, {b}Dexter{/b} will be looking for blood after what happened on the basketball court."
    show player 4 at Position (xoffset=7) with dissolve
    player_name "..."
    show player 12 with dissolve
    player_name "I'll need lots of dexterity to avoid his attacks and strength to put him down fast."
    player_name "Otherwise, I won't stand a chance..."
    show player 5
    player_name "..."
    show player 38 at Position (xoffset=51) with dissolve
    player_name "Am I ready for this?!"
    show player 3 at Position (xoffset=26) with dissolve
    return

label school_roxxy_locker_sex:
    scene expression "backgrounds/location_school_locker_room_backpack_day_blur.jpg"
    show old_becca 6 at Position (xpos=315)
    show old_roxxy 1g at Position (xpos=600)
    show old_missy 7 at left
    with dissolve
    becca "... It's that good?!"
    show old_becca 5
    show old_roxxy 1h
    roxxy "Fucking. Mind. Blowing!"
    show old_roxxy 1g
    show old_missy 5
    missy "Ooooh, I'm getting wet just thinking about it..."
    show old_missy 7
    show old_roxxy 1h
    roxxy "Like, oh my god... I can't even describe the way it feels."
    show old_roxxy 1g
    show old_becca 2
    becca "... Does it hurt?"
    show old_becca 1
    show old_roxxy 2
    roxxy "Yeah, a lot at first!"
    show old_missy 3
    show old_roxxy 1b
    roxxy "... But after a while it hurts less..."
    show old_roxxy 1h
    roxxy "... And then later it still hurts but in a really, REALLY good way!"
    show old_roxxy 1g
    show old_becca 5
    becca "Hmm..."
    show old_missy 8
    missy "God, that's so hot!"
    show old_missy 7
    show old_becca 3b
    becca "It does sound pretty hot..."
    show old_becca 5
    show old_roxxy 1h
    roxxy "You have no idea!"
    show old_roxxy 1g
    becca "..."
    show old_missy 8
    missy "So, when do we get to play with him?!"
    show old_roxxy 2b
    show old_missy 7
    show old_becca 3b
    becca "{b}Missy{/b}!!!"
    show old_becca 3
    show old_missy 8
    missy "... What?!"
    show old_roxxy 3d
    missy "Don't act like you aren't thinking the same thing!"
    show old_missy 7
    show old_becca 26 with dissolve
    becca "..."
    show old_becca 24 with dissolve
    show old_roxxy 3c
    roxxy "... Seriously?!"
    roxxy "He's MY fucking boyfriend! Why should I let you dumb skanks play with him?!"
    show old_roxxy 3d
    show old_missy 1b
    missy "Uhh, because we're your dumb skanks!"
    show old_missy 8
    missy "... And besides, we all know it turns you on..."
    show old_missy 7
    show old_roxxy 2b
    roxxy "!!!" with hpunch
    show old_roxxy 3c
    roxxy "What the hell are you talking about?!"
    show old_roxxy 3d
    show old_missy 8
    missy "Psh, don't lie!"
    show old_missy 7
    show old_becca 25
    becca "We've both seen you playing with yourself during our games of spin the bottle, {b}Roxxy{/b}..."
    show old_becca 24
    show old_roxxy 2c
    roxxy "... I do not!"
    show old_roxxy 2b
    show old_missy 1b
    missy "You do so!!!"
    show old_missy 7
    show old_becca 25
    becca "It's not very subtle..."
    show old_becca 24
    show old_roxxy 29
    roxxy "..."
    show old_roxxy 30
    roxxy "Tch, okay. Fine!"
    show old_roxxy 3c
    roxxy "I admit, it's kinda hot watching everybody fooling around when we play..."
    roxxy "That doesn't mean I'm going to let you start fucking him..."
    show old_roxxy 3d
    show old_becca 25
    becca "..."
    show old_missy 4
    missy "Why not?!"
    show old_missy 2b
    show old_roxxy 3
    roxxy "Because he's my man!"
    roxxy "Not yours! MINE!"
    show old_roxxy 3b
    becca "..."
    show old_missy 8
    missy "Yeah, but..."
    missy "Just think about this, {b}Roxxy{/b}."
    missy "{b}Becca{/b} naked... On her back... Her pale, freckled tits, heaving with anticipation..."
    show old_missy 7
    show old_roxxy 1
    show old_becca 27 with dissolve
    becca "Anticipation?! What the hell are you on about?!"
    show old_becca 26
    show old_missy 4
    missy "Shut up! I'm trying to paint a picture here!"
    show old_missy 2b
    roxxy "..."
    show old_missy 8
    missy "{b}[firstname]{/b}'s huge throbbing cock, rubbing against her clit as she moans and begs you to let her have it..."
    show old_missy 7
    becca "..."
    show old_roxxy 1b
    roxxy "... I'm listening."
    show old_roxxy 1
    show old_missy 8
    missy "{i}*Ahem*{/i}!!!"
    show old_missy 7
    show old_becca 27
    becca "What?!"
    show old_becca 26
    show old_missy 8
    missy "{b}Becca{/b} begs you to let her have it..."
    show old_missy 7
    show old_becca 27
    becca "Seriously?!"
    show old_becca 26
    show old_missy 4
    missy "Do it, bitch! Don't fucking ruin this for me!"
    show old_missy 2b
    show old_becca 24 with dissolve
    becca "..."
    show old_becca 25
    becca "Please, let me have it {b}Roxxy{/b}..."
    show old_missy 7
    show old_roxxy 4
    roxxy "Hahaha, you would really beg me for it, {b}Becca{/b}?"
    show old_roxxy 1
    show old_becca 25
    becca "... I don't know."
    show old_becca 24
    show old_missy 8
    missy "Oh, she totally would! Look at how turned on she is, just thinking about it..."
    show old_missy 7
    show old_becca 27 with dissolve
    becca "I am not!"
    show old_becca 26
    show old_missy 8
    missy "Bitch, you're practically panting."
    show old_missy 7
    becca "..."
    show old_becca 24 with dissolve
    show old_roxxy 1g
    roxxy "Hmm."
    show old_roxxy 1h
    roxxy "... And what about you?!"
    show old_roxxy 1g
    show old_becca 26 with dissolve
    show old_missy 1b
    missy "Me?!"
    show old_missy 1
    show old_roxxy 1h
    roxxy "You gonna beg me too?"
    show old_roxxy 1g
    show old_missy 8
    missy "I'll do whatever you want me to do!"
    missy "You want me to beg? I'll beg."
    missy "I'll suck your tits or lick your pussy... Hell, I'll toss your salad if you want!"
    missy "Just as long as you let me take a ride on that huge nerd cock of his!"
    show old_missy 7
    show old_roxxy 4
    roxxy "Hahahaha!"
    show old_roxxy 1g
    show old_missy 8
    missy "C'mon, you have to admit. It's pretty hot."
    missy "Your own personal bitches, willing to do anything you desire, for a chance at your man's cock..."
    show old_missy 7
    show old_becca 27
    becca "I am not tossing her salad..."
    show old_becca 26
    show old_missy 2
    missy "Psh, you totally would {b}Becca{/b}. Don't lie!"
    show old_missy 7
    show old_becca 24 with dissolve
    becca "..."
    show old_roxxy 1h
    roxxy "You really put a lot of thought into this..."
    show old_roxxy 1h
    show old_missy 6
    missy "Hah, more than a lot, believe me!"
    show old_missy 7
    roxxy "..."
    show old_missy 8
    missy "So, what do you say?!"
    show old_missy 7
    roxxy "..."
    show old_roxxy 1g
    roxxy "... Maybe."
    show old_roxxy 1h
    show old_missy 3
    show old_becca 2
    becca "!!!"
    show old_missy 1b
    missy "{i}*Gasp*{/i} Really?!"
    show old_missy 1
    show old_roxxy 1b
    roxxy "We would have to establish some ground rules..."
    roxxy "... Like you two do everything I say, no arguments."
    show old_roxxy 1g
    show old_missy 1b
    missy "I am SO totally on board with that!"
    show old_missy 1
    becca "..."
    show old_roxxy 1b
    roxxy "{b}Becca{/b}?"
    show old_roxxy 1
    show old_missy 7b with dissolve
    becca "!!!"
    show old_missy 1 with dissolve
    show old_becca 25
    becca "... I'll do everything you say."
    becca "No arguments..."
    show old_becca 24
    show old_roxxy 1h
    roxxy "... Even if I tell you to eat me out or swallow {b}[firstname]{/b}'s load?"
    show old_roxxy 1g
    show old_missy 4
    missy "Hell yes! Gladly!"
    show old_missy 1b
    missy "Anything you want, {b}Roxxy{/b}! I'm your bitch!"
    show old_missy 1
    becca "..."
    show old_roxxy 1b
    roxxy "{b}Becca{/b}?"
    show old_roxxy 1g
    show old_becca 25
    becca "... Yeah, okay."
    show old_becca 24
    show old_roxxy 1h
    roxxy "Okay, what?!"
    show old_roxxy 1g
    show old_becca 25
    becca "I'll be your bitch too, okay?!"
    show old_becca 24
    show old_roxxy 4
    roxxy "Hahaha!"
    show old_roxxy 1h
    roxxy "... Hmm, I'll think about it."
    show old_roxxy 1g
    show old_missy 7
    missy "..."
    becca "..."
    show old_roxxy 1b
    roxxy "Now, if you'll excuse me."
    show old_roxxy 1h
    roxxy "I'm gonna go find {i}my man{/i}!"
    hide old_roxxy with dissolve
    pause
    show old_becca 1f at Position (xpos=400) with dissolve
    show old_missy 4
    missy "Damn it, I was hoping she would agree right away..."
    show old_missy 2b
    show old_becca 2f
    becca "... Me too."
    show old_becca 1f
    show old_missy 1b
    missy "See, I fucking knew you were into it!"
    show old_missy 1
    show old_becca 2f
    becca "Shut up!"
    show old_becca 1f
    show old_missy 8
    missy "You're such a slut."
    show old_missy 7
    show old_becca 2f
    becca "Yeah, well... At least I'm not as big a slut as you!"
    show old_becca 1f
    show old_missy 5
    missy "Psh, whatever."
    show old_missy 2
    missy "My sluttiness might have just got us a date with {b}[firstname]{/b}'s magic cock!"
    missy "You should be thanking me right now!"
    show old_missy 2b
    show old_becca 7f
    becca "..."
    hide old_becca
    hide old_missy
    with dissolve

    scene expression player.location.background_blur
    show player 13 at left
    with dissolve
    show old_roxxy 1b at right with dissolve
    roxxy "There you are!"
    show old_roxxy 1
    show player 14
    player_name "Hey, {b}Roxxy{/b}!"
    player_name "What are you up to?"
    show player 13
    show old_roxxy 1h
    roxxy "Heh, I was just thinking about you..."
    show old_roxxy 1g
    show player 14
    player_name "Oh yeah?"
    player_name "What about me?"
    show player 13
    show old_roxxy 1h
    roxxy "Oh, you know... Just how strong and manly you are..."
    roxxy "... And how I'd like to ride that strong, manly cock of yours right here and now."
    show old_roxxy 1g
    show player 11
    player_name "!!!" with hpunch
    show player 10
    player_name "What?! We can't do that!"
    player_name "We're at school!"
    show player 5
    show old_roxxy 4
    roxxy "Hehehe, don't worry!"
    show old_roxxy 1h
    roxxy "Nobody is gonna see us..."
    show old_roxxy 1g
    show player 11
    player_name "..."
    show old_roxxy 1h
    roxxy "I have a plan!"
    hide old_roxxy with dissolve
    show player 12
    player_name "What the-"

    scene location_school_cutscene06
    show text _ ("Again, {b}Roxxy{/b} dragged me into my locker like some rag doll!") as caption
    with fade
    pause

    scene location_school_locker_inside01
    show player locker 1
    show old_roxxy locker 1b
    with fade
    player_name "Great, we're stuffed in my locker again..."
    show player locker 2
    show old_roxxy locker 1
    roxxy "Hehe, shut up and get your cock out!"
    show old_roxxy locker 1b
    show player locker 7
    player_name "You're serious?!"
    show player locker 5
    show old_roxxy locker 1
    roxxy "Hell yeah, I'm serious!"
    roxxy "I want you inside me, right now!"
    show old_roxxy locker 1b
    show player locker 6
    player_name "What the heck got you so worked up?!"
    show player locker 5
    show old_roxxy locker 1
    roxxy "Mmm, you'll find out soon enough."
    show old_roxxy locker 1b
    show player locker 11 with dissolve
    player_name "..."
    show player locker 12 with dissolve
    pause
    hide old_roxxy
    show player locker 13
    with dissolve
    roxxy "... But right now, I want you to concentrate..."
    show player locker 14 with dissolve
    pause
    roxxy "... On fucking me senseless!"
    player_name "O-okay..."
    show player locker 15
    roxxy "!!!" with hpunch
    roxxy "Ahhh..."
    return

label school_roxxy_locker_sex_repeat:
    $ player.go_to(L_school_hall)
    scene expression player.location.background_blur
    show player 12 with dissolve
    player_name "... Now where the hell is she?!"
    show player 4 with dissolve
    roxxy "Pssst!"
    show player 11f
    player_name "!!!" with hpunch

    scene location_school_cutscene06
    show text _ ("Again, {b}Roxxy{/b} dragged me into my locker like some rag doll!") as caption
    with fade
    pause
    hide caption with dissolve
    show text _ ("I wasn't her boy toy, was I?") as caption with dissolve
    pause

    scene location_school_locker_inside01
    show player locker 8
    show old_roxxy locker 1
    with fade
    roxxy "Finally! I was starting to think you chickened out on me!"
    show old_roxxy locker 1b
    show player locker 6
    player_name "Seriously, you wanna do this again?!"
    show player locker 5
    show old_roxxy locker 1
    roxxy "Absolutely!"
    show old_roxxy locker 1b
    show player locker 6
    player_name "You realize what would happen if we got caught having sex on school grounds?!"
    show player locker 5
    show old_roxxy locker 1
    roxxy "Yeah, we'd both be expelled."
    show old_roxxy locker 1b
    player_name "... Exactly!"
    show player locker 11 with dissolve
    pause
    show player locker 12 with dissolve
    pause
    hide old_roxxy
    show player locker 13
    with dissolve
    roxxy "So let's not get caught..."
    show player locker 14 with dissolve
    player_name "... Why aren't you worried about-"
    roxxy "{b}[firstname]{/b}, shut up and fuck me!"
    show player locker 15
    player_name "Fine!" with hpunch
    return

label roxxy_locker_sex_loop_pre:
    scene expression "backgrounds/location_school_locker_inside01.jpg"
    $ M_roxxy.set("sex speed", .09)
    show expression AnimatedImage("roxxys_locker", [1,2,3,4,5,6,7,8,9,10], M_roxxy) as roxxys_locker with dissolve
    return

label roxxy_locker_sex_loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                show expression AnimatedImage("roxxys_locker", [1,2,3,4,5,6,7,8,9,10], M_roxxy) as roxxys_locker
                $ animated = True
            pause 5
            call expression game.dialog_select("roxxy_locker_hscene_dialog")
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [1,2,3,4,5,6,7,8,9,10]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "roxxys_locker {}".format(pose_list[pose_counter]) as roxxys_locker
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call expression game.dialog_select("roxxy_locker_hscene_dialog")
        $ animcounter += 1
    if M_roxxy.get("roxxy locker sex first"):
        $ M_roxxy.set("roxxy locker sex first", False)
    call screen roxxy_locker_sex_options

label roxxy_locker_hscene_dialog:
    $ random_count = randomizer()
    if animcounter == 0:
        if M_roxxy.get("roxxy locker sex first"):
            player_name "Shhh!!!"
            player_name "You have to be quiet or someone will catch us!"
            roxxy "I know!"
            roxxy "It's not exactly easy, you know!"
            player_name "Well then, stop and I'll fuck you later tonight!"

        elif not M_roxxy.get("roxxy locker sex first"):
            if random_count > 33 and random_count <= 66:
                roxxy "Mmm, I love this dick, so fucking much!"
                player_name "Shh!!"
                roxxy "{i}*Whimper*{/i}"

            elif random_count > 66:
                roxxy "Aahh!!"

    elif animcounter == 1:
        if M_roxxy.get("roxxy locker sex first"):
            roxxy "Mmm..."

        elif not M_roxxy.get("roxxy locker sex first"):
            if random_count <= 33:
                roxxy "Mmm, this is so fucking hot!"
                player_name "... Yeah, I know."
                player_name "I'm sweating like crazy."
                roxxy "Eww! That's not what I meant!"
                player_name "..."
                roxxy "I mean, like, someone could totally catch us in here fucking!"
                player_name "..."
                roxxy "Fuck, that's hot!"
                player_name "You are so weird sometimes..."
                roxxy "Hehehe, shut up and fuck me harder!"

            elif random_count > 66:
                roxxy "Ooh, fuck me, {b}[firstname]{/b}!"
                player_name "..."
                roxxy "Fuck me harder!!"
        else:

            roxxy "{b}[firstname]{/b}!!!"

    elif animcounter == 2:
        if M_roxxy.get("roxxy locker sex first"):
            player_name "{b}Roxxy{/b}!!!"
            roxxy "Shut up and fuck me!"
            player_name "..."
            player_name "Fine!"
            $ M_roxxy.set("sex speed", .06)
            roxxy "Fuuuuuck..." with hpunch
            player_name "Be quiet, bitch!"
            roxxy "{i}*Whimper*{/i}"

        elif not M_roxxy.get("roxxy locker sex first"):
            if random_count > 33 and random_count <= 66:
                player_name "Ouch!"
                roxxy "... What?!"
                player_name "I hit my head on the top of the stupid locker!"
                roxxy "Hahaha, don't be a baby!"
                player_name "Well, it hurt!"
                roxxy "Yeah, and you pulling my hair hurts too... You don't hear me complaining."
                player_name "... Why didn't you just say something? I would have stopped."
                roxxy "{i}*Gasp*{/i} Don't you dare stop!"
                roxxy "Pull it harder!"

            elif random_count > 66:
                player_name "Shh!!! Someone is going to hear you!"
                roxxy "I don't care!"
                roxxy "Let them hear me!"
                roxxy "This is so fucking good!!!"
                player_name "Damn it, {b}Roxxy{/b}!"
                player_name "They'll expel us!"
                roxxy "{i}*Whimper*{/i}"
                roxxy "... Fine."
        else:

            roxxy "Oh god, oh god, OH GOD!!!"

    elif animcounter == 3:
        if M_roxxy.get("roxxy locker sex first"):
            roxxy "Oh god, oh god, OH GOD!!!"
            player_name "Shut up and cum!!!"

        elif not M_roxxy.get("roxxy locker sex first"):
            if random_count > 33 and random_count <= 66:
                player_name "..."
                roxxy "Mmm! Fuuuuuck yessss!!!"
        else:

            if random_count > 50:
                roxxy "Haaah, I'm getting close."
                player_name "Good, me too!"
    return

label roxxy_locker_sex_cum:
    call expression game.dialog_select("roxxy_locker_sex_cum_pre")
    if M_roxxy.get("roxxy locker sex"):
        call expression game.dialog_select("roxxy_locker_sex_cum_repeat")
    else:

        call expression game.dialog_select("roxxy_locker_sex_cum_first")
    $ renpy.end_replay()
    $ persistent.cookie_jar["Roxxy"]["unlocked"] = True
    $ persistent.cookie_jar["Roxxy"]["gallery"]["05_unlocked"] = True
    $ M_roxxy.trigger(T_roxxy_locker_sex)
    $ player.go_to(L_school_hall)
    $ game.timer.tick()
    $ game.main()

label roxxy_locker_sex_cum_pre:
    scene expression "backgrounds/location_school_locker_inside01.jpg"
    show player locker 15_15b
    player_name "Tch!" with flash
    roxxy "!!!"
    roxxy "{i}*Gasp*{/i}!!!"
    show player locker 15
    show xray_roxxy_locker at Position (align=(0,0))
    with dissolve
    pause
    hide xray_roxxy_locker
    show player locker 16
    with dissolve
    return

label roxxy_locker_sex_cum_first:
    player_name "You alright?"
    show player locker 17b with dissolve
    roxxy "Haah... Haah..."
    roxxy "Yeah, just give me a second..."
    roxxy "Phew."
    show player locker 17
    player_name "That was crazy."
    show player locker 17b
    roxxy "Yeah, but it felt amazing, didn't it?"
    show player locker 17
    player_name "Heh, yeah..."
    show player locker 17b
    roxxy "I think we might have to try this again sometime!"
    show player locker 17
    player_name "Huh?! No way!"
    player_name "What if we get caught?!"
    show player locker 17b
    roxxy "Hehe, we'll just have to be careful..."
    show player locker 17
    player_name "..."
    show player locker 17b
    roxxy "C'mon, pull your pants up and let's get out of here while the hall is empty!"
    show player locker 17
    player_name "{i}*Sigh*{/i}"
    scene black with fade

    scene expression player.location.background_blur
    show player 14 at left
    show old_roxxy 1g at right
    with dissolve
    player_name "Seriously, what brought that on?!"
    show player 13
    show old_roxxy 4
    roxxy "Hehe, I can't say."
    show old_roxxy 1g
    show player 14
    player_name "Why not?!"
    show player 13
    show old_roxxy 1h
    roxxy "... Because I'm planning a surprise for you!"
    show old_roxxy 1g
    show player 12
    player_name "Huh?"
    player_name "What kind of surprise?"
    show player 13
    show old_roxxy 1h
    roxxy "Hehe, the kind only {i}my man{/i} deserves..."
    show old_roxxy 1g
    show player 11
    player_name "..."
    show player 13
    show old_roxxy 1b
    roxxy "Just remember to show up for the party this weekend!"
    show old_roxxy 1g
    show player 14
    player_name "You and the girls doing the beach thing again?"
    show player 13
    show old_roxxy 1h
    roxxy "Always."
    show old_roxxy 1g
    show player 14
    player_name "So {b}Saturday evening at the beach{/b}?"
    show player 13
    show old_roxxy 1b
    roxxy "Mmmhmm."
    roxxy "Don't be late!"
    show old_roxxy 1
    show player 14
    player_name "Heh, alright."
    show player 13
    show old_roxxy 1h
    roxxy "See you later, {b}[firstname]{/b}."
    show old_roxxy 1g
    show player 14
    player_name "Bye, {b}Roxxy{/b}."
    hide player
    hide old_roxxy
    with dissolve
    return

label roxxy_locker_sex_cum_repeat:
    player_name "You alright?"
    show player locker 17b with dissolve
    roxxy "Haah... Haah..."
    roxxy "Yeah, just give me a second..."
    roxxy "Phew."
    show player locker 17
    player_name "C'mon, let's get out of here!"
    scene black with fade

    scene expression player.location.background_blur
    show player 10 at left
    show old_roxxy 1g at right
    with dissolve
    player_name "You know, we really can't keep doing this!"
    show player 5
    show old_roxxy 1h
    roxxy "Why not?!"
    show old_roxxy 1g
    show player 10
    player_name "We're gonna get caught, {b}Roxxy{/b}!"
    show player 5
    show old_roxxy 2
    roxxy "Psh, you worry too much!"
    show old_roxxy 1g
    show player 16
    player_name "..."
    show old_roxxy 2
    roxxy "Don't give me that look!"
    show old_roxxy 48 with dissolve
    roxxy "C'mon, you know I really get off on this!"
    roxxy "You aren't gonna take that away from me... Are you?!"
    show old_roxxy 47
    show player 14
    player_name "{i}*Sigh*{/i} Alright, alright!"
    player_name "Just put your hypnotic boobs away!"
    show player 13
    show old_roxxy 4 with dissolve
    roxxy "Hehehe, thank you {b}[firstname]{/b}!"
    hide player
    show old_roxxy 92 at left
    with dissolve
    pause
    show old_roxxy 59e with dissolve
    player_name "C'mon, we have to get to class..."
    show old_roxxy 59d
    roxxy "Ooh, yes sir..."
    roxxy "Hehehe!"
    hide old_roxxy with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
