label annies_house_first_time:
    scene expression player.location.background_blur with None
    show anon:
        xoffset 400
    show richard f_angry:
        flip
        xoffset 150
    show lucy f_sad:
        xoffset 100
    richard "No, I wanna know how the chair got broken, {b}Lucy{/b}?!"

    show anon f_worried
    lucy @ f_thinking "I dunno, dear..."

    lucy "{b}Johnny{/b} says they were playing tag and {b}Molly{/b} tripped and knocked it over."

    show lucy f_sad_down
    richard "So you were letting them run in the house, after I specifically told you not to let them do that."

    lucy "It was just an accident, dear."

    show lucy f_sad
    richard "I don't care, this is unacceptable!"

    richard "We have rules in the house for a reason... If they can't follow them, then they need to stay out!"

    show lucy f_confused
    lucy "Tsk, you're making such a fuss over a silly chair {b}Richard{/b}..."

    lucy "Can't you just repair it?"

    richard "Yeah, because that's exactly what I wanna do after working my ass off all day..."

    lucy "There's no rush... Maybe this weekend you could-"

    richard "I'm working all weekend!!"

    show lucy f_sad
    lucy "Lagi?!"

    richard "Ya!"

    lucy "B-but you don't have to-"

    richard "I'm trying to build a business, {b}Lucy{/b}."

    show lucy f_sad_down
    lucy "{i}*Huh*{/i} Saya tahu."

    lucy "I just wish you were around more-"

    richard "You knew what you were signing up for when I started this company!"

    lucy @ -m_talk "..."
    richard "I, on the other hand, had no idea your stupid daycare was gonna be such a pain in my ass!"

    richard "I should never have agreed to it!"

    lucy "maafkan aku... aku-"

    pause
    show lucy f_sad
    lucy "I'll just buy a new chair, okay?"

    lucy "Then you won't have to-"

    show lucy f_confused
    show richard f_angry_yell a_frustrated with dissolve
    richard "TIDAK!"

    show lucy f_sad_down
    show richard f_angry
    richard "We can't afford that, {b}Lucy{/b}!"

    show richard f_angry_yell a_stop with dissolve
    richard "Arrggghh!!!"

    richard "Hanya-"

    show richard f_angry a_frustrated with dissolve
    richard "Set the chair aside and I'll get to it when I get to it!"

    lucy "O-oke..."

    show richard f_stern_down a_watch with dissolve
    richard "I'm late for work!"

    show richard f_angry a_frustrated:
        unflip
        xoffset -200
    anon "Excuse me, I-"

    show anon f_surprised
    show richard a_stop with dissolve
    richard "I don't have time, talk to her!"

    hide richard with dissolve
    anon f_skeptical @ -m_talk "..."
    anon f_worried "Are you alright, ma'am?"

    show lucy f_sad
    lucy "Hmm?"

    show lucy f_thinking
    lucy "Oh, yeah... I'm fine."

    show lucy f_sad_down
    anon "Anda yakin?"

    show lucy f_normal
    lucy "Mmhmm."

    lucy "Apa yang bisa saya bantu?"

    anon "I'm looking for the daycare."

    lucy "Well, you've found it!"

    anon f_normal "Benar-benar?"

    lucy "Are you a father?"

    anon f_laugh "Ya."

    show anon f_grin
    lucy "Aww, I bet your kid is just adorable!"

    anon f_normal "Well, I think so!"

    lucy @ f_laugh "hehe!"

    lucy "Why don't you come inside and have a look around?"

    anon "Saya ingin itu."

    show lucy:
        flip
        xoffset 600
    with dissolve
    lucy "I'll give you the whole tour."

    scene black with fade
    pause
    $ player.go_to(L_annie_daycare)
    scene expression player.location.background_blur
    show lucy
    show anon
    with fade
    lucy "... And over here is our arts and crafts table."

    anon "Wow, this is all really impressive..."

    anon "... And all the kids seem so happy!"

    lucy @ f_laugh "Hehe, terima kasih!"

    anon "How many did you say you have right now?"

    lucy "Just eight at the moment."

    anon "This place is huge for just eight kids!"

    lucy "Yeah, my husband went a little overboard building it."

    lucy "Honestly, I was hoping we'd get more but it's such a small town, you know?"

    lucy "Clients have been tough to come by..."

    anon "I can understand."

    lucy "If you know anyone with kids, be sure to recommend us."

    anon "Saya pasti akan melakukannya."

    anon "Thank you for the tour, Mrs-?"

    lucy "Oh, you can just call me {b}Lucy{/b}."

    anon "Alright then, {b}Lucy{/b}."

    anon "I'm {b}[firstname]{/b}."

    lucy "It's been a pleasure meeting you, {b}[firstname]{/b}."

    lucy "Bring your little one next time!"

    anon "Akan dilakukan."

    hide anon with dissolve
    return

label annie_front_diane_build_toys:
    scene location_annie_cutscene02
    show text _ ("Man, I'm sure glad my dad taught me how to use this stuff before he passed away.\nIt would have been embarrassing had I been unable to help {b}Diane{/b} and {b}Lucy{/b} out.") as caption
    with fade
    pause
    hide caption with dissolve
    show text _ ("Making toys is fun!") as caption with dissolve
    pause

    scene location_annie_cutscene03
    show text _ ("They turned out really... Uhh... Unique!") as caption
    with fade
    pause
    hide caption with dissolve
    show text _ ("At least they are safe.\nThat's the most important thing, right?") as caption with dissolve
    pause

    scene expression "backgrounds/location_annie_frontyard_day_blur.jpg"
    show player 184 at Position (xpos=350)
    with fade
    player_name "I'll just set the toy down here..."

    show player 429 at left with dissolve
    player_name "I hope the kids like them..."

    show player 426
    show lucy with dissolve
    lucy "You all done out here?!"

    show player 11 with dissolve
    player_name "!!!"
    show player 29 with dissolve
    player_name "Oh, uhh... H-hey, {b}Lucy{/b}."

    player_name "Ya, menurutku begitu."

    show player 3
    lucy "Well, let's have a look."

    show lucy f_normal_down
    player_name "..."
    show lucy f_laugh
    lucy "Aww, they're adorable {b}[firstname]{/b}!"

    show lucy f_normal
    show player 10 with dissolve
    player_name "... You don't think they're ugly?"

    show player 5
    show lucy f_normal_down
    lucy "Not at all!"

    lucy "I think they're perfect!"

    lucy "The kids will really love these!"

    show lucy f_normal
    show player 17
    player_name "Heh, awesome!"

    show player 13
    lucy "You're so creative!"

    show lucy a_cleavage with dissolve
    lucy "How much do I owe you?"

    show lucy f_normal_down
    show player 10
    player_name "Hah?!"

    show player 14
    player_name "T-tidak, tidak!"

    player_name "You don't owe me anything for this, {b}Lucy{/b}!"

    show player 13
    show lucy f_normal a_money with dissolve
    lucy "Oh, come now."

    lucy "You deserve something for such fine work!"

    show player 14
    player_name "Hehe no, really, I don't want anything..."

    show player 13
    show lucy a_idle with dissolve
    lucy "Hmm."

    show lucy f_smirk
    lucy "Well, how about..."

    hide player
    show lucy b_kiss_mc
    with dissolve
    lucy "Muah!"

    show player 29 at left
    hide lucy
    show lucy f_smirk
    with dissolve
    pause
    show player 13 at left
    show xtra 21 at left
    with dissolve
    lucy "Will that do?"

    show player 21
    hide xtra
    player_name "Heh, y-yeah!"

    player_name "T-thanks, {b}Lucy{/b}!"

    show player 18
    show lucy f_laugh
    lucy "My pleasure, {b}[firstname]{/b}!"

    show lucy f_bigsmile
    pause
    show player 13
    player_name "..."
    show lucy f_normal
    lucy "Well, I'd best get back in there to the kids..."

    lucy "You wanna come in?"

    show player 14
    player_name "Oh, uhh... No, I should {b}go check on Diane's barn{/b} and see where Richard is at with it."

    show player 13
    lucy "Aww, well... Alright."

    lucy "Kembalilah dan temui aku segera, oke?"

    show player 17
    player_name "Hehe, you betcha!"

    show player 13
    show lucy a_wave with dissolve
    lucy "Sampai jumpa, {b}[firstname]{/b}."

    hide lucy with dissolve
    pause
    show player 17
    player_name "Wah!"

    show player 14
    player_name "{b}Annie{/b}'s mom is so nice!"

    show player 12
    player_name "What in the world went wrong with {b}Annie{/b}!"

    show player 4 with dissolve
    pause
    show player 14 with dissolve
    player_name "Oh well, I'd best head back to {b}Diane{/b}'s."

    hide player with dissolve
    return


label annies_house_diane_help_annie:
    scene expression "backgrounds/location_annie_livingroom_day_blur.jpg"
    show player 5 at left
    show old_annie 3 at right
    with dissolve
    annie "{b}[firstname]{/b}!"

    show old_annie 6
    show player 12
    player_name "Hai, {b}Annie{/b}."

    show player 5
    show old_annie 5
    annie "What are you doing in my house?!"

    show old_annie 6
    show player 14
    player_name "I'm getting ready to build a couple toys for your mom's daycare."

    show player 10
    player_name "Could you show me {b}where your dad keeps his tools{/b}?"

    show player 5
    show old_annie 5
    annie "Why isn't {b}Dad{/b} building them?"

    show old_annie 6
    show player 10
    player_name "Hmm?"

    player_name "Oh, uhh... My friend needed your dad to start work on her barn ASAP, so I offered to help out with the toys."

    show player 5
    show old_annie 3
    annie "Like my dad needs help from a moron like you..."

    show old_annie 1
    show player 12
    player_name "... Well, I guess I'm not that stupid 'cause he's letting me build them, by myself!"

    show player 90
    show old_annie 3
    annie "Ya benar."

    annie "Did my mom talk him into it?"

    show old_annie 1
    show player 12
    player_name "Yeah, kinda."

    show player 5
    show old_annie 3
    annie "Of course she did..."

    annie "Typical {b}Mom{/b}, no appreciation for craftsmanship."

    show old_annie 1
    show player 90
    player_name "..."
    annie "Who builds a barn within city limits anyways?!"

    show old_annie 5
    annie "You're lucky business is slow right now, otherwise, my dad would never have taken that job."

    show old_annie 6
    show player 12
    player_name "Yeah, whatever {b}Annie{/b}..."

    player_name "Are you gonna help me or not?"

    show player 90
    show old_annie 5
    annie "No, I'm not."

    annie "I've gotta keep an eye on the delinquents in detention this evening for {b}Mrs. Smith{/b}, and afterwards she wants me to draw her a bath-"

    show old_annie 28
    annie "!!!"
    show player 11
    player_name "!!!" with hpunch
    show player 10
    player_name "Did you just say you're going to draw a bath for {b}Mrs. Smith{/b}?"

    show player 11
    show old_annie 5
    annie "... Tidak."

    show old_annie 6
    show player 10
    player_name "What, are you giving her baths now?!"

    show player 5
    show old_annie 8
    annie "TIDAK!!"

    annie "I'm not- {i}*Sigh*{/i} The point is I'm leaving."

    show old_annie 5
    annie "Try not to burn my house down, moron."

    show old_annie 6
    player_name "..."
    hide old_annie with dissolve
    pause
    show player 17
    player_name "Make sure you get all her nooks and crannies!"

    show player 13
    annie "SHUDDUP!!!"

    show player 14
    player_name "Why don't you give her a pedicure while you're at it?!"

    show player 12
    player_name "Sheesh, what a weirdo..."

    show player 4 with dissolve
    pause
    show player 10 with dissolve
    player_name "Okay, I just need a {b}hammer and handsaw{/b} to build a spring rider and seesaw."

    player_name "{b}Lucy{/b} said they should be in here somewhere..."

    hide player with dissolve
    return

label annie_front_diane_ask_help_annie:
    scene expression "backgrounds/location_annie_frontyard_day_blur.jpg"
    show player 13 at left
    show richard:
        flip
        xoffset 275
    show lucy f_sad:
        xoffset 125
    with dissolve
    lucy "I just don't understand why you can't do this later?"

    show player 5
    richard "This is the next item on my list, that's why!"

    lucy "Yeah, but you know I can't bring the kids out here while you've got all these dangerous tools lying around..."

    richard "So?!"

    richard "They can play inside, can't they?!"

    lucy "{b}Richard{/b}, it's such a beautiful day out..."

    lucy "The kids wanna enjoy it."

    lucy "Can't you just go and get started on the barn job for {b}Diane{/b}?"

    richard "Tidak!"

    richard "You know I knock my jobs off in the order I receive them, {b}Lucy{/b}."

    richard "Otherwise, things get jumbled up and before you know it, chaos!"

    show lucy f_confused
    lucy "Why can't you just move this item down the list, you know, below the barn job!"

    lucy "I don't see the harm in-"

    show lucy f_sad
    show player 11
    show richard f_angry_yell
    richard "CHAOS WOMAN!" with hpunch
    richard "ABSOLUTE AND UTTER CHAOS!!!"

    show richard f_angry
    show lucy f_sad_down
    lucy "{i}*Huh*{/i}"

    show lucy f_confused
    lucy "Oh, {b}[firstname]{/b}!"

    lucy "Apa yang kamu lakukan di sini?"

    show richard f_normal:
        unflip
        xoffset -275
    with dissolve
    richard "Hmm, the milk man?"

    show richard:
        flip
        xoffset 275
    with dissolve
    richard "For heaven's sake, did you order more already?!"

    lucy "Saya kira tidak demikian..."

    richard "I swear, those brats are gonna drink me right into the poor house!"

    show lucy f_thinking
    lucy "... Did I place another order?"

    show lucy f_confused
    show richard:
        unflip
        xoffset -275
    with dissolve
    show player 10
    player_name "I'm not here for a delivery, ma'am."

    show player 5
    show lucy f_laugh
    lucy "Oh, thank goodness!"

    show lucy f_normal
    lucy "I thought I'd made a mistake again."

    show richard:
        flip
        xoffset 275
    with dissolve
    richard "Well, the day is still young. Plenty of time for you to screw something up."

    show lucy f_sad_down
    show player 90
    pause
    show player 12
    player_name "Actually I came by to see if I could help {b}Richard{/b} with anything?"

    show player 5
    show lucy f_confused
    show richard:
        unflip
        xoffset -275
    with dissolve
    richard @ -m_talk "Hmm?"

    richard "Help me with what?"

    show player 10
    player_name "Well, {b}Diane{/b} said you had a few odd jobs to handle here at the house before you could start on her barn."

    show player 29 with dissolve
    player_name "I thought, maybe I could lend a hand?"

    show player 3
    show lucy f_normal
    lucy "Oh, that's a wonderful idea!"

    show richard f_confused
    richard "Hah?!"

    richard "Well, hold on now."

    richard "I can't afford to start paying for a-"

    show player 12 with dissolve
    player_name "I'll work for free!"

    show player 5
    richard "Free?!"

    lucy "Such a sweet boy..."

    show player 10
    player_name "So long as it gets you over to {b}Diane{/b}'s as quickly as possible."

    show player 5
    richard "Hmm, entahlah..."

    richard "I like to make sure the work I do is of the highest quality-"

    lucy "Oh, mewah sekali!"

    lucy "It's just a couple of toys for the little ones. I'm sure {b}[firstname]{/b} is more than capable of building toys."

    show player 29 with dissolve
    player_name "Y-yeah, that shouldn't be a problem."

    show player 5 with dissolve
    lucy "There, you see!"

    lucy "Cross this item off your list and go on over to {b}Diane{/b}'s!"

    richard "saya..."

    pause
    show richard:
        flip
        xoffset 275
    with dissolve
    richard "I suppose, I can get started on the barn while the boy takes a swing at it..."

    show richard f_normal
    richard "... Nothing's crossed off the list until completion though!"

    richard "I'll be back to check on those toys later tonight!"

    lucy "Sounds fair."

    show lucy a_shoo f_laugh with dissolve
    lucy "Now shoo!"

    show lucy f_normal a_idle with dissolve
    richard "Tch, hold on!"

    richard "I've gotta gather my tools..."

    hide richard with dissolve
    lucy "Ayo, ayo, ayo!"

    show player 13
    lucy "Thank goodness you showed up when you did."

    lucy @ f_laugh "He was driving me crazy!"

    show player 14
    player_name "Heh, yeah?"

    show player 13
    lucy "You're not gonna insist on starting right away, are you?"

    show player 10
    player_name "Hmm?"

    show player 14
    player_name "Oh, n-no... I'll start whenever is best for you, ma'am."

    show player 13
    lucy "{b}Lucy{/b}, {b}[firstname]{/b}."

    show player 10
    player_name "Hah?"

    show player 5
    lucy "Call me {b}Lucy{/b}."

    show player 14
    player_name "O-okay, {b}Lucy{/b}."

    show player 13
    lucy "I'm gonna let the kids out to play, while the weather is so nice."

    lucy "They can really be a handful when they're cooped up inside all day."

    lucy "You can start on the toys once they wear themselves out."

    lucy @ f_laugh "Sound good?"

    show player 14
    player_name "Tentu."

    show player 13
    lucy "Do you like kids?"

    show player 10
    player_name "Uhh yeah, I guess..."

    show player 5
    lucy "Hehe, well, you'd better be sure, if you're gonna stick around."


    scene location_annie_cutscene01
    show text _ ("{b}Lucy{/b} wasn't kidding!\nThe toddlers poured forth from the daycare like a locust swarm.\nScreaming, yelling, and hurling toys...\nIt was kind of terrifying!") as caption
    with fade
    pause
    hide caption with dissolve
    show text _ ("All the while {b}Lucy{/b} could hardly contain her happiness.\nShe really did enjoy looking after them and seeing her smile made my day!") as caption with dissolve
    pause

    scene expression "backgrounds/location_annie_daycare_day_blur.jpg"
    show player 12 at left
    show lucy b_messy
    with fade
    player_name "Sialan..."

    show player 5
    show lucy f_laugh
    lucy "Hehe, aku tahu."

    lucy "Aren't they wonderful?!"

    show lucy f_normal
    show player 12
    player_name "Hah?"

    show player 29 with dissolve
    player_name "I mean, yeah... Heh, wonderful!"

    show player 3
    lucy "You're really good with them, {b}[firstname]{/b}."

    show player 12 with dissolve
    player_name "Oh, I dunno about that..."

    show player 5
    lucy @ f_laugh "aku serius!"

    lucy "It's refreshing to see a young man who's so good with children."

    lucy "It seems like all of the dads I meet through the daycare can't wait to be rid of their kids."

    show player 10
    player_name "Benar-benar?"

    player_name "That's just sad..."

    player_name "What about {b}Richard{/b}?"

    player_name "It seems like {b}Annie{/b} idealizes him..."

    show player 5
    lucy "Hehe well, let's just say he took a very hands-off approach to raising {b}Annie{/b}."

    lucy "His main focus has always been his business."

    show player 10
    player_name "That seems really unfair to you {b}Lucy{/b}..."

    show player 5
    show lucy a_wave with dissolve
    lucy "Oh, tidak apa-apa."

    show lucy a_idle with dissolve
    lucy "{b}Richard{/b} never really wanted kids."

    lucy "I knew what I was getting into when I convinced him to have {b}Annie{/b}."

    lucy "I worry about how it affected her though."

    lucy "She'll do anything to gain her father's approval."

    show player 35
    player_name "Hmm, that does explain some things about her behavior..."

    show player 34
    show lucy f_confused
    lucy "What's that dear?"

    show player 10
    player_name "Oh, uhh... Nothing ma'-"

    show player 14
    player_name "{i}*Ahem*{/i} I mean, nothing, {b}Lucy{/b}."

    player_name "I should probably get started on those toys soon, huh?"

    show player 13
    show lucy f_normal
    lucy "Anda benar."

    lucy "I should get the little ones inside for nap time."

    show player 10
    player_name "Does {b}Richard{/b} have any tools I can use?"

    show player 13
    show lucy f_laugh a_cover with dissolve
    lucy "Haha, does {b}Richard{/b} have any tools..."

    show lucy f_normal a_idle with dissolve
    lucy "Go check inside the house, you'll find what you need in no time."

    show player 14
    player_name "Terima kasih."

    hide player
    hide lucy
    with dissolve
    return

label annies_house_livingroom_diane_delivery_2:
    scene expression "backgrounds/location_annie_frontyard_day_blur.jpg"
    show richard a_phone_talk f_phone
    show player 13 at left
    with dissolve
    richard "No, absolutely not!"

    richard "Well, I don't care if you don't like it..."

    show player 5
    pause
    richard "Tidak..."

    richard "The fact of the matter is that it's OSHA regulation."

    richard "No, I do things strictly by the book!"

    richard "I told you as much when you hired me."

    richard @ f_normal -m_talk "..."
    richard "No, more money won't make it go away."

    richard "Rules are rules."

    richard "Look, I need you to hold on for a second."

    show richard f_normal a_phone with dissolve
    richard "Can I help you?"

    show player 12
    player_name "Uhh, maybe..."

    show player 239_240 with dissolve
    pause
    show player 163c with dissolve
    player_name "I'm supposed to deliver this-"

    show player 163g
    richard "Oh, you're the milk guy..."

    richard "Ugh, alright. Follow me."

    show richard a_phone_talk f_phone:
        flip
        xoffset 500
    with dissolve
    richard "Now, where were we?"

    richard "Oh right, OSHA guidelines article 7..."

    hide richard with dissolve
    player_name "..."
    hide player with dissolve
    scene expression "backgrounds/location_annie_daycare_day_blur.jpg"
    show richard a_phone:
        flip
        xcenter 0.75
    show player 163b at left
    with dissolve
    richard "{b}Lucy{/b}!"

    richard "The milk man's here!"

    lucy "Oh, coming!"

    show richard a_phone:
        unflip
        xoffset -200
    with dissolve
    richard "My wife's the one who ordered it."

    richard "She'll sort you out."

    show richard a_phone_talk:
        flip
        xcenter 0.75
    with dissolve
    show player 163c
    player_name "O-oke."

    show player 163b
    show lucy:
        xoffset 125
    with dissolve
    lucy "Phew, these kids are wearing me out!"

    richard "Eh ya..."

    lucy "{b}Richard{/b}, could you, umm... Help carry these over to the house?"

    show richard f_angry
    richard "Not now, {b}Lucy{/b}! Can't you see I'm on the phone with a client?!"

    show richard f_phone
    richard "Oh, sorry... One second."

    show richard a_phone f_angry with dissolve
    richard "This daycare was your dumb idea and you should handle it your own damn self!"

    show lucy f_sad
    richard "... And make sure you count the money this time before handing it over!"

    richard "Money is tight enough around here without you throwing more down the drain!"

    show player 163g
    lucy "Yes, dear..."

    show lucy f_sad_down
    hide richard with dissolve
    richard "Sorry, about that again..."

    lucy @ -m_talk "..."
    show player 163c
    player_name "I'll help you, ma'am."

    show player 163b
    show lucy f_sad
    lucy "Oh, that's not necessary. I'm sure you have lots of-"

    show player 163c
    player_name "I insist."

    show player 163b
    show lucy f_normal
    lucy @ -m_talk "..."
    lucy "Well, aren't you sweet!"

    lucy "Let me call my daughter over to watch the kids for a second."

    show player 163c
    player_name "Ya baiklah."

    show player 163b
    hide lucy with dissolve
    player_name "..."
    lucy "{b}Annie{/b}, sweetie?"

    lucy "Could you come help me for a second?"

    annie "Ugh, I was just walking out the door, {b}Mom{/b}..."

    lucy "I only need you for a couple minutes."

    annie "Ughhh!!!"

    show old_annie 7 at Position (xpos=600)
    show lucy:
        xoffset 125
    with dissolve
    annie "This had better not make me late!"

    annie "{b}Mrs. Smith{/b} doesn't tolerate-"

    show old_annie 1
    annie "..."
    show old_annie 4
    annie "What is he doing here?"

    show old_annie 6
    lucy f_confused @ -m_talk "Hmm?"

    lucy "Do you two know each other?"

    show player 163c
    player_name "Heh, we're in the same class at school."

    show player 163b
    show lucy f_laugh
    lucy "Well, isn't that nice?"

    show lucy f_normal
    show old_annie 5
    annie "Hardly..."

    show old_annie 6
    if not L_annie_front.first_visit:
        lucy "He's brought us more of that wonderful milk the children like so much."

        show old_annie 3
        annie "You work for a milk company?"

        show old_annie 1
        show player 163c
        player_name "Well, my friend {b}Diane{/b} owns the company."

        player_name "I just help her out as much as possible."

        show player 163b
    else:
        lucy "This nice young man-"

        lucy "Sorry, I didn't catch your name?"

        show player 163c
        player_name "{b}[firstname]{/b}."

        show player 163b
        lucy "Hi, {b}[firstname]{/b}. I'm {b}Lucy{/b}."

        show player 163c
        player_name "Nice to meet you, ma'am."

        show player 163b
    lucy @ f_laugh "Ya ampun."

    lucy "I hope you're friends with this one, {b}Annie{/b}?"

    lucy "I like him!"

    show old_annie 3
    annie "He's a delinquent!"

    show old_annie 1
    show player 163g
    lucy "Oh, don't call him that!"

    show old_annie 4
    annie "... That's what he is!"

    show old_annie 1
    lucy "{b}[firstname]{/b}, offered to haul all this milk inside for me."

    lucy "Would you watch the kids, while I help him?"

    show player 163b
    show old_annie 4f with dissolve
    annie "No way! Absolutely not!"

    annie "You know I HATE kids!"

    show old_annie 1f
    lucy "Pleeeeeeeeease?"

    lucy "It'll just take a moment."

    show old_annie 6f
    annie "..."
    show old_annie 5f
    annie "Why can't {b}Dad{/b} do it?!"

    show old_annie 6f
    lucy "Oh, he's on the phone arguing with a client."

    show old_annie 5f
    annie "... Is that moron still complaining about the OSHA regulations?!"

    annie "It's not like {b}Dad{/b} wrote the rules, he just abides by them like any decent person would..."

    show old_annie 6f
    show lucy f_confused
    lucy "aku tidak-"

    lucy "..."
    lucy "What's an OSHA?"

    show old_annie 7f
    annie "Errghh!! Never mind..."

    show old_annie 4f
    annie "Cepatlah!"

    hide old_annie
    show lucy b_hug_annie
    with dissolve
    lucy "Thank you, sweetie!"

    lucy "Follow me, {b}[firstname]{/b}!"

    show old_annie 6f at Position (xpos=600)
    hide lucy
    with dissolve
    show player 163c
    player_name "Ya, Bu."

    hide player with dissolve
    annie "..."
    show old_annie 4f
    annie "Hey! Stop running!!"

    hide old_annie with dissolve
    annie "Eugh, don't put that in your mouth!!!"

    scene expression "backgrounds/location_annie_livingroom_day_blur.jpg"
    show lucy b_bend
    show player 426 at left
    with dissolve
    lucy "Alright, everything looks good."

    lucy "I dunno what you all are putting in this milk but the kids just can't get enough!"

    player_name "Mmmhmm."

    lucy "This will all be gone in a couple weeks."

    lucy "I'll need to order a lot more next time."

    lucy "Assuming {b}Richard{/b} lets me."

    player_name "..."
    lucy "That wouldn't be a problem, would it?"

    player_name "..."
    show lucy b_dressed f_confused
    lucy "{b}[firstname]{/b}?"

    show player 11
    player_name "!!!"
    show player 29 with dissolve
    player_name "I'm sorry, what was that last bit?"

    show player 3
    show lucy f_normal
    lucy "I said I'll need to order more next time, if that's alright?"

    show player 29
    player_name "... Yeah, I think so."

    show player 17 with dissolve
    player_name "I'll speak with {b}Diane{/b} about it."

    show player 13
    lucy @ f_laugh "Luar biasa!"

    lucy "As for your payment..."

    show lucy f_normal_down a_cleavage with dissolve
    show player 11
    player_name "!!!"
    show lucy a_money with dissolve
    lucy "That should cover it."

    show lucy f_normal a_idle
    show player 638b at Position (xoffset=-19)
    with dissolve
    player_name "..."
    show player 638 at Position (xoffset=-21)
    player_name "Uhh, this is too much."

    show player 13
    show lucy a_money f_normal_down with dissolve
    lucy @ -m_talk "..."
    show player 14
    player_name "That's fifty dollars more than the price..."

    show player 13
    show lucy f_confused
    lucy "!!!"
    show lucy f_laugh
    lucy "Wah!"

    show lucy f_normal
    lucy "Hehe, I'm such a klutz with money..."

    show lucy f_laugh a_cleavage with dissolve
    lucy "... And you're a sweetheart!"

    hide player
    show lucy b_hug_mc:
        xoffset 150
    with dissolve
    lucy "Thank you for being honest, {b}[firstname]{/b}!"

    player_name "!!!"
    pause
    show player 29 at left
    show lucy f_normal b_dressed:
        xoffset 0
    with dissolve
    player_name "Heh. N-no problem, ma'am."

    player_name "I wouldn't want your husband to get angry at you again."

    show player 3
    show lucy f_confused
    lucy "Hmm?"

    show lucy f_laugh a_wave with dissolve
    lucy "Oh! No..."

    show player 13 with dissolve
    lucy "He's just so busy with {b}his carpentry business{/b} and all!"

    lucy "He doesn't have time for me and my problems."

    show lucy f_normal a_idle with dissolve
    player_name "..."
    show player 10
    player_name "He's a {b}carpenter{/b}?"

    show player 5
    lucy @ -m_talk "Mmmhmm."

    show lucy f_sad
    lucy "He's been doing it for over twenty years."

    lucy "Poor dear, works himself to the bone."

    show player 12
    player_name "Well, he should make time."

    show player 14
    player_name "You're such a nice lady!"

    show player 13
    show lucy f_normal
    lucy "Aww, well, thank you, {b}[firstname]{/b}!"

    lucy "You're nice too!"

    annie "DON'T THROW THINGS!!!" with hpunch
    show player 11
    player_name "!!!"
    show lucy f_confused
    annie "AAAHHH!!"

    lucy "Uh oh..."

    show player 13
    lucy "It sounds like the kids are getting the better of {b}Annie{/b} in there."

    lucy "I'd better go rescue her!"

    hide lucy with dissolve
    player_name "..."
    show player 17
    player_name "( Oh, I have to check this out! )"

    hide player with dissolve
    scene expression "backgrounds/location_annie_daycare_day_blur.jpg"
    show old_annie 25 at right
    show player 11 at Position (xpos=400)
    show lucy f_confused:
        flip
        xoffset -100
    with dissolve
    annie "I TOLD YOU TO STOP RUNNING!!!"

    show old_annie 24
    pause
    show old_annie 25
    annie "Ugh, finally!"

    annie "What took you so long?!"

    show old_annie 24
    lucy "I'm sorry, sweetie. I-"

    show old_annie 25
    annie "Look at me, I'm a disaster now!"

    annie "I'm going to have to shower again!"

    show old_annie 24
    show lucy f_sad_down
    lucy @ -m_talk "..."
    show old_annie 25
    annie "Thanks a lot, {b}Mom{/b}!"

    show old_annie 26 with dissolve
    pause
    hide old_annie with dissolve
    pause
    show player 10f at right with dissolve
    player_name "Wow, that was..."

    player_name "... You alright, ma'am?"

    show player 5f
    show lucy f_sad
    lucy "Hmm?"

    lucy "Oh, tidak apa-apa."

    lucy @ -m_talk "..."
    lucy "Thanks again for your help today, {b}[firstname]{/b}."

    show player 14f
    player_name "It was no problem, ma'am."

    player_name "I'll see you next time."

    show player 13f
    hide lucy with dissolve
    pause
    show player 5f
    player_name "( That poor woman... )"

    pause
    show player 18f
    player_name "( Welp, I should {b}get this money back to Diane{/b} and tell her that the daycare will be needing more next time. )"

    hide player with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
