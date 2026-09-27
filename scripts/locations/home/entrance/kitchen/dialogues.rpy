label kitchen_jenny_final_breakfast:
    scene expression player.location.background_blur with None
    show jenny f_upset:
        flip
        xoffset 150
    show debbie f_sad:
        xoffset 90
    with fade
    debbie "Oh, good grief {b}[jen_name]{/b}..."

    debbie "I never wanted you to leave in the first place!"

    show jenny f_eyeroll
    jenny "Well, I want to get a place of my own, it's just..."

    show jenny f_sad
    jenny "I'm not ready yet."

    debbie f_normal "That's perfectly fine, dear."

    debbie "You're welcome to stay here at home forever, so far as I'm concerned."

    debbie @ f_laugh "God knows, I could use the help!"

    show jenny f_normal
    jenny "Yeah, that's exactly what I was thinking, and with my work going so well, I could probably chip in a couple hundred more a month."

    debbie "Oh, that would be wonderful, dear!"

    show anon f_normal:
        xoffset -100
    with dissolve
    anon "Apa yang terjadi?"

    debbie "Good morning, sweetie!"

    debbie "We were just talking about {b}[jen_name]{/b} moving out."

    anon f_shock "APA?!"

    anon f_worried "Y-you're moving out?!"

    show jenny f_grin:
        unflip
        xoffset -200
    with dissolve
    debbie @ f_laugh "Oh, no, no, no!"

    debbie "I meant to say, she's not moving out."

    show jenny f_normal
    jenny "Yeah, I've decided to stay here a while longer."

    jenny "Save up some money, you know?"

    debbie "Isn't that wonderful, {b}[firstname]{/b}?!"

    anon f_normal "Y-yeah, wonderful!"

    hide jenny
    show debbie b_robe_hug3
    with dissolve
    debbie "I'm just so proud of you, dear!"

    show debbie b_robe_hug4
    jenny "T-thanks, {b}Mom{/b}..."

    show debbie b_robe
    show jenny at flip
    show jenny b_dressed a_hips:
        xoffset 250
    with dissolve
    debbie "Why don't you two go have a seat at the table and I'll whip you up some eggs and bacon?"

    show jenny f_normal
    jenny "Baiklah."

    hide jenny with dissolve
    anon f_laugh "Mmm, that sounds great!"

    hide anon with dissolve
    $ player.go_to(L_home_diningroom)
    scene expression game.timer.image("dining_room{}")
    show expression "characters/jenny/layeredimage/jenny_breakfast_table.png" zorder 3
    show anon b_dinner_sitting_look_left f_worried zorder 1
    show jenny f_phone_upset a_magic_sit_stand_phone b_magic_sit_stand_dressed zorder 1
    pause
    anon "Jadi uhh..."

    anon "About last night..."

    show jenny f_upset
    jenny "Ugh, you're not going to start in with this lovey-dovey bullshit again, are you?"

    anon "Why are you being so weird about it?"

    show jenny f_angry
    jenny "Umm, you're the one being weird!"

    show jenny f_upset a_idle with dissolve
    jenny "I'm not interested in dating you, {b}[firstname]{/b}..."

    jenny "We're having phenomenal sex and making great money, why can't that be enough for you?!"

    anon "You really don't want more?"

    jenny "What, like marriage and kids?!"

    jenny "A little brick house with a white picket fence?"

    anon f_normal "... Sounds kinda nice."

    show jenny f_gross
    jenny "Eugh, don't make me barf!"

    anon f_worried @ -m_talk "..."
    show jenny f_upset
    show debbie b_breakfast_potatoes zorder 2 with dissolve
    show anon f_normal_high
    debbie "Alright, who's hungry?!"

    jenny "Right here!"

    show debbie b_breakfast_potatoes3 with dissolve
    show anon b_dinner_sitting f_normal
    pause
    show debbie b_breakfast_potatoes with dissolve
    show anon f_shy_down
    debbie "What were you all talking about?"

    jenny "Tidak ada yang penting."

    show anon b_dinner_sitting_look_left f_worried
    anon "..."
    anon f_worried_high "Actually, I've just lost my appetite."

    show debbie f_sad
    show jenny f_eyeroll
    jenny "Ugh, so what, now you're all mad?"

    show jenny f_upset
    show anon f_worried
    debbie @ -m_talk "..."
    anon b_dinner_sitting "Can I be excused?"

    debbie "O-of course..."

    debbie "... Is everything alright, sweetie?"

    anon f_tired "Ya, aku baik-baik saja."

    hide anon with dissolve
    debbie "What's going on with you two?"

    jenny "It's nothing, {b}Mom{/b}."

    jenny "{b}[firstname]{/b}'s just being a big baby..."

    $ player.go_to(L_home_entrance)
    scene expression player.location.background_blur with None
    show anon f_worried with dissolve
    anon @ -m_talk "( Well, that could have gone better... )"

    pause
    anon f_skeptical @ -m_talk "( She's just so damn stubborn! )"

    anon @ -m_talk "( Even if she did want more, she'd never admit it. )"

    anon f_tired @ -m_talk "( {i}*Sigh*{/i} )"

    anon f_worried @ -m_talk "( I should just {b}give her some space{/b}... )"

    anon @ -m_talk "( ... Maybe she'll come around? )"

    hide anon with dissolve
    return

label kitchen_jenny_helping_with_breakfast_confront_her:
    show debbie f_normal
    debbie "Sweetie, are you coming?"

    show anon f_worried with dissolve:
        unflip
        xoffset 0
    anon "Actually, I just remember something I need to do."

    debbie f_sad "Oh."

    anon "Rain check?"

    debbie f_normal "Tentu!"

    anon @ f_normal "Terima kasih, {b}[deb_name]{/b}."

    hide debbie with dissolve
    anon @ -m_talk "( {b}[jen_name]{/b} said she was heading upstairs to take a shower. )"

    anon @ -m_talk "( I should hurry if I wanna catch her! )"

    hide anon with dissolve
    return

label kitchen_jenny_helping_with_breakfast_let_it_go:
    show anon f_thinking a_thinking with dissolve
    anon @ -m_talk "( Hmm, whatever. )"

    show anon f_worried a_idle with dissolve
    anon @ -m_talk "( {i}*Sigh*{/i} I probably shouldn't worry about it too much. )"

    anon @ -m_talk "( I mean, at least she's giving money to {b}[deb_name]{/b} again... )"

    anon @ -m_talk "( That's the important thing. )"

    debbie "Sweetie, are you coming?"

    anon f_normal "Ya!"

    anon @ -m_talk "( I should head to the dining room and join {b}[deb_name]{/b} for breakfast. )"

    hide anon with dissolve
    return

label kitchen_jenny_helping_with_breakfast:
    scene expression player.location.background_blur with None
    show debbie
    show jenny:
        flip
        xoffset 150
    with dissolve
    debbie "Well, of course I'm happy that you're gonna start contributing, dear."

    debbie "I'm just curious about this new job you've got?"

    show jenny f_eyeroll
    jenny "Ugh, it's nothing special..."

    show jenny f_normal
    debbie "Transcribing, you said?"

    jenny "Ya."

    debbie "What are you transcribing?"

    jenny "I dunno, {b}Mom{/b}..."

    pause
    jenny "... Customer service calls and stuff."

    debbie @ f_laugh "Oh, that's neat!"

    jenny "Tidak juga..."

    jenny "... It pays though."

    show anon
    debbie "Well, I'm proud of you, dear."

    show jenny f_eyeroll
    jenny "Eh ya."

    show jenny f_normal
    anon "Apa yang terjadi?"

    debbie "{b}[jen_name]{/b} was just telling me about her new job."

    anon f_skeptical "Ah, benarkah?"

    show anon f_snarky
    show jenny f_angry a_crossed:
        unflip
        xoffset -250
    with dissolve
    debbie "She's transcribing things over the internet."

    anon "You don't say..."

    debbie "It sounds really interesting."

    show jenny f_normal:
        flip
        xoffset 150
    with dissolve
    jenny "It's not."

    debbie "Why don't you come have breakfast with {b}[firstname]{/b} and me?"

    debbie "You can tell us all about it."

    show jenny f_upset
    jenny "Ehh, no thanks."

    jenny "I need a shower."

    hide jenny with dissolve
    pause
    debbie @ f_sorry "Oh, well... okay, dear."

    debbie "You'll join me, won't you {b}[firstname]{/b}?"

    show anon f_normal
    anon "Ya, tentu saja."

    hide anon
    show debbie b_robe_hug1
    with dissolve
    debbie "Aww, you're such a good boy!"

    show debbie b_robe_hug2 with dissolve
    anon "Heh, thanks, {b}[deb_name]{/b}."

    anon "You go on ahead, I'll be right there."

    show debbie b_robe_hug1 with dissolve
    debbie "Okay, sweetie."

    show anon
    hide debbie
    with dissolve
    pause
    show anon f_snarky:
        flip
        xoffset -500
    with dissolve
    pause
    anon @ -m_talk "( Transcribing, huh? )"

    anon @ -m_talk "( She's so full of crap... )"

    anon @ -m_talk "( ... And she's lying to {b}[deb_name]{/b} about it. )"

    return

label kitchen_jenny_sluttygram_pics:
    $ player.go_to(L_home_diningroom)
    scene expression game.timer.image("dining_room{}")
    show jenny b_breakfast_dressed a_phone f_upset_down zorder 1
    show anon b_dinner_sitting_look_left a_bowl f_shy_down zorder 0
    show expression "characters/jenny/layeredimage/jenny_breakfast_table.png" zorder 2
    with dissolve
    pause
    show anon f_looking_down_eating a_eating with dissolve
    pause 
    show anon f_surprised_food a_resting with dissolve
    jenny "Oh, what the hell!"

    anon f_surprised_food "Apa yang sedang kamu lakukan?"

    jenny "..."
    jenny "I can't believe how fucking stupid these people are!"

    anon f_grumpy_food_left "Uhh, hello?!"

    show jenny f_angry
    jenny "Apa?!"

    anon f_surprised_food "I asked what you are doing?"

    show jenny f_eyeroll
    jenny "Tidak ada apa-apa."

    show jenny f_upset
    jenny "Just, shut up and go away..."

    jenny "... Wimp."

    show jenny f_upset_down
    anon f_grumpy_food_left "Uh, baiklah."

    hide anon
    show player 323c at Position(xpos=610,ypos=770)
    with dissolve
    anon "I dunno why you have to be such a bitch, all the tim-"

    show player 323d
    show jenny f_upset_down
    jenny "Tunggu sebentar!"

    anon "..."
    jenny "What do you know about social media?"

    show player 323e
    anon "Hah?"

    anon "Mengapa?"

    show player 323b
    jenny "Sit down."

    show player 323c
    anon "... Oke."

    hide player
    show anon b_dinner_sitting_look_left a_bowl f_worried zorder 0
    with dissolve
    jenny "I made an account on this website where loser guys pay hot girls to post pictures of themselves."

    show jenny f_grin a_phoneshow with dissolve
    jenny "I'm sure you've heard of it, you are a loser after all..."

    scene expression "backgrounds/location_home_diningroom_sluttygram.jpg" with dissolve
    anon "Sluttygram, seriously?!"

    anon "This is your bright idea for making money?"

    pause
    scene expression game.timer.image("dining_room{}")
    show jenny b_breakfast_dressed a_phoneshow f_upset zorder 1
    show anon b_dinner_sitting_look_left f_worried zorder 0
    show expression "characters/jenny/layeredimage/jenny_breakfast_table.png" zorder 2
    with dissolve
    jenny "So what if it is?!"

    show jenny a_phone with dissolve
    jenny "I'm hot enough to do something like this..."

    show jenny f_eyeroll
    jenny "... Way hotter than all of these little bitches!"

    show jenny f_upset
    jenny "I should be making a killing on this site!"

    anon "Well, you're awfully full of yourself, aren't you?"

    show jenny f_grin
    jenny "Pfft, says the guy who won't stop perving on me!"

    anon "Hmm, fair enough."

    anon "Jadi apa masalahnya?"

    show jenny f_normal
    jenny "The problem is, I've had this account active for a couple weeks now, and I've barely gotten any followers at all!"

    anon "Well, these things take time, you know?"

    anon "You don't just get a million followers overnight."

    jenny "That's bullshit!"

    jenny "I don't have time to wait around, I need money now!"

    anon "Then maybe you should go back to {b}Consum-R{/b} and-"

    show jenny f_upset_down
    jenny "Seriously, look at all the followers this skank has!"

    pause
    jenny "And this one!"

    show jenny f_upset a_phoneshow with dissolve
    show anon f_surprised_left_low
    pause
    show jenny f_upset_down a_phone with dissolve
    show anon f_worried
    jenny "... And oh my god, look at that one!"

    show jenny f_upset a_phoneshow with dissolve
    anon f_normal "Oh ho, I'm looking."

    show anon f_surprised_left_low
    jenny "She looks like she fell out of the ugly tree and hit every branch on the way down..."

    anon f_normal "Mmm, I dunno... she looks pretty good to me!"

    show jenny a_phone with dissolve
    jenny "Tch, the only reason you're saying that is because her tits are hanging out..."

    show jenny f_upset
    anon @ f_worried "Tidak!"

    pause
    anon "That's not... the only reason."

    anon "Though now that you mention it, all of those girls are posting way more provocative pictures than you are."

    show jenny f_sad
    jenny "Provocative?"

    show jenny f_grin
    pause
    jenny "Don't you mean slutty?!"

    anon "Tentu oke."

    show jenny f_sad
    pause
    jenny "So, you think I should post some sluttier pictures?!"

    anon f_worried "No, I think you should get a regular job like a normal person."

    show jenny f_angry
    pause
    jenny "No way, screw that!"

    jenny "Ikutlah denganku."

    show jenny b_breakfast_gettingup f_upset with dissolve
    anon "Hah?"

    hide anon
    show jenny b_breakfast_pulling with dissolve
    anon "Where are we-"

    hide jenny with dissolve
    jenny "Shut up and come on."

    scene black with dissolve
    $ player.go_to(L_home_sisbedroom)
    label jenny_taking_pictures_replay:
    if store._in_replay is not None:
        $ player.location = L_home_sisbedroom
    scene expression player.location.background_blur with None
    show player 12 at left
    show jenny
    with dissolve
    player_name "What the heck are we doing?!"

    show player 90
    show jenny f_upset a_camera_give with dissolve
    jenny "{i}We're{/i} taking some dirty pictures for my dumb Sluttygram account, so more horny losers will subscribe to my feed!"

    show player 728b
    show jenny a_hips
    with dissolve
    player_name "When did you get a digital camera?!"

    show player 728
    jenny "None of your business, wimp."

    show player 728b
    player_name "Is that what you spent my money on?!"

    hide jenny with dissolve
    scene expression "backgrounds/location_home_jennybedroom_closeup_peek.jpg" with None
    show jenny b_bed_dressed a_tie f_normal_low with dissolve
    jenny "..."
    show jenny b_bed_tied a_knot with dissolve
    player_name "{b}[jen_name]{/b}, this is stupid!"

    player_name "Why don't you just go back up to {b}Consum-R{/b} and ask if you can have your old job back?!"

    show jenny a_down with dissolve
    player_name "I'm sure they'll-"

    pause
    show jenny b_bed_back_tied a_down f_normal_low with dissolve
    player_name "They'll-"

    show jenny a_pull f_normal with dissolve
    jenny "There. How's that?"

    player_name "..."
    player_name "You know, on second thought."

    player_name "I think the Sluttygram idea is marvelous and I'm fully on board with this plan now."

    show jenny f_grin
    jenny "Heh, just shut up and take the pictures, loser!"

    call screen jenny_photo1

label kitchen_jenny_sluttygram_pics_post_photo1:
    scene expression "backgrounds/location_home_jennybedroom_closeup_peek.jpg" with None
    show jenny b_bed_back_tied a_down f_normal
    with fade
    jenny "How did that look?"

    show jenny f_grin
    jenny "It's hot, right?"

    player_name "Y-ya!"

    jenny "You should probably get a nice shot of my ass too."

    jenny "I bet those losers will loooove that."

    call screen jenny_photo2

label kitchen_jenny_sluttygram_pics_post_photo2:
    scene expression "backgrounds/location_home_jennybedroom_closeup_peek.jpg" with None
    show jenny b_bed_back_tied a_down f_grin
    with fade
    jenny "Alright, time for the finale."

    jenny "Make sure you get a good shot."

    player_name "Ini luar biasa!"

    jenny "Yeah, yeah. Hurry it up."

    call screen jenny_photo3

label kitchen_jenny_sluttygram_pics_post_photo3:
    $ renpy.end_replay()
    $ persistent.cookie_jar["Jenny"]["unlocked"] = True
    $ persistent.cookie_jar["Jenny"]["gallery"]["02_unlocked"] = True
    $ player.go_to(L_home_sisbedroom)
    scene expression player.location.background_blur with None
    show jenny b_tied f_normal a_hips
    show player 727 at left
    with dissolve
    jenny "Alright, lemme see!"

    hide player
    show anon
    show jenny f_normal_low a_camera_look
    with dissolve
    jenny "..."
    show jenny f_normal
    jenny "Oh yeah, if this doesn't bring in the followers, nothing will."

    show jenny f_grin
    jenny "Those other skanks are about to learn what real hotness looks like!"

    show jenny f_grin_down
    pause
    anon "I think you ruined your shirt..."

    show jenny f_normal
    jenny "Hah?"

    show jenny f_normal_low
    pause
    show jenny f_grin
    jenny "Yeah, whatever. I've got more shirts."

    show jenny f_upset
    jenny "Why are you still here?!"

    anon f_skeptical "Apa maksudmu?"

    show anon f_worried
    jenny "I mean, get out."

    jenny "I'm done with you."

    anon f_skeptical "What the hell, I thought we were-"

    show jenny f_angry
    jenny "Goodbye, perv!"

    anon @ -m_talk "..."
    show anon f_sad_down
    anon "{i}*Huh*{/i}"

    hide anon with dissolve
    show jenny f_grin_down
    pause
    show jenny f_laugh
    jenny "Damn, I'm sexy!"

    scene black with dissolve
    $ player.go_to(L_home_hallway)
    scene expression player.location.background_blur with None
    show anon f_normal with dissolve
    anon @ -m_talk "( I can't believe that just happened. )"

    anon @ -m_talk "( She was actually being kind of cool for a few minutes there. )"

    anon f_laugh "( And then she practically stripped for me! )"

    pause
    anon f_worried @ -m_talk "( Too bad she went back into bitch mode after I took the pictures... )"

    anon f_normal @ -m_talk "( Oh well. )"

    pause
    show anon f_thinking a_thinking with dissolve
    anon @ -m_talk "( I wonder if I can get a copy of those photos somehow? )"

    hide anon with dissolve
    $ game.timer.tick()
    $ M_jenny.trigger(T_jenny_took_pictures)
    $ game.main()

label kitchen_jenny_have_breakfast:
    scene expression player.location.background_blur with None
    show anon
    show debbie
    with dissolve
    anon "Morning {b}[deb_name]{/b}."

    hide anon
    show debbie b_robe_hug1
    with dissolve
    debbie "Good morning, sweetie."

    pause
    show anon
    show debbie b_robe
    with dissolve
    anon "Mmm, breakfast smells wonderful!"

    debbie @ f_laugh "Hehe, it's almost done."

    debbie "{b}Why don't you go sit down at the table{/b} and I'll bring it to you?"

    anon "Awesome, thanks, {b}[deb_name]{/b}!"

    show anon:
        flip
        xoffset -500
    with dissolve
    anon "( {b}[deb_name]{/b} makes the best breakfast! )"

    hide anon
    hide debbie
    with dissolve

    $ player.go_to(L_home_diningroom)
    scene expression game.timer.image("dining_room{}") with None
    show jenny b_breakfast_dressed a_idle f_normal_low zorder 1
    show anon b_dinner_sitting_look_left zorder 0
    show expression "characters/jenny/layeredimage/jenny_breakfast_table.png" zorder 2
    with dissolve
    pause
    anon "Pagi."

    jenny "Mmhmm."

    anon f_tired "Why are you eating cereal?"

    anon "Didn't you see {b}[deb_name]{/b} cooking breakfast?"

    show anon f_normal
    show jenny f_eyeroll
    jenny "Yes, but I was recently told I need to grow up and support myself, remember?"

    show jenny f_normal_low
    anon f_surprised_left "..."
    anon f_normal "Are you really still pouting about that?"

    jenny "I'm not pouting."

    anon "Yes, you are."

    jenny "Tsk, shut up."

    pause
    pause
    show jenny f_normal
    jenny "Hey, lend me sixty dollars."

    anon f_worried "Hah?!"

    show jenny f_upset
    jenny "I said, lend me sixty dollars."

    anon "What for?!"

    show jenny f_eyeroll
    jenny "Ugh, that's none of your business!"

    show jenny f_upset
    anon "Umm, it's my money... So yes, it kinda is my business!"

    jenny "{i}*Sigh*{/i} Look, I know a way I can make some money but I need to buy something first."

    jenny "I'll pay you back."

    anon f_normal "Ya benar."

    anon "How are you gonna pay me back?!"

    anon "You don't even have a job."

    show jenny f_angry
    jenny "Don't be a dick, {b}[firstname]{/b}!"

    show jenny f_upset
    jenny "I know {b}Diane{/b} is overpaying you for whatever the hell you're doing at her house."

    anon "I'm tending her garden."

    show jenny f_grin
    jenny "Ya, terserah."

    jenny "Tidak peduli."

    jenny "The point is, you can spare sixty measly dollars."

    anon f_worried "Mustahil!"

    anon "I need every cent I can get if I want to make tuition next year..."

    anon "... Especially now that {b}Dad{/b}'s gone."

    show jenny f_angry
    jenny "Grr, fine..."

    jenny "... But I'm gonna remember this!"

    show debbie b_breakfast_potatoes with dissolve
    pause
    show jenny f_normal_low
    show anon f_normal_high
    debbie "Here you go, sweetie."

    show debbie b_breakfast_potatoes3 with dissolve
    anon b_dinner_sitting f_normal "Terima kasih, {b}[deb_name]{/b}."

    show debbie b_breakfast_potatoes
    show anon a_bowl f_shy_down
    with dissolve
    debbie "You want me to fix you a plate, {b}[jen_name]{/b}?"

    show jenny b_breakfast_gettingup f_upset with dissolve
    jenny "No, I do not."

    show debbie f_sad
    show anon f_looking_down_eating a_eating
    hide jenny
    with dissolve
    pause
    show anon f_looking_down_food a_resting with dissolve
    debbie "What's the matter with her?"

    anon f_surprised_high_food "She's still pouting over what you said the other night."

    debbie "{i}*Sigh*{/i} I guess, I should go and apologize to her."

    anon "No you shouldn't, {b}[deb_name]{/b}."

    anon "Dia hanya menyebalkan."

    debbie "{b}[firstname]{/b}!"

    debbie "Don't say that about {b}[jen_name]{/b}!"

    anon "Sorry, {b}[deb_name]{/b}..."

    anon "... But it's true."

    debbie f_normal "Tsk, just eat your breakfast."

    anon f_normal_high "Thanks again for this, it's delicious!"

    debbie "You're welcome, sweetie."

    scene black with dissolve
    hide anon
    hide debbie
    hide expression "characters/jenny/layeredimage/jenny_breakfast_table.png"
    return

label kitchen_diane_3way_aftermath:
    scene expression "backgrounds/location_home_kitchen_day_closeup.jpg"
    show jenny a_juice f_gross zorder 2:
        flip
        xoffset 200
    show old_debbie 11b zorder 1 at right
    with dissolve
    debbie "Oh, would you let it go already, {b}[jen_name]{/b}!"

    show old_debbie 10b
    show jenny f_upset
    jenny "No, I don't understand this!"

    jenny "You're really gonna let {b}Diane{/b} stay?!"

    jenny "She was fucking {b}[firstname]{/b}!"

    jenny "Right there in our living room!!"

    show jenny f_gross
    show old_debbie 11b
    debbie "I told you, I dealt with it."

    show old_debbie 10b
    show jenny f_upset
    jenny "You dealt with it?!"

    jenny "What does that even-"

    show player 14 at left with dissolve
    player_name "Morning!"

    show player 13
    show jenny f_gross:
        unflip
        xoffset -200
    show old_debbie 2
    debbie "Good morning, sweetie!"

    show old_debbie 1
    show player 14
    player_name "It smells wonderful in here!"

    show player 13
    show old_debbie 3
    debbie "Hehe, I'm making your favorite!"

    show old_debbie 1
    show player 14
    player_name "Smiley face pancakes?!"

    show player 13
    show old_debbie 2
    debbie "And three strips of bacon!"

    show old_debbie 1
    show player 17
    player_name "Yum!!"

    show player 18
    show old_debbie 3
    debbie "hehe!"

    hide player
    show old_debbie 4
    show jenny:
        flip
        xoffset 0
    with dissolve
    pause
    show jenny f_eyeroll
    jenny "Ugh!"

    show jenny f_upset
    jenny "You guys are getting weirder and weirder every day!"

    show jenny f_gross
    pause
    show jenny f_upset
    jenny "Apa pun."

    jenny "I don't even care anymore!"

    hide jenny with dissolve
    jenny "Buncha weirdos!"

    show old_debbie 1
    show player 5f at left
    with dissolve
    pause
    debbie "Oh, don't mind her {b}[firstname]{/b}."

    show player 5 with dissolve
    show old_debbie 2
    debbie "She's just being dramatic."

    debbie "You know how she is..."

    show old_debbie 1
    show player 10
    player_name "Y-ya."

    show player 13
    pause
    show player 14
    player_name "Did {b}Diane{/b} already leave this morning?"

    show player 13
    debbie "Hmm?"

    show old_debbie 2
    debbie "Oh, yeah... She was gone before the sun was up."

    debbie "Said she wanted to get a head start on the day."

    debbie "Sounds like she'll have lots of work waiting for you."

    show old_debbie 1
    show player 29 with dissolve
    player_name "Heh, y-yeah... Work."

    show player 13 with dissolve
    show old_debbie 2
    debbie "C'mon, we'd better get some food into you."

    debbie "You're gonna need lots of energy to keep up with {b}Diane{/b}!"

    show old_debbie 1
    show player 14
    player_name "O-okay, {b}[deb_name]{/b}."

    hide player
    hide old_debbie
    with dissolve
    return

label kitchen_diane_breeding_candidate:
    scene expression "backgrounds/location_home_kitchen_day_closeup.jpg"
    show player 14 at left
    show jenny a_juice zorder 2:
        flip
        xoffset 200
    show old_debbie 1 zorder 1 at right
    with dissolve
    player_name "Selamat pagi."

    show player 13
    show jenny f_eyeroll
    show old_debbie 2
    debbie "Morning, sweetie!"

    show old_debbie 1
    show jenny f_upset
    show player 10
    player_name "Where's {b}Diane{/b}?"

    show player 13 with None
    show jenny zorder 0:
        unflip
        xoffset -200
    with dissolve
    debbie "Hmm?"

    show old_debbie 2
    debbie "Oh, she took off early this morning, all excited about something."

    show old_debbie 1
    show player 14
    player_name "Excited?"

    show player 13
    show old_debbie 2
    debbie "Yeah, she was even more amped up than the morning her barn was finished."

    show old_debbie 1
    show player 14
    player_name "Benar-benar?"

    show player 13
    show jenny f_upset
    jenny "She's so weird."

    show old_debbie 13
    debbie "Oh, hush."

    show old_debbie 14
    show jenny f_eyeroll
    jenny "Well, she is!"

    show jenny f_upset
    show old_debbie 13
    debbie "{b}[jen_name]{/b}!"

    show old_debbie 14b
    pause
    show old_debbie 2
    debbie "Did {b}Diane{/b} tell you what's going on?"

    show old_debbie 1
    show player 29 with dissolve
    player_name "Oh, uhh..."

    player_name "N-nope, heh."

    show player 14 with dissolve
    player_name "I should probably get over there and see what she's up to..."

    show player 13
    show old_debbie 2
    debbie "Well, hold on now."

    debbie "You need your breakfast!"

    show old_debbie 1
    show player 14
    player_name "Tidak, tidak apa-apa."

    player_name "I'm not really hungry."

    show player 13
    show old_debbie 2
    debbie "Tsk, it's not good to skip breakfast, {b}[firstname]{/b}."

    show old_debbie 1
    show player 14
    player_name "Really {b}[deb_name]{/b}, I'm fine."

    player_name "Thanks though!"

    show player 13
    debbie "..."
    show old_debbie 2
    debbie "Oke."

    show old_debbie 1
    show player 14
    player_name "I'll see you both later tonight."

    show player 13
    show old_debbie 2
    debbie "Be careful, sweetie."

    show old_debbie 1
    hide player with dissolve
    pause
    show jenny f_gross
    jenny @ -m_talk "..."
    show jenny f_upset
    jenny "Something strange is going on with those two."

    show old_debbie 2
    debbie "Apa maksudmu?"

    show old_debbie 1 with None
    show jenny:
        flip
        xoffset 0
    with dissolve
    jenny @ -m_talk "..."
    show old_debbie 2
    debbie "They're just excited about the new business."

    show old_debbie 1
    jenny "Ya benar."

    show old_debbie 14
    debbie "Hmm?"

    jenny "Ugh, nothing. Never mind."

    jenny "I'll be in my room."

    hide jenny with dissolve
    show old_debbie 13
    debbie "Alright, dear."

    hide old_debbie with dissolve
    return

label kitchen_diane_barn_news:
    scene expression "backgrounds/location_home_kitchen_day_closeup.jpg"
    show diane b_nightgown_dip:
        xoffset 400
    show jenny a_juice f_gross:
        flip
        xoffset 50
    with dissolve
    debbie "Ha ha ha!"

    show jenny f_normal
    show diane b_nightgown f_smirk:
        xoffset -150
    show old_debbie 1 at right
    with {'master': dissolve}
    jenny "You guys are so weird... I'm outta here."

    show jenny f_normal with dissolve:
        unflip
        xoffset -415
    diane "Aww, what's the matter princess?"

    show jenny:
        flip
        xoffset 50
    with {'master': dissolve}
    diane "You jealous?"

    show jenny f_eyeroll
    jenny "Psh."

    show jenny f_normal:
        unflip
        xoffset -415
    with dissolve
    diane "Don't be grumpy, I'll take you for a spin too."

    show diane a_slap
    show jenny f_surprised_down_back
    jenny "!!!" with hpunch
    show diane f_laugh a_idle
    show jenny f_upset:
        flip
        xoffset 100
    with dissolve
    jenny "N-no way!"

    diane "Hahaha, look at those rosie cheeks!"

    show old_debbie 3
    debbie "Haha!"

    show jenny f_eyeroll
    jenny "Ugh, shuddup!"

    show jenny f_upset
    show player 14 behind jenny at left with dissolve
    player_name "Apa yang terjadi?"

    show player 13
    show old_debbie 1
    show diane f_normal
    diane "{b}[firstname]{/b}!!!"

    show old_debbie 2
    debbie "Good morning, sweetie."

    show old_debbie 1
    show diane f_laugh
    diane "It's done, it's done, it's doooooooone!!!"

    show diane f_cheese
    show player 13
    player_name "Hmm?"

    show player 17
    player_name "Wait, you mean the barn is done?!"

    show player 13
    show diane f_normal
    diane "Bingo!"

    diane "{b}Richard{/b} just called to let me know that everything is ready."

    show jenny f_eyeroll
    jenny "Saya tidak mengerti."

    show jenny f_normal
    jenny "I'd much rather have a house than a stupid barn."

    show diane f_smirk
    diane "Yeah well, I'd rather have a fun roommate, than a sour puss!"

    show old_debbie 13
    debbie "{i}*Sigh*{/i} You two..."

    show old_debbie 14
    show player 14
    player_name "Well, I'm excited!"

    show player 13
    show diane f_normal
    diane "See!!"

    diane "{b}[firstname]{/b} knows how to react to good news!"

    hide player
    show diane b_nightgown_hug2:
        xoffset 0
    show jenny f_gross:
        unflip
        xoffset -100
    with dissolve
    diane @ -m_talk "Terima kasih, {b}[firstname]{/b}!"

    show diane b_nightgown_hug3
    player_name "Y-ya."

    show diane b_nightgown_hug4
    show jenny f_upset
    jenny "Ugh, terserah."

    jenny "I'll be in my room."

    hide jenny with dissolve
    pause
    show diane b_nightgown:
        unflip
        xoffset -150
    show player 14 at left
    with dissolve
    player_name "So are we heading over there?"

    show player 13
    show diane f_normal
    diane "You bet we are!"

    show old_debbie 2
    debbie "Ah ah ah!"

    show diane:
        flip
        xoffset 250
    with dissolve
    debbie "After breakfast!"

    show old_debbie 1
    show diane f_laugh
    diane "Aww, but Mooooom!"

    show diane f_normal
    show old_debbie 2
    debbie "{b}Diane{/b}, it's the most important meal of the day."

    show old_debbie 1
    diane "I've been waiting almost thirty years for this, I'm going!"

    diane "We'll just have to eat an extra big dinner tonight!"

    show diane f_smirk:
        unflip
        xoffset -150
    with dissolve
    diane "Right, {b}[firstname]{/b}?!"

    show player 29 with dissolve
    player_name "aku uhh..."

    show player 3
    show old_debbie 3
    debbie "Hahaha, alright fine."

    show old_debbie 2
    show diane:
        flip
        xoffset 250
    with dissolve
    debbie "Go have your fun."

    show player 13
    hide old_debbie
    show diane f_normal b_nightgown_hug1:
        flip
        xoffset 400
    with dissolve
    diane "Terima kasih!"

    show old_debbie 1 at right
    show diane b_nightgown:
        unflip
        xoffset -150
    with dissolve
    diane "Ayo, {b}[firstname]{/b}!"

    diane "Let's go {b}check out the new barn{/b}!"

    hide diane with dissolve
    show old_debbie 2
    debbie "Just make sure you get dressed first!"

    show old_debbie 1
    show player 14
    player_name "Hehe, I've never seen her so excited..."

    show player 13
    show old_debbie 2
    debbie "Yeah, you'd better go with her."

    hide player
    show old_debbie 4
    with dissolve
    pause
    show old_debbie 5
    player_name "Alright, I'll see you tonight {b}[deb_name]{/b}."

    show old_debbie 2 with dissolve
    debbie "Be safe!"

    hide old_debbie with dissolve
    return

label kitchen_diane_dinner:
    scene location_home_kitchen_day_blur
    show player 14 at left
    show old_debbie 1 at right
    with dissolve
    player_name "Hey, {b}[deb_name]{/b}. I have the fish you wanted."

    show player 13
    show old_debbie 2
    debbie "Thanks, sweetie! Now I can finish dinner."

    debbie "I'll let you know when it's finished, okay?"

    show player 203

    scene black

    scene expression L_home_entrance.background_blur
    show diane b_classy:
        xoffset 100
    show old_debbie 91f
    with dissolve
    diane "Mmm, is that {i}sea trout{/i} I'm smelling?!"

    diane "You didn't?!"

    show old_debbie 93f
    debbie "Of course I did!"

    debbie "I know how to treat my girl right!"

    show diane f_laugh
    show old_debbie 91f
    diane "Oh my gosh, I could totally kiss you right now!"

    show player 203 at left with dissolve
    show diane f_normal
    diane "There he is..."

    diane "... The {i}man of the house{/i}!"

    show player 14
    player_name "Hai, {b}Diane{/b}."

    show player 17
    player_name "That dress looks great on you!"

    show diane f_laugh
    show player 203
    diane "Oh stop it, you!"

    show player 13
    show diane f_normal
    show old_debbie 93f
    debbie "He's quite the little charmer, isn't he?"

    show old_debbie 91f
    diane "I don't know how you manage to keep your hands off him!"

    diane "Where's that unpleasant daughter of yours?"

    diane "Will she be joining us tonight?"

    show player 10
    player_name "Yes, she'll be joining us."

    show player 12
    player_name "She's just upstairs getting ready."

    show player 203
    show diane f_laugh
    diane "Typical spoiled princess..."

    show diane f_normal
    diane "... Well, I'm not waiting for her!"

    diane "Not when {b}[deb_name]{/b}'s sea trout is on the menu!"

    show old_debbie 92f
    debbie "Hey, be nice!"

    show old_debbie 93f
    debbie "{b}[jen_name]{/b}'s had a rough couple years."

    show old_debbie 91f
    show diane f_laugh
    diane "{i}*Snort*{/i} If you say so."

    show old_debbie 93f
    show diane f_normal
    debbie "Saya bersedia."

    debbie "Now both of you get in there and sit down while I scrounge up a bottle of wine!"

    show old_debbie 92f
    debbie "I've got this new brand I want you to try."

    hide old_debbie
    hide diane
    with dissolve
    show player 14
    player_name "I should {b}join them in the dining room{/b}."

    player_name "{b}[deb_name]{/b}'s cooking smells delicious!"

    hide player
    with dissolve

    $ player.go_to(L_home_diningroom)
    scene location_home_dining
    show anon b_dinner_sitting f_normal zorder 0:
        xoffset 32
    show diane b_dinner
    show jenny b_dinner_casual_side a_side1:
        xoffset -250
    show old_debbie 65 at Position(xpos=887)
    show table 1 zorder 2
    with fade
    debbie "... The school really ordered that much?!"

    debbie "It's a good thing you've got {b}[firstname]{/b} to help you, huh?"

    show jenny a_side2 with dissolve
    debbie "It seems like he's always over there nowadays."

    show old_debbie 64
    show jenny b_dinner_casual f_surprised a_idle with dissolve
    show anon f_laugh
    diane "Well, there's just so much work that needs doing between the garden and the milk business."

    diane "... And he's shown such an aptitude for it as well!"

    show old_debbie 65
    debbie "Ah, benarkah?"

    show jenny f_gross
    show old_debbie 64
    show diane a_hand with dissolve
    show anon b_dinner_sitting_look_left
    diane "Oh ya."

    diane "You should really be proud of him, {b}[deb_name]{/b}!"

    diane "He's such a responsible young man..."

    show jenny b_dinner_casual_side a_side1 with dissolve
    show anon f_surprised_left a_touch1:
        xoffset 0
    show diane a_hand2 b_dinner_open
    with dissolve
    anon "( !!! )"
    show jenny a_side2 with dissolve
    diane "... And so smart..."

    diane "... And strong..."

    show anon f_surprised_teeth_left a_touch2
    show diane a_hand3
    with dissolve
    diane "... And gentle."

    show jenny a_side1 with dissolve
    anon "{i}*Meneguk*{/i}"

    show old_debbie 65
    debbie "Aww, of course I'm proud of him!"

    if M_debbie.finished_state(S_debbie_diane_visit) or store._in_replay is not None:
        show old_debbie 67 with dissolve
        debbie "He's really been stepping up around here lately too."

        show old_debbie 68 with dissolve
        anon "( !!! )"
        show old_debbie 69 with dissolve
        pause
        show old_debbie 71 with dissolve
        debbie "Helping out with chores..."

        debbie "... Doing maintenance around the house..."

        show old_debbie 69 with dissolve
        pause
        show old_debbie 71 with dissolve
        debbie "... He's taking such good care of {b}[jen_name]{/b} and me."

        show old_debbie 69 with dissolve
        anon f_normal "Hehehe, I-"

        show old_debbie 68 with dissolve
        anon f_tired "... I mean, it's nothing... really I-"

    show anon f_surprised_teeth_left od_dinner_sitting_boner
    show jenny f_gross b_dinner_casual a_idle
    show old_debbie 64
    with dissolve
    jenny "Ugh, all this lovey-dovey shit is gonna make me barf..."

    show diane f_annoyed_left
    diane "We don't need commentary from the peanut gallery, {b}[jen_name]{/b}..."

    diane "... If you don't have anything nice to say, then don't say nothing at all."

    show diane f_normal
    show jenny f_eyeroll
    jenny "Eugh, whatever."

    show jenny f_gross
    pause
    jenny "You guys are the worst."

    pause
    jenny "Hmm..."

    show jenny f_grin_down a_drop with dissolve
    jenny "... Oops."

    show jenny b_dinner_casual_bending
    show diane f_annoyed_left
    with dissolve
    pause
    show expression "backgrounds/location_home_dining_under.jpg"
    hide table
    hide diane
    show diane dinner_under_hand
    jenny "( !!! )" with hpunch
    pause
    scene location_home_dining
    show anon b_dinner_sitting_look_left a_touch2 f_surprised_teeth_left od_dinner_sitting_boner zorder 0
    show diane b_dinner_open a_hand3 f_annoyed_left
    show old_debbie 64 at Position(xpos=880)
    show table 1 zorder 2
    if M_jenny.finished_state(S_jenny_catch_her_jilling) or store._in_replay is not None:
        show jenny f_gross b_dinner_casual a_idle:
            xoffset -250
        with dissolve
        jenny "( ... )"
    else:
        show jenny b_dinner_casual f_surprised a_idle:
            xoffset -250
        with dissolve
        jenny "( What the fuck... )"

    show old_debbie 65
    show diane f_normal
    debbie "So have you had any luck finding a new workplace?"

    show old_debbie 64
    show jenny b_dinner_casual_bending with dissolve
    diane "Hmm?"

    show anon f_normal a_idle
    show diane a_touch1
    with dissolve
    diane "Oh, uhh... No, unfortunately there just isn't anything available near town."

    show diane a_touch
    show old_debbie 64d
    show anon b_dinner_sitting
    debbie "Please tell me you aren't really gonna move away from us..."

    show jenny f_gross b_dinner_casual a_idle
    show old_debbie 64c
    show diane a_touch1
    show anon b_dinner_sitting_look_left
    with dissolve
    diane "Well, not if I can help it!"

    show jenny f_surprised
    diane "{b}[firstname]{/b} actually came up with a good idea the other day..."

    show old_debbie 65
    show jenny f_normal_closed a_facepalm with dissolve
    debbie "Oh ya?"

    show old_debbie 64
    diane "... Why buy a barn outside of town that doesn't even fit my business model?"

    diane "Wouldn't it be much better to build a custom one on the land I already own?"

    show old_debbie 64b
    show anon b_dinner_sitting
    debbie "Hmm?"

    show old_debbie 65
    debbie "You don't have enough land to build a barn, {b}Diane{/b}..."

    show old_debbie 64
    show anon b_dinner_sitting_look_left
    diane "Well no, not yet..."

    diane "... But once I demolish the house, I think-"

    show old_debbie 67 with dissolve
    show anon b_dinner_sitting
    debbie "You're gonna demolish your house?!"

    show old_debbie 64c with dissolve
    show anon b_dinner_sitting_look_left
    diane "Tentu, kenapa tidak?"

    show old_debbie 65
    show anon b_dinner_sitting
    debbie "But..."

    debbie "... It's such a nice house!"

    show old_debbie 64
    show diane f_laugh
    show anon b_dinner_sitting_look_left
    diane "Oh, it's not that nice..."

    show diane f_normal
    diane "... And besides, it's way too big for just little old me."

    show old_debbie 65
    show anon b_dinner_sitting
    debbie "Okay, but where will you live?"

    show old_debbie 64
    show anon b_dinner_sitting_look_left
    diane "Ehh, I'm not certain about that part yet..."

    diane "... I mean, I'm sure I can find something but I don't really have time to drag my feet on this."

    diane "If I'm gonna do it, I'll have to start construction right away!"

    diane "Otherwise, I risk losing my customer base."

    debbie "..."
    show old_debbie 65
    show anon b_dinner_sitting
    debbie "Do you even know anyone that's capable of building something like that?"

    show old_debbie 64
    show anon b_dinner_sitting_look_left
    diane "Tentu saja!"

    diane "One of my best customers is married to a carpenter."

    anon "Hmm?"

    anon "Oh, you mean {b}Annie{/b}'s dad?"

    diane "Yeah, his name is {b}Richard{/b}, right?"

    anon "Ya."

    anon "He doesn't seem like a very nice guy though."

    show diane a_touch
    diane "Well, that's alright."

    diane "I don't need him to be nice!"

    diane "I just need him to be competent..."

    diane "... And cheap!"

    show diane f_laugh a_touch1
    show old_debbie 66
    diane "Haha!"

    debbie "Haha!"

    show diane f_normal
    show old_debbie 65
    show anon b_dinner_sitting
    debbie "Well, you can always stay here with us while you look for a new place, you know?"

    show old_debbie 64
    show jenny f_surprised with dissolve
    jenny "( !!! )"
    show jenny f_gross
    show anon f_surprised_left
    show diane a_normal with dissolve
    jenny "Apa?!"

    diane "Oh, I don't want to be a bother..."

    show old_debbie 65
    show anon f_normal
    debbie "It's no bother!"

    debbie "You're as good as family and more than welcome to stay as long as you need!"

    show old_debbie 64
    show anon f_surprised_left
    jenny "{b}Mom{/b}, I really don't think it's a good idea... She-"

    show diane f_annoyed_left
    diane "Shh, nobody's talking to you!"

    show diane f_normal
    show old_debbie 65
    show anon f_normal
    debbie "Well, I think it's a wonderful idea!"

    debbie "It'll give you kids a chance to bond with {b}Diane{/b}."

    debbie "Plus we could really use the extra help around here..."

    debbie "... Even if it's only temporary."

    show old_debbie 64
    show anon f_surprised_left
    jenny "But where's she gonna sleep?!"

    show old_debbie 65
    show anon f_normal
    debbie "We'll figure something out."

    show old_debbie 64
    show anon b_dinner_sitting_look_left
    diane "The couch will suit me just fine."

    show jenny f_eyeroll
    show anon f_surprised_left
    jenny "Ugh, this is a stupid fucking idea!"

    show jenny f_gross
    show diane f_annoyed_left
    diane "Hey, don't talk to your mother like that!"

    jenny @ -m_talk "..."
    jenny "Apa pun."

    jenny "I'll be in my room."

    show diane zorder 1
    show jenny b_dinner_walking zorder 0 with dissolve
    pause
    hide jenny with dissolve
    pause
    show anon f_normal
    show diane f_normal
    diane "Sheesh, that girl needs to learn some respect..."

    show old_debbie 65
    show anon b_dinner_sitting
    debbie "Oh, {b}Diane{/b}... leave it be."

    show old_debbie 64
    show anon b_dinner_sitting_look_left
    diane "I'm serious..."

    diane "... Our parents would have never let us talk to them like that!"

    show old_debbie 65
    show anon b_dinner_sitting
    debbie "It's just a phase..."

    debbie "... She'll got out of it."

    show old_debbie 64
    show anon b_dinner_sitting_look_left
    diane "Hmph, if you say so..."

    show anon b_dinner_sitting
    anon "So {b}Diane{/b} is really going to live with us?"

    show old_debbie 65
    debbie "Tentu!"

    show old_debbie 64
    show anon b_dinner_sitting_look_left
    diane "Just give me a couple days to get the construction plans sorted out."

    show old_debbie 66
    show anon b_dinner_sitting
    debbie "Oh, ini sangat mengasyikkan!"

    show old_debbie 65
    show anon b_dinner_sitting_look_left
    debbie "It'll be just like those sleepovers we used to have when we were girls!"

    show diane f_laugh
    show old_debbie 66
    diane "Ha ha ha!"

    debbie "Ha ha ha!"

    scene black with fade
    hide diane
    hide anon
    hide table
    hide old_debbie

    scene expression background(l=L_home_entrance, t=3)
    show diane b_classy
    show old_debbie 91f
    show player 203 at left
    with dissolve
    diane "Well, I guess I'll head home and start packing!"

    show old_debbie 92f
    debbie "Saya tidak sabar!"

    show old_debbie 91f
    show diane f_laugh
    diane "Hehe, me neither!"

    hide old_debbie
    show diane b_dinner_hug4
    with dissolve
    diane "I'll see you really soon."

    show diane b_dinner_hug3
    debbie "Be careful going home!"

    show old_debbie 91f
    show diane b_classy f_normal
    with dissolve
    diane "I always am."

    show old_debbie 91 at Position (xoffset=100)
    hide player
    show diane b_dinner_hug2
    with dissolve
    diane "Come by the house soon, {b}[firstname]{/b}."

    diane "I'll definitely need your help with all this."

    show diane b_dinner_hug1
    player_name "Y-ya, oke."

    show old_debbie 91f
    show player 13 at left
    show diane b_classy f_shamed_smile
    with dissolve
    diane "And tell the spoiled princess I said bye."

    show diane f_normal
    show old_debbie 93f
    debbie "Hehe, aku akan melakukannya."

    hide old_debbie
    hide diane
    hide player
    with dissolve
    $ persistent.cookie_jar["Diane"]["unlocked"] = True
    $ persistent.cookie_jar["Diane"]["gallery"]["03_unlocked"] = True
    $ renpy.end_replay()
    return

label kitchen_diane_debbie_dinner_outfit:
    pause
    debbie "Oh!"

    debbie "{b}[firstname]{/b}, before you go, do you have a second to look at something?"

    show player 14
    show old_debbie 61
    player_name "Of course, {b}[deb_name]{/b}. What do you need?"

    show player 1
    show old_debbie 62
    debbie "I have a new outfit for dinner tonight and I wanted to get your opinion."

    debbie "Let me go put it on real fast."

    hide old_debbie with dissolve
    scene home_livingroom_b
    show player 14
    player_name "I'm excited to see {b}[deb_name]{/b} all dressed up!"

    show player 11
    debbie "Sayang!"

    debbie "I'm ready!"

    show player 2
    player_name "Coming!"

    hide player with dissolve
    return

label kitchen_diane_meet_debbie_kitchen:
    scene location_home_kitchen_day_blur
    show old_debbie 2 at right with dissolve
    show player 203 at left with dissolve
    debbie "Itu dia!"

    show old_debbie 3
    debbie "I need your help with something..."

    show old_debbie 2
    show player 11
    debbie "{b}Diane{/b} is coming over for dinner tonight."

    debbie "... And I need you to {b}pick up some sea trout down at the pier{/b}."

    debbie "I want to cook her something special and sea trout is her absolute favorite!"

    show old_debbie 1
    show player 2
    player_name "That's a nice surprise!"

    player_name "It'll be good for her to get out of her house for a while."

    player_name "I worry about her sometimes... All alone over there."

    player_name "I'll {b}swing by the pier and grab some sea trout{/b} on my way home."

    scene homekitchen
    show player 1 at left
    show old_debbie 62 at right
    with dissolve
    debbie "Terima kasih sayang."

    return

label kitchen_sis_telescope_1:
    scene homekitchen
    show player 1 at left
    show old_debbie 2 at right
    with dissolve
    debbie "Hey, sweetie!"

    debbie "Hungry for some breakfast?"

    show old_debbie 51 at Position(xpos=1025)
    show player 10
    player_name "I don't know If I have time, {b}[deb_name]{/b}."

    if game.timer.is_weekend():
        player_name "I have to meet {b}Erik{/b} at his house..."

    else:
        player_name "I'm running late for school."

    show player 11
    show old_debbie 52
    debbie "Honey, you have to eat!"

    show player 11
    if game.timer.is_weekend():
        debbie "I don't care if your friend {b}Erik{/b} has to wait all day..."

    else:
        debbie "I don't care if your school calls me to complain about you being late..."

    show player 1
    debbie "You can't just go out on an empty stomach!"

    show player 14
    show old_debbie 51
    player_name "I guess I could take a few minutes to eat something..."

    show player 1
    show old_debbie 2
    debbie "I prepared some cereal for you in the {b}dining room{/b}."

    hide player
    hide old_debbie
    with dissolve
    return

label kitchen_mom_start:
    scene expression player.location.background_blur
    show debbie
    show anon with dissolve
    debbie "Good morning, sweetie! I made you some breakfast!"

    debbie "I thought you'd like something special for your first day back at school."

    anon "Thanks {b}[deb_name]{/b}, but I'm not sure I have time."

    debbie "You're sure? I made your favorite..."

    debbie "... Happy face pancakes with three strips of baaaacon!"

    anon "Ya ampun..."

    anon @ f_thinking a_thinking -m_talk "..."
    anon "No, I really shouldn't..."

    anon "I think {b}Erik{/b} overslept again and I don't wanna be late on my first day back."

    debbie @ f_laugh "Hah, again huh?"

    debbie "Well, I guess you'd better get a move on then."

    anon "Yeah, thanks anyways, {b}[deb_name]{/b}."

    show anon with dissolve:
        flip
        xoffset -500
    debbie "My pleasure, sweet- Oh! Wait!"

    show anon with dissolve:
        unflip
        xoffset 0
    anon @ -m_talk "Hmm?"

    debbie @ f_laugh "I nearly forgot!"

    debbie "I spoke with my friend {b}Diane{/b} yesterday, and she mentioned that she could use some {b}help with her garden{/b}."

    debbie "She asked if you might be willing?"

    anon f_worried "Apa?!"

    anon "I don't know anything about gardening, {b}[deb_name]{/b}..."

    debbie @ f_laugh "Oh c'mon, it's easy! {b}Diane{/b} will teach you, and if you do a good job, she'll pay you as well!"

    debbie "It could be a good way to {b}earn a little extra money for college{/b}, don't you think?"

    anon "Ya, menurutku."

    anon f_normal "I'll swing by her place after school today."

    debbie "Atta' boy!"

    hide anon
    show debbie b_robe_hug1
    with dissolve
    debbie "I know these last few weeks have been hard..."

    debbie "But your father would want you to carry on, you know?"

    debbie "You'll get through this. I promise things will get better."

    show debbie b_robe_hug2
    anon "Yeah, I-I know. Thanks, {b}[deb_name]{/b}..."

    show debbie b_robe_hug1
    debbie "Chin up, sweetie! I'm here for you."

    hide debbie with dissolve
    return

label kitchen_mom_dinner:
    scene location_home_kitchen_day_blur
    show old_debbie 2 at right with dissolve
    show player 203 at left with dissolve
    debbie "Itu dia!"

    show old_debbie 3
    debbie "I need your help with something..."

    show old_debbie 2
    show player 11
    debbie "My friend {b}Diane{/b} is coming over for dinner tonight."

    debbie "... And I need you to {b}pick up some sea trout down at the pier{/b}."

    debbie "I want to cook her something special and it's her absolute favorite!"

    show old_debbie 1
    show player 2
    player_name "Oh, {b}Diane{/b} is coming over? That's a nice surprise!"

    player_name "It'll be good for her to get out of her house for a while."

    player_name "I worry about her sometimes... All alone over there."

    player_name "I'll {b}swing by the pier and grab some sea trout{/b} on my way home."

    scene homekitchen
    show player 1 at left
    show old_debbie 62 at right
    with dissolve
    debbie "{b}[firstname]{/b}, before you go, do you have a second to look at something?"

    show player 14
    show old_debbie 61
    player_name "Of course, {b}[deb_name]{/b}. What do you need?"

    show player 1
    show old_debbie 62
    debbie "I have a new outfit for dinner tonight and I wanted to get your opinion."

    debbie "Let me go put it on real fast."

    hide old_debbie with dissolve
    scene home_livingroom_b
    show player 14
    player_name "I'm excited to see {b}[deb_name]{/b} all dressed up!"

    show player 11
    debbie "Sayang!"

    debbie "I'm ready!"

    show player 2
    player_name "Coming!"

    hide player with dissolve
    return

label kitchen_mom_debt_call:
    scene expression player.location.background_blur
    show debbie f_angry a_phone:
        flip
        xoffset 500
    debbie "No, I've told you already!"

    debbie "I don't know anything about any money..."

    show anon f_worried with dissolve
    pause
    debbie "That's right, I had no idea he was involved in any of this!"

    pause
    debbie "Apa?!"

    debbie f_sad "Y-you can't-"

    pause
    debbie "I don't have it!!"

    pause
    debbie f_angry @ -m_talk "..."
    debbie "Don't you threaten me!"

    anon f_shock "!!!"
    anon f_worried @ -m_talk "( Someone is threatening her? )"

    pause
    debbie "I don't have to listen to this."

    pause
    debbie "I'm hanging up now."

    debbie "Don't call back here again."

    pause
    debbie "JUST LEAVE US ALONE!!!"

    show debbie a_phone_facepalm f_sad_closed with dissolve
    pause
    anon "{b}[deb_name]{/b}?"

    debbie @ -m_talk "Hmm?"

    show debbie a_phone_down f_sad with dissolve:
        unflip
        xoffset 0
    debbie "Oh, hey there sweetie."

    anon "What was that all about?"

    debbie "Oh, it's nothing."

    anon "Apa kamu yakin?"

    anon "It sounded pretty bad..."

    debbie "Just some people making up a bunch of nonsense."

    anon @ -m_talk "..."
    anon "Did {b}Dad{/b} owe people money or something?"

    anon "Because I can find a job and-"

    debbie "No, no, don't be silly."

    debbie "You need to focus on school and save your money for tuition."

    anon "{b}[deb_name]{/b}, seriously, I want to help."

    anon "I'm old enough."

    anon "You don't have to carry the burden all on your own."

    debbie "Oh sayang..."

    show anon b_empty
    show debbie b_robe_hug_mc
    with dissolve
    debbie "You're such a wonderful boy!"

    debbie "It's nothing for you to worry about, okay?"

    show debbie b_robe f_normal
    show anon -b_empty
    with dissolve
    debbie "Just a simple misunderstanding, I promise."

    anon f_normal "O-oke."

    pause
    debbie "Did you go see {b}Diane{/b} about that gardening work, like I told you?"

    anon "Yeah, I went by to see her after school."

    debbie "And how was it?"

    anon @ a_behind_head "Umm, it was okay."

    anon "Her garden is quite a bit bigger than I expected."

    debbie @ f_laugh "Hehe, I can imagine."

    anon f_tired "It was a lot of work."

    anon "I'm pretty exhausted."

    debbie "Oh, you poor thing."

    debbie "Do you want me to fix you something to eat?"

    anon "Tidak, tidak apa-apa."

    anon "I think I'm just going to go to bed."

    debbie "Baiklah."

    debbie "Sweet dreams."

    anon @ a_wave "Good night, {b}[deb_name]{/b}."

    hide anon with dissolve

    $ player.go_to(L_home_entrance)
    scene expression player.location.background_blur with fade
    show anon f_worried with dissolve:
        flip
    anon @ -m_talk "( Hmm, {b}[deb_name]{/b} said there's nothing to worry about, but she's just putting on a brave face... I can tell. )"

    anon f_thinking a_thinking @ -m_talk "( I wonder who was on the other end of that phone? )"

    anon @ -m_talk "( I've got a bad feeling about this... )"

    hide anon with dissolve
    return

label kitchen_mom_diane_visit:
    scene homekitchen_secret
    show diane b_kitchen
    show old_debbie 59f at Position(xpos=0.3318,ypos=1.000)
    diane "... I don't see the problem. Isn't it a good thing that he's helping you around the house?"

    show old_debbie 60f
    debbie "I know, it's just..."

    debbie "He's been so... affectionate towards me lately..."

    show diane f_laugh
    show old_debbie 59f
    diane "That's not surprising, he just lost the only family he ever had..."

    show diane f_normal
    diane "He probably just needs someone he can feel close with..."

    diane "Especially with all this other stuff that's been happening to you guys."

    show old_debbie 17f at Position(xpos=0.3318,ypos=1.1130)
    debbie "It's not that. There's more to it! It's the way he looks at me, you know?"

    show old_debbie 59f at Position(xpos=0.3318,ypos=1.000)
    show diane f_surprised
    diane @ -m_talk "..."
    show diane f_normal
    diane "Apa maksudmu?"

    show old_debbie 60f
    debbie "Well, a little while ago I... I started noticing things..."

    show old_debbie 59f
    diane "... Like?"

    show old_debbie 60f
    debbie "Like how he's always getting hard around me..."

    debbie "... And touching me... in certain ways."

    show diane f_surprised
    show old_debbie 59f
    diane @ -m_talk "..."
    show old_debbie 60f
    debbie "And the other day, I found him playing with himself; in my bed!"

    debbie "... With my underwear!"

    show diane f_normal
    show old_debbie 59f at Position(xpos=0.3318,ypos=1.000)
    diane "What did you do?!"

    show old_debbie 60f
    debbie "We talked about it!"

    debbie "I told him not to do that kind of stuff in my room, but..."

    show old_debbie 59f
    diane "But, what?"

    show old_debbie 60f at Position(xpos=0.3318,ypos=1.000)
    debbie "I caught him again! He apologized and started talking about urges that he couldn't control..."

    show old_debbie 59f
    diane "Okay, so what did you say to that?"

    show diane f_surprised
    show old_debbie 17f at Position(xpos=0.3318,ypos=1.1130)
    debbie "... I kinda... let him finish."

    show diane f_normal
    show old_debbie 20f at Position(xpos=0.3318,ypos=1.1130)
    diane "You watched him masturbate?"

    show old_debbie 60f at Position(xpos=0.3318,ypos=1.000)
    debbie "I didn't know what to do!"

    debbie "I thought maybe if he just got it out of his system..."

    debbie "... You know?"

    show old_debbie 59f
    diane "That's so naughty..."

    show old_debbie 60f
    debbie "There's more..."

    show old_debbie 59f
    diane "More?!"

    diane "You're serious?!"

    diane "Tell me!"

    show diane f_surprised
    show old_debbie 60f
    debbie "{b}Diane{/b}..."

    show diane f_normal
    show old_debbie 59f
    diane "{b}[deb_name]{/b}, tell me!"

    show diane f_surprised
    show old_debbie 60f
    debbie "... We've been taking showers together."

    show diane f_normal
    show old_debbie 59f
    diane "Wah..."

    show diane f_teasing
    diane "... How is he?"

    show diane f_surprised
    show old_debbie 60f
    debbie "{b}Diane{/b}!!"

    show diane f_laugh
    show old_debbie 59f
    diane "Apa?!"

    show diane f_thinking
    diane "Don't act like a prude! We both know you're dying to tell me!"

    show diane f_surprised
    show old_debbie 60f
    debbie "... {i}*Sigh*{/i}"

    show diane f_teasing
    show old_debbie 59f
    diane "Did you... touch him?"

    show diane f_smirk
    show old_debbie 60f
    debbie "... Ya."

    debbie "I kinda, jerked him off..."

    show diane f_teasing
    show old_debbie 59f
    diane "All the way?"

    show diane f_smirk
    show old_debbie 60f
    debbie "... Until he came, yeah."

    show old_debbie 59f
    if not M_diane.finished_state(S_diane_drunken_garden_work):
        show diane f_teasing
        diane "So how is it?"

        show diane f_smirk
        show old_debbie 60f
        debbie "... How is what?"

        show diane f_teasing
        show old_debbie 59f
        diane "His {i}dick{/i}, {b}[deb_name]{/b}! Is it big?"

        show diane f_smirk
        show old_debbie 60f
        debbie "( !!! )"
        show old_debbie 59f
        debbie "..."
        show diane f_explain
        diane "Don't get shy on me now, girl. Spit it out!"

        show old_debbie 60f
        show diane f_smirk
        debbie "{b}Diane{/b}, he's got the biggest... {i}dick{/i} I've ever seen!"

        show diane f_teasing
        show old_debbie 59f
        diane "... You don't say?!"

    show diane f_laugh
    diane "I'm surprised you stopped at the handjob..."

    show diane f_smirk
    show old_debbie 16f at Position(xpos=0.3318,ypos=1.1130)
    debbie "{b}Diane{/b}, he's just a kid!"

    show diane f_teasing
    show old_debbie 15f
    diane "Pfft, he's in college!"

    show diane f_smirk
    show old_debbie 16f
    debbie "Yeah, but I'm old enough to be his mother!"

    show diane f_laugh
    show old_debbie 15f
    diane "... But you aren't his mother, {b}[deb_name]{/b}!"

    show diane f_normal
    show old_debbie 16f
    debbie "Oh, I dunno, {b}Diane{/b}..."

    show diane f_surprised
    show old_debbie 15f
    diane "He obviously wants to."

    show diane f_normal
    show old_debbie 16f
    debbie "Please, tell me I'm not doing something terribly wrong here..."

    show old_debbie 15f
    diane "It's your decision, but..."

    diane "I think you should relax and enjoy it a little. Who cares about the age difference?"

    show old_debbie 16f
    debbie "Really? You don't think it's wrong?"

    show old_debbie 15f
    diane "Nope. I don't see the harm in it!"

    show old_debbie 16f
    debbie "I suppose we aren't hurting anybody... and we're both consenting adults."

    show diane f_laugh
    show old_debbie 15f
    diane "Plus this is all really HOT!"

    show diane f_normal
    show old_debbie 16f
    debbie "You are such a bad influence! I don't know why I listen to you!"

    show old_debbie 15f
    diane "... Because you know I'm right! Just give it a chance. Who knows maybe it was meant to be?"

    show old_debbie 62f at Position(xpos=0.3318,ypos=1.000)
    debbie "Yeah, I suppose anything is possible..."

    show old_debbie 61f
    diane "Alright, well, I'd better head home. It's getting late."

    show diane f_teasing
    diane "We'll continue this another time. I want all the juicy details for my spank bank!"

    show diane f_normal
    show old_debbie 62f
    debbie "{b}Diane{/b}! You're terrible!"

    debbie "Why don't you come by for dinner sometime? I'd love to see you more often!"

    show old_debbie 61f
    diane "I'm always down for dinner, {b}[deb_name]{/b}. Just as long as I'm not the one doing the cooking!"

    diane "Good luck, honey."

    scene expression L_home_entrance.background_blur
    show player 5
    player_name "( That... was a lot to take in. )"

    player_name "( {b}[deb_name]{/b} seemed really conflicted about all of this... )"

    show player 203
    player_name "( She said she's enjoying it, though. )"

    player_name "( Either way, I'm glad {b}Diane{/b} thinks it's okay for us to be doing these things! )"

    return

label kitchen_mom_kissing_practice:
    show player 2 at left
    show old_debbie 14b at right
    player_name "Aww, c'mon {b}[deb_name]{/b}!"

    player_name "You're the one who said I need to get out and start dating."

    player_name "It would definitely help if I knew how to kiss a girl properly, wouldn't it?"

    show player 1
    debbie "..."
    show old_debbie 13
    debbie "... Well."

    debbie "Y-yeah, I suppose I could give you a few pointers."

    show old_debbie 14
    show player 2
    player_name "I would really appreciate it, {b}[deb_name]{/b}."

    show player 1
    show old_debbie 73 at Position(xpos=0.85, ypos=1.0) with dissolve
    debbie "O-okay, umm... Come in close to me."

    show player 227c at Position(xpos=0.25, ypos=1.0) with dissolve
    show old_debbie 72
    player_name "Baiklah."

    show player 227
    show old_debbie 73
    debbie "Good. Now, lean in, that's it."

    show player 227c zorder 1 at Position(xpos=0.30, ypos=1.0) with dissolve
    show old_debbie 72 zorder 0 at Position(xpos=0.80, ypos=1.0) with dissolve
    player_name "Oke."

    show player 227
    show old_debbie 73
    debbie "... Close your eyes and gently press your lips against mine..."

    hide player
    show old_debbie 79 at Position(xpos=0.70, ypos=1.0) with dissolve
    pause
    show old_debbie 80
    pause
    show old_debbie 79
    debbie "MM."

    show old_debbie 78 at Position(xpos=0.80, ypos=1.0) with dissolve
    show player 227 at Position(xpos=0.30, ypos=1.0) with dissolve
    pause
    show player 227c
    player_name "Bagaimana tadi?"

    show player 227
    show old_debbie 77
    debbie "... Wow."

    show player 227c
    show old_debbie 76
    player_name "Bad?"

    show player 227
    show old_debbie 73
    debbie "N-no. That was quite good!"

    show player 227c
    show old_debbie 72
    player_name "Benar-benar?!"

    show player 227
    show old_debbie 73
    debbie "Yeah. Are you sure this is your first time?"

    show player 227c
    show old_debbie 72
    player_name "Heh, yeah. Do you have any pointers?"

    show player 227
    debbie "..."
    show old_debbie 73
    debbie "Baiklah, mari kita lihat..."

    debbie "Oh, aku tahu!"

    debbie "Kiss me again and I'll show you a little trick!"

    hide player
    show old_debbie 79 at Position(xpos=0.70, ypos=1.0) with dissolve
    pause
    show old_debbie 80
    pause
    show old_debbie 79
    pause
    show old_debbie 80c
    player_name "( !!! )" with hpunch
    show old_debbie 76 at Position(xpos=0.80, ypos=1.0) with dissolve
    show player 227 at Position(xpos=0.30, ypos=1.0) with dissolve
    debbie "..."
    show player 227c
    player_name "Wah!"

    player_name "That thing you did with your tongue, that was so cool!"

    show player 227
    show old_debbie 75
    debbie "Hehe, ya."

    show old_debbie 73
    debbie "It's just a little something I picked up a while back..."

    show player 227c
    show old_debbie 72
    player_name "Hmm, can I try it?"

    show player 227
    show old_debbie 73
    debbie "Oh... Uh."

    show player 227c
    show old_debbie 72
    player_name "Silakan?"

    show player 227c
    show old_debbie 73
    debbie "Y-yeah... Sure!"

    hide player
    show old_debbie 79 at Position(xpos=0.70, ypos=1.0) with dissolve
    pause
    show old_debbie 80
    pause
    show old_debbie 79
    pause
    show old_debbie 80b
    debbie "( !!! )" with hpunch
    show old_debbie 78 at Position(xpos=0.80, ypos=1.0) with dissolve
    show player 227 at Position(xpos=0.30, ypos=1.0) with dissolve
    debbie "..."
    show player 227c
    player_name "How was that?!"

    show player 227
    debbie "Hmm..."

    show player 227c
    player_name "{b}[deb_name]{/b}?"

    show player 227
    show old_debbie 77
    debbie "Oh, sorry!"

    show old_debbie 75
    debbie "That was REALLY good, sweetie!"

    debbie "I mean, wow! You're gonna be quite the little heartbreaker once you get out into the dating world!"

    show player 227c
    show old_debbie 76
    player_name "Really? Thanks, {b}[deb_name]{/b}!"

    show player 227
    debbie "Mmmhmm."

    hide player
    show old_debbie 79 at Position(xpos=0.70, ypos=1.0) with dissolve
    pause
    show old_debbie 80
    pause
    show old_debbie 79
    pause
    show old_debbie 78 at Position(xpos=0.80, ypos=1.0) with dissolve
    show player 233 at Position(xpos=0.30, ypos=1.0) with dissolve
    pause 
    show old_debbie 77
    pause
    show old_debbie 74
    debbie "Oh!"

    debbie "Oh my..."

    show player 230
    player_name "..."
    show player 232
    player_name "Maaf, {b}[deb_name]{/b}."

    player_name "I didn't mean to..."

    show player 231
    show old_debbie 75
    debbie "Hehe, it's okay, sweetie. It's perfectly understandable."

    show old_debbie 73
    debbie "We'd better take a break though."

    show player 232
    show old_debbie 72
    player_name "... Yeah. O-okay."

    player_name "Do you think, maybe, we could do this again sometime?"

    show player 231
    debbie "..."
    show player 232
    player_name "You know... Just for practice?"

    show player 231
    show old_debbie 73
    debbie "I suppose that would be okay."

    debbie "Just to practice though!"

    show player 232
    show old_debbie 72
    player_name "Ya, tentu saja!"

    show player 231
    show old_debbie 73
    debbie "Alright. Feel free to ask me anytime."

    show player 232
    show old_debbie 72
    player_name "Terima kasih, {b}[deb_name]{/b}!"

    show player 231
    show old_debbie 73
    debbie "Tidak masalah, {b}[firstname]{/b}."

    show player 232
    show old_debbie 72
    player_name "Sampai jumpa!"

    hide old_debbie with dissolve
    show player 1 at Position(xpos=0.55, ypos=1.0) with dissolve
    player_name "..."
    show player 21f at Position (xpos=0.5, ypos=1.0) with dissolve
    player_name "Itu luar biasa!"

    return

label kitchen_mom_dishes:
    scene expression player.location.background_blur with None
    show old_debbie 116 at right
    with dissolve
    pause
    show old_debbie 117 at Position(xpos=1014)
    pause
    show old_debbie 116 at right
    pause
    show old_debbie 117 at Position(xpos=1014)
    pause
    show old_debbie 116 at right
    show player 1 at left with dissolve
    pause
    show old_debbie 117 at Position(xpos=1014)
    pause
    show old_debbie 119 at Position(xpos=1014)
    debbie "Oh, hey, sweetie!"

    show old_debbie 120
    show player 14
    player_name "Hai, {b}[deb_name]{/b}!"

    show old_debbie 119
    show player 1
    debbie "Anda butuh sesuatu?"

    debbie "I'm just finishing up the dishes..."

    show old_debbie 120
    return

label kitchen_mom_dishes_yes:
    show old_debbie 118
    show player 14
    player_name "Why don't you take a break for a while?"

    player_name "I'll dry the rest."

    show old_debbie 119
    show player 1
    debbie "That's very sweet but you don't have to do that."

    show old_debbie 118
    show player 14
    player_name "Nah, it's fine. I'm bored anyways."

    show old_debbie 119
    show player 1
    debbie "Heh, well, alright. If you're bored anyways..."

    show player 272
    show old_debbie 62
    debbie "Just dry and store them away in the cupboard."

    show player 273
    show old_debbie 61
    player_name "Akan dilakukan."

    show old_debbie 63
    show player 272
    debbie "Thanks for helping out around here, {b}[firstname]{/b}."

    show player 274
    show old_debbie 61
    player_name "My pleasure, {b}[deb_name]{/b}."


    scene location_home_cutscene01
    show text _ ("I don't think {b}[deb_name]{/b} had ever had help with dishes before...\nShe told me her late husband never did any work around the house and my dad only really helped with yardwork or broken appliances.\nShe stayed with me in the kitchen until I was finished and we had a nice long chat.\nIt was nice getting to know {b}[deb_name]{/b} better...") as caption
    with fade
    pause

    scene black with dissolve
    return

label kitchen_mom_dishes_no:
    show player 14 at left
    show old_debbie 120 at Position(xpos=1014)
    player_name "Okay. I'll come back later, then."

    return

label kitchen_diane_debbie_evening_visit:
    scene expression "backgrounds/location_home_kitchen_secret.jpg"
    show diane b_kitchen
    show old_debbie 165bf at Position(xpos=0.3318,ypos=1.000)
    with dissolve
    debbie "And you're getting plenty of rest?"

    show old_debbie 169bf
    show diane f_lookup
    diane "Yes, Mom."

    show diane f_smirk
    show old_debbie 165f
    debbie "Oh, hush!"

    show old_debbie 164f
    show diane f_laugh
    diane "Haha!"

    show diane f_normal
    show old_debbie 165f
    debbie "I just worry about you is all."

    show old_debbie 164f
    diane "I know, {b}[deb_name]{/b} and I really do appreciate it..."

    diane "... But I've got everything under control, I promise."

    diane "I've settled into a nice work schedule and {b}[firstname]{/b} has been making sure I stick to it."

    show old_debbie 165bf
    debbie "He doesn't know... about the, you know..."

    show old_debbie 169bf
    show diane f_shamed_smile
    diane "Mmm, yeah..."

    diane "... About that-"

    show diane f_shamed
    show old_debbie 165bf
    debbie "{b}Diane{/b}!!!"

    show old_debbie 169bf
    show diane f_shamed_smile
    diane "I didn't mean for him to find out!"

    diane "He sorta... caught me... that night you sent him over with the pie."

    show diane f_shamed
    show old_debbie 169bf
    debbie "..."
    show diane f_smirk
    diane "Thanks for that, by the way!"

    show old_debbie 164bf at Position (xoffset=10) with dissolve
    debbie "..."
    show diane f_laugh
    diane "Your pie really was delicious, {b}[deb_name]{/b}."

    show diane f_smirk
    show old_debbie 165bf with dissolve
    debbie "You know, if you'd told me about your little side business from the start, I'd never have sent him over to tend your garden in the first place!"

    show old_debbie 169bf
    show diane f_laugh
    diane "Haha, well... I guess it's a good thing I didn't tell you then, huh?"

    show diane f_smirk
    debbie "..."
    show diane f_normal
    diane "He's really shown an aptitude for it, you know?"

    diane "His thumb is even more green than mine!"

    debbie "..."
    show old_debbie 165bf
    debbie "You don't have him in there with you while you're doing it, do you?"

    show old_debbie 169bf
    show diane f_surprised_down
    diane "Uhh-"

    show diane f_shamed_smile
    diane "N-no... Not usually."

    show diane f_shamed
    show old_debbie 165bf
    debbie "{b}Diane{/b}!!!"

    show old_debbie 169bf
    show diane f_shamed_smile
    diane "Apa?!"

    show diane f_shamed
    diane "You know how he can be!"

    diane "So determined to help out with every little thing..."

    show diane f_shamed_smile
    diane "... He keeps popping his head in and asking to lend a hand!"

    show diane f_shamed_look
    diane "Then you went and got him all worked up about my health, and it's become practically impossible to keep him out!"

    show diane f_shamed
    show old_debbie 165bf
    debbie "I think it might be best if he stops working for you."

    show old_debbie 169bf
    diane "Oh, now you're being ridiculous!"

    show old_debbie 165bf
    debbie "It's not right for him to-"

    show old_debbie 169bf
    diane "He's not a little boy anymore, {b}[deb_name]{/b}!"

    show diane f_normal
    diane "An occasional glimpse of my tits isn't going to hurt him."

    debbie "..."
    if M_debbie.finished_state(S_debbie_diane_visit):
        show diane f_smirk
        diane "Besides, the stuff happening in my shed is far tamer than your little shower sessions with him!"

        show old_debbie 164bf at Position (xoffset=10)
        debbie "!!!" with hpunch
        show old_debbie 166df with dissolve
        debbie "Itu bukan-"

        show old_debbie 166cf
        debbie "{i}*Sigh*{/i} I should never have told you about that."

        show old_debbie 166ef
        show diane f_laugh
        diane "Haha, please!"

        show diane f_smirk
        diane "Who else do you have to discuss these things with?!"

        diane "Relax, I think it's super hot!"

        show old_debbie 165bf
        debbie "Ya, aku sadar."

        show old_debbie 169bf
    else:
        show diane f_normal
        diane "You're really making too big a deal of this, {b}[deb_name]{/b}."

        diane "{b}[firstname]{/b} is really mature for his age."

        debbie "..."
        show diane f_explain
        diane "He's been a perfect gentleman about the whole thing."

        show diane f_normal
        diane "You should spend more time with him and you'd see what I mean."

        show old_debbie 165bf
        debbie "You really think he can handle it?"

        show old_debbie 169bf
        show diane f_laugh
        diane "There's not a doubt in my mind."

        show diane f_normal
        show old_debbie 166bf
        debbie "( Hmm, maybe I {i}should{/i} spend more time with him... )"

        show old_debbie 169bf
    show diane f_normal
    diane "Look, I really can't afford to lose {b}[firstname]{/b} right now, {b}[deb_name]{/b}..."

    diane "... Not when my business is just taking off."

    debbie "..."
    show old_debbie 165bf
    debbie "Things are really going that well?"

    show old_debbie 169bf
    show diane f_laugh
    diane "Better than I ever imagined!"

    show diane f_normal
    diane "I'm already looking into expanding."

    show old_debbie 165bf
    debbie "What do you mean expand?"

    show old_debbie 169bf
    diane "Well, getting a proper work space for one thing."

    show old_debbie 165bf
    debbie "Workspace?"

    show old_debbie 169bf
    show diane f_laugh
    diane "Ya!"

    show diane f_thinking
    diane "I was looking at the most adorable little barn the other day, about two hours drive outside of town."

    show diane f_normal
    diane "I'll have to send you the pictures."

    show old_debbie 168f
    debbie "Barn?!"

    debbie "You can't be serious."

    show old_debbie 164f
    show diane f_explain
    diane "Heh, I'm dead serious."

    show diane f_normal
    diane "You know I've always wanted one."

    show old_debbie 165f
    debbie "Yeah, but we both know this isn't the type of livestock you envisioned filling it with."

    show old_debbie 164f
    diane "Itu benar."

    show diane f_smirk
    diane "This is even better!"

    show old_debbie 168f
    debbie "Oh my gosh, you're such a weirdo."

    show old_debbie 165f
    show diane f_laugh
    diane "Ha ha ha!"

    debbie "Ha ha ha!"

    show diane f_normal
    debbie "So where is this all going anyway?"

    debbie "Are you eventually gonna start looking for more women to join your little milk business?"

    show old_debbie 164f
    diane "Ya, mungkin..."

    diane "... I mean, I'm not there yet, but it's definitely something I'm considering."

    show diane f_smirk
    diane "Why, are you volunteering?"

    show old_debbie 168f
    debbie "Pfft, no way!"

    show old_debbie 164f
    show diane f_laugh
    diane "Ah, ayolah!"

    show old_debbie 165f
    debbie "Tidak uh!"

    debbie "I'm not getting mixed up with your kinky business ideas."

    show old_debbie 164f
    diane "Ugh, you are such a wet blanket sometimes..."

    diane "... But see, that's why I need {b}[firstname]{/b} to keep helping me!"

    diane "Nobody else will work as hard as he does."

    show diane f_thinking
    diane "At least nobody that I can afford to pay."

    show diane f_normal
    show old_debbie 169bf
    debbie "..."
    show old_debbie 165bf
    debbie "Benar."

    debbie "But I want you to promise me there won't be any funny business going on!"

    show old_debbie 169bf
    diane "Oh my gosh, stop worrying!"

    diane "I'll be on my best behavior, I promise."

    show old_debbie 169bf
    debbie "Hmmph."

    show old_debbie 169bf
    diane @ -m_talk "..."
    show old_debbie 165bf
    debbie "You're not really going to move two hours away from us, are you?!"

    show old_debbie 169bf
    diane "I don't have much choice."

    diane "{b}Mayor Rump{/b} bought up all the farm land around town and his people insist he's not willing to sell."

    diane "So I've been forced to look a bit further out."

    show old_debbie 165bf
    debbie "Gosh, what am I gonna do if you leave?"

    show old_debbie 169bf
    diane "Oh, don't get all boo-hooey yet."

    diane "There's still time and who knows, I might find something closer."

    debbie "..."
    show diane f_laugh
    diane "If you keep making that face, it's gonna freeze that way!"

    show diane f_normal
    show old_debbie 168f
    debbie "Hehe, diamlah!"

    show old_debbie 164f
    show diane f_laugh
    diane "Ha ha ha!"

    show diane f_surprised_down
    diane "Phew, look at the time..."

    show diane f_normal
    diane "... I've gotta get home and pump one more batch before bed."

    show old_debbie 165f
    debbie "Aww, but you've only just got here!"

    show old_debbie 164f
    show diane f_shamed_smile
    diane "I know, I'm sorry."

    show diane f_normal
    diane "I'll call you tomorrow, okay?"

    show old_debbie 165f
    debbie "Ya baiklah."

    hide old_debbie
    show debbie b_empty:
        flip
        xoffset 85
    show diane b_hug_deb:
        xoffset -228
    with dissolve
    debbie "Be careful going home."

    diane "Saya akan."

    show old_debbie 164f at Position(xpos=0.3318,ypos=1.000)
    show diane f_laugh b_casual a_idle:
        xoffset 0
    with dissolve
    diane "Don't forget to try that milk I brought you!"

    show diane f_normal
    show old_debbie 165f
    debbie "Ehh, we'll see."

    show old_debbie 164f
    diane "I'm serious, {b}[deb_name]{/b}!"

    diane "Put a splash in your morning coffee or something."

    diane "You'll be hooked, I'm telling ya!"

    show old_debbie 165f
    debbie "Goodbye, {b}Diane{/b}."

    show old_debbie 164f
    show diane f_laugh
    diane "Hah, see ya, {b}[deb_name]{/b}."

    scene black
    with fade
    hide diane
    hide old_debbie
    pause

    scene expression background(l=L_home_entrance, t=2)
    show player 5 at left with dissolve
    show diane b_casual f_smirk
    with dissolve
    diane "Oh, hey there {b}[firstname]{/b}!"

    diane "Are your ears burning?"

    show player 10
    player_name "Hmm?"

    show player 5
    diane "We were just talking about you in there."

    show player 29 with dissolve
    player_name "O-oh, yeah?"

    show player 3
    diane "You coming by tomorrow?"

    show player 29
    player_name "Entahlah, mungkin."

    show player 3
    diane "Well, I hope you do."

    hide player
    show diane b_kiss_casual
    with dissolve
    pause
    show player 21 at left
    show diane b_casual
    with dissolve
    diane "I'm gonna need those magic hands of yours for a big job real soon..."

    show player 28
    player_name "{i}*Gulp*{/i} O-oke."

    show player 21
    show diane f_laugh
    diane "hehe."

    diane "See ya, stud!"

    show diane f_smirk
    show player 29 with dissolve
    player_name "Bye, {b}Diane{/b}."

    hide player
    hide diane
    with dissolve
    return

label ano02_food_home_kitchen:
    scene expression player.location.background_blur
    show jenny f_upset a_juice:
        xoffset -100
    show debbie:
        xoffset 100
    with dissolve
    show anon with dissolve
    debbie "Good morning, sweetie."

    anon "Morning, {b}[deb_name]{/b}."

    anon "{b}[jen_name]{/b}."

    jenny @ f_eyeroll "Meh."

    pause
    anon "What smells so good?"

    show jenny f_drink a_juice_drink with dissolve
    debbie "Oh, I'm making a sausage and egg casserole."

    show jenny a_juice f_upset with dissolve
    anon @ f_laugh "That sounds amazing!"

    debbie "Well, there's plenty for everyone."

    debbie "Why don't you two go take a seat at the table and I'll bring you some."

    anon "Manis!"

    jenny "Ugh, no thanks."

    debbie f_sad "You don't want any?"

    show jenny f_angry with dissolve:
        flip
        xoffset 300
    jenny "I just told you I'm doing a juice cleanse!"

    anon f_skeptical "Juice cleanse?"

    anon "Apa itu?"

    show jenny f_upset with dissolve:
        unflip
        xoffset -100
    jenny "It means I'm only drinking juice for the next three days, dummy."

    anon f_worried "Oh-kay..."

    anon "Mengapa?!"

    jenny "I need to get rid of these love handles before beach season."

    anon "What love handles?"

    show debbie f_normal
    anon f_flirt "You look fine."

    jenny f_gross "Jangan kotor."

    show anon f_normal
    debbie "I don't think people do juice cleanses to lose weight, dear."

    show jenny f_eyeroll with dissolve:
        flip
        xoffset 300
    jenny "Umm, yes they do..."

    jenny f_upset "I was reading about it online."

    anon "Well, I think it sounds stupid."

    show jenny f_angry with dissolve:
        unflip
        xoffset -100
    jenny "You're stupid!"

    debbie f_angry "Enough!"

    show jenny f_angry_pouting
    show anon f_surprised
    debbie "I'm tired of you two fighting all the time!"

    jenny f_upset "He started it."

    anon f_worried "I did not!"

    debbie "I said, enough!"

    show anon f_sad_down
    "{i}*Ding Dong*{/i}"

    show anon f_worried
    debbie f_normal "Oh, that's probably the police lady coming to check in on us."

    jenny "Police lady?"

    debbie "{b}[firstname]{/b}, would you go and let her in please?"

    anon "Ya baiklah."

    hide anon with dissolve
    debbie "Terima kasih sayang."

    jenny "Why are the police stopping by to check in on us?"

    debbie f_sad "{i}*Huh*{/i}"

    scene black with fade
    pause 1
    $ player.go_to(L_home_entrance)
    scene expression player.location.background_blur
    show anon with dissolve:
        xoffset 300
    anon @ -m_talk "( A juice cleanse with apple juice... )"

    anon f_laugh "( What a moron. )"

    "{i}*Ding Dong*{/i}"

    anon f_worried "Yeah, yeah... I'm coming!"

    hide anon with dissolve
    return

label ano02_next_home_kitchen:
    scene expression player.location.background_blur
    show debbie f_sad
    show yumi a_notes:
        flip
        xoffset 100
    with dissolve
    debbie "{b}[jen_name]{/b} and I have a hair appointment on Tuesday."

    yumi "Down at Cindi Kim's?"

    show anon f_worried behind yumi with dissolve:
        xoffset -100
    debbie "Is that going to be a problem?"

    yumi "No, that'll be fine."

    pause
    yumi "Does your daughter go out much at night?"

    yumi "Like dancing with friends or anything?"

    debbie f_normal @ f_laugh "Oh, goodness no!"

    debbie "She spends most of her time on the phone, or upstairs with that computer of hers."

    show debbie f_sad
    yumi "Oke."

    pause
    show yumi f_normal_right
    anon "I guess I'm heading to school..."

    show yumi f_normal
    debbie @ -m_talk "Hmm?"

    debbie "Oh, no you're not!"

    debbie "You're not leaving this house with that maniac running around."

    show yumi f_normal_right
    anon "{b}[deb_name]{/b}, I'm already months behind in my classes."

    anon "You really want me to miss more?"

    yumi f_normal a_idle "He's right, ma'am."

    yumi "You can't let these crazies prevent you and your family from living your lives."

    debbie "Y-ya, tapi-"

    yumi "I assure you, we have a lot of patrols out combing the city for this guy."

    yumi "He will be perfectly safe."

    debbie @ -m_talk "..."
    debbie "Alright, just-"

    debbie "Be careful, okay?"

    show yumi f_normal_right
    anon "Aku akan menjadi."

    hide anon with dissolve
    show yumi f_normal
    debbie "This whole thing is making me a nervous wreck..."

    yumi f_concerned "Everything is going to be fine, ma'am."

    pause
    yumi a_notes "Now then, where were we?"


    $ player.go_to(L_home_entrance)
    scene expression player.location.background_blur with fade
    show anon f_worried with dissolve
    anon @ -m_talk "( I don't like this one bit. )"

    anon f_sad_down @ -m_talk "( {i}*Sigh*{/i} I need some air. )"

    hide anon with dissolve
    return

label ano02_next_home_kitchen.repeat:
    $ player.go_to(L_home_entrance)
    scene expression player.location.background_blur
    show anon f_worried with dissolve
    anon @ -m_talk "( I shouldn't interrupt them.. )"

    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
