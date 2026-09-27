label debXX_call_home_garage_car:
    scene expression background(608, 512, 3.8, l=L_dealership_showroom) as underlay:
        xoffset 150
    show josephine b_dressed_bored:
        xoffset 150
    show xtra3 as counter at right:
        xoffset 150

    $ renpy.dynamic(stage=background(512, 400, 1.6))
    show expression stage as stage
    show anon a_phone f_shy_low with dissolve:
        flip
        xoffset -500
    show anon a_phone_talk f_normal with dissolve
    "{i}*Dering* *Dering*{/i}"

    show expression stage as stage at phoneright with phoneright.show
    "{i}*Dering* *Dering*{/i}"

    anon f_worried @ -m_talk "( I hope I have the correct number... )"

    "{i}*Dering* *Dering*{/i}"

    show josephine a_phone b_dressed f_eyeroll with dissolve:
        flip
        xoffset 575
    josephine f_angry @ f_eyeroll "Urgh..."

    "{i}*Ring* *Ri-*{/i}"

    show josephine f_angry_down a_phone_cord_talk2 with dissolve

    if M_anon.finished_state(S_ano09_blow):
        jump debXX_call_home_garage_car.friends
    elif M_anon.finished_state(S_ano05_deal):
        call debXX_call_home_garage_car.contact
    else:
        call debXX_call_home_garage_car.unknown

    show josephine f_normal_down
    anon f_normal @ f_brag_closed "Oh bagus."

    anon "I was worried I might have the wrong number."

    josephine @ -m_talk "..."
    show anon f_worried
    pause
    anon "Are you still there?"

    josephine "Bisakah saya membantu Anda dengan sesuatu?"

    anon "My friend's car needs a new engine and I'd like you to check the warranty."

    josephine f_normal_down "Name?"

    anon "Nama saya {b}[firstname]{/b}."

    josephine @ f_eyeroll "Not {i}your{/i} name..."

    josephine f_bored "I need the name on the account."

    anon @ f_shy "Oh maaf."

    anon f_normal "It's {b}[deb_name] Cummings{/b}."

    josephine f_normal_down a_phone_cord_talk "Astaga..."

    pause
    josephine "You still at 240 Cookie Street?"

    anon "Eh ya."

    pause
    josephine @ -m_talk "Hmm."

    josephine "License plate, \"DTF M0M\"..."

    josephine f_bored "Dengan serius?"

    anon @ f_grin -m_talk "..."
    josephine f_normal_down "It looks like the warranty expired three months ago."

    anon f_worried "Ah, crap."

    anon "Apa kamu yakin?"

    josephine f_bored "What, do you think I can't read an expiration date?"

    show josephine a_phone_cord_talk2 f_normal_down
    pause

    if M_anon.finished_state(S_ano05_deal):
        anon "Well, is there anything you can do?"

    else:
        anon "Well, is there anything you can do, Miss... Umm?"

        josephine "{b}Yosephine{/b}."

        anon "Oh, that's a nice name."

        josephine "..."
        anon "Is there anything you can do, {b}Josephine{/b}?"


    josephine "We can have our mechanic swing by to take a look but it'll cost you an arm and a leg..."

    anon "Berapa harganya?"

    josephine f_bored "Dude, I dunno..."

    pause
    josephine f_normal_down @ f_eyeroll "... For an entirely new engine, probably in the neighborhood of eight thousand dollars."

    anon f_shock "Eight thousand dollars?!"

    anon "{b}[deb_name]{/b} can't afford that!"

    show anon f_surprised_teeth
    josephine @ -m_talk "..."
    anon f_sad_down "Besar."

    anon "Thanks for all the help..."

    show anon a_phone with dissolve
    show expression stage as stage with {'master': phoneright.hide}
    "{i}*Bip*{/i}"

    show anon a_idle with dissolve:
        unflip
        xoffset 0
    pause
    anon @ -m_talk "( What the heck am I going to do now? )"

    anon @ -m_talk "( I might have to bite the bullet and pay for the engine repairs myself... )"

    anon @ -m_talk "( ... Or maybe I can convince her to help me? )"

    pause
    anon @ -m_talk "( Either way, I'll have to call back her to sort this out. )"

    hide anon with dissolve
    return


label debXX_call_home_garage_car.contact:
    josephine f_bored "Halo?"

    anon "{b}Yosephine{/b}?"

    show josephine f_normal_down
    josephine @ -m_talk "Hmm?"

    return


label debXX_call_home_garage_car.friends:
    josephine f_bored "Halo?"

    anon "{b}Yosephine{/b}?"

    josephine f_sexy "{b}[firstname]{/b}?"

    anon "Hai."

    josephine a_phone_cord_talk "I wasn't expecting you to be on the other end of this line..."

    josephine "Apa yang terjadi?"

    anon "Well, actually... I've got a bit of a problem I was hoping you could help me with?"

    josephine "Heh, I've never been propositioned over the phone before..."

    anon f_confused @ -m_talk "Hmm?"

    josephine "Is this like a phone sex thing?"

    anon f_surprised "No, nothing like that!"

    pause
    anon f_shy "I mean, maybe later... That would be awesome!"

    josephine "Hehe, what's the problem then?"

    anon f_worried "My friend's car needs a new engine and I'd like you to check the warranty."

    josephine f_normal "Okay, that's easy enough."

    josephine f_normal_down a_phone_cord_talk "Name?"

    anon "{b}[firstname]{/b}?"

    anon f_normal "What, did you forget?"

    josephine f_eyeroll "Not {i}your{/i} name..."

    josephine @ f_sexy "I need the name on the account, stupid."

    anon "Oh benar..."

    anon "Maaf."

    anon "It's {b}[deb_name] Cummings{/b}."

    show josephine f_normal_down
    pause
    josephine "You still at 240 Cookie Street?"

    anon "Eh ya."

    pause
    josephine @ -m_talk "Hmm."

    josephine "License plate, \"DTF M0M\"..."

    josephine f_bored "Dengan serius?"

    anon @ f_grin -m_talk "..."
    josephine f_normal "It looks like the warranty expired three months ago."

    anon f_worried "Ah, crap."

    anon "Apa kamu yakin?"

    josephine "That's what the computer says."

    anon "Apa yang akan saya lakukan sekarang?"

    label debXX_call_home_garage_car.redux:
    josephine "Anda tahu apa?"

    josephine "I've got this."

    show josephine f_normal_down
    anon f_surprised "Hah?"

    josephine "Yeah, I'll just extend the warranty."

    anon "You can do that?"

    josephine f_sexy "Bitch, I can do whatever the hell I want!"

    josephine "What's my dad gonna do, fire me?"

    show josephine f_normal_down
    anon f_normal "That's exactly what you want him to do."

    pause
    josephine "Di sana."


    if game.timer.is_dark():
        josephine f_sexy "Someone will be out to service the car first thing tomorrow."

    else:
        josephine f_sexy "Someone will be out to service the car later today."


    anon "You're amazing, {b}Josephine{/b}."

    josephine @ f_laugh "Aku tahu."

    josephine "Ada lagi?"

    anon "Nope, that was it."

    josephine "You can repay me by coming back to the dealership and keeping me company."

    anon "Bisa."

    anon "Sampai berjumpa lagi."

    josephine "Nanti, {b}[firstname]{/b}."

    show josephine a_idle f_sexy_down
    show anon a_phone
    with dissolve
    show expression stage as stage with {'master': phoneright.hide}
    "{i}*Bip*{/i}"

    show anon a_idle with dissolve:
        unflip
        xoffset 0
    pause
    anon f_grin @ -m_talk "( It really is all about who you know! )"

    hide anon with dissolve
    return


label debXX_call_home_garage_car.unknown:
    josephine f_bored "{i}*Sigh*{/i} Hello?"

    anon "Halo?"

    anon f_skeptical "Is this the Saga Car Dealership?"

    josephine @ -m_talk "Mhmm."

    return


label debXX_cash_home_garage_car:
    scene expression background(608, 512, 3.8, l=L_dealership_showroom) as underlay:
        xoffset 150
    show josephine b_dressed_bored:
        xoffset 150
    show xtra3 as counter at right:
        xoffset 150

    $ renpy.dynamic(stage=background(512, 400, 1.6))
    show expression stage as stage
    show anon f_worried with dissolve
    anon @ -m_talk "( Maybe we can work something out this time? )"

    show anon a_phone f_shy_low with dissolve:
        flip
        xoffset -500
    pause 1
    show anon a_phone_talk f_normal with dissolve
    "{i}*Dering* *Dering*{/i}"

    show expression stage as stage at phoneright with phoneright.show
    "{i}*Dering* *Dering*{/i}"

    show josephine a_phone b_dressed f_eyeroll with dissolve:
        flip
        xoffset 575
    josephine f_angry @ f_eyeroll "Urgh..."

    "{i}*Ring* *Ri-*{/i}"

    show josephine f_angry_down a_phone_cord_talk2 with dissolve

    josephine "Halo?"

    anon "{b}Yosephine{/b}?"


    if M_anon.finished_state(S_ano09_blow):
        jump debXX_cash_home_garage_car.friends

    josephine @ -m_talk "Hmm?"

    anon "Oh bagus."

    anon "Hey, it's me again..."

    josephine @ -m_talk "..."
    show anon f_worried
    pause
    anon "You know, the guy who needed the engine repair on my friend's vehicle?"

    josephine @ f_bored "Do you have the money?"


    menu:
        "Yes. ($8,000)":
            jump debXX_cash_home_garage_car.cash
        "Are you sure there's nothing you can do?":

            jump debXX_cash_home_garage_car.stat

    return


label debXX_cash_home_garage_car.cash:
    if not player.has_money(8000):
        anon "You said it was eight thousand?"

        josephine @ f_bored "Ya."

        anon "Alright, I'll call back when I have it."

        show anon a_phone with dissolve
        show expression stage as stage with {'master': phoneright.hide}
        "{i}*Bip*{/i}"

        hide anon with dissolve
        return

    anon f_normal "Ya?"

    josephine a_phone_cord_talk f_surprised "Wait, you do?"

    anon @ f_laugh "Eh ya."

    josephine "I wasn't expecting that..."

    anon "When can we expect the mechanic?"


    if game.timer.is_dark():
        josephine f_normal_down "I'll have someone out there first thing tomorrow."

    else:
        josephine f_normal_down "I'll have someone out there later today."


    anon f_normal "Terima kasih."

    show josephine a_idle f_normal_down
    show anon a_phone
    with dissolve
    show expression stage as stage with {'master': phoneright.hide}
    "{i}*Bip*{/i}"

    show anon a_idle with dissolve:
        unflip
        xoffset 0
    pause
    anon a_money @ f_shy_low -m_talk "( I'll just leave this with the car for when they get here. )"

    hide anon with dissolve
    $ player.spend_money(8000)
    return True


label debXX_cash_home_garage_car.friends:
    josephine f_sexy "{b}[firstname]{/b}?"

    anon "Hai."

    josephine a_phone_cord_talk "I wasn't expecting you to be on the other end of this line..."

    josephine "Apa yang terjadi?"

    anon "Remember when I called about the warranty on my friend's car?"

    josephine "Oh right..."

    josephine @ f_laugh "\"DTF M0M\" ..."

    anon "That's the one-"

    call debXX_call_home_garage_car.redux
    return True


label debXX_cash_home_garage_car.stat:
    anon "Are you sure there's nothing you can do?"

    josephine f_concerned "Seperti apa?"

    anon @ f_sad_down "Aku tidak tahu."

    anon f_skeptical "Can't you like, extend the warranty or something?"

    josephine f_normal_down "Heh, I mean, I {i}could{/i} do that..."

    josephine "But why should I?"


    if player.stats.chr() < 8:
        anon f_shy "B-because you're a nice lady?"

        $ display.toast(chr_fail)
        josephine @ f_bored "Wrong."

        anon f_worried "Ah, kawan..."

        josephine "Better luck next time."

        show josephine a_idle with dissolve
        show expression stage as stage with {'master': phoneright.hide}
        "{i}*Bip*{/i}"

        anon f_surprised_down a_phone @ -m_talk "( She hung up! )"

        anon f_sad_down @ -m_talk "( Oh well... It was worth a shot... )"

        hide anon with dissolve
        return

    anon f_skeptical "Because it will piss off your boss?"

    if M_anon.finished_state(S_ano05_deal):
        josephine f_eyeroll "Nice try, bow-"

    else:
        josephine f_eyeroll "Nice try-"

    josephine a_phone_cord_talk f_surprised "Wait, what did you say?"

    anon f_normal "You obviously don't like working there..."

    josephine f_normal "No, I fucking hate it!"

    anon "Yeah, I can tell."

    anon "Why not stick it to the company then?"

    josephine @ -m_talk "..."
    josephine f_sexy "Anda tahu apa?"

    $ display.toast(chr_pass)
    josephine "Why not."

    josephine "Screw this place!"

    show josephine f_normal_down
    anon @ f_laugh "Heh, awesome."


    if game.timer.is_dark():
        josephine f_normal_down "I'll have someone out there first thing tomorrow."

    else:
        josephine f_normal_down "I'll have someone out there later today."


    anon @ f_laugh "Terima kasih banyak!"

    show anon a_phone
    show josephine a_idle
    with dissolve
    show expression stage as stage with {'master': phoneright.hide}
    "{i}*Bip*{/i}"

    hide anon with dissolve
    return True
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
