label tattoo_parlor_garage_eve_party_start:
    scene expression player.location.background_blur with None
    show anon f_surprised with dissolve
    anon @ -m_talk "( Okay, this is a lot of people! )"

    show anon f_normal
    pause
    anon @ -m_talk "( I should look for one of the girls. )"

    hide anon with dissolve
    return

label tattoo_parlor_garage_eve_clients_check_shop:
    scene expression player.location.background_blur with None
    show anon
    show odette f_tired b_wakeup a_head
    with dissolve
    anon "Hai, {b}Odette{/b}."

    odette "Shhh, not so loud, {b}[firstname]{/b}..."

    show anon f_worried
    pause
    odette "Ugh, turn off that bright light!"

    show odette a_sides with dissolve
    anon "Ehh, you mean the sun?"

    odette "Yes, turn off the sun... Please."

    anon f_normal @ f_laugh "Heh, I don't think I can do that..."

    pause
    odette "Apa yang kamu lakukan di sini sepagi ini?"

    anon "I wanted to check up on {b}Eve{/b} and make sure she's okay."

    odette a_head "Well, aren't you sweet."

    odette "She's probably doing a lot better than I am right now..."

    anon f_worried "Y-yeah, you look really... Umm..."

    pause
    odette "Hungover?"

    show odette a_sides with dissolve
    anon f_normal "Ya."

    pause
    odette "I might have gone a little overboard with the fireball last night..."

    pause
    odette "Do you know how to make a Bloody Mary?"

    anon @ f_skeptical "T-tidak?"

    odette "God, I'd kill for a Bloody Mary right now!"

    anon "Are they upstairs?"

    odette @ -m_talk "Hmm?"

    odette "{b}Grace{/b} wasn't in the shop?"

    anon f_worried "Tidak."

    odette "Oh, crap... If she overslept, she's going to be pissed."

    anon "Mengapa Anda mengatakan itu?"

    odette "Because drinking last night was my idea, and she's already way behind on her rent this month..."

    anon @ f_surprised "She is?"

    odette "Hmm, I probably shouldn't have told you that..."

    odette a_head "Eugh, my head is pounding!"

    odette "I think you should be the one who wakes them up."

    anon @ f_confused "Hah?!"

    anon @ a_point_self "W-why me?"

    odette "Because, if I go up there {b}Grace{/b} is going to murder me!"

    anon "Uhh, I don't know-"

    odette a_cheeks f_pouting "You don't wanna see me get murdered, do you handsome?"

    pause
    anon @ f_sad_down "{i}*Sigh*{/i} N-no..."

    odette a_idle f_smirk "You'll be fine up there, they're both head over heels for you!"

    anon "Ya baiklah."

    odette "Just be real gentle about it, okay?"

    odette "They're definitely going to be hung over too."

    anon @ a_salute "Saya akan."

    hide anon with dissolve
    return

label tattoo_parlor_garage_eve_bike_breakdown_repair_pass:
    anon "I dunno, I-"

    show eve a_boobs f_happy_down with dissolve
    pause
    anon "!!!"
    show eve f_surprised a_arrest with dissolve
    anon "Yeah, look here..."

    eve f_normal_down a_idle @ -m_talk "Hmm?"

    anon "These wires are a bit frayed."

    pause
    anon "And here, these bolts are a bit loose."

    eve "Would that really stop the bike from starting?"

    anon "It's possible..."

    eve "Can you fix it?"

    anon "Saya kira demikian."

    anon "Just give me one second..."

    pause
    anon "Can you hand me that wrench?"

    eve "Y-ya, tentu saja."

    show eve b_dressed_pickup with dissolve
    pause
    show eve b_dressed a_wrench with dissolve
    anon "Terima kasih."

    return

label tattoo_parlor_garage_eve_bike_breakdown_repair_fail_repeat:
    anon "Tidak."

    pause
    show anon f_sad_down a_behind_head:
        flip
    with dissolve
    show eve f_normal
    anon "Crap!"

    show anon a_idle
    anon "I don't understand why it isn't working..."

    return

label tattoo_parlor_garage_eve_bike_breakdown_repair_intro_repeat:
    scene expression player.location.background_blur with None
    show anon
    show eve f_happy
    with dissolve
    eve "Hai, {b}[firstname]{/b}!"

    hide eve
    show anon b_hug_eve f_shy_down
    with dissolve
    eve "I was hoping you'd come over today."

    anon "Did {b}Grace{/b} get her bike fixed yet?"

    eve "Tidak, belum."

    show anon b_dressed f_normal
    show eve f_sad
    with dissolve
    eve "Mengapa?"

    anon "You think I can take a look at it again?"

    eve @ f_disgusted "Ehh, sure... I guess?"

    anon @ f_laugh "Terima kasih!"

    hide anon
    show eve f_normal_down:
        flip
        xoffset 300
    with dissolve
    pause
    anon "Hmm."

    eve "Anda melihat sesuatu?"

    return

label tattoo_parlor_garage_eve_bike_breakdown_repair_fail:
    anon "Uhh, oke..."

    show anon f_worried o_oil:
        flip
    with dissolve
    show eve f_normal
    anon "I was wrong."

    anon "This is a LOT different than a lawn mower engine..."

    eve @ f_eyeroll "Well duh!"

    anon f_sad_down "Maaf."

    return

label tattoo_parlor_garage_eve_bike_breakdown_repair_fail_continued:
    eve f_happy @ f_laugh "Hehe, it's okay {b}[firstname]{/b}."

    eve "Let's just go upstairs and play some {i}Street Kombat{/i}, yeah?"

    anon f_normal "Baiklah."


    scene location_tattoo_bedroom_cutscene01
    show text _ ("It would have been the perfect opportunity to earn some brownie points with {b}Eve{/b} and her sister.\nToo bad motorcycles have very little in common with lawnmowers.\nI probably would have been able to see that coming if I had been just a little smarter...") as caption
    with fade
    pause

    scene location_tattoo_bedroom_cutscene04
    show text _ ("Still, I did get to spend the evening with {b}Eve{/b}. Even if she did end up mercilessly schooling me in {i}Street Kombat{/i}.\n\n") as caption
    with fade
    pause
    pause
    show text _ ("\n\nRepeatedly.") with dissolve
    pause

    $ player.go_to(L_tattooparlor_bedroom)
    scene expression player.location.background_blur
    show eve f_happy
    show anon f_sad_down
    with fade
    eve "That was so much fun!"

    anon "Y-ya, benar."

    eve "Hey, don't be a sore loser!"

    anon f_grumpy "I'm not, I-"

    pause
    anon "I just can't believe how good you are at that game!"

    eve "I'm not THAT good..."

    eve "You just suck."

    anon f_sad_down @ f_surprised "Apa?!"

    eve @ f_laugh "Ha ha ha!"

    eve "I'm kidding!"

    eve f_pouting "Aduh..."

    hide anon
    show eve b_dressed_kiss:
        xoffset 100
    with dissolve
    anon "!!!"
    eve "MM."

    pause
    show eve b_dressed f_sexy:
        xoffset 0
    show anon f_flirt
    with dissolve
    eve "Feel better now?"

    anon "Yes, actually."

    eve f_happy @ f_laugh "hehe!"

    eve "We should do this again."

    anon "Tentu saja."

    eve "Just remember, {b}I have detention during the week{/b}."

    eve "So it'll have to be {b}during the weekend{/b}."

    anon "Ya baiklah."

    hide eve
    show anon b_hug_eve f_shy_down
    with dissolve
    anon "Sampai jumpa lagi."

    eve "Sampai jumpa, {b}[firstname]{/b}."

    hide anon
    show eve f_happy
    with dissolve
    return

label tattoo_parlor_garage_eve_bike_breakdown_repair_intro:
    scene expression player.location.background_blur with None
    show eve:
        flip
        xoffset 400
    with dissolve
    eve "I can't believe she's giving you this much trouble."

    grace "Well, it is an old second-hand part..."

    pause
    eve "You should have sprung for a new one."

    grace "Tch, like we can afford that!"

    eve f_sad_down "Y-ya, aku tahu."

    show anon with dissolve
    grace "C'mon baby, work for Mama!"

    "{i}*Engine revving*{/i}"

    grace "Sialan!"

    show grace o_oil f_weary a_rag:
        xoffset 50
    with dissolve
    grace "{i}*Sigh*{/i} I need to take a break."

    anon "Not having any luck?"

    show grace f_normal a_idle with dissolve
    eve f_surprised "!!!"
    show eve f_happy:
        unflip
        xoffset -250
    with dissolve
    eve "{b}[firstname]{/b}!!!"

    grace "Halo, {b}[firstname]{/b}."

    pause
    anon "Hi, {b}Grace{/b}."

    anon "You know, you've got something on your face..."

    eve f_happy_right @ f_laugh "Haha!"

    grace @ f_eyeroll "Yeah, yeah... Very funny."

    grace "I don't understand why it isn't working!"

    grace "Everything looks fine."

    eve "Did you try rebooting it?"

    show grace f_happy
    anon @ f_laugh "Haha!"

    grace @ f_laugh "Hehe, shut up!"

    grace "You two have the same silly sense of humor... You know that?"

    eve f_happy @ -m_talk "Mmhmm."

    eve f_happy_right "Why do you think I like him so much?"

    show anon f_grin
    show eve f_happy
    pause
    show anon f_normal
    show eve f_happy_right
    grace "I'm going to go wash up and check on {b}Odette{/b}."

    grace "God knows what she's doing in the shop by herself."

    grace "Can you two behave yourselves if I leave you alone in here?"

    eve "Tidak."

    eve f_happy "Why don't you run upstairs and grab us some beer, {b}[firstname]{/b}?"

    eve "I'll call the hookers..."

    anon f_shock "!!!"
    grace a_hips_mad @ f_laugh "{b}Malam{/b}!"

    eve f_happy_right @ f_laugh "Haha, I'm just joking!"

    anon @ f_laugh a_behind_head "Haha!"

    show anon f_normal
    grace @ f_eyeroll "Brat."

    grace "Saya akan segera kembali."

    hide grace with dissolve
    show eve f_happy
    anon "It sucks she can't get her bike working..."

    eve f_normal "Ya, saya tahu."

    eve "I wish I could do something to cheer her up."

    show anon f_thinking a_thinking with dissolve
    pause
    anon f_normal a_idle "I could try and take a look at it?"

    eve f_surprised "You mean, {b}Grace{/b}'s bike?"

    anon "Ya."

    eve f_disgusted "What do you know about bikes, {b}[firstname]{/b}?"

    anon f_grin @ f_unimpressed "Oh, absolutely nothing..."

    eve f_normal @ f_eyeroll "..."
    anon f_normal "... But I used to help my dad out when he fixed the lawn mower all the time."

    anon @ f_laugh "How different could it be?"

    eve f_sad_down "Uhh, entahlah..."

    anon "It wouldn't hurt to take a look, right?"

    eve f_normal "Saya kira tidak."

    hide anon
    show eve f_normal_down:
        flip
        xoffset 300
    with dissolve
    pause
    anon "Hmm."

    eve "Anda melihat sesuatu?"

    return

label tattoo_parlor_garage_eve_big_sis_check_garage:
    scene expression player.location.background_blur
    show anon f_worried with dissolve
    anon "Is that {b}Odette{/b}?"

    hide anon with dissolve
    return

label tattoo_parlor_garage_eve_visit_garage:
    scene expression player.location.background_blur with None
    show anon
    show eve f_nervous
    eve "This is our garage."

    anon "Hey, it's pretty cozy in here..."

    eve "Y-you like it?"

    anon "Ya, benar."

    pause
    show anon f_surprised a_point with dissolve
    anon "Whoa, whose motorcycle is that?!"

    show anon a_idle with dissolve
    eve f_laugh "Heh, that belongs to my sister..."

    show anon f_normal
    eve f_happy "She's in the process of restoring it."

    anon "Does it work?"

    eve "Tentu saja."

    anon @ f_laugh "Ini sangat keren!"

    eve "Aku tahu, kan?!"

    pause
    anon "Where do those stairs lead?"

    eve "Up to our apartment."

    anon f_skeptical "You have to go through the garage to get up to your apartment?"

    eve @ -m_talk "Mhmm."

    anon "That's weird..."

    eve @ f_laugh "Haha, yeah... That's the first thing I thought too."

    eve "There's a stairwell inside too but my sister has it blocked off at the moment."

    anon f_worried "Oh."

    show anon f_normal
    eve "It grows on you, I promise."

    eve "I actually think it's pretty cool, now."

    eve @ f_laugh "Like we live in a secret base or something."

    anon "Menarik..."

    pause
    eve "C'mon, {b}I'll show you the upstairs{/b}."

    hide anon
    hide eve
    with dissolve
    return

label tattoo_parlor_garage_pantie_collection:
    scene expression player.location.background_blur with None
    if player.location.is_here(M_odette):
        show anon f_surprised with dissolve
        if (M_eve.odette_depressed or (game.timer.is_evening()
                and (M_odette.pregnancy or M_grace.pregnancy)) or
                M_eve.finished_state(S_eve_lesbians_aftermath)):
            anon @ -m_talk "( Better not, she's right there! )"

        else:
            anon @ -m_talk "( Better not, she might wake up! )"

    else:
        show anon f_surprised_down a_panties_odette1 with dissolve
        anon @ -m_talk "( These are {b}Odette{/b}'s panties. )"

        anon @ -m_talk "( What are they doing up in the garage? )"

        anon f_thinking @ -m_talk "( Weird... )"

        pause
        if M_somrak.finished_state(S_somrak_start):
            anon f_grin "( I bet {b}Master Somrak{/b} would like these. )"

            $ player.get_item("odette_panties")
        else:
            anon f_surprised_down @ -m_talk "( Better replace them before I get caught! )"

        hide anon with dissolve
    $ game.main()
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
