label ross_button_dress_code:
    show anon f_worried:
        flip
    show ross a_sides:
        flip
    with dissolve
    anon "Hi {b}Miss Ross{/b}, I was hoping you could talk to {b}Mrs. Smith{/b} about the new dress code policy..."
    ross f_confused "She's implementing a new dress code policy?!"
    ross "B-but this is a public school!!"
    anon f_skeptical "I know, right?!"
    anon f_worried @ f_skeptical "It's ridiculous!"
    ross f_angry a_hip_angry "I hope she's not planning to stuff you students into big ugly uniforms, because I won't stand for it!"
    ross "Kids your age need to express themselves, otherwise, it can stifle your development into adults!"
    anon "Well, there's nothing concerning clothing, really..."
    ross "I swear, I'll march right down there and-"
    pause
    ross f_confused a_hip "Wait a second, there's no restriction on clothing?"
    anon "No, ma'am..."
    anon "... But it prohibits hair dye and I thought-"
    ross f_normal a_sides @ f_laugh "Well, that's not so bad..."
    ross "Why are you so upset, {b}[firstname]{/b}?"
    ross @ f_eyeroll "You don't even color your hair..."
    anon @ a_rub f_tired "Y-yeah, but-"
    ross "Phew, you really had me worked up for a moment!"
    anon "I'm worried about {b}Eve{/b}."
    anon "She really likes her blue hair and-"
    ross "Oh, {b}Eve{/b} will be fine, sweetie."
    ross "In fact, you tell her I think she looks much better in her natural blonde."
    anon f_skeptical "Y-yeah, okay, but-"
    ross "I don't know why she changed it in the first place..."
    anon "What about us kids needing to express ourselves?"
    ross "I'm sorry, {b}[firstname]{/b}... I'm not risking my job over hair dye."
    anon f_surprised "B-but-"
    ross "There are plenty of other ways she can express herself."
    ross "A nice, short skirt or a low-cut top, maybe?"
    anon f_worried "{i}*Sigh*{/i} I don't think {b}Eve{/b} is into that kind of stuff..."
    ross "Sure she is, sweetie."
    ross "She just needs someone to help build her confidence up."
    anon f_skeptical "I guess..."
    hide anon with dissolve
    return

label button_ross_grab_clay:
    scene expression player.location.background_closeup
    show player 1f at right
    show old_ross 2 at left
    with dissolve
    ross "{b}Go grab a slab of clay{/b}, {b}[firstname]{/b}, so we can get started."
    show player 2f
    show old_ross 1
    player_name "Yes, ma'am."

    return

label button_ross_find_partner:
    scene expression player.location.background_closeup
    show player 2f at right
    show old_ross 1 at left
    with dissolve
    player_name "Hey, {b}Miss Ross{/b}. You ready to get started?"
    show player 1f
    show old_ross 2
    ross "Hey there, {b}[firstname]{/b}! Just about..."
    show old_ross 11 with dissolve
    ross "I actually wanted to discuss something with you first."
    show player 2f
    show old_ross 10
    player_name "Oh?"
    show old_ross 11
    show player 1f
    ross "I think we should get you a partner for these sessions, what do you think?"
    show old_ross 10
    show player 10f
    player_name "A partner?"
    show old_ross 11
    show player 11f
    ross "Yeah, somebody to work alongside you and bounce ideas back and forth!"
    show old_ross 10
    show player 2f
    player_name "Sure, okay."
    player_name "Did you have anyone in mind?"
    show player 1f
    show old_ross 10b with dissolve
    ross "Hmm..."
    show old_ross 11 with dissolve
    ross "Well, my initial thought is {b}Eve{/b}. She's a talented artist just like yourself..."
    ross "... But I doubt she'd have time with all her musical studies."
    show old_ross 10b with dissolve
    pause
    show old_ross 11 with dissolve
    ross "Do you think {b}Mia{/b} would be interested?"
    ross "She's just such a cutie pie, isn't she?"
    show old_ross 10
    show player 2f
    player_name "Err, yeah. I suppose."
    show player 1f
    show old_ross 11
    ross "Great! Well, why don't you go talk to her?"
    ross "Tell her I said to get her cute butt in here!"
    show player 11f
    show old_ross 10
    player_name "..."

    return

label button_ross_ask_mia_partner:
    scene expression player.location.background_closeup
    show player 1f at right
    show old_ross 2 at left
    with dissolve
    ross "{b}[firstname]{/b}, you're back!"
    ross "Where's {b}Mia{/b}?"
    show player 10f
    show old_ross 1
    player_name "Oh, uhh... I haven't convinced her yet."
    show player 11f
    show old_ross 2
    ross "Well, get a move on, {b}[firstname]{/b}!"
    ross "We need her enthusiasm if we're gonna win this thing!"
    return

label button_ross_mia_is_partner:
    scene expression player.location.background_closeup
    show player 1f zorder 1 at right
    show old_ross 2 at left
    show old_mia 7 zorder 0 at Position(xpos=0.65, ypos=1.0)
    with dissolve
    ross "Hey there, cutie pie!"
    show old_ross 1
    show old_mia 56 at Position(xpos=0.635, ypos=1.0) with dissolve
    mia "... Oh, umm. H-hello."
    show old_ross 2
    show old_mia 55
    ross "I'm so glad, {b}[firstname]{/b} convinced you to join us!"
    show old_ross 1
    show old_mia 56
    mia "Hehe, yeah... He said you guys really needed my help?"
    show old_ross 2
    show old_mia 55
    ross "We surely do!"
    show old_ross 1
    show player 2f
    show old_mia 8b at Position(xpos=0.65, ypos=1.0) with dissolve
    player_name "So are we ready to start now?"
    show player 1f
    show old_ross 11 with dissolve
    ross "Yup! Why don't you both get out your art pads and have a seat opposite each other."
    show player 2f
    show old_ross 10
    player_name "Okay."
    show old_mia 8
    show player 596f with dissolve
    mia "..."
    show old_mia 12
    mia "Umm, question..."
    show old_mia 8
    show old_ross 11
    ross "Yes, dear?"
    show old_mia 12
    show old_ross 10
    mia "What if I don't have an art pad?"
    show old_mia 8
    show old_ross 25
    ross "Oh, right."
    show old_ross 25b
    ross "Well, usually I'd provide you with one of those..."
    show old_ross 25
    ross "... But I'm afraid we've exhausted our stores."
    show old_ross 24
    show player 598f
    player_name "That sucks!"
    show player 596f
    show old_mia 12b
    mia "Oh well, it's no big deal. I'm not very good at drawing anyways..."
    show old_mia 10
    mia "I'll just watch."
    show old_mia 7
    show old_ross 11
    ross "Nonsense!"
    ross "We'll get you one!"
    show old_ross 27 with dissolve
    ross "{b}[firstname]{/b}, why don't you go ask {b}Eve{/b} if we can borrow one of hers."
    show old_ross 26
    show player 598f
    player_name "... Y-yeah, okay!"
    show old_ross 27
    show player 596f
    ross "See, {b}[firstname]{/b} to the rescue!"
    show player 1f
    show old_ross 11
    with dissolve
    ross "We'll just stay here and have some girl talk."
    show old_ross 13
    ross "Right, cutie pie?"
    show old_ross 12
    show old_mia 56 at Position(xpos=0.635, ypos=1.0) with dissolve
    mia "Heh, okay..."
    show old_mia 55
    show player 2f
    player_name "Be right back."
    return

label button_ross_find_art_pad:
    scene expression player.location.background_closeup
    show old_ross 13 at left
    show old_mia 55 at Position(xpos=0.435, ypos=1.0)
    show player 1f at right
    with dissolve
    ross "... You know, {b}Mia{/b}. I used to be friends with a girl who looked just like you!"
    show old_ross 12
    show old_mia 56
    mia "Really?"
    show old_ross 13
    show old_mia 55
    ross "Absolutely! Her name was Starchild, and we used to follow our favorite band all over the country."
    show old_ross 12
    show old_mia 12b at Position(xpos=0.45, ypos=1.0) with dissolve
    mia "Well, that sounds pretty neat!"
    show old_ross 13
    show old_mia 8b
    ross "Oh, it was!"
    ross "That girl always had the best drugs!"
    show old_ross 11
    ross "... And what a kisser! She could do things with her tongue that woul-"
    show player 10f
    show old_ross 10
    show old_mia 55 at Position(xpos=0.435, ypos=1.0) with dissolve
    player_name "{i}*Ahem*{/i} Am I interrupting something?"
    show player 11f
    show old_mia 12f with dissolve
    mia "{b}[firstname]{/b}, you're back!"
    show old_mia 12bf
    mia "Thank goodness!"
    show old_mia 8bf
    show old_ross 11
    ross "Did you manage to {b}get Eve's art pad{/b}?"
    show player 10f
    show old_ross 10
    player_name "No, sorry. I'm still working on it."
    show player 11f
    show old_ross 11
    ross "Tsk, well shoo then! We're having girl talk here..."
    show old_ross 10
    show player 10f
    player_name "... A-alright. I'll be back."
    hide player with dissolve
    show old_mia 12f at Position(xpos=0.55, ypos=1.0) with dissolve

    mia "No! Wait! Hold up!"
    show old_mia 8f
    pause
    show old_ross 13 at Position(xpos=0.15, ypos=1.0) with dissolve
    ross "Now where was I?"
    show old_ross 12
    show old_mia 8b with dissolve
    mia "..."
    show old_ross 13
    ross "Oh, right! She could do things with her tongue that would make a whore blush!"
    show old_ross 12
    show old_mia 56 at Position(xpos=0.535, ypos=1.0) with dissolve
    mia "... Oh my."
    return

label button_ross_found_art_pad:
    scene expression player.location.background_closeup
    show old_ross 46 at left
    show old_mia 55 at Position(xpos=0.435, ypos=1.0)
    show player 11f zorder 1 at right
    with dissolve
    ross "... Hmm, I think my favorite one is the {b}Praia do Abricó{/b}."
    show old_ross 11 with dissolve
    ross "It's back home in Rio de Janeiro."
    show old_ross 10
    show old_mia 56
    mia "Oh, I dunno..."
    mia "... I don't think I'm brave enough for a nude beach."
    show old_ross 13
    show old_mia 55
    ross "Oh, sure you are, cutie pie!"
    ross "Nobody should be ashamed of their body. The human form is a work of art after all..."
    show old_ross 13
    ross "... Especially yours."
    ross "You're just absolutely gorgeous, {b}Mia{/b}!"
    show old_ross 12
    show old_mia 56
    mia "Wow, I... Uhh..."
    show player 10f

    player_name "{i}*Ahem*{/i}"
    show player 11f
    show old_mia 12bf with dissolve
    mia "Oh, {b}[firstname]{/b}, thank goodness you're back!"
    show old_mia 8b zorder 0 at Position(xpos=0.65, ypos=1.0) with dissolve
    show player 2f
    player_name "You guys having fun?"
    show player 1f
    show old_ross 11
    ross "We're having a blast!"
    ross "I assume you {b}got the art pad{/b}?"
    show old_ross 10
    show player 598f with dissolve
    player_name "Yup, I got it right here."
    show player 596f
    show old_ross 11 with dissolve
    ross "Good work, {b}[firstname]{/b}!"
    ross "We should get started now."
    ross "I want both of you to take a seat opposite one another."
    show old_ross 58 with dissolve
    ross "... Because today you're going to be drawing portraits of each other using pencil and paper."
    show player 598f
    show old_ross 10 with dissolve
    player_name "So you want me to draw {b}Mia{/b}?"
    show player 596f
    show old_ross 11
    ross "That's right and {b}Mia{/b}, I want you to draw {b}[firstname]{/b}."
    show old_ross 10
    show old_mia 12b
    mia "I'll try..."
    show old_ross 13
    show old_mia 8b
    ross "You're just too adorable, aren't you?"
    show old_ross 12
    show old_mia 55 at Position(xpos=0.635, ypos=1.0) with dissolve
    ross "Don't worry, there's no such thing as bad art!"
    show old_mia 56
    mia "... If you say so."
    show old_mia 55
    show old_ross 11
    ross "Now let's get started."

    scene location_school_art_cutscene06
    show text _ ("I always did enjoy art but drawing a live model was a totally different experience...") as caption
    with fade
    pause
    hide caption with dissolve
    show text _ ("... I'm glad {b}Miss Ross{/b} had chosen {b}Mia{/b} as my partner for this.") as caption with dissolve
    pause
    hide caption with dissolve
    show text _ ("She really was cute!") as caption with dissolve
    pause

    scene expression player.location.background_closeup
    show player 1 zorder 1 at left
    show old_mia 8b at right
    show old_ross 11f zorder 0 at Position(xpos=0.535, ypos=1.0)
    with fade
    ross "Well done, both of you!"
    ross "It's such a beautiful drawing, {b}[firstname]{/b}!"

    show old_ross 28f at Position(xpos=0.435, ypos=1.0) with dissolve
    ross "I'm feeling very good about our chances in this art contest..."
    ross "You should show {b}Mia{/b}."
    show old_ross 12 at Position(xpos=0.35, ypos=1.0)
    show player 560
    with dissolve

    pause
    show old_mia 69
    mia "{i}*Gasp*{/i}"
    show old_mia 10
    mia "Wow! It's so good!"
    show old_mia 7
    show old_ross 11
    ross "Isn't it?"
    show old_ross 13
    ross "It's almost as beautiful as the real thing!"
    show old_ross 13c
    ross "Don't you think, {b}[firstname]{/b}?"
    show player 561
    show old_ross 12b
    player_name "Y-yeah, almost..."

    show player 560
    show old_ross 12
    show old_mia 56 with dissolve
    mia "Aww, thanks, {b}[firstname]{/b}."
    show old_mia 55
    show old_ross 13
    ross "Alright then, let's see how you did {b}Mia{/b}?"
    show old_mia 59b with dissolve
    mia "Mmm, no. That's okay. I'd rather not."
    show old_ross 11
    show old_mia 59d
    ross "Oh, pish posh! Don't play so hard to get!"
    ross "Remember, there's no such thing as bad art..."
    show old_ross 10
    show old_mia 59e
    mia "... Okay."
    show old_mia 59c
    show old_ross 24

    ross "..."
    show old_mia 59
    mia "I told you, I'm not very good..."
    show old_mia 59c
    show old_ross 25
    ross "Well no, it's... Interesting..."
    show old_ross 11
    ross "There's definitely room for improvement."
    show player 561
    show old_ross 10
    player_name "I like it, {b}Mia{/b}!"
    show player 560
    show old_mia 57
    mia "You do?"
    show player 561
    show old_mia 58
    player_name "Yeah, it's really cute!"

    show player 560
    show old_ross 11
    ross "There, now see, {b}Mia{/b}. {b}[firstname]{/b} likes it!"
    show old_ross 10
    mia "..."
    show old_ross 11
    ross "Well, I think we had better call it there for today."
    ross "We made some really good progress, you two!"
    show old_ross 58 at Position(xpos=0.41, ypos=1.0) with dissolve
    ross "Make sure you both get lots of rest and don't forget to do those meditations I taught you!"
    show old_ross 10 at Position(xpos=0.35, ypos=1.0) with dissolve
    show player 2
    with dissolve
    player_name "Alright, I'll try, {b}Miss Ross{/b}."
    player_name "See ya, {b}Mia{/b}!"
    show player 1
    show old_mia 56 with dissolve
    mia "Bye, {b}[firstname]{/b}."
    return

label button_ross_collage:
    scene expression player.location.background_closeup
    show player 2f zorder 1 at right
    show old_mia 2f zorder 0 at Position(xpos=0.55, ypos=1.0)
    with dissolve
    player_name "You ready for another session with {b}Miss Ross{/b}?"
    show player 1f
    show old_mia 6f
    mia "Yeah, I guess..."
    show player 10f
    show old_mia 2f
    player_name "You don't seem very excited about it."
    player_name "I thought you loved art?"
    show player 11f
    show old_mia 6f
    mia "I do love art."
    mia "... And I really like watching you and {b}Miss Ross{/b} work."
    show old_mia 6bf
    mia "It's just..."
    show old_mia 6f
    mia "{b}Miss Ross{/b} makes me feel a little self-conscious."
    show player 10f
    show old_mia 2f
    player_name "She does?"
    show player 11f
    show old_mia 6f
    mia "She's being very forward with me, don't you think?"
    show player 2f
    show old_mia 2f
    player_name "Yeah, but she's like that with everyone."
    show player 1f
    show old_mia 6f
    mia "Is she?"
    mia "I dunno, she's lived such an adventurous life, and she's so full of experience..."
    show old_mia 6bf
    mia "She makes me feel so boring."
    show player 2f
    show old_mia 2f
    player_name "I don't think you're boring, {b}Mia{/b}."
    show player 1f
    show old_mia 4f
    mia "You don't?"
    show old_mia 1f
    show player 2f
    player_name "Not at all."
    player_name "I think you just need to relax and keep an open mind."
    player_name "I betcha {b}Miss Ross{/b} can teach us a lot of cool stuff!"
    show old_mia 5f
    show player 1f
    mia "..."
    show old_mia 3f
    mia "Yeah, maybe you're right, {b}[firstname]{/b}!"
    show old_mia 4f
    mia "I coul-"
    show old_mia 1f
    show player 11f
    show old_ross 11 at left with dissolve

    ross "There's my favorite students!"
    show old_mia 8b at Position(xpos=0.65, ypos=1.0) with dissolve
    ross "What are you two lovebirds talking about?"
    show old_mia 55 at Position(xpos=0.635, ypos=1.0) with dissolve
    show player 10f
    player_name "Lovebirds?"
    show old_mia 56
    show player 11f
    mia "We were just wondering what todays session would be about?"
    show old_mia 55
    show old_ross 13
    ross "Straight to business, huh?"
    ross "You little firecracker, I love it!"
    show old_ross 12
    mia "..."
    show old_ross 58 with dissolve
    ross "Today you're each going to make a collage!"
    show old_ross 10 with dissolve
    show old_mia 12b at Position(xpos=0.65, ypos=1.0) with dissolve
    mia "Collage? I don't even know what that means..."
    show old_mia 8b
    show old_ross 27 with dissolve
    ross "Oh, they are so much fun! You're going to love them {b}Mia{/b}!"
    ross "We're going to cut pictures out of magazines and glue them together to make art."
    show old_ross 26
    show player 2f
    show old_mia 7
    player_name "Sounds like fun to me."
    show player 1f
    show old_mia 10
    mia "Yeah, it really does."
    show old_mia 7
    show old_ross 11 with dissolve
    ross "Alright, well, I've got just about everything we need right here. We're just missing {b}rubber cement{/b} and {b}a big stack of magazines{/b}."
    ross "Why don't you two go find us some?"
    show old_ross 10
    show player 2f
    player_name "We can do that, right {b}Mia{/b}?"
    show player 1f
    show old_mia 10b
    mia "Absolutely. In fact, I think my dad has some rubber cement at home."
    show old_mia 10
    mia "I'll go get it!"
    hide old_mia with dissolve

    show old_ross 11
    ross "... And away she goes!"
    ross "I guess that means you're in charge of finding the {b}magazines{/b}, {b}[firstname]{/b}."
    ross "If you can find {b}three BIG stacks of magazines{/b}, I think that should be enough."
    show player 2f
    show old_ross 10
    player_name "Any idea where I could find some?"
    show player 1f
    show old_ross 10b with dissolve
    ross "Hmm..."
    show old_ross 11
    ross "... I'd start at the {b}Library{/b}. They should have a huge selection to choose from!"
    show player 2f
    show old_ross 10
    player_name "Alright, I'll go check it out."
    return

label button_ross_find_magazines:
    scene expression player.location.background_closeup
    show player 2f zorder 1 at right
    show old_ross 10 at left
    with dissolve
    player_name "Where did you say I should look again?"
    show player 1f
    show old_ross 11
    ross "For the {b}magazines{/b}?"
    ross "{b}Try the library{/b}."
    ross "And see if you can find {b}three BIG stacks of magazines{/b}, alright?"
    if M_ross.get("talked with jane"):
        hide old_ross with dissolve
        show player 10 with dissolve
        player_name "{i}*Sigh*{/i}"
        player_name "The library doesn't have any magazines though."
        if M_ross.get("magazines remaining") == 3:
            player_name "And I still need to find 3 more magazines."
        elif M_ross.get("magazines remaining") == 2:
            player_name "And I still need to find 2 more magazines."
        elif M_ross.get("magazines remaining") == 1:
            player_name "And I still need to find 1 more magazine."
        player_name "I guess I should {b}look around here at school{/b}."
    else:
        show old_ross 10
        show player 2f
        player_name "{b}Library{/b}, got it!"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
