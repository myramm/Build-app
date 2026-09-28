label terry_dialogue_terry_start:
    show old_terry 1 at Position(xpos=0.6992,ypos=0.7047)
    show player 13 at left with dissolve
    pause
    show player 36
    player_name "Hello."
    show player 13
    show old_terry 2
    terry "Well, what have we here?"
    terry "Come to do a bit a fishin', have we?"
    show player 29
    show old_terry 1
    player_name "What makes you think that?"
    show player 3
    show old_terry 2
    terry "Oh ho, I know the look of a fisherman when I see one."
    show player 11
    terry "What's your name, lad?"
    show old_terry 1
    show player 14
    player_name "{b}[firstname]{/b}."
    show player 13
    show old_terry 2
    terry "Good to meet ya, {b}[firstname]{/b}!"
    terry "{b}Captain Terry{/b} at your service!"
    show player 14
    show old_terry 1
    player_name "Is this your dock?"
    show player 13
    show old_terry 2
    terry "Indeed it is... And this here's my shop."
    terry "Fish and tequila, the two things I love best in this world!"
    show old_terry 1
    show old_sara 4 at right with dissolve
    sara "..."
    show old_sara 5
    sara "The two things you love best, huh?"
    show player 11
    show old_sara 4
    show old_terry 17b
    terry "Err... well, not more than you of course..."
    show old_terry 18b
    show old_sara 5
    sara "Uh huh."
    show old_sara 2
    sara "And who's this then?"
    show player 13
    show old_sara 1
    player_name "..."
    show old_terry 2
    terry "This here's {b}[firstname]{/b} and he's come to do a bit of fishin'."
    show old_terry 1
    show player 29
    player_name "H-hello, Miss?"
    show old_terry 15
    terry "Meet the lovely {b}Sara{/b}."
    show player 14
    show old_terry 1
    player_name "Your wife?"
    show player 13
    show old_terry 16
    terry "Lord no, lad..."
    terry "... My wife is the sea!"
    show old_terry 15
    show old_sara 4
    terry "{b}Sara{/b} here means far more to me than any wife."
    show old_sara 3
    terry "She's the love of my life, my first mate, and my business partner!"
    show old_terry 1
    show old_sara 2
    sara "Hehe, alright, well done."
    sara "I'll forgive you for the fish and tequila remark."
    show player 13
    sara "Anything I can get for you boys, just give me a holler, okay?"
    show old_sara 1
    show old_terry 16
    terry "Will do my love, will do!"
    show old_terry 1
    show old_sara 2
    sara "Nice to meet you, {b}[firstname]{/b}."
    show player 36
    show old_sara 1
    player_name "You too {b}Miss Sara{/b}!"
    hide old_sara
    with dissolve
    pause
    show player 13
    show old_terry 15
    terry "Oh ho, I always hate to see her go but I sure do love to watch her leave."
    player_name "..."
    show player 2
    show old_terry 1
    player_name "So, where's the best place to fish around here {b}Captain Terry{/b}?"
    show player 1
    show old_terry 2
    terry "Well, right off the dock, of course!"
    terry "Just cast a line from that {b}chair{/b} over yonder and the fish won't be long comin'."
    show player 2
    show old_terry 1
    player_name "Alright, any other tips?"
    show player 1
    show old_terry 4 at Position(xpos=0.71,ypos=0.7047)
    terry "Hmm..."
    show old_terry 2 at Position(xpos=0.6992,ypos=0.7047)
    terry "... Pay close attention to what bait you're usin'."
    terry "Because not every fish likes the same type."
    show player 2
    show old_terry 1
    player_name "Okay, got it."
    show player 1
    show old_terry 2
    terry "Oh, and if you catch anything out there, remember, I'll buy it off ya for a good price!"
    show player 2
    show old_terry 1
    player_name "Alright, I'll keep that in mind."
    show player 1
    show old_terry 2
    terry "Oh, and don't go in the water!"
    show player 10
    show old_terry 1
    player_name "Huh?"
    player_name "How come?"
    show player 11
    show old_terry 2
    terry "There be dangerous things swimming 'round this dock."
    show player 10
    show old_terry 1
    player_name "Really?"
    show player 11
    show old_terry 2
    terry "You can bet your derriere on that!"
    terry "The fishin's great but you don't wanna be swimmin' here!"
    show player 10
    show old_terry 1
    player_name "Oh, umm... okay Captain."
    player_name "Thanks for letting me know."
    show player 11
    show old_terry 2
    terry "Aye, good luck out there, Skipper!"
    hide player with dissolve
    return

label terry_dialogue_terry_nemesis:
    show player 2 at left
    player_name "Hey, {b}Captain Terry{/b}, I-"
    show player 10
    player_name "Oh..."
    show player 11
    show tstand 3 at right with dissolve
    terry "I almost had him, {b}Sara{/b}!"
    terry "Had him {i}*Hic*{/i} had him right there on the dock!"
    show tstand 14
    sara "Yes, I know, dear."
    show tstand 3
    terry "The little demon snapped at my hand and I dropped 'em!"
    terry "Right back in th- {i}*Hic*{/i}"
    terry "Right back in the drink he went!"
    show tstand 14
    sara "Mhmm."
    show tstand 3
    terry "Ker Ssssplaaaaash!"
    terry "Oh hohohoho!"
    show player 10
    show tstand 5
    player_name "Uhh... you alright {b}Captain Terry{/b}?"
    show player 11
    show tstand 3
    terry "Skipper!"
    show tstand 15
    terry "Ooooh... Oh ho... I'm- {i}*Hic*{/i}"
    terry "I'm fiiiiiine!"
    terry "Feelin' just wonderfuuuul."
    show tstand 6
    sara "Hello {b}[firstname]{/b}."
    show player 36
    show tstand 5
    player_name "Hi, {b}Miss Sara{/b}."
    show player 10
    player_name "What's wrong with the captain?"
    show player 11
    show tstand 6
    sara "Nothing's wrong, {b}[firstname]{/b}"
    sara "He just had a bad day and too much tequila."
    show tstand 3
    terry "Ooh noooo... No, I'm- {i}*Hic*{/i}"
    terry "I'm sober as a- {i}*Hic*{/i}"
    terry "Sober as a church mouse."
    show tstand 6
    sara "I'm taking him to bed."
    show player 10
    show tstand 5
    player_name "Oh, okay."
    show player 11
    show tstand 3
    terry "That devil fish don't know who he's messin' with, I telllll yooouu!"
    show tstand 14
    sara "Aww, {b}Terry{/b}..."
    sara "... You can't keep doing this to yourself."
    show tstand 4
    show player 38
    player_name "Devil fish?"
    player_name "What's he on about?"
    show player 11
    show tstand 6
    sara "{i}*Sigh*{/i}"
    sara "I don't think he'd want me telling you."
    show tstand 3
    terry "Oh ho, non- {i}*Hic*{/i}"
    terry "Nonsense!"
    terry "I trust the Skipper here."
    show tstand 4
    sara "..."
    show tstand 14
    sara "You're sure?"
    show tstand 3
    terry "Ayeeee."
    show tstand 6
    sara "You see, {b}Terry{/b} here..."
    sara "... He's been chasing after this particular fish for years."
    show tstand 15
    terry "Tigger!"
    terry "Damn his scaly hide!"
    show player 10
    show tstand 5
    player_name "That's an odd name for a fish."
    show player 11
    show tstand 15
    terry "He ain't no fish!"
    terry "He's a devil, the ocean shat out to torment me, I tell ya!"
    show tstand 5
    player_name "..."
    show player 10
    player_name "Why does {b}Captain Terry{/b} hate him so much?"
    show player 11
    show tstand 6
    sara "Well, you see, a few years back, Tigger kinda... attacked {b}Terry{/b}."
    show tstand 5
    show player 12
    player_name "Attacked him?!"
    show player 11
    show tstand 3
    terry "Took me- {i}*Hic*{/i}"
    terry "Took me little piggy."
    show player 10
    show tstand 5
    player_name "Little piggy?"
    show player 11
    show tstand 15
    terry "You know, the one that went wee wee wee all the way home?"
    show player 3
    show tstand 5
    player_name "..."
    show tstand 6
    sara "... His toe."
    show player 29
    show tstand 5
    player_name "Ooooh!"
    show player 30
    player_name "Gross."
    show player 2
    player_name "So, that's why you warned me not to swim around the dock."
    show player 1
    show tstand 15
    terry "That's it exactly!"
    show player 2
    show tstand 5
    player_name "Can I help?"
    show player 1
    show tstand 3
    terry "Oh no, lad!"
    terry "Tigger's my curse and I can't be unleashin' him on someone else."
    show tstand 6
    sara "I really think it's best I get him into bed."
    sara "{b}[firstname]{/b}, why don't you come back another time?"
    show player 10
    show tstand 5
    player_name "Oh, okay {b}Miss Sara{/b}."
    show player 11
    show tstand 14
    sara "Come on {b}Terry{/b}."
    show tstand 3
    terry "Whatever you say, my- {i}*Hic*{/i}"
    terry "My love!"
    show tstand 3f at Position(xpos=1.05,ypos=1.0)
    terry "♪Ohhh, better far to live and die♪..."
    show tstand 3f at Position(xpos=1.25,ypos=1.0)
    terry "... ♪Under the brave black flag I fly♪..."
    hide tstand with dissolve
    show player 10
    player_name "I feel bad for the captain..."
    player_name "I wish I could help him."
    hide player with dissolve
    return

label terry_dialogue_terry_retire:
    show tstand 11 at right with dissolve
    terry "I tell ya, love... that fish is livin' on borrowed time!"
    terry "I'll mount his cursed hide in the shop for all to see!"
    show tstand 16
    sara "Oh {b}Terry{/b}, I don't see how a compass is going to accomplish that..."
    show tstand 10
    show player 36 at left with dissolve
    player_name "Hey Captain!"
    show tstand 12
    pause
    player_name "Hello, {b}Miss Sara{/b}."
    show player 1
    show tstand 13
    sara "Well, hi there, {b}[firstname]{/b}."
    sara "Come for a drink?"
    show tstand 11
    terry "Aye, a nice shot of tequila before you head out to fish!"
    show player 29
    show tstand 17
    player_name "Oh, no thank you..."
    player_name "... I actually came by to give you something, Captain."
    show player 3
    show tstand 17
    terry "Oh ho, you're too kind, Skipper."
    terry "What have you got for me this time?"
    show player 2
    player_name "Well..."
    show player 239_240
    pause
    show player 465 with hpunch
    show tstand 18
    player_name "... This!"
    show player 464
    terry "By Blackbeard's barnacled behind!"
    show tstand 2 zorder 1 at Position(xpos=.9,ypos=1.0)
    show old_sara 4 zorder 2 at Position(xpos=.8325,ypos=1.0) with dissolve
    terry "That's him!"
    terry "The Skipper caught old Tigger!"
    show player 465
    show tstand 1
    player_name "He put up one hell of a fight!"
    show player 464
    show old_sara 2
    sara "Wow, that is one ugly fish..."
    show old_sara 1
    show tstand 2
    terry "I told ya... straight outta hell that fish!"
    terry "Let's get a closer look at him!"
    show player 1
    show tstand 7
    terry "I can't believe it."
    show tstand 9
    terry "..."
    show tstand 8
    terry "I CAN'T believe it!"
    terry "You see {b}Sara{/b}... I told you the compass would do the trick!!"
    show tstand 9
    show old_sara 5
    sara "{b}Terry{/b}, the compass didn't do this... {b}[firstname]{/b} did!"
    show tstand 8
    show old_sara 4
    terry "Aye, he did... because I have the compass!"
    terry "Don't you see?!"
    pause
    terry "I've gotta get him inside, be right back!"
    show tstand 9
    hide tstand with dissolve
    show old_sara 2
    sara "I can't believe it's finally over."
    sara "This obsession of his is at an end."
    sara "You have no idea how much this means to me, {b}[firstname]{/b}!"
    sara "I'm afraid I'll never be able to repay you!"
    show player 2
    show old_sara 1
    player_name "Oh, that's okay, {b}Miss Sara{/b}."
    player_name "I just wanted to help {b}Caplan Terry{/b}."
    show player 1
    sara "..."
    player_name "Err, I mean... {b}CAPTAIN Terry{/b}."
    show old_sara 2
    sara "You're a good kid."
    sara "I..."
    show old_sara 1
    show tstand 2 at Position(xpos=.725,ypos=1.0)
    show old_sara 3
    terry "Do you know what this means?!"
    show tstand 1
    player_name "..."
    show old_sara 6
    sara "That we can finally talk about you retiring?"
    show tstand 2
    show old_sara 3
    terry "What?!"
    terry "Oh, sure, suuure... we'll get right to that, love."
    terry "After I've had myself a nice long swim!"
    hide tstand with dissolve
    show old_sara 4f
    terry "Hahahaha!"
    show old_sara 5f
    sara "Wait a second!"
    show old_sara 4f
    pause
    show old_sara 5f
    sara "{b}Terry{/b}!!!"
    show player 23
    sara "Oh my gosh, don't take those off... there's people watching!"
    show player 11
    show old_sara 4f
    pause
    show old_sara 5f
    sara "Ugh."
    hide old_sara with dissolve

    show player 13
    player_name "..."

    scene location_pier_running
    show text _ ("{b}Captain Terry{/b} had spent years avoiding that water...") as caption
    with fade
    pause
    hide caption with dissolve
    show text _ ("... But now that Tigger was finally gone, it seems he couldn't wait to get reacquainted.") as caption with dissolve
    pause
    hide caption with dissolve
    show text _ ("I couldn't contain my smile as I watched him gleefully bound into the water.") as caption with dissolve
    pause
    hide caption with dissolve
    show text _ ("The pride I felt at bringing him this moment...") as caption with dissolve
    pause
    hide caption with dissolve
    show text _ ("... Is something I'll never forget.") as caption with dissolve
    pause
    return

label terry_dialogue_terry_tigger_sign:
    scene location_pier_cutscene
    show text _ ("My first return to the captain's shack found him hard at work.") as caption
    with fade
    pause
    hide caption with dissolve
    show text _ ("It seemed {b}Captain Terry{/b} had wasted little time getting Tigger stuffed and mounted.") as caption with dissolve
    pause
    hide caption with dissolve
    show text _ ("True to his word, he was hanging his trophy up for all to see.") as caption with dissolve
    pause

    scene location_pier_day_closeup
    show tstand 1f
    with fade
    show tstand 2f
    terry "Hah, I bet my toe isn't tasting so good now is it, ya big ugly bastard?!"
    show tstand 1f
    show player 13 at left with dissolve
    player_name "..."
    show player 14
    player_name "I like the new wall ornament, Captain."
    show player 13
    show tstand 2 at right
    terry "Aye, it's a hell of a thing, isn't it Skipper?"
    terry "Thanks again, fer catchin' that menace."
    show tstand 1
    show player 14
    player_name "I'm just happy I could help."
    show tstand 2
    show player 13
    terry "Well, you're a good lad."
    terry "You let me know if there's ever anything me and mine can do for ya."
    show tstand 1
    show player 14
    player_name "Okay, Captain... I will!"
    show tstand 2
    show player 13
    terry "Anything at all now... ya hear me?"
    show tstand 1
    show player 14
    player_name "I hear you."
    show player 13
    pause
    show player 12
    player_name "So, where is {b}Miss Sara{/b} at today?"
    show tstand 2
    show player 11
    terry "Ahh, she's off plannin' for our vacation."
    show tstand 1
    show player 10
    player_name "Vacation, huh?"
    player_name "Where you going?"
    show tstand 2
    show player 11
    terry "Wherever the lady says... Hah!"
    show tstand 1
    show player 14
    player_name "Haha, I'm happy for you guys."
    player_name "When are you leaving?"
    show tstand 2
    show player 13
    terry "Bah, I'd wager not anytime soon Skipper."
    terry "The little lady is just full of excitement right now."
    terry "What with me finally hanging up the hat and all."
    show tstand 1
    show player 14
    player_name "Oh, okay!"
    show tstand 2
    show player 13
    terry "Speaking of my retirement; I wanted to let you know..."
    terry "... I'll still buy any fish that you catch off my dock there Skipper."
    show tstand 1
    show player 10
    player_name "But I thought you weren't gonna sell them anymore?"
    show tstand 2
    show player 11
    terry "Well, I'm still allowed to eat 'em, aren't I?"
    show tstand 1
    show player 10
    player_name "Oh, y-yeah... of course!"
    show tstand 2
    show player 11
    terry "Oh ho, you know I can't get on without my fish and tequila..."
    show player 13
    terry "... And the fresher the fish the better!"
    show tstand 1
    show player 14
    player_name "Alright, I'll keep that in mind, Captain."
    show tstand 2
    show player 13
    terry "Good lad!"
    terry "Well, I reckon I'd best be off."
    show tstand 1
    pause
    show tstand 2
    terry "Remember now, anything you need, I'm yer man!"
    show tstand 1
    show player 14
    player_name "Alright, Captain! I'll see ya around!"
    show player 13
    hide tstand with dissolve
    show player 4
    player_name "( Hmm, I bet {b}Aqua{/b} would let me catch a few fish here and there. )"
    player_name "( Now that {b}Captain Terry{/b} is retired. )"
    return

label terry_dialogue_intro:
    show old_terry 1 at Position(xpos=0.6992,ypos=0.7047)
    show player 36 at left with dissolve
    player_name "Hey Captain!"
    show player 203
    show old_terry 2
    terry "Well, hello there Skipper!"
    terry "Anything I can do for ya?"
    return

label terry_dialogue_buy_fish:
    show old_terry 1
    show player 4
    pause
    show player 12
    player_name "Do you have any fresh fish for sale?"
    show player 203
    show old_terry 2
    terry "Of course! You came to the right place."
    terry "I have sea trout, snapper and mackerel."
    terry "What'll it be?"
    return

label terry_dialogue_buy_fish_buy:
    if not player.has_money(100):
        call expression game.dialog_select("terry_dialogue_buy_fish_buy_no_money")
        call expression game.dialog_select("terry_dialogue_buy_fish_nevermind")

    call expression game.dialog_select("terry_dialogue_buy_fish_buy_pre")

    if fish == "Seatrout":
        show old_terry 5
        $ player.get_item("seatrout")

    elif fish == "Snapper":
        show old_terry 6
        $ player.get_item("snapper")

    elif fish == "Mackerel":
        show old_terry 7
        $ player.get_item("mackerel")

    call expression game.dialog_select("terry_dialogue_buy_fish_buy_after")
    $ player.spend_money(100)
    return

label terry_dialogue_buy_fish_buy_no_money:
    player_name "( I don't have enough money... )"
    return

label terry_dialogue_buy_fish_buy_pre:
    show player 4
    pause
    show player 2
    player_name "{b}[fish]{/b}."
    terry "That's a great choice!"
    show old_terry 4
    terry "Let me get that for you..."
    return

label terry_dialogue_buy_fish_buy_after:
    terry "Here ya go, mate!"
    show player 17
    player_name "Thank you!"
    return

label terry_dialogue_buy_fish_nevermind:
    show player 10
    show old_terry 1
    player_name "Hmm... I think I'll pass."
    show player 203
    show old_terry 2
    terry "No problem, mate! Maybe some other time."
    return

label terry_dialogue_sell_fish:
    scene expression game.timer.image("pier_closeup{}")
    show old_terry 1 at Position(xpos=0.6992,ypos=0.7047)
    show player 4 at left
    pause
    show player 13
    show old_terry 2
    terry "Caught anything good, Skipper?"
    show old_terry 1
    show player 14
    player_name "Yeah, actually, I was wondering if you wanted to buy them."
    show player 13
    show old_terry 2
    terry "Of course, lad."
    terry "What do you have?"
    show old_terry 1
    return

label terry_dialogue_sell_fish_sell:
    call expression game.dialog_select("terry_dialogue_sell_fish_sell_pre")

    if fish == "Seatrout":
        show old_terry 5
        $ player.remove_item("seatrout")

    elif fish == "Snapper":
        show old_terry 6
        $ player.remove_item("snapper")

    elif fish == "Mackerel":
        show old_terry 7
        $ player.remove_item("mackerel")

    call expression game.dialog_select("terry_dialogue_buy_fish_buy_after")
    $ player.get_money(80)
    call popup ('earn', 80)
    return

label terry_dialogue_sell_fish_sell_pre:
    show player 14
    player_name "Here's a fresh {b}[fish]{/b}."
    show player 13
    show old_terry 2
    terry "Nice catch, lad!"
    show old_terry 4
    terry "Let me get your money."
    show old_terry 1
    return

label terry_dialogue_sell_fish_nevermind:
    show player 10
    show old_terry 1
    player_name "Hmm... Actually, it must have wiggled out..."
    show player 13
    show old_terry 2
    terry "No problem, mate! Maybe some other time."
    show old_terry 1
    return

label terry_dialogue_buy_drink_pre:
    show player 12
    show old_terry 1
    player_name "You sell drinks?"
    show player 11
    show old_terry 3
    pause
    show old_terry 2
    terry "Only one kind: pure tequila gold!"
    terry "$5 a shot, mate."
    return

label terry_dialogue_buy_drink:
    if not player.has_money(5):
        call expression game.dialog_select("terry_dialogue_buy_drink_no_money")
    else:

        call expression game.dialog_select("terry_dialogue_buy_drink_buy")
        $ player.spend_money(5)
    return

label terry_dialogue_buy_drink_no_money:
    player_name "( I don't have enough money... )"
    return

label terry_dialogue_buy_drink_buy:
    show player 188
    show old_terry 1
    pause
    show player 189
    pause
    show player 190
    pause
    show player 191
    player_name "Ugh! That's really strong!"
    show player 185
    show old_terry 2
    terry "Haha!"
    terry "It's the good stuff! You'll get used to it!"
    return

label terry_dialogue_buy_drink_pass:
    show old_terry 1
    show player 10
    player_name "I think I'll pass. I can't drink that stuff."
    show old_terry 2
    show player 203
    terry "No problem, mate! Maybe some other time."
    return

label terry_dialogue_fishing:
    show player 2
    show old_terry 1
    player_name "Can I try to catch some fish here?"
    show player 203
    show old_terry 3
    pause
    show old_terry 2
    terry "I see the open water is catching your eye."
    show player 31f at Position(xpos=-0.1412,ypos=1.0000) with dissolve
    show old_terry
    terry "Just {b}use the chair at the end of the pier{/b}. It's a great spot!"
    show player 203 at left with dissolve
    terry "Make sure you have a {b}fishing rod{/b}, and that you're using the right {b}bait{/b}."
    show old_terry 3
    pause
    show old_terry 2
    terry "Oh! If you catch anything, come back here, and I'll buy them off you for a reasonable price."
    return

label terry_dialogue_fishing_bait:
    show player 2
    show old_terry 1
    player_name "Can you tell me more about the bait types?"
    show player 203
    show old_terry 2
    terry "Sure thing, mate!"
    terry "First, you need to know what kind of fish you're tying to catch."
    terry "Every {b}kind of fish likes a specific type of bait{/b}!"
    terry "Sea trout like worms, snapper like blue bait, and mackerel like the green baits!"
    show player 2
    show old_terry 1
    player_name "Awesome! Thanks for the tip!"
    player_name "But where could I find those different types of bait?"
    show player 203
    show old_terry 2
    terry "I don't sell equipment in my shack."
    terry "You'll have to {b}look around town{/b} to find them."
    show player 2
    show old_terry 1
    player_name "I see..."
    player_name "Thanks, {b}Captain Terry{/b}!"
    return

label terry_dialogue_secret:
    show player 2 at left
    show old_terry 1 at Position(xpos=0.6992,ypos=0.7047)
    player_name "How did you get so good at fishing, Captain?"
    show old_terry 2
    show player 203
    terry "Oh ho, years of practice, Skipper."
    show player 2
    show old_terry 1
    player_name "Is that all?"
    show old_terry 2
    show player 203
    terry "Well, I also got a secret weapon!"
    show old_terry 1
    show player 14
    player_name "Really?!"
    player_name "Could you show me?"
    show old_terry 15
    show player 203
    terry "Hah, you can't be expectin' a master fisherman to reveal all his secrets!"
    show old_terry 1
    show player 2
    player_name "Aww, c'mon Captain. You can tell me!"
    show old_terry 2
    show player 203
    terry "Hmm."
    show old_terry 16
    terry "Ahaha, well, you're a persistent on, aren't ya?"
    terry "I like that!"
    show old_terry 15
    terry "Every good fisherman needs persistence."
    show old_terry 2
    terry "Alright Skipper, c'mere and I'll show you my secret lure."
    show old_terry 9 at Position(xpos=0.671,ypos=0.7047)
    show player 14
    player_name "Secret lure?"
    player_name "Neat!"
    player_name "What's it do?"
    show old_terry 10
    show player 203
    terry "Oh ho, this baby catches everything!"
    terry "The fish just can't resist it!"
    show old_terry 9
    show player 14
    player_name "Wow!"
    player_name "Would you sell it to me?"
    show old_terry 11
    show player 203
    terry "Haha, sell it to you?!"
    terry "Lad, it's priceless!"
    show old_terry 13
    show player 24
    player_name "Oh, I see."
    show old_terry 11
    terry "Well, don't be lookin' so down..."
    show old_terry 10
    terry "... I tell you what... You find me something equally priceless and I'll trade you."
    show old_terry 1 at Position(xpos=0.6992,ypos=0.7047)
    show player 12
    player_name "Well, what did you have in mind?"
    show old_terry 2
    show player 11
    terry "How about the {b}Golden Compass{/b}?"
    show old_terry 1
    show player 12
    player_name "What's that?"
    show old_terry 2
    show player 11
    terry "An old fisherman's tale."
    terry "Long ago, there was a great builder of ships livin' around these parts."
    terry "They say he possessed a golden compass that could lead you to your heart's desire."
    show old_terry 1
    show player 12
    player_name "That sounds made up!"
    show old_terry 15
    show player 11
    terry "Ho ho, aye, that it does lad."
    show old_terry 2
    terry "But if such a thing were to exist..."
    terry "I reckon it would be well worth tradin' my lure for."
    terry "What do you say?"
    show old_terry 1
    show player 14
    player_name "Hmm, I suppose I could look into it."
    show old_terry 2
    show player 13
    terry "There's a good lad!"
    show old_terry 1
    show player 14
    player_name "Where do you recommend I start?"
    show old_terry 2
    show player 13
    terry "I'd start searchin' for the ship builder."
    terry "If he really existed, I reckon he's buried somewhere in the town graveyard."
    show old_terry 1
    show player 14
    player_name "Sounds good, what was his name?"
    show old_terry 16
    show player 13
    terry "Oh ho, I haven't the slightest."
    show old_terry 1
    show player 10
    player_name "Ah, jeez."
    show old_terry 2
    show player 11
    terry "Maybe you should ask around town?"
    terry "One of the {b}older residents{/b} might know something."
    show old_terry 1
    show player 10
    player_name "Alright, I guess I'd better get started."
    show old_terry 2
    show player 13
    terry "Best of luck, Skipper!"
    show old_terry 1
    show player 14
    player_name "Thanks, Captain."
    return

label terry_dialogue_lure:
    show old_terry 1 at Position(xpos=0.6992,ypos=0.7047)
    show player 14 at left
    player_name "What did you want in trade for the lure again?"
    show old_terry 2
    show player 13
    terry "I'm afraid nothin' short of the {b}Golden Compass{/b} will do, Skipper."
    show old_terry 1
    show player 14
    player_name "Oh, that's right!"
    player_name "Where should I start looking?"
    show old_terry 2
    show player 13
    terry "I'd ask around town if I were you."
    terry "See if {b}any of the older residents know somethin' about the guy who owned it{/b}."
    terry "It's said he was a great builder of ships."
    show old_terry 1
    show player 14
    player_name "Okay, thanks Captain."
    return

label terry_dialogue_golden_compass:
    show player 2 at left
    show old_terry 1 at Position(xpos=0.6992,ypos=0.7047)
    player_name "You still got that lure, Captain?"
    show player 1
    show old_terry 15
    terry "You betcha! Never let it out of my sight."
    show player 2
    show old_terry 1
    player_name "Good, because guess what I've brought you?"

    show old_terry 19
    show player 239_240
    pause
    show player 466
    show old_terry 17
    terry "Couldn't be..."
    show player 467
    show old_terry 19
    player_name "I found it! I found the {b}Golden Compass{/b}!"
    show player 466
    show old_terry 17
    terry "You're kiddin'!"
    show player 467
    show old_terry 19
    player_name "Here, have a look!"

    show player 1
    show old_terry 21 at Position(xpos=0.654,ypos=0.712)
    pause
    show old_terry 22
    terry "By Blackheart's slimy backside!"
    terry "The damned thing does exist!"
    show player 10
    show old_terry 21
    player_name "..."
    player_name "You mean you didn't really believe in it?"
    show player 5
    show old_terry 22
    terry "Lord no, lad. I never intended to part with my lure..."
    terry "I need it to catch Tigger and my lure is the only bait he's ever gone after."
    terry "Well, ignorin' my missin' piggy, of course."
    show player 24
    show old_terry 21
    player_name "Oh, I see."

    show old_terry 4 at Position(xpos=0.71,ypos=0.7047)
    pause
    show old_terry 10 at Position(xpos=0.671,ypos=0.7047)
    terry "I reckon this belongs to you now!"

    show player 470
    show old_terry 2 at Position(xpos=0.6992,ypos=0.7047)
    pause
    show player 471
    player_name "What? But you just said-"
    show player 470
    show old_terry 15
    terry "Well, I don't need it now, do I Skipper?!"
    show old_terry 16
    terry "I've got the Golden Compass."
    show old_terry 15
    show player 13
    terry "A golden compass that will lead me to my heart's desire."
    terry "And since my heart desires that little bastard's head..."
    terry "Well, I'd say this is a fair trade, wouldn't you?"

    show player 14
    show old_terry 1
    player_name "Yeah!"
    show player 13
    show old_terry 2
    terry "Now you just be careful usin' that lure!"
    terry "It sometimes catches... {i}unexpected things{/i}."
    show player 14
    show old_terry 1
    player_name "I'll be careful, Captain."
    show player 13
    show old_terry 22 at Position(xpos=0.654,ypos=0.712)
    terry "Good lad. Now, let me have a look at this beauty!"
    show old_terry 21
    show player 34f
    player_name "( Hmm... {i}Unexpected things{/i}? )"
    player_name "( I wonder what that means? )"
    call popup ('give', 'special_lure')
    return

label terry_dialogue_retire:
    show player 2 at left
    show old_terry 1 at Position(xpos=0.6992,ypos=0.7047)
    player_name "Hey, Captain... I have a question for you..."
    show player 1
    show old_terry 2
    terry "What can I do for you, Skipper?"
    show player 2
    show old_terry 1
    player_name "You ever thought about retiring from the fishing business?"
    show player 1
    show old_terry 19
    terry "Hmm..."
    show old_terry 20
    terry "To tell ya the truth, Yes."
    terry "I've been thinkin' about it for a few years now."
    show player 2
    show old_terry 1
    player_name "Really?"
    show player 1
    show old_terry 17
    terry "Don't get me wrong, lad... I love the hunt!"
    show old_terry 20
    terry "Nothin' beats a day on the sea, rod in the water, the breeze in my beard..."
    show old_terry 15
    terry "... That is... nothin' but my {b}Sara{/b}."
    show player 2
    show old_terry 1
    player_name "You really love her, huh, Captain?"
    show player 1
    show old_terry 15
    terry "Aye lad, I really do..."
    show old_terry 17
    terry "... And she's been wantin' me to retire for as long as I can remember."
    show old_terry 20
    terry "Says she wants to travel a bit, see the world."
    show old_terry 17
    terry "Truth be told I think she just wants me around more often."
    show player 2
    show old_terry 1
    player_name "So why don't you do it?"
    show player 1
    show old_terry 17
    terry "I can't, Skipper..."
    terry "... Not in good conscious!"
    terry "Not while that demon fish is still out there lurkin' about!"
    show player 10
    show old_terry 18
    player_name "Ahh, Tigger?"
    show player 11
    show old_terry 20
    terry "{i}*Spits*{/i} Aye, Tigger."
    show old_terry 2
    terry "But now that you've brought me the Golden Compass..."
    terry "... It's only a matter of time till that bastard meets his end!"
    show player 10
    show old_terry 1
    player_name "Okay, well, thanks for being honest with me, Captain."
    show player 11
    show old_terry 2
    terry "Don't mention it, Skipper!"
    show old_terry 16
    terry "You proved yourself a true blue friend to me and mine."
    show player 34
    show old_terry 1
    player_name "( I bet if I caught Tigger, {b}Captain Terry{/b} would quit fishing. )"
    player_name "( I have to try... {b}Aqua{/b} is counting on me! )"
    return

label terry_dialogue_fake_id:
    show old_terry 1 at Position(xpos=0.6992,ypos=0.7047)
    show player 10 at left
    player_name "Hey, {b}Captain Terry{/b} can I ask you something?"
    show player 5
    show old_terry 2
    terry "Aye, what is it Skipper?"
    show old_terry 1
    show player 10
    player_name "I heard a rumor recently..."
    player_name "... And I was wondering if you know anything about making fake IDs?"
    show player 5
    show old_terry 17b
    terry "Oh ho, whereabouts did you hear a rumor like that?!"
    show old_terry 18
    show player 29 with dissolve
    player_name "Heh, I umm..."
    show player 10 with dissolve
    player_name "... Well, let's just say a friend mentioned it."
    show player 5
    show old_terry 17
    terry "Hmm, I see."
    terry "Well, if I did know somethin', lad..."
    terry "... It wouldn't be too smart for me to go blabbin' about it, now would it?"
    show old_terry 18
    show player 10
    player_name "Yeah, I suppose not."
    show player 5
    show old_terry 15
    terry "What's a fine boy like you needin' a fake ID for anyways?"
    terry "I'm more than happy to give ya a drink or two from the bar."
    show old_terry 3 with dissolve
    show player 10
    player_name "It's not for me, {b}Captain{/b}..."
    show old_terry 1 with dissolve
    player_name "... You see, there's this... Umm, girl."
    show player 5
    show old_terry 2
    terry "Oh, found yourself a pretty one have ya?"
    show old_terry 1
    show player 29 with dissolve
    player_name "Y-yeah."
    show player 3
    show old_terry 15
    terry "Well, say no more then!"
    show old_terry 16
    terry "If the lady needs a fake ID, then a fake ID I shall provide!"
    show old_terry 1
    show player 14 with dissolve
    player_name "Really?"
    show player 13
    show old_terry 15
    terry "Sure!"
    terry "Just {b}bring me an up-to-date photo of the lass and four hundred dollars{/b}."
    terry "I'll get it done in a jiffy!"
    show old_terry 1
    show player 17
    player_name "Thanks, {b}Captain{/b}!"
    show player 13
    show old_terry 16
    terry "My pleasure, Skipper."
    show old_terry 3 with dissolve
    player_name "( I should {b}go and tell Roxxy{/b} the good news! )"
    return

label terry_dialogue_fake_id_picture_first:
    show old_terry 1 at Position(xpos=0.6992,ypos=0.7047)
    show player 14 at left
    player_name "So, about that {b}fake ID{/b}..."
    show player 13
    show old_terry 15
    terry "Oh, did you bring me a photo?"
    show old_terry 1
    show player 14
    player_name "Yup, I've got it!"
    show player 239_240 with dissolve
    pause
    show player 646 with dissolve
    player_name "Here you go."
    show player 13
    show old_terry 9b
    with dissolve
    terry "Bonny's backside!"
    terry "You weren't kidding, Skipper..."
    terry "... You've netted yourself a siren!"
    show old_terry 13b
    show player 14
    player_name "Heh, yeah."
    show player 13
    show old_terry 10b
    terry "You'd best be careful with this one..."
    terry "... Siren songs are pretty but most men go chasin' them don't ever return!"
    pause
    terry "You've ehh, got the four hundred dollars as well?"
    show old_terry 1
    return

label terry_dialogue_fake_id_picture_repeat:
    show old_terry 1 at Position(xpos=0.6992,ypos=0.7047)
    show player 10 at left
    player_name "I was hoping you could make that {b}fake ID{/b} for me now?"
    show player 5
    show old_terry 2
    terry "I sure can, Skipper."
    terry "You have the four hundred dollars?"
    show old_terry 1
    return

label terry_dialogue_fake_id_yes:
    show player 14
    player_name "Of course."
    player_name "I should go call the girls and tell them where to pick it up."
    show player 13
    show old_terry 15
    terry "Sounds like a plan, Skipper."
    show old_terry 1
    show player 14
    player_name "I'll be back."
    scene black with fade
    scene expression game.timer.image("pier_closeup{}")
    show old_terry 2 at Position(xpos=0.6992,ypos=0.7047)
    show player 13 at left
    with dissolve
    terry "Just a few more minutes, Skipper."
    show old_terry 1
    show player 14
    player_name "Awesome, thanks so much for this, {b}Captain Terry{/b}."
    show player 13
    show old_terry 15
    terry "Oh ho ho, it's my pleasure, lad."
    show old_terry 1
    roxxy "There you are, finally!"
    show old_roxxy 1bf at Position (xpos=500)
    show old_becca 1 at Position(xpos=315)
    show old_missy 1 at left
    show player 13f at right
    with dissolve
    roxxy "This place wasn't easy to find!"
    show old_roxxy 1f f
    show old_missy 2
    missy "Uhh, what's that smell?"
    show old_missy 2b
    show old_terry 18
    show player 10f
    player_name "... Fish?"
    show player 5f
    show old_becca 2b with dissolve
    becca "Eugh, disgusting!"
    show old_becca 1 with dissolve
    terry "..."
    show old_terry 17
    terry "Disgusting?!"
    terry "Lass, this is how I make my living, you know..."
    show old_terry 18
    show old_becca 2
    becca "Gross."
    show old_becca 1
    terry "..."
    show old_terry 17
    terry "I hadn't realized you were into the prissy, snobbish type, Skipper."
    show old_terry 18
    show player 10f
    player_name "I'm not really."
    show player 5f
    show old_becca 8
    becca "Pfft, as if!"
    becca "You don't stand a chance, nerd!"
    show old_becca 1
    show old_missy 6
    missy "Haha!"
    show old_missy 1
    show old_roxxy 28f at Position (xoffset=33) with dissolve
    roxxy "{i}*Sigh*{/i}"
    show old_roxxy 1bf with dissolve
    roxxy "So, you make fake IDs, huh?"
    show old_roxxy 1f f
    show old_terry 17
    terry "Aye."
    terry "But don't you go spreading that around, ya hear?"
    show old_terry 17b
    terry "My little side business isn't exactly above board."
    show old_terry 18
    show old_roxxy 4f
    roxxy "Well, I think it's pretty cool!"
    show old_roxxy 1bf
    roxxy "How did you meet this guy, {b}[firstname]{/b}?"
    show old_roxxy 1f f
    show old_terry 15
    terry "Oh ho, the Skipper and I are thick as thieves!"
    terry "He's quite the little fisherman, he is!"
    show old_terry 1
    show old_roxxy 2f
    roxxy "Oh, you fish too?"
    show old_roxxy 1f f
    show player 14f
    player_name "Yeah, every now and then."
    show player 13f
    show old_roxxy 2f
    roxxy "Eugh, fish freak me out."
    roxxy "Aren't they like... you know, slimy?"
    show old_roxxy 1f f
    show player 10f
    player_name "Ehh, yeah... sometimes, I guess."
    show player 5f
    show old_missy 1b
    missy "Awesome!"
    show old_missy 1
    show old_becca 2b with dissolve
    becca "Eww, no!"
    show old_becca 1 with dissolve
    show old_terry 18
    show old_missy 2
    missy "Oh, right. I meant..."
    show old_missy 3
    show old_roxxy 3cf
    roxxy "Would you two shut up?!"
    show old_roxxy 3df
    show old_missy 2b
    terry "..."
    show old_roxxy 1f f
    show old_terry 15
    terry "Well, this {b}fake ID{/b} should be good to go."
    show old_terry 1
    show old_roxxy 1bf
    roxxy "Oh, lemme see!"
    show old_roxxy 4f
    roxxy "Finally, we won't have to rely on {b}Dexter{/b} for booze..."
    roxxy "... This weekend is gonna be awesome!"
    show old_roxxy 1f f
    show player 14f
    player_name "Yeah, it sounds like a lot of fun."
    show player 13f
    show old_becca 2
    becca "Umm, you're not invited, loser!"
    show old_becca 3
    show player 5f
    show old_missy 2
    missy "... He's not?"
    show old_missy 2b
    show old_becca 3b
    becca "No way!"
    show old_becca 1
    show player 24f
    player_name "..."
    show old_roxxy 2f
    roxxy "Yeah, sorry {b}[firstname]{/b}..."
    roxxy "... It's just, I've got a reputation to uphold, you know?."
    show old_roxxy 1f f
    show old_terry 17
    terry "Now hold on just a minute!"
    terry "The Skipper here has just gone and spent four hundred dollars on you lot..."
    terry "... And you're not even inviting him to the party?!"
    terry "That's a real shit thing to do."
    show old_terry 18
    show old_becca 3
    show old_missy 1b
    missy "I think he should come!"
    show old_missy 1
    show old_becca 3b
    becca "Shut up, {b}Missy{/b}!"
    becca "Everyone will see him with us!"
    show old_becca 1
    show old_roxxy 2f
    roxxy "Yeah, we can't be seen hanging out with him."
    show old_roxxy 1f f
    show old_terry 17
    terry "Well, I'm thinking maybe I don't give you this fake ID after all."
    show old_terry 18
    show player 5f
    show old_roxxy 2bf
    roxxy "..."
    show old_terry 17
    terry "That's right."
    terry "Four hundred dollars is a lot of money for a lad his age and you gals are gonna have to make a return on his investment."
    show old_terry 18
    show old_roxxy 3cf
    roxxy "You serious, old man?!"
    show old_roxxy 3f
    roxxy "We don't have any money!"
    show old_roxxy 3bf
    show old_terry 15
    terry "Well, maybe you should give him something else then?"
    show old_terry 1
    show old_roxxy 3df
    roxxy "..."
    show old_roxxy 3cf
    roxxy "Like what?"
    show old_roxxy 3df
    show old_terry 15
    terry "How about your friends there give him a peek at what's hidin' under them shirts?"
    show old_terry 1
    show player 13f
    show old_roxxy 2bf
    show old_becca 2
    becca "WHAT?!"
    becca "I'm not flashing him!"
    show old_becca 3
    show old_missy 1b
    missy "I'll do it!"
    show old_roxxy 1f f
    show old_missy 1
    show old_becca 3b
    becca "Ugh, of course you will..."
    becca "... You're such a skank."
    show old_becca 3
    show old_missy 2
    missy "Hey, I am not!"
    show old_missy 2b
    show old_roxxy 2f
    roxxy "Fine by me."
    show old_roxxy 1f f
    show old_becca 2
    becca "{b}Roxxy{/b}, I'm not taking my tits out in from of them!"
    show old_becca 1
    show old_roxxy 2f
    roxxy "Just shut up and do it, {b}Becca{/b}."
    roxxy "Nobody else is around."
    show old_roxxy 1f f
    show old_becca 3b
    becca "Yeah, but-"
    show old_becca 1
    show old_roxxy 3 at Position (xpos=550) with dissolve
    roxxy "Do you want the booze or not?!"
    show old_roxxy 3d
    show old_becca 3
    show old_missy 1b
    missy "I do!"
    show old_missy 9 with dissolve
    show old_roxxy 1
    pause
    show old_missy 10 with dissolve
    pause
    show old_roxxy 1f f at Position (xpos=500) with dissolve
    show old_terry 15
    terry "Oh ho ho!"
    show old_terry 1
    show old_missy 11
    show old_terry 15
    terry "Now those are some nice perky ones, don't you think, Skipper?!"
    show old_terry 1
    show player 14f
    player_name "... Yeah!"
    show player 13f
    show old_missy 10
    missy "You really like them, {b}[firstname]{/b}?!"
    show old_missy 11
    show player 17f
    player_name "Heh, definitely!"
    show player 13f
    show old_missy 11b
    missy "See, {b}Becca{/b}!"
    show old_missy 11
    show old_becca 8
    becca "You actually like those little mosquito bites?!"
    show old_becca 7
    show player 14f
    player_name "What's not to like?"
    show player 13f
    show old_terry 15
    terry "Ho ho, the captain's never met a pair of breasts he didn't like!"
    show old_terry 1
    show old_roxxy 30 at Position (xpos=550) with dissolve
    roxxy "C'mon {b}Becca{/b}... Everyone is waiting!"
    show old_roxxy 3d
    show old_becca 2
    becca "{i}*Sigh*{/i} Fine!"
    show old_becca 9 with dissolve
    show old_roxxy 1
    pause
    show old_becca 10
    show old_terry 15
    terry "Oh ho ho, not bad!"
    show old_terry 1
    show old_roxxy 1f f at Position (xpos=500) with dissolve
    show player 14f
    player_name "Wow!"
    show player 13f
    show old_becca 11
    becca "See, way better than {b}Missy{/b}'s skittle tits..."
    show old_becca 11b
    show old_missy 11b
    missy "Screw you {b}Becca{/b}!"
    missy "At least mine aren't all covered in freckles!"
    show old_missy 11c
    show old_becca 11c
    becca "Pshh, shows what you know..."
    becca "... Lots of guys like my freckles!"
    show old_becca 11b
    show old_missy 11b
    missy "Yeah, right."
    show old_missy 11c
    show old_terry 15
    terry "Hahaha!"
    terry "Well, what say you, Skipper?!"
    terry "Which pair do you like more?"
    show old_terry 1
    show old_missy 11
    show old_becca 10
    return

label terry_dialogue_fake_id_yes_becca:
    show player 14f
    player_name "Heh, I like {b}Becca{/b}'s."
    show player 13f
    show old_becca 11c
    becca "See, I knew {b}[firstname]{/b} would agree!"
    show old_becca 11b
    show old_missy 4d with dissolve
    missy "..."
    show old_becca 9 with dissolve
    pause 1
    show old_becca 2 with dissolve
    becca "Even nerdy guys like him like big tits."
    show old_becca 3
    show old_missy 4c
    missy "..."
    show old_missy 4d
    missy "{i}*Sniff*{/i}"
    hide old_missy with dissolve
    show old_becca 3b
    becca "Sheesh, what a baby."
    show old_becca 2
    becca "Can we have the {b}ID{/b} now?"
    show old_becca 1
    show old_terry 15
    terry "What do you think, lad?"
    show old_terry 1
    show player 14f
    player_name "Yeah, they earned it."
    show player 13f
    show old_terry 2
    terry "Very well, here ya go, Pixie."
    show old_terry 1
    show old_roxxy 3cf
    roxxy "Umm, it's {b}Roxxy{/b}."
    show old_roxxy 3df
    show old_terry 2
    terry "Uh huh."
    terry "C'mon, Skipper!"
    terry "Let's get a bottle of tequila and head out to the dock for a bit..."
    terry "... I'll tell ya about the time I spotted a mermaid over by the cove!"
    show old_terry 15
    show player 14f
    player_name "Cool!"
    hide old_terry
    hide player
    with dissolve
    terry "She was naked as the day she was born and prettier than them three snobby girls combined!"
    terry "I had a lot of tequila that day, but I swear on my mother she was blue like the sea!"
    show old_becca 2
    becca "C'mon, {b}Roxxy{/b}."
    show old_roxxy 3d at Position (xpos=550) with dissolve
    becca "We'd better go and find little Miss Weeps-a-lot."
    show old_becca 1
    show old_roxxy 30
    roxxy "... Yeah."
    hide old_becca with dissolve

    show old_roxxy 1kf at Position (xpos=500) with dissolve
    roxxy "..."
    hide old_roxxy with dissolve
    return

label terry_dialogue_fake_id_yes_missy:
    show old_terry 1 at Position(xpos=0.6992,ypos=0.7047)
    show old_roxxy 1f f at Position (xpos=500)
    show old_becca 10 at Position(xpos=315)
    show old_missy 11 at left
    show player 17f at right
    with dissolve
    player_name "Heh, I like {b}Missy{/b}'s!"
    show player 13f
    show old_roxxy 2bf
    show old_missy 10
    missy "YES!!!"
    show old_missy 7
    show old_becca 11
    becca "WHAT?!"
    show old_becca 9 with dissolve
    pause 1
    show old_becca 1 with dissolve

    show old_missy 8
    missy "You're the best, {b}[firstname]{/b}!"
    show old_missy 7
    show old_becca 3b
    becca "Psh, whatever."
    becca "Who cares what some nerd thinks?!"
    hide old_becca with dissolve
    show old_roxxy 1bf
    roxxy "Don't mind her."
    roxxy "She's just being a bitch."
    show old_roxxy 1f f
    show old_missy 1b
    missy "{b}Roxxy{/b}, did you hear?!"
    missy "{b}[firstname]{/b} said my tits were better than {b}Becca{/b}'s!!!"
    show old_missy 1
    show old_roxxy 3cf
    roxxy "{i}*Sigh*{/i} Of course I heard..."
    roxxy "... I'm not deaf, am I?!"
    show old_roxxy 29f
    show old_missy 6
    missy "Hehehe!"
    show old_missy 1
    show old_roxxy 3cf
    roxxy "Can we have the {b}ID{/b} now?"
    show old_roxxy 3df
    show old_terry 2
    terry "What do you think, lad?"
    show old_terry 1
    show player 14f
    player_name "Yeah, they earned it."
    show player 13f
    show old_roxxy 1f f
    show old_terry 2
    terry "Very well, here ya go, Pixie."
    show old_terry 1
    show old_roxxy 3cf
    roxxy "Umm, it's {b}Roxxy{/b}."
    show old_roxxy 3df
    show old_terry 2
    terry "Uh huh."
    terry "C'mon, Skipper!"
    terry "Let's get a bottle of tequila and head out to the dock for a bit..."
    terry "... I'll tell ya about the time I spotted a mermaid over by the cove!"
    show old_terry 15
    show player 14f
    player_name "Cool!"
    hide old_terry
    hide player
    with dissolve
    terry "She was naked as the day she was born and prettier than them three snobby girls combined!"
    terry "I had a lot of tequila that day, but I swear on my mother she was blue like the sea!"
    show old_missy 2
    missy "Ugh, {b}Becca{/b} can be such a drama queen..."
    show old_missy 2b
    show old_roxxy 30f
    roxxy "Yeah, we'd better go and find her."
    hide old_missy with dissolve

    show old_roxxy 1kf at Position (xpos=500) with dissolve
    roxxy "..."
    hide old_roxxy with dissolve
    return

label terry_dialogue_fake_id_no:
    show player 10
    player_name "Oh, crap."
    player_name "I forgot about the four hundred dollars."
    show player 5
    show old_terry 16
    terry "Hah! No worries lad."
    show old_terry 17
    terry "Just come back and see me when you have it."
    show old_terry 1
    show player 10
    player_name "Yeah, okay."
    hide player with dissolve
    return

label terry_dialogue_goldschwagger:
    scene expression game.timer.image("pier_closeup{}")
    show old_terry 1 at Position(xpos=0.6992,ypos=0.7047)
    show player 10 at left
    with dissolve
    player_name "Have you ever heard of {b}GoldSchwagger Vodka{/b}?"
    show player 5
    show old_terry 2
    terry "Oh, sure!"
    terry "That's the one with the little gold flecks in it, aye?"
    show old_terry 1
    show player 14
    player_name "Yeah, that's the stuff!"
    show player 13
    show old_terry 2
    terry "Oh ho, my {b}Sara{/b}... She can't get enough of that stuff, bless her heart."
    terry "I don't understand the fascination, myself."
    terry "It's a bit on the weak side if you ask me."
    terry "I guess the lady folk just like seeing all that gold!"
    show old_terry 1
    show player 14
    player_name "Heh, yeah..."
    player_name "So, you have any extra bottles I could buy off you?"
    show player 13
    show old_terry 2
    terry "Hmm, you know... I just might at that!"
    show old_terry 4 at Position(xpos=0.71,ypos=0.7047) with dissolve
    terry "Let me see here..."
    show old_terry 23 with dissolve
    terry "Aye, this one is good and fresh..."
    show old_terry 23b
    show player 14
    player_name "Wow, it's so... Shiny!"
    show player 13
    show old_terry 23
    terry "Oh ho ho!"
    terry "I tell ya what, Skipper. Why don't you go ahead and take it."
    terry "Free of charge!"
    show old_terry 23b
    show player 10
    player_name "Huh?"
    show player 12
    player_name "You don't want any money for it?"
    show player 13
    show old_terry 23
    terry "Ah, I've a feeling it's for those pretty lasses you were with the other day, aye?"
    show old_terry 23b
    show player 12
    player_name "... Yeah, it's for the redhead."
    show player 13
    show old_terry 23
    terry "Oh, the snobby one!"
    terry "Boy, she had a pair of tits on her, didn't she?!"
    show old_terry 23b
    show player 17
    player_name "..."
    show player 13
    show old_terry 23
    terry "You take it, lad."
    show player 653
    show old_terry 16 at Position(xpos=0.6992,ypos=0.7047)
    with dissolve
    terry "What kind of wingman would I be if I charged ya for it?!"
    show player 654b
    show goldschwagger_label at Position (xoffset=-88,yoffset=-220)
    with dissolve
    show old_terry 15
    terry "Besides, I think my {b}Sara{/b} is finally coming around on the tequila!"
    terry "Which is good!"
    terry "A proper drink, for a proper lady!"
    terry "Wouldn't you agree, Skipper?!"
    show old_terry 1
    show player 654
    player_name "Hah, if you say so, {b}Captain Terry{/b}!"
    player_name "Thanks so much for this!"
    show player 654b
    show old_terry 2
    terry "Don't mention it!"
    terry "Now you go and get 'em, Skipper!"
    show old_terry 1
    hide player
    hide goldschwagger_label
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
