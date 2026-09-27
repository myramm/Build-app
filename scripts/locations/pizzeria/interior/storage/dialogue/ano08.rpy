label ano08_sack_flour_fail:
    scene expression background(832, 370, 2.6) as stage
    show anon f_hurt b_flour with dissolve:
        xoffset 350
    anon "Ngghhh!"

    pause
    $ display.toast(str_fail)
    anon b_dressed_catch_breath "!!!" with hpunch
    anon "Holy crap, that's heavy!"

    pause
    anon f_sad_down b_dressed a_behind_head "I should really {b}hit the gym{/b} and build up my strength..."

    hide anon with dissolve
    return

label ano08_sack_flour_pass:
    scene expression background(832, 370, 2.6) as stage
    show anon f_hurt b_flour with dissolve:
        xoffset 350
    anon "Ngghhh!"

    pause
    $ display.toast(str_pass)
    anon b_dressed a_flour f_surprised "Holy crap, this is heavy!"

    anon f_hurt "Now I just need to {b}bring this to Maria{/b}."

    hide anon with dissolve

    $ player.go_to(L_pizzeria_kitchen)
    call maria_button_stage
    with fade
    show anon a_flour f_hurt behind maria with dissolve
    anon "Dimana kamu menginginkannya?"

    show maria a_spoon_sides f_normal with dissolve:
        unflip
        xoffset 0
    maria "Wow, you're stronger than you look..."

    anon "Hehe, terima kasih."

    maria @ a_spoon_point "Right over there will be fine."

    anon "Mengerti."

    show anon with dissolve:
        flip
        xoffset -500
    show anon with MoveTransition(4):
        xoffset -600
    show anon f_tired b_flour with dissolve
    anon "Phew, that's a lot of flour."

    show anon b_dressed a_idle with dissolve:
        unflip
        xoffset 0
    maria @ f_laugh "Well, we make a lot of pizza, don't we?"

    anon f_shy "Hehe, benar."

    anon f_normal "Can I get you anything else?"

    maria "Nah, you've done plenty, thanks."

    maria "Go and tell my husband that you deserve a raise, would ya?"

    anon f_shy "Heh, that's not necessary..."

    maria "No, I mean it!"

    maria "It's been so nice havin' someone dependable helpin' out around here..."

    maria "... Especially with all this pregnancy stuff {b}Tony{/b} and I are dealin' with."

    anon f_normal "Really, it's no problem."

    maria "We're real lucky we found ya, kid."

    anon "Heh, I feel the same way about you guys..."

    "{i}*Crash*{/i}{w=.25}{nw}" with hpunch
    show maria f_surprised a_mouth
    show anon f_hurt
    with {'master': fastdissolve}
    "{i}*Crash*{/i}{fast}"

    show anon f_surprised with {'master': dissolve}:
        flip
        xoffset -550
    tony "What the hell!"

    maria f_sad a_sides "{b}Tony{/b}?!"

    tony "Who do you think you are, breakin' my fuckin' door?!"

    show maria f_surprised
    dimitri "Privyet, fat boy."

    anon f_worried "Uh oh."

    show anon a_sides with dissolve
    show maria f_sad a_point
    hide anon
    with {'master': dissolve}
    maria "Where are you goin'?!"

    maria -a_point "Kid?!"

    maria "Don't go out there!"


    $ player.go_to(L_pizzeria_interior)
    scene expression player.location.background_closeup
    show tony f_angry:
        flip
        xoffset -70
    show xtra 12 as counter
    show igor:
        xoffset 250
    show dimitri f_grin:
        xoffset 100
    with fade
    dimitri "You make real food here or just this Italian shit bread?"

    dimitri "Some pelmeni or a nice borscht perhaps?"

    igor "No, {b}Dimitri{/b}, you always order the borscht..."

    igor "I want pirozhki this time!"

    dimitri f_angry_right "Shut up, idiot!"

    dimitri "Is just joke!"

    igor f_disgust_down "Aww, but I'm hungry..."

    dimitri "Focus!"

    igor "Sorry, {b}Dimitri{/b}."

    show igor f_normal
    show dimitri f_angry
    tony "Yeah, very funny, asshole."

    tony @ a_point "Why don't you two fuck off back to your boss now?!"

    tony "I ain't got time to deal with your nonsense."

    dimitri "Tsk, come now, that's not very hospitable..."

    dimitri "I just come to make talk."

    tony f_suspicious "Do you have any idea who you're dealin' with?"

    dimitri "Oh, everyone knows the Plumber."

    dimitri "Big-time heavy for Rossi up in Brooklyn..."

    dimitri @ a_out "... Many years ago, of course."

    pause
    dimitri @ a_point "I was surprised to find you here, in this sad little town."

    dimitri "Old, fat, and smelling of uncooked meat..."

    tony "'Ey, you betta watch ya fuckin' mouth!"

    dimitri @ f_normal "{b}Raz{/b} say, your boss no longer in business."

    tony @ -m_talk "..."
    dimitri f_grin "Is it true you tuck tail and run like sissy girl?"

    igor @ f_laugh a_point "Heh, sissy girl!"

    dimitri @ f_angry_right "Maybe we get him flower dress to wear, eh?"

    igor @ f_laugh "Hahahaah!"

    show anon f_angry behind counter with dissolve:
        xoffset -200
    anon "{b}Tony{/b}?"

    anon "Apa yang terjadi?"

    tony "Get back to the kitchen, champ."

    tony a_fists "Saya mengerti."

    dimitri f_normal "So, you mean to protect the boy?"

    show dimitri f_grin a_out with dissolve:
        xoffset 20
    dimitri "That is not so smart, fat boy..."

    show dimitri a_idle
    show tony a_point_under
    show tony_arms_dressed_a_point_under as arms:
        align (1., .1)
        crop (0, 0, 624, 768)
        xoffset -70
        xzoom -1
    with {'master': dissolve}
    tony "Back off, cream puff!"

    show tony a_fists
    hide arms
    with {'master': dissolve}
    tony "You don't wanna tango with me."

    dimitri f_angry "I will break you."

    show anon f_shock
    show tony f_surprised a_idle
    show maria f_angry a_shotgun behind dimitri:
        flip
        xoffset 110
    show dimitri a_sides f_surprised:
        xoffset 80
    with {'master': dissolve}
    maria "Get the fuck out of my shop!"

    show igor a_gun_jacket with {'master': dissolve}
    tony "{b}Maria{/b}!?"

    show anon f_surprised
    dimitri f_normal "Apa ini?"

    igor "Lady has gun, {b}Dimitri{/b}!"

    show anon f_worried
    show tony f_angry
    dimitri f_angry_right "Yes, I know."

    dimitri "I have eyes, idiot!"

    show dimitri f_angry
    maria "Get."

    maria "Out."

    dimitri "We just want the boy..."

    dimitri "Hand him over and we leave you in peace."

    maria "That's not happenin'."

    tony "You heard the lady."

    tony "Persetan!"

    anon @ -m_talk "..."
    pause
    igor f_curious "You want I should shoot them, {b}Dimitri{/b}?"

    show dimitri a_stop with dissolve
    pause
    dimitri f_grin a_point "That is big gun for lady..."

    show dimitri a_thinking with dissolve
    dimitri "You know how to use?"

    show maria a_shotgun_pump with dissolve
    pause .1
    show maria a_shotgun
    show dimitri f_surprised
    with dissolve
    maria "Take one more step and you're gonna find out."

    pause
    dimitri f_grin a_idle @ f_laugh "Hahahaah!"

    dimitri @ a_point_thumb "I like this one!"

    dimitri "She has balls."

    pause
    igor a_idle f_sad "Eugh!"

    igor "You like balls, {b}Dimitri{/b}?"

    dimitri f_angry_right "Itu bukan-"

    dimitri f_angry @ a_facepalm f_eyeroll "{i}*Huh*{/i} Sudahlah."

    dimitri "We go now."

    pause
    hide igor
    show dimitri:
        flip
        xoffset 700
    with dissolve
    pause
    show dimitri a_point behind maria with dissolve:
        unflip
        xoffset 200
    dimitri "But this isn't over, fat boy!"

    dimitri a_idle f_grin "Next time you need more than wife to protect you..."

    pause
    dimitri "See you soon, little bunny."

    anon @ -m_talk "..."
    hide dimitri with dissolve
    pause
    show anon f_sad_down
    show maria a_shotgun_point
    with {'master': dissolve}
    tony f_sad @ f_surprised "Jesus, {b}Maria{/b}..."

    show maria f_annoyed:
        unflip
        xoffset 30
    with dissolve
    maria "Don't you \"Jesus, {b}Maria{/b}\" me!"

    maria "I knew this was gonna happen!"

    tony f_angry "I had everything under control."

    maria "Bullshit, you had everything under control!"

    anon f_worried "This is all my fault..."

    maria "What, you were gonna fight 'em off with ya bare hands?!"

    maria "That big bald one woulda ate you alive!"

    show tony a_frustrated with {'master': dissolve}:
        xoffset 0
    tony a_idle @ a_frustrated "Bah, I've toppled trees bigger than that dirty Ruskie before!"

    anon "I'm so sorry."

    tony @ a_heart "Look, you're upsettin' {b}[firstname]{/b}..."

    maria f_sad @ -m_talk "..."
    maria "It's alright, kid."

    maria "We aren't gonna let anything happen to ya."

    anon "I can't believe I dragged you guys into this..."

    show tony f_normal with dissolve:
        unflip
        xoffset -400
    tony "'Ey, cut that out, champ."

    maria "You didn't drag us into anything."

    show tony f_suspicious with dissolve:
        flip
        xoffset 0
    tony "If anyone should be apologizin', it's that dumbass father of yours."

    show anon f_sad_down
    maria f_angry "{b}Toni{/b}!"

    tony @ a_frustrated "Apa?!"

    tony "Gettin' his family involved with these animals..."

    maria "You shouldn't speak ill of the dead!"

    show tony f_sad with dissolve:
        unflip
        xoffset -400
    pause
    tony "Sorry, champ."

    anon "N-no, you're right."

    anon "My dad's the one that started all this..."

    show maria f_sad
    pause
    anon f_worried "It's just so unlike him, you know?"

    maria "Everybody has secrets, kid."

    maria "You're learnin' that the hard way."

    tony "Somethin's gotta be done."

    show tony f_thinking a_thinking with dissolve
    anon "Apa maksudmu?"

    tony f_suspicious a_idle "I mean, I'm gonna check in with some of my old contacts..."

    maria f_confused "Eddie Four-Fingers?"

    show tony f_normal with dissolve:
        flip
        xoffset 0
    tony "Itu benar."

    tony "If anybody's got information on what {b}Raz{/b} is up to these days, it's him."

    anon "Why do they call him Four-Fingers?"

    tony @ f_normal_right "Because he's only got four fingers on his left hand, champ..."

    maria f_normal "He lost his pinky over a game of cards."

    anon @ f_surprised "!!!"
    tony @ f_smirk_wink "Heh, never bet on a pair of ducks."

    pause
    anon "Is there anything I can do to help you find him?"

    maria f_annoyed "No, I don't want you gettin' involved!"

    anon "But I'm already involved..."

    tony @ f_laugh "Hah!"

    tony "He's got you there, darlin'!"

    maria f_angry "You're not puttin' this kid in danger, {b}Tony{/b}!"

    maria "Maksudku!"

    tony @ a_frustrated "Baiklah, baiklah..."

    tony "I'm just sayin', you gotta respect the kid's gumption."

    maria @ -m_talk "..."
    show tony f_sad with dissolve:
        unflip
        xoffset -400
    tony "Look, champ, I know you wanna help out and get to the bottom of this whole thing..."

    tony "... And I promise I'll share whatever information I get with ya."

    tony "But until then, I want you to just lay low and keep ya nose clean."

    tony "berubah-ubah?"

    anon f_unimpressed "Why does everyone keep telling me to lay low?!"

    show maria f_sad
    anon "What good is that gonna do?"

    pause
    anon "And I'm not a kid, you know?!"

    tony f_normal @ f_laugh "Heh, we know that, champ..."

    maria "Tolong, {b}[firstname]{/b}."

    maria "For my sake?"

    anon f_sad_down "{i}*Huh*{/i}"

    anon "Bagus."

    tony f_normal "Di sana."

    show tony with dissolve:
        flip
        xoffset 0
    tony "Now could you put the gun away, please?"

    maria f_normal_down a_shotgun "Oh benar."

    maria f_normal @ f_laugh "I forgot I was holdin' the damn thing..."

    hide maria
    show tony f_laugh:
        unflip
        xoffset -400
    with dissolve
    tony "Well, that's real comfortin'!"

    show tony f_normal
    maria "Oh sial!"

    maria "My lasagna burned!"

    tony "I ain't never seen that woman point a gun at nobody before..."

    tony "She must have really taken a shine on you, champ."

    anon "When do you think you'll have that info?"

    tony "I'll start makin' the calls tonight but it might take me some time to track Eddie down."

    tony "In the meantime, these pizzas ain't gonna deliver themselves..."

    tony @ f_smirk_wink "You know what I mean?"

    anon f_sad_down "Ya baiklah."

    show tony a_mc_hip_single:
        xoffset -232
    show tony_arms_dressed_a_mc_shoulder_single:
        xoffset -232
    with dissolve
    tony "'Ey, chin up, champ!"

    tony "Uncle {b}Tony{/b}'s gonna see you through this..."

    anon f_sad "Terima kasih, {b}Tony{/b}."

    tony f_suspicious "You just focus on savin' that money up, capisce?"

    anon f_normal @ f_laugh "Ya baiklah."

    tony f_normal @ f_laugh "Attaboy!"


    $ game.timer.tick(2)
    $ player.go_to(L_pizzeria_exterior)
    scene expression player.location.background_blur with fade
    show anon f_worried with dissolve
    anon @ -m_talk "( Man, that was terrifying... )"

    anon @ -m_talk "( ... But {b}Maria{/b} and {b}Tony{/b} didn't seem fazed at all! )"

    pause
    anon @ -m_talk "( I'm sure they've dealt with bigger problems than {b}Dimitri{/b} and {b}Igor{/b} in the past; being ex-mafia and all. )"

    anon @ -m_talk "( I sure did luck out, finding them. )"

    pause
    anon @ -m_talk "( All I can do now is wait to see what {b}Tony{/b} finds out. )"

    hide anon with dissolve
    return


label ano08_sack_flour_late:
    scene expression background(832, 370, 2.6) as stage
    show anon a_sides f_worried_low with dissolve:
        xoffset 350
    anon @ -m_talk "( Ooops! I left it too late, {b}Maria{/b}'s not here right now. )"

    show anon f_worried:
        xoffset -150
        xzoom -1
    with {'master': dissolve}
    anon @ -m_talk "( I should probably come back during the day. )"

    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
