label music_classroom_dewitt_intro:
    scene music_classroom_c
    show dewitt 1 at left
    show player 14f at right
    with dissolve
    player_name "Hey, {b}Miss Dewitt{/b}."

    show player 13f
    show dewitt 2
    dewitt "Oh my goodness, {b}[firstname]{/b}! Is that you, sugar?"

    dewitt "I was starting to think you up and moved to a different school or something!"

    show dewitt 1
    show player 10f
    player_name "Heh, no. I had some uh, \"family issues\" come up."

    show player 5f
    show dewitt 2
    dewitt "Yeah, I heard about your father passing. Such a shame..."

    dewitt "Is there anything I can do for you, sugar?"

    show dewitt 1
    show player 10f
    player_name "Actually, I was hoping we could talk about getting my grade back on track?"

    show player 5f
    show dewitt 2
    dewitt "Well, I betcha we can figure something out."

    dewitt "Why don't you go pick out an instrument and have a seat."

    dewitt "We'll get you back in the groove."

    show dewitt 3
    show player 11f
    pause
    show dewitt 1
    show player 10f
    player_name "Alright, any instrument in particular, {b}Miss Dewitt{/b}?"

    show player 5f
    show dewitt 2
    dewitt "Hmm, how about you give those drums over there a try?"

    show dewitt 1
    show player 14f
    player_name "Tentu saja!"

    hide player with dissolve

    scene music_class_cs01
    show text _ ("I never got to play the drums before.") as caption
    with fade
    pause

    scene music_class_cs02
    show text _ ("It was actually pretty difficult keeping a steady rhythm, but kind of fun...") as caption
    with fade
    pause

    scene music_class_cs03
    show text _ ("!!!") as caption
    with hpunch
    pause

    scene music_class_cs04
    show text _ ("Good thing {b}Miss Dewitt{/b} is so nice to me...\nBecause I'm terrible...") as caption
    with fade
    pause

    scene music_classroom_c
    show dewitt 1 at left
    show player 37f at right
    with fade
    player_name "I'm so sorry, {b}Miss Dewitt{/b}!"

    player_name "Aku tidak bermaksud-"

    show player 3f at Position (xoffset=-8) with dissolve
    show dewitt 2
    dewitt "Hehehe, it's alright, sugar."

    dewitt "You aren't the first person to try and beat out a rhythm on these lovely ladies!"

    show dewitt 3
    show player 11f with dissolve
    player_name "..."
    show player 5f
    show dewitt 2
    dewitt "Perhaps we should get you on something a little more, elegant?"

    dewitt "Hmm, the flute maybe..."

    show dewitt 1
    show player 12f
    player_name "... Eh, the flute?"

    player_name "That's kinda girly, isn't it?"

    show player 5f
    show dewitt 2
    dewitt "Oh, lord no, sugar!"

    dewitt "Men have been playing the flute since the stone ages."

    show dewitt 1
    show player 10f
    player_name "Benar-benar?"

    show player 5f
    show dewitt 2
    dewitt "Anda sebaiknya mempercayainya!"

    dewitt "Ancient armies from all over the world used the flute to keep the rhythm in their battle lines."

    dewitt "Nothing girly about that, is there?"

    show dewitt 1
    show player 12f
    player_name "No, I guess not."

    show player 5f
    show dewitt 2
    dewitt "Maybe you should give it some thought then?"

    show dewitt 1
    show player 10f
    player_name "Mungkin..."

    show player 5f
    show dewitt 2
    dewitt "Excuse me, sugar, but I'd better get this class under control."

    hide dewitt with dissolve

    scene studyclass02
    show text _ ("I spent the whole day trying not to play off tempo...") as caption
    with fade
    pause

    scene studyclass03
    show text _ ("... Finally the bell rang.") as caption
    with fade
    pause

    scene music_classroom_c
    show dewitt 2
    with fade
    dewitt "Well done everybody! That was an awesome jam session!"

    dewitt "Now, before you all head out, I need a moment of your time!"

    show dewitt 14 at Position (xoffset=-127) with dissolve
    dewitt "Hei!"

    dewitt "{b}Tyrone{/b}, eyes up front!"

    show dewitt 13 at Position (xoffset=-127)
    tyrone "..."
    show dewitt 2 with dissolve
    dewitt "Now, I wanted to remind everybody that the musical talent show is coming up, very soon."

    dewitt "... And we still have a lot of open slots that need to be filled."

    show dewitt 3 at Position (xoffset=-7)
    dewitt "Remember, I'm offering extra credit to everyone that participates."

    player_name "!!!"
    show dewitt 2
    dewitt "I'd really like to see this year's show go off without a hitch!"

    dewitt "So please, don't hesitate to come and talk to me if you're interested."

    show dewitt 3 at Position (xoffset=-7)
    dewitt "Thanks and have a groovy afternoon, everybody!"

    show dewitt 1 at right with dissolve
    pause 0.5
    hide dewitt with dissolve
    pause 1

    show player 17 with dissolve
    player_name "Extra credit is just what I need!"

    show player 14
    player_name "I'll do anything to improve my grade at this point."

    player_name "I should {b}talk with Miss Dewitt about the talent show tomorrow{/b}."

    hide player with dissolve
    return

label music_classroom_dewitt_smith_berating:
    scene music_classroom_c
    show dewitt 13 at left
    show principal 5 at right
    with dissolve
    smith "You can't seriously be going forward with that pathetic talent show again!"

    show principal 4 with dissolve
    smith "Wasn't last year embarrassing enough for you?!"

    show principal 26 at Position (xoffset=-70)
    show dewitt 14
    dewitt "Why do you do this every year?!"

    dewitt "I'm just trying to instill a love of music in these students and every year you shit all over it!"

    show dewitt 13
    show principal 27 at Position (xoffset=-70)
    smith "Aww, poor little {b}Melody{/b}."

    smith "At least you won't have to worry about it much longer..."

    show principal 26 at Position (xoffset=-70)
    show dewitt 14
    dewitt "Ugh, what are you on about now?"

    show dewitt 13
    show principal 27 at Position (xoffset=-70)
    smith "I've got a meeting with the school board this afternoon."

    smith "You see, I told them all about the money you wasted on that joke of a talent show last year..."

    smith "... And when it flops again this time, they've already agreed to let me reallocate the funding towards worthier endeavors."

    show principal 26 at Position (xoffset=-70)
    show dewitt 14
    dewitt "Worthier endeavors?"

    dewitt "You can be a real bitch, you know that?"

    show dewitt 13
    show principal 5 with dissolve
    smith "Ha ha ha!"

    smith "I can't wait to see how you screw things up this time..."

    show principal 26 at Position (xoffset=-70) with dissolve
    show dewitt 14
    dewitt "Grrr..."

    dewitt "Just get out of my classroom, would ya?!"

    show dewitt 13
    show principal 38 with dissolve
    smith "Hahahahaah!"

    hide principal with dissolve
    show dewitt 12
    dewitt "God, I hate that woman."

    hide dewitt with dissolve
    return

label music_classroom_dewitt_talent_show_help:
    scene music_classroom_c
    show dewitt 10b at left
    show player 10f at right
    with dissolve
    player_name "Hey there, {b}Miss Dewitt{/b}."

    show player 5f
    show dewitt 11b
    dewitt "Hello, sugar. How you doing?"

    show dewitt 10b
    show player 10f
    player_name "saya baik-baik saja."

    show player 14f
    player_name "I was hoping I could talk to you about joining the talent show?"

    show player 13f
    show dewitt 11b
    dewitt "Oh, well, that's nic-"

    show dewitt 9
    pause 2
    show dewitt 11
    dewitt "Wait. Did you just ask about the talent show?!"

    show dewitt 9
    show player 12f
    player_name "... Ya?"

    show player 5f
    show dewitt 3 with dissolve
    dewitt "Ya ampun!"

    show dewitt 4 with dissolve
    show player 10f
    player_name "Uhh, you alright, {b}Miss Dewitt{/b}?"

    show player 5f
    show dewitt 11
    dewitt "I'm just a bit emotional is all."

    show dewitt 11b
    dewitt "{b}Mrs. Smith{/b} is looking for any excuse she can find to cancel the talent show this year."

    show dewitt 12
    dewitt "... And so far I only have one volunteer."

    show dewitt 10b
    show player 12f
    player_name "Siapa?"

    show player 5f
    show dewitt 11
    dewitt "{b}Tyrone{/b}."

    dewitt "... But I can't just have him play solo the entire time!"

    show dewitt 10
    show player 14f
    player_name "Well, I'll join and I'll ask around too!"

    show dewitt 4
    player_name "Maybe I can find you more volunteers?"

    hide player
    show dewitt 6 at right
    with dissolve
    dewitt "Oh, bless you, sugar!"

    dewitt "That would be wonderful!"

    show dewitt 7
    pause
    show dewitt 15 at left
    show player 14f at right
    with dissolve
    player_name "Heh, it's no problem..."

    show player 13f
    show dewitt 3 with dissolve
    dewitt "Oh, {b}[firstname]{/b}, you just flipped my day right side up again!"

    show dewitt 1
    show player 14f
    player_name "Glad I could help make you happy!"

    show player 13f
    show dewitt 2
    dewitt "Such a sweet little man..."

    dewitt "What instrument did you want to play?"

    show dewitt 1
    show player 14f
    player_name "Well, I dunno. I like the drums."

    show player 13f
    show dewitt 8 with dissolve
    dewitt "Heh, oh yeah. I remember our little drumming session from yesterday."

    show dewitt 15
    show player 10f
    player_name "... Again, I'm really sorry about that."

    show player 5f
    show dewitt 16
    dewitt "Don't you worry about it, sugar."

    show dewitt 17 with dissolve
    show player 11f
    dewitt "These ladies have a habit of getting in the way."

    dewitt "You wouldn't believe how hard they make it for me to play the guitar."

    dewitt "... I think they just like the attention."

    show dewitt 15 with dissolve
    show player 13f
    player_name "..."
    show dewitt 5
    dewitt "Anyway, I'm afraid {b}Tyrone{/b} already signed up to play the drums."

    show dewitt 16
    dewitt "I know you'd play them with enthusiasm from your playful love taps yesterday."

    show dewitt 4
    show player 10f
    player_name "Dia melakukannya?"

    show player 12f
    player_name "Hmm, I dunno what to choose..."

    show player 10f
    player_name "Bagaimana menurutmu?"

    show player 5f
    show dewitt 5
    dewitt "Well, how about the flute?"

    show dewitt 4
    show player 12f
    player_name "Uh, jangan ini lagi..."

    show player 5f
    show dewitt 8
    dewitt "Oh, ayolah!"

    show dewitt 5
    dewitt "There's nothing finer than a man who knows how to handle his flute!"

    show dewitt 4
    player_name "..."
    show player 12f
    player_name "Sungguh?"

    show player 5f
    show dewitt 5
    dewitt "Anda sebaiknya mempercayainya!"

    show dewitt 8
    dewitt "I'll even give you free lessons!"

    show dewitt 4
    show player 10f
    player_name "You know how to play the flute?"

    show player 5f
    show dewitt 16
    dewitt "Oh, sugar. My skill with the flute is unrivaled!"

    dewitt "I can work miracles with this mouth!"

    show dewitt 15
    show player 14f
    player_name "Well, I suppose I could try it if you're willing to give me free lessons."

    show player 13f
    show dewitt 16
    dewitt "I'm more than willing."

    show dewitt 15
    show player 14f
    player_name "Alright, I guess I'll take the flute then."

    show player 13f
    show dewitt 5
    dewitt "Good decision, {b}[firstname]{/b}!"

    dewitt "Let me just go get it. One sec."

    hide dewitt with dissolve
    pause
    pause
    show player 55f with dissolve
    player_name "{i}*Menguap*{/i}"

    pause
    show player 13f with dissolve
    pause
    show dewitt 11 at left with dissolve
    dewitt "Um, well, we did have one."

    show dewitt 10b
    dewitt "Hmm. I wonder where it went."

    show dewitt 11
    dewitt "I must have loaned it out earlier this year."

    dewitt "I guess they never returned it, though."

    dewitt "Why don't you {b}take a peek at the instrument signout sheet inside the classroom locker{/b}."

    show dewitt 4
    show player 14f
    player_name "Alright! I'll go and have a look!"

    show player 13f
    show dewitt 5
    dewitt "Hurry back, sugar!"

    hide player
    hide dewitt
    with dissolve
    return

label music_classroom_music_sheet:
    scene music_classroom_c
    show music_checkout_form with dissolve
    pause
    player_name "Hmm..."

    player_name "It looks like {b}Judith{/b} was the last person to check out the school's flute."

    player_name "{b}I guess I'd better track her down{/b}!"

    hide music_checkout_form with dissolve
    $ game.main()

label music_classroom_dewitt_return_flute:
    scene music_classroom_c
    show dewitt 1 at left
    show player 14f at right
    with dissolve
    player_name "Hey, {b}Miss Dewitt{/b}."

    player_name "I found the school's flute."

    show player 13f
    show dewitt 2
    dewitt "I knew you would, sugar!"

    show dewitt 1
    show player 10f
    player_name "... But I'm afraid it's broken beyond repair."

    show player 5f
    show dewitt 11b with dissolve
    dewitt "Broken?! What are we gonna do?"

    show dewitt 10b
    show player 14f
    player_name "Well, I kinda, made one!"

    show player 239_240f with dissolve
    pause
    show player 567cf with dissolve
    player_name "Bagaimana menurutmu?"

    show player 567bf
    show dewitt 5
    dewitt "Wow! You made that?!"

    show dewitt 4
    show player 567cf
    player_name "Yeah, at home in my garage."

    show player 567bf
    show dewitt 16
    dewitt "You're really good with wood, huh?"

    show dewitt 15
    show player 567cf
    player_name "I know right?"

    show player 567bf
    show dewitt 5
    dewitt "Mind if I take a closer look?"

    show dewitt 4
    show player 567cf
    player_name "Tentu!"

    show player 13f with dissolve
    show dewitt 34 with dissolve
    dewitt "The length and girth are..."

    dewitt "Sempurna."

    dewitt "When you're done with this flute, I wouldn't mind borrowing it for a night or two!"

    show dewitt 33
    show player 11f
    player_name "???"
    show dewitt 34
    dewitt "What? I like breaking in new instruments!"

    show dewitt 33
    show player 14f
    player_name "Alright, deal."

    player_name "I tried playing it earlier. It isn't too hard!"

    show player 13f
    show dewitt 40 with dissolve
    dewitt "Great! Here's the sheet music for the concert. Your part shouldn't be too difficult."

    dewitt "Practice every night and you'll be ready for the concert in no time."

    show dewitt 4 with dissolve
    show player 386f with dissolve
    player_name "Alright, {b}Miss Dewitt{/b}. I will!"

    show player 385f
    show dewitt 5
    dewitt "Now, if you don't mind, let's hear what you can do! Class is just about to start."

    show dewitt 4
    show player 386f
    player_name "Oke."

    hide player with dissolve

    scene music_class_cs05
    show text _ ("It was weird not sitting with the percussion section...\n... But sitting in the flute section had its perks though.") as caption
    with fade
    pause
    return

label music_classroom_dewitt_talent_show_progress:
    scene music_classroom_c
    show player 13f at right
    show dewitt 2 at left
    with dissolve
    dewitt "Halo, {b}[firstname]{/b}."

    dewitt "Have you been practicing those fingerings I taught you?"

    show dewitt 1
    show player 10f
    player_name "F-fingerings?"

    show player 11f
    show dewitt 8 with dissolve
    dewitt "You know, on the flute, silly."

    show dewitt 4
    show player 17f
    player_name "O-oh yeah! I think I'm getting pretty good."

    show player 14f
    player_name "You're a great teacher, {b}Miss Dewitt{/b}!"

    show player 13f
    show dewitt 5
    dewitt "Well, you're a fast learner, sugar."

    show dewitt 11
    dewitt "I just hope we get more students to sign up soon, otherwise, we might have to cancel the show."

    show dewitt 10
    show player 12f
    player_name "You still haven't had any volunteers?"

    show player 5f
    show dewitt 11b
    dewitt "Nope, not a one."

    show dewitt 12
    dewitt "I'm starting to get worried, {b}[firstname]{/b}..."

    show dewitt 10b
    show player 14f
    player_name "There's still time, {b}Miss Dewitt{/b}."

    player_name "I'll bet I can round up a few people for you!"

    show player 13f
    show dewitt 11
    dewitt "You'd really do that?"

    show dewitt 10
    show player 33f
    player_name "Sangat!"

    show player 13f
    show dewitt 5
    dewitt "Oh, you're so sweet!"

    show dewitt 4
    show player 14f
    player_name "Heh, lemme go see who I can convince."

    show player 13f
    show dewitt 3 with dissolve
    dewitt "Good luck, sugar!"

    hide player
    hide dewitt
    with dissolve
    return

label music_classroom_dewitt_talent_get:
    scene music_classroom_c
    show dewitt 4 at left
    show dewitt 4 at Position (xpos=110)
    show player 14f at right
    with dissolve
    player_name "I found two more volunteers for the talent show!"

    show player 13f
    show dewitt 5
    dewitt "Really?! Who did you find and what do they play?"

    show dewitt 4
    show player 14f
    player_name "Well, it turns out that {b}Eve{/b} is a singer."

    show player 13f
    show dewitt 5
    dewitt "You don't say! Is she any good?"

    show dewitt 4
    show player 14f
    player_name "She's got a voice like an angel, you won't believe it!"

    show player 13f
    show dewitt 5
    dewitt "That's wonderful! Who else did you get?"

    show dewitt 4
    show player 14f
    player_name "{b}Kevin{/b} is gonna play the guitar."

    show player 13f
    show dewitt 5
    dewitt "Well, now you're getting me excited! I've heard {b}Kevin{/b} play before, and he's very talented."

    show dewitt 4
    show player 14f
    player_name "Yeah, I've heard good things."

    show player 13f
    show dewitt 5
    dewitt "Lord, {b}[firstname]{/b}! You've got the makings of your very own band!"

    show dewitt 8
    dewitt "As a matter of fact! That's not a bad idea!"

    show dewitt 4
    show player 10f
    player_name "Hah?"

    show player 5f
    show dewitt 5
    dewitt "For the finale of the show, we should have all three of you play something together!"

    show dewitt 4
    show player 10f
    player_name "Benar-benar?"

    show player 11f
    show dewitt 8
    dewitt "Absolutely! It's perfect!"

    show dewitt 4
    show player 14f
    player_name "Heh, okay. If that's what you want?"

    show player 13f
    show dewitt 5
    dewitt "Oh, yay!! I can't wait to see this show!"

    show dewitt 23 at Position (xoffset=45) with dissolve
    pause
    show dewitt 22 at Position (xoffset=45) with dissolve
    pause
    show dewitt 27 at Position (xoffset=-119) with dissolve
    pause
    show dewitt 24 at Position (xpos=110) with dissolve

    show player 23f
    player_name "!!!"

    show player 11f
    show dewitt 25 at Position (xoffset=69) with dissolve
    dewitt "Oh! Shit!"

    dewitt "My bad, {b}[firstname]{/b}..."

    dewitt "My girls are trying to celebrate too!"


    show player 14f
    player_name "Heh, it's alright. I don't mind."

    show player 13f
    show dewitt 16 with dissolve
    dewitt "Oh, I bet you don't, sugar!"

    dewitt "I guess you can consider that a little extra reward for all your hard work."

    dewitt "If we manage to pull this talent show off, I might let you have a private viewing."

    show dewitt 15
    show player 11f
    player_name "{i}*Meneguk*{/i}"

    show dewitt 8
    dewitt "Aww, you're such a cutie!"

    show dewitt 4
    show player 14f
    player_name "I should probably get back to practicing."

    show player 13f
    show dewitt 5
    dewitt "Now that's a good idea. Thanks again, {b}[firstname]{/b}."

    show dewitt 4
    show player 36f with dissolve
    player_name "Bye, {b}Miss Dewitt{/b}."

    hide player
    hide dewitt
    with dissolve
    return

label music_classroom_dewitt_music_sheets:
    scene music_classroom_c
    show old_kevin 23 zorder 2 at right
    show dewitt 1 zorder 3 at left
    with dissolve
    pause
    show player 13f zorder 1 at Position (xpos=700) with dissolve
    show dewitt 2
    dewitt "Oh good, you're here, {b}[firstname]{/b}."

    dewitt "I was just handing out the music sheets."

    show dewitt 1
    show player 10f
    player_name "Music sheets?"

    show player 5f
    show dewitt 2
    dewitt "For the finale, remember?"

    show dewitt 1
    show player 17f
    player_name "Oh, right. Yeah, I remember."

    show player 13f
    show old_kevin 26 with dissolve
    kevin "It's actually a pretty cool song!"

    show old_kevin 23 with dissolve
    show dewitt 2
    dewitt "Heh, well of course it is!"

    show dewitt 3
    dewitt "Look at who you're working with here, mister!"

    show dewitt 1
    show player 10f
    player_name "Shouldn't {b}Eve{/b} be here?"

    show player 13f
    show old_kevin 24
    kevin "She's here..."

    kevin "... Or well, she was."

    show old_kevin 23
    show dewitt 2
    dewitt "She went to grab something from her locker."

    show dewitt 1
    show player 14f
    player_name "Did she like the song too?"

    show player 13f
    show dewitt 2
    dewitt "Anda sebaiknya mempercayainya!"

    show dewitt 1
    show player 14f
    player_name "Looks like everything is going to work out then, huh?"

    show player 13f
    show dewitt 2
    dewitt "Yeah, all thanks to you, sugar!"

    show dewitt 4 with dissolve
    show old_kevin 24
    kevin "I can't wait to get up there and start playing! The crowd is gonna love this!"

    show old_kevin 23
    show player 11f
    show dewitt 9
    eve "{b}Miss Dewitt{/b}!"

    show eve f_surprised a_wtf zorder 0:
        xoffset -300
    with fastdissolve
    eve "Guys, come quick! You're not going to believe this!"

    show dewitt 11
    dewitt "What's that matter, sweetie?"

    show dewitt 10
    eve f_sad a_cover "Someone vandalized the auditorium!"

    show old_kevin 24
    show player 23f
    show dewitt 11b
    dewitt "Apa?!"

    show dewitt 10b
    eve "Yeah, there's graffiti everywhere!"

    show player 22f
    hide dewitt with dissolve
    show eve a_sides f_surprised:
        flip
        xoffset 100
    with dissolve
    eve "C'mon guys!"

    hide player
    hide eve
    hide old_kevin
    with dissolve
    return

label music_classroom_dewitt_check_up:
    scene music_classroom_c
    show dewitt 9f at left
    show player 10f at right
    with dissolve
    player_name "{b}Miss Dewitt{/b}, you in here?"

    show player 11f
    show dewitt 9d with dissolve
    dewitt "Yeah, I'm right here, sugar."

    show dewitt 9c
    show player 10f
    player_name "Kamu baik-baik saja?"

    show player 11f
    show dewitt 9d
    dewitt "Oh, I'll be okay. I'm just a little down in the dumps at the moment."

    show dewitt 9f with dissolve
    show player 25f
    player_name "( Hmm, I guess I should give her some space for the time being. )"

    hide player
    hide dewitt
    with dissolve
    return

label music_classroom_dewitt_find_dewitt:
    scene music_classroom_c
    show dewitt 9f at left
    show player 14f at right
    with dissolve
    player_name "{b}Miss Dewitt{/b}, you in here?"

    show player 13f
    show dewitt 9d with dissolve
    dewitt "Yeah, I'm right here, sugar."

    show dewitt 9c
    show player 10f
    player_name "Kamu baik-baik saja?"

    show player 5f
    show dewitt 9d
    dewitt "Oh, I'll be okay. I'm just a little down in the dumps at the moment."

    show dewitt 9f with dissolve
    show player 14f
    player_name "Aku punya kejutan untukmu!"

    show player 13f
    show dewitt 9d with dissolve
    dewitt "I'm not really in the mood for games, {b}[firstname]{/b}..."

    show dewitt 9c
    show player 14f
    player_name "No games. Seriously, I have something that's gonna cheer you up!"

    show player 13f
    show dewitt 9d
    dewitt "Oh, sugar. You're so sweet."

    show dewitt 9c
    show player 14f
    player_name "Ikutlah denganku!"

    show player 13f
    show dewitt 9d
    dewitt "{i}*Sigh*{/i} Alright, lead the way."

    hide player
    hide dewitt
    with dissolve
    return

label music_classroom_dewitt_talent_show_practice:
    scene music_classroom_c
    show player 13f at right
    show dewitt 2 at left
    with dissolve
    dewitt "Halo, {b}[firstname]{/b}!"

    show dewitt 1
    show player 14f
    player_name "Hey {b}Miss Dewitt{/b}!"

    show player 13f
    show dewitt 3
    dewitt "You ready for practice?"

    show dewitt 1
    show player 17f
    player_name "Anda yakin!"

    show player 13f
    show dewitt 2
    dewitt "Go take a seat then, sugar."

    hide player with dissolve

    scene music_class_cs06
    show text _ ("Practicing with {b}Kevin{/b} and {b}Eve{/b} was so much fun!\nWe were going to slay at the talent show for sure!") as caption
    with fade
    pause

    scene music_classroom_c
    show old_kevin 23 at Position (xpos=600)
    show eve f_happy
    show player 14 at left
    with fade
    player_name "That was a good session. We're sounding really good, you guys!"

    show player 13
    eve @ f_laugh "Yeah, this is so much fun!"

    show old_kevin 24
    kevin "It's a shame we'll never get to play..."

    show old_kevin 24b
    show eve f_confused
    show player 5
    player_name "..."
    eve "Huh? What are you talking about, {b}Kevin{/b}?"

    show old_kevin 24f with dissolve
    kevin "There's no way {b}Mrs. Smith{/b} is going to let this talent show actually happen!"

    kevin "{b}[firstname]{/b} and I heard her and {b}Annie{/b} plotting."

    kevin "They're bound to have something up their sleeve!"

    show old_kevin 24bf
    show eve f_sad
    eve "... Shouldn't we tell {b}Miss Dewitt{/b}?"

    show old_kevin 24f
    kevin "Why? There's nothing she can do to stop it..."

    show old_kevin 24bf
    show player 10
    player_name "It'll just upset her."

    show player 12
    player_name "We're going to have to deal with {b}Mrs. Smith{/b} ourselves!"

    show player 13
    show eve f_surprised
    show old_kevin 20 with dissolve
    pause
    show old_kevin 32 with dissolve
    kevin "I'm in!"

    show old_kevin 23
    eve f_nervous_down @ -m_talk "..."
    eve f_nervous "You guys are serious?"

    eve "{b}Mrs. Smith{/b} will expel us in a heartbeat if she catches us messing with her..."

    show old_kevin 24f with dissolve
    kevin "So? You just wanna let her shit all over {b}Miss Dewitt{/b}'s talent show?!"

    show old_kevin 24bf
    eve "I'm not saying that!"

    eve "... It's just... We have to be careful! That's all."

    eve @ f_sad "My sister will KILL me if I get expelled!"

    show player 14
    player_name "You don't have to be involved, {b}Eve{/b}. {b}Kevin{/b} and I can handle it."

    show player 13
    eve a_point f_happy @ f_eyeroll "Pfft, ya benar!"

    eve a_hip @ a_point "I can't wait to hear the plan you two numbskulls come up with!"

    eve "It'll fail for sure without my feminine wiles!"

    show player 14
    player_name "Heh, good. It'll be a lot easier with three people."

    show player 13
    show old_kevin 9b with dissolve
    kevin "So, what's the plan, {b}[firstname]{/b}?"

    show old_kevin 23
    show player 10
    player_name "We just have to figure out a way to keep {b}Mrs. Smith{/b} and {b}Annie{/b} as far away from the auditorium as possible!"

    show player 5
    show old_kevin 20 with dissolve
    kevin "..."
    eve f_confused "You mean, like trapping them somewhere?"

    show player 11
    player_name "!!!"
    show player 35
    player_name "That's not a bad idea..."

    show eve f_happy
    show old_kevin 23 with dissolve
    player_name "We could trap them in {b}Mrs. Smith{/b}'s office until the talent show is over!"

    show player 13
    eve @ f_laugh "See, I told you... Feminine wiles!"

    show old_kevin 9b
    kevin "Yeah, yeah... We're very impressed. How exactly are we supposed to trap them in her office though?!"

    show old_kevin 23
    show player 4 with dissolve
    eve f_nervous_down a_idle @ -m_talk "..."
    player_name "..."
    show eve f_nervous
    pause
    eve a_idle @ a_wtf "What? Do I have to plan the entire thing myself?!"

    show player 10 with dissolve
    player_name "Well, we can't just lock them in there. {b}Annie{/b} has a master key to the entire school."

    show player 5
    show old_kevin 24
    kevin "... Yeah, and even if she didn't, {b}Mrs. Smith{/b} would probably just send her out the window for help."

    show old_kevin 23
    eve f_happy @ f_laugh "Haha, I would pay to see that!"

    show player 10
    player_name "So we need to incapacitate them somehow..."

    show player 5
    show old_kevin 20 with dissolve
    kevin "..."
    eve "My sister has a taser at the shop... We could zap them?"

    show player 10
    player_name "That's a little extreme, don't you think?"

    show player 5
    show old_kevin 21
    kevin "It's not like {b}Mrs. Smith{/b} doesn't deserve it..."

    show old_kevin 23 with dissolve
    show player 12
    player_name "No tasers!"

    show player 10
    show eve f_nervous_down
    player_name "... {b}Mrs. Smith{/b} might be pure evil but I don't think {b}Annie{/b} is..."

    player_name "She's just misguided."

    show player 5
    eve f_nervous "Well, that's the only idea I've got."

    show player 34
    player_name "..."
    show old_kevin 22 with dissolve
    kevin "Tunggu sebentar!"

    show player 13
    kevin "Saya mengerti!"

    kevin "Remember that adhesive we made in {b}Miss Okita{/b}'s class a while back?"

    show old_kevin 23 with dissolve
    show player 10
    player_name "... Tidak?"

    show player 5
    show old_kevin 9b
    kevin "Ah that's right, you weren't back at school yet."

    show old_kevin 23f with dissolve
    eve f_happy "saya ingat."

    eve "That stuff was like insanely sticky! You needed a chemical solvent to neutralize it..."

    show old_kevin 32f
    kevin "Tepat!"

    show player 13
    kevin "Remember how {b}Dexter{/b} got his hand stuck to his forehead?!"

    show old_kevin 23f
    eve @ f_laugh "Hahaha! Yeah! That shit was hilarious!"

    eve "It took {b}Miss Okita{/b} twenty minutes to get him sorted out."

    show player 14
    player_name "Wow! It's that strong?"

    show player 13
    show old_kevin 32 with dissolve
    kevin "Yeah, bro! This stuff is wicked!"

    show old_kevin 23
    eve f_nervous "Do you remember how to make it?"

    show old_kevin 9bf with dissolve
    kevin "I think so, yeah."

    show eve f_happy
    show old_kevin 23f
    show player 14
    player_name "So, what are you proposing?"

    show player 13
    show old_kevin 9b with dissolve
    kevin "I'm thinking, we sneak into {b}Mrs. Smith{/b}'s office at night and glue her chairs to the floor."

    kevin "We also apply some to the cushions and presto! They'll be stuck there until someone finds them."

    kevin "Even then... They'll need the solvent to get free!"

    show old_kevin 23
    eve "I hate to say it but... That's actually kinda brilliant!"

    show player 17
    player_name "Nice job, {b}Kevin{/b}!"

    show player 13
    show old_kevin 9b
    kevin "... I guess us men aren't so stupid after all."

    show old_kevin 23
    eve @ f_laugh "Heh, yeah well... Even a broken clock is right twice a day."

    show player 14
    player_name "So, do we need to gather ingredients or something?"

    show player 13
    eve @ f_confused a_wtf -m_talk "..."
    show old_kevin 9b
    kevin "Nah, man. Everything we need is in the science lab."

    kevin "Just {b}meet me there tomorrow after class{/b} and I'll whip us up a batch!"

    show old_kevin 23
    show player 14
    player_name "Alright, we'll meet up once it's finished to plan for {b}Mrs. Smith{/b}'s office."

    player_name "Remember, nobody says a word to {b}Miss Dewitt{/b}. I don't want to see her upset again."

    hide player
    hide old_kevin
    hide eve
    with dissolve
    pause
    show dewitt 9c with dissolve
    dewitt "..."
    show dewitt 9d
    dewitt "He's going through all this trouble because he doesn't want to see me upset?"

    show dewitt 9f
    dewitt "{i}*Sniff*{/i} What a wonderful kid..."

    hide dewitt with dissolve
    return

label dewitt_talent_show_helping_kevin:
    player_name "( I should {b}convince Kevin to join the talent show{/b} first. )"

    return

label dewitt_talent_show_helping_eve:
    player_name "( I should {b}convince Eve to join the talent show{/b} first. )"

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
