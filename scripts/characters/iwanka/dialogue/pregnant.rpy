label iwanka_button_pregnant:
    if M_iwanka.pregnancy.stage == 1 and not game.timer.is_morning():
        if player.location == L_boat_bridge:
            show anon b_onbed_back with dissolve:
                flip
                offset (100, 110)
        else:
            show anon b_onbed_back with dissolve:
                offset (-100, 20)
    else:
        show anon with dissolve

    if M_iwanka.pregnancy.stage < 3:
        anon "Hey, {b}Iwanka{/b}."
        iwanka f_excited "There's my baby daddy!"
        anon @ f_surprised "!!!"
        anon "I guess I am, huh?"
        iwanka @ f_laugh "Hehe!"
    else:

        iwanka "Ugh, don't look at me..."
        anon f_worried "Huh?"
        iwanka "I'm hideous!"
        anon "No, you're not."
        anon f_shy "You look great!"
        iwanka "Don't lie to me, {b}[firstname]{/b}..."
        iwanka "I look like I swallowed a beach ball."

    menu iwanka_button_pregnant.choice:
        "How are you feeling?":

            if M_iwanka.pregnancy.stage == 1:
                jump iwanka_button_pregnant.advice
            elif M_iwanka.pregnancy.stage == 2:
                jump iwanka_button_pregnant.bulemia
            else:
                jump iwanka_button_pregnant.horny

        "Can I get you anything?" if not M_iwanka.pregnancy.stage < 3:
            jump iwanka_button_pregnant.cheese
        "{b}Melonia{/b}.":

            if M_iwanka.pregnancy.stage == 1:
                jump iwanka_button_pregnant.grandma
            elif M_iwanka.pregnancy.stage == 2:
                jump iwanka_button_pregnant.clueless
            else:
                jump iwanka_button_pregnant.parents
        "I should go.":

            pass

    if M_iwanka.pregnancy.stage < 3:
        anon f_normal "I should go."
        iwanka f_normal "Is my mother still making you clean things?"
        anon "Yeah, but it's fine."
        anon "I need the money."
        iwanka f_disgusted "Eugh, like fucking her isn't work enough..."
        anon "I'll see you later, okay?"
        iwanka "Yeah, okay."
    else:

        anon f_normal @ a_wave "I should go."
        iwanka f_normal "Alright, but keep your phone with you."
        iwanka "This baby is gonna drop any day now."
        anon "I'll be there."

    hide anon with dissolve
    return


label iwanka_button_pregnant.advice:
    anon f_normal "How are you feeling?"
    iwanka f_excited "My friend Chelsea said I should be experiencing lots of morning sickness by this point..."
    iwanka "... But so far so good."
    anon "Chelsea?"
    iwanka "Yeah, she's an old friend from college."
    iwanka "Her father was a mayor in a small town too."
    iwanka "So we kinda just, I dunno, clicked."
    anon @ f_laugh "That's awesome!"
    iwanka "She's had a bunch of babies so I've been asking her for advice."
    anon "Well, I'm happy to hear you have someone advising you."
    jump iwanka_button_pregnant.choice


label iwanka_button_pregnant.bulemia:
    anon f_normal "How are you feeling?"
    iwanka f_normal "I'm fine."
    anon "Are you sure?"
    anon "Still not getting any morning sickness?"
    iwanka "Yeah, I am but it's not so bad."
    anon "Really?"
    iwanka @ f_eyeroll "Please, {b}[firstname]{/b}, I went through a bulimic phase in high school..."
    iwanka "... Puking is nothing new to me."
    anon f_worried "That's-"
    anon "Umm, okay."
    iwanka "Chelsea says I should be experiencing weird food cravings soon."
    anon f_normal "Oh, yeah?"
    iwanka "She said for her, it's usually cheese puffs dipped in maple syrup."
    anon f_disgusted "Eww, that's disgusting!"
    iwanka @ f_laugh "Haha!"
    iwanka "Don't worry, I wouldn't be caught dead eating something that gross."
    jump iwanka_button_pregnant.choice


label iwanka_button_pregnant.cheese:
    anon f_normal "Can I get you anything?"
    iwanka f_normal "Actually, now that you mention it."
    iwanka "Could you get me some of those cheese puff thingies?"
    anon "You want cheese puffs?"
    iwanka "Yeah."
    pause
    iwanka "And some maple syrup."
    anon f_disgusted "Wait a second..."
    iwanka f_annoyed "Don't judge me!"
    jump iwanka_button_pregnant.choice


label iwanka_button_pregnant.clueless:
    anon f_worried "Have you told {b}Melonia{/b} yet?"
    iwanka f_normal "Nope."
    anon "{b}Iwanka{/b}, she's going to figure it out..."
    iwanka "I doubt it."
    anon "You're already starting to show and this time next week you'll-"
    iwanka f_surprised "Oh."
    iwanka "Em."
    iwanka "GEE!!!"
    iwanka f_annoyed "Are you saying I'm fat?!"
    anon f_worried @ f_shock "What?!"
    anon "N-no, that's not-"
    iwanka "You better not be saying I'm fat!"
    iwanka "I will absolutely lose my shit!"
    anon f_shy "Seriously, you look great, {b}Iwanka{/b}!"
    iwanka @ -m_talk "Mhmm."
    jump iwanka_button_pregnant.choice


label iwanka_button_pregnant.grandma:
    anon f_worried "Have you told {b}Melonia{/b} she's going to be a grandmother?"
    iwanka f_normal "Are you joking?"
    iwanka @ f_eyeroll "She'll just lecture me about being irresponsible and then tell me to get rid of it."
    anon "You think so?"
    iwanka "I know so."
    anon "Well, you have to tell her eventually..."
    iwanka "That's your opinion."
    jump iwanka_button_pregnant.choice


label iwanka_button_pregnant.horny:
    anon f_worried "How are you feeling?"
    iwanka f_bored "Horny."
    iwanka "And not like, regular horny either..."
    iwanka "... Weird horny."
    anon "Huh?"
    iwanka "I keep having these lucid dreams involving octopuses."
    anon f_surprised_teeth @ f_shock "Octopuses?!"
    iwanka "You know, like... Doing things..."
    anon f_worried "Things?"
    iwanka "... With their tentacles."
    anon "You're having sex dreams about octopuses?!"
    iwanka "I can't get it out of my head!"
    pause
    iwanka "I told you it was weird."
    jump iwanka_button_pregnant.choice


label iwanka_button_pregnant.parents:
    anon f_worried "{b}Melonia{/b} has to have figured it out by now, right?"
    iwanka f_bored "No."
    anon @ f_surprised "Seriously?!"
    anon "How could she not have noticed the belly?"
    iwanka "Umm, because she doesn't pay attention to me..."
    iwanka f_annoyed "I told you that!"
    anon "Still though."
    anon "It's her grandchild, we should tell her."
    iwanka "I suppose you wanna go down to the prison and tell my father too?"
    anon @ -m_talk "..."
    iwanka "Yeah, I didn't think so."
    iwanka "My parents suck, {b}[firstname]{/b}."
    iwanka "I accepted that a long time ago and there's no reason for you to be bothered by it."
    jump iwanka_button_pregnant.choice
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
