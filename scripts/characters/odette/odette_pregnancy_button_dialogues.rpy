label button_odette_pregnancy_leave_stage_0:
label button_odette_pregnancy_leave_stage_1:
    anon @ a_wave "I'll leave you be."
    odette "Alright."
    odette "Give {b}Evie{/b} a kiss for me, okay?"
    anon "Will do."
    hide anon with dissolve
    return

label button_odette_pregnancy_leave_stage_2:
label button_odette_pregnancy_leave_stage_3:
    anon f_normal "I'll leave you be."
    odette f_normal "Alright."
    odette f_smirk "Give {b}Evie{/b} a kiss for me, okay?"
    anon "Will do."
    hide anon with dissolve
    return

label button_odette_pregnancy_bathroom_stage_4:
    scene expression background(544, 288, 2.) as stage at flip
    show layer master at flip
    show odette f_smirk b_naked_pregnant_belly a_towel
    show anon f_flirt with dissolve
    odette "Back again?"
    anon "I can't help it."
    anon "You're just so sexy right now..."
    odette @ f_laugh "Hehe, it's alright."
    show odette a_remove1 with dissolve
    pause
    show odette a_remove2 with dissolve
    show anon f_flirt_low
    odette "I don't mind."
    odette a_squeeze "Look as long as you want, big fella."
    pause
    hide anon with dissolve
    $ game.main()
    return

label button_odette_pregnancy_leave_stage_4:
    anon "I'll leave you be."
    odette "Alright."
    odette "Give {b}Evie{/b} a kiss for me, okay?"
    anon "Will do."
    hide anon with dissolve
    return

label button_odette_pregnancy_get_anything_0:
label button_odette_pregnancy_get_anything_1:
    anon "Can I get you something?"
    odette f_smirk "Well, a nice deep dicking would be nice..."
    odette @ f_eyeroll a_shrug "... But I sorta promised {b}Grace{/b} I wouldn't, at least not until after the baby pops out."
    anon @ f_sad_down "Oh."
    odette @ f_sad "Yeah..."
    odette "... But believe me, the second I'm able, we're fucking hard... Got it?"
    anon f_normal @ f_flirt "Heh, okay."
    return

label button_odette_pregnancy_get_anything_2:
label button_odette_pregnancy_get_anything_3:
    anon "Can I get you anything?"
    odette "Heh, not unless you know somewhere around town that sells funnel cake?"
    anon f_skeptical "Funnel cake?"
    odette "Oh my god, I've been craving it so bad!"
    odette @ f_eyeroll "You have no idea."
    show anon f_normal
    pause
    odette "Maybe with some nacho cheese dip..."
    pause
    odette f_surprised "{i}*Gasp*{/i} Or salsa!"
    anon f_disgusted_down "Okay, eww."
    odette f_sad "Yeah, I know it's gross... I can't explain it."
    pause
    odette "Ugh, my mouth is watering just thinking about it!"
    anon "Uhh, I don't know any place around here that sells funnel cake..."
    anon f_worried "I could get you donuts?"
    odette "Ugh, no... It's okay."
    anon "You sure?"
    odette "Yeah."
    odette "Thanks anyways."
    return

label button_odette_pregnancy_get_anything_4:
    anon "Can I get you anything?"
    odette f_tired "Oh man, don't go there {b}[firstname]{/b}..."
    odette "I want dick, so bad!"
    anon f_disgusted_down "Ehh."
    odette "All the toys in the world can't replace the real thing."
    anon f_worried "We could always-"
    odette f_surprised "No, don't tempt me!"
    odette "{b}Grace{/b} said we could fuck all we want once the baby is born and I wanna keep my promise."
    anon f_surprised "Alright."
    odette f_tired "I just hope it happens soon, I'm dying here..."
    odette f_tired_down "You hear that, you little shit?!"
    odette "Time's up, come out of there already!"
    anon f_worried @ f_worried_left "Hehe!"
    return

label button_odette_pregnancy_how_feeling_0:
label button_odette_pregnancy_how_feeling_1:
    anon "How are you feeling?"
    odette @ f_confused "Uhh, fine?"
    pause
    odette "Why do you ask?"
    anon @ a_point "You know, because of the baby..."
    odette "Oh, right!"
    odette "The baby."
    odette "Yeah, I'm good so far."
    odette "No worries."
    anon "Alright."
    return

label button_odette_pregnancy_how_feeling_2:
label button_odette_pregnancy_how_feeling_3:
    anon f_worried "How are you feeling?"
    odette @ f_tired "Ehh, okay I guess..."
    odette "Morning sickness is a bitch and a half!"
    anon "Oh?"
    odette f_sad "Yeah, and my tits are killing me too!"
    anon "That sucks..."
    odette f_smirk @ f_eyeroll "{i}*Sigh*{/i} Yeah."
    odette "I'm really glad {b}Grace{/b} talked me out of the nipple piercings..."
    odette @ f_laugh "Hehehe!"
    odette "But seriously, I'm good."
    show anon f_normal
    odette "She's been taking good care of me."
    anon "Well, I'm glad to hear it."
    odette "Yup."
    return

label button_odette_pregnancy_how_feeling_4:
    anon "How are you feeling?"
    odette f_tired "Ugh, I'm so ready to get this demon child out of me..."
    anon f_worried "That bad, huh?"
    odette "You have no idea!"
    odette "The little brat keeps me up all night, kicking!"
    odette "I swear to god, it's trying to play soccer with my kidneys."
    anon "That sounds rough."
    odette "{i}*Sigh*{/i} Yeah."
    return

label button_odette_pregnancy_intro_4:
    scene expression player.location.background_closeup with None
    show anon
    show odette f_smirk
    with dissolve
    anon "Hello, {b}Odette{/b}."
    odette "Hey, big fella."
    return

label button_odette_pregnancy_intro_2:
label button_odette_pregnancy_intro_3:
    scene expression player.location.background_closeup with None
    show anon
    show odette f_smirk
    with dissolve
    anon "Hello, {b}Odette{/b}."
    odette "Hey, big fella."
    return

label button_odette_pregnancy_intro_0:
label button_odette_pregnancy_intro_1:
    scene expression player.location.background_closeup with None
    show anon
    show odette f_smirk
    with dissolve
    anon "Hello, {b}Odette{/b}."
    odette "Hey, big fella."
    return

label button_odette_pregnancy_gave_birth_leave:
    anon a_idle f_normal "I'll leave you be."
    odette "Give {b}Evie{/b} a kiss for me."
    anon "Will do."
    hide anon with dissolve
    return

label button_odette_pregnancy_gave_birth_need_anything:
    anon "You guys need anything?"
    odette "Yeah, a wet nurse would be nice."
    anon @ f_worried a_behind_head "Ehh, not sure I can help you there..."
    odette "Hehe, no?"
    odette "Tsk, you got my hopes up."
    anon "Sorry."
    odette "That's alright, you can make it up to me soon."
    anon @ -m_talk "Hmm?"
    odette f_smirk "My pussy is on the mend and pretty soon, I'm going to need that dick."
    anon a_behind_head f_shy "{i}*Gulp*{/i} O-okay..."
    odette "I'm serious, {b}[firstname]{/b}..."
    show anon f_surprised
    odette "You better fuck me real hard!"
    anon "I understand."
    odette @ f_laugh "Hehehe!"
    return

label button_odette_pregnancy_gave_birth_intro:
    scene expression player.location.background_closeup with None
    show odette f_happy_down a_baby
    show anon
    with dissolve
    odette "If you don't slow down on the breastfeeding, {b}Mommy{/b}'s tits are gonna fall off..."
    odette "Yes, they are!"
    odette @ f_laugh "Hehehe!"
    anon "Hey there."
    odette f_smirk "Hey, big fella."
    return

label button_odette_pregnancy_yup:
    anon "Yeah, how are you guys doing?"
    odette "We're both doing well."
    show odette f_happy_down
    if M_odette.pregnancy.baby_gender == "boy":
        odette "I just finished feeding him."
        odette "He sure is a hungry little guy..."
        odette "... Spends half the day with my nipple in his mouth."
        anon "Heh, I can't really blame him there..."
    elif M_odette.pregnancy.baby_gender == "twins":
        odette "I just finished feeding them."
        odette "They sure are some hungry little things..."
        odette "... Spend half the day with my nipple in their mouths."
        anon "Heh, I can't really blame them there..."
    else:
        odette "I just finished feeding her."
        odette "She sure is a hungry little girl..."
        odette "... Spends half the day with my nipple in her mouth."
        anon "Heh, I can't really blame her there..."
    anon "I didn't think those breasts could get any bigger but somehow they managed it..."
    odette @ f_laugh "Hehehe!"
    pause
    anon @ a_wave "I guess I should leave you guys to rest."
    odette f_normal "Peek in on {b}Grace{/b} and make sure she's doing okay while I'm stuck in here, yeah?"
    anon "I can do that."
    odette "Thanks, {b}[firstname]{/b}."
    pause
    if M_odette.pregnancy.baby_gender == "twins":
        anon "I'll see you soon, little ones."
    else:
        anon "I'll see you soon, little one."
    odette @ f_laugh "Hehehe!"
    hide anon with dissolve
    return

label button_odette_pregnancy_bedridden:
    scene expression game.timer.image("location_hospital_baby_bed{}")
    show odette b_gown_bed f_smirk
    show anon with dissolve
    odette "Hey, big fella."
    odette "You come by to check on us again?"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
