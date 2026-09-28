label jenny_pregnancy_baby_need_anything:
    show anon f_normal
    anon "You guys need anything?"
    show jenny f_happy_down
    jenny "No, we're good."
    jenny "Aren't we?"
    jenny "Yes, we are!"
    jenny "We're wonderful!"
    return

label jenny_pregnancy_baby_looking_forward_daycare:
    show anon f_normal
    anon "Looking forward to daycare?"
    show anon f_surprised
    show jenny f_angry
    jenny "Fuck no!"
    show jenny f_upset
    jenny "I hate thinking about leaving them with a stranger."
    anon f_worried "It won't be a stranger, {b}[jen_name]{/b}..."
    anon f_normal "{b}[deb_name]{/b} and {b}Diane{/b} know the lady running the place."
    anon "I've heard she's really nice!"
    jenny "I don't care if she's Mary fucking Poppins, I don't like leaving my kid with her!"
    anon "Heh, I never took you for the momma bear type..."
    show jenny f_happy_down
    jenny "Yeah, well... I am."
    anon f_laugh "Haha!"
    show anon f_normal
    return

label jenny_pregnancy_baby_leave:
    show anon f_normal
    anon "I'll leave you be."
    show jenny f_happy_down
    jenny "Say bye to {b}Daddy{/b}..."
    jenny "Bye-bye, {b}Daddy{/b}!"
    anon f_laugh "Heh, bye-bye!"
    hide anon with dissolve
    return

label jenny_pregnancy_debbie_driving_crazy:
    show anon f_worried
    anon "{b}[deb_name]{/b} is driving you crazy?"
    show jenny f_eyeroll
    jenny "Oh my god, yes!!"
    show jenny f_upset
    anon "How so?"
    jenny "She's always following me around, trying to get me to eat..."
    jenny "It's annoying!!"
    anon "It's just her maternal instincts kicking in, {b}[jen_name]{/b}."
    anon "She wants to take care of her daughter and grandchild."
    show jenny f_eyeroll
    jenny "Yeah, yeah, I know."
    show jenny f_upset
    jenny "I just wish she'd shut up about the whole being a grandmother thing..."
    jenny "... I swear, she's sappier than you are about this stuff."
    anon f_normal "Heh, I think it's sweet."
    show jenny f_eyeroll
    jenny "Ugh, whatever."
    show jenny f_upset
    return

label jenny_pregnancy_can_i_get_you_something_3:
    show anon f_worried
    anon "Can I get you something?"
    show jenny f_upset
    jenny "Like what?!"
    anon f_normal "I dunno, a foot massage or something?"
    show anon f_grin
    show jenny f_gross
    jenny "Eww, no!"
    jenny "I don't even wanna show you my feet right now, they're gigantic!"
    anon f_flirt "Really, I won't mind, we can just-"
    jenny "No!"
    anon f_skeptical "Okay, no foot rub."
    show anon f_worried
    show jenny f_upset
    pause
    anon "Something to eat maybe?"
    show jenny f_normal a_magic_sit_stand_belly_touch with dissolve
    jenny "Oh, that would be awesome!"
    jenny "I have been craving some really weird stuff though..."
    anon "What do you mean?"
    show jenny f_upset
    jenny "You'll just laugh at me."
    anon f_normal "No, I won't."
    jenny @ -m_talk "..."
    anon "I promise!"
    show jenny f_sad
    jenny "Alright."
    show jenny f_eyeroll
    jenny "{i}*Sigh*{/i} Chalk."
    show jenny f_sad
    anon f_shock "What?!"
    show anon f_surprised_teeth
    show jenny f_normal
    jenny "I can't explain it... I just really wanna bite into a big hunk of chalk..."
    show jenny f_gross
    pause
    jenny "It's weird right?"
    anon "..."
    jenny "Do they make edible chalk?"
    anon f_laugh "Hahaha!"
    show jenny f_angry a_magic_sit_stand_crossed with dissolve
    pause
    anon f_worried "I'm sorry, I just wasn't prepared for-"
    jenny "You said you wouldn't laugh!"
    anon "I know, I'm really sorry!"
    anon f_normal "No, {b}[jen_name]{/b}, I don't think they make edible chalk..."
    show jenny f_sad
    jenny "Hmmph, well they should!"
    anon f_worried "You really wanna eat chalk?!"
    jenny "Yes."
    show jenny f_grin a_magic_sit_stand_belly_touch with dissolve
    jenny "... And marshmallows."
    anon f_laugh "Okay, marshmallows we can definitely do."
    anon "I'll get you some!"
    show anon f_normal
    show jenny f_normal
    jenny "With pickles!"
    anon f_surprised @ -m_talk "..."
    jenny "Oh, and mustard!"
    anon f_worried "Eugh, okay."
    show jenny f_eyeroll
    jenny "But not regular mustard."
    show jenny f_grin a_magic_sit_stand_crossed with dissolve
    jenny "I want that expensive Dijon stuff!"
    anon "R-right."
    anon "I'll get right on that."
    anon @ -m_talk "( Oh my god, that's so disgusting!!! )"
    return





label jenny_pregnancy_about_debbie:
    show anon f_worried
    anon "About {b}[deb_name]{/b}..."
    show jenny f_grin
    jenny "I can't believe she almost bought that bullshit story..."
    anon "I don't understand why we can't just tell her the truth?"
    show jenny f_angry
    jenny "You wanna tell my mom that you're the father?!"
    jenny "She would totally flip out, you moron!"
    anon "I don't think she'd-"
    show anon f_surprised
    jenny "No fucking way, {b}[firstname]{/b}!"
    anon f_worried "{b}[jen_name]{/b}..."
    jenny "I SAID NO!"
    anon f_tired "{i}*Sigh*{/i}"
    show anon f_worried
    return

label jenny_pregnancy_can_i_get_you_something:
    show anon f_worried
    anon "Can I get you something?"
    show jenny f_eyeroll
    jenny "Yeah, a time machine."
    show jenny f_upset
    anon f_confused "Huh?"
    show anon f_worried
    show jenny f_angry
    jenny "So I can go back in time and make you pull out!"
    show jenny f_gross
    anon @ -m_talk "..."
    return

label jenny_pregnancy_are_you_still_mad:
    show anon f_worried
    anon "Are you still mad?"
    show jenny f_angry a_magic_sit_stand_crossed with dissolve
    jenny "Of course I'm mad, you idiot!"
    show jenny f_upset
    jenny "Do you realize how much this is going to cost me?"
    anon f_confused "Huh?"
    show anon f_worried
    jenny "Who's going to watch my shows if I get fat?!"
    anon "You're not going to get fat, {b}[jen_name]{/b}..."
    anon "... And even if you do, some people are into that."
    show jenny f_eyeroll
    jenny "Ugh, some freaks you mean."
    show jenny f_upset
    anon "Everything is going to be fine, you'll see."
    show jenny f_phone_upset a_magic_sit_stand_phone with dissolve
    jenny "Whatever."
    return

label jenny_pregnancy_leave:
    show anon f_worried
    anon "I'll leave you be."
    show jenny f_eyeroll
    jenny "Fucking finally!"
    show jenny f_phone_upset
    anon "You'll let me know if you need anything?"
    show jenny f_upset
    jenny "Yeah, yeah, I'll let you know."
    jenny "Go away."
    show jenny f_phone_upset
    anon f_tired "{i}*Sigh*{/i}"
    hide anon with dissolve
    return

label jenny_pregnancy_you_doing_ok_1:
    show anon f_worried
    anon "You doing okay?"
    show jenny f_phone_upset
    jenny "I'm fine."
    pause
    anon "You sure?"
    anon "W-we can talk about it, if you-"
    show anon f_surprised
    if randomizer() > 50:
        show jenny f_angry
        jenny "Oh my god, shut up!"
        jenny "My mom might hear you, moron!"
        anon f_worried "I'm just saying-"
        show jenny f_eyeroll
        jenny "I know what you're saying, {b}[firstname]{/b}!"
        show jenny f_upset
        jenny "Seriously, I'm fine!"
    else:
        show jenny f_upset
        jenny "I said I'm fine, {b}[firstname]{/b}!"
    jenny "Drop it."
    show jenny f_phone_upset
    anon "O-okay."
    return

label jenny_pregnancy_you_doing_ok_2:
    show anon f_worried
    anon "You doing okay?"
    show jenny f_gross
    jenny "No, I'm not okay!"
    jenny "This entire thing sucks!"
    anon "What's the matter?!"
    show jenny f_eyeroll
    jenny "Hmm, well, let's see..."
    show jenny f_gross
    jenny "... For starters, I puke my guts out every fucking morning."
    jenny "Then I eat like a cow because your idiot offspring is determined to make me fat."
    show jenny f_upset
    anon "{b}[jen_name]{/b}..."
    jenny "I'm uncomfortable, pretty much all day."
    show jenny f_angry
    jenny "Oh, and I wake up and pee like four times a night now!"
    show jenny f_gross
    anon "I'm sorry?"
    show jenny f_angry
    jenny "You should be sorry!"
    jenny "This is all your fault, asshole!"
    show jenny f_gross
    return

label jenny_pregnancy_you_doing_ok_3:
    show anon f_worried
    anon "You doing okay?"
    show jenny f_gross
    jenny "No, I'm not okay!"
    show jenny f_angry a_magic_sit_stand_belly_touch with dissolve
    jenny "Just look at what you did to me, {b}[firstname]{/b}!"
    jenny "I'm a fucking whale!"
    anon "You're not a whale, {b}[jen_name]{/b}..."
    show jenny f_sad
    jenny "Yes, I am!"
    anon f_normal "No, you're beautiful..."
    jenny "Beautiful?!"
    show anon f_worried
    show jenny f_angry
    jenny "What are you, retarded?!"
    anon "You're carrying our child... I think it's beautiful."
    show jenny f_eyeroll a_magic_sit_stand_crossed with dissolve
    jenny "Oh my god, you are the worst!"
    show jenny f_sad
    pause
    jenny "I just want this thing out of me!"
    return

label jenny_button_pregnancy_stage_1:
    if player.location == L_home_diningroom:
        scene expression game.timer.image("dining_room{}")
        show expression "characters/jenny/layeredimage/jenny_breakfast_table.png" zorder 2
        show anon b_dinner_sitting_look_left f_normal zorder 1
    else:
        scene expression player.location.background_closeup
        show anon f_normal zorder 1
    show jenny f_phone_upset a_magic_sit_stand_phone b_magic_sit_stand_dressed zorder 1
    anon "Hey."
    show anon f_worried
    jenny @ -m_talk "..."
    return

label jenny_button_pregnancy_stage_2:
    if player.location == L_home_diningroom:
        scene expression game.timer.image("dining_room{}")
        show expression "characters/jenny/layeredimage/jenny_breakfast_table.png" zorder 2
        show anon b_dinner_sitting_look_left f_normal zorder 1
    else:
        scene expression player.location.background_closeup
        show anon f_normal zorder 1
    show jenny f_phone_upset a_magic_sit_stand_phone b_magic_sit_stand_dressed zorder 1
    with dissolve
    anon "Hey, {b}[jen_name]{/b}."
    show jenny f_eyeroll
    jenny "Ugh, what do you want, {b}[firstname]{/b}?"
    show jenny f_gross a_magic_sit_stand_crossed with dissolve
    return

label jenny_button_pregnancy_stage_3:
    if player.location == L_home_diningroom:
        scene expression game.timer.image("dining_room{}")
        show expression "characters/jenny/layeredimage/jenny_breakfast_table.png" zorder 2
        show anon b_dinner_sitting_look_left f_worried zorder 1
    else:
        scene expression player.location.background_closeup
        show anon f_worried zorder 1
    show jenny f_phone_upset a_magic_sit_stand_phone b_magic_sit_stand_dressed zorder 1
    anon "Hey, {b}[jen_name]{/b}."
    show jenny f_surprised a_magic_sit_stand_crossed with dissolve
    jenny "Shit, you scared me!"
    show jenny f_upset
    jenny "I thought you were my mom..."
    jenny "... She's driving me crazy."
    show jenny f_gross
    return

label jenny_button_pregnancy_holding_baby:
    scene expression player.location.background_closeup
    $ player.last_baby_gender = M_jenny.pregnancy.baby_gender
    show jenny a_baby b_casual f_happy_down
    show anon f_normal with dissolve
    jenny "You are just so beautiful, aren't you little one?!"
    jenny "You definitely got your looks from your mommy."
    jenny "Which is lucky because your daddy is basically a bridge troll."
    anon f_worried "Hey!"
    show jenny f_laugh
    jenny "Hahahaah!"
    show jenny f_happy_down
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
