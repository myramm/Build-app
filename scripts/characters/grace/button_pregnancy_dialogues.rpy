label button_grace_pregnancy_need_anything_babies:
    anon "You guys need anything?"
    grace "No, everything is wonderful!"
    grace f_happy_down "We're doing just fine, aren't we?"
    grace "Yes, we are!"
    pause
    grace "Mmm, our child is so beautiful, {b}[firstname]{/b}!"
    anon @ f_laugh "Hehe!"
    return

label button_grace_pregnancy_gave_birth_intro:
    scene expression player.location.background_closeup with None
    show anon
    show grace a_baby f_happy_down
    with dissolve
    grace "{b}Mommy{/b} loves you so much..."
    grace "Yes, she does!"
    grace @ f_laugh "Hehehe!"
    anon "Hey there."
    grace f_happy "Hey, {b}[firstname]{/b}."
    grace "I'm so glad you talked me into this!"
    anon "Oh, yeah?"
    grace "Yeah!"
    return

label button_grace_pregnancy_bedridden_yup:
    anon "Yeah, how are you guys doing?"
    grace f_happy_down @ f_tired "{i}*Yawn*{/i} Sleepy."
    if M_grace.pregnancy.baby_gender == "boy":
        anon "Do you want me to take him?"
    elif M_grace.pregnancy.baby_gender == "twins":
        anon "Do you want me to take them?"
    else:
        anon "Do you want me to take her?"
    grace "No, it's okay."
    if M_grace.pregnancy.baby_gender == "boy":
        grace "He's such a good boy, you know?"
    elif M_grace.pregnancy.baby_gender == "twins":
        grace "They're so good, you know?"
    else:
        grace "She's such a good girl, you know?"
    grace "Always so calm and relaxed."
    anon "Oh, yeah?"
    if M_grace.pregnancy.baby_gender == "boy":
        grace "I'm not sure he's even cried once since the delivery room."
    elif M_grace.pregnancy.baby_gender == "twins":
        grace "I'm not sure they've cried once since the delivery room."
    else:
        grace "I'm not sure she's even cried once since the delivery room."
    pause
    if M_grace.pregnancy.baby_gender == "boy":
        grace "Must come from you because he definitely didn't get that trait from me!"
    elif M_grace.pregnancy.baby_gender == "twins":
        grace "Must come from you because they definitely didn't get that trait from me!"
    else:
        grace "Must come from you because she definitely didn't get that trait from me!"
    anon @ f_laugh "Hehe!"
    pause
    grace f_happy "I wonder if you could do me a favor, {b}[firstname]{/b}?"
    anon "Sure, anything!"
    grace "Peek in on {b}Odette{/b} and make sure she's doing okay while I'm stuck in here, yeah?"
    anon "I can do that."
    grace "Thanks, {b}[firstname]{/b}."
    pause
    if M_grace.pregnancy.baby_gender == "twins":
        anon f_shy_low "I'll see you soon, little ones."
    else:
        anon f_shy_low "I'll see you soon, little one."
    grace @ f_laugh "Hehe!"
    hide anon with dissolve
    return

label button_grace_pregnancy_bedridden_intro:
    scene expression game.timer.image("location_hospital_baby_bed{}")
    show grace b_gown_bed
    show anon with dissolve
    grace "Hey, {b}[firstname]{/b}."
    grace "You come by to check on us again?"
    return

label button_grace_ill_leave_you_be_baby:
    anon "I'll leave you be."
    grace f_happy "Come back and see us soon, okay?"
    anon "Will do."
    hide anon with dissolve
    return

label button_grace_ill_leave_you_be:
    anon "I'll leave you be."
    grace "Alright."
    anon "I'm here if you need me, okay?"
    grace f_normal "Thanks for checking in, {b}[firstname]{/b}."
    hide anon with dissolve
    return

label button_grace_get_you_something_0:
label button_grace_get_you_something_1:
    anon f_normal "Can I get you something?"
    grace f_normal "No, I'm okay."
    grace "Thanks for offering."
    anon "Has {b}Odette{/b} been helping you?"
    grace @ f_sad_down "Yeah."
    grace "She's actually been really great so far!"
    anon "That's good to hear."
    return

label button_grace_get_you_something_2:
label button_grace_get_you_something_3:
    anon "Can I get you anything?"
    grace "No, I'm okay."
    pause
    grace f_sad_down @ f_sad "Just make sure you're taking good care of my sister, yeah?"
    grace "This whole situation with the baby just makes me feel awful."
    anon "You shouldn't worry so much."
    anon "I always take good care of {b}Eve{/b}."
    grace "I can't help it."
    return

label button_grace_get_you_something_4:
    anon "Can I get you anything?"
    grace "Ehh, no... I don't think so."
    pause
    grace "Are you nervous about becoming a father?"
    anon @ a_behind_head "Yeah, a little."
    anon "More excited than anything though."
    grace @ f_laugh "Hehe, me too."
    pause
    grace "Just remember, we can't let {b}Eve{/b} know that you're the father."
    anon "I remember."
    grace "Thank you, {b}[firstname]{/b}."
    return

label button_grace_pregnancy_bathroom_4:
    scene expression background(544, 288, 2.) as stage at flip
    show layer master at flip
    show grace b_naked_pregnant_belly a_cover f_sad
    show anon f_flirt_low with dissolve
    grace "You can't really like my belly this much..."
    anon "Oh, I do."
    anon "I really, REALLY do."
    grace f_happy @ f_laugh "Hehehe!"
    anon "Could you maybe strike that sexy pose again?"
    grace a_shy @ f_sexy "You mean like this?"
    anon "Just like that!"
    pause
    anon f_flirt "You are so beautiful."
    grace @ f_eyeroll "Oh, c'mon... Stop it."
    anon "I mean it!"
    grace @ f_laugh "Hehehe!"
    pause
    hide anon with dissolve
    $ game.main()
    return

label button_grace_pregnancy_intro:
    scene expression player.location.background_closeup with None
    show anon
    show grace b_magic
    with dissolve
    anon "Hello, {b}Grace{/b}."
    grace "Hey, {b}[firstname]{/b}."
    return

label button_grace_pregnancy_how_are_you_feeling_0:
label button_grace_pregnancy_how_are_you_feeling_1:
    anon "How are you feeling?"
    grace f_sad "Worried, frightened, conflicted..."
    show anon f_worried
    grace "Take your pick."
    anon "Everything will be okay, I promise."
    grace f_normal @ f_laugh "Heh, I appreciate you saying that, {b}[firstname]{/b}."
    anon "But that's just blind hope, there's no way to be certain of anything."
    show grace f_sad_down
    anon f_normal "I'm certain that no matter what happens, I'll be there for you and our child."
    grace f_normal "Aww, you are like, the sweetest man ever!"
    grace "My sister is so lucky to have you."
    anon "And I'm lucky to have her."
    return

label button_grace_pregnancy_how_are_you_feeling_2:
label button_grace_pregnancy_how_are_you_feeling_3:
    anon "How are you feeling?"
    grace f_sad @ f_eyeroll "Ugh, miserable..."
    anon f_worried @ -m_talk "Hmm?"
    grace "It's the stupidest thing!"
    grace "I'm hungry, like, all the time!"
    grace f_sad_down "But then half the time I eat, I get sick and puke it all back up..."
    anon "That doesn't sound good."
    grace "{i}*Sigh*{/i} Yeah, {b}Odette{/b} thinks I need to change my diet."
    grace f_sad "She's insisting we go see the doctor about it tomorrow and double check that everything is alright."
    anon f_normal "Sounds like she's really on top of things."
    grace f_normal "Heh, yeah."
    grace "She's full of surprises, huh?"
    anon "I'll have to thank her for taking such good care of you."
    return

label button_grace_pregnancy_how_are_you_feeling_4:
    anon "How are you feeling?"
    grace f_normal @ f_eyeroll "Like I'm about to burst!"
    grace "In fact, you better watch your shoes..."
    anon @ f_laugh "Hehe!"
    grace "I thought I'd be more anxious at this point, you know?"
    grace "But for some reason, I feel serene."
    grace "Heh, maybe I just can't hear the nerves over the sound of my feet barking."
    anon @ f_confused "Your feet are hurting?"
    anon "I can rub them for you, if you want?"
    grace "No, it's okay {b}[firstname]{/b}..."
    grace "{b}Odette{/b} has been giving me full body massages every night."
    grace "She's been amazing with this whole thing."
    anon f_grumpy "Tch, she's hogging all work..."
    grace "Hehehe, does that upset you?"
    anon "No, I guess not..."
    anon "As long as you're happy, I'm happy."
    grace @ f_laugh "That's sweet, {b}[firstname]{/b}."
    show anon f_normal
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
