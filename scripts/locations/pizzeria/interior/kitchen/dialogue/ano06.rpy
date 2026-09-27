label ano06_cook_pizzeria_kitchen:
    call maria_button_stage
    show maria f_annoyed
    show anon behind maria with dissolve
    maria "Alright now, kid."

    maria @ a_finger1 "I'm only gonna go over this once, so pay attention."

    anon "Ya, Bu."

    maria "In my kitchen we only serve hand-tossed dough."

    show maria a_point with dissolve
    show anon f_surprised_down
    maria "None of that thin crust crap!"

    show maria a_idle with dissolve
    show anon f_worried
    maria @ f_eyeroll "And don't even get me started on deep dish..."

    maria "Only a fuckin' looney would call that abomination a pizza!"

    maria "More like, tomato soup in a bread bowl if you ask me."

    maria @ a_whatever "But we'll save all that for another day..."

    maria "For now, I just want you to look at the recipe and top the pizzas."

    anon "Baiklah."

    show maria a_point with dissolve
    show anon f_surprised_teeth
    maria "Don't be stingy with any of it neither!"

    show maria a_idle with dissolve
    show anon f_worried
    maria "This is my livelihood and I want it done right."

    anon "Ya, Bu."

    maria f_normal "Bagus."

    maria "Now, when you're done toppin', you gotta slide it into the oven and let it go for exactly seven minutes and thirty seconds."

    anon "How hot does the oven need to be?"

    maria "Hey, now that's a good question, kid!"

    show anon f_normal
    maria "It really depends on what kind of oven ya got."

    maria "These here, I run at seven hundred degrees."

    anon @ f_surprised "Wow, that's really hot!"

    maria "I use a double pizza stone setup too."

    anon @ f_confused "Maksudnya itu apa?"

    maria "Well, you see, you got the bottom stone... That's where the pizza goes..."

    maria "... But then I also put a stone on a rack directly above it."

    maria "That traps the heat in, kinda like an oven inside the oven."

    anon a_thinking f_thinking "An oven inside an oven, huh?"

    maria "It gives the pizzas that perfect, crispy crust."

    anon a_idle f_normal @ f_brag_closed "Alright, I'll remember that."

    maria "So, {b}you follow the recipe to the letter{/b}."

    maria @ a_finger1 "Don't skimp on the toppings..."

    maria @ a_finger2 "... And you leave it in the oven for how long?"

    anon "Seven minutes and thirty seconds."

    maria @ f_laugh a_point "Ding, ding, ding!"

    maria "We have a winner!"

    maria a_crossed "I guess, {b}Tony{/b} was right about you after all."

    pause
    maria "Now, let's do a quick one together, yeah?"

    anon "Oke."

    show maria a_point with {'master': dissolve}:
        flip
        xoffset 600
    maria "Alright, so your dough is over here..."

    show maria a_crossed behind anon
    show anon:
        xoffset 400
    with {'master': dissolve}
    maria "... All nice and pizza shaped, thanks to yours truly."

    maria "All you gotta do now is read the recipe and add the correct toppings as it calls for them."

    show anon with {'master': dissolve}:
        xoffset 200
    anon "Ya, saya bisa melakukan itu."

    show maria with {'master': dissolve}:
        unflip
        xoffset 200
    maria "Let's see it."


    label ano06_cook_pizzeria_kitchen.retry:
    show screen minigame_pizza2(('hawaiian',)) with fade
    call screen empty()
    hide screen minigame_pizza2
    $ renpy.dynamic(res=_return)

    call maria_button_stage
    show maria:
        xoffset 200
    show anon behind maria:
        xoffset 200

    if res:
        show anon f_worried
        show maria f_angry
        with fade
        maria "C'mon, what's the matter with you?!"

        anon "S-sorry, {b}Maria{/b}!"

        anon "I got confused."

        maria "All you gotta do is read the recipe!"

        maria a_point "You can read, right?"

        anon f_sad_down "... Ya."

        maria a_idle "Well, hurry up and try again!"

        jump ano06_cook_pizzeria_kitchen.retry

    with fade
    maria "Hey, not bad!"

    maria "I'm startin' to think you might actually have an aptitude for this, kid."

    anon "Terima kasih."

    maria "Are you good to keep goin' by yourself for a while?"

    maria "'Cause I gotta mind the counter 'til {b}Tony{/b} gets back."

    anon "Yep, no problem."

    maria "I can't tell you how happy I am to finally have some good help around here."

    anon "It's my pleasure, {b}Maria{/b}."

    maria @ f_laugh "Your pleasure, huh?"

    maria "Man, you're a good kid!"

    pause
    maria "Tell you what... You crank out a few more pies like this and I'll be forced to reward ya."

    anon f_skeptical "What kind of reward?"

    maria "Heh, somethin' special that I usually only do for {b}Tony{/b}."

    anon f_normal @ f_surprised "Oh?"

    maria "Trust me, you'll love it."

    pause
    maria "Now get to it!"

    anon @ f_brag_closed a_salute "Ya, Bu."


    call minigame_pizza2 (3)

    call maria_button_stage
    show maria:
        flip
        xoffset -100
    show anon behind maria:
        flip
        xoffset 50
    with fade
    maria "How's it goin' back here?"

    anon "Everything is fine."

    pause
    anon "How's it goin' up there?"

    maria a_crossed "Heh, I'm bored outta my mind to be honest."

    maria "I'd much rather be back here and have you up there."

    anon "Well, we can switch, if you want?"

    maria a_idle "Nah, it's okay."

    maria @ f_laugh "I can't believe you did so well!"

    pause
    maria "Oh, that reminds me."

    maria f_sexy "I promised you a reward, didn't I?"

    maria "... And I should probably give it to you before {b}Tony{/b} gets back."

    maria "He might get upset if he sees..."

    show maria with dissolve:
        xoffset -50
    anon f_shy "S-sees what?"

    maria "Just relax, kid."

    maria "It's gonna blow your mind!"

    anon "{i}*Gulp*{/i} W-what's going to blow my mind?"

    maria a_cannoli_hold "Why, one of my famous cannolis, of course!"

    anon f_shock "..."
    pause
    show maria a_cannoli_give with dissolve
    maria "Here, give it a taste."

    show maria a_idle
    show anon a_cannoli f_sad_down
    with dissolve
    anon @ -m_talk "..."
    maria "C'mon, don't leave me in suspense all day!"

    show anon a_cannoli_eat f_cough with dissolve
    pause
    anon a_cannoli_eaten f_surprised_shock_food @ -m_talk "!!!" with hpunch
    anon f_orgasm_food o_boner "Ya Tuhan..."

    maria f_normal "Benar?"

    anon "This is the most delicious thing I've ever tasted!"

    maria @ f_laugh "hehe!"

    anon f_normal "Why don't you sell these?"

    anon "You would make a fortune!"

    maria "Ahh, I dunno about that..."

    anon "aku serius!"

    anon "It's like, a crime you aren't selling these!"

    maria "Well, they're {b}Tony{/b}'s favorite thing in the entire world, and he's not big on sharing them."

    anon "Oh?"

    maria "I mean, he might be alright with you havin' one here or there, 'cause you're his protégé, or whatever."

    maria "But he ain't gonna ever let me sell 'em, that's for sure."

    anon "Yeah, I guess I can understand him wanting them all to himself."

    anon "I kinda want them all to myself too!"

    anon "They're so good!"

    show anon a_cannoli_gobble f_yawn with dissolve
    show maria f_surprised_low m_talk
    pause
    maria f_laugh "Hah, you remind me so much of {b}Tony{/b} when he was younger..."

    show maria f_normal -m_talk
    show anon f_orgasm_food a_idle with dissolve
    pause
    maria "I can see why he's takin' a shine on you."

    anon "Ya?"

    maria "I ain't seen him buddy up to someone like this since Luigi died."

    pause
    anon f_worried @ f_skeptical "Luigi?"

    anon "That was {b}Tony{/b}'s friend that died, right?"

    maria f_sad "Oh, they was more than friends."

    maria "Luigi was like a brother to {b}Tony{/b}."

    maria "They grew up in that orphanage together and then watched each other's backs, workin' for the mob all those years..."

    maria f_sad_down "{b}Tony{/b} ain't never been the same since it happened."

    pause
    anon f_surprised "Wait a second, did you just say {b}Tony{/b} was in the mob?"

    maria f_surprised "!!!"
    maria "You mean, he didn't tell you?"

    anon "Tidak."

    maria "Ah, sial!"

    pause
    show anon f_shock o_empty with fastdissolve
    anon "{b}Tony{/b} was in the Russian Mafia?!"

    show anon f_surprised_teeth
    maria f_confused "Russian?!"

    maria f_normal @ f_laugh "Tentu saja tidak!"

    anon f_skeptical "Tapi kamu baru saja mengatakan-"

    maria "He was in the Italian Mafia, you knucklehead."

    anon f_worried "Oh."

    anon f_normal "Yeah, that makes more sense."

    show maria f_eyeroll
    pause
    show maria f_normal
    anon f_thinking a_thinking @ -m_talk "( So {b}Tony{/b} is ex-Italian Mafia, huh? )"

    anon @ -m_talk "( That explains why he knows so much about the crimewave in Summerville. )"

    maria f_sad "Ugh, look, kid..."

    maria "Just forget I said anything, will ya?"

    show anon f_worried a_idle with dissolve
    maria "I know you got somethin' goin' on with those dirty Russians..."

    maria "... Which is probably why {b}Tony{/b}'s been keeping you in the dark about all this."

    maria "He doesn't want you doing anything stupid and gettin' yourself hurt."

    tony "{b}Maria{/b}, I'm back!"

    maria @ f_surprised "!!!"
    maria "{i}*Sigh*{/i} Perfect timing."

    show tony f_suspicious behind maria with dissolve:
        xoffset -200
    tony "You're supposed to be up at the counter, ain't ya?"

    tony "What are ya doin' back here?"

    maria f_annoyed "Oh, relax, will ya?"

    maria "It's not like we've got customers out there at the moment..."

    tony "That's not the point!"

    tony "You can't just go leavin' the store front unattended during business hours!"

    maria "Baiklah, sialan."

    maria "You ain't gotta yell at me, {b}Tony{/b}!"

    show tony b_dressed_slumped f_sad_down with dissolve
    pause
    tony "I know, I-"

    tony "{i}*Sigh*{/i} I'm sorry, darlin'."

    maria f_sad a_sides "What's goin' on?"

    maria "Did somethin' happen at the doctor's office?"

    pause
    tony "My boys can't swim, {b}Maria{/b}..."

    show anon f_surprised_teeth
    maria "Apa?!"

    tony "Yeah, the doc says there's not a chance in hell."

    maria "Oh, honey, it's gonna be alright..."

    show tony f_angry b_dressed a_frustrated with {'master': dissolve}
    maria "We'll-{w=.5}{nw}"

    tony "What are you talkin' about?!"

    tony "It's not gonna be alright!"

    show tony b_dressed_slumped f_sad_down with dissolve
    tony "After everything I put you through and now I can't even give ya this..."

    tony "It's fuckin' karma, catchin' up with me."

    maria "{b}Tony{/b}..."

    tony "What the hell kinda man am I?"

    maria "Tch, stop talkin' like that!"

    show tony b_dressed_hug
    hide maria
    with dissolve
    show anon f_worried
    maria "You're the best man I've ever met and that's the end of it!"

    maria "We'll figure something out."

    anon @ -m_talk "..."
    pause
    show tony b_dressed a_sides
    show maria f_sad:
        flip
        xoffset -50
    with dissolve
    tony "I dunno what you think we're gonna do, there's nothin' for it!"

    tony "{i}*Sigh*{/i} I gotta go sit down or somethin'..."

    hide tony with dissolve
    pause
    maria @ -m_talk "..."
    anon "Uhh, is everything alright?"

    maria @ -m_talk "Hmm?"

    pause
    maria "Oh, sorry about that, kid."

    pause
    maria "Ehh, why don't you take the rest of the day off?"

    maria "{b}Tony{/b} and I got a lot of talkin' to do."

    anon "Y-ya, oke."

    show maria with {'master': dissolve}:
        unflip
        xoffset -500
    anon "Let me know if there's anything I can do to help?"

    hide maria with {'master': dissolve}
    maria "Terima kasih, {b}[firstname]{/b}."

    pause
    anon @ -m_talk "( I wonder what all that was about? )"

    pause
    anon @ -m_talk "( I should clear out and give them some space. )"

    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
