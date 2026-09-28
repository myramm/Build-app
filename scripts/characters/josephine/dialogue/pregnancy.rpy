label josie_pregnancy_notify:
    scene expression player.location.background
    "{i}*Brrrzzzt* *Brrrzzzt*{/i}"

    scene expression background(608, 512, 3.8, l=L_dealership_showroom) as underlay:
        xoffset -400
    show josephine a_phone_talk f_concerned:
        xoffset -500
    show xtra3 as counter at right:
        xoffset -400

    $ renpy.dynamic(stage=player.location.background_phone)
    show expression stage as stage
    show anon f_confused with dissolve:
        flip
    anon @ -m_talk "Hmm?"
    anon a_phone f_thinking_down "It's {b}Josephine{/b}."
    show anon a_phone_talk f_normal with dissolve:
        unflip
        xoffset 500
    show expression stage as stage at phoneleft with phoneleft.show
    anon "Hello?"
    josephine f_bored "Hey, what's up, bowl cut?"
    anon f_unimpressed "{i}*Sigh*{/i} How many times do I have to ask you to stop calling me that?"
    josephine f_sexy @ f_laugh "Heh, at least one more."
    anon "Stop calling me bowl cut!!"
    josephine @ f_eyeroll "Fiiine."
    pause
    josephine "So guess what!"
    anon "What?"
    josephine "I think I'm pregnant."
    anon f_shock "!!!" with hpunch
    anon "Y-you're pregnant?!"
    show anon f_surprised_teeth
    josephine f_normal_down @ -m_talk "Mhmm."
    anon f_worried "Like... With a baby?"
    josephine f_angry "What other kind of pregnant is there?"
    anon f_skeptical "Is this a joke?"
    pause
    anon f_normal @ f_laugh "Or that troll thing you like doing?"
    josephine "No."
    josephine f_bored "I'm serious, {b}[firstname]{/b}."
    show anon f_worried
    josephine "I have a baby growing inside me and it's yours..."
    pause
    anon "And you're one hundred percent sure it's mine?"
    josephine f_angry "Hey, what is that supposed to mean?!"
    anon "N-nothing, I just-"
    josephine "What do you think I just sleep with every guy who walks into the dealership?!"
    anon "Of course not, I'm just-"
    pause
    anon "Never mind."
    anon "Are you planning to keep it?"
    josephine f_sexy @ f_laugh "Hell yeah I'm gonna keep it!"
    josephine "Are you kidding?"
    josephine "I'll get three months maternity leave!"
    anon f_hurt @ -m_talk "..."
    josephine "Plus, it's really gonna piss my dad off."
    anon f_worried "{b}Josephine{/b}, those both seem like really bad reasons to have a baby..."
    josephine "You think so?"
    anon "Yes."
    josephine f_pouting @ -m_talk "Hmm."
    pause
    josephine f_sexy "Nah, I disagree."
    anon "Maybe we should-"
    josephine "I'm having it."
    anon @ -m_talk "..."
    anon "Oh kay."
    josephine f_bored "I think you should come by today..."
    anon "I dunno, I've got some things-"
    josephine "... We can discuss names and stuff."
    anon @ -m_talk "..."
    josephine "Right now, I'm leaning towards Gaylord if it's a boy..."
    anon f_surprised "!!!"
    josephine "... Maybe Phelony if it's a girl."
    anon f_angry "You are not naming our kid Gaylord or Phelony!"
    josephine f_sexy @ f_laugh "Haha, why not?!"
    anon f_worried "I'll be down there right away!"
    josephine "Good call."
    josephine "See you soon, bowl cut!"
    show josephine a_phone with dissolve
    show expression stage as stage with {'master': phoneleft.hide}
    "{i}*Beep*{/i}"
    anon "Stop calling me bowl cut!!!"
    pause
    anon "{b}Josephine{/b}?!"
    pause
    anon f_worried "Hello?"
    anon f_thinking_down a_phone @ -m_talk "( Holy crap... )"
    anon f_surprised_teeth_low @ -m_talk "( What have I done?! )"
    hide anon with dissolve
    return True


label josie_pregnancy_notify.repeat:
    scene expression player.location.background
    "{i}*Brrrzzzt* *Brrrzzzt*{/i}"

    scene expression background(608, 512, 3.8, l=L_dealership_showroom) as underlay:
        xoffset -400
    show josephine a_phone_talk f_bored:
        xoffset -500
    show xtra3 as counter at right:
        xoffset -400

    $ renpy.dynamic(stage=player.location.background_phone)
    show expression stage as stage
    show anon f_confused with dissolve:
        flip
    anon @ -m_talk "Hmm?"
    anon a_phone f_worried_low "It's {b}Josephine{/b}."
    show anon a_phone_talk f_normal with dissolve:
        unflip
        xoffset 500
    show expression stage as stage at phoneleft with phoneleft.show
    anon "Hello?"
    josephine "Hey, {b}[firstname]{/b}."
    anon "What's going on?"
    josephine "Well, I'm pregnant again..."
    anon f_worried @ f_surprised "!!!"
    anon "Again?!"
    josephine "Yup."
    josephine "Your pull out game is weaksauce, dude..."
    anon "I assume you're going to keep it?"
    josephine "Duh."
    josephine f_sexy "Three months maternity leave."
    anon f_sad_down "{i}*Sigh*{/i} Right."
    josephine "Come hang out with me at the dealership."
    anon "Yeah, okay."
    anon "I'll see you soon."
    show josephine a_phone
    show anon f_worried_low a_phone
    with dissolve
    show expression stage as stage with {'master': phoneleft.hide}
    "{i}*Beep*{/i}"
    pause
    anon "Here we go again."
    hide anon with dissolve
    return True


label josie_pregnant_labor_1:
    scene expression player.location.background_blur
    show anon f_normal with dissolve
    anon "Looks like I got a text."
    hide anon with dissolve
    return


label josie_pregnant_labor_2:
    scene expression player.location.background_blur
    if player.location != L_map:
        show anon f_surprised a_phone with dissolve
    anon "{b}Josephine{/b} had the baby?!"
    anon "Holy crap!"
    pause
    anon "I'd better head to {b}the clinic{/b} to check on them."
    if player.location != L_map:
        hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
