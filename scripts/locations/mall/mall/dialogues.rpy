label mall_eve_make_up_go_to_mall_has_items:
    scene expression player.location.background_blur with None
    show eve f_happy
    show anon
    with dissolve
    anon "I have some {b}candles{/b} and some {b}chocolates{/b} already."
    eve f_surprised "Oh, well..."
    return

label mall_eve_make_up_go_to_mall_first:
    scene expression player.location.background_blur with None
    show eve f_happy
    show anon
    with dissolve
    eve "You know, I used to avoid places like this before I met you..."
    eve "I always felt like everyone was judging me."
    anon "And now?"
    eve "Now, I don't give a damn!"
    pause
    eve "You like who I am and that's all I care about."
    anon "Heh, yes I do."
    anon f_flirt "I like you very much!"
    show eve b_dressed_kiss1:
        xoffset -400
    hide anon
    with dissolve
    pause
    show eve b_dressed f_laugh:
        xoffset -200
    show anon f_flirt_grin
    with dissolve
    eve "Hehe!"
    show eve f_happy
    anon f_normal @ a_behind_head "{i}*Ahem*{/i} W-where should we start?"
    eve "{b}Consum-R{/b} should have candles and that new store {b}Cupid{/b} on the second floor probably has chocolates."
    anon "Alright."
    hide anon
    hide eve
    with dissolve
    return

label mall_eve_make_up_go_to_mall_repeat:
    scene expression player.location.background_blur with None
    show anon with dissolve
    anon @ -m_talk "( Hmm, {b}Eve{/b} wants me to pick up {b}candles{/b} from {b}Consum-R{/b} and {b}chocolates{/b} from {b}Cupid{/b}. )"
    anon @ -m_talk "( That shouldn't be too hard. )"
    hide anon with dissolve
    return


label mall_eve_clients_mall_fliers:
    scene expression player.location.background_blur with None
    show anon:
        flip
        xoffset 100
    show eve a_flyers f_happy_right:
        xoffset -200
    with dissolve
    eve "This was such a good idea, {b}[firstname]{/b}!"
    anon @ f_laugh "Heh, thanks!"
    eve "Now we just need to hang a few around the mall, and we'll move on to somewhere else."
    anon "Yeah, okay."
    show kassy:
        flip
    with dissolve
    show eve f_happy
    kassy "Hey, what are you all marketing?"
    eve "My sister's tattoo parlor."
    eve "You want one?"
    show kassy f_smirk_down a_flyer with dissolve
    pause
    kassy f_normal "Hmm, {b}Sugar Tats{/b}?"
    kassy @ f_laugh "Hah, that's so funny, I love it!"
    show kassy f_smirk_down
    pause
    kassy f_normal "Oh, twenty percent off!"
    kassy "I bet my friend {b}Lily{/b} would be way into this!"
    kassy "We'll check it out for sure!"
    eve @ f_laugh "Awesome, see you there!"
    hide kassy with dissolve
    pause
    eve f_happy_right "Oh my god it's working!"
    eve "{b}Grace{/b} is going to be so excited if we pull this off."
    eve "Hurry up and hang those, {b}[firstname]{/b}!"
    eve "We'll {b}head to the Library{/b} next."
    anon @ f_laugh "Yes, ma'am."
    hide anon
    hide eve
    with dissolve
    return

label mall_jenny_get_a_mask:
    scene expression game.timer.image('location_mall{}_crowd_blur')
    show player 11 at left with dissolve
    player_name "( What the- )"
    player_name "( There's a crowd of people outside {b}Cosmic Cumics{/b}! )"
    show player 31 with dissolve
    player_name "( Is that {b}Erik{/b}? )"
    hide player with dissolve
    return

label mall_jenny_go_shopping:
    scene expression player.location.background_blur with None
    show anon f_worried
    show jenny b_casual f_upset:
        flip
        xoffset 500
    with dissolve
    anon "Would you slow down?!"
    pause
    anon f_skeptical "{b}[jen_name]{/b}!"
    jenny "Don't talk to me."
    anon f_grumpy "Ugh, why do you always have a stick up your butt?"
    anon "Can't you just be chill for a little while?"
    jenny "No, I can't be chill. Not when I have a loser shadowing my every move."
    show anon f_worried
    anon "Nobody is even looking at us, {b}[jen_name]{/b}!"
    show jenny f_eyeroll
    jenny "Whatever."
    show jenny f_upset
    pause
    anon "Where are we going anyways?"
    pause
    anon f_grumpy "I'm just gonna keep asking, you know?"
    pause
    anon f_unimpressed "{b}[jen_name]{/b}, where are we-"
    show anon f_surprised
    show jenny f_angry:
        unflip
        xoffset 0
    with dissolve
    jenny "Grr, we're going to {b}Pink{/b} on the second floor, okay?!"
    anon f_worried "More sex toys?"
    show jenny f_upset
    jenny "I swear to god, if you don't shut up, the only place you're going is the hospital."
    jenny "To get my foot surgically removed from your ass."
    anon f_unimpressed @ f_unimpressed_bored "Heh, good one."
    show jenny:
        flip
        xoffset 500
    with dissolve
    pause
    anon f_worried "I don't know what you're so bent out of shape for anyways..."
    anon "Like I said, nobody here cares if we're tog-"
    if M_grace.sex_1st_time:
        grace "{b}[jen_name]{/b}?!"
    else:
        grace "{b}[firstname]{/b}?!"
    show anon f_surprised
    show jenny f_surprised
    pause
    show anon:
        flip
        xoffset -210
    show jenny f_sad:
        unflip
        xoffset 0
    show grace:
        flip
    with dissolve
    if M_grace.sex_1st_time:
        jenny "{b}Grace{/b}?"
    else:
        anon "{b}Grace{/b}?"
    show anon f_normal

    if not M_eve.finished_state(S_eve_visit_tattoo_shop):
        grace "Oh my god, it is you!"
        grace "I haven't seen you since high school!"
        show jenny f_eyeroll
        jenny "Ehh, yeah..."
        show jenny f_upset
        grace "How have you been?"
        jenny "I'm fine."
        grace "Well, that's good."
        pause
        grace "I'm doing great too."
        grace "I opened up my own tattoo parlor, over on the north side of town."
        grace "{b}Sugar Tats{/b}."
        grace "You heard of it?"
        jenny "No."
        grace "Oh, you have to come check it out!"
        grace "We get pretty busy in the evenings but if you came before that we'd have time to chat and catch up."
        jenny "Yeah, no thanks {b}Grace{/b}..."
        grace "Ah, you're probably busy, huh?"
        grace "What are you doing for work nowadays?"
        if M_jenny.get('dominance') <= 0:
            show jenny f_surprised
            jenny "I uhh..."
            anon f_worried "H-hi, I'm {b}[firstname]{/b}."
            show jenny f_normal
        else:
            anon f_snarky @ f_laugh "Heh, yeah {b}[jen_name]{/b}... What are you doing for work?"
            show jenny f_sad
            jenny "I uhh..."
        grace "Oh, I'm sorry. I didn't know you two were together."
        grace "I'm {b}Grace{/b}."
        show anon f_normal
        anon "Nice to meet you."
        grace @ f_laugh "Wow, {b}[jen_name]{/b}! Your boyfriend is cuuuute!"
        show jenny f_angry
        anon f_worried "Oh, I'm not-"
        show anon f_surprised
        show jenny f_upset
        jenny "Ugh, he is NOT my boyfriend!"
        anon f_worried "I'm her roommate."
        grace "Oh, I see."

    elif M_grace.sex_1st_time:
        grace "Oh my god, it is you!"
        grace "I haven't seen you since high school!"
        show jenny f_eyeroll
        jenny "Ehh, yeah..."
        show jenny f_upset
        anon "Hello, {b}Grace{/b}."
        grace "Hey, {b}[firstname]{/b}."
        grace "What are you-"
        pause
        grace f_surprised "Wait a minute, you two aren't... Together, are you?!"
        anon f_surprised_teeth "!!!"
        jenny f_gross "Umm, fuck no!"
        anon f_sad_down "..."
        jenny "Gross!!"
        anon f_worried "{b}[jen_name]{/b} is my roommate."
        grace "O-oh."
        grace f_normal @ f_laugh "Phew, that's a relief!"
        pause
        grace "So..."
    else:

        grace "Fancy meeting you here."
        grace "{b}Eve{/b} isn't with you?"
        jenny f_upset "What the fuck?"
        grace @ f_laugh "Whoa!!"
        grace "Is that, {b}[jen_name]{/b}?!"
        jenny f_angry "Who's {b}Eve{/b}?"
        grace "I haven't seen you since high school!"
        grace "What are you-"
        pause
        grace f_sad "Wait a minute, you two aren't... Together, are you?!"
        show anon f_surprised_teeth
        jenny f_upset @ f_eyeroll "Pfft, like I would ever-"
        anon f_worried "No, no, no!!"
        show jenny f_angry
        anon "We are definitely not together, I promise you!"
        pause
        show anon f_worried_left
        pause
        anon "What?"
        show anon f_worried
        jenny "He's my roommate."
        grace "O-oh."
        grace @ f_normal "Phew, I was worried I'd have to kick your ass for a second there, {b}[firstname]{/b}..."
        grace "Umm, y-you know... For {b}Eve{/b}'s sake."
        show grace f_normal
        pause
        grace "So, {b}[jen_name]{/b}..."

    grace "You're still living at home then?"
    show jenny f_eyeroll
    jenny "N-not because I have to or anything..."
    show jenny f_upset
    jenny "They're just... Having money problems and I'm helping them out, you know?"
    anon @ -m_talk "..."
    grace "Oh, I can totally relate."
    grace "I took my sister in a couple years ago, after our parents died."
    if not M_grace.sex_1st_time:
        jenny "{b}Eve{/b}, I assume?"
        anon @ f_worried_left "Yup."
    grace "She's been living with me ever since."
    grace "Family comes first, right?"
    jenny "I didn't know you have a sister..."
    grace "Oh, yeah... She's younger than us."
    if M_grace.sex_1st_time:
        anon f_normal "She's in my class."
    show jenny f_eyeroll
    jenny "Yeah, that's great..."
    show jenny f_upset
    show anon f_worried
    pause

    if not M_eve.finished_state(S_eve_visit_tattoo_shop):
        pass

    elif M_grace.sex_1st_time:
        grace "You know, {b}[jen_name]{/b}, you're welcome to come meet her."
        grace "My tattoo parlor is over on the north side of town."
        grace "Maybe we could all hang out sometime?"
        jenny "You own a tattoo parlor?"
        grace @ f_laugh "Yup!"
        grace "{b}Sugar Tats{/b}."
        grace "You haven't heard of it?"
        jenny "No."
        anon f_normal "It's really awesome!"
        grace @ f_laugh "Hehe, thanks {b}[firstname]{/b}!"
        show jenny f_eyeroll
        jenny "Eugh..."
        show jenny f_upset
        grace "We get pretty busy in the evenings but if you came before that we'd have time to chat and catch up."
        jenny "Yeah, no thanks {b}Grace{/b}..."
        grace "Ah, you're probably busy, huh?"
        grace "What are you doing for work nowadays?"
        if M_jenny.get('dominance') <= 0:
            show jenny f_surprised
            jenny "I uhh..."
            show jenny f_sad
            show anon f_worried
            pause
            anon f_shy "H-hey, {b}Grace{/b}... Umm, how is {b}Odette{/b} doing?"
            show jenny f_normal
            grace @ -m_talk "Hmm?"
            grace "Oh, you know her, she's a handfull."
            anon f_normal @ f_laugh "Heh, totally."
            grace "Her newest thing is trying to convince me into taking some yoga classes at the gym."
            grace @ f_eyeroll "Like we can afford that..."
        else:
            anon f_laugh "Heh, yeah {b}[jen_name]{/b}... What are you doing for work?"
            jenny f_angry "Shut up, {b}[firstname]{/b}!!!"
            anon "Haha!"
            show anon f_normal
            show jenny f_sad
            jenny "I uhh..."
            pause
            jenny f_angry "Tsk, who asked you to be so nosy, anyways?"
            grace f_sad "Oh, umm... My bad."
            grace "I was just trying to catch up."
            jenny f_upset @ f_eyeroll "Eugh."
        grace f_normal "Oh, that reminds me..."
    else:

        grace "You're welcome to come meet her... If you want?"
        grace "My tattoo parlor is over on the north side of town."
        grace "I'm sure she'd love to-"
        jenny "You own a tattoo parlor?"
        grace @ f_laugh "Yup!"
        grace "{b}Sugar Tats{/b}."
        grace "You haven't heard of it?"
        jenny "No."
        anon f_normal "It's really awesome!"
        grace @ f_laugh "Hehe, thanks {b}[firstname]{/b}!"
        jenny @ f_eyeroll "Eugh..."
        grace "Just come with {b}[firstname]{/b} next time."
        grace "We'll rent a movie or something."
        jenny "Yeah, no thanks {b}Grace{/b}..."
        grace "Ah, you're probably busy, huh?"
        grace "What are you doing for work nowadays?"
        if M_jenny.get('dominance') <= 0:
            show jenny f_surprised
            jenny "I uhh..."
            show jenny f_sad
            show anon f_worried
            pause
            anon f_shy "H-hey, {b}Grace{/b}... What brings you here?"
            grace @ -m_talk "Hmm?"
            grace "Oh, I used up the last of my massage oil the other day, when you and I-"
            show jenny f_upset
            show grace f_surprised
            show anon f_surprised_teeth
            pause
            grace "{i}*Ahem*{/i} I mean, when {b}Odette{/b} and I..."
            jenny a_crossed f_angry @ -m_talk "..."
            anon f_shy "I'm surprised you didn't send {b}Odette{/b} to pick some up."
            grace f_normal @ f_laugh "Hah, I can't trust her to get the right stuff."
            grace @ f_eyeroll "Last time she brought home some strawberry flavored off brand... It was awful!"
            anon f_normal @ f_laugh "Haha!"
            jenny f_upset @ f_eyeroll "Eugh."
        else:
            anon f_laugh "Heh, yeah {b}[jen_name]{/b}... What are you doing for work?"
            jenny f_angry "Shut up, {b}[firstname]{/b}!!!"
            anon "Haha!"
            show anon f_normal
            show jenny f_sad
            jenny "I uhh..."
            pause
            jenny f_angry "Tsk, who asked you to be so nosy, anyways?"
            grace f_sad "Oh, umm... My bad."
            grace "I was just trying to catch up."
            jenny f_upset @ f_eyeroll "Eugh."

    if M_grace.sex_1st_time:
        if not M_eve.finished_state(S_eve_visit_tattoo_shop):
            grace "Oh, I ran into {b}Cedric{/b} the other day."
            grace "He mentioned you guys had broken up a few months ago."
        else:
            grace "I ran into {b}Cedric{/b} the other day."
            grace "He mentioned you guys had broken up."
        jenny "Yeah, I need someone more motivated than boring old {b}Cedric{/b}."
        grace "Aww, I always thought he was kinda sweet..."
        show jenny f_angry
        grace "... But I imagine you're looking for bigger fish, eh?"
        grace "You always were popular with the guys."
        show jenny f_upset
        jenny "You know, {b}Grace{/b}... This has been fun and all, but I'm really busy, so if you don't mind?"
        if not M_eve.finished_state(S_eve_visit_tattoo_shop):
            grace "Oh, right... Sorry."
            grace @ f_laugh "I could jabber on all day, hehe."
        else:
            grace "Y-yeah, okay."
    else:
        jenny "You know, {b}Grace{/b}... This has been fun and all, but we're busy, so if you don't mind?"
        grace f_normal "Y-yeah, okay."

    pause
    grace "Why don't I give you my card, in case you change your mind-"
    jenny "NO, no... That's okay."
    jenny "I won't."
    show grace f_suspicious
    jenny "Come on, loser."
    hide jenny with dissolve
    pause
    show anon:
        unflip
        xoffset 300
    with dissolve
    pause
    show anon:
        flip
        xoffset -210
    with dissolve
    anon "S-sorry about that."
    grace f_normal "It's alright. I wasn't expecting anything different."
    grace "She hasn't changed one bit since high school."
    anon "Yeah."

    if not M_grace.sex_1st_time:
        grace "It's hard to believe you're related."
        anon @ f_laugh "Heh, tell me about it."
        grace f_sexy "You coming by the house later?"
        show grace f_surprised
        pause 1
        grace f_uneasy "Y-you know, to see my sister?"
        anon "Yeah, of course."
        grace f_normal "Cool."
        pause

    anon "I should probably catch up with her."
    grace @ f_laugh "Hehe, good luck."
    anon f_normal "Thanks."
    hide grace with dissolve
    pause
    show anon f_skeptical a_salute with dissolve:
        unflip
        xoffset 400
    anon @ -m_talk "( Hmm, now where did {b}[jen_name]{/b} go? )"
    anon @ -m_talk "( She said she was headed towards, {b}Pink{/b}... {b}I should check there{/b}. )"
    hide anon with dissolve
    return

label mall_first_visit:
    scene mall
    show player 14 with dissolve
    player_name "( I love the mall! )"
    show player 17
    player_name "( You can go shopping for all sorts of stuff, there's even a movie theater! )"
    hide player 17 with dissolve
    return

label mall_diane_get_bug_spray:
    scene expression "backgrounds/location_mall_day_blur.jpg"
    show player 13 at left
    show diane b_casual
    with dissolve
    diane "Mmm, it's nice to get out of the house for a while."
    show player 14
    player_name "Yeah, how come you don't go out more?"
    show player 13
    diane "Oh, I don't know."
    diane "There's not much to do in this town by yourself..."
    show player 14
    player_name "{b}[deb_name]{/b} would hang out with you."
    show player 13
    show diane f_shamed_smile
    diane "Heh, {b}[deb_name]{/b} has her own stuff going on..."
    diane "... I don't wanna bother her."
    show diane f_shamed
    show player 14
    player_name "Oh, please! {b}[deb_name]{/b} has tons of free time."
    show player 10
    player_name "Especially now, with my dad gone..."
    show player 5
    diane @ -m_talk "..."
    show diane f_shamed_smile
    diane "You're right, I should make more of an effort."
    diane "We used to be so close when we were younger."
    show diane f_shamed
    show player 10
    player_name "... And if she's busy..."
    show player 17
    player_name "You can always ask me!"
    show player 13
    show diane f_laugh
    diane "Hah, you don't wanna hang out with an old lady like me!"
    show diane f_normal
    show player 14
    player_name "You aren't old {b}Diane{/b}!"
    player_name "Besides, you're one of the most fun people I know!"
    show player 13
    diane "I am?"
    show player 17
    player_name "Yeah!"
    show player 13
    diane "Thanks, {b}[firstname]{/b}..."
    diane @ -m_talk "..."
    show diane f_shamed_smile
    diane "{i}*Ahem*{/i} Well, we should {b}head towards Consum-R and get that pesticide{/b}."
    show diane f_normal
    show player 14
    player_name "Right behind you."
    hide player
    hide diane
    with dissolve
    return

label mall_mom_mall_outing:
    scene mall
    show player 13 at left with dissolve
    show old_debbie 165 at Position(xpos=.75, ypos=1.0) with dissolve
    debbie "Thanks again for coming with me, sweetie!"
    show player 14
    show old_debbie 164
    player_name "No problem, {b}[deb_name]{/b}. I'm having fun!"
    show player 13
    show old_debbie 166
    debbie "Me too!"
    show old_debbie 164
    debbie "..."
    show old_debbie 165
    debbie "Are there any stores you'd like to visit while we're here?"
    show player 14
    show old_debbie 164
    player_name "Hmm, no, not really."
    show player 13
    show old_debbie 165
    debbie "Alright, well, {b}Tammy{/b} was telling me all about this {b}new store{/b} that opened up recently."
    debbie "I think she said it was called {b}Cupid{/b}."
    debbie "We should go check it out! What do you say?"
    show player 14
    show old_debbie 164
    player_name "Sure, {b}[deb_name]{/b}. Okay."
    show player 13
    show old_debbie 165
    debbie "... It should be up on the {b}second floor{/b}."
    show old_debbie 167 at right with dissolve
    debbie "Lead the way, sweetie."
    hide player
    hide old_debbie
    with dissolve
    return

label mall_roxxy_fake_id_ask_terry:
    scene mall
    show player 13 at left
    show old_roxxy 2 at right
    with dissolve
    roxxy "So you have a job, huh?"
    show old_roxxy 1
    show player 14
    player_name "Yeah."
    show player 13
    show old_roxxy 1b
    roxxy "... And you make good money?"
    show old_roxxy 1
    show player 29 with dissolve
    player_name "I dunno."
    player_name "Good enough, I guess..."
    show player 13 with dissolve
    show old_roxxy 1l with dissolve
    roxxy "Hmm..."
    show old_roxxy 1d
    roxxy "So, if you had a girlfriend... You could like... Buy her clothes and stuff, huh?"
    show old_roxxy 1e
    show player 12
    player_name "Uhh, yeah. I suppose."
    show player 5
    show old_roxxy 1h with dissolve
    roxxy "Interesting..."
    show old_roxxy 1b
    roxxy "C'mon, {b}the photo booth should be on the second floor{/b}!"
    hide old_roxxy with dissolve
    show player 10
    player_name "O-okay."
    hide player with dissolve
    return

label mom_mall_outing_block:
    scene expression player.location.background_blur
    show player 1
    player_name "Hmm, I'm supposed to be {b}looking for a store called Cupid{/b}."
    show player 4
    player_name "{b}[deb_name]{/b} said it should be {b}on the second floor{/b}."
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
