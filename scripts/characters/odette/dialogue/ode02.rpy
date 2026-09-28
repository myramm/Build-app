label ode02_init_odette:
    odette f_smirk "You're not gonna chicken out on me, are you?"
    anon f_worried "{i}*Gulp*{/i} N-no."
    anon "I'm just making sure you still wanna do it..."
    odette "Well, of course."
    show anon f_hurt
    pause
    odette @ f_laugh "Heh, don't worry {b}[firstname]{/b}... It'll be fun."
    show anon f_worried
    odette "Just {b}meet me there during the next full moon{/b}, okay?"

    $ renpy.dynamic(ttl=game.timer.days_until_lunar(.5))
    $ renpy.dynamic(day=game.timer.dayOfWeek(delta=ttl, full=True))

    if game.timer.is_fullmoon():
        odette @ f_wink "By which I mean tonight!"
        anon f_surprised "Y-yeah, okay..."
    elif ttl > 21:
        odette @ f_sad "The last one only just ended, so it'll be a few weeks."
        anon "Oh, okay."
    elif ttl > 14:
        odette @ f_pouting "The last one was only a week or so ago, so the next won't be for a few weeks yet."
        anon "Yeah, okay."
    elif ttl > 7:
        odette @ f_shy "The next one is just over a week away, I'm so excited!"
        anon "That soon?"
        odette @ f_laugh "Worried, big fella?"
    elif ttl > 1:
        odette "The next one is on [day], I hope you're ready!"
        anon f_shy "Do I have a choice?"
        odette @ f_laugh "Hehe, nope!"
    else:
        odette @ f_wink "Oh, and {i}spoiler alert{/i}: That's tomorrow!"
        anon f_surprised @ -m_talk "{i}*Gulp*{/i}"

    show anon f_normal
    return


label ode02_tomb_odette:
    scene odette b_vamp_front f_vamp_tongue
    anon "( !!! )" with hpunch
    anon "{b}Odette{/b}?"
    anon "Is that you?"

    scene black with fasteyeshut
    pause .05

    scene odette b_vamp_front_normal with fasteyeopen
    odette "Hey there, big fella..."
    odette "... Nice of you to finally join me in my humble abode."

    scene location_crypt_side
    show odette b_vamp_sitting_cape_normal f_smirk
    show anon f_worried:
        xoffset -150
    with fade
    anon "Your humble abode?"
    anon "T-this is a crypt!"
    odette @ f_laugh "Hehe, isn't it awesome?"
    anon f_worried_low "I... Umm-"
    odette "You should have seen it before I came along..."
    show anon f_worried
    odette "... It was ghastly!"
    anon "Y-yeah, this is kinda... Morbid, isn't it?"
    odette f_happy_up "Morbid?"
    pause
    odette f_smirk @ f_laugh "Are you saying you don't like my new home?"
    anon a_behind_head "Err..."
    odette "You don't find it erotic?"
    anon f_surprised a_sides "Erotic?!"
    odette @ f_happy_up "All these spirits laid to rest here..."
    odette "... Can you feel them watching you?"
    show anon f_worried a_surprised_up_both with {'master': dissolve}:
        flip
        xoffset -650
    anon "W-watching me?"
    show odette b_vamp_normal f_tired_happy_lipbite with dissolve:
        xoffset -480
    pause
    show anon f_surprised_teeth
    odette f_smirk "Mmm, I get tingles running up my spine just thinking about it..."
    show anon a_surprised_shoulders:
        unflip
        xoffset -150
    show odette f_laugh:
        xoffset -200
    with {'master': dissolve}
    anon "!!!"
    show anon f_skeptical a_sides
    with {'master': dissolve}
    odette "Hehehehe!"
    show anon f_worried_low
    pause
    anon "What are you wearing?"
    show odette f_smirk
    anon f_frown_down a_point_down "And where are your shoes?"
    show anon f_surprised_low a_sides behind odette
    show odette b_vamp_show:
        xoffset -250
    with dissolve
    odette "Do you like it?"
    odette "It's my halloween costume from last year."
    show odette b_vamp_normal f_smirk:
        xoffset -150
    show anon f_worried
    with dissolve
    odette "Or, well... At least it's the cape from my halloween costume."
    anon "You probably shouldn't be barefoot in here."
    odette "The rest of it would just get in our way, don't you think?"
    anon f_frown_down "I'm just saying, you're gonna end up with hook worms or something..."
    odette @ f_laugh "Hehehe!"
    show anon f_worried
    show odette f_drink a_blood_cup_drink
    with dissolve
    odette "Mmm!"
    anon "W-what are you drinking there?"
    show odette f_smirk a_idle with dissolve
    odette "Oh, this?"
    show odette with {'master': dissolve}:
        xoffset -225
    odette "Just some red wine... Would you like some?"
    anon "I ehh... No, I probably shouldn't..."
    odette "Come now, I insist!"
    anon "N-no, really that's-"
    show odette a_blood_cup_force
    show anon f_smoke a_up
    with {'master': dissolve}
    anon "!!!"
    pause
    odette "That's it."
    odette "Drink deep, big fella."
    show odette a_idle
    show anon f_worried a_sides
    with dissolve
    anon "Eugh, that doesn't taste like wine to me..."
    odette "Heh, it's a very special blend."
    odette "I made it myself."
    show odette f_drink a_blood_cup_drink with dissolve
    anon "Really?"
    show odette a_idle f_smirk with dissolve
    anon "Isn't it supposed to be sweet?"
    pause
    anon "Because that's more like a salty flavor..."
    anon "... It's kinda syrupy too."
    show odette a_blood_cup_force
    show anon f_smoke a_up
    with dissolve
    odette "Shh."
    anon "!!!"
    odette "This is going to make you feel fantastic, just trust me."
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
    anon "My arms feel weird."
    show odette a_idle f_smirk o_blood
    with dissolve
    odette "That means it's working."
    show anon a_surprised_lips f_surprised_down with dissolve
    anon "N mah rips fee numb..."
    odette @ f_laugh "Hehe!"
    anon a_sides f_surprised "Id dis namol?"
    odette "Perfectly normal, {b}[firstname]{/b}."
    odette a_blood_cup_throw "Don't you worry your pretty little head."
    show odette a_blood_wipe o_empty with dissolve
    anon @ -m_talk "Hmm."
    show odette a_undress1 with dissolve
    pause
    show odette b_naked a_vamp_undress2
    show anon a_surprised_hands f_surprised_low
    with dissolve
    anon "Ah joo shurr?"
    show odette a_idle with dissolve
    anon "Kaz dis dunnit-"
    jump odette_button_crypt.resume
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
