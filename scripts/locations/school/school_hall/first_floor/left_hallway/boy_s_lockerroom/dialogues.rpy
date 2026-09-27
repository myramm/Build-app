label locker_room_eve_roxxy_bullying:
    scene expression player.location.background_blur with None
    show eve b_pants f_sad_down:
        xoffset 50
    show roxxy b_undies f_normal_down:
        xoffset -700
    show missy b_undies f_angry:
        flip
        xoffset 150
    show becca b_undies:
        xoffset -250
    becca "Diam, {b}Nona{/b}..."

    missy "aku serius!"

    show roxxy b_pullup1 with dissolve
    missy "{b}Coach Bridget{/b} is totally into girls!"

    becca "Who told you that?"

    show roxxy b_shorts a_pullup with dissolve
    missy f_happy "Nobody told me, it's so obvious!"

    becca @ f_eyeroll "The only thing obvious here is that you have no idea what you're talking about..."

    show missy f_angry
    show roxxy a_remove1 with dissolve
    pause
    show roxxy b_dressed f_normal:
        flip
        xoffset -50
    with dissolve
    show becca b_pants_pull with dissolve
    roxxy "I dunno, I could see it."

    show roxxy a_hips
    show missy:
        unflip
        xoffset -450
    show becca b_pants a_pull f_normal_down
    with dissolve
    missy f_normal "Ya?"

    show eve f_confused b_sweatshirt_remove with dissolve
    roxxy "I mean, sure... She's so butch and that pink hair..."

    show becca a_sides f_thinking with dissolve
    becca "Hmm, I guess the hair thing is pretty weird..."

    becca f_normal "Isn't she's like, in her mid-thirties or something?"

    becca "Who does that?!"

    show eve f_sad_down a_remove2 with dissolve
    missy "She's a dyke for sure!"

    show roxxy f_surprised
    show eve f_confused
    becca "That doesn't necessarily make her a dyke..."

    show roxxy f_glaring
    show eve f_surprised b_dressed_hoodless a_hoodless_remove1 with dissolve
    eve "!!!"
    show eve f_nervous_down b_dressed a_idle with dissolve
    becca "Maybe, her hair is going gray or someth-"

    roxxy "What the fuck are you looking at, freak?!"

    show roxxy zorder 1:
        xoffset 400
    show missy f_angry zorder 1:
        flip
        xoffset 0
    show becca f_upset:
        flip
        xoffset 200
    with dissolve
    eve f_normal "Tidak ada apa-apa."

    roxxy "Uh huh... I see you listening in on our conversation!"

    eve "T-tidak, aku tidak-"

    roxxy "You got something to add?!"

    becca f_sexy "Speaking of bad dye jobs..."

    show roxxy f_sexy
    missy f_normal @ f_laugh "Haha, totally!"

    show eve f_angry
    becca "I bet she's a lesbian too."

    eve "Saya tidak!"

    becca "Ya benar."

    becca "Why else would you dye that rats nest blue?"

    roxxy "It's probably the only thing that keeps the lice in check..."

    missy @ f_angry "Eugh!"

    becca @ f_laugh "Haha!"

    eve "Screw you, {b}Roxxy{/b}!"

    roxxy @ f_angry "Tch, don't get lippy with me!"

    roxxy "It's not my fault you're disgusting..."

    becca "She probably dyes it to distract people from noticing her flat chest!"

    eve f_cry_down @ f_surprised "!!!"
    becca "Just look at that washboard!"

    missy @ f_laugh "Haha!"

    roxxy "Is that why you always rush in here to get changed before the rest of us?!"

    roxxy "Don't worry, freak... You'll hit puberty someday..."

    becca @ f_laugh "Ha ha ha!"

    show eve:
        flip
        xoffset 700
    with dissolve
    roxxy "Aww, where you going?"

    hide eve with dissolve
    becca "Probably off to listen to emo shit and cut herself..."

    missy "Yeah, totally!"

    anon "{b}Malam{/b}?"

    anon "Ada apa?"

    pause
    if not M_roxxy.finished_inclusive(S_roxxy_end):
        show anon f_worried:
            flip
            xoffset 100
        with dissolve
        anon "Were you guys making fun of-"

        show anon f_surprised
        becca f_upset "{i}*Terkesiap*{/i}"

        show missy a_wave f_happy with dissolve
        becca a_cover "What the fuck, perv!"

        show missy a_sides with dissolve
        roxxy "So what if we were?"

        roxxy "It's her own fault... She shouldn't be eavesdropping on our conversation!"

        anon "You shouldn't treat people like that, {b}Roxxy{/b}..."

        anon "Especially {b}Eve{/b}, she's got enough problems without you three piling on!"

        roxxy f_eyeroll "Boo hoo."

        show anon f_angry
        roxxy "Why do you care, anyways?"

        roxxy "You like her or something?!"

        show missy f_angry
        anon f_worried "Apa?"

        anon "I-itu bukan-"

        show roxxy f_normal
        becca @ f_laugh "Ha, he totally does!"

        missy @ f_confused "Anda melakukannya?"

        roxxy f_sexy "Well, they would make the perfect couple, wouldn't they?"

        roxxy "The loser and the freak."

        becca "Yeah, just imagine what their kids would be like..."

        roxxy @ f_angry "Eugh, gross!"

        show anon f_angry
        becca f_sexy @ f_laugh "Haha!"

        roxxy @ f_laugh "Haha!"

        missy @ -m_talk "..."
        anon f_worried "Whatever, forget it."

        anon "You three will never change..."

        hide anon with dissolve
        roxxy "Ya itu benar!"

        roxxy "You better walk away!"

        missy a_wave f_happy "Bye, {b}[firstname]{/b}!"

        show roxxy f_glaring
        show becca f_glaring_back
        pause
        missy f_confused "Apa?"

    else:
        show anon f_angry:
            flip
            xoffset 100
        with dissolve
        anon "Were you guys making fun of her?!"

        show missy a_wave f_happy with dissolve
        becca f_shy "H-hei, {b}[firstname]{/b}."

        show missy a_sides with dissolve
        roxxy "Just a little bit..."

        anon f_worried "Why are you acting like that?"

        show missy f_angry
        show becca f_shy
        roxxy f_worried "Aku tidak bermaksud-"

        pause
        roxxy "She started it... She was eavesdropping on our conversation!"

        anon "I don't care!"

        anon "{b}Eve{/b} has enough problems without you three piling on!"

        roxxy f_worried "So what, you're mad at me?"

        anon f_worried "{i}*Sigh*{/i} Just try and be nice, okay?"

        anon "For me."

        roxxy "Alright, I'll try."

        roxxy "For you."

        anon f_normal "Terima kasih."

        anon "I'm gonna go make sure she's okay..."

        hide anon
        show anon f_worried:
            xoffset 600
        with dissolve
        roxxy "Tunggu!"

        hide anon
        show anon f_worried:
            flip
            xoffset 100
        with dissolve
        anon @ -m_talk "Hmm?"

        roxxy f_sexy "Are you going to have time for me later?"

        anon f_flirt "Ya, tentu saja."

        roxxy "Bagus!"

        hide anon
        show roxxy b_kiss:
            flip
            xoffset 50
        with dissolve
        pause
        show anon:
            flip
            xoffset 100
        show roxxy b_dressed:
            flip
            xoffset 400
        with dissolve
        roxxy "Don't leave me waiting too long!"

        hide anon with dissolve
        pause
        becca f_sexy "Does your boyfriend have a thing for that freak?"

        show roxxy f_angry:
            unflip
            xoffset 0
        with dissolve
        roxxy "Psh, no!"

        roxxy "He's just a nice guy, you know that..."

        missy @ -m_talk "..."
        roxxy a_point_self "Seriously, why would he want that stick when he has all this to play with?!"

        becca "I dunno, I hope you're right..."

    scene black with fade
    pause
    $ player.go_to(L_school_lefthallway)
    scene expression player.location.background_blur
    show anon f_worried with dissolve
    anon @ -m_talk "( Hmm, {b}Eve{/b} looked pretty upset... )"

    anon @ -m_talk "( I should go and {b}find her{/b}. )"

    hide anon with dissolve
    return

label boys_lockerroom_roxxy_shower_event:
    scene locker_empty_b with None
    show old_roxxy 17 at right
    show old_becca 1 at Position(xpos=315)
    show old_missy 1 at left
    with dissolve
    roxxy "... And then he told me to solve my own problems!"

    show old_roxxy 16
    show old_becca 2
    becca "I can't believe {b}Dexter{/b} is being such a baby!"

    show old_becca 1
    show old_roxxy 17
    roxxy "Oh well, he was unreliable anyways."

    show old_roxxy 16
    show old_becca 3
    show old_missy 2
    missy "How can anyone be so stupid?!"

    show old_missy 1
    show old_becca 1
    show old_roxxy 17
    roxxy "Ugh! I know right?!"

    roxxy "He had one job to do!"

    show old_roxxy 16
    show old_becca 2
    becca "So, how are you going to get through French?"

    becca "You know, you can't copy off us anymore..."

    show old_becca 3
    show old_missy 2
    missy "Yeah, {b}Miss Bissette{/b} said if we get caught cheating again, she's going to fail all of us."

    show old_missy 1
    show old_becca 1
    show old_roxxy 17
    roxxy "Yeah, I know!"

    show old_roxxy 16
    show old_becca 2
    becca "Why don't you just get the homework off that nerd yourself?"

    show old_becca 1
    show old_roxxy 17
    roxxy "Ugh, I dunno."

    roxxy "He's so disgusting..."

    show old_roxxy 16
    show old_missy 6
    missy "Haha!"

    show old_missy 1
    show old_becca 8
    becca "Just pretend to flirt with him a little..."

    becca "He'll hand his homework to you for sure."

    show old_becca 7
    show old_roxxy 17
    roxxy "Eugh, shut up!"

    roxxy "... You're going to make me puke!"

    show old_roxxy 16
    show old_becca 2
    becca "Okay, someone else then..."

    show old_becca 3
    show old_missy 1b
    missy "What about {b}Kevin{/b}?"

    missy "He's kinda cute."

    show old_missy 1
    show old_roxxy 17
    roxxy "Pfft!"

    show old_roxxy 16
    show old_becca 4
    becca "Haha!"

    becca "... Yeah, he's cute."

    show old_becca 8
    becca "I don't think he'd be into {b}Roxxy{/b} though."

    becca "She doesn't have the right equipment for {b}Kevin{/b}!"

    show old_becca 7
    show old_roxxy 17
    show old_missy 3
    roxxy "Yeah, I'd need a cock to get the homework off him!"

    show old_roxxy 16
    show old_becca 3
    show old_missy 2
    missy "Tunggu sebentar..."

    missy "... {b}Kevin{/b}'s gay?"

    show old_missy 1
    show old_roxxy 17
    roxxy "You seriously didn't know?"

    show old_roxxy 16
    show old_becca 3b
    becca "It's so obvious..."

    show old_becca 3
    missy "..."
    show old_missy 2
    missy "So what are you going to do?"

    show old_missy 1
    show old_becca 1
    becca "..."
    show old_roxxy 17
    roxxy "Saya tidak tahu..."

    show old_roxxy 16
    pause
    show old_becca 3
    show old_missy 2
    missy "{b}Miss Bissette{/b} is the worst."

    show old_missy 1
    show old_becca 2
    becca "Yeah, too bad you don't have a penis, {b}Roxxy{/b}. I hear she loves trading good grades for dick."

    show old_missy 6
    show old_becca 1
    missy "Haha!"

    show old_missy 1
    show old_roxxy 17
    roxxy "I can't fail these exams or I'm going to look like an idiot in front of everyone!"

    show old_roxxy 16
    show old_becca 2
    becca "You know, I heard that {b}Mrs. Smith{/b} keeps all the tests locked up in her house until finals."

    show old_becca 1
    show old_roxxy 17
    roxxy "Benar-benar?"

    show old_roxxy 16
    show old_missy 1b
    missy "Yeah, I heard that too!"

    show old_missy 1
    roxxy "Hmm..."

    show old_roxxy 17
    roxxy "Ugh, this whole conversation is making my head hurt."

    show old_roxxy 18 at Position(xoffset=-20) with dissolve
    pause
    show old_roxxy 19 at Position (xoffset=-1) with dissolve
    roxxy "I'm gonna take a shower."

    show old_roxxy 20 at Position (xoffset=-67) with dissolve
    roxxy "Make sure nobody bothers me."

    show old_roxxy 21 with dissolve
    show old_becca 2
    becca "Dengan serius?"

    becca "We have stuff to do too, you know?"

    show old_becca 3
    show old_roxxy 22 with dissolve
    show old_missy 2
    missy "Yeah, we have to get to class soon!"

    show old_roxxy 23 with dissolve
    show old_missy 1
    show old_becca 1
    show old_roxxy 24
    roxxy "Oh, diamlah!"

    roxxy "You bitches can miss one class!"

    show old_missy 3
    roxxy "I really need to relax and clear my head for a bit..."

    show old_roxxy 23
    show old_becca 2
    becca "Uh, baiklah."

    show old_becca 1
    show old_missy 1
    missy "..."
    hide old_missy
    hide old_roxxy
    hide old_becca
    with dissolve
    pause
    show old_erik 61 at right
    show anon b_jersey f_worried
    with dissolve
    anon "Just grab your clothes, man. I'll deal with the girls."

    show old_erik 63
    erik "Hehe, baiklah."

    erik "Terima kasih kawan!"

    show old_erik 61
    anon f_normal "Tidak masalah!"

    hide anon
    hide old_erik
    with dissolve
    return

label boys_lockerroom_judith_changing:
    scene locker
    show anon f_normal_left:
        xoffset 50
    show judith:
        xzoom -1
        xoffset -100
    with {'master': dissolve}
    anon "Melihat?"

    anon "It's not too bad, there's only a few people in here!"

    show anon f_surprised
    show judith f_surprised
    show annie with {'master': dissolve}
    annie "I hope you two remember the rules in regards to being late!"

    annie "If you're not in uniform and in the courtyard in one min-"

    anon f_brag_closed "It's okay, {b}Annie{/b}... We get it."

    anon "We'll be outside in just a moment..."

    show anon f_worried
    show judith f_confused
    annie "As the Student Union President and official hallway monitor..."

    annie "... It is my duty to write infractions to anyone breaking school guidelines!"

    anon f_unimpressed "Look..."

    show judith f_normal
    anon f_unimpressed_bored "{b}Judith{/b} is not very comfortable in the guys' locker room."

    anon "She's going to need some extra time to get ready, okay?"

    show anon f_angry
    annie f_annoyed "Is that right, {b}Judith{/b}?"

    show anon f_worried_left
    judith f_sad_down "Ya..."

    judith "Y-ya..."

    show judith f_sad
    show anon f_angry
    annie "Ada apa?"

    annie "Just a little bit insecure around the boys?"

    annie "... Or are you inciting disorder and disobeying the rules?"

    show anon f_worried_left
    judith f_sad_down "It's not..."

    judith a_cover_face "It's just that..."

    show anon f_surprised_left
    judith f_cry @ f_sad_closed a_cover_boobs "... I'm not... Wearing a bra!"

    show anon f_surprised
    annie "Oh, I see... Coming up with excuses to skip class, are we?"

    annie f_normal "Your lack of obedience is alarming, and I will not allow it!"

    annie @ f_angry "Get dressed immediately, or I'm sending you both to detention!!"

    show anon b_dressed_changing3
    show judith f_sad_down b_dressed_remove01
    with {'master': dissolve}
    pause
    show judith b_dressed_remove02 with dissolve
    pause
    show anon b_dressed_changing2
    show judith b_dressed_remove03
    with {'master': dissolve}
    show judith b_dressed_remove04 with dissolve
    show judith b_dressed_remove05 with dissolve
    pause
    show judith b_pants_remove01
    show anon b_underwear f_sad_down
    with {'master': dissolve}
    pause
    show judith b_undies a_idle with dissolve
    anon f_surprised_left_low @ -m_talk "..."
    pause
    show anon f_surprised_down
    pause
    show anon o_underwear_boner1 with dissolve
    pause
    show anon o_underwear_boner2 with dissolve
    show annie f_shock_down1
    pause
    show annie f_shock_down2
    pause
    anon f_worried @ f_sad_down a_rub "Shit..." with hpunch
    judith a_surprised f_surprised_low "Ya ampun..."

    annie f_angry a_point1 "This..."

    pause
    annie a_point2 f_angry @ f_shock_down2 -m_talk "This is... Improper... And shameful!!"

    show judith f_sad_down a_idle with dissolve
    anon @ f_worried_left "I'm... So sorry..."

    annie a_note_write @ a_jersey_give "Put your uniforms on and get your asses to class, NOW!!!"

    show annie f_annoyed_down with None
    show judith b_pants_remove01:
        yoffset 30
    show anon b_dressed_changing2 o_empty:
        yoffset 30
    with {'master': dissolve}
    pause
    show judith b_shorts a_changing1:
        yoffset 0
    show anon b_jersey_changing:
        yoffset 0
    with {'master': dissolve}
    annie "I will have to report this incident to {b}Mrs. Smith{/b}, along with your infractions for being late..."

    show judith a_changing2
    show anon b_jersey
    with {'master': dissolve}
    pause
    show judith b_jersey f_sad_down a_idle
    with {'master': dissolve}
    annie a_note_hips f_annoyed "... Now, move it!!"

    hide judith
    hide anon
    hide annie
    with {'master': dissolve}
    $ renpy.end_replay()
    return

label boys_lockerroom_martinez_book_search:
    scene boys_locker_room_backpack_day_b
    show player 14f with dissolve
    player_name "Aha, there's {b}Martinez{/b}'s backpack!"

    player_name "They must be showering..."

    show player 13f
    player_name "..."
    show player 14f
    player_name "This is my chance."

    player_name "Remember, {b}[firstname]{/b}, sneaky!"

    hide player with dissolve
    return

label boys_lockerroom_webcam_quest:
    scene locker_night
    show player 14 at left with dissolve
    show old_erik 1 at right with dissolve
    player_name "Okay, this is the place!"

    show player 1
    show old_erik 5
    erik "The locker room?!"

    show old_erik 1
    show player 35
    player_name "Yah... But I need to {b}find a hidden spot{/b}..."

    player_name "... There has to be a place in this room where I could hide something small..."

    hide old_erik 1
    hide player 35
    return

label airvent_webcam_quest_intro:
    scene locker_night
    show player 34 at left with dissolve
    show old_erik 1 at right with dissolve
    player_name "Hmm..."

    show player 43
    show old_erik 13
    player_name "Up there!"

    show old_erik 14
    erik "The air vent?"

    show old_erik 1
    show player 14
    player_name "Yeah! It's perfect!"

    player_name "It has a view of the entire room..."

    player_name "... Just stand right under it."

    show player 17
    player_name "I'll climb on your shoulders to reach it!"

    show player 1
    show old_erik 3
    erik "Oke..."

    hide old_erik
    show player 128 at center
    with dissolve
    player_name "Alright, stay still!"

    hide player
    hide old_erik
    scene locker_closeup
    show player 129
    with dissolve
    player_name "Stay still!"

    show player 130
    player_name "It's almost done..."

    show player 131
    player_name "..."
    player_name "Di sana!"

    hide player
    scene locker_night
    show player 43 at left
    show old_erik 1 at right
    with dissolve
    player_name "Alright! Let's get out of here..."

    show player 11
    show old_erik 5
    erik "Should I know what this is about?"

    return

label airvent_webcam_quest_do_not_tell:
    show old_erik 3 at right
    show player 10 at left
    player_name "It's probably better if you don't know..."

    player_name "... It's nothing that bad, anyway..."

    show player 21
    player_name "... And it will help with my homework!!"

    show player 13
    erik "Okay, then..."

    show old_erik 5
    erik "... Can we leave now?"

    show old_erik 1
    show player 14
    player_name "Yeah, let's go."

    hide old_erik 1 with dissolve
    hide player 14 with dissolve
    return

label airvent_webcam_quest_tell:
    show player 24 at left
    show old_erik 1 at right
    player_name "{i}*Sigh*{/i}..."

    player_name "It's the librarian."

    show player 25
    player_name "She won't order the {b}textbooks{/b} I need..."

    player_name "... Unless I do this for her."

    show player 5
    show old_erik 5
    erik "What? Why?"

    show old_erik 1
    show player 10
    player_name "It seems like the library ran out of budget to get new books."

    player_name "Anyway, it's done now. Let's just go..."

    show player 13
    show old_erik 4
    erik "Okay. Thanks for letting me know about it."

    hide player 13 with dissolve
    hide old_erik 1 with dissolve
    return

label airvent_webcam_quest:
    call expression game.dialog_select("airvent_webcam_quest_intro")
    $ player.remove_item("supersaga_webcam")
    $ M_erik.set("webcam help", True)
    menu:
        "Can't tell you.":
            call expression game.dialog_select("airvent_webcam_quest_do_not_tell")
        "Hidden webcam.":

            call expression game.dialog_select("airvent_webcam_quest_tell")

    $ game.timer.tick()
    call expression game.dialog_select("town_map_dialogue")

label roxxy_shower_dialogue_intro:
    scene locker_empty_b with None
    show anon b_jersey f_surprised
    show old_becca 3f at Position(xpos=650)
    show old_missy 2f at right
    with dissolve
    missy "Uhh... What are you doing?"

    show old_missy 1f
    show old_becca 2f
    becca "The shower is occupied..."

    show old_becca 1f
    anon "I just finished gym class! I NEED to take a shower."

    show old_missy 2f
    missy "Uhh... No. You don't."

    show old_missy 1f
    anon f_worried @ f_skeptical "Yes, I do! I have music soon and I'm all sweaty!"

    anon "I can't go to class like this..."

    show old_becca 2f
    becca "We said it's occupied!"

    show old_becca 1f
    show old_missy 2f
    missy "Yeah, what part of \"occupied\" do you not understand?"

    show old_missy 1f
    anon f_unimpressed "I'm surprised you even know the meaning of the word \"occupied\"."

    show old_becca 4f
    becca "Haha!"

    show old_becca 3f
    show old_missy 4f
    missy "Hey, don't laugh at me, you dumb slut!"

    show old_missy 1f
    anon @ -m_talk "..."
    show old_becca 2 with dissolve
    becca "Don't call me a slut, you bimbo!"

    show old_becca 1
    show old_missy 2f
    missy "Well, don't call me a bimbo, you twat!"

    show old_missy 1f
    anon @ -m_talk "..."
    show old_becca 1f with dissolve
    becca "..."
    missy "..."
    return

label roxxy_shower_dialogue_leave:
    show old_becca 1f
    show old_missy 1f
    anon f_unimpressed "Fine!!"

    anon "I'll go shower at home..."

    show old_missy 3f
    show old_becca 2f
    becca "Hah?"

    becca "... Oh, right! Yeah, go shower at home!"

    becca "This is a nerd free zone!"

    show old_becca 1f
    show old_missy 1bf
    missy "Hehe, ya!"

    show old_missy 1f
    anon @ -m_talk "..."
    anon f_worried "You really shouldn't talk about people like that."

    show old_becca 2f
    becca "Whatever, loser."

    show old_becca 1f
    show old_missy 2f
    missy "Tersesat!"

    hide old_missy
    hide old_becca
    hide anon
    with dissolve
    return

label roxxy_shower_dialogue_please_fail:
    show old_becca 1f
    show old_missy 1f
    anon f_normal @ f_worried "... C'mon, pretty please?"

    pause
    show anon f_surprised
    show old_becca 2f
    becca "Begging isn't going to work on us, nerd boy..."

    show old_becca 3f
    show old_missy 8f
    missy "Yeah, we don't care how cute you are!"

    show old_missy 7f
    anon @ -m_talk "..."
    show old_becca 2b with dissolve
    becca "Apa-apaan ini, {b}Nona{/b}?!"

    show old_becca 1 with dissolve
    show old_missy 2f
    missy "... Hah?"

    show old_missy 1f
    show old_becca 2
    becca "Did you just say you think he's cute?!"

    show old_becca 1
    show old_missy 2f
    missy "No! I don't... I didn't..."

    missy "I mean... Ewww!!"

    show old_missy 1f
    show old_becca 2
    becca "... Whatever."

    show old_becca 1f with dissolve
    anon @ f_worried "Listen, I really need a shower!"

    show old_becca 2f
    becca "Oh... My... God! GO AWAY!"

    show old_becca 1f
    show old_missy 2f
    missy "We aren't letting you in, dork!"

    show old_missy 1f
    anon f_skeptical "Ugh, alright!"

    anon "I guess, I'll just go shower at home then!"

    hide old_missy
    hide old_becca
    hide anon
    with dissolve
    return

label roxxy_shower_dialogue_please_pass:
    show old_becca 1f
    anon f_normal "You know, you look great in that skirt {b}Missy{/b}!"

    show old_becca 3f
    becca "..."
    show old_missy 1bf
    missy "... I do?"

    show old_missy 1f
    anon f_laugh "Oh ya!"

    anon "It really shows off those long gorgeous legs of yours!"

    show anon f_grin
    show old_missy 1bf
    missy "You think my legs are gorgeous?"

    show old_missy 1f
    anon f_snarky "Yeah, I bet {b}Becca{/b} wishes she had legs like that!"

    show old_becca 2bf
    becca "What?! No I don't!"

    show anon f_normal
    becca "Who cares about legs?!"

    becca "Everyone knows all guys care about are tits and this skank can't compete with me there!"

    show old_becca 1f
    show old_missy 3f
    missy "!!!" with hpunch
    show old_becca 3f
    show old_missy 4f
    missy "Yeah, well, at least I'm not an ugly ass ginger!"

    show old_missy 4bf
    show old_becca 2b
    becca "!!!" with hpunch
    becca "Better a ginger than a fake tanned whore!"

    show old_becca 1
    show old_missy 4f
    missy "What?! This is natural, bitch!"

    missy "You're just jealous 'cause you look like Casper the Ghost's ugly girlfriend!"

    show old_missy 4bf
    show old_becca 2b
    becca "!!!" with hpunch
    becca "Persetan denganmu!"

    hide old_missy
    show old_becca 12f at right
    with dissolve
    missy "Ouch! What the..."

    becca "Rrraaaggh!!!"

    becca "Take it back!!!"

    show old_becca 13f at Position (xoffset=-85)
    missy "Make me!" with hpunch
    show old_becca 12f with dissolve
    anon "Welp."

    show old_becca 13f at Position (xoffset=-85) with dissolve
    anon "That should keep them busy for a while..."

    show old_becca 12f with dissolve
    anon @ f_laugh "Now, time for my shower!"

    hide old_becca
    hide anon
    with dissolve
    scene lockershowers with fade
    anon "..."
    show anon f_surprised b_jersey
    show old_roxxy 23f at right
    with dissolve
    pause
    show old_roxxy 25 with dissolve
    roxxy "!!!" with hpunch
    show old_roxxy 26
    show anon f_surprised_teeth
    roxxy "What the fuck are you doing in here?!"

    show old_roxxy 25
    anon f_worried "Uhh..."

    anon "... Taking a shower?"

    show anon f_surprised_teeth
    show old_roxxy 26
    roxxy "NO!! Get OUT of here!" with hpunch
    show old_roxxy 25
    anon f_skeptical "C'mon, {b}Roxxy{/b}... I really need a shower!"

    anon "I promise I won't look at you!"

    show anon f_normal
    show old_roxxy 26
    roxxy "How did you get past {b}Becca{/b} and {b}Missy{/b}?"

    show old_roxxy 25
    anon @ f_laugh "Oh, yeah... They're uhh... Having a little lovers quarrel out there..."

    show old_roxxy 26
    roxxy "Ugh, I'm surrounded by morons..."

    show old_roxxy 25
    anon @ f_laugh "... Actually, you're kinda like the Queen of the Morons."

    show old_roxxy 26
    roxxy "..."
    show old_roxxy 25
    pause
    show old_roxxy 26
    show anon f_surprised_teeth
    roxxy "Fuck you! Take your stupid shower!"

    roxxy "Aku keluar dari sini!"

    roxxy "... Brengsek."

    hide old_roxxy with fastdissolve
    anon f_worried "I'm just joking with you, {b}Roxxy{/b}..."

    pause
    anon f_normal @ -m_talk "( Oh well... )"

    anon @ -m_talk "( At least I can shower in peace now. )"

    anon @ f_laugh -m_talk "( {b}Roxxy{/b} sure does have a nice body on her! )"

    pause
    anon f_worried @ -m_talk "( I hope {b}Dexter{/b} doesn't find out about this... )"

    hide anon with dissolve
    return

label latinas_shower_dialogue:
    $ persistent.cookie_jar["Latina Twins"]["gallery"]["02_unlocked"] = True

    scene latinas_shower_cs01
    show text _ ("My heart raced as I quietly snuck the book out of {b}Martinez{/b}'s backpack...\nI knew they would tear me to pieces if they caught me.") as caption
    with fade
    pause

    scene latinas_shower_cs02
    show text _ ("But a final cursory glance into the shower revealed that I had nothing to worry about.\nIt seemed the girls were about to create their own distraction!") as caption
    with fade
    pause

    scene latinas_shower_cs03
    show text _ ("If they found out I was watching, I truly would be dead...\nBut it wasn't an easy scene to walk away from!") as caption
    with fade
    pause
    hide caption with dissolve
    show text _ ("They really did everything together...") as caption with dissolve
    pause

    $ renpy.end_replay()
    scene locker
    show player 14f
    with fade
    player_name "... I had better get out of here before they notice me."

    player_name "I hope I got the right book..."

    hide player with dissolve
    show book_06_c with dissolve
    player_name "{b}Chola's Tricks{/b}?"

    player_name "..."
    player_name "What the heck is a Chola?!"

    hide book_06_c with dissolve

    if M_bissette.is_state(S_bissette_jane_return_books):
        call expression game.dialog_select("bissette_book_search_2_books_left")
    elif M_bissette.is_state([S_bissette_got_dexters_book, S_bissette_got_eriks_book, S_bissette_got_martinez_book]):
        call expression game.dialog_select("bissette_book_search_1_book_left")
    else:
        call expression game.dialog_select("bissette_book_search_no_books_left")
    $ M_bissette.trigger(T_bissette_ask_martinez)
    $ player.get_item("cholas_tricks")
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
