label daisy_button_baby_leave:
    show player 14b
    player_name "I'll leave you guys be."
    show player 1b
    show daisy f_normal
    daisy "Alright."
    daisy f_down "Say, \"Bye-bye Daddy.\""
    show player 17
    player_name "Hehe."
    show player 14b
    if M_daisy.pregnancy.baby_gender == "twins":
        player_name "Goodbye, little ones."
    else:
        player_name "Goodbye, little one."
    hide player
    hide daisy
    with dissolve
    return

label daisy_button_get_anything_baby:
    show player 14b
    player_name "Can I get you anything?"
    show player 1b
    show daisy f_normal
    daisy "No, I'm okay."
    daisy "Thanks, {b}[firstname]{/b}."
    show player 14b
    player_name "You're welcome."
    show player 1b
    return

label daisy_button_hows_baby_doing_boy:
    show player 14b
    player_name "How's he doing?"
    show player 1b
    show daisy f_normal
    daisy "He sleeps a lot..."
    daisy "... And when he's not sleeping, he's eating!"
    show player 14b
    player_name "Heh, so he takes after his mommy then?"
    show player 1b
    daisy @ f_laugh "Nu uh!"
    show player 17
    player_name "Hehehe."
    show player 1b
    return

label daisy_button_hows_baby_doing_twins:
    show player 14b
    player_name "How are they doing?"
    show player 1b
    show daisy f_normal
    daisy "They sleep a lot..."
    daisy "... And when they're not sleeping, they're eating!"
    show player 14b
    player_name "Heh, so they take after their mommy then?"
    show player 1b
    daisy @ f_laugh "Nu uh!"
    show player 17
    player_name "Hehehe."
    show player 1b
    return

label daisy_button_hows_baby_doing_girl:
    show player 14b
    player_name "How's she doing?"
    show player 1b
    show daisy f_normal
    daisy "She sleeps a lot..."
    daisy "... And when she's not sleeping, she's eating!"
    show player 14b
    player_name "Heh, so she takes after her mommy then?"
    show player 1b
    daisy @ f_laugh "Nu uh!"
    show player 17
    player_name "Hehehe."
    show player 1b
    return

label daisy_button_gave_birth_intro:
    scene expression player.location.background_blur with None
    show player 14b at left
    show daisy a_baby f_down
    with dissolve
    player_name "Hey, {b}Daisy{/b}."
    show player 1b
    if M_daisy.pregnancy.baby_gender == "boy":
        daisy "Isn't he wonderful, {b}[firstname]{/b}?"
        show player 14b
        player_name "He sure is!"
        show player 1b
        daisy f_normal "He has your eyes."
    elif M_daisy.pregnancy.baby_gender == "twins":
        daisy "Aren't they wonderful, {b}[firstname]{/b}?"
        show daisy f_down
        show player 14b
        player_name "They sure are!"
        show player 1b
        daisy f_normal "They have your eyes."
    else:
        daisy "Isn't she wonderful, {b}[firstname]{/b}?"
        show daisy f_down
        show player 14b
        player_name "She sure is!"
        show player 1b
        daisy f_normal "She has your eyes."
    pause
    daisy f_down "And my horns!"
    daisy f_normal @ f_laugh "Hehehe!"
    return

label daisy_button_hows_the_baby_1:
    show player 14b at left
    show daisy
    player_name "How's the baby?"
    show player 1b
    daisy "Umm, I dunno."
    daisy "It makes me sick in the mornings but otherwise, I feel the same as always."
    show player 14b
    player_name "Well, that's good."
    player_name "You make sure and tell {b}Diane{/b} or me if you ever feel like something is wrong, okay?"
    show player 1b
    daisy "Y-yeah, okay {b}[firstname]{/b}."
    return

label daisy_button_hows_the_baby_2:
    show player 1b at left
    show daisy f_normal
    daisy "Hehe, look {b}[firstname]{/b}!"
    daisy f_down "My boobies are getting bigger!"
    show player 14b
    player_name "Yeah, you're producing more milk in preparation for the baby."
    show player 1b
    daisy f_normal "Oh, that will make {b}Diane{/b} happy, won't it?"
    show player 14b
    player_name "Yeah, it sure will."
    show player 1b
    pause
    show daisy f_down a_touch with dissolve
    daisy "Did you see my tummy?"
    show daisy f_normal
    show player 14b
    player_name "Yeah."
    show player 1b
    daisy f_sad "Do you think it's ugly?"
    show player 14b
    player_name "No, not at all!"
    player_name "I think it's kinda cute, actually..."
    show player 1b
    daisy f_laugh "Really?!"
    daisy "Hehe, you're weird {b}[firstname]{/b}!"
    show daisy f_normal a_idle with dissolve
    show player 17
    player_name "Hehe!"
    show player 1b
    return

label daisy_button_hows_the_baby_3:
    show player 1b at left
    show daisy a_touch f_sad
    daisy "{i}*Sigh*{/i}"
    daisy "This baby business is a real hassle, you know?!"
    show player 10b
    player_name "Oh?"
    show player 5b
    daisy "I have to pee like every five minutes!"
    show player 14b
    player_name "Heh, yeah that does sound like a hassle!"
    show player 1b
    daisy f_down "... And the baby is dancing all the time!"
    show player 14b
    player_name "Dancing?"
    show player 1b
    daisy f_normal "Yeah, {b}Diane{/b} says it's kicking but I don't know why it would kick me..."
    daisy "I'm its mommy after all."
    show player 14b
    player_name "Heh, I'm sure you're right."
    player_name "It's probably just excited to come out."
    show player 1b
    daisy f_laugh "Yeah!"
    daisy "I mean, I dance when I'm excited."
    show daisy f_normal a_idle with dissolve
    show player 14b
    player_name "Heh, you sure do."
    show player 1b
    return

label daisy_button_intro_end:
    scene expression player.location.background_blur with None
    show daisy
    show player 1b at left
    with dissolve
    daisy "{i}*Gasp*{/i} {b}[firstname]{/b}!!!"
    show player 14b

    if game.timer.is_morning():
        player_name "Good morning, {b}Daisy{/b}."
    else:
        player_name "Hey {b}Daisy{/b}."

    hide player
    show daisy b_naked_hug
    with dissolve

    if game.timer.is_morning():
        daisy "Morning hugs!!!"
    else:
        daisy "I missed you!"

    pause
    show daisy b_naked
    show player 14b at left

    if game.timer.is_morning():
        player_name "Heh, okay."
    else:
        player_name "Y-yeah, I missed you too."

    show player 1b
    return

label daisy_button_have_sex_first:
    show player 14b at left
    show daisy
    player_name "You still want to have sex?"
    show player 1b
    daisy "Oh, yes!"
    daisy "Very much!"
    pause
    show player 14b
    player_name "Alright, let's do it."
    show player 1b
    daisy "{i}*Gasp*{/i} Really?!"
    daisy @ f_laugh "Yay!!!"
    show player 14b
    player_name "C'mon, let's go to one of the milking machines."
    show player 1b
    daisy f_laugh "Okay!"
    hide player
    hide daisy
    with dissolve
    pause
    return

label daisy_button_have_sex_repeat:
    show player 10b at left
    show daisy
    player_name "You wanna... You know?"
    show player 5b
    daisy "{i}*Gasp*{/i} Have sex?!"
    show player 14b
    player_name "Y-yeah."
    show player 1b
    daisy "Of course!"
    daisy "I love it when we have sex!"
    show player 14b
    player_name "Heh, let's head over to the milking machines then."
    show player 1b
    daisy f_laugh "Okay!"
    hide player
    hide daisy
    with dissolve
    pause
    scene expression "backgrounds/location_barn_sex_back_day.jpg"
    show daisy_sex_breed pre_talk
    show daisy_sex_breed_mc
    with dissolve
    daisy "Alright, weasel... Come on in!"
    daisy "Hehehe!"
    hide daisy_sex_breed_mc
    show daisy_sex_breed insert_and_pullout
    with dissolve
    pause
    show daisy_sex_breed creampie_pullout with dissolve
    pause 1
    show daisy_sex_breed creampie
    daisy "!!!" with hpunch
    $ animated = False
    return

label daisy_button_diane_breeding:
    scene expression player.location.background_blur with None
    show player 13 at left
    show diane b_naked f_shamed_smile
    with dissolve
    diane "Psst, {b}[firstname]{/b}."
    show diane f_shamed
    show player 5
    player_name "Hmm?"
    show player 10
    player_name "{b}Diane{/b}, what's going on?"
    show player 5
    show diane f_shamed_smile
    diane "Were you on your way to see {b}Daisy{/b}?"
    show diane f_shamed
    show player 14
    player_name "Yeah, I was just on my way to milk her."
    show player 13
    diane f_smirk "Mmm, watching you milk her gets me so-"
    pause
    hide player
    show diane b_pull_mc_naked:
        flip
    diane "Come with me!" with hpunch
    diane "{b}Daisy{/b} can wait a little longer."
    diane "I need you inside me, right now!"
    hide diane with dissolve
    player_name "O-okay-"
    scene expression "backgrounds/location_barn_sex_back_day.jpg"
    show diane_sex_breed pre_talk
    show diane_sex_breed_mc
    with dissolve
    diane "C'mon stud, give it to me!"
    hide diane_sex_breed_mc
    show diane_sex_breed insert_and_pullout
    with dissolve
    pause
    show diane_sex_breed creampie_pullout with dissolve
    pause 1
    show diane_sex_breed creampie
    diane "Oh, yeaaaah!!" with hpunch
    $ M_diane.set('sex speed', 0.09)
    show expression AnimatedImage("diane_sex_back", [1,2,3,4,5,6,7,8,9,10], M_diane) as diane_sex_breed at Position(xalign = 0.0, yoffset = 0)
    pause
    diane "Ahh!"
    pause
    diane "Thank you, {b}[firstname]{/b}."
    diane "It's wrong of me to steal you away from {b}Daisy{/b} while she's still adjusting but..."
    diane "... I really nee-"
    diane "Ah, shit!"
    diane "... Really needed this today!"
    pause
    player_name "Heh, it's no problem {b}Diane{/b}."
    pause
    scene location_diane_garden_cutscene12
    with fade
    player_name "I think {b}Daisy{/b}'s been adjusting really well."
    player_name "She seems really happy living here."
    diane "I think so too."
    diane "We really lucked out finding her."
    diane "She's so adorable!"
    player_name "Plus, she's helping you out with your business now, right?"
    diane "Definitely!"
    diane "She produces more than I do, and she's not even-"
    scene location_diane_garden_cutscene12b with fade
    "{i}*Clink*{/i}{p=1}{nw}"
    "{i}*SMASH*{/i}!!!" with hpunch
    player_name "What the-"
    pause
    diane "{b}Daisy{/b}?!"

    scene expression player.location.background_blur with None
    show player 368f at Position (xpos=650)
    show diane b_naked f_smirk:
        xoffset 100
    show daisy b_naked_shy f_sad:
        flip
    with dissolve
    daisy "I didn't-"
    daisy "I-I-I wasn't-"
    diane "Were you watching us?"
    pause
    daisy "I'm sorry, please don't be mad!"
    show diane f_laugh
    diane "Hehe, it's alright, sweetie!"
    hide daisy
    show daisy b_naked_diane_comfort:
        xoffset -312
    show diane b_empty f_smirk_fardown zorder 1:
        xoffset -312
    with dissolve
    diane "Shh, we're not mad."
    show daisy b_naked_diane_comfort2
    daisy "{i}*Sniff*{/i} Y-you're not mad?"
    show daisy b_naked_diane_comfort
    diane "Of course not!"
    diane "You were just curious, weren't you?"
    show daisy b_naked_diane_comfort2
    daisy "Y-yeah..."
    show diane b_naked a_idle f_smirk:
        xoffset 100
    hide daisy
    show daisy:
        flip
    with dissolve
    daisy "I've never seen anyone else play {i}hide the weasel{/i} before..."
    show player 367f
    player_name "Hide the weasel?"
    show player 368f
    daisy "Master and I used to play it too!"
    pause
    daisy "His weasel wasn't as large as {b}[firstname]{/b}'s though..."
    show player 367f
    player_name "You mean, {b}Jebadiah{/b} was having sex with you?!"
    show player 368f
    show diane f_shamed_smile
    diane "{i}*Sigh*{/i} Of course he was..."
    diane "... The dirty old bastard."
    show diane f_shamed
    daisy "Don't be upset {b}Diane{/b}..."
    daisy f_laugh "Master just needed my help!"
    daisy "I didn't want his weasel to get sick and die!"
    show daisy f_normal
    show player 367f
    player_name "Okay, I'm confused."
    show player 368f
    daisy "That's why you play with {b}[firstname]{/b}, right?"
    pause
    show diane f_shamed_smile
    diane "Sweetie, exactly what did that old man tell you?"
    show diane f_shamed
    daisy "Umm, that sometimes a man's weasel gets sick and becomes hard all over..."
    player_name "..."
    daisy "... And when that happens, he needs to put it inside a woman's hidey-hole."
    daisy "Otherwise, it turns blue and falls off."
    pause
    show diane f_shamed_smile
    diane "Well, he was a creative old bastard... I'll give him that."
    show diane f_shamed
    show player 367f
    player_name "... Hidey-hole?"
    show player 368f
    daisy "Yeah!"
    hide daisy
    show daisy b_naked_behind:
        xoffset -450
    with dissolve
    show diane f_surprised_front
    daisy "Master said his weasel liked my hidey-hole the best!"
    show player 430f
    with hpunch
    pause
    show player 66f
    daisy "{i}*Gasp*{/i}"
    hide daisy
    show daisy f_sad:
        flip
    with dissolve
    show diane f_surprised
    daisy "Look {b}Diane{/b}!"
    daisy "{b}[firstname]{/b}'s weasel is getting sick again!"
    show diane f_surprised_front
    show player 67f
    pause
    hide daisy
    show daisy b_naked_behind:
        xoffset -450
    with dissolve
    daisy "Do you want to use my hidey-hole this time?!"
    show player 430bf
    player_name "Uhh."
    show player 430f
    show diane f_shamed_smile
    diane "No, no, no..."
    diane "{b}[firstname]{/b}'s {i}*Ahem*{/i} weasel... Will be just fine."
    show diane f_shamed
    hide daisy
    show daisy f_normal:
        flip
    with dissolve
    show diane f_shamed_smile
    diane "Right now, I think you and I need to have a talk."
    show diane f_shamed
    daisy "Oh, okay."
    diane f_smirk "I'm sure {b}[firstname]{/b} can take care of that on his own, can't you {b}[firstname]{/b}?"
    show player 432f
    player_name "Y-yeah..."
    show player 431f
    diane "Why don't you head on home for the day and give us some girl time."
    show player 432f
    player_name "Sure thing."
    show player 431f
    daisy @ f_laugh "Byeeee, {b}[firstname]{/b}!"
    show player 432f
    player_name "Heh, bye {b}Daisy{/b}."
    hide player
    hide daisy
    hide diane
    with dissolve
    return

label daisy_button_more_jebadiah_delmont_2:
    hide anon
    show player 10b at left
    with {'master': fastdissolve}
    player_name "There's something I still don't understand, {b}Daisy{/b}."
    show player 5b
    show daisy f_normal
    daisy @ -m_talk "Hmm?"
    show player 10b
    player_name "Why were you so frightened of me when you first appeared?"
    show player 5b
    daisy f_sad "Oh."
    daisy f_surprised_after_appear "Umm..."
    pause
    show player 10b
    player_name "You don't have to tell me if you don't want to."
    show player 5b
    daisy f_sad "No, I..."
    daisy "... I want to."
    daisy f_sad_closed "I just..."
    pause
    show daisy a_cover -b_naked_flowers with dissolve
    daisy "I was a bad girl, {b}[firstname]{/b}!"
    show player 10b
    player_name "Huh?!"
    player_name "I find that hard to imagine."
    show player 5b
    daisy f_sad "No, I was!"
    show daisy a_idle
    daisy "You see, Master forgot to lock the shack one night and I-"
    daisy @ f_sad_closed "I..."
    pause
    daisy "I just wanted to go for a walk!"
    pause
    daisy "But I got lost..."
    show player 10b
    player_name "You did?"
    show player 5b
    daisy "Uh huh."
    daisy "It was so scary!"
    daisy "I was lost for days with no food or water..."
    daisy "... But then, they saved me."
    show player 10b
    player_name "Who saved you?"
    show player 5b
    daisy "Bernice and Jethro."
    daisy "They brought me back to their house and gave me food."
    show player 10b
    player_name "Well, that was lucky."
    show player 5b
    daisy "It was..."
    daisy @ a_wiping_tears "{i}*Sniff*{/i}"
    daisy "They were very nice people."
    daisy "Master didn't think so though..."
    player_name "Hmm?"
    daisy "He was so mad at me!"
    daisy "I told him I didn't mean to, but he grabbed me by the arm really hard and pulled me out of the house."
    daisy "Jethro yelled at him to take it easy and Master hit him."
    daisy "Over and over and over again."
    daisy "It was awful!"
    show player 10b
    player_name "What an asshole..."
    player_name "Why was he so mad?!"
    show player 5b
    daisy "He said other people couldn't be trusted, especially men."
    daisy "That they would hand me over to the Gophermant for a pat on the head."
    show player 10b
    player_name "Gophermant?!"
    show player 5b
    pause
    show player 10b
    player_name "Do you mean the {i}Government{/i}?"
    show player 5b
    daisy "Yeah, that's the one."
    player_name "..."
    show player 10b
    player_name "So then what happened?"
    show player 5b
    daisy "After that, Master started to chain me up in the shack at night."
    show player 10b
    player_name "He chained you up?!"
    show player 5b
    daisy "Yeah, he said it was for my own good..."
    daisy "... That I was a bad girl."
    show player 10b
    player_name "You're not a bad girl, {b}Daisy{/b}."
    player_name "It sounds to me, like he was a bad master."
    show player 5b
    daisy "{i}*Sniff*{/i} R-really?"
    show player 10b
    player_name "Yes."
    player_name "You definitely didn't deserve to be treated like that!"
    show player 5b
    daisy @ f_sad_closed "It's hard to sleep when you're chained up."
    show player 10b
    player_name "I bet."
    player_name "I'd like to chain him up and show him how it feels!"
    show player 5b
    daisy @ -m_talk "..."
    show player 10b
    player_name "So that's why you were scared when you saw us?"
    show player 5b
    daisy "Uh huh."
    daisy "I was worried Master would find out."
    show player 10b
    player_name "Well, there's no need to worry about that."
    player_name "{b}Diane{/b} and I won't let anybody hurt you ever again."
    show player 5b
    return

label daisy_button_how_are_your_flowers_3:
    hide anon
    show player 14b at left
    with {'master': fastdissolve}
    player_name "How are your flowers?"
    show daisy f_normal
    daisy "Oh, the sunflowers you got me are so pretty!"
    daisy "I love them!"
    show player 14b
    player_name "That's great!"
    player_name "I had a feeling they would cheer you up."
    show player 1b
    daisy @ -m_talk "Mmhmm!"
    return

label daisy_button_you_seem_happy:
    hide anon
    show player 14b at left
    with {'master': fastdissolve}
    player_name "You seem really happy today."
    show player 1b
    show daisy f_normal
    daisy "I am!"
    daisy "Very, very happy!"
    daisy "I get to live here in the nice barn and {b}Diane{/b} takes care of me and you bring me yummy pizza..."
    pause
    daisy "I'm glad you were the one who found me {b}[firstname]{/b}."
    show player 14b
    player_name "Yeah, me too."
    player_name "I like seeing you happy, {b}Daisy{/b}!"
    show player 1b
    daisy f_surprised_after_appear "!!!"
    show daisy a_touch with dissolve
    pause
    show player 10b
    player_name "You okay?"
    show player 5b
    daisy f_normal "Y-yeah."
    daisy a_idle "Sometimes, I feel funny in my tummy when you're around..."
    player_name "Hmm?"
    show player 10b
    player_name "Does it hurt?"
    show player 5b
    daisy f_down "N-no, it feels... All tingly."
    show player 10b
    player_name "Huh, weird."
    show player 5b
    return

label daisy_button_want_me_to_milk_you:
    show daisy f_normal
    show player 1b at left
    daisy "Umm, {b}[firstname]{/b}?"
    show player 14b
    player_name "Yeah?"
    show player 1b
    daisy "C-could you milk me?"
    show daisy f_down b_naked_boob with dissolve
    daisy "'Cause my boobies are all full again."
    pause
    show player 14b
    player_name "{i}*Gulp*{/i} S-sure."
    hide player
    show daisy b_player_milking
    with dissolve
    daisy @ -m_talk "!!!"
    player_name "Does that feel alright?"
    daisy "Y-yes."
    player_name "Just relax and enjoy, {b}Daisy{/b}."
    return

label daisy_button_finished_milking_intro:
    scene expression player.location.background_blur with None
    show player 1b at left
    show daisy f_laugh a_up
    with dissolve
    daisy "{i}*Gasp*{/i} {b}[firstname]{/b}!!!"
    show daisy f_normal a_idle with dissolve
    show player 14b
    player_name "Hey, {b}Daisy{/b}."
    show player 1b
    daisy "What are we gonna do today?!"
    show player 14b
    player_name "Heh, I don't know yet."
    show player 1b
    return

label daisy_button_daisy_need_milking:
    scene expression player.location.background_blur with None
    show player 1b at left
    show daisy f_laugh
    with dissolve
    daisy "Okay, I'm ready!"
    show daisy f_normal
    show player 10b
    player_name "C-can I ask you something?"
    show player 5b
    daisy @ -m_talk "Hmm?"
    show player 10b
    player_name "How come you want me to-"
    player_name "{i}*Ahem*{/i} M-milk you?"
    show player 5b
    daisy "Well, {b}Diane{/b} says you're better at it than she is and..."
    daisy f_down "... And I..."
    pause
    daisy "... Y-you make me..."
    daisy "... I dunno."
    show daisy f_laugh
    show player 14b
    player_name "Umm, okay."
    show daisy f_normal
    player_name "I guess we should get started, huh?"
    show player 1b
    pause
    hide player
    show daisy b_player_milking f_down
    with dissolve
    daisy @ -m_talk "!!!"
    player_name "Does that feel alright?"
    daisy "Y-yes."
    player_name "Let me know if I do anything that doesn't, okay?"
    daisy f_normal_smelling @ -m_talk "Mmmhmm."
    pause
    daisy f_down "{b}Diane{/b} was right, you are really good at this!"
    player_name "Heh, thanks."
    daisy "Ahh!"
    player_name "Just relax and enjoy, {b}Daisy{/b}."
    return

label daisy_button_get_new_flowers_has_flowers:
    scene expression player.location.background_blur with None
    show player 14b at left
    show daisy b_naked_shy f_sad
    with dissolve
    player_name "Hey, {b}Daisy{/b}."
    show player 1b
    daisy "Hi, {b}[firstname]{/b}."
    show player 14b
    player_name "I've got something for you."
    show player 1b
    daisy @ -m_talk "Hmm?"
    show player 239_240 with dissolve
    pause
    show player 722 with dissolve
    pause
    show daisy f_normal b_naked a_cover with dissolve
    daisy "{i}*Gasp*{/i} Wowzers!!!"
    show player 1b
    show daisy a_sunflower1 f_down
    with dissolve
    daisy "Look how big and pretty they are!"
    pause
    show daisy a_sunflower2 f_normal_smelling with dissolve
    daisy @ -m_talk "Mmm!"
    show daisy b_naked_hug
    hide player
    with dissolve
    daisy "Thank you, thank you, thank you!!!"
    show player 14b at left
    show daisy a_sunflower1 b_naked f_down zorder 1:
        xoffset -200
    with dissolve
    player_name "Heh, you're welcome."
    show player 1b
    daisy "What are these flowers called?"
    show player 14b
    player_name "Those are called {b}sunflowers{/b}."
    show player 1b
    daisy f_normal "Why do they call them that?"
    show player 14b
    player_name "Hmm, probably because of their yellow color."
    show player 1b
    daisy "Oh, I get it."
    show daisy
    daisy f_down @ f_laugh "Like the sun!"
    show player 14b
    player_name "Heh, that's right."
    show player 1b
    show daisy
    daisy f_normal @ f_laugh "Hehe!"
    show diane b_shirtless f_shamed_fardown with dissolve:
        xoffset 100
    show player 13
    diane "Oh, did you get new flowers?"
    show daisy f_laugh:
        flip
        xoffset 200
    with dissolve
    daisy "{b}[firstname]{/b} brought me some!"
    show daisy f_down
    show diane f_smirk
    diane "Well, wasn't that nice of him..."
    daisy f_normal "Uh huh!"
    daisy "{b}[firstname]{/b} is the nicest man ever!"
    show daisy f_down
    diane "He certainly is."
    pause
    show diane f_shamed_fardown
    diane "Alright, we should get those flowers in some water so I can get you milked, sweetie."
    diane "Lots of work to be done today."
    show daisy f_shy:
        unflip
        xoffset -200
    with dissolve
    daisy "I want {b}[firstname]{/b} to do it."
    show player 11
    player_name "!!!" with hpunch
    show player 10b
    player_name "W-what?"
    show player 5b
    show daisy f_normal:
        flip
        xoffset 200
    with dissolve
    daisy f_normal "Is it okay if {b}[firstname]{/b} milks me, {b}Diane{/b}?"
    diane "It's fine with me."
    show daisy f_shy:
        unflip
        xoffset -200
    with dissolve
    show diane f_smirk
    daisy "Will you milk me, {b}[firstname]{/b}?"
    show player 14b
    player_name "Uhh, sure... If that's what you want."
    show player 1b
    daisy f_normal @ f_laugh "Yay!!"
    diane "Just be careful with her, okay?"
    show player 14
    player_name "Y-yeah, I will."
    show player 13
    show diane f_shamed_fardown
    diane "Alright, let's go take care of those flowers."
    daisy "Okay."
    daisy @ f_shy_back "I'll be right back, {b}[firstname]{/b}."
    show player 14b
    player_name "O-okay."
    hide player
    hide daisy
    hide diane
    with dissolve
    return

label daisy_button_get_new_flowers_no_flowers:
    scene expression player.location.background_blur with None
    show player 10b at left
    show daisy a_cover f_sad_closed
    with dissolve
    player_name "You okay?"
    show player 5b
    show daisy a_wiping_tears with dissolve
    daisy "Yeah."
    show daisy a_cover b_naked_shy f_sad
    with dissolve
    daisy "I just miss my flowers..."
    show player 10b
    player_name "I'm sorry, {b}Daisy{/b}."
    player_name "Can I get you anything?"
    player_name "I don't like seeing you sad like this..."
    show player 5b
    daisy "No, it's alright."
    pause
    daisy "Thanks, {b}[firstname]{/b}."
    hide daisy with dissolve
    show player 5
    player_name "( Hmm, I should {b}go to Cupid in the mall and get her some new flowers{/b}. )"
    show player 13
    player_name "( I bet that will cheer her up. )"
    pause
    player_name "( {b}Diane{/b} said I should {b}look for sunflowers{/b}. )"
    hide player with dissolve
    return

label daisy_button_sleeping:
    show player 434 with dissolve
    player_name "( Aww, look how cute she is when she's sleeping! )"
    player_name "( I should leave her be. )"
    hide player with dissolve
    return

label daisy_button_no_veggie_pizza:
    hide anon
    show player 1b at left
    with {'master': fastdissolve}
    show daisy f_normal
    daisy "Did you bring me another {b}veggie pizza{/b}?"
    show player 10b
    player_name "No, not today."
    show player 5b
    daisy f_sad "Aww..."
    show player 10b
    player_name "Sorry, {b}Daisy{/b}..."
    player_name "... Maybe tomorrow, okay?"
    show player 5b
    daisy "Okay."
    return

label daisy_button_has_veggie_pizza:
    hide anon
    show player 14b at left
    with {'master': fastdissolve}
    player_name "I brought you something!"
    show player 1b
    show daisy f_normal
    daisy "{i}*Gasp*{/i} A present?!"
    player_name "Mmmhmm."
    show player 239_240 with dissolve
    pause
    show player 719c with dissolve
    daisy "{b}Veggie pizza{/b}?!"
    show player 719d
    player_name "Hehe, that's right!"
    show player 719c
    daisy @ f_laugh "Yay!!"
    show player 721 with dissolve
    pause
    show player 18
    show daisy a_pizza_slice b_naked
    with dissolve
    pause
    show daisy f_laugh a_up with dissolve
    daisy "I love pizza!!"
    show player 17
    player_name "Me too!"
    show player 1b
    show daisy a_pizza_eat f_empty with dissolve
    pause
    daisy "Mmm!"
    hide player
    hide daisy
    with dissolve
    return

label daisy_button_more_jebadiah_delmont:
    show player 10b
    player_name "So, do you think you're ready to tell me more about your old master?"
    show player 5b
    show daisy f_sad b_naked_shy
    with dissolve
    daisy "Mmm, maybe..."
    daisy "What do you want to know?"
    show player 10b
    player_name "What was he like?"
    show player 5b
    daisy "Hmm, Master was..."
    daisy "... Different, than you and {b}Diane{/b}."
    daisy "He didn't get along with other people very well, but he didn't want to be alone either."
    daisy "So he made me."
    show player 10b
    player_name "He made you?"
    show player 5b
    daisy "Mmhmm."
    show player 10b
    player_name "How did he do that?"
    show player 5b
    daisy "I don't know..."
    show daisy f_normal b_naked with dissolve
    daisy "... Maybe he used his magics?"
    pause
    show player 14b
    player_name "So you really saw him do magic then?"
    show player 1b
    daisy @ f_laugh "Oh yes, wonderful magics!"
    pause
    daisy "He could remove his thumb or pull money out from behind my ear whenever he wanted!"
    show player 5b
    player_name "..."
    daisy "He had a storm cloud that he trapped inside a stick!"
    show player 10b
    player_name "Huh?"
    show player 5b
    daisy "Yeah, if you turned it upside down, you could hear it raining inside!"
    player_name "..."
    daisy @ f_laugh "Oh, oh, oh, and he had a glass ball full of snow from the north pole!"
    show player 10b
    player_name "Let me guess: you had to shake it, and then the snow would fall?"
    show player 5b
    daisy "Yeah!"
    daisy f_shy "How did you know that?!"
    show player 14b
    player_name "They're called snow globes."
    show player 1b
    daisy f_sad "{i}*Gasp*{/i} Do you know magics too?!"
    show player 10b
    player_name "{b}Daisy{/b}, I don't think any of that was magic..."
    show player 5b
    daisy f_normal "What about his wand then?!"
    show player 10b
    player_name "Wand?"
    show player 5b
    daisy "Yeah, it would make a clicky sound and then fire would spurt from the tip!"
    daisy @ f_laugh "It was definitely magics!"
    daisy "I saw it."
    player_name "..."
    return

label daisy_button_milking_business:
    show player 14b
    player_name "So, you like it when {b}Diane{/b} milks you?"
    show player 1b
    show daisy f_normal
    daisy "Oh, yes!"
    show daisy f_laugh a_up with dissolve
    daisy "Milking makes my boobies feel good!"
    show daisy f_normal a_idle with dissolve
    daisy "Plus, she's much gentler than Master was..."
    pause
    daisy "... I just wish it didn't tickle me so!"
    show player 14b
    player_name "I'm sure she'll figure out a way to do it without tickling you."
    show player 1b
    daisy "I hope so."
    daisy "I want {b}Diane{/b} to sell my milk too and make people happy!"
    return

label daisy_button_how_are_your_flowers_2:
    show player 14b
    player_name "How are your flowers?"
    show player 1b
    show daisy f_normal
    daisy "They're still doing good."
    daisy "I give them water and sunlight every day, just like you told me."
    show player 14b
    player_name "That's wonderful, {b}Daisy{/b}."
    show player 1b
    daisy "Mmhmm."
    daisy "{b}Diane{/b} says there's lots of flowers in the world and they come in all sorts of different colors too!"
    daisy "Is that true?"
    show player 14b
    player_name "Yup, it's true."
    show player 1b
    show daisy f_laugh a_cover with dissolve
    daisy "Wowzers!"
    show daisy f_normal a_idle with dissolve
    daisy "I hope I get to see them all someday..."
    return

label daisy_button_finished_pizza_intro:
    scene expression player.location.background_blur with None
    show player 1b at left
    show daisy f_normal
    daisy "Hi, {b}[firstname]{/b}!"
    show player 14b
    player_name "Hey, {b}Daisy{/b}."
    player_name "How are you today?"
    show player 1b
    daisy @ f_sad "Mmm, I'm bored."
    daisy "What are you doing?"
    return

label daisy_button_get_pizza_has_not_pizza:
    scene expression player.location.background_blur with None
    show player 1b at left
    show daisy f_laugh
    with dissolve
    daisy "Pizza!"
    daisy "Hehehe!"
    show daisy f_normal
    show player 14b
    player_name "Heh, she's so excited."
    player_name "I should {b}head to Tony's Pizza and get her a veggie pizza{/b}."
    hide player
    hide daisy
    with dissolve
    return

label daisy_button_get_pizza_has_pizza:
    scene expression player.location.background_blur with None
    show player 719d at left
    show daisy
    with dissolve
    player_name "{b}Daisy{/b}?"
    player_name "Look what I've brought for you!"
    show player 719c
    show daisy f_laugh
    daisy "Pizza?!"
    show daisy f_normal
    show player 720 with dissolve
    player_name "Mmmhmm!"
    daisy "Oh, it smells really good!"
    pause
    daisy f_sad "How do I eat it?"
    show player 720b
    player_name "Hehe, lemme show you."
    show daisy f_normal
    show player 721 with dissolve
    player_name "You just hold it like this and start eating from this end here."
    show player 719d with dissolve
    player_name "Mmm, so good!!"
    show player 719c
    pause
    show player 719d
    player_name "Now you try."
    show daisy a_pizza_hold
    show player 1b
    with dissolve
    daisy "O-okay."
    show daisy a_pizza_slice f_sad with dissolve
    daisy "Like this?"
    show daisy f_normal
    show player 14b
    player_name "Yup, just like that."
    show player 1b
    daisy "{i}*Gasp*{/i} Wowzers!!! My first pizza!"
    show player 17 with dissolve
    player_name "Hehe!"
    show player 1b
    show daisy a_pizza_eat f_empty with dissolve
    daisy "Mmmhmm!!!"
    show player 11
    player_name "!!!" with hpunch
    pause
    daisy "More!"
    show player 10b
    player_name "Yeah, eat as much as you'd like..."

    scene location_diane_garden_cutscene13
    show text _ ("The pizza went over even better than I had expected.\nTo this day I have never seen anyone throw down food like {b}Daisy{/b}.") as caption
    with fade
    pause
    hide caption with dissolve
    show text _ ("{b}Daisy{/b} went through eight pieces in the time it took me to eat two!") as caption with dissolve
    pause

    scene expression player.location.background_blur
    show player 1b at left
    show daisy o_sauce f_burp
    with fade
    daisy "{i}*Buuuuurp*{/i}"
    show daisy f_normal
    show player 14b
    player_name "Heh, you alright over there?"
    show player 1b
    daisy @ f_laugh "That was so delicious!!"
    daisy "Can I eat pizza every day?!"
    show player 17
    player_name "Haha, I don't think that would be a good idea..."
    show player 1b
    daisy f_sad "Oh."
    show player 14b
    player_name "... But I can bring you some every now and then."
    show player 1b
    show daisy f_laugh a_up with dissolve
    daisy "Yay!"
    daisy "I like pizza!"
    show daisy f_normal a_idle with dissolve
    show player 14b
    player_name "Hehe, me too!"
    show player 433
    daisy "Thank you, {b}[firstname]{/b}!"
    hide player
    show daisy b_naked_hug o_empty
    with dissolve
    player_name "Y-you're welcome, {b}Daisy{/b}."
    show daisy f_normal o_sauce b_naked
    show player 1b at left
    with dissolve
    daisy "I'm gonna go see if {b}Diane{/b} wants some pizza too!"
    hide daisy with dissolve
    show player 13
    pause
    show player 14
    player_name "You better tell her to hurry, there's only a few slices left!"
    show player 13
    pause
    show player 18
    player_name "( I'm really glad I did this. )"
    player_name "( {b}Daisy{/b} is so cute when she's happy. )"
    show player 13
    pause
    show player 426
    player_name "( Alright, I'd better finish up here and get to work on the garden before I run out of daylight. )"
    hide player with dissolve
    return

label daisy_button_leave:
    hide anon
    show player 14b at left
    with {'master': fastdissolve}
    if not M_daisy.finished_state(S_daisy_get_pizza):
        show daisy f_shy b_naked_shy
    else:
        show daisy f_normal
    player_name "I should get back to work."
    player_name "Let me know if you need anything, okay?"
    show player 1b
    daisy "O-okay."
    daisy "Bye, {b}[firstname]{/b}."
    hide player
    hide daisy
    with dissolve
    return

label daisy_button_jebadiah_delmont:
    show player 10b at left
    show daisy f_shy b_naked_shy
    player_name "So your old master doesn't sound like a very nice guy, huh?"
    show player 5b
    daisy f_sad "Mmm, he {i}could{/i} be nice... Sometimes."
    daisy "When I was a good girl."
    show player 10b
    player_name "Oh?"
    show player 5b
    daisy f_shy "He would bring me presents and teach me songs."
    show player 10b
    player_name "Well, that doesn't sound so bad..."
    show player 5b
    show daisy f_sad a_cover with dissolve
    daisy "As long as I stayed quiet in the shack and didn't touch his things, I was a good girl."
    show player 10b
    player_name "What happened if you left the shack?"
    show player 5b
    daisy f_sad_closed "I don't-"
    daisy "H-he would-"
    show daisy b_naked a_cover with dissolve
    pause
    show player 10b
    player_name "Do you wanna talk about it?"
    show player 5b
    daisy "No, please no!"
    show player 10b
    player_name "It's okay, we don't have to-"
    show player 433
    daisy "No, no, no, no-"
    show player 10b
    player_name "{b}Daisy{/b}, it's okay..."
    player_name "We don't have to talk about him at all if you don't want to."
    show player 5b
    daisy f_sad "{i}*Sniff*{/i} I-I'm a good girl?"
    show player 14b
    player_name "Of course!"
    show player 10b
    player_name "I didn't mean to upset you, I-"
    show player 5b
    pause
    show player 14b
    player_name "You don't need to worry, {b}Daisy{/b}."
    player_name "{b}Diane{/b} and I would never hurt you."
    show player 1b
    show daisy f_sad b_naked_shy with dissolve
    daisy "O-okay."
    return

label daisy_button_about_yourself:
    show player 14b at left
    show daisy f_shy b_naked_shy
    player_name "Tell me about yourself."
    show player 1b
    daisy "Me?!"
    show player 14b
    player_name "Yeah, I'd like to know more about you."
    show player 1b
    daisy "I don't..."
    daisy "... There's not much-"
    show player 14b
    player_name "Is there anything you like?"
    show player 1b
    daisy "Umm, flowers?"
    show player 17
    player_name "Heh, anything besides flowers?"
    show player 1b
    daisy @ f_down -m_talk "Hmm."
    daisy "Oats!"
    show player 10b
    player_name "Oats?"
    show player 5b
    daisy "Yeah, Master used to feed me oats all the time."
    daisy @ f_laugh "It was yummy!"
    show player 14b
    player_name "What's {b}Diane{/b} been feeding you?"
    show player 1b
    daisy "Oh, lots of stuff..."
    daisy "She says I should try other things and not just eat oats all the time."
    show player 14b
    player_name "She's right."
    player_name "What have you tried so far?"
    show player 1b
    daisy "Mmm, I've tried lettuce, carrots, bopples, grapes-"
    show player 10b
    player_name "Bopples?"
    player_name "What's a bopple?"
    show player 1b
    daisy @ f_down "Umm, they are red and crunchy and they make my tongue feel funny."
    player_name "Hmm?"
    daisy "{b}Diane{/b} says it's because they are sweet."
    show player 14b
    player_name "Do you mean an apple?"
    show player 1b
    daisy f_down @ f_laugh "Yes, that's it!"
    daisy "Apple."
    daisy f_shy "It was yummy too, but oats are much better!"
    show player 14b
    player_name "Heh, okay."
    show player 1b
    return

label daisy_button_how_are_your_flowers_1:
    show player 14b at left
    show daisy f_shy b_naked_shy
    player_name "How are your flowers?"
    player_name "Have you been watching them closely?"
    show player 1b
    daisy "Yes, very closely!"
    daisy "{b}Diane{/b} was right, they do drink the water!"
    daisy "It's so neat!"
    show player 17
    player_name "Hehehe."
    show player 1b
    daisy "Do you wanna watch them with me?!"
    show player 14b
    player_name "Uhh, no... Sorry {b}Daisy{/b}, I have too much work to do around here."
    show player 1b
    daisy "Oh, okay."
    return

label daisy_button_still_nervous:
    show player 14b
    show daisy f_shy b_naked_shy
    player_name "I still make you nervous, huh?"
    show player 1b
    daisy "Y-yeah... A little."
    pause
    daisy "S-sorry."
    show player 14b
    player_name "Heh, you don't need to be sorry."
    player_name "It's okay, I understand."
    show player 1b
    pause
    show player 14b
    player_name "There's no rush."
    show player 1b
    return

label daisy_button_intro_scared:
    scene expression player.location.background_blur with None
    show player 10b at left
    show daisy b_naked_behind_sad
    with dissolve
    player_name "Hi there, uhh-"
    show player 11
    show daisy b_jump_scared
    cow "EEEEP!!!" with hpunch
    show daisy b_naked a_cover f_sad_closed
    pause
    show player 24
    diane "{b}[firstname]{/b}!"
    show diane b_naked f_shamed_smile:
        xoffset 100
    diane "She's still frightened of you!"
    show diane f_shamed
    show player 25
    player_name "I'm sorry, I didn't mean to scare her."
    show player 24
    show diane f_shamed_smile
    diane "It's alright."
    diane "Just give me a little more time with her, okay?"
    show diane f_shamed
    pause
    show diane f_shamed_smile
    diane "{b}I'll let you know when she's ready to speak with you{/b}."
    show diane f_shamed
    show player 25
    player_name "O-okay."
    hide player with dissolve
    return

label daisy_button_intro:
    scene expression player.location.background_blur with None
    show player 14b at left
    show daisy f_shy b_naked_shy
    with dissolve
    player_name "Hey, {b}Daisy{/b}."
    show player 1b
    daisy @ -m_talk "..."
    daisy "H-hi."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
