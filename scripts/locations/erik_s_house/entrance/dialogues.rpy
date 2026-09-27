label eriks_house_intro:
    scene expression game.timer.image("erik_entrance{}_c")
    show player 1 at left
    show mrsj 17 at right
    with dissolve
    mrsj "Halo, {b}[firstname]{/b}!"

    show mrsj 14
    show player 36 with dissolve
    player_name "Hi, {b}Mrs. Johnson{/b}."

    show player 13 with dissolve
    show mrsj 17
    mrsj "It's been a while since your last visit!"

    show mrsj 14
    show player 25
    player_name "Yeah, I've been a bit busy lately..."

    show mrsj 20
    show player 24
    mrsj "{b}Erik{/b} told me about your father..."

    mrsj "I was so sorry to hear. Let us know if you ever need anything, okay?"

    show mrsj 19c
    show player 10
    player_name "Thanks, {b}Mrs. Johnson{/b}."

    player_name "Right now I'm focusing on catching up in school and saving money for tuition."

    show player 13
    show mrsj 17
    mrsj "It's nice to hear of a young man, such as yourself, acting so responsibly."

    show mrsj 49
    mrsj "Just make sure you save yourself some time to chase after girls, honey."

    show mrsj 50
    show player 21
    player_name "Ya baiklah..."

    show player 13
    pause
    show mrsj 17
    mrsj "Well, it's good to see you again!"

    show mrsj 18
    mrsj "You're probably here to see {b}Erik{/b}, not little ol' me."

    show mrsj 17
    mrsj "It's been so quiet around here..."

    show mrsj 14
    show player 10
    player_name "Apa maksudmu?"

    show player 5
    show mrsj 19
    mrsj "Well, {b}Erik{/b} doesn't get many visitors and you seem to be his only friend."

    show mrsj 17
    show player 13
    mrsj "I want you to know that you're always welcome in this house. Day or night."

    show mrsj 49
    mrsj "You and {b}Erik{/b} are good kids."

    show mrsj 50
    show player 2
    player_name "Thanks, {b}Mrs. Johnson{/b}."

    show player 13
    pause
    show player 12
    player_name "Where is {b}Erik{/b} anyways?"

    show player 5
    show mrsj 17
    if L_erikhouse_basement.is_here(M_erik):
        mrsj "I think I saw him just a bit ago. He was making a rare appearance outside his room!"

        mrsj "He's in the basement right now."

    elif game.timer.is_morning():
        mrsj "He left for school a little while ago."

        mrsj "You better hurry too or you'll be late!"

    else:
        mrsj "I'm not actually sure at the moment, but feel free to have a look around for him."

    if game.timer.is_dark():
        show mrsj 18
        mrsj "Well, it's getting a bit late for me."

        show mrsj 17
        show player 13
        mrsj "I'm off to bed, so you have fun. But remember to keep the volume to a respectable level if you play some video games."

        show mrsj 14
        show player 14
        player_name "Will do. Have a good night {b}Mrs. Johnson{/b}!"

    else:
        mrsj "Anyway, I should probably get going."

        show player 13
        mrsj "I have to teach yoga lessons in the afternoon down at the gym."

        mrsj "I've got some new students, and I'd better hurry up, so I'm not late!"

        show mrsj 14
        show player 14
        player_name "Okay, have fun!"

        show player 13
        show mrsj 17
        mrsj "You too! Tell {b}Erik{/b} I'll be back with dinner and not to eat too many sweets."

        show mrsj 49
        mrsj "I want him nice and hungry for me tonight!"

    hide mrsj
    hide player
    with dissolve
    return

label erikentrance_erik_orcette_inspection:
    scene expression game.timer.image("erik_entrance{}_c")
    show player 375 at left
    show mrsj 17 at right
    with dissolve
    mrsj "Halo, {b}[firstname]{/b}!"

    mrsj "Are you looking for {b}Erik{/b}?"

    show mrsj 14
    show player 377
    player_name "!!!"
    show player 376
    player_name "H... Hi, {b}Mrs. Johnson{/b}."

    show player 378
    mrsj "..."
    show mrsj 17
    mrsj "So, what're you two up to..."

    show mrsj 14
    show player 376
    player_name "Oh, tidak ada apa-apa!"

    show player 377
    show mrsj 49
    mrsj "What is it that you're holding anyway?"

    mrsj "Something new you and {b}Erik{/b} are going to play with, huh?"

    show mrsj 50
    player_name "!!!"
    show player 379
    player_name "Uh... Yeah, something like that."

    show player 377
    show mrsj 17
    mrsj "I just love surprises! What is it? It has to be some new game."

    mrsj "That's all {b}Erik{/b} does these days..."

    show mrsj 14
    show player 379
    player_name "Yeah... Um... It's not... Well..."

    show player 377
    show mrsj 17
    mrsj "Let me see!"

    show player 23 with dissolve
    show mrsj 43 with dissolve
    player_name "Tunggu!"

    show player 22
    mrsj "!!!"
    show mrsj 44
    mrsj "What... Is it?"

    show mrsj 46
    show player 10
    player_name "It's..."

    show player 11
    show mrsj 43
    mrsj "Is this one of those fake sex things they advertise online?"

    show mrsj 46
    show player 10
    player_name "eh..."

    show player 24
    show mrsj 44
    mrsj "Did {b}Erik{/b} put you up to this?"

    mrsj "I've seen it flash across his computer screen when I entered his room one time."

    show mrsj 46
    show player 25
    player_name "No. No. It's... Um... Mine."

    show player 24
    player_name "I... Uh... Was going to... Just show him?"

    show mrsj 45
    mrsj "Haha."

    mrsj "Boys and their toys!"

    show mrsj 46
    player_name "..."
    show player 25
    show mrsj 44
    mrsj "Oh honey... It's alright!"

    mrsj "Young men exploring their sexuality is a good thing!"

    mrsj "Maybe seeing your new toy will motivate him to... Get out of his room?"

    mrsj "The real thing is... Even better, young man."

    show mrsj 46
    show player 22
    player_name "{i}*Meneguk*{/i}"

    show mrsj 44
    if L_erikhouse_erikroom.is_here(M_erik):
        mrsj "{b}Erik{/b} is upstairs, honey."

    else:
        mrsj "{b}Erik{/b} is at school right now anyway, honey."

    mrsj "Oh, and make sure to use lube with that thing."

    mrsj "You don't want to get friction burns on your... Parts."

    hide mrsj with dissolve
    show player 377 with dissolve
    pause
    show player 376
    player_name "( Wow... I thought she was going to be disgusted at me for this... )"

    player_name "( But she seemed pretty cool about it? )"

    player_name "( {b}Erik{/b} sure is lucky he ended up here... )"

    hide player with dissolve
    return

label erikentrance_mrsj_yoga:
    scene expression game.timer.image("erik_entrance{}_c")
    show mrsj 17 at right
    show player 13 at left
    with dissolve
    mrsj "Oh, good!"

    show mrsj 19
    mrsj "{b}[firstname]{/b}, I hate to bother you, but are you available tonight?"

    show mrsj 19c
    show player 10
    player_name "Hah?"

    show player 11
    show mrsj 19
    mrsj "I need someone to go and teach my yoga class for me tonight. I have another appointment I need to attend."

    show mrsj 14
    show player 12
    player_name "Aku?!"

    show player 5
    show mrsj 49
    mrsj "Apakah kamu pikir kamu bisa membantu... Tetangga kesayanganmu??"

    show mrsj 50
    show player 38 with dissolve
    player_name "Uhh... I... Guess I could try?"

    show player 29 with dissolve
    player_name "But I don't know much about yoga..."

    show player 11 at left with dissolve
    show mrsj 17
    mrsj "It's a beginners class!"

    mrsj "You'll do fine!"

    show mrsj 57 with dissolve
    mrsj "Here is a list of the yoga moves to do in front of the class."

    show mrsj 58
    pause
    show mrsj 14
    show player 386
    with dissolve
    player_name "Terima kasih."

    show player 380
    pause
    show player 384
    player_name "Umm... These moves look pretty complicated..."

    show player 385
    show mrsj 17
    mrsj "My friend {b}Anna{/b} will be there to assist you during the class."

    show mrsj 18
    mrsj "She's my little eager beaver. Always willing to help and to please."

    show mrsj 14
    show player 386
    player_name "Oh. Okay... I'll try my best."

    show player 385
    show mrsj 49
    mrsj "You're so sweet. I'll make sure to pay you back one day!"

    show mrsj 17
    mrsj "I gotta go, so study those moves!"

    mrsj "Selamat tinggal!"

    show mrsj 14
    show player 386
    player_name "Bye, {b}Mrs. Johnson{/b}."

    show player 385
    hide mrsj with dissolve
    show player 381
    player_name "I should have a look at those instructions before I go to yoga class tonight..."

    hide player with dissolve
    call popup ('give', 'instructions1')
    return

label erikentrance_mrsj_yoga_thanks:
    scene expression game.timer.image("erik_entrance{}_c")
    show mrsj 17 at right
    show player 17 at left
    with dissolve
    mrsj "{b}[firstname]{/b}!!"

    mrsj "How did your first time instructing a yoga class go?"

    show mrsj 14
    show player 14
    player_name "I think I did okay?"

    show player 13
    show mrsj 17
    mrsj "Was {b}Anna{/b} able to help you?"

    show mrsj 14
    show player 14
    player_name "Yeah, she was there."

    player_name "She is really good at yoga..."

    show player 17
    player_name "... And flexible!"

    show player 13
    show mrsj 18
    mrsj "Ha ha ha!"

    show mrsj 49
    mrsj "{b}Anna{/b} can get into any position I put her in."

    mrsj "I've had her twisted up like a pretzel, once."

    show mrsj 50
    show player 12
    player_name "Benar-benar?"

    show player 11
    show mrsj 49
    mrsj "Oh yeah. She's very good in tight... Situations."

    mrsj "And a little baby oil doesn't hurt either..."

    show mrsj 50
    show player 13
    player_name "..."
    show mrsj 19
    mrsj "Umm... Anyway, so, you think you'd do it again?"

    show mrsj 14
    show player 14
    player_name "Well, she invited me to do more yoga with her at the gym in the evening."

    show player 13
    show mrsj 18
    mrsj "You should go!"

    show mrsj 49
    mrsj "{b}Anna{/b} can teach you a lot of things..."

    show mrsj 50
    show player 17
    player_name "I'm sure, haha."

    show player 13
    show mrsj 19
    mrsj "Thank you for helping me. Again."

    show mrsj 17
    mrsj "And don't think I've forgotten how much you've done for {b}Erik{/b} and me."

    show mrsj 49
    mrsj "I owe you... A lot."

    show mrsj 50
    show player 33
    player_name "Don't worry about it. It's no problem."

    hide player
    hide mrsj
    with dissolve
    return

label erikentrance_erik_feed_intro:
    scene expression game.timer.image("erik_inside{}_b")
    show player 10 with dissolve
    player_name "( It's quiet, is anyone home? )"

    player_name "( Maybe {b}Erik{/b} is in his room. )"

    show player 17
    player_name "( I hope he's not sleeping... Or doing something else. )"

    hide player with dissolve
    return

label erikentrance_erik_thief_thanks:
    scene expression game.timer.image("erik_entrance{}_c")
    show mrsj 19 at right
    show player 13 at left
    with dissolve
    mrsj "{b}[firstname]{/b}!"

    mrsj "I just wanted to say thank you so much for, you know, protecting us."

    show mrsj 20
    mrsj "It's pretty embarrassing you had to see my ex-husband like that..."

    show mrsj 19c
    show player 33
    player_name "I just wanted to make sure you didn't get your house broken into."

    show player 13
    show mrsj 17
    mrsj "I'm lucky to have such a wonderful neighbor..."

    show mrsj 14
    show player 17
    player_name "Oh, thanks!"

    show player 13
    show mrsj 49
    mrsj "I should... Reward you with something special, for what you've done for us..."

    show mrsj 50
    show player 4 with dissolve
    player_name "..."
    show player 29 with dissolve
    player_name "Uhh, you don't have to, {b}Mrs. Johnson{/b}!"

    show player 13 with dissolve
    show mrsj 49
    mrsj "Oh, no. I insist!"

    mrsj "I'll think of something and I'm sure you're going to like it..."

    show mrsj 50
    show player 17
    player_name "Haha, baiklah."

    hide player
    hide mrsj
    with dissolve
    return

label erikentrance_erik_poker_intro:
    scene expression game.timer.image("erik_inside{}_b")
    show player 14 at left
    show old_erik 1 zorder 1 at right
    with dissolve
    player_name "Hey, {b}Erik{/b}."

    show old_erik 4
    show player 1
    erik "Hey, did you find anyone?"

    show old_erik 1
    show player 10
    player_name "Not much so far, everyone is either busy or just doesn't want to come over."

    show old_erik 5
    show player 11
    erik "Even {b}Mia{/b}?"

    show old_erik 1
    show player 10
    player_name "I think she's busy with homework."

    show old_erik 3
    show player 5
    erik "Aww man, who else is gonna play cards with us?"

    show player 1
    show old_erik 1b at Position(xpos=870)
    show mrsj 17b zorder 2 at right
    with dissolve
    mrsj "Is something wrong, pumpkin?"

    show old_erik 4b
    show mrsj 14b
    erik "Oh, it's nothing, {b}Mrs. Johnson{/b}."

    show old_erik 1b
    show mrsj 18
    mrsj "Oh, come on! I heard you guys talking about inviting friends over."

    show old_erik 5b
    show mrsj 14b
    erik "Well, we can't find anyone to play poker with us."

    show old_erik 1b
    show mrsj 17
    mrsj "Ooh, that sounds fun!"

    show old_erik 5b
    show mrsj 14b
    erik "It would be more fun if we had other players..."

    show old_erik 1b
    show player 11
    show mrsj 17
    mrsj "Bagaimana dengan saya?"

    show player 13
    show mrsj 18
    mrsj "I'd like to play..."

    show player 1
    show old_erik 4b
    show mrsj 14b
    erik "Benar-benar?"

    show old_erik 1b
    show mrsj 17
    mrsj "Yeah! It's not fair that a couple of good boys like you can't find someone to play with..."

    mrsj "Tell you what, if you need another player, let me know, I'm always up for a nice poker night!"

    show old_erik 1
    show player 14
    show mrsj 14
    player_name "Kedengarannya luar biasa!"

    show player 17
    player_name "Thanks, {b}Mrs. Johnson{/b}."

    show player 1
    show old_erik 1 at right
    hide mrsj
    with dissolve
    pause
    show player 14
    player_name "Dude!! I can't believe {b}Mrs. Johnson{/b} is going to play with us."

    show old_erik 4
    show player 1
    erik "Well, I guess we found someone..."

    hide player
    hide old_erik
    with dissolve
    return

label erikentrance_erik_fork_intro:
    scene expression game.timer.image("erik_inside{}_b")
    show mrsj 17 at right
    show player 1 at left
    with dissolve
    mrsj "{b}[firstname]{/b}!"

    show player 11
    mrsj "Can I have a quick word with you before you go see {b}Erik{/b}?"

    show mrsj 14
    show player 14
    player_name "Sure, {b}Mrs. Johnson{/b}."

    show mrsj 20
    show player 11
    mrsj "I... I don't remember much of last night."

    show mrsj 19
    mrsj "Whatever happened, I want to apologize."

    show player 13
    mrsj "I drank too much, and I shouldn't have done those things with you boys."

    show mrsj 19c
    show player 10
    player_name "Oh, it's fine, {b}Mrs. Johnson{/b}..."

    show mrsj 19
    show player 13
    mrsj "You don't resent me, right?"

    show mrsj 19c
    show player 14
    player_name "Tentu saja tidak."

    player_name "I think it was fun!"

    show mrsj 19
    show player 1
    mrsj "What about {b}Erik{/b}?"

    mrsj "Did he have fun too?"

    show player 14
    show mrsj 14
    player_name "I... I think so?"

    show mrsj 17
    show player 1
    mrsj "Well... As long as you boys didn't find it too strange..."

    show mrsj 19c
    show player 14
    player_name "Did you talk to him about it?"

    show mrsj 19
    show player 11
    mrsj "No! God no."

    show mrsj 20
    mrsj "I don't want to make this more awkward than it already is."

    show mrsj 19
    mrsj "But... Could you do me a favor and talk to him about it?"

    mrsj "I just want to make sure he's not mad at me about it."

    show mrsj 14
    show player 14
    player_name "Sure, {b}Mrs. Johnson{/b}. I'll talk to him."

    show mrsj 18
    show player 1
    mrsj "Thanks, you're so sweet."

    hide player
    hide mrsj
    with dissolve
    return

label erikentrance_mrsj_cupid_couple:
    scene expression player.location.background_closeup
    show june 2 at Position (xpos=700)
    show old_erik 1 at right
    with None
    show player 14 at left
    with dissolve
    player_name "Oh, hey guys!"

    show player 1
    show old_erik 4
    erik "Hai, {b}[firstname]{/b}!"

    show june 3
    show old_erik 1
    june "Hai!"

    show player 14
    show june 2
    player_name "I didn't know you two were already hanging out!"

    show player 1
    show old_erik 4
    erik "Yeah, we've been playing {i}Ork Bork{/i} a lot..."

    show old_erik 1
    show june 6
    june "Haha. Yeah, we're totally addicted!"

    show june 2
    show player 14
    player_name "So, you two have been getting along fine, huh?"

    show player 1
    show old_erik 4
    if game.timer.is_dark():
        erik "Yeah, actually we have to do something... In my err... Room."

        show old_erik 1
        show player 11
        show june 3
        june "Yeah, we have to, uhm... Look over something?"

    else:
        erik "Yeah, actually we just finished..."

        show old_erik 1
        show player 11
        show june 3
        if game.timer.is_morning():
            june "Yeah, we have to get to school now, c'mon {b}Erik{/b}."

        else:
            june "Yeah, I have to get to the computer lab now."

    show june 2
    show player 14
    player_name "Oh... I see!"

    show player 17
    player_name "It's alright, I'll see you both another time."

    show player 1
    show june 6
    june "Sampai jumpa, {b}[firstname]{/b}."

    show june 2
    show old_erik 4
    erik "Later, man."

    hide june
    hide old_erik
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
