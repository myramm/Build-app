label button_ross_ask_model:
    scene expression player.location.background_closeup
    show old_ross 25 at left
    show player 1f at right
    ross "Any luck?"
    show player 2f
    show old_ross 24
    player_name "Not yet."
    show player 1f
    show old_ross 25
    ross "Well, make sure you {b}ask all your classmates{/b}."
    show old_ross 25b
    ross "Hopefully, somebody will be brave enough to model for us..."
    return

label button_ross_found_model:
    scene expression player.location.background_closeup
    show player 2f zorder 1 at right
    show old_judith 1 zorder 2 at Position(xpos=0.65, ypos=1.0)
    show old_ross 10 zorder 2 at left
    with dissolve
    player_name "I'm back {b}Miss Ross{/b} and I found us a model!"
    show player 1f
    show old_ross 11
    ross "{i}*Gasp*{/i} {b}Judith{/b}!"
    show old_ross 27 with dissolve
    ross "This is perfect! She's got a wonderful body for this!"

    show old_ross 26
    show old_judith 4
    pause
    show old_judith 5
    judith "Oh umm, {b}Miss Ross{/b} is gonna be here too huh?"
    show player 10f
    show old_judith 1
    player_name "Yeah, is that alright?"
    show player 11f
    show old_judith 3
    judith "I dunno..."
    show old_judith 6
    show old_ross 27
    ross "Oh look at her turning red, how delightful!"
    show old_ross 60 with dissolve
    ross "Here, sweetie, take this and go change out of those clothes."

    ross "We'll wait right here for you."
    show old_ross 59
    show old_judith 3
    judith "Umm..."
    show old_ross 60
    show old_judith 6
    ross "Don't dawdle, we want as much time with you as possible."

    hide old_judith
    show old_ross 11
    with dissolve
    ross "Great job, {b}[firstname]{/b}! She's gonna make a superb model!"
    show old_ross 10
    show player 1f
    pause
    show old_mia 8b zorder 0 at Position(xpos=0.65, ypos=1.0) with dissolve
    pause
    show old_ross 11

    ross "... And here's our little cutie pie, just in time!"
    show old_ross 10
    show old_mia 12b
    mia "Yeah, I couldn't find anybody. I'm sorry guys..."
    show old_ross 11
    show old_mia 8b
    ross "Oh, no worries! {b}[firstname]{/b} came through like he always does."
    show old_ross 10
    show old_mia 10b
    mia "Really? You actually got someone to volunteer?"
    show old_mia 9
    mia "That's amazing, {b}[firstname]{/b}!"
    show old_mia 11
    show player 2f
    player_name "... Yeah, {b}Judith{/b} agreed to-"
    show old_judith 59f zorder 0 at Position(xpos=0.35, ypos=1.0)
    show player 11f
    with dissolve
    pause
    show old_judith 44f
    show old_judithr 1f zorder 1 at Position(xpos=0.35, ypos=1.0)
    with dissolve
    show old_mia 7
    pause
    show old_judith 45f
    judith "... What's {b}Mia{/b} doing here?!"
    show old_judith 44f
    show old_ross 11
    ross "She's going to be drawing you as well, sweetie."
    show old_judith 45f
    show old_ross 10
    judith "I'm having second thoughts about all this..."
    show old_judith 52f
    judith "I thought it was just gonna be you and I, {b}[firstname]{/b}!"
    show old_judith 51f
    show old_ross 25
    ross "Calm down, {b}Judith{/b}... Everything is going to be fine, dear."
    show old_ross 11
    ross "You have nothing to be embarrassed about. Does she guys?"
    show old_ross 10
    show player 2f
    player_name "Not at all."
    show player 1f
    show old_mia 10
    mia "Yeah, don't worry, {b}Judith{/b}. {b}Miss Ross{/b} has been teaching us that everyone's body is beautiful."
    show old_mia 7
    show old_ross 11
    ross "That's right, {b}Mia{/b}. They're all beautiful in their own unique way."
    ross "You should be proud of your body, {b}Judith{/b}."
    show old_ross 10
    show old_judith 52f
    judith "I dunno..."
    show old_judith 51f
    show old_ross 58 with dissolve
    ross "I've got an idea!"
    hide old_ross with dissolve
    pause
    show old_ross 40 zorder 2 at left with dissolve

    ross "These always calm me down when I'm feeling anxious..."
    ross "Everybody take one."
    show old_ross 41
    show player 2f
    player_name "Oh, I've heard you make the best brownies!"
    show player 1f
    show old_ross 40
    ross "Hehe, you better believe it!"
    ross "It's my secret recipe..."
    show old_ross 44 with dissolve
    pause
    show old_ross 43 with dissolve
    ross "... One hundred percent all natural."
    hide player
    show player 602 zorder 4 at right
    with dissolve
    show old_ross 42
    pause
    show player 599f with dissolve
    pause
    show player 600f
    show old_mia 73 zorder 3 at Position(xpos=0.55, ypos=1.0)
    with dissolve
    pause
    hide old_judith
    hide old_judithr
    show old_mia 71
    show old_judith 60 zorder 5 at Position(xpos=0.60, ypos=1.0)
    with dissolve
    pause
    hide old_judith
    show old_mia 71 at Position(xpos=0.65, ypos=1.0)
    show old_judith 47f zorder 0 at Position(xpos=0.35, ypos=1.0)
    show old_judithr 1f zorder 1 at Position(xpos=0.35, ypos=1.0)
    with dissolve
    pause
    show old_mia 72

    mia "Yum!! These are delicious!"
    show old_mia 71
    show old_judith 48f
    judith "{i}*Nom nom nom*{/i}"
    show old_ross 43
    show old_judith 47f
    ross "Take it slow, {b}Judith{/b}. You don't wanna eat these too fast."
    show old_ross 42
    show old_judith 48f
    judith "Oh my gosh! They're so good!"
    show old_judith 49f
    judith "Mmm..."
    show old_mia 74f
    show player 26f
    player_name "Heh, they had a kinda... Earthy flavor."
    show player 13f
    show old_ross 13
    ross "How's everybody feeling?"
    show old_ross 12
    show player 26f
    player_name "Goooood. Really gooood."
    show player 13f
    show old_judith 50f
    judith "Meeee tooo."
    show old_judith 49f
    show old_mia 75bf at Position(xpos=0.63, ypos=1.0) with dissolve
    mia "Heheheheheheheehee!"
    show old_judith 50f
    show old_mia 74f at Position(xpos=0.65, ypos=1.0) with dissolve
    judith "This robe is super itchy!"
    show old_judith 49f
    show old_ross 13
    ross "Well, now that you're feeling more relaxed, why don't you take it off, sweetie."
    ross "We can get this show on the road."
    show old_ross 12
    show old_judith 50f
    judith "Mmm, yeah, okay..."
    hide old_judith
    hide old_judithr
    show old_judith 56f zorder 0 at Position(xpos=0.35, ypos=1.0)
    with dissolve
    pause
    show old_judith 49f with dissolve
    pause
    show old_ross 13
    ross "Very good, dear."
    show old_ross 11
    ross "Now then, {b}[firstname]{/b} and {b}Mia{/b}, why don't you two get seated and find your charcoal."
    show old_ross 10
    show old_mia 75bf at Position(xpos=0.63, ypos=1.0) with dissolve
    mia "Heheheheeahahaaha!"
    mia "Everything is so twirly!!"
    show old_mia 74f at Position(xpos=0.65, ypos=1.0) with dissolve
    show old_ross 11
    ross "Yes, it sure is, cutie pie."
    show old_ross 13
    ross "{b}Judith{/b} you need to take off your underwear too, sweetie."
    show old_ross 12
    show old_judith 51f
    judith "Hmm?"
    show old_judith 52f
    judith "You mean I have to show my..."
    judith "My..."
    judith "... Pussy?"
    show old_judith 51f
    show old_mia 75bf at Position(xpos=0.63, ypos=1.0) with dissolve
    mia "Pffftt!!! AHahahaah! That's such a funny word!"
    mia "Puuuusssy! HahahaaH!"
    show old_mia 74f at Position(xpos=0.65, ypos=1.0) with dissolve
    show old_ross 11
    ross "Heh, calm down, {b}Mia{/b}!"
    show old_ross 25
    ross "You're still feeling self-conscious, {b}Judith{/b}?"
    show old_ross 24
    judith "Mmmhmm..."
    show old_ross 11
    ross "Well, what if the rest of us stripped down too?"
    show old_ross 10
    show old_judith 54f
    pause
    show old_judith 55f
    judith "... Yeah! That's a good idea!"
    show old_judith 54f
    show player 26f
    player_name "You want us to get naked too?"
    show player 13f
    show old_ross 11
    ross "We'll just strip down to our underwear."
    ross "That should be good enough, right {b}Judith{/b}?"
    show old_ross 10
    show old_judith 55f
    judith "... Yeah! I wanna see {b}[firstname]{/b}'s underwear!"
    show old_judith 54f
    show old_ross 11
    ross "Very good then..."
    hide old_ross
    show old_ross 14 at Position(xpos=0.15, ypos=1.0)
    with dissolve
    pause
    show old_ross 15 at Position(xpos=0.14, ypos=1.0) with dissolve
    pause
    show old_ross 16 at Position(xpos=0.13, ypos=1.0) with dissolve
    pause
    show old_ross 17 with dissolve
    pause
    show old_ross 36 at Position(xpos=0.15, ypos=1.0) with dissolve
    ross "Go ahead you two..."
    show old_ross 37
    show old_mia 75f with dissolve
    mia "... Wait! Me?"
    show old_mia 74f
    show old_ross 36
    ross "Especially you, cutie pie!"
    show old_ross 37
    show old_mia 75bf at Position(xpos=0.63, ypos=1.0) with dissolve
    mia "Heheheheheeeh, okey-dokey!"
    show old_mia 76f at Position(xpos=0.62, ypos=1.0) with dissolve
    pause
    show old_mia 77f at Position(xpos=0.64, ypos=1.0) with dissolve
    pause
    show old_mia 78f at Position(xpos=0.66, ypos=1.0) with dissolve
    pause
    show old_mia 79f at Position(xpos=0.66, ypos=1.0) with dissolve
    pause
    show old_mia 80f at Position(xpos=0.66, ypos=1.0) with dissolve
    pause
    show old_mia 81f at Position(xpos=0.65, ypos=1.0) with dissolve
    show old_ross 36
    ross "You didn't have to take off your bra, cutie pie!"
    show old_mia 82f
    show old_ross 37
    mia "I didn't?"
    show old_mia 81f
    show old_ross 36
    ross "Hehe, nope I said, \"Down to our underwear.\""
    show old_mia 82f
    show old_ross 37
    mia "Ooooh..."
    mia "Okey-dokey!"
    show old_mia 82bf at Position(xpos=0.635, ypos=1.0) with dissolve
    mia "This is fun!"
    show old_mia 81f at Position(xpos=0.65, ypos=1.0) with dissolve
    show old_ross 36
    ross "Yes, it certainly is, dear."
    ross "We're waiting, {b}[firstname]{/b}."
    show old_ross 37
    show player 21f
    player_name "Y-yeah. Okay!"
    show player 8f with dissolve
    pause
    show player 265f with dissolve
    pause
    show old_judith 53f
    pause
    show player 267f
    player_name "( !!! )" with hpunch
    judith "... Wow!"
    show old_mia 82bf at Position(xpos=0.635, ypos=1.0) with dissolve
    mia "It looks kinda angry! Pffft, hahahahaa!!!"
    show old_mia 81f at Position(xpos=0.65, ypos=1.0) with dissolve
    show old_judith 55f
    judith "It's so big..."
    show old_judith 54f
    show player 265bf
    show old_ross 36
    ross "It sure is, dear."
    ross "... You still have to take those panties off before we can draw you."
    show old_ross 37
    show old_judith 55f
    judith "... And pink."
    show old_judith 54f
    show old_ross 36
    ross "Here, I'll help!"
    hide old_ross
    show old_judith 61f at Position(xpos=0.22, ypos=1.0) with dissolve
    pause 
    show old_judith 62f with dissolve
    pause
    hide old_judith
    show old_judith 66f zorder 1 at Position(xpos=0.35, ypos=1.0)
    show old_ross 36 zorder 0 at left
    with dissolve
    ross "There's a good girl."
    ross "Now, go stand over there on the pedestal for me, okay?"
    show old_ross 37
    show old_judith 66f
    judith "..."
    show old_ross 36
    hide old_judith with dissolve

    ross "You two start drawing."
    show old_ross 37
    show player 265cf
    player_name "Yes, ma'am."

    scene location_school_art_cutscene08
    show text _ ("I could tell {b}Judith{/b} was still really nervous as {b}Miss Ross{/b} helped her up onto the pedestal.") as caption
    with fade
    pause
    hide caption with dissolve
    show text _ ("It was very brave of her to model for an audience.") as caption with dissolve
    pause
    hide caption with dissolve
    show text _ ("... But she wasn't exactly striking an inspirational pose up there.") as caption with dissolve
    pause

    scene expression player.location.background_closeup
    show old_judith 65b zorder 1 at Position(xpos=0.5, ypos=1.0)
    show old_ross 37 zorder 0 at left
    with fade
    pause
    show old_ross 36
    ross "Sweetie? You have to loosen up a little..."
    show old_ross 37
    show old_judith 66
    judith "I don't..."
    judith "I mean, I..."
    hide old_ross
    show old_ross 36f zorder 0 at Position(xpos=0.7, ypos=1.0)
    with dissolve
    show old_judith 65b
    ross "Shhh."
    ross "It's alright, {b}Judith{/b}."
    hide old_ross
    show old_judithross 2 zorder 0 at Position(xpos=0.685, ypos=1.0)
    with dissolve
    ross "Just breathe in deeply..."
    show old_judith 66
    pause
    show old_judith 65b
    ross "... That's it."
    show old_judithross 1
    pause
    show old_judithross 2
    ross "You're a beautiful angel, {b}Judith{/b}."
    show old_judithross 1
    show old_judith 66
    judith "... I am?"
    show old_judithross 2
    show old_judith 65b
    ross "Oh yes! You're breathtaking, sweetie!"
    show old_judithross 1
    pause
    hide old_judithross
    show old_judith 67 at Position(xpos=0.4, ypos=1.0)
    with dissolve
    ross "Spread your wings, {b}Judith{/b}."
    ross "Let the world see you fly!"
    show old_judith 68b
    show old_ross 36f at Position(xpos=0.65, ypos=1.0)
    with dissolve
    ross "{i}*Gasp*{/i} Perfection!"
    show old_judith 69
    show old_ross 37f
    judith "... You think I'm perfect?"
    show old_judith 68
    show old_ross 36f
    ross "Of course, sweetie!"
    ross "Just look at that curvaceous body..."
    ross "How could anyone resist it?"
    show old_ross 37f
    pause
    show old_ross 36f
    ross "Now, don't you move an inch!"
    ross "Give the artists a chance to capture your beauty!"
    show old_ross 37f
    show old_judith 69b
    judith "O-okay..."

    scene location_school_art_cutscene07
    show text _ ("{b}Miss Ross{/b} had definitely made {b}Judith{/b} more comfortable.") as caption
    with fade
    pause
    hide caption with dissolve
    show text _ ("... And she had given me the perfect inspiration for my drawing!") as caption with dissolve
    pause
    hide caption with dissolve
    show text _ ("Though it was little hard to concentrate on my work with {b}Miss Ross{/b} hovering over my shoulder...") as caption with dissolve
    pause

    scene expression player.location.background_closeup
    show old_judith 68 zorder 1 at Position(xpos=0.4, ypos=1.0)
    show old_ross 36f zorder 0 at Position(xpos=0.65, ypos=1.0)
    with fade
    ross "It's very good, {b}[firstname]{/b}, but I think you could do better."
    ross "I'm not sure you're really capturing the curves of her delicious body."
    show old_ross 37f
    player_name "What do you mean?"
    show old_ross 36f
    ross "Well, have a look!"
    ross "Sometimes you have to really get hands on with your subject and feel the shapes."
    ross "... And {b}Judith{/b} here has such great contours!"
    hide old_ross
    show old_judith 70
    with dissolve
    pause
    show old_judith 71 with dissolve
    pause
    show old_judith 72 with dissolve
    pause
    show old_judith 72b
    judith "( !!! )" with hpunch
    judith "AAAhh!"
    show old_judith 72e
    ross "... Well, look who came out to play!"
    show old_judith 72c_72d
    pause
    judith "Mmm..."
    show old_judith 72e
    ross "How does that feel, sweetie?"
    show old_judith 72
    judith "Really..."
    judith "Ahh, really good!"
    show old_judith 72e
    ross "Yes, you just enjoy, dear."
    show old_judith 72c_72d
    judith "NNGGHH!"
    pause
    show old_judith 72
    judith "Haaaah!"
    show old_judith 72e
    ross "Beautiful!"
    show old_judith 72
    judith "OH, I CAN'T!"
    show old_judith 73 zorder 1 at Position(xpos=0.45, ypos=1.0)
    show old_ross 37f zorder 0 at Position(xpos=0.65, ypos=1.0)
    with dissolve
    judith "( !!! )" with hpunch
    judith "AAAHHH!"
    show old_judith 66
    judith "Haaah... Haaah..."
    show old_judith 65
    show old_ross 36f
    ross "Very good, sweetie!"

    show old_judith 58f zorder 0 at left
    show old_ross 37f
    with dissolve
    judith "That was..."
    show old_judith 57f
    judith "..."
    show old_judith 58f
    judith "... Can we do that again?"
    show old_judith 57f
    show old_ross 36f
    ross "... Maybe later, sweetie."
    show old_ross 36 at Position(xpos=0.60, ypos=1.0)
    with dissolve
    ross "Do you understand now, what I mean about feeling the shapes, {b}[firstname]{/b}?"
    show old_ross 37
    player_name "I'm not sure..."
    show old_mia 82 zorder 1 at Position(xpos=0.35, ypos=1.0) with dissolve

    mia "I think I get it, {b}Miss Ross{/b}!"
    show old_mia 81
    show old_ross 36f with dissolve
    ross "Good, you can help me show him then."
    show old_ross 36 with dissolve
    ross "Come up here and join us, {b}[firstname]{/b}!"
    show old_ross 37
    player_name "Really?"
    show old_ross 36
    ross "Yes, this is something every good artist needs to understand."
    hide old_mia
    hide old_ross
    show old_rossg 3 at Position(xpos=0.60, ypos=1.0)
    with dissolve
    player_name "O-okay."
    show old_rossg 1
    ross "Now, go ahead."
    show old_rossg 2
    ross "Both of you..."
    show old_rossg 1
    ross "... Feel the shapes."
    show old_rossg 4
    mia "Hehehe, okay!"
    show old_rossg 5_6 with dissolve
    pause
    show old_rossg 3 with dissolve
    player_name "... Like that?"
    show old_rossg 1
    ross "Mmmhmm... Just like that..."
    show old_rossg 4
    mia "Hehehee, I hope God isn't watching..."
    show old_rossg 2
    ross "You're both doing a great job!"
    show old_rossg 1
    ross "Keep going."
    show old_rossg 5_6 with dissolve
    pause
    ross "Mmm..."
    pause
    show old_rossg 1 with dissolve
    ross "Very good, {b}[firstname]{/b}!"
    show old_rossg 2
    ross "Now try feeling, {b}Mia{/b}'s shapes."
    show old_rossg 3
    player_name "I uhh..."
    show old_rossg 4
    mia "It's okay!"
    mia "Feel the shapes, {b}[firstname]{/b}!"
    show old_rossg 7_8 at Position(xpos=0.59, ypos=1.0) with dissolve
    pause
    show old_rossg 4 at Position(xpos=0.6, ypos=1.0) with dissolve
    mia "Honk honk!"
    show old_rossg 9 with dissolve
    mia "Pfft, hahahahaha!!"
    show old_rossg 2 with dissolve
    ross "Oh, isn't she just the most adorable thing ever?!"
    ross "Alright, now feel mine again..."
    show old_rossg 5_6 with dissolve
    pause
    show old_judith 58f
    judith "... You guys can feel my shapes if you want."
    show old_judith 57f
    show old_rossg 2 with dissolve
    ross "Well, goodness! Look who's finally coming out of her shell!"
    ross "We'll get to you in a second, sweetie. Why don't you go check the supply cabinet for me..."
    ross "There should be some incense and candles in there to help us set the mood."
    show old_judith 58f
    show old_rossg 5_6 with dissolve
    judith "... Yes, ma'am."
    hide old_judith
    with dissolve
    pause
    show old_rossg 10 with dissolve
    smith "WHAT IN THE WORLD IS GOING ON IN HERE?!" with hpunch
    smith "WHY ARE YOU ALL NAKED?!"
    hide old_rossg
    show old_mia 83 zorder 2 at left
    show old_ross 39 zorder 1 at Position(xpos=0.25, ypos=1.0)
    show player 100 zorder 0 at Position(xpos=0.35, ypos=1.0)
    show principal 3 at right
    with dissolve
    ross "{b}Mrs. Smith{/b}! I was just teaching the students some art techniques..."
    show old_ross 38
    show principal 38
    smith "ART TECHNIQUES?! DO I LOOK LIKE AN IDIOT TO YOU?!"
    show old_ross 39
    show principal 3
    ross "Of course not, we were just-"
    show principal 28
    show old_ross 38
    smith "DO I NEED TO REMIND YOU THAT THIS IS A SCHOOL AND NOT A BROTHEL!"
    show old_ross 39
    show principal 3
    ross "You're being ridiculous, I'm just trying to help them improve their art."
    hide principal
    show principal 34 zorder 3 at Position(xpos=0.65, ypos=1.0)
    with dissolve
    show old_ross 38
    smith "JUST GET SOME CLOTHES ON, ALL OF YOU!" with hpunch

    hide old_mia
    hide player
    show principal 29 at right
    show old_ross 17 at Position(xpos=0.25, ypos=1.0)
    with dissolve
    pause
    show old_ross 16 at Position(xpos=0.25, ypos=1.0) with dissolve
    pause
    show old_ross 15 at Position(xpos=0.26, ypos=1.0) with dissolve
    pause
    show old_ross 14 at Position(xpos=0.26, ypos=1.0) with dissolve
    pause
    show old_ross 24 zorder 1 at Position(xpos=0.25, ypos=1.0)
    show old_mia 41 zorder 2 at left
    show player 8 zorder 0 at Position(xpos=0.35, ypos=1.0)
    with dissolve
    show principal 27
    smith "You had better have a damn good explanation for this, {b}Barbara{/b}!"
    show old_mia 45
    show player 11 at Position(xpos=0.38, ypos=1.0)
    with dissolve
    show old_ross 25
    show principal 29
    ross "{b}Mia{/b} and I were helping {b}[firstname]{/b} here practice."
    ross "Trying to prepare him for-"
    show old_ross 24
    ross "..."
    show principal 27
    smith "Prepare him for what?!"
    show principal 29
    show old_mia 46
    mia "This ar-"
    show old_mia 45
    show old_ross 25
    ross "A gift!"
    ross "... He was going to paint something for you, {b}Mrs. Smith{/b}!"
    show old_ross 24
    pause
    show old_ross 25
    ross "A gift, to hang up in your office!"
    show old_ross 24
    show principal 27
    smith "A gift?! For me?! What, like a portrait?"
    show principal 29
    show old_ross 25
    ross "Well, sure! If that's what you want..."
    show principal 27
    show old_ross 24
    smith "Is he any good?"
    show old_ross 25
    show principal 29
    ross "Very good, come have a look for yourself!"
    show principal 41 with dissolve
    pause
    show principal 42
    smith "What the hell is this?"
    show principal 41
    show old_mia 46
    mia "Oh, that's umm... That's mine, ma'am."
    mia "... I'm not very good."
    show old_mia 45
    smith "..."
    show principal 42
    smith "Then why are you here, after school, taking private courses?"
    show principal 41
    show old_ross 25
    ross "My classes aren't just for talented artists."
    ross "They are open to anyone with a desire to express themselves through art."
    ross "... And {b}Mia{/b} here has a great love for art."
    show old_ross 24
    show principal 42
    smith "Uh huh..."
    smith "In reality, you just found yourself a cute little package, didn't you?"
    show principal 41
    show old_ross 25b
    ross "That's not..."
    show old_ross 24
    show principal 42
    smith "... And now you're just working to unwrap it, huh?"
    smith "Have yourself a little taste?"
    smith "... I'm well aware of your methods {b}Barbara{/b}."
    hide principal
    show principal 43 at Position(xpos=0.7, ypos=1.0)
    with dissolve
    pause
    show principal 44 at Position(xpos=0.72, ypos=1.0) with dissolve
    smith "Hmm."
    show principal 45
    smith "The boy painted this?"
    show principal 44
    show player 10
    player_name "Yes, ma'am."
    show player 11
    show principal 45
    smith "Well, I guess I was wrong about you, {b}[firstname]{/b}."
    smith "You're actually good for something, after all..."
    show principal 44
    show old_ross 11
    ross "He is very talented, isn't he?"
    show old_ross 24
    hide principal
    show principal 27 at right
    with dissolve
    smith "Oh, shut up!"
    smith "I should fire you, right here and now!"
    smith "In here getting groped by naked students..."
    hide principal
    show principal 35b at Position(xpos=0.83, ypos=1.0)
    with dissolve
    smith "..."
    show principal 35c
    smith "This is impressive work though."
    show principal 35
    smith "Hmm..."
    hide principal
    show principal 27 at right
    with dissolve
    smith "I'm feeling generous, so I {i}MIGHT{/i} let this incident slide!"
    show old_ross 25
    show principal 26
    ross "That would be wond-"
    show old_ross 24
    show principal 27
    smith "... But only if your student here can recreate this quality on a portrait of me!"
    show principal 26
    show old_ross 25
    ross "Oh, that's shouldn't be a problem. Right, {b}[firstname]{/b}?"
    show old_ross 24
    show player 10
    player_name "Uhh..."
    show player 11
    show principal 27
    smith "And it has to be to my exact specifications!"
    smith "No funny business!"
    show principal 29
    show old_ross 25
    ross "Oh, of course! Anything you want, ma'am."
    show principal 27
    show old_ross 24
    smith "Damn right, anything I want!"
    show principal 27
    smith "Now you kids get your asses home before I change my mind and expel you both!"
    show principal 29
    show old_ross 25
    ross "Go on you two. I'll see you tomorrow."
    return

label button_ross_found_model.replay:
    $ player.go_to(L_school_artclassroom)
    jump button_ross_found_model
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
