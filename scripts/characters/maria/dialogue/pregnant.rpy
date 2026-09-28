label maria_button_pregnant:
    $ renpy.dynamic(local=flip if game.timer.is_evening() and
                                  L_maria_lounge.is_here(M_maria) else reset)

    if M_maria.pregnancy.stage <= 2:
        show anon at local with dissolve
        anon "Hey, {b}Maria{/b}."
        if not L_maria_lounge.is_here(M_maria):
            maria @ -m_talk "Hmm?"
            if M_maria.pregnancy.stage == 1:
                show maria a_spoon_hips f_normal
            show maria f_normal:
                unflip
                xoffset 0
            with dissolve
        maria "Hey there, handsome!"
    elif M_maria.outfit.get == 'apron' and not M_maria.once('pregnant_outfit'):
        show anon f_surprised_low at local with dissolve
        anon "{b}M-Maria{/b}?!!"
        if not L_maria_lounge.is_here(M_maria):
            maria @ -m_talk "Hmm?"
            show maria with dissolve:
                unflip
                xoffset 0
        show anon f_surprised
        maria "Hey, {b}[firstname]{/b}."
        pause
        maria f_sad "Something the matter?"
        anon "Y-you're naked."
        maria f_normal @ f_laugh "Heh, oh... That."
        maria "Yeah, I know."
        maria "{b}Tony{/b} likes seein' me all knocked up like this..."
        maria f_sexy "It gets him all horned up, hehe!"
        anon f_flirt_low "{i}*Gulp*{/i} I can see why..."
        maria @ f_laugh "Oh, so you like it too, huh?"
        anon @ -m_talk "Mhmm."
        maria "You want me to take the apron off?"
        jump maria_button_pregnant.flash
    elif M_maria.outfit.get == 'apron':
        show anon f_flirt at local with dissolve
        anon "Hey, {b}Maria{/b}."
        if not L_maria_lounge.is_here(M_maria):
            maria @ -m_talk "Hmm?"
            show maria with dissolve:
                unflip
                xoffset 0
        maria "Hey there, handsome!"
        show maria b_apron_pregnant_belly_wipe f_normal_down with dissolve
        pause
        show anon f_surprised_low o_boner with dissolve
        maria "You need something?"
        show maria b_magic f_normal with dissolve
    else:
        show anon f_flirt at local with dissolve
        anon "Hey, {b}Maria{/b}."
        if not L_maria_lounge.is_here(M_maria):
            maria @ -m_talk "Hmm?"
            show maria with dissolve:
                unflip
                xoffset 0
        maria "Hey there, handsome!"
        maria "You need something?"

    menu maria_button_pregnant.choice:
        "How are you feeling?":
            if M_maria.pregnancy.stage == 1:
                jump maria_button_pregnant.fine
            elif M_maria.pregnancy.stage == 2:
                jump maria_button_pregnant.garlic
            else:
                jump maria_button_pregnant.belly

        "Take the apron off?" if M_maria.outfit.get == 'apron':
            jump maria_button_pregnant.apron

        "Do you need any help?" if M_maria.pregnancy.stage < 3 and L_pizzeria_kitchen.is_here(M_maria):
            jump maria_button_pregnant.help

        "Sex." if M_maria.pregnancy.stage < 3 and L_pizzeria_kitchen.is_here(M_maria):
            jump maria_button_pizzeria.sex

        "Sex." if M_maria.pregnancy.stage > 2 and L_pizzeria_kitchen.is_here(M_maria):
            jump maria_button_pregnant.sex
        "I should go.":

            pass

    anon f_normal "I should go."
    show maria f_normal
    anon "Lots of pizza to deliver."
    maria f_normal "Heh, alright."
    maria "Be careful out there, {b}[firstname]{/b}."
    anon "Of course."
    hide anon with dissolve
    return


label maria_button_pregnant.apron:
    anon f_flirt "Can you take the apron off?"
    maria f_sexy @ f_laugh "Again?"
    jump maria_button_pregnant.flash


label maria_button_pregnant.belly:
    anon f_normal "How are you feeling?"
    maria f_normal_down "I'll be glad to get this little one out of me."
    anon "Oh?"
    maria "This damn belly keeps gettin' in my way."
    maria f_normal @ f_laugh "It's like tryin' to cook with a bag of flour strapped to me!"
    anon "Yeah, I can imagine..."
    jump maria_button_pregnant.choice


label maria_button_pregnant.fine:
    anon f_normal "How are you feeling?"
    maria f_normal @ f_eyeroll "Oh, I'm fine."
    maria "The kid's the size of a peanut right now, so it ain't no bother."
    anon "No morning sickness or anything?"
    maria "Hmm, not really?"
    maria "But I always did have a strong stomach."
    anon "Well, that's a blessing."
    jump maria_button_pregnant.choice


label maria_button_pregnant.flash:
    anon f_shy "Yes, please."
    maria @ f_laugh "Hehe!"
    maria "Okay."
    show maria a_untie_pregnant_belly with dissolve
    pause
    show maria b_naked_pregnant_belly a_idle with dissolve
    maria "Well?"
    anon "Wow!"
    pause
    anon f_flirt_low "You are so sexy!"
    maria "Thanks, handsome!"
    show maria b_magic a_untie_pregnant_belly with dissolve
    pause
    maria f_normal a_idle @ f_laugh "Anything else I can do for you?"
    jump maria_button_pregnant.choice


label maria_button_pregnant.garlic:
    anon f_normal "How are you feeling?"
    show maria f_normal
    anon "Still no morning sickness?"
    maria @ f_laugh "Nope, not a bit!"
    maria "My sense of smell is going a bit wonky but other than that, I feel great."
    anon "Your sense of smell?"
    anon "I don't understand."
    maria "My doctor says it's not unusual for a woman's sense of smell or taste to change during pregnancy."
    maria "For instance, I usually {i}LOVE{/i} the smell of garlic..."
    maria "... But right now, I can't fuckin' stand it!"
    anon f_worried @ f_skeptical "Really?"
    maria f_annoyed "Did you know there isn't a single garlic-free item on our menu?"
    anon @ -m_talk "..."
    maria "Not a single fuckin' one!"
    pause
    maria "I'm gonna have to yell at {b}Tony{/b} about this later..."
    anon "O-okay."
    anon @ -m_talk "( Poor {b}Tony{/b}... )"
    jump maria_button_pregnant.choice


label maria_button_pregnant.help:
    anon f_normal "Do you need any help?"
    maria f_normal "You remember how to work the prep station?"
    anon "Of course."
    maria "Well, you're more than welcome to do that, if you'd like."
    maria "Do a good job and there might be a reward waitin' for ya..."
    jump maria_button_pizzeria.cooking


label maria_button_pregnant.sex:
    anon f_flirt "Can we have sex still?"
    maria f_sexy "Mm, I was hopin' you'd ask..."
    maria "These hormones got me so horny, {b}[firstname]{/b}!"
    maria "I just can't stop thinkin' about that dick of yours..."

    call scene_maria_sex_kitchen.pregnant
    $ unlock_scene('maria', '03_unlocked', variant='pregnant')

    call maria_button_stage
    show maria:
        unflip
        xoffset 0
    show anon:
        xoffset 46
    with fade
    maria "Heh, I think the little one approves..."
    maria "It's goin' crazy in there!"
    anon "Really?!"
    show anon a_empty f_shy_low
    show maria apron_pregnant_belly_a_grab_mc
    with dissolve
    maria "Yeah, see for yourself."
    show maria apron_pregnant_belly_a_grab_mc2 with dissolve
    pause
    anon f_surprised_low "Whoa!"
    anon "I can feel it kicking!"
    maria @ f_laugh "Hehe, yup!"
    show anon b_empty a_idle
    show maria b_magic_kiss_mc_cheek behind anon:
        xoffset 46
    with dissolve
    pause
    show anon b_dressed f_normal
    show maria b_magic a_idle f_normal
    with dissolve
    maria "That was wonderful, {b}[firstname]{/b}."
    maria "Thank you."
    anon @ f_laugh a_behind_head "Heh, no problem!"
    hide anon with dissolve
    return 'afterglow'
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
