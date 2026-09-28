label ano26_init_tony:
    return

label ano26_init_tony.pizzeria:
    show tony f_smirk
    show anon with dissolve:
        flip
    tony "You get the bag yet?"
    anon "Yup, we're good to go."
    tony f_normal @ f_laugh "Excellent."
    tony m_talk "{b}Bring the bag with ya to the bank Tuesday morning and I'll meet ya there.{/b}"

    if 'a_baby' not in renpy.get_attributes('tony'):
        show tony a_point with {'master': dissolve}

    tony "Don't be late!"

    if 'a_baby' not in renpy.get_attributes('tony'):
        show tony a_idle -m_talk with {'master': dissolve}

    anon "I won't."
    tony "Attaboy."
    hide anon with dissolve
    return


label ano26_init_tony.bank:
    show anon with dissolve:
        xzoom -1
    tony "Ya bring the bag?"
    anon "Yeah, I got it right here, {b}Tony{/b}."
    show anon a_backpack f_looking_down with dissolve
    pause
    show anon f_normal a_duffel_give with dissolve
    tony "Beautiful!"
    show anon a_idle
    show tony a_duffel_search f_normal_down
    with dissolve
    tony "Let's see here."
    pause
    tony a_duffel_give_mask "Put this on."
    show tony a_duffel_search
    show anon a_baklava1 f_worried_low
    with dissolve
    anon "Uhh, okay..."
    show anon a_baklava2 with dissolve
    pause
    show anon f_confused a_sides of_ski_mask with dissolve
    anon "{b}Tony{/b}, why is there a green hat attached to my mask?"
    tony f_smirk "'Cause that was Luigi's mask and it's his signature look."
    anon @ -m_talk "Hmm?"
    tony f_normal_down "Man, this stuff takes me back."
    pause
    tony a_duffel_give_mini_gun "Here's your piece."
    show tony a_duffel_search
    show anon a_tiny_gun_look f_worried_low
    with dissolve
    anon @ -m_talk "..."
    show tony a_baklava1 with dissolve
    anon f_worried "Seriously?"
    tony a_baklava2 f_question "What?"
    show tony o_ski_mask a_idle with dissolve
    anon f_skeptical "This is the gun you're giving me?"
    tony f_smirk "Pretty nice, eh?"
    anon "No, it's ridiculous!"
    show tony f_sad
    anon "Did you get it in the kids department or something?"
    tony "Hey, c'mon... that was Luigi's favorite."
    anon "I feel like I'm gonna break this thing!"
    anon "I can't even get my finger inside the trigger guard..."
    tony f_smirk "Oh, don't worry about pullin' the trigger."
    anon @ -m_talk "Hmm?"
    tony f_laugh "It ain't got no bullets in it."
    anon @ f_surprised "!!!"
    anon "What do you mean, it doesn't have any bullets in it?!"
    tony f_suspicious "You plannin' on shootin' somebody tough guy?"
    anon f_worried "Well, no... but-"
    tony "Then why do you need bullets?"
    anon "I dunno..."
    show tony a_duffel_search f_normal_down with dissolve
    pause
    anon "... What if something goes wrong in there?"
    show tony a_duffel_gun1 with dissolve
    show tony f_normal a_duffel_gun2 with dissolve
    tony "Then I'll handle it."
    anon f_surprised "!!!"
    anon f_unimpressed "You're taking that?!"
    tony a_gun_down @ -m_talk "Mhmm."
    pause
    anon @ a_tiny_gun_move f_worried_low "And I get this?"
    tony f_smirk "Hey, it's not the size of the gun that matters, champ..."
    tony "... It's the caliber of the bullets."
    anon a_tiny_gun_down f_angry "But you didn't give me any bullets!!!"
    tony "You ready?"
    show anon f_surprised
    tony "Let's do this!"
    anon "Well, hold on a second... shouldn't we-"
    show tony a_gun_up f_laugh with {'master': dissolve}:
        xoffset -450
        xzoom 1
    tony "LEEEEEEEROOOOOOOOOOY!!!"
    hide tony with {'master': dissolve}
    anon f_shock @ -m_talk "..."
    anon a_tiny_gun_look f_disgusted_low @ -m_talk "..."
    anon a_tiny_gun_down f_tired "{i}*Sigh*{/i}"
    hide anon with dissolve

    scene expression background(512, 512, 3, l=L_bank_lobby)
    show tony b_casual a_gun_point o_ski_mask:
        xoffset -300
        xzoom 1
    with fade
    tony "Alright everybody, this is a hold-up!"
    show tony a_gun_cock1 with dissolve
    show tony a_gun_cock2 with fastdissolve
    show tony a_gun_cock1 with fastdissolve
    pause
    tony a_gun_point "Get on ya heads and put your hands behind ya knees!"
    show tony f_surprised
    pause
    tony a_gun_lower "What the-"
    show tony f_angry a_gun_down with dissolve:
        xoffset 200
        xzoom -1
    tony "There's nobody in here!"
    show anon f_unimpressed of_ski_mask with dissolve:
        xzoom -1
    anon "Duh."
    anon "{b}Liu{/b} said they were always dead on Tuesday mornings, remember?"
    anon "That's part of the plan."
    tony "Well, yeah... but, I thought there would at least be a couple people."
    show tony with dissolve:
        xoffset -300
        xzoom 1
    tony "Where's the fun in this?"
    anon "We're not here for fun... we're here to get the briefcase."
    tony "Aww, man."
    anon "Go tie up the security guard while I make a show of forcing {b}Liu{/b} downstairs."
    tony "Yeah, yeah..."
    hide tony with dissolve
    tony "Hey, wake up, old timer!"
    pause
    show anon a_tiny_gun_look f_disgusted_low with dissolve:
        xoffset 500
        xzoom 1
    pause
    anon f_worried "Well, here goes nothing..."
    hide anon with dissolve
    return


label ano26_talk_tony:
    scene expression background(512, 512, 3)
    show anon of_ski_mask with dissolve:
        xoffset -250
        xzoom -1
    anon @ -m_talk "( {b}Tony{/b}'s handling the security guard. )"
    show anon with dissolve:
        xoffset 250
        xzoom 1
    anon @ -m_talk "( I should start by making a show with {b}Liu{/b} for the cameras. )"
    anon @ -m_talk "( {b}I'll need to force her downstairs into the vault{/b}. )"
    hide anon with dissolve
    return


label ano26_move_tony:
    scene expression background(512, 512, 3)
    show anon of_ski_mask with dissolve:
        xoffset -250
        xzoom -1
    anon @ -m_talk "( {b}Tony{/b} will join us when he's tied up the security guard. )"
    show anon with dissolve:
        xoffset 250
        xzoom 1
    anon @ -m_talk "( Meanwhile I need to keep up this charade with {b}Liu{/b} for the cameras. )"
    anon @ -m_talk "( {b}We should head downstairs to the vault{/b}. )"
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
