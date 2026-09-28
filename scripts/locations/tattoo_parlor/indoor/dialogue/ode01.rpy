label ode01_init_tattoo_parlour:
    scene expression background(400, 400, 2) as stage
    show grace a_sides:
        xoffset -100
    show odette:
        flip
        xoffset 190
    show eve f_drawing_down a_artpad_drawing:
        xoffset 100
    show anon behind odette with dissolve:
        xoffset -100
    odette "C'mon, babe!"
    odette "It'll make me so happy."
    grace @ f_eyeroll "Heh, you're ridiculous..."
    odette "Please?!"
    show grace f_uneasy_back with dissolve:
        flip
        xoffset 490
    grace "I'm not doing... THAT... In a cemetery!"
    hide grace with dissolve
    show odette with {'master': dissolve}:
        xoffset 460
    odette "I'm telling you, you're gonna love it!"
    hide odette with {'master': dissolve}
    grace "Not happening."
    anon f_shy "{b}Eve{/b}?"
    eve f_happy "{i}*Gasp*{/i} {b}[firstname]{/b}!!"
    show eve b_dressed_hug_jump_anon behind anon:
        xoffset -100
    show anon b_empty f_shy_low
    with fastdissolve
    eve "I was hoping you'd come by today."
    anon "Heh, what's going on?"
    show eve b_dressed_kiss:
        xoffset -450
    hide anon
    with dissolve
    anon "!!!"
    eve "Mmm."
    show eve b_dressed_flirt:
        xoffset -450
    show anon f_flirt_low behind eve:
        xoffset -100
    with dissolve
    eve "I missed you!"
    show eve b_dressed_tired f_happy_closed:
        flip
        xoffset 100
    anon a_surprised_up_both f_surprised_low "Y-yeah, I missed you too."
    show anon f_surprised_down o_boner of_blush
    show eve b_dressed_pickup:
        flip
        xoffset 150
    with dissolve
    pause
    show anon a_empty f_surprised_left
    show anon_arms_dressed_a_cover_boner as arms behind eve:
        xoffset -100
    show eve b_dressed f_laugh a_artpad:
        unflip
        xoffset -400
    with dissolve
    pause
    hide arms
    show anon a_surprised f_surprised_down -of_blush
    show eve f_sexy
    with dissolve
    pause
    show anon a_sides f_normal
    show eve f_nervous_down a_artpad_drawing
    with dissolve
    pause
    anon a_idle "Is everything alright with {b}Odette{/b} and your sister?"
    eve f_happy @ -m_talk "Hmm?"
    eve "Oh, yeah."
    eve "They're just arguing about some silly sex thing {b}Odette{/b} wants to do..."
    anon f_shy "Sex thing?"
    eve "You know how she can be..."
    anon "Yeah, believe me... I know."
    show anon f_shy_low -o_boner with dissolve
    pause
    anon @ f_normal_low "What are you drawing?"
    eve @ f_laugh "Just some Halloweenie stuff..."
    anon f_normal "Really?"
    eve "You wanna see?"
    anon "Of course!"
    show eve a_artpad_show
    show anon f_looking_down
    with dissolve
    pause

    scene closeup_drawing_03 with fade
    anon "Whoa."
    pause
    anon "This is awesome!"
    eve "You like it?"
    anon "What are you supposed to be?"
    eve "Vampire hunters, duh."
    anon "It's so cool!"
    pause

    scene expression background(400, 400, 2) as stage
    show anon:
        xoffset -100
    show eve a_artpad_show:
        xoffset -400
    with fade
    anon "Are you going to dress up like that for real?"
    eve o_blush f_nervous_down a_artpad "I dunno, maybe..."
    pause
    eve f_nervous "Would you, umm... Like that?"

    menu:
        "Hell yeah!":
            anon @ f_laugh "You would look like a total bad ass."
            eve "I would?"
            anon "Vampire hunting sisters, it's perfect!"
            show eve f_happy -o_blush with {'master': dissolve}
            eve "Maybe I'll talk to {b}Grace{/b} about it..."
            anon "Yeah, you should."
        "You should go as something sexier!":

            anon f_flirt "You should go as something sexier!"
            eve f_surprised "M-me?"
            anon "Well, yeah."
            eve f_sad "Like what?"
            anon "I dunno..."
            anon f_thinking a_thinking @ -m_talk "Hmmm..."
            anon f_flirt a_frustrated "... A sexy cat?"
            show anon a_idle
            show eve f_nervous
            with dissolve
            pause
            eve "You really think I could pull that off?"
            anon "I know you could."
            show eve f_thinking_lip -o_blush with {'master': dissolve}
            pause
            eve f_nervous "I'll think about it..."

    show grace f_angry a_crossed with dissolve:
        xoffset -100
    show anon f_surprised
    odette "Hey, you didn't hear me complain when you wanted to do it in the bathroom of that {i}Hysteria! At the Discotheque{/i} concert!"
    show anon f_worried
    show eve f_eyeroll
    show odette f_angry behind grace:
        xoffset 150
    show grace a_upset:
        flip
        xoffset 400
    with dissolve
    grace "That was you!"
    show eve f_drawing_down a_artpad_drawing with dissolve
    odette f_confused "... It was?"
    grace a_crossed @ f_disgusted "And it was disgusting!"
    odette f_smirk "Oh, right."
    odette f_annoyed a_crossed "I dunno why you're complaining about it..."
    odette "... I was the one kneeling on the floor in filth."
    odette "All you had to do was lean against the stall door."
    show eve f_disgusted behind anon with dissolve:
        flip
        xoffset 200
    eve @ -m_talk "..."
    grace "Yeah, until my panties got stuck on that latch and we fell!"
    odette @ f_laugh "Hehehe!"
    odette f_smirk "It didn't stop you from cumming on my face though, did it?"
    eve f_angry "Oh my god..."
    show grace f_embarrassed behind odette with dissolve:
        unflip
        xoffset -90
    eve "Could you two like, stop talking about this please?"
    grace "Sorry, {b}Sis{/b}."
    show grace f_eyeroll
    odette f_annoyed "Don't apologize!"
    show grace f_uneasy behind eve:
        flip
        xoffset 375
    show odette a_idle
    with {'master': dissolve}
    odette "There's nothing wrong with being sexually adventurous, {b}Evie{/b}."
    odette "You and {b}[firstname]{/b} should try it sometime."
    show anon f_surprised
    show eve f_lipbite_right o_blush
    show grace f_angry
    with {'master': dissolve}
    grace "Alright, enough."
    show anon f_worried
    show eve f_drawing_down
    grace "If you want to rent some scary ghost movies and make a night of it on the couch, I'm down."
    grace "But it's a hard pass on the cemetery, okay?"
    show eve -o_blush
    show odette a_crossed f_pouting_right
    with dissolve
    grace "So just drop it."
    odette "Fine."
    pause
    odette "Forgive me for trying to spice up our love life a little!"
    show grace f_embarrassed with dissolve:
        unflip
        xoffset -100
    grace "I think it's plenty spicy already..."
    show odette f_pouting
    show anon of_blush f_surprised a_point_self
    with dissolve
    pause
    show anon f_surprised_high a_sides with dissolve
    pause
    show anon f_surprised_low a_idle behind eve with dissolve:
        xoffset -60
    pause
    show anon f_shy_low -of_blush
    show grace f_tired:
        flip
        xoffset 400
    with dissolve
    grace "Now, if you'll excuse me..."
    grace "... I need to start working on that new price board for the shop."
    show grace a_sides with dissolve:
        xoffset 500
    odette @ -m_talk "Mhmm."
    hide grace
    show odette f_tired a_idle:
        flip
        xoffset 650
    with dissolve
    odette "Whatever makes you happy, dear..."
    show odette a_crossed with dissolve:
        unflip
        xoffset 150
    show anon f_shy
    pause
    show odette f_tired_happy_lipbite
    anon f_surprised @ -m_talk "( !!! )"
    show anon f_worried_low
    pause
    show odette f_smirk a_idle behind eve with dissolve:
        xoffset -50
    odette "So, {b}Evie{/b}..."
    show eve f_normal
    show anon f_worried
    eve @ -m_talk "Hmm?"
    odette "I don't suppose you and {b}[firstname]{/b} would like to check out this super awesome place I found?"
    eve f_confused "In the church graveyard?"
    eve "Are you crazy?"
    eve f_thinking_down "I have enough nightmares, thank you."
    show eve f_drawing_down
    odette f_sad "Oh, c'mon!"
    odette "You always love those creepy movies I show you, right?"
    eve f_sad "I do."
    show odette f_normal
    eve "And if there's one thing I've learned from them, it's that it's a bad idea to go fooling around in a graveyard!"
    show eve f_drawing_down
    show odette f_tired
    pause
    odette "Fine."
    odette f_smirk "I guess it's just you and me then, big fella?"
    anon f_worried @ a_behind_head "Err."
    odette "You're not scared, are you?"
    show eve behind anon
    show anon:
        xoffset -100
    with dissolve
    anon "N-no, of course not."
    anon "I just, umm... You know, {b}Eve{/b}'s not going so... I wouldn't wanna-"
    odette "Wanna what?"
    odette "Keep your good friend {b}Odette{/b} company while she explores a creepy cemetery?"
    odette f_sad "What if a zombie attacks me?"
    odette "Who's gonna protect me?"
    anon "Do you care if I go with her?"
    show anon behind eve
    show eve f_confused:
        unflip
        xoffset -400
    with dissolve
    eve "You really want to?"
    anon "I mean, it would be bad to let her go alone... Right?"
    odette f_smirk @ a_swooning f_laugh "Oh, my hero!"
    show eve f_angry behind anon with dissolve:
        flip
        xoffset 200
    eve "Ugh, I guess if it gets her to shut up about it... Then whatever..."
    eve f_drawing_down @ f_thinking_down "... I'm fine with it."
    odette @ a_excited "Yay!"
    anon "Do you just wanna meet there tonight?"

    if game.timer.is_fullmoon():
        odette a_idle f_normal "Yes, but only because the timing works out."
        odette "If this is a one time thing, I want it to be extra special!"
        anon @ -m_talk "Huh?"
    else:
        odette f_thinking a_idle "No, if this is a one time thing, I want it to be extra special..."
        pause

    show odette f_smirk

    $ renpy.dynamic(ttl=game.timer.days_until_lunar(.5))
    $ renpy.dynamic(day=game.timer.dayOfWeek(delta=ttl, full=True))

    if game.timer.is_fullmoon():
        odette "Tonight will be a full moon."
    elif ttl > 7:
        odette "Let's plan on doing this {b}during the next full moon{/b}."
    elif ttl > 1:
        odette "Let's plan to do this {b}on [day], during the next full moon{/b}."
    else:
        odette "Let's plan to do this {b}tomorrow, during the next full moon{/b}."

    anon f_worried "Full moon?"
    odette @ a_shrug "Everyone knows the spirits of the dead are stronger on {b}full moons{/b}."
    anon "{i}*Gulp*{/i} R-right, okay."
    odette "And don't chicken out on me!"

    if game.timer.is_fullmoon():
        anon "{b}Church graveyard. Tonight.{/b}"
    else:
        anon "{b}Church graveyard. Full moon.{/b}"

    anon "I'll be there."
    show odette f_laugh with {'master': dissolve}:
        flip
        xoffset 600
    odette "Hehe, this is gonna be fun!"
    hide odette with dissolve
    pause
    show anon behind eve
    show eve f_sad:
        unflip
        xoffset -400
    with dissolve
    eve "Just be careful, okay?"
    eve "If {b}Odette{/b} does something stupid and pisses off an evil spirit..."
    eve "... Just run away and let it eat her."
    anon @ f_laugh "Heh, I couldn't do that."
    eve f_happy "No, seriously."
    eve "You have my permission."
    show eve f_laugh
    anon f_laugh "Hehe!"

    scene black with slowdissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
