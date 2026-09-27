label school_righthallway_eve_ross_argument:
    scene expression player.location.background_blur
    show anon f_skeptical a_salute with dissolve
    anon @ -m_talk "Hmm?"

    show anon a_idle with dissolve
    anon f_worried "It looks like {b}Miss Ross{/b} is arguing with {b}Eve{/b}..."

    anon "I wonder what that's about?"

    return

label prom_poster:
    show expression game.timer.image("prom_poster_day{}")
    pause
    anon "( The prom is coming up soon. )"

    anon "( Seems like it'd be a good time... If I had a date. )"

    anon "( I'd better hurry and find someone. )"

    anon "( I wonder who I could ask. )"

    $ game.main()

label school_righthallway_roxxy_go_in_auditorium:
    scene expression player.location.background_blur
    show player 642 at left
    show old_erik 4 at right
    with dissolve
    erik "Hei!"

    erik "What's up, dude?!"

    show old_erik 1
    show player 641
    player_name "Oh, hey, {b}Erik{/b}."

    player_name "I'm just taking these records to the auditorium for {b}Miss Dewitt{/b}..."

    show player 642
    show old_erik 4
    erik "Ah, right on..."

    erik "It looks heavy!"

    show old_erik 1
    show player 641
    player_name "A bit, yeah."

    player_name "Apa yang kamu lakukan di sini?"

    show player 642
    show old_erik 4
    erik "I was just heading to the auditorium too."

    erik "I've got a small break before my next class and its usually quiet and dark in the auditorium."

    erik "Which is perfect for playing games on my handheld!"

    show old_erik 1
    show player 641
    player_name "Hmm, why do you need it dark and quiet?"

    show player 642
    show old_erik 5
    erik "I err... I dunno."

    show old_erik 4
    erik "It's just more peaceful I guess!"

    show old_erik 5
    erik "You want me to help you carry that?"

    show old_erik 1
    show player 641
    player_name "Nah, I've got it."

    player_name "What game are you playing-"

    show player 642
    show old_erik 1b
    dexter "Aww, c'mon {b}Becca{/b} just lemme get a peek..."

    player_name "..."
    show old_erik 3b
    erik "Wait a second. Was that {b}Dexter{/b}?"

    show old_erik 52
    show player 641
    player_name "Yeah, it sounds like him..."

    show player 642
    show old_erik 3b
    erik "What the heck is he doing in the auditorium?"

    show old_erik 52
    show player 641
    player_name "No idea..."

    player_name "We should check it out!"

    show player 642
    show old_erik 3b
    erik "... Ehh, really?"

    show old_erik 52
    show player 641
    player_name "Yeah, man. C'mon!"

    hide player
    hide old_erik
    with dissolve

    scene location_school_assembly_hall_cutscene08
    show text _ ("What was going on in the assembly hall?") as caption
    with fade
    pause

    scene assembly_hall_paint02_c
    show old_dexter 34
    show old_becca 2 at left
    with fade
    becca "{b}Dexter{/b} stop it!"

    becca "Ugh, is this what you called me in here for?!"

    show old_becca 1
    show old_dexter 35
    dexter "Hah?!"

    dexter "What's the problem?"

    dexter "{b}Roxxy{/b} and I are on a break and you're always wearing those low-cut tops with your tits hanging out anyways..."

    dexter "Just let me see 'em for a second."

    show old_dexter 34
    show old_becca 2
    becca "Mustahil!"

    becca "We're at school!"

    becca "... And even if we weren't. I don't like you that way."

    show old_becca 1
    show old_dexter 35
    dexter "Psh, stop pretending you don't want it..."

    show old_dexter 34
    show old_becca 2
    becca "I'm not pretending anything!"

    show old_becca 1
    show old_dexter 36
    dexter "Hey, what's that on your jeans?!"

    show old_becca 14 at Position (xoffset=86) with dissolve
    becca "Hmm?"

    show old_dexter 37 at left
    hide old_becca
    with dissolve
    becca "Ouch! What the fuck, {b}Dexter{/b}!"

    show old_becca 14 at left
    show old_becca 14 at Position (xoffset=86)
    hide old_dexter
    show old_dexter 35
    with dissolve
    dexter "Hahaha, I've always thought you had a great butt..."

    show old_dexter 34
    hide old_becca
    show old_dexter 38 at left
    with dissolve
    becca "Goddamnit. I'm leaving!"

    show old_dexter 40 with dissolve
    dexter "Hei!"

    dexter "You aren't going anywhere 'til I see those tits!"

    show old_dexter 39
    becca "What the hell is with you today?!"

    becca "Aku bilang tidak!"

    show old_dexter 40
    dexter "Nobody tells me no!"

    scene black with fade
    scene expression game.timer.image("backgrounds/location_school_right_hall{}_blur.jpg")
    show player 12f at right
    show old_erik 51f
    with dissolve
    player_name "We have to do something!"

    show player 90f
    show old_erik 3bf
    erik "B-but... {b}Dexter{/b} will kill us!"

    show old_erik 51f
    show player 12f
    player_name "We can't just stand here! C'mon!"

    hide player
    hide old_erik
    with dissolve
    scene assembly_hall_paint02_c
    show old_erik 51 at Position (xpos=950)
    show player 12f at Position (xpos=775)
    show old_dexter 34 at Position (xpos=400)
    show old_becca 16 zorder 1 at left
    with dissolve
    player_name "Back off her!"

    show player 90f
    show old_dexter 24 at Position (xoffset=47)
    dexter "Hmm?!"

    show old_dexter 23 at Position (xoffset=47)
    show old_becca 17 with dissolve
    becca "Screw you, {b}Dexter{/b}!"

    hide old_dexter
    show old_becca 18
    dexter "Ghhurt!" with hpunch
    show old_dexter 41 at Position (xoffset=-80)
    show old_becca 2b
    with dissolve
    becca "Brengsek!"

    show old_becca 19
    hide old_dexter with dissolve
    dexter "{i}*Cough*{/i}"

    hide player
    show old_becca 21f at Position (xpos=421)
    with dissolve
    player_name "!!!"
    show old_erik 3b
    erik "Sialan!"

    show old_erik 52
    show old_becca 19 at Position (xpos=400)
    show player 10f at Position (xpos=775)
    with dissolve
    player_name "{b}Becca{/b}, are you okay?"

    show player 11f
    show old_becca 20
    becca "{b}[firstname]{/b}!!!"

    becca "I was just... I mean, {b}Dexter{/b} was..."

    show old_becca 19
    show player 12f
    player_name "I know. We saw it..."

    show player 5f
    becca "..."
    show old_erik 4
    erik "You just kicked his nuts to the moon!"

    erik "Itu luar biasa!"

    show old_erik 1
    show old_becca 20
    becca "... It was?"

    show old_becca 19
    show player 14f
    player_name "Haha, sepenuhnya."

    show player 13f
    dexter "Ugh... {i}*Cough* *Sputter*{/i}"

    show player 12f
    player_name "... Are you sure you're okay though?"

    show player 5f
    show old_becca 20
    becca "{i}*Sniff*{/i} Yeah, I think so..."

    becca "I've never seen him act that way before!"

    show old_becca 19
    show player 12f
    player_name "Well, don't worry. I don't think he'll try something like that again..."

    show player 14f
    show old_dexter 41 zorder 0 at Position (xpos=400) with dissolve
    player_name "... Man, you really got him good!"

    show player 13f
    dexter "{i}*Cough*{/i} Uhh... My... Nads..."

    show old_roxxy 3cf at Position (xpos=75) with dissolve
    roxxy "What the hell is going on-"

    show old_roxxy 2cf
    roxxy "What's the matter with {b}Becca{/b}?"

    show old_roxxy 27f at Position (xoffset=34) with dissolve
    roxxy "..."
    show old_roxxy 28f at Position (xoffset=34)
    roxxy "... And why are you holding your balls, {b}Dexter{/b}?"

    show old_roxxy 27f at Position (xoffset=34)
    menu:
        "Tell {b}Roxxy{/b}.":
            show player 12f
            player_name "{b}Dexter{/b} was trying to force {b}Becca{/b} to flash him."

            show player 90f
            show old_becca 19f
            show old_roxxy 3cf
            with dissolve
            roxxy "... Seriously?"

            show old_roxxy 3bf
            show old_erik 3b
            erik "Yeah, we saw it."

            show old_erik 52
            show old_roxxy 3f
            roxxy "You idiot!"

            roxxy "What the hell's the matter with you?!"

            show old_roxxy 3bf
            show old_dexter 41 at Position (xoffset=2)
            dexter "{i}*Gasp* *Wheeze*{/i} ... Help."

            show old_dexter 41 at Position (xoffset=0)
            show old_becca 20f
            becca "{i}*Sniff*{/i} {b}[firstname]{/b} ran in and tried to stop him."

            show old_becca 19f
            show old_roxxy 2cf
            roxxy "You stood up to {b}Dexter{/b}?"

            show old_roxxy 2bf
            show player 10f
            player_name "Err, kinda..."

            show player 5f
            show old_roxxy 3cf
            roxxy "Are you nuts?"

            roxxy "You realize he would kill you, right?"

            show old_roxxy 3df
            show player 12f
            player_name "... Tidak?"

            show player 90f
            show old_roxxy 2f
            roxxy "Uhh, yeah. He would absolutely destroy you."

            roxxy "Jangan bodoh."

            show old_roxxy 1f f
            show old_dexter 41 at Position (xoffset=2)
            dexter "Uhh... You're so dead, {b}[firstname]{/b}..."

            show old_dexter 41 at Position (xoffset=0)
            show player 11f
            show old_roxxy 3f
            roxxy "Oh, diamlah!"

            roxxy "You're not gonna do a damn thing!"

            show player 13f
            roxxy "If this gets out you'll be expelled for sure!"

            roxxy "... And that will be the least of your problems!"

            show old_roxxy 3bf
            show old_dexter 41 at Position (xoffset=2)
            dexter "..."
            show old_dexter 41 at Position (xoffset=0)
            show old_roxxy 3f
            roxxy "Uh huh. That's what I thought."

            show old_roxxy 3cf
            roxxy "C'mon, {b}Becca{/b}. I'll walk you to the locker room."

            show old_roxxy 3df
            becca "..."
            show old_roxxy 3d with dissolve
            show old_becca 20f
            becca "Tunggu!"

            show old_becca 5 with dissolve
            pause
            show old_becca 22f at Position (xpos=457)
            hide player
            with dissolve
            show old_roxxy 3df
            player_name "!!!" with hpunch
            show old_becca 8 at Position (xpos=400)
            show player 13f at Position (xpos=775)
            with dissolve
            show old_roxxy 2bf
            becca "Terima kasih."

            show old_becca 7
            show old_roxxy 1f f
            show player 14f
            player_name "Heh, I didn't really do anything."

            show player 13f
            show old_becca 8
            becca "Ya, benar!"

            becca "saya..."

            becca "... Just thanks!"

            hide old_becca
            hide old_roxxy
            with dissolve
        "Remain silent.":

            show player 10f
            player_name "aku uhh..."

            show player 5f
            player_name "..."
            show old_becca 20f with dissolve
            becca "{b}Dexter{/b} was forcing me to flash him!"

            show old_becca 19f
            show old_roxxy 3cf with dissolve
            roxxy "... Seriously?"

            show old_roxxy 3bf
            show old_erik 3b
            erik "Yeah, we saw it."

            show old_erik 52
            show old_roxxy 3f
            roxxy "You idiot!"

            roxxy "What the hell's the matter with you?!"

            show old_roxxy 3bf
            show old_dexter 41 at Position (xoffset=2)
            dexter "{i}*Gasp* *Wheeze*{/i} ... Help."

            show old_dexter 41 at Position (xoffset=0)
            show old_becca 20 with dissolve
            becca "{i}*Sniff*{/i} {b}[firstname]{/b} ran in and tried to stop him."

            show old_becca 19f with dissolve
            show old_roxxy 2cf
            roxxy "You stood up to {b}Dexter{/b}?"

            show old_roxxy 2bf
            show player 10f
            player_name "Err, kinda..."

            show player 5f
            show old_roxxy 3cf
            roxxy "Are you nuts?"

            roxxy "You realize he would kill you, right?"

            show old_roxxy 3df
            show player 10f
            player_name "... Tidak?"

            show player 5f
            show old_roxxy 2f
            roxxy "Uhh, yeah. He would absolutely destroy you."

            roxxy "Jangan bodoh."

            show old_roxxy 1f f
            show old_dexter 41 at Position (xoffset=2)
            dexter "Uhh... You're so dead, {b}[firstname]{/b}..."

            show old_dexter 41 at Position (xoffset=0)
            show player 11f
            show old_roxxy 3f
            roxxy "Oh, diamlah!"

            roxxy "You're not gonna do a damn thing!"

            roxxy "If this gets out you'll be expelled for sure!"

            show player 5f
            roxxy "... And that will be the least of your problems."

            show old_roxxy 3bf
            show old_dexter 41 at Position (xoffset=2)
            dexter "..."
            show old_dexter 41 at Position (xoffset=0)
            show old_roxxy 3cf
            roxxy "Uh huh. That's what I thought."

            roxxy "C'mon, {b}Becca{/b}. I'll walk you to the locker room."

            hide old_becca
            hide old_roxxy
            with dissolve
    show player 13f
    player_name "..."
    show old_erik 3b
    erik "... So, you're really friends with them now, huh?"

    show old_erik 52
    show player 14 at Position (xpos=700) with dissolve
    player_name "Yeah, kind of."

    show player 13
    show old_erik 4
    erik "That's so awesome, dude!"

    show old_erik 1
    show old_dexter 41 at Position (xoffset=2)
    dexter "{i}* Merengek*{/i}"

    show old_dexter 41 at Position (xoffset=0)
    show player 11
    show old_erik 3b
    erik "... Uhh, we should probably get out of here."

    show old_erik 52
    show player 12
    player_name "Yeah, let's go."

    hide player
    hide old_erik
    with dissolve
    scene expression player.location.background_blur
    show player 13 at left
    show old_erik 4
    with dissolve
    erik "... So what happened after the fake ID?"

    show old_erik 1
    show player 14
    player_name "I don't think I can say..."

    player_name "... But I've been helping {b}Roxxy{/b} out with some personal stuff."

    show player 13
    erik "..."
    show old_erik 4
    erik "Oooh, I get it. Ten-four, dude."

    erik "I hear what you're saying."

    show old_erik 1
    show player 14
    player_name "Heh, what? I don't think you do..."

    show player 13
    show old_roxxy 3c at right with dissolve
    roxxy "Well, that was a mess..."

    show old_roxxy 3d
    show old_erik 1f with dissolve
    show player 10
    player_name "Is {b}Becca{/b} doing okay?"

    show player 5
    show old_roxxy 33 with dissolve
    roxxy "Yeah, she's fine."

    roxxy "She was just a bit shocked is all."

    show old_roxxy 30 with dissolve
    roxxy "I can't believe {b}Dexter{/b} did that!"

    roxxy "I mean, he's done a lot of stupid shit in the past..."

    show old_roxxy 3c
    roxxy "... But never anything creepy!"

    show old_roxxy 3d
    show player 10
    player_name "Well, I'm just glad {b}Erik{/b} and I were there..."

    show player 5
    show old_roxxy 2
    roxxy "... Who's {b}Erik{/b}?"

    show old_roxxy 1
    show old_erik 2f with dissolve
    erik "..."
    show player 12
    player_name "Umm, my friend {b}Erik{/b}..."

    show player 90
    show old_roxxy 1b
    roxxy "Oh benar!"

    roxxy "Sorry, I forgot you were there."

    show old_roxxy 1
    show old_erik 3bf with dissolve
    erik "... That's okay."

    show old_erik 1f
    show old_roxxy 1b
    roxxy "So uhh, I was gonna tell you..."

    roxxy "The girls and I are doing a bikini contest this weekend and you should totally come!"

    show old_roxxy 1
    show old_erik 51f
    show player 10
    player_name "Benar-benar?"

    show player 14
    player_name "Kedengarannya luar biasa!"

    show player 13
    show old_roxxy 2
    roxxy "I know right?!"

    show old_roxxy 1b
    roxxy "Just {b}come to the beach on Saturday afternoon{/b}!"

    show old_roxxy 1
    show old_erik 1f
    show player 14
    player_name "Alright, I'll be there."

    show player 13
    show old_roxxy 1b
    roxxy "Heh, cool."

    roxxy "See ya, {b}[firstname]{/b}!"

    hide old_roxxy with dissolve
    pause
    show old_erik 4 with dissolve
    erik "Whoa, dude!"

    erik "A bikini contest?!"

    erik "That's so awesome!"

    show old_erik 1
    show player 14
    player_name "You wanna come with me?"

    show player 13
    show old_erik 3b
    erik "Aww, I can't."

    erik "I wish I could, but I've got a raid with my guild Saturday afternoon..."

    show old_erik 52
    show player 12
    player_name "Skip it!"

    show player 14
    player_name "C'mon man, think about all those bikinis!"

    show player 13
    show old_erik 3b
    erik "Are you nuts?! I can't skip a raid!"

    erik "That's a 50 DKP MINUS!"

    show old_erik 52
    show player 10
    player_name "... Hah?"

    show player 5
    show old_erik 3b
    erik "It's a big deal, dude!"

    show old_erik 52
    show player 14
    player_name "Heh, alright. Fine."

    player_name "I guess I'll go by myself then..."

    show player 13
    show old_erik 3b
    erik "Shoot, I've gotta get to computer lab."

    show old_erik 3
    erik "I'll catch you later, dude."

    show old_erik 4
    show player 14
    player_name "See you around, {b}Erik{/b}."

    hide player
    hide old_erik
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
