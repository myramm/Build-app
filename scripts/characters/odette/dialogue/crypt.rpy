label odette_button_crypt:
    scene odette b_vamp_front
    odette "So you decided to come back, huh?"

    scene black with fasteyeshut
    pause .05

    scene odette b_vamp_front_normal with fasteyeopen
    anon "Umm... {i}*Gulp*{/i} Y-yes."
    odette "Where's {b}Evie{/b}?"
    anon "She was too afraid to come."
    odette "Aww, that's too bad."
    odette "We could have had a lot of fun together."

    scene location_crypt_side
    show odette b_vamp_sitting_cape_normal f_smirk
    show anon f_worried:
        xoffset -150
    with fade
    odette "I'll have to make do with just you then, won't I?"
    anon "Y-yeah, I guess..."
    odette "That's fine."
    show anon f_surprised_teeth a_surprised_up
    show odette b_vamp_normal f_smirk:
        xoffset -480
    odette "You're quite delicious, you know?" with hpunch
    anon f_worried a_neck_hurt "D-delicious?"
    show odette f_laugh:
        xoffset -225
    with dissolve
    odette "Hehehe!"
    show anon a_sides behind odette
    show odette f_smirk
    with {'master': dissolve}
    odette "Here, have a drink."
    anon a_behind_head "Oh, I dunno..."
    anon "... Last time it really-"
    show odette a_blood_cup_force
    show anon f_smoke a_up
    with dissolve
    anon "!!!"
    odette "Shh."
    odette "Trust me, {b}[firstname]{/b}."
    show odette a_idle
    show anon f_disgusted a_sides
    with dissolve
    anon "Hmm, it's kind of sweet this time..."
    odette "Yeah, it gets better the more you drink it."
    show anon f_skeptical
    show odette f_drink a_blood_cup_drink with {'master': dissolve}
    anon "Really?"
    anon "That's kinda weird... Isn't it?"
    odette a_idle f_smirk "You ask a lot of questions, don't you?"
    anon a_behind_head f_shy "Heh, sorry..."
    show odette f_drink a_blood_cup_drink with dissolve
    anon "I'm just a curious person by nature I suppos-"
    show odette a_blood_cup_force f_smirk
    show anon f_smoke a_up
    with dissolve
    anon "!!!"
    odette "That's it."
    odette "Drink deep, big fella."
    pause
    show odette a_idle
    show anon f_disgusted a_sides
    with dissolve
    anon "Eugh, man..."
    anon "It's so thick."
    odette @ -m_talk "Mhmm."
    show odette f_drink a_blood_cup_drink behind anon
    show anon a_surprised_hands f_surprised_low
    with dissolve
    pause
    anon "Aww, man... Not again."
    show odette a_idle f_smirk o_blood
    with dissolve
    odette "What's the matter?"
    anon a_surprised_lips f_surprised_down "Mah rips ahr numb ngin..."
    show odette a_blood_cup_throw f_laugh with dissolve
    odette "Hehe!"
    show anon f_surprised a_sides
    show odette a_blood_wipe o_empty f_smirk
    with {'master': dissolve}
    anon "Haw cam joo dun feer dis?"
    show odette a_undress1
    with dissolve
    pause
    show anon f_surprised_low
    show odette b_naked a_vamp_undress2
    with {'master': dissolve}
    odette "It effects everyone differently I suppose."
    show anon f_surprised
    show odette a_idle
    with dissolve
    pause
    label odette_button_crypt.resume:
    hide anon
    show odette b_kiss_anon:
        xoffset -500
    with dissolve
    anon "!!!"
    pause
    odette "Mmm."
    pause

    scene odette b_vamp_bite f_normal:
        xoffset 0
    show location_crypt_bite_overlay
    with fade
    odette "You smell delicious!"
    anon "Die drew?"
    odette f_lip_normal @ -m_talk "Mhmm!"

    scene location_crypt_side
    show odette b_kiss_anon:
        xoffset -500
    with fade
    pause
    anon "Ngh!"
    pause

    scene odette b_vamp_bite f_fangless:
        xoffset 0
    show location_crypt_bite_overlay
    with fade
    odette "You taste even better!"
    odette "So full of life and vigor..."

    if M_odette.is_state(S_ode02_tomb):
        anon "Wha joo ears arways dat korar?"
        odette f_curious -m_talk "Hmm?"
    else:
        anon "Joo ears ar glue-ing ngin!"
        odette "My ears?"
        show odette f_curious

    anon "Joo earss..."
    anon "Grr... {i}EYES{/i}!"
    show odette f_fangless

    if M_odette.is_state(S_ode02_tomb):
        odette "My eyes?"
        odette "What about them?"
        anon "Thar glue-ing."

    odette f_laugh "Heh, you're so adorable."

    scene location_crypt_side
    show odette b_kiss_anon:
        xoffset -500
    with fade
    pause
    anon "Hngggh!!"
    pause

    scene odette b_vamp_bite f_bite:
        xoffset 0
    show location_crypt_bite_overlay
    with fade

    if M_odette.is_state(S_ode02_tomb):
        odette "Mmm, I could just eat you up..."
        show odette f_tongue
        anon "!!!" with hpunch
        show odette f_lip
        anon "Ar dos fangs?!"
    else:
        odette "I wish {b}Eve{/b} was here to help me devour you..."
        show odette f_tongue
        anon "!!!" with hpunch
        show odette f_lip
        anon "Angs!"
        anon "Ah knu id!!"

    odette f_bite "... I want you inside me!"
    anon "Hmm?!"

    scene location_crypt_side
    show odette b_naked_vamp f_smirk:
        xoffset -400
    show anon f_worried o_boner a_surprised behind odette:
        xoffset -150
    with fade

    if M_odette.is_state(S_ode02_tomb):
        anon "W-wait, ahm nut zhur dis-"
    else:
        anon "W-wait, ah hab kuestins..."

    show anon f_surprised_down
    odette f_teeth_look a_grope "I need it now!"
    show anon f_worried

    if M_odette.is_state(S_ode02_tomb):
        anon "Mah bahdie feers word!"
    else:
        anon "A juh-"

    show anon f_surprised_teeth
    odette f_smirk a_hips "Strip."
    show odette f_laugh behind anon
    show anon b_dressed_pickup f_worried -o_boner:
        offset (-250, 50)
    with {'master': dissolve}
    anon "Uh-cuh! Uh-cuh!"
    show odette f_teeth_look
    show anon a_sides b_shirt f_worried_surprised od_dick2:
        offset (-150, 0)
    with dissolve
    pause
    show odette b_naked_pull_anon f_smirk:
        xoffset -150
    show anon b_empty:
        xoffset -125
    with {'master': dissolve}
    odette "Hurry!"
    show odette b_vamp_sitting_up:
        xoffset 0
    show anon f_side_shy b_empty:
        xoffset 216
    with {'master': dissolve}
    odette "Fuck me right here on my throne!"
    anon "Mah regs dun wurkn!"

    call scene_odette_sex_crypt.repeat
    $ unlock_scene('Odette', '03_unlocked')

    scene odette b_vamp_bite f_bite
    show location_crypt_bite_overlay as overlay
    with fade
    anon "Waz wrung wit mer?"
    odette "The seed of life, bestowed upon the unholy."
    anon "Unhoreee?!"
    odette "A ritual of darkness!"
    odette "A contract forged in passion and sealed with blood!"
    anon "Brud?"
    anon "W-wher ah joo-"
    odette "Denizens of the night!"
    odette "Come forth and serve me!"
    anon "Kun we jurs cudder?"
    show location_crypt_bite02 behind overlay
    anon "!!!" with hpunch
    show location_crypt_bite03 behind overlay with dissolve
    anon "Ooh, dat feers..."
    show location_crypt_bite04 behind overlay with dissolve
    anon "... Reer..."
    pause
    anon "... Gud."
    show location_crypt_bite04 behind overlay

    scene black with {'master': dissolve}
    odette "Hehehe!"
    "..."
    return 'sleep'
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
