label barn_daisy_pregnancy_anouncement_repeat:
    scene expression player.location.background_blur with None
    show player 10 at left
    show diane b_naked:
        xoffset 100
    show daisy:
        xoffset -200
    with dissolve
    player_name "Hey, I got your text."
    show player 5
    diane "Hey, {b}[firstname]{/b}."
    diane "You uhh, might want to sit down for this..."
    player_name "Hmm?"
    show player 10b
    player_name "What's going on?"
    show player 5
    diane "{b}Daisy{/b} is pregnant again."
    show player 10b
    player_name "Again?!"
    player_name "That's-"
    show player 5
    pause
    show player 30
    player_name "Are you sure?"
    show player 5
    diane "Well, the poor thing has been sick every morning for the past 3 days, and she missed her... Umm..."
    pause
    show diane f_shamed_fardown
    diane "{i}*Ahem*{/i} I'm pretty sure."
    show player 10b
    player_name "Phew, okay..."
    show player 5b
    show diane f_normal
    diane "Oh, don't you worry. Everything is going to be fine."
    diane @ f_laugh "A child is a blessing!"
    show player 10b
    player_name "How are you taking all this {b}Daisy{/b}?"
    show player 5b
    daisy "I'm gonna be a mommy again!"
    show diane f_laugh
    diane "Hehe, you certainly are sweetie."
    show diane f_smirk_fardown
    diane "C'mon, let's go and get you some food."
    diane "You're eating for two now."
    show diane f_smirk
    hide daisy with dissolve
    pause
    diane "Chin up, {b}[firstname]{/b}!"
    show player 5
    player_name "Hmm?"
    diane "You're gonna be a father again."
    diane "It's good news."
    show player 14
    player_name "Yeah, I know."
    show player 13
    show diane f_laugh
    diane "Congratulations!"
    show diane f_smirk
    show player 14
    player_name "Thanks, {b}Diane{/b}."
    hide diane with dissolve
    pause
    show player 24
    player_name "( Holy crap. )"
    player_name "( {b}Daisy{/b} is going to have another kid... )"
    player_name "{i}*Gulp*{/i} I hope I'm ready for this."
    hide player with dissolve
    return

label barn_daisy_pregnancy_seen_in_labor:
    scene expression player.location.background_blur with None
    show player 5 at left
    show diane b_naked:
        xoffset 100
    show daisy a_baby f_down:
        xoffset -200
    with dissolve
    diane "There he is!"
    pause
    show diane f_teasing_look
    show daisy f_normal
    diane "There's your daddy!"
    show diane f_normal
    show player 3 with dissolve
    player_name "{i}*Gulp*{/i}"
    diane "Come on, handsome."
    if M_daisy.pregnancy.baby_gender == "boy":
        diane "You have to meet your new son."
        show diane f_smirk_fardown
        show player 10 with dissolve
        player_name "{b}M-my son{/b}?"
    elif M_daisy.pregnancy.baby_gender == "twins":
        diane "You have to meet your children."
        show diane f_smirk_fardown
        show player 10 with dissolve
        player_name "{b}C-children{/b}?"
    else:
        diane "You have to meet your new daughter."
        show diane f_smirk_fardown
        show player 10 with dissolve
        player_name "{b}M-my daughter{/b}?"
    show player 13
    diane @ -m_talk "Mmhmmm."
    show player 426
    show daisy f_down
    with dissolve
    pause
    show player 14
    player_name "Wow..."
    if M_daisy.pregnancy.baby_gender == "boy":
        player_name "... He's so cute!"
    elif M_daisy.pregnancy.baby_gender == "twins":
        player_name "... They're so cute!"
    else:
        player_name "... She's so cute!"
    show player 426
    show diane f_laugh
    diane "Hehe, yup."
    if M_daisy.pregnancy.baby_gender == "boy":
        diane "Just like his daddy."
    elif M_daisy.pregnancy.baby_gender == "twins":
        diane "Just like their daddy."
    else:
        diane "Just like her mommy."
    show diane f_cheese
    show player 14b
    player_name "How are you feeling {b}Daisy{/b}?"
    show player 1b
    show diane f_smirk_fardown
    show daisy f_sad
    daisy "Tired."
    show diane f_normal
    if M_daisy.pregnancy.baby_gender == "boy":
        diane "She was up all night pushing this little guy out."
    elif M_daisy.pregnancy.baby_gender == "twins":
        diane "She was up all night pushing these little ones out."
    else:
        diane "She was up all night pushing this little gal out."
    diane "It took a lot out of her."
    show diane f_smirk_fardown
    pause
    show daisy f_down
    show player 10
    player_name "Everything went okay though, right?"
    show player 5
    show diane f_normal
    diane "Oh, yeah."
    diane "You'll be back on your feet in no time, won't you sweetie?"
    show diane f_smirk_fardown
    daisy "Yeah!"
    show daisy f_laugh
    if M_daisy.pregnancy.baby_gender == "twins":
        daisy "We have babies, {b}[firstname]{/b}!"
    else:
        daisy "We have a baby, {b}[firstname]{/b}!"
    show daisy f_normal
    show player 14b
    player_name "Y-yeah, I know."
    player_name "Don't worry, I'll take care of you guys."
    show player 1b
    show diane f_laugh
    diane "Aww, you're so sweet, {b}[firstname]{/b}."
    show diane f_smirk_fardown
    diane "C'mon, we should let them rest."
    diane "Say bye to daddy!"
    show diane f_normal
    pause
    show player 429
    player_name "I'll see you all soon, okay."
    show player 1b
    show daisy f_normal
    daisy "Okay, {b}[firstname]{/b}."
    hide daisy
    hide player
    hide diane
    with dissolve
    return

label barn_daisy_pregnancy_anouncement_first:
    scene expression player.location.background_blur with None
    show player 10 at left
    show diane b_naked f_sad:
        xoffset 100
    show daisy f_sad:
        xoffset -200
    with dissolve
    player_name "Hey, I got your text."
    show player 5
    diane "Hey, {b}[firstname]{/b}."
    diane "You uhh, might want to sit down for this..."
    player_name "Hmm?"
    show player 10b
    player_name "What's going on?"
    show player 5
    diane "I think {b}Daisy{/b} is pregnant."
    show player 23
    player_name "What?!"
    player_name "I didn't think-"
    player_name "I mean, are you sure?!"
    show player 5
    diane "Well, the poor thing has been sick every morning for the past 3 days, and she missed her... Umm..."
    pause
    diane "{i}*Ahem*{/i} I'm pretty sure."
    show player 10
    player_name "Wow, umm... Okay."
    player_name "I didn't think she could get pregnant."
    show player 5
    diane "Yeah, I didn't think so either..."
    show player 10
    player_name "What are we going to do?"
    show player 5
    show diane f_normal
    diane "Oh, don't you worry. Everything is going to be fine."
    show diane f_laugh
    diane "A child is a blessing!"
    show diane f_normal
    show player 10b
    player_name "How are you taking all this {b}Daisy{/b}?"
    show player 5b
    show daisy f_sad
    daisy "I..."
    pause
    daisy "I don't know..."
    daisy "Do you think I'll be a good mommy?"
    diane "Of course you will, sweetie!"
    diane "Besides, {b}[firstname]{/b} and I will be here to help you, every step of the way."
    diane "Won't we, {b}[firstname]{/b}?"
    show player 14
    player_name "Y-yeah, of course!"
    show player 13
    diane "In fact, why don't you come with me. I've got some books on the subject you can look at."
    daisy "O-okay, {b}Diane{/b}."
    hide daisy
    hide diane
    with dissolve
    pause
    show player 24
    player_name "Holy crap."
    player_name "{b}Daisy{/b} is going to have my child..."
    player_name "{i}*Gulp*{/i} I hope I'm ready for this."
    hide player with dissolve
    return

label barn_daisy_caught_breeding_aftermath:
    scene expression player.location.background_blur with None
    show player 1b at left
    show daisy f_laugh:
        xoffset -200
    show diane b_naked f_smirk:
        xoffset 80
    with dissolve
    daisy "Hi, {b}[firstname]{/b}!"
    show daisy f_normal
    show player 14b
    player_name "Hey, {b}Daisy{/b}. {b}Diane{/b}."
    show player 1
    diane "Hello."
    pause
    show diane a_nudge f_smirk_fardown with dissolve
    diane "{i}*Ahem*{/i}"
    show diane a_idle with dissolve
    daisy f_shy "S-so, {b}Diane{/b}'s been telling me all about sex..."
    show player 11
    player_name "!!!"
    daisy "... And how it's something that two consenting adults should only do when they love each other very much."
    show player 10b
    player_name "O-okay?"
    show player 5b
    diane "Aaand?"
    daisy "... And that my master was lying and taking advantage of me, which is wrong..."
    diane "That's right."
    daisy @ f_laugh "Oh!"
    daisy "... And that they're not called a weasel or a hidey-hole."
    daisy "You have a penis and I have a floogina!"
    player_name "..."
    diane "VA-gina, dear."
    show daisy f_laugh
    daisy "Oops, sorry!"
    daisy "Vagina. I have a vagina."
    show daisy f_shy
    diane "Very good, sweetie."
    show daisy f_normal:
        flip
        xoffset 200
    with dissolve
    daisy "So can {b}[firstname]{/b} and I have sex now?!"
    show player 11
    show diane f_surprised
    player_name "!!!" with hpunch
    show diane f_shamed_smile
    diane "{i}*Sigh*{/i}"
    show player 5
    show diane f_shamed_fardown
    diane "{b}Daisy{/b}, I told you why {b}[firstname]{/b} and I are having sex, didn't I?"
    daisy "Yes, because you're consenting adults that love each other very much..."
    daisy "... And it increases your milk production."
    diane "That's right, it's for my business."
    daisy @ f_laugh "I'm part of the business too!"
    diane "I know that, but-"
    daisy "... And I'm an adult and I love {b}[firstname]{/b}..."
    daisy "... And I wanna have sex too!"
    diane "{i}*Sigh*{/i}"
    diane "Well, that's between you and {b}[firstname]{/b} then."
    show daisy:
        unflip
        xoffset -200
    with dissolve
    show diane f_shamed
    show player 10
    player_name "Huh?!"
    show player 5
    pause
    show player 10
    player_name "Y-you're serious?!"
    show player 5
    show diane f_shamed_smile
    diane "She's right."
    diane "You're both adults and if you two wanna have sex, I can't stop you."
    diane "I'd rather we keep this all out in the open instead of you two doing it behind my back."
    show diane f_shamed
    show player 10
    player_name "I wasn't..."
    player_name "I mean, I wouldn't have-"
    show player 5
    show diane f_shamed_smile
    diane "It's alright, {b}[firstname]{/b}."
    diane "{b}Daisy{/b} is a sweet girl and she really likes you."
    diane "If you like her too, then there's nothing wrong with you two having sex."
    diane "Just promise me you'll be careful."
    show diane f_shamed
    show player 24
    player_name "..."
    show player 5b
    show daisy f_normal
    daisy "I'll be careful!"
    show diane f_laugh
    diane "Hehe, good girl {b}Daisy{/b}."
    show diane f_smirk
    pause
    diane "Alright, you two have a lot to talk about and I should get back to work."
    diane "Let me know if you need anything."
    show daisy f_laugh:
        flip
        xoffset 200
    with dissolve
    show diane f_smirk_fardown
    daisy "Thanks, {b}Diane{/b}!"
    show daisy f_normal
    diane "You're welcome, sweetie."
    hide diane with dissolve
    pause
    show daisy f_shy:
        unflip
        xoffset -200
    with dissolve
    daisy "Are you okay, {b}[firstname]{/b}?"
    daisy "You look funny."
    show player 10b
    player_name "I don't..."
    show player 5b
    pause
    show player 10b
    player_name "This is all really sudden."
    show player 5b
    daisy f_sad "Oh."
    daisy "You mean, you don't want to have sex with me?"
    show player 10b
    player_name "I'm not saying that, it's just... Are you sure this is what you want?"
    show player 5b
    daisy f_normal "Oh, yes!"
    daisy "You take care of me and bring me pizza and pretty flowers!"
    daisy "You're like the bestest man in the whole world!"
    daisy "I'd much rather have sex with you than with Master..."
    show player 10b
    player_name "Yeah, but you don't have to have sex with anybody, {b}Daisy{/b}..."
    show player 5b
    daisy "I want to!"
    daisy f_sexy "I think it will be fun to put your weasel in my hidey-hole!"
    player_name "..."
    daisy "Sorry, I meant your penis... In my floogina."
    show player 10b
    player_name "Vagina."
    show player 5b
    daisy f_shy "Oh, right!"
    pause
    daisy f_normal "So, do you wanna have sex?!"
    return

label barn_daisy_caught_breeding_aftermath_yes:
    show player 14b
    player_name "Alright, let's do it."
    show player 1b
    show daisy f_normal
    daisy "{i}*Gasp*{/i} Really?!"
    show daisy f_laugh
    daisy "Yay!!!"
    show daisy f_normal
    show player 14b
    player_name "C'mon, let's go to one of the milking machines."
    show player 1b
    show daisy f_laugh
    daisy "Okay!"
    hide daisy
    hide player
    with dissolve
    pause
    return

label barn_daisy_caught_breeding_aftermath_no:
    show player 10b
    player_name "{b}Daisy{/b}, I don't think this is a good idea."
    show player 5b
    show daisy f_sad
    daisy "It's not?"
    show player 10b
    player_name "We shouldn't rush into this without giving it more thought."
    show player 5b
    daisy "More thought?"
    daisy "I've been thinking about having sex with you for a long time!"
    show player 10b
    player_name "Y-you have?"
    show player 5b
    daisy "Uh huh."
    pause
    show player 10b
    player_name "Still, I think... I need some time to process all of this..."
    show player 5b
    daisy "Oh, okay."
    pause
    daisy "You'll let me know when you're ready though, right?"
    show player 10b
    player_name "Yeah, I will."
    show player 5b
    pause
    show player 10b
    player_name "Thanks for understanding, {b}Daisy{/b}."
    show player 5b
    daisy "You're welcome."
    pause
    show player 10b
    player_name "I should-"
    player_name "{i}*Ahem*{/i} I should get back to work."
    show player 5b
    daisy "Okay."
    hide player
    hide daisy
    with dissolve
    return

label barn_dialogue_daisy_caught_breeding:
    scene expression player.location.background_blur with None
    show player 12 with dissolve
    player_name "No, {b}Diane{/b} wanted some alone time with {b}Daisy{/b} to sort out that whole, \"weasel\" situation..."
    player_name "I shouldn't interfere."
    hide player with dissolve
    return

label barn_daisy_dead_flowers:
    scene expression player.location.background_blur with None
    show player 1b at left
    show daisy b_naked_behind_sad zorder 1
    with dissolve
    daisy "Oh no!!!"
    show player 5b
    player_name "Hmm?"
    daisy "No, no, no, no!!"
    show player 10b
    player_name "{b}Daisy{/b}?"
    show player 5b
    show daisy b_naked a_cover f_sad with dissolve
    daisy "{b}[firstname]{/b}, it's terrible!"
    daisy "{i}*Sniff*{/i} Something's wrong!"
    show player 10b
    player_name "Huh?"
    show player 5b
    daisy "I think they're sick!"
    show player 10b
    player_name "{b}Daisy{/b}, I don't-"
    player_name "Who's sick?"
    show player 5b
    show daisy a_vase_wilted:
        xoffset -200
    with dissolve
    daisy "My flowers!!!"
    show player 10b
    player_name "All of them?!"
    show player 5b
    daisy "{i}*Sniff*{/i} Y-yes..."
    show player 10b
    player_name "How did that happen?"
    show player 5b
    daisy "I don't know! {i}*Sniff*{/i}"
    daisy "They were pretty yesterday..."
    show player 10b
    player_name "I'm so sorry, {b}Daisy{/b}..."
    show player 5b
    show diane f_sad b_shirtless:
        xoffset 100
    with dissolve
    show player 5
    diane "Is {b}Daisy{/b} crying?!"
    show daisy:
        flip
        xoffset 300
    with dissolve
    daisy "{b}Diane{/b}, something's wrong with my pretty flowers!!"
    pause
    show diane f_shamed_fardown
    diane "Aww, sweetie..."
    diane "That's just how it goes with flowers..."
    diane "... They aren't meant to live forever."
    diane "It'll be okay."
    daisy "{i}*Sniff*{/i} But... But..."
    daisy "How do we fix them?"
    diane "I'm afraid, some things, just can't be fixed dear..."
    daisy "... No..."
    hide daisy
    hide diane
    show daisy b_naked_diane_shirtless_comfort
    show diane b_empty f_shamed_look
    with dissolve
    diane "There, there."
    diane "Shhh."
    show diane f_shamed_look_closed
    show daisy b_naked_diane_shirtless_comfort2
    daisy "{i}*Sniff*{/i} What are we gonna do?"
    show daisy b_naked_diane_shirtless_comfort
    show diane f_shamed_look
    diane "Well, why don't we add them to the compost pile out back?"
    diane "That way, they can help us make new flowers one day."
    show daisy b_naked_diane_shirtless_comfort2
    show diane f_shamed_look_closed
    daisy "R-really?"
    show daisy b_naked_diane_shirtless_comfort
    diane "Mmhmm."
    show diane f_shamed_look
    diane "C'mon, sweetie. I'll show you."
    show diane f_shamed_look_closed
    show daisy b_naked_diane_shirtless_comfort2
    daisy "{i}*Sniff*{/i} O-okay."
    hide daisy
    show diane f_shamed b_shirtless:
        flip
        xoffset 500
    with dissolve
    pause
    show diane with dissolve:
        unflip
        xoffset 0
    diane "{b}[firstname]{/b}?"
    show player 13
    player_name "Hmm?"
    diane "Why don't you {b}run over to the mall and get her some new flowers{/b}?"
    show player 10
    player_name "Right now?"
    show player 5
    diane "Yeah, it'll be a nice surprise for her."
    show player 14
    player_name "Yeah, okay."
    show player 13
    diane "Try to get her something big and colorful."
    diane @ f_laugh "{b}Sunflowers{/b} would be perfect!"
    show player 14
    player_name "Okay, I'll {b}look for sunflowers{/b}."
    show player 13
    daisy "{b}Diane{/b}?!"
    show diane:
        flip
        xoffset 500
    with dissolve
    diane "Coming, sweetie!"
    hide diane
    show diane b_shirtless:
        unflip
        xoffset 0
    with dissolve
    diane "Thanks, {b}[firstname]{/b}."
    hide diane with dissolve
    pause
    show player 4 with dissolve
    player_name "( Hmm, I think that new store {b}Cupid at the mall sells flowers{/b}. )"
    player_name "( {b}I should start there{/b}. )"
    hide player with dissolve
    return

label barn_front_daisy_pizza_craving:
    scene expression player.location.background_blur with None
    show player 684 with dissolve
    player_name "( Ugh, it's so freaking hot out today! )"
    pause
    show player 24 with dissolve
    player_name "{i}*Sigh*{/i} I should take a break for a while..."
    show player 11
    daisy "{b}Diane{/b}!"
    daisy "That tickles!!!"
    show player 30
    player_name "Hmm?"
    show player 5
    diane "Well, we want to make sure we got it all, don't we?"
    daisy "Yes..."
    show player 10
    player_name "What are they up to in there?"
    hide player with dissolve
    pause

    $ player.go_to(L_diane_barn_interior)
    scene expression player.location.background_blur with None
    show daisy b_diane_milking f_laugh with dissolve
    daisy "Hehehe!"
    diane "Heh, you have to stop squirming, sweetie."
    daisy "I can't help it!"
    show player 10 at left with dissolve
    player_name "What's going on in-"
    show player 11
    pause
    show player 29 with dissolve
    player_name "Whoa."
    show player 3
    show daisy f_normal
    daisy "H-hi, {b}[firstname]{/b}."
    show daisy b_naked:
        xoffset -200
    show diane b_naked:
        xoffset 100
    with dissolve
    diane "Hey, {b}[firstname]{/b}."
    diane "I'm just milking our new friend here."
    show player 14 with dissolve
    player_name "Y-yeah, I can see that."
    player_name "Sorry, I'll leave you two alone."
    show player 13
    show diane f_laugh
    diane "Oh, nonsense!"
    show diane f_normal
    diane "It's nothing you haven't seen before."
    show diane f_smirk_fardown
    show daisy f_shy_back
    diane "You don't mind if {b}[firstname]{/b} stays, do you sweetie?"
    show daisy f_shy_back
    daisy "No, it's okay."
    daisy f_shy "{b}[firstname]{/b} is nice, right?"
    diane "Heh, yes. {b}[firstname]{/b} is very nice."
    show diane f_smirk
    show daisy f_normal
    show player 14
    player_name "How long has this been going on?"
    show player 13
    diane "Mmm, just a couple of days."
    diane "The poor thing started acting strange and I couldn't figure out what the problem was."
    diane "It turns out her \"boobies\" were hurting."
    show diane f_cheese
    pause
    show diane f_laugh
    diane "Haha, her words, not mine."
    show diane f_smirk_fardown
    show daisy f_sad
    daisy "Well, Master used to milk me every day..."
    daisy "... But he's not around to do it anymore."
    diane "Thank goodness for that."
    diane "You're much better off without that creepy old man!"
    pause
    show daisy f_normal:
        flip
        xoffset 300
    with dissolve
    daisy "... Yeah."
    daisy "I like when {b}Diane{/b} does it better."
    show daisy f_normal
    show diane f_laugh
    diane "Heh."
    show diane f_smirk_fardown
    diane "Well, if you think I'm good at it, you should see {b}[firstname]{/b}!"
    show daisy f_shy
    daisy "Really?!"
    diane "Mmmhmm."
    show daisy:
        unflip
        xoffset -200
    with dissolve
    daisy "{b}Diane{/b} says that you milk her sometimes too?"
    show diane f_smirk
    show player 14b
    player_name "Y-yeah, sometimes..."
    show player 1b
    show daisy f_normal
    daisy "I've never met anyone else that needs to be milked like me."
    show diane f_smirk_fardown
    diane "Perhaps {b}[firstname]{/b} can tell you more about what we do here and take your mind off all the tickling, huh?"
    hide diane
    hide daisy
    show daisy b_diane_milking
    with dissolve
    daisy "Y-yeah, okay."
    show player 10
    player_name "Uhh, sure..."
    show player 14
    player_name "{i}*Ahem*{/i} You see, {b}Diane{/b} sells her milk to people who need it."
    show player 1
    show daisy f_shy
    daisy "People need it?"
    show player 14
    player_name "Yeah."
    player_name "Some of her customers drink it and others cook with it."
    player_name "Heh, I even heard some of my friends say they are mixing it into their protein shakes..."
    show player 1
    show daisy f_laugh
    daisy "Wowzers, {b}Diane{/b} must have yummy milk!"
    show daisy f_normal
    show player 14
    player_name "Yeah, it's really tasty!"
    show player 1
    show daisy f_shy_back
    daisy "{b}Diane{/b}, you should sell my milk too!"
    show daisy b_naked f_normal:
        flip
        xoffset 300
    show diane b_naked f_smirk_fardown:
        xoffset 100
    with dissolve
    daisy "Master says it's the best in the whole world!"
    diane "You'd be okay with me selling some?"
    daisy "Of course!"
    daisy "I wanna help people too!"
    show diane f_laugh
    diane "Haha, you're such a good girl, {b}Daisy{/b}."
    show diane f_smirk_fardown
    daisy "Uh huh!"
    diane "I think we're about done for today..."
    diane "Feeling better?"
    daisy "Yes, much better."
    daisy "Thank you, {b}Diane{/b}!"
    diane "No problem, sweetie."
    pause
    diane "We should probably get some food in you now, don't you think?"
    daisy @ f_laugh "{i}*Gasp*{/i} Oats?!"
    show diane f_laugh
    diane "Heh, oats again?"
    show diane f_smirk_fardown
    diane "{i}*Sigh*{/i} Don't you get tired of eating oats all the time?"
    daisy "Nope!"
    daisy "Master always feeds me oats, they're yummy!"
    diane "Okay, but your old master doesn't control what you eat anymore..."
    diane "Wouldn't you rather try something else?"
    daisy @ f_normal_smelling -m_talk "Mmm"
    daisy "I dunno..."
    daisy "What's better than oats?"
    diane "Hehe, lots of things!"
    diane "You could try some more things out of my garden?"
    daisy @ f_normal_smelling -m_talk "Hmm..."
    show daisy:
        unflip
        xoffset -200
    with dissolve
    daisy "What do you like to eat, {b}[firstname]{/b}?"
    show diane f_normal
    show player 10b
    player_name "Me?"
    show player 17
    player_name "Cheeseburgers!"
    show player 1b
    show diane f_sad
    diane "{b}[firstname]{/b}, are you crazy?!"
    show player 5
    diane "We cannot feed her a cheeseburger!!"
    show player 10
    player_name "Hmm, why not?"
    show player 5
    pause
    show player 11
    pause
    show player 29 with dissolve
    player_name "Oh, right..."
    show diane f_smirk
    player_name "... Because that's beef, and she's..."
    show player 3
    pause
    show player 14b
    player_name "Sorry."
    show player 1b
    daisy "What's a cheese burger?"
    show diane f_smirk_fardown
    diane "Never mind that, dear."
    show diane f_normal
    show player 14b
    player_name "Pizza then!"
    show player 1b
    daisy f_shy "Pizza?"
    pause
    daisy f_normal @ f_laugh "Hehe, that's a funny word!"
    show diane f_thinking
    diane "That could work, I guess..."
    show diane f_normal
    show player 13
    diane "You wanna {b}run over to Tony's Pizzeria and grab a pizza{/b} for her to try?"
    show player 14
    player_name "Yeah, I can do that."
    show player 13
    daisy "Pizza!"
    daisy @ f_laugh "Hehehe!"
    diane "Just remember she's a herbivore, okay?"
    diane "I don't know if she'd be able to handle meat."
    show player 14
    player_name "Got it!"
    player_name "One {b}veggie pizza{/b}, coming up!"
    hide player with dissolve
    show daisy:
        flip
        xoffset 300
    with dissolve
    show diane f_smirk_fardown
    daisy "PIZZA!!!"
    show diane f_laugh
    diane "Hehe!"
    hide diane
    hide daisy
    with dissolve
    return

label barn_front_daisy_picking_flowers:
    scene expression player.location.background_blur with None
    show player 14 at left
    show diane b_shirtless
    with dissolve
    player_name "Hey {b}Diane{/b}."
    show player 13
    diane "Hey there, stud."
    diane "How are you today?"
    show player 14
    player_name "I'm alright."
    player_name "What are you doing out here in the garden?"
    player_name "Shouldn't you be inside with our new friend?"
    show player 13
    diane "Actually, it was her idea."
    show player 5
    player_name "Hmm?"
    diane "See for yourself."
    show player 5f with dissolve
    pause
    scene expression "backgrounds/location_diane_garden_cutscene11.jpg" with fade
    player_name "Wow, look at her..."
    player_name "... She's smiling!"
    diane "I know, isn't it adorable?!"
    diane "You should have seen how timid she was when she asked to leave the barn."
    diane "It about broke my heart."
    player_name "I can imagine."
    player_name "Why is she naked?"
    diane "Well, I gave her some clothes, but she said she didn't like wearing them."
    diane "I didn't wanna force her."
    scene expression player.location.background_blur with None
    show player 10 at left
    show diane b_shirtless:
        xoffset 100
    with dissolve
    player_name "So..."
    player_name "What are you gonna do with her?"
    show player 5
    diane "Hmm?"
    show player 10
    player_name "I mean, shouldn't we call somebody or something?"
    show player 5
    diane "Heh, who in the world would we call for something like this?"
    show player 10
    player_name "I dunno? Animal control?"
    show player 5
    diane "No, we'll let her decide what she wants to do."
    diane "For now, it's probably best if she stays here in the barn."
    diane "Who knows what would happen if anybody saw her."
    show player 10
    player_name "Y-yeah, I guess that makes sense."
    show player 5
    cow "{b}Diane{/b}!"
    cow "{b}Diane{/b} did you see all the flowers?!"
    show daisy a_bouquet f_down:
        xoffset -200
    with dissolve
    show player 1b
    cow "They're so pret-"
    show daisy f_scared
    pause
    show daisy f_sad
    show player 5b
    cow "Eep!"
    show diane f_shamed_smile
    diane "Shh, it's alright sweetie."
    diane "Remember, what we talked about?"
    diane "This is {b}[firstname]{/b} and he's a nice man."
    diane "He won't hurt you."
    show diane f_shamed
    cow @ -m_talk "..."
    show daisy f_shy_back
    show diane f_shamed_smile
    diane "You're not going to hurt her right, {b}[firstname]{/b}?"
    show diane f_shamed
    show player 29 with dissolve
    show daisy f_sad
    player_name "Not at all."
    show player 4
    cow @ -m_talk "..."
    show player 14b with dissolve
    player_name "I like your flowers."
    show player 1b
    cow "Y-you do?"
    show diane f_normal
    show player 14b
    player_name "Yes, they're very pretty."
    show player 1b
    pause
    cow "{b}Diane{/b} says you're the one who woke me up."
    show player 14b
    player_name "Oh, umm... Yeah, I suppose I was."
    show player 1b
    show daisy f_sad_closed
    cow "T-thank you, for that."
    show daisy f_shy
    show player 17
    player_name "Heh, you don't have to thank me."
    show player 14b
    player_name "I'm just happy you're here now."
    show player 1b
    cow "Me too."
    show daisy f_normal:
        flip
        xoffset 200
    with dissolve
    cow "C-can I keep these, {b}Diane{/b}?"
    show player 13
    diane "You wanna keep the flowers?"
    show daisy f_shy
    cow "If that's okay?"
    show diane f_laugh
    diane "Heh, well, of course it's okay, sweetie!"
    show diane f_normal
    diane "Let's go and put them in some water, so they have something to drink, okay?"
    show daisy f_laugh
    cow "Y-yeah, okay!"
    show daisy f_normal
    diane "Follow me, both of you."
    hide diane with dissolve
    show player 1b
    pause
    show daisy f_shy:
        unflip
        xoffset -200
    with dissolve
    show player 18
    pause
    show daisy f_sad:
        flip
        xoffset 200
    with dissolve
    cow "W-wait for me!"
    hide daisy with dissolve
    show player 11
    pause
    show player 5
    player_name "( Well, at least she isn't recoiling in fear anymore. )"
    player_name "( That's a step in the right direction. )"

    $ player.go_to(L_diane_barn_interior)
    scene expression player.location.background_blur with None
    show player 1 at left
    show diane b_shirtless f_smirk_fardown:
        xoffset 100
    show daisy a_bouquet f_shy:
        flip
        xoffset 250
    with dissolve
    cow "S-so they drink the water?"
    diane "Mmhmm, they need water to produce food for themselves."
    cow "... But where is the mouth on a flower?"
    diane "Hehe, no dear."
    diane "They drink water using their roots."
    diane "It flows right up the stem and into the petals."
    show daisy f_normal
    cow "Really?!"
    show diane a_vase1 with dissolve
    diane "Lemme show you."
    pause
    show daisy a_idle
    show diane f_laugh a_vase2
    with dissolve
    diane "Just like that, see?"
    show diane f_smirk_fardown a_idle
    show daisy a_vase
    with dissolve
    diane "Now, you check in on them throughout the day and you'll see the water level goes down as they drink."
    cow "O-okay, {b}Diane{/b}."
    show diane f_smirk
    show player 14b
    player_name "You gotta make sure they get sunlight too."
    show player 1b
    show daisy f_shy:
        unflip
        xoffset -200
    with dissolve
    cow "Sunlight?"
    show diane f_smirk_fardown
    diane "He's right."
    show daisy:
        flip
        xoffset 250
    with dissolve
    diane "Flowers need sunlight too, otherwise, they'll wilt and die."
    show daisy f_normal
    cow "O-okay."
    cow "Will you show me how to catch sunlight?"
    show player 17
    player_name "Haha!"
    show player 1b
    show diane f_laugh
    show daisy f_sad
    diane "You don't catch it, sweetie."
    show diane f_smirk_fardown
    diane "All you need to do is place them in a spot where they can see the sun for a few hours a day."
    show daisy f_normal
    cow "Oh, I can do that!"
    show daisy f_shy:
        unflip
        xoffset -200
    with dissolve
    cow "T-thanks, {b}[firstname]{/b}!"
    show diane f_smirk
    show player 14b
    player_name "You're welcome, eh..."
    player_name "What do I call you?"
    show player 1b
    cow @ -m_talk "Hmm?"
    show player 14b
    player_name "Do you have a name?"
    show player 1b
    cow @ f_sad_closed -m_talk "Umm..."
    cow "{b}Diane{/b} calls me sweetie?"
    show diane f_normal
    diane "Hehe, that's more of a term of endearment then a real name, dear."
    cow "Oh, I umm..."
    show player 10b
    player_name "Didn't your... Uhh, master give you a name?"
    show player 433
    cow "He called me little pet..."
    cow "... Or sometimes..."
    cow f_sad @ f_sad_closed "N-naughty girl."
    show diane f_laugh
    diane "Well, those won't do!"
    show diane f_normal
    show player 10b
    player_name "Definitely not."
    show player 5b
    show daisy f_shy
    pause
    show player 14b
    player_name "You should pick your own name."
    show player 1b
    cow "I can pick it?"
    diane "That's a great idea, {b}[firstname]{/b}!"
    cow "B-but, I don't know any names..."
    show player 14b
    player_name "That's alright, we'll help you!"
    show player 1b
    cow "O-okay."
    diane "Dorothy!"
    show daisy f_scared
    cow @ -m_talk "Mmm..."
    show player 10
    player_name "Bessie?"
    show player 5
    show diane f_shamed_smile
    show daisy f_shy_back
    diane "Eww, no."
    show diane f_normal
    diane "How about Molly?"
    show daisy f_shy
    cow @ -m_talk "Mmm..."
    show player 17
    player_name "Clarabelle!"
    show player 13
    show daisy f_down
    show diane f_laugh
    diane "Hah, why do you keep saying cow names?"
    show diane f_normal
    show player 14
    player_name "Umm, because she's a cow girl?"
    show player 13
    show diane f_smirk
    diane "Yeah, but she's definitely more girl than cow!"
    show player 14
    player_name "C'mon, it's not like I'm trying to name her Buttercup or something..."
    show player 1b
    cow "What is this called?"
    show diane f_normal
    diane "Hmm?"
    show daisy f_shy a_flower with dissolve
    cow "The flower, what is it called?"
    show diane f_smirk_fardown
    diane "That flower is called {b}Daisy{/b}."
    show daisy f_down
    cow "{b}Daisy{/b}..."
    show daisy f_laugh
    cow "I like that!"
    show daisy f_normal
    cow "Can I be {b}Daisy{/b}?"
    diane "Hehe, of course sweetie."
    show player 17
    player_name "That's a beautiful name and it suits you!"
    show player 1b
    cow "It does?"
    show diane f_normal
    diane "I agree."
    show diane f_smirk_fardown
    show daisy f_laugh:
        flip
        xoffset 250
    with dissolve
    cow "O-okay!"
    show daisy f_normal
    diane "So it's decided then."
    diane "Your name is {b}Daisy{/b}."
    show daisy f_laugh:
        unflip
        xoffset -200
    with dissolve
    daisy "My name is {b}Daisy{/b}."
    show daisy f_normal
    show player 14b
    player_name "Nice to meet you, {b}Daisy{/b}!"
    show player 1b
    daisy @ f_laugh "Hehe!"
    show daisy a_idle with dissolve
    daisy "Nice to meet you, {b}[firstname]{/b}!"
    show diane f_normal
    diane "Aww, my heart could just melt right now."
    show diane f_smirk_fardown
    show daisy f_sad:
        flip
        xoffset 250
    with dissolve
    daisy "{i}*Gasp*{/i} They can do that?!"
    show player 17
    player_name "Pfft, hahaha!"
    show player 1b
    diane "Heh, no sweetie."
    show daisy f_normal
    diane "That's just an expression."
    diane "It means I'm really happy."
    daisy "Oh."
    show daisy f_laugh a_up with dissolve
    daisy "Then, my heart could melt too!"
    show daisy f_normal a_idle with dissolve
    show player 17
    show diane f_laugh
    diane "Hahaha!"
    player_name "Hahaha!"
    show player 1b
    pause
    show diane f_smirk_fardown
    diane "Alright, well..."
    show diane f_smirk
    diane "{b}[firstname]{/b} and I should really get some work done before we run out of daylight."
    show diane f_smirk_fardown
    daisy "Oh."
    diane "You just take care of your flowers for now and let us know if you need anything, okay?"
    daisy "Y-yeah."
    show diane f_normal
    diane "Alright, c'mon {b}[firstname]{/b}."
    hide diane with dissolve
    show player 14b
    player_name "Goodbye, {b}Daisy{/b}."
    show player 1b
    show daisy f_laugh:
        unflip
        xoffset -200
    with dissolve
    daisy "Bye!"
    hide player
    hide daisy
    with dissolve
    return

label barn_daisy_awakened_statue:
    scene expression player.location.background_blur with None
    show diane b_shirtless f_shamed_fardown a_blanket:
        xoffset 100
    show daisy b_naked_shy f_sad:
        flip
        xoffset 200
    with dissolve
    diane "Here you go, sweetie."
    hide diane
    hide daisy
    show daisy b_naked_blanket_cover1 f_shy_back zorder 0
    show diane f_down_front b_empty zorder 1
    with dissolve
    pause
    show daisy b_naked_blanket_cover2
    cow "Uhh, t-thank you."
    show daisy b_naked_shy a_blanket f_sad zorder 2:
        flip
        xoffset 200
    hide diane
    show diane b_shirtless f_shamed_fardown
    with dissolve
    diane "You're welcome."
    show player 5 at left with dissolve
    pause
    diane "Now tell me about how you ended up in my garden, dear."
    show player 5b
    cow "I..."
    cow "I'm not sure."
    cow "Master was worried about something and said I had to go back to sleep."
    pause
    cow "I begged him not to!"
    cow "I hate it when he makes me sleep."
    diane "I'm not sure I understand..."
    show diane f_shamed
    show player 10
    player_name "He turned her into a statue."
    show player 5b
    show daisy b_jump_scared
    cow "EEEEP!" with hpunch
    show diane b_empty f_thinking_back zorder 1:
        xoffset -98
    show daisy b_naked_cower f_sad zorder 0:
        unflip
        xoffset 57
    with dissolve
    pause
    show diane f_shamed
    diane "What?"
    show player 10
    player_name "{b}Jebadiah Delmont{/b} was supposedly some kind of hillbilly wizard."
    player_name "I think he must have been keeping her a secret by turning her into a statue."
    player_name "That way nobody would see her."
    show player 5
    show diane f_smirk
    diane "Hillbilly wizard?!"
    diane "That's silly!"
    show player 10
    player_name "I know, but-"
    show player 5
    show diane f_laugh
    diane "Hahaha, you can't be serious!"
    show diane f_smirk
    show player 12
    player_name "I didn't believe it either but... I mean..."
    show diane f_thinking
    show player 469 with dissolve
    player_name "How else do you explain her?"
    show player 5b with dissolve
    show daisy f_sad
    cow "Please, I didn't mean to-!"
    show daisy b_naked_shy a_cover
    show diane b_shirtless f_shamed_fardown:
        flip
        xoffset 250
    with dissolve
    show player 5
    diane "Aww, sweetie..."
    diane "Nobody is gonna hurt you, okay?"
    diane "{b}[firstname]{/b} here is the nicest guy you'll ever meet."
    show diane f_shamed_fardown
    pause
    show diane f_shamed_smile:
        unflip
        xoffset -200
    with dissolve
    diane "I think she's a little frightened of you, {b}[firstname]{/b}..."
    show diane f_shamed
    pause
    show diane f_shamed_smile
    diane "Why don't you head on home for the day and give me some time to calm her down, okay?"
    show diane f_shamed
    show player 10
    player_name "Uhh, yeah. Okay."
    player_name "If you're sure you'll be alright?"
    show player 5
    show diane f_shamed_smile
    diane "Oh, I'll be fine."
    diane "Go on, {b}we can talk about this later{/b}, okay?"
    show diane f_shamed
    hide player with dissolve
    return

label barn_player_completed_mysterious_statue:
    scene expression player.location.background_blur with None
    show diane b_naked
    show player 13 at left
    with dissolve
    diane "Hey, {b}[firstname]{/b}."
    diane "Ready to get to work?"
    show player 14
    player_name "Actually, I wanted to show you something."
    show player 13
    diane "Oh?"
    show player 14
    player_name "You remember that broken statue {b}Richard{/b} found buried under your house?"
    show player 13
    diane "Yeah, with those creepy legs, right?"
    show player 17
    player_name "Heh, yeah..."
    show player 14
    player_name "Well, I think I found all the pieces."
    show player 13
    diane "Really?"
    show player 14
    player_name "Check it out."
    show player 239_240 with dissolve
    pause
    show player 717 with dissolve
    show diane f_smirk_fardown
    diane "Oh, wow!"
    diane "It's a woman!"
    show player 717b
    player_name "Yeah, with really weird legs..."
    player_name "... And horns."
    show player 717
    diane "Aww, look at her cute little ears!"
    diane "She reminds me of those silly goat men in the old myths!"
    diane "You know, the ones with the pan flutes?"
    show player 717b
    player_name "Satyrs."
    show player 717
    show diane f_laugh
    diane "Is that what they were called?"
    show diane f_normal
    player_name "Mmhmmm."
    diane "She's so cool!"
    show diane f_smirk_fardown
    pause
    diane "I wonder why she's holding a bucket?"
    show player 717b
    player_name "I think it's a milk pail."
    show player 717
    show diane f_normal
    diane "What makes you think that?"
    show player 717b
    player_name "I dunno, just a feeling, I guess..."
    show player 717
    diane "So, she's like a little milk maid?"
    show player 717b
    player_name "Hehe, yeah."
    player_name "A {i}cow girl{/i} milk maid."
    show player 717
    show diane f_laugh
    diane "Oh my gosh, I love it!"
    show diane f_normal
    show player 717b
    player_name "Hehe, I thought you might."
    show player 717c
    pause
    show player 717b
    player_name "Why don't you keep it?"
    show player 717
    show diane f_smirk_fardown
    diane "Really?"
    show player 717b
    player_name "Yeah."
    player_name "I don't have anywhere to put it at my house."
    show player 717
    show diane f_thinking
    diane "Hmm."
    show diane f_normal
    diane "It would look great in my garden, don't you think?"
    show player 717b
    player_name "Definitely!"
    show player 13
    show diane a_statue_full f_down_front
    with dissolve
    pause
    show diane f_reading_intrigued
    diane "I can't believe this thing turned out to be such a beautiful creature!"
    pause
    show diane f_laugh
    diane "Thanks, {b}[firstname]{/b}!"
    show diane f_normal
    show player 14
    player_name "No problem!"
    show player 13
    diane "I'm gonna go and find a place for it {b}out in the garden{/b}, right now!"
    hide diane with dissolve
    pause
    show player 18
    player_name "( Well, that certainly made {b}Diane{/b} happy. )"
    show player 4 with dissolve
    player_name "( I wonder if {b}Clyde{/b}'s grandfather made it? )"
    player_name "( ... And why? )"
    pause
    show player 34 with dissolve
    player_name "( Hmm, maybe {b}I should take a closer look at that statue{/b} sometime... )"
    hide player with dissolve
    return

label barn_diane_return_outfit_package:
    scene expression player.location.background_blur
    show player 14 at left
    show diane b_shirtless
    with dissolve
    player_name "Hey {b}Diane{/b}, I'm back!"
    show player 13
    diane "Gosh, you were gone quite a while..."
    diane "... Was there any trouble?"
    show player 14
    player_name "Heh, yeah... I ran into {b}Veronica{/b} again."
    show player 13
    show diane f_laugh
    diane "Again?!"
    show diane f_normal
    diane "Is that girl stalking you or something?"
    show player 10
    player_name "N-no, I don't think so."
    player_name "She was at {b}Pink{/b}..."
    show player 13
    show diane f_smirk
    diane "Oh, was she shopping for something naughty?"
    show player 14
    player_name "Eh, she was in the back room, actually..."
    player_name "... Blowing off steam."
    show player 13
    show diane f_shamed_smile
    diane "Oh, goodness..."
    diane "... The poor dear must really be stressed out."
    show diane f_shamed
    show player 14
    player_name "N-no, she seemed quite... relaxed, last I saw her..."
    player_name "... {i}*Ahem*{/i} But you should probably still call."
    show player 13
    show diane f_normal
    diane "I'll do that."
    pause
    diane "But in the meantime, did you get the package?"
    show player 17
    player_name "I did."
    show player 239_240 with dissolve
    pause
    show player 170 with dissolve
    player_name "Are you going to tell me what's inside now?"
    show player 13
    show diane f_laugh a_box
    with dissolve
    diane "Don't worry, you'll find out soon."
    show diane f_smirk
    diane "This is so exciting!"
    show player 29 with dissolve
    player_name "A-are we really gonna have sex, {b}Diane{/b}?"
    show player 3
    diane "Oh, you better believe it!"
    diane "I just need to get everything ready."
    diane "Would you mind stepping outside for a moment?"
    show player 29
    player_name "O-okay, sure."
    hide player with dissolve
    scene expression "backgrounds/location_barn_garden_day_blur.jpg"
    show player 18 with dissolve
    player_name "( I can't believe this is really about to happen... )"
    player_name "( ... I'm gonna have sex with {b}Diane{/b}! )"
    show player 13
    diane "Okay, {b}[firstname]{/b}!"
    diane "I'm ready!"
    show player 14
    player_name "C-coming!"
    show player 33
    player_name "( Phew. Alright, {b}[firstname]{/b}! This is it! )"
    hide player with dissolve
    scene expression "backgrounds/location_barn_day_blur.jpg"
    show player 10f with dissolve
    player_name "{b}D-diane{/b}?"
    show player 13f
    $ M_diane.outfit.set_default_outfit_schedule([["cow","cow","nightgown","nightgown"]])
    show diane f_smirk b_naked
    diane "I'm here."
    show player 11 at left
    player_name "!!!" with hpunch
    show player 23
    player_name "..."
    diane "Well, what do you think?"
    show player 428
    show diane a_check f_smirk_down with dissolve
    pause
    show player 426
    show diane a_idle with dissolve
    show player 429
    player_name "Y-you look..."
    show player 29 with dissolve
    show diane f_cheese
    player_name "... Wow!"
    show player 3
    show diane f_smirk
    diane "Is it too much?"
    show player 12 with dissolve
    player_name "NO!"
    show player 26
    player_name "It's really, really sexy!"
    show player 426
    diane "You think so?!"
    player_name "I do!"
    show player 26
    show player 426
    diane "Oh, good!"
    diane "I was worried you'd find it silly."
    show player 29 with dissolve
    player_name "So, how do you wanna-"
    hide player
    show diane b_kiss_naked:
        xoffset -172
    with dissolve
    player_name "!!!"
    pause
    show diane b_pull_mc_naked with dissolve
    diane "Mmm, I can't wait another second!"
    diane "We'll use the milking station..."
    diane "... It's perfect!"
    pause 
    hide diane with dissolve
    scene expression "backgrounds/location_barn_sex_back_day.jpg"
    show diane_sex_breed pre_talk
    show diane_sex_breed_mc
    with dissolve
    diane "Give it to me, stud!"
    diane "I want you to breed me like an animal!"
    player_name "O-okay..."
    hide diane_sex_breed_mc
    show diane_sex_breed insert_and_pullout
    with dissolve
    pause
    show diane_sex_breed creampie_pullout with dissolve
    pause 1
    show diane_sex_breed creampie
    diane "Oh my god!" with hpunch
    return

label barn_diane_outfit_package:
    scene expression player.location.background_blur
    show player 29 at left
    show diane b_shirtless f_smirk
    with dissolve
    player_name "H-hey, {b}Diane{/b}."
    show player 3
    diane "Hi, handsome."
    diane "You look anxious to get started!"
    show player 29
    player_name "Heh, y-yeah."
    show player 3
    diane "Mmm, me too..."
    diane "... But there's one last thing I want you to do for me."
    show player 14 with dissolve
    player_name "A-anything!"
    show player 13
    diane "I need you to go and pick up a special package at the mall for me."
    show player 14
    player_name "I can do that!"
    show player 14f with dissolve
    player_name "I'll be back before you-"
    show diane f_laugh
    show player 11 with dissolve
    diane "Hold on just a second!"
    show player 13
    show diane f_smirk
    diane "I haven't even told you what store that package is in!"
    show player 14
    player_name "S-sorry."
    show player 13
    show diane f_laugh
    diane "Haha, it's alright."
    show diane f_smirk
    diane "You'll need to {b}look around on the second floor for a store called Pink{/b}."
    show player 17
    player_name "Pink, got it!"
    show player 13
    diane "Tell the lady at the front desk that you're there to collect a package under the name {b}Diane{/b}."
    show diane f_normal
    diane "... And don't look inside!"
    show player 14
    player_name "O-okay."
    show player 13
    diane "It's very important that you don't look inside the package, {b}[firstname]{/b}!"
    show diane f_smirk
    diane "I don't want you to spoil the surprise."
    show player 14
    player_name "I promise I won't look."
    show player 13
    diane "Good boy."
    hide player
    show diane b_kiss_shirtless
    with dissolve
    pause
    show player 13 at left
    show diane b_shirtless
    with dissolve
    diane "Hurry back to me, stud."
    show player 14
    player_name "Yes, ma'am!"
    hide player
    hide diane
    with dissolve
    return

label barn_diane_barn_checkup:
    scene expression player.location.background_blur with None
    show player 14 at left
    show diane b_casual
    with dissolve
    player_name "Hey, {b}Diane{/b}!"
    player_name "I'm ready to-"
    show player 11
    pause
    show player 14
    player_name "Where's your overalls?"
    show player 13
    diane "Hey, {b}[firstname]{/b}."
    diane "I was just about to walk out the door."
    show player 10
    player_name "Oh?"
    player_name "Where are you going?"
    show player 5
    diane "I made an appointment to see a doctor this morning."
    diane "If we're gonna... You know."
    show diane f_wink
    pause
    show diane f_normal
    diane "I wanna get checked out and make sure everything's in tip-top shape."
    show player 14
    player_name "Ah, I see."
    player_name "Well, can I come with you?"
    show player 13
    diane "You wanna come with me to see the doctor?"
    show player 17
    player_name "Sure!"
    show player 13
    diane "Alright."
    diane "I would definitely appreciate the company."
    show diane f_laugh
    diane "Doctors kinda freak me out."
    show diane f_normal
    show player 14
    player_name "Hehe, really?"
    show player 13
    diane "Yeah."
    diane "All that poking and prodding, you know?"
    show player 14
    player_name "Hah, yeah. I know what you mean."
    show player 13
    diane "Well, come on then, stud."
    diane "Let's get moving!"
    show player 14
    player_name "Y-yes, ma'am!"
    hide player
    hide diane
    with dissolve
    return

label barn_diane_return_production_book:
    scene expression player.location.background_blur with None
    show diane b_shirtless
    show player 13 at left
    with dissolve
    diane "Finally, you're back!"
    diane "I was starting to think you got lost or something."
    show player 14
    player_name "Yeah, sorry."
    player_name "I stopped off at the library."
    show player 13
    diane "Oh?"
    show player 14
    player_name "Yeah, I ran into {b}Veronica{/b} at Consum-R, and we started talking."
    player_name "She says hi by the way."
    show player 13
    show diane f_laugh
    diane "Oh, I love her! She's such a sweetie!"
    show diane f_normal
    show player 14
    player_name "I asked her about increasing milk production."
    show player 11
    show diane f_sad
    diane "WHAT?!" with hpunch
    show diane f_scared
    pause
    show diane f_sad
    diane "You didn't tell her I'm milking myself, did you?!"
    show player 10
    player_name "N-no, of course not."
    show player 5
    show diane f_lookup
    diane "Phew! I was really worried there for a sec!"
    show diane f_normal
    show player 10
    player_name "There's no need to worry."
    player_name "She was asking how the business was going, and she was very pushy..."
    player_name "She wants to work for you, you know?"
    show player 5
    diane "Yeah, I know."
    show player 10
    player_name "She seems pretty knowledgeable."
    show player 5
    diane "She is!"
    diane "Her parents owned a huge dairy farm out west, and she grew up working it."
    show player 12
    player_name "So when I said you were looking to increase milk production, she assumed I meant cows."
    show player 13
    diane "Oh, good."
    diane "I'm not ready to tell her yet."
    show player 14
    player_name "Anyways, she sent me down a path to find this."
    show player 239_240 with dissolve
    pause
    show player 369 with dissolve
    player_name "I hope it helps..."
    show player 13
    show diane a_book_cover f_reading_intrigued
    with dissolve
    diane "Hmm, {i}Breeder's Guide{/i}?"
    show diane f_normal
    show player 14
    player_name "Yeah, it turns out, there's a fairly easy answer to your milk production problems..."
    show player 13
    show diane a_book f_down_front with dissolve
    pause
    show diane f_surprised_down
    diane "!!!" with hpunch
    diane "I..."
    show diane f_reading_intrigued
    diane "This is-"
    diane "I mean... I can't-"
    show diane f_laugh
    diane "Hahaha!"
    show diane f_normal
    diane "Could you imagine me pregnant?"
    show player 14
    player_name "Sure, why not?"
    show player 13
    show diane f_thinking
    diane @ -m_talk "..."
    show diane f_laugh
    diane "Nobody would want to have a baby with me!"
    show diane f_normal
    show player 14
    player_name "I don't know about that..."
    player_name "You're beautiful, and smart, and driven, and so much fun to be around!"
    player_name "I bet, there are tons of guys out there who would be thrilled to have a baby with you, {b}Diane{/b}."
    show player 13
    show diane f_shamed_smile
    diane "... Yeah, right."
    show diane f_shamed
    show player 14
    player_name "I mean, I would."
    show player 13
    show diane f_laugh
    diane "Haha, now you're just being ridiculous..."
    show diane f_shamed
    show player 12
    player_name "Hmm?"
    show player 14
    player_name "I'm serious."
    show player 13
    show diane f_shamed_smile
    diane "Look, I know we have a little fun sometimes, but we can't do that!"
    show diane f_shamed
    show player 10
    player_name "Why not?"
    show player 5
    show diane f_shamed_smile
    diane "It isn't right!"
    show diane f_shamed_smile_back
    diane "... And what would {b}[deb_name]{/b} say?!"
    diane "She'd probably never talk to me again!"
    show diane f_shamed
    show player 14
    player_name "Oh, she wouldn't do that."
    player_name "You're like, her favorite person in the entire world, {b}Diane{/b}."
    show player 13
    show diane f_shamed_smile
    diane "You really think it's a good idea for you and I to have a baby?!"
    show diane f_shamed
    show player 14
    player_name "Well, I dunno... Maybe?"
    show player 13
    show diane f_shamed_smile_back
    diane "Tch, I don't think you've really thought this through..."
    show diane f_shamed
    show player 12
    player_name "I just want to help you, {b}Diane{/b}!"
    show player 5
    show diane f_shamed_smile
    diane "Oh, stop it!"
    show diane f_shamed
    player_name "..."
    show diane f_shamed_smile
    diane "I appreciate what you're saying {b}[firstname]{/b}, but it's just out of the question, alright?"
    show diane f_shamed
    show player 24
    player_name "{i}*Sigh*{/i} If you say so..."
    show diane f_shamed_smile
    diane "Now, why don't you go tend to the garden while I finish up in here."
    show diane f_shamed
    show player 25
    player_name "Alright."
    hide player with dissolve
    pause
    show diane f_down_front
    pause
    diane @ -m_talk "( Oh my... )"
    diane @ -m_talk "( Just imagine being bred like an animal! )"
    diane @ -m_talk "( Mmm, it's so hot! )"
    show diane f_reading_blushing
    diane @ -m_talk "( I can't believe {b}[firstname]{/b} really wants to do that with me! )"
    show diane f_reading_lip_bite
    diane @ -m_talk "( ... Maybe... )"
    pause
    show diane a_book_close f_explain with dissolve
    diane @ -m_talk "( No! Stop it, {b}Diane{/b}! )"
    diane @ -m_talk "( Get those naughty thoughts out of your head right now! )"
    show diane a_book_throw with dissolve
    diane @ -m_talk "( Even I'm not perverted enough to do something like that! )"
    show diane a_idle with dissolve
    pause
    show diane f_smirk
    diane "Phew, I need some air..."
    hide diane with dissolve
    return


label barn_building_inform_carpenter:
    scene expression player.location.background_blur with None
    show player 13 at left
    show diane b_casual a_bag f_laugh
    with dissolve
    diane "{b}[firstname]{/b}, there you are!"
    show diane f_normal
    diane "I was just about to head to your house."
    show player 14
    player_name "Wow, he's already started building!"
    show player 13
    show diane f_laugh
    diane "Yup!"
    diane "Isn't it exciting!"
    show diane f_cheese
    show player 14
    player_name "Yeah, it really is."
    player_name "Did he give you a time frame for when he expects to complete it?"
    show player 13
    show diane f_normal
    diane "Hmm, not exactly, but he'll call when it's ready."
    hide player
    show diane b_casual_bag_hug f_laugh:
        xoffset -414
    with dissolve
    diane "C'mon, roomie."
    diane "We gotta get home before {b}[deb_name]{/b} starts worrying."
    show player 14 at left
    hide diane
    show diane b_casual a_bag
    with dissolve
    player_name "Heh, yes ma'am."
    hide player
    hide diane
    with dissolve
    return

label barn_diane_check_barn_out:
    scene expression L_diane_barn_interior.background_blur
    show diane b_shirtless:
        flip
        xoffset 100
    show richard
    show player 13 at left
    with dissolve
    richard "Hey, you got here quick."
    show player 17
    player_name "Heh, I could barely keep up with her."
    show player 13
    show diane f_laugh
    diane "I'm excited!"
    show diane f_cheese
    show richard f_confused
    richard "Hah, I guess you're ready for the tour then?"
    show diane f_normal
    diane "Yes, please!"
    show richard f_normal
    richard "Alright then, follow me."
    hide richard
    hide diane
    hide player
    with dissolve
    scene expression L_diane_barn.background with fade
    richard "I did everything exactly to your specifications."
    richard "All the doors are thick and sturdy with custom-built locking mechanisms, so you shouldn't have to worry about anyone breaking in."
    diane "Niiice!"
    scene expression L_diane_barn_garden.background with fade
    richard "I made sure to keep the grunts out of your garden so everything there should be more or less the way you left it."
    richard "... And the hay guys had some excess they didn't use, so I told them to stack it under the awning out back."
    diane "That's perfect!"
    scene expression L_diane_barn_interior.background with fade
    player_name "Whoa!"
    diane "Hehe!"
    richard "Again, everything was done to your specifications."
    richard "You've got plenty of extra storage space on the second floor and room to expand, should you ever decide to."
    diane "It's so beautiful!"
    player_name "What are those machines for?!"
    scene expression L_diane_barn_interior.background_blur
    show diane b_shirtless:
        flip
        xoffset 100
    show richard f_confused
    show player 13 at left
    with dissolve
    richard "Yeah, about those..."
    richard "A couple fellas showed up with them about three days ago, saying you ordered them."
    richard "All the paperwork checked out, and they did all the installation."
    richard "I still don't have any idea what they do..."
    show diane f_laugh
    diane "Hehe, those are, uhh... It's a secret of the trade!"
    show diane f_normal
    richard "Hmmph."
    show richard f_normal
    richard "Fair enough."
    pause
    richard "Welp, I think that about covers it."
    diane "Thanks so much, {b}Richard{/b}."
    diane "This all looks even better than I imagined it."
    richard "Well, I'd appreciate it if you could recommend me to anyone you know who's needing work done."
    diane "I certainly will!"
    richard "Alright, then I'll leave you to it."
    richard "Oh, wait!"
    richard "I nearly forgot."
    diane "Hmm?"
    show richard a_statue with dissolve
    show diane f_down_front
    show player 433
    richard "The hay delivery guys found this half buried in the corner the other day."
    show richard f_confused
    richard "It's the damnedest thing..."
    show player 434
    richard "I dunno how I missed it when I was working on the foundation."
    show diane a_statue
    show richard a_idle
    with dissolve
    richard "You know anything about it?"
    show diane f_normal
    diane "I've never seen it before..."
    diane "... Looks like some sort of statue or something."
    richard "Yeah, that's what I was thinking."
    show player 14
    player_name "Can I see it?"
    show diane f_down_front a_idle:
        unflip
        xoffset -300
    show player 688
    with dissolve
    player_name "( Are those hooves? )"
    player_name "( ... And a tail too. )"
    show player 689
    player_name "( There's something written on the bottom of it. )"
    show expression "objects/closeup_statue_01.png"
    hide player
    hide diane
    hide richard
    with dissolve
    diane "What's that written on the bottom?"
    player_name "{b}\"Delmont.\"{/b}"
    player_name "Hmm, {b}Delmont{/b}..."
    player_name "It sounds familiar."
    hide expression "objects/closeup_statue_01.png"
    show diane b_shirtless:
        xoffset -300
    show richard
    show player 689 at left
    with dissolve
    diane "Maybe it's a name?"
    show richard f_confused
    richard "... Or a surname?"
    show richard f_normal
    show player 12 with dissolve
    player_name "You mind if I hang on to it?"
    show player 5
    diane "Knock yourself out."
    show player 13
    richard "Well..."
    show diane:
        flip
        xoffset 200
    richard "Give me a call if you need anything else."
    diane "Thanks again, {b}Richard{/b}."
    hide richard with dissolve
    pause
    diane "Say hi to {b}Lucy{/b} for me!"
    pause
    show diane f_laugh:
        unflip
        xoffset 0
    with dissolve
    diane "Oh, this is wonderful!"
    show diane f_normal
    diane "Isn't it wonderful, {b}[firstname]{/b}?!"
    show player 14
    player_name "Heh, it does look really nice."
    player_name "So what are those machines for?!"
    show player 13
    diane "Oh, right."
    diane "Those are milking machines."
    show player 10
    player_name "They are?"
    show player 13
    diane "You lay in them and attach the milkers to your breasts."
    diane "I had them custom-built for comfort, since I have to spend so many hours milking."
    show player 14
    player_name "I see."
    show player 13
    show diane f_smirk
    diane "Gravity should make your job a lot easier with me in that position..."
    show player 11
    player_name "!!!" with hpunch
    show player 10
    player_name "My job?!"
    show player 11
    show diane f_laugh
    diane "Of course!"
    show diane f_smirk
    diane "You're the one who keeps asking if you can help..."
    diane "... And with those magic hands of yours, I figured, who better?"
    show player 10
    player_name "So I'm going to be milking you?"
    show player 11
    diane "Is that a problem?"
    show player 29 with dissolve
    player_name "N-no!"
    show player 3
    pause
    show player 10 with dissolve
    player_name "How come there are three of them though?"
    show player 5
    show diane f_laugh
    diane "Heh, well, I'll have to expand and bring more ladies in eventually, right?"
    show diane f_normal
    show player 10
    player_name "M-more, ladies?"
    player_name "You mean, I'm gonna be milking more ladies?"
    show player 11
    diane "Maybe."
    show diane f_smirk
    diane "That's between you and them."
    show player 29 with dissolve
    player_name "I uhh... Wha-"
    player_name "{i}*Ahem*{/i} W-who do you have in mind?"
    show player 3
    show diane f_laugh
    diane "Hahaha, calm down handsome."
    show diane f_normal
    diane "I don't have anyone in mind right now..."
    diane "It could be a long while before I find the right fit for a job like that."
    show player 14 with dissolve
    player_name "Heh, right. That makes sense."
    show player 13
    diane "In the meantime, I'll have to see about {b}finding a way to increase my production{/b}..."
    show player 10
    player_name "What do you mean?"
    show player 5
    diane "Well, I'm nearing my limit on how much breast milk I can produce in a day."
    diane "There's gotta be something I can do to increase the flow..."
    show player 10
    player_name "Increase the flow?"
    player_name "... Maybe you should speak with a doctor?"
    show player 5
    diane "Yeah, that might be a good idea."
    diane "Don't worry, {b}[firstname]{/b}, I'll figure something out."
    show player 14
    player_name "N-no, I'll help too!"
    show player 13
    show diane f_laugh
    diane "Haha, there's something else I need you to do."
    show diane f_normal
    show player 14
    player_name "Anything!"
    show player 13
    diane "I don't think I ordered enough {b}storage containers for the milk{/b}."
    diane "Would you {b}run over to Consum-R and buy me one more{/b}?"
    show player 14
    player_name "Sure thing."
    show player 13
    diane "Thanks, {b}[firstname]{/b}."
    hide player
    hide diane
    with dissolve
    call popup ('give', 'mysterious_statue_1')
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
