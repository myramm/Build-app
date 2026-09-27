label jenny_bedroom_cannot_snoop:
    if game.timer.is_evening():
        scene expression "backgrounds/location_home_jennybedroom_jenny_evening_blur.jpg"
    elif game.timer.is_dark():
        scene expression "backgrounds/location_home_jennybedroom_night_blur.jpg"
    else:
        scene expression "backgrounds/location_home_jennybedroom_jenny_day_blur.jpg"
    show anon f_worried with dissolve
    anon @ -m_talk "( I can't snoop around with {b}[jen_name]{/b} here! )"

    anon f_thinking a_thinking @ -m_talk "( I should come back when she is not around anymore. )"

    hide anon
    return

label sis_bedroom_jenny_pregnancy_announcement_repeat:
    scene expression player.location.background_blur
    show jenny f_upset a_crossed
    show anon f_worried with dissolve
    anon "You wanted to see me?"

    jenny "Ya."

    jenny "Congratulations, dummy... I'm pregnant again."

    show jenny f_angry_pouting
    anon @ f_shock "Apa lagi?!"

    show jenny f_angry
    jenny "I told you not to cum inside me!"

    anon @ f_tired "{i}*Huh*{/i}"

    anon "Does this mean you're gonna get all bitchy again?"

    jenny "PERmisi?!"

    anon @ f_shock "Apa-"

    anon "aku tidak bermaksud-"

    show anon f_surprised_teeth
    pause
    anon @ f_shock "Please, don't get the hair dryer..."

    jenny "Keluar saja!"

    anon f_worried "Well, hold on."

    anon "I know this isn't an ideal situation but I'm here for you, you know?"

    show jenny f_eyeroll
    jenny "Ugh, seriously get out!"

    show jenny f_angry
    anon "O-oke..."

    hide jenny with dissolve
    pause
    anon @ -m_talk "( Well, I tried... )"

    hide anon with dissolve
    return

label sis_bedroom_jenny_pregnancy_announcement_first:
    scene expression player.location.background_blur
    show anon f_worried with dissolve
    anon "Hey, I came as soon as I-"

    show jenny f_angry a_hit2 with dissolve
    show anon b_dressed_blocking with dissolve
    jenny "You fucking asshole!"

    show jenny a_hit with dissolve
    anon "Apa yang-"

    show jenny a_hit2 with dissolve
    jenny "I knew this was going happen!"

    show jenny a_hit with dissolve
    anon "Kenapa kamu-"

    show jenny a_hit2 with dissolve
    jenny "YOU STUPID, IDIOT, MOTHER-"

    show jenny a_hit with dissolve
    anon "Stop hitting me!"

    show jenny a_upset with dissolve
    jenny "Grrr!!!"

    show anon b_dressed f_skeptical with dissolve
    anon "Sheesh, what's gotten into you?!"

    jenny "Your potato-headed spawn, that's what!"

    anon "Hah?"

    show jenny a_crossed with dissolve
    jenny "I'm pregnant, you moron!"

    anon f_shock "!!!"
    anon "K-kamu hamil?!"

    show anon f_surprised_teeth
    jenny "Yes, dummy!"

    jenny "You just had to keep cumming inside me..."

    jenny "Menurutmu apa yang akan terjadi?!"

    anon f_skeptical "Hey, that's not fair!"

    anon "This is just as much your fault as it is mine!"

    show jenny f_eyeroll
    jenny "Pfft, whatever."

    show jenny f_angry_pouting_top
    pause
    anon f_worried "S-so, what are you going to tell {b}[deb_name]{/b}?"

    show jenny f_eyeroll
    jenny "Ugh, I don't know..."

    show jenny f_angry_pouting_top
    anon "She's going to figure it out eventually."

    show jenny f_upset
    jenny "Yeah, but not for a while, I'll think of something..."

    pause
    anon f_laugh "aku akan menjadi seorang ayah..."

    show anon f_grin
    show jenny f_eyeroll
    jenny "Yeah, I feel sorry for the kid already."

    show jenny f_angry_pouting_top
    anon f_normal "... And {b}[jen_name]{/b}, you're going to be a mother!"

    pause
    anon f_worried "You're not even a little bit excited?"

    show jenny f_sad
    pause
    jenny "T-tidak, aku-"

    show jenny f_angry
    pause
    show jenny a_upset with dissolve
    jenny "Grr, I can't believe you're excited about this!"

    anon "..."
    jenny "You're always a pain in my ass, you know that?!"

    show jenny a_crossed with dissolve
    anon "Saya minta maaf?"

    show jenny f_eyeroll
    jenny "Just, ugh... Forget it."

    show jenny f_upset
    jenny "Keluar."

    anon "Apa?!"

    show jenny f_angry
    jenny "Get the fuck out of my room, {b}[firstname]{/b}!"

    hide jenny with dissolve
    anon "O-oke..."

    $ player.go_to(L_home_hallway)
    scene expression player.location.background_blur
    show anon f_worried
    with fade
    anon @ -m_talk "( I'm not sure she knows how to feel right now... )"

    anon @ -m_talk "( ... And what will {b}[deb_name]{/b} do when she finds out?! )"

    show anon f_surprised_teeth
    pause
    anon "( Oh man, things are about to get a lot more complicated around here... )"

    hide anon with dissolve
    return

label sis_bedroom_jenny_cheerleader_sex:
    if store._in_replay is not None:
        $ player.location = L_home_sisbedroom
    scene expression player.location.background_blur with None
    show anon f_worried
    show jenny f_upset
    with dissolve
    anon "Alright, I got your uniform down from the attic."

    show jenny f_gross_down
    jenny "Is it all dusty?"

    show jenny f_gross
    anon "No, it looks fine to-"

    show jenny f_upset
    jenny "Give it here!"

    show jenny f_upset_down a_hips_cheer with dissolve
    pause
    jenny "Hmm, it'll have to do."

    anon @ -m_talk "..."
    show jenny f_upset
    jenny "Why are you still wearing clothes?!"

    anon "Uhh..."

    show jenny f_grin_down b_pull1 with dissolve
    pause
    show jenny b_pull2 with dissolve
    pause
    show jenny b_pull3 with dissolve
    show jenny b_pull4 with dissolve
    show anon f_surprised
    pause
    show jenny b_panties a_hips f_upset with dissolve
    show jenny f_upset
    jenny "Hurry up, my fans are waiting..."

    show jenny b_naked f_grin_down a_panties_remove with dissolve
    anon f_worried "B-benar..."

    show jenny b_cheer_dress1
    show anon b_dressed_changing
    with dissolve
    pause
    show anon b_dressed_changing2 with dissolve
    pause
    show anon b_underwear f_worried with dissolve
    anon "What are we doing today?"

    show jenny b_cheer_dress3 f_grin with dissolve
    jenny "Something special."

    show jenny b_cheer_dress2 with dissolve
    pause
    show jenny b_cheer a_hips f_sexy with dissolve
    jenny "Well, what do you think?"

    anon "It's a bit small..."

    show jenny f_laugh
    jenny "Haha, more than a bit!"

    show jenny b_cheer_showoff f_sexy with dissolve
    jenny "It's sexy though, right?"

    show jenny b_cheer_side f_normal
    with dissolve
    anon f_laugh "Y-ya!"

    show anon f_normal
    show jenny b_cheer a_hips f_sexy with dissolve
    jenny "Haha, good!"

    jenny "Naiklah ke tempat tidur."

    hide anon with dissolve
    pause
    jenny "... Dan kenakan topengmu!"

    scene expression "backgrounds/location_home_jennybedroom_closeup_peek.jpg" with None
    $ M_jenny.set('cam show mask', True)
    show anon b_bed_jenny_sit f_shy_down of_mask
    show jenny o_under_body_laptop o_naked_bed_belly_cheer b_naked_bed_bellytype f_sexy_down
    with dissolve
    pause
    show jenny f_laugh
    jenny "Hehe, see!"

    show jenny f_sexy_down
    jenny "I told you guys I used to be head cheerleader."

    pause
    jenny "Ah, benarkah?"

    pause
    jenny "So you always wanted to fuck a cheerleader, huh?"

    pause
    jenny "How about the rest of you boys?!"

    jenny "You wanna see me get fucked?"

    anon f_surprised @ -m_talk "( !!! )"
    "{i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i}"

    jenny "You can do better than that..."

    "{i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i}"

    show jenny f_laugh
    jenny "Hehehe!"

    show jenny f_sexy_down
    jenny "Baiklah, biarkan aku menyiapkan semuanya..."

    show jenny b_bed_climbing o_cheer_bed_climbing
    show anon b_bed_jenny_laying_undies_arms of_bed_jenny_laying_undies_arms_mask_X
    show expression "characters/anon/anon_overlay_dick_od_bed_jenny_laying_dick7.png" zorder 2
    show expression "characters/jenny/layeredimage/jenny_overlay_o_laptop.png"
    with dissolve
    jump jenny_cheer_sex_intro_prepare

label sis_bedroom_jenny_get_cheerleader_outfit:
    show anon f_worried
    show jenny f_upset a_crossed
    with dissolve
    jenny "Apa yang kamu lakukan?!"

    anon "You told me to meet you here this afternoon."

    jenny "Yeah, {b}with my cheerleading uniform{/b}!"

    anon "Oh benar."

    jenny "Hurry up and go {b}get it from the attic{/b}!"

    hide jenny with dissolve
    jenny "Idiot..."

    hide anon with dissolve
    return

label sis_bedroom_jenny_start_camshow_blowjob:
    if store._in_replay is not None:
        $ player.location = L_home_sisbedroom
        scene expression player.location.background_blur with None
    show anon f_worried
    with dissolve
    jenny "Itu dia!"

    show jenny b_naked a_hips f_upset with dissolve
    jenny "Ayo pergi!"

    anon "You're naked..."

    jenny "Tidak apa-apa?"

    jenny "Everyone is waiting on you, dummy!"

    anon "aku tidak-"

    jenny "C'mon, get your clothes off!"

    scene black with fade
    pause
    scene expression "backgrounds/location_home_jennybedroom_cutscene05.jpg" with dissolve
    jenny "Put your mask on!"

    anon "Aku tahu."

    jenny "Well, hurry up!"

    anon "Stop pulling me!"

    scene expression "backgrounds/location_home_jennybedroom_closeup_peek.jpg" with None
    $ M_jenny.set('cam show mask', True)
    show anon b_bed_jenny_sit f_shy_down of_mask
    show jenny o_under_body_laptop b_naked_bed_bellytype f_sexy_down
    with dissolve
    jenny "That's right, we're doing a special show today..."

    show jenny b_naked_bed_belly with dissolve
    pause
    jenny "You'll just have to wait and find out, won't you?"

    pause
    jenny "Oh, you wanna see his big dick, huh?"

    jenny "Well, I wanna see more tips!"

    "{i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i}"

    "{i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i}"

    jenny "Hehe, ini dia!"

    jenny "Give me a second to get everything set up..."

    show jenny o_laptop b_bed_climbing
    show anon b_bed_jenny_laying_undies_arms of_bed_jenny_laying_undies_arms_mask_X od_bed_jenny_laying_dick1
    show expression "characters/anon/anon_overlay_dick_od_bed_jenny_laying_dick1.png"
    with dissolve
    anon "A-apa yang kamu-"

    show jenny b_bed_back_sit a_sit_handcuffs with dissolve
    jenny "..."
    anon "H-hey, I didn't agree to handcuffs!"

    show jenny a_sit_tie
    show anon oh_bed_jenny_laying_undies_handcuffs
    with dissolve
    jenny "Diam!"

    hide expression "characters/anon/anon_overlay_dick_od_bed_jenny_laying_dick1.png"
    show expression "characters/anon/anon_overlay_dick_od_bed_jenny_laying_dick7.png"
    with dissolve
    if M_jenny.get("dominance") <= 0:
        jenny "You're only here to do what I tell you, remember?!"

        anon "Y-ya..."

        jenny "I think you mean, \"Yes, {b}Princess [jen_name]{/b}.\""

        anon "Yes, {b}Princess [jen_name]{/b}..."

        show jenny a_sit_hips with dissolve
        jenny "Hahahaah!"

    else:
        anon "This isn't funny, {b}[jen_name]{/b}!"

        anon "Get these off me!"

        jenny "Oh, just relax for a second."

        show jenny a_sit_hips with dissolve
        jenny "You're going to like this, I promise."

        anon "..."
    show jenny b_bed_back_look a_up f_normal with dissolve
    pause
    show jenny a_butt with dissolve
    jenny "Now, let's give the big fella some air, shall we?"

    show jenny b_bed_front_sit a_sides f_sexy_down with dissolve
    hide expression "characters/anon/anon_overlay_dick_od_bed_jenny_laying_dick7.png"
    show jenny a_pull1
    with dissolve
    pause
    show jenny a_pull2 with dissolve
    jenny "Hehe, looks like he's ready to give you guys a good show."

    show anon od_bed_jenny_laying_dick6
    show expression "characters/anon/anon_overlay_dick_od_bed_jenny_laying_dick6.png"
    show jenny a_sides
    with dissolve
    "{i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i}"

    show jenny f_sexy_down
    jenny "Today's not going to be about him though..."

    hide expression "characters/anon/anon_overlay_dick_od_bed_jenny_laying_dick6.png"
    show jenny b_bed_front_laying
    with dissolve
    pause
    jenny "Hehe, that's right."

    jenny "Today, my little boy toy is going to learn about eating pussy."

    "{i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i}"

    anon "Apa?!"

    anon "This wasn't-"

    show jenny b_bed_pussy1
    show expression "characters/anon/anon_overlay_dick_od_bed_jenny_laying_dick6.png"
    with dissolve
    anon "!!!"
    anon "Mrphmmmmll-"

    jenny "Apa itu tadi, mainan anak laki-laki?"

    jenny "We can't hear you..."

    show jenny f_laugh
    jenny "Hahahaah!"

    show anon od_empty
    show jenny b_bed_pussy f_sexy_down
    with dissolve
    jenny "C'mon, stop fighting and stick your tongue out!"

    pause
    jenny "{i}*Gasp*{/i} Oh, yeah!"

    jenny "Ini dia!"

    pause
    show jenny f_nipple2
    jenny "Mmm, fuuuuck..."

    show jenny f_sexy_down
    pause
    jenny "He's pretty good at this you guys!"

    show jenny f_nipple2
    jenny "Ahhh!"

    show jenny f_nipple3
    pause
    show jenny f_nipple2
    jenny "Ngghhh, right there!"

    show jenny f_nipple3
    jenny "{i}* Merengek*{/i}"

    pause
    show jenny f_nipple2
    jenny "Oh sial!"

    jenny "OHHH, SHIT!"

    jenny "aku akan-"

    show jenny f_nipple3
    "{i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i}"

    pause
    show jenny b_bed_pussy1 f_nipple2
    jenny "NGGHHH!!!" with flash
    pause
    hide expression "characters/anon/anon_overlay_dick_od_bed_jenny_laying_dick6.png"
    show jenny b_bed_front_laying f_nipple2
    show anon od_bed_jenny_laying_dick6
    with dissolve
    jenny "Haah... Haaah..."

    anon "{i}*Terkesiap*{/i}"

    anon "{i}*Batuk* *Gagap* *Batuk*{/i}"

    anon "I thought you were gonna drown me!"

    show jenny f_laugh
    jenny "Hehehe!"

    show jenny f_sexy_down
    jenny "So boys, how was the show?"

    jenny "Cukup bagus, ya?"

    pause
    jenny "Hmm?"

    pause
    show jenny f_gross_down
    jenny "Eww, fuck no!"

    pause
    jenny "No way! I don't do that!"

    pause
    jenny "Umm, because it's gross?"

    pause
    show jenny f_laugh
    jenny "Hehe, ya benar..."

    show jenny f_sexy_down
    jenny "You guys would have to tip me a ton of money before I'd ever consider-"

    "{i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i}"

    show jenny f_surprised_down
    "{i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i}"

    jenny "Aww, c'mon you guys..."

    show jenny f_gross_down
    anon "Apa yang terjadi?"

    jenny "{i}*Sigh*{/i} They want me to suck your dick..."

    anon "!!!"
    jenny "Apakah tidak ada hal lain yang bisa saya lakukan?"

    pause
    jenny "Uh, baiklah..."

    jenny "... But don't expect this to become a regular thing!"

    anon "{i}*Gulp*{/i} A-are you really going to-"

    show jenny b_bed_pussy1 f_upset
    show expression "characters/anon/anon_overlay_dick_od_bed_jenny_laying_dick6.png"
    with dissolve
    anon "!!!"
    jenny "Diam!"

    anon "Mrphmmmmll-"

    show jenny f_eyeroll
    jenny "{i}*Sigh*{/i} I can't believe I'm doing this..."

    $ animated = True
    $ anim_toggle = True
    $ M_jenny.set('sex speed', .12)
    scene expression "backgrounds/location_home_jennybedroom_sex_hj.jpg" with None
    show expression AnimatedImage("jenny_bj", [1,2,3,4,5,6,7,8,9], M_jenny) as jenny_bj at Position(xalign = 0.0, yoffset = 0)
    anon "Nnnrrrmmph-" with hpunch
    jenny "{i}*Gluulggh*{/i}"

    jump jenny_bj_loop

label sis_bedroom_jenny_get_a_mask_quest:
    scene expression player.location.background_blur with None
    show jenny f_angry
    show anon f_worried
    with dissolve
    jenny "Sudah waktunya!"

    anon "Hah?"

    jenny "I've been waiting forever!"

    anon "I came right-"

    show anon f_surprised
    jenny "Diam!"

    anon f_worried @ -m_talk "..."
    show jenny f_upset
    jenny "Ugh, this is such a bad idea..."

    if M_jenny.get("dominance") <= 0:
        anon @ f_confused "Are you going to tell me-"

        jenny "Didn't I tell you to shut up?!"

        anon "Ya?"

        jenny "So why are you still talking?!!"

        anon "Maafkan aku, aku-"

        show anon f_surprised
        jenny "Don't be sorry, be quiet!"

        anon f_worried @ -m_talk "..."
        jenny @ -m_talk "..."
        show jenny f_eyeroll
        jenny "Akhirnya!"

        show jenny f_upset
        jenny "{i}*Sigh*{/i} Alright, here's the deal."

        jenny "As I'm sure you've figured it out by now, I've been doing camshows for money recently..."

        jenny "... I know it's not the most glamorous profession but it's bringing in buttloads of money."

        anon "You realize {b}[deb_name]{/b} is going to kill you, right?"

        jenny "{b}Mom{/b} isn't going to find out!"

        anon @ -m_talk "..."
        show jenny f_angry
        jenny "I swear to god, I'll kill you if you say one peep to her!"

        anon "{i}*Gulp*{/i} I wouldn't-"

        anon "I mean, I'm not going to tell her!"

        jenny "Damn right you're not!"

        show jenny f_upset
        pause
        jenny "In fact, you're going to help me."

        anon f_surprised "Hmm?"

        jenny "You see, my fans are tired of watching me with just toys."

        jenny "They wanna see me with a real guy and since I can't find one of those..."

        show jenny f_eyeroll a_crossed with dissolve
        jenny "... You'll have to do."

        show jenny f_upset
        anon f_worried @ a_point_self "A-aku?!"

        jenny "Yes, you."

        anon "Are you talking, like... s-sex?"

        show jenny f_gross
        jenny "Sex?!"

        jenny "Eww, tidak!"

        show jenny f_angry
        jenny "What the hell is your problem?!"

        show jenny f_gross
        anon "T-tapi-"

        show jenny f_angry
        jenny "As if I would ever have sex with you, gross!"

        show jenny f_gross
        anon @ f_confused "Okay, I'm confused."

        show jenny f_eyeroll
        jenny "You're an idiot."

        show jenny f_gross
        anon "What do you want me to do?"

        show jenny f_upset
        jenny "I want you to sit on the bed and keep your mouth shut."

        jenny "Do you think you can manage that?!"

        anon "Y-ya."

        show anon at Position (xoffset=50) with dissolve
        jenny "Not right now, moron!"

        show anon with dissolve
        anon "B-but you just said-"

        jenny "We're not going to stream right this second!"

        jenny "Besides, we need a couple things first."

        anon "Seperti apa?"

        jenny "You need a mask or something."

        anon "A mask?"

        jenny "Yeah, to cover your face."

        anon @ f_confused "K-kenapa?"

        show jenny f_angry
        jenny "Umm, because I don't want anyone to know it's you, dummy!"

        show jenny f_upset
        jenny "Do you have any idea what people would say if they saw me doing stuff with you?!"

        show jenny f_eyeroll
        jenny "Ugh, I don't even wanna think about it."

        show jenny f_gross
        anon "Oh."

        show jenny f_upset a_hips with dissolve
        jenny "So just run over to the mall and pick up a ski mask or something..."

        anon "What if they don't have any ski masks?"

        jenny "Then figure something out, loser!"

        anon @ f_sad_down "{i}*Huh*{/i} Baik."

        anon "Ada lagi?"

        jenny "No, I'll get the other stuff."

        jenny "Just {b}don't come back here without a mask{/b}, got it?!"

        anon "Ya, saya mengerti."

        jenny "Bagus."

        jenny "Sekarang enyahlah!"

        hide jenny with dissolve
        pause
        anon f_sad_down "{i}*Huh*{/i}"

        show anon f_tired a_facepalm with dissolve
        anon @ -m_talk "( Alright, I should {b}head to the mall and look for a mask{/b}. )"

        hide anon with dissolve
    else:
        anon f_grumpy "Would you tell me what's going on already?!"

        show jenny f_upset
        jenny "Don't you raise your voice with me!"

        jenny "You're lucky I'm even consider-"

        anon "Okay, I'm outta here."

        show anon:
            flip
            xoffset -500
        with dissolve
        jenny "No, wait!!"

        show anon f_snarky:
            unflip
            xoffset 0
        with dissolve
        jenny "sial..."

        show jenny f_eyeroll
        jenny "{i}*Sigh*{/i} I need your help, okay?"

        show jenny f_gross
        anon f_worried @ f_skeptical "If you're gonna act like a bitch, then you can forget my help."

        show jenny f_upset
        jenny "Grr, fine!"

        show jenny f_eyeroll
        jenny "I'll... Ugh, I'll be nice."

        show jenny f_gross
        anon "Ya benar."

        show jenny f_upset
        jenny "Would you-"

        show jenny f_angry_pouting_top
        pause
        show jenny f_upset
        jenny "Can I at least explain the situation?"

        anon "Okay, let's hear it."

        show jenny f_eyeroll
        jenny "{i}*Sigh*{/i} As I'm sure you have figured it out by now, I've been doing camshows for money recently."

        show jenny f_upset
        anon f_normal "Heh, yeah... It wasn't exactly hard to piece together, {b}[jen_name]{/b}."

        show jenny f_angry
        jenny "Don't laugh, it's good money!"

        anon @ f_laugh "Heh, okay but you realize {b}[deb_name]{/b} is going to kill you, right?"

        jenny "You didn't tell her, did you?"

        anon "No, I didn't tell her."

        pause
        show jenny f_eyeroll
        jenny "Phew, that's good!"

        show jenny f_upset
        jenny "What {b}Mom{/b} doesn't know, won't hurt her."

        anon "So what do you want my help with?"

        show jenny f_sad
        jenny "Well, it's..."

        jenny "Y-you see..."

        anon @ f_skeptical -m_talk "..."
        anon "Just spit it out."

        jenny "My fans are..."

        jenny "... Well, they're tired of watching me with toys and..."

        pause
        anon "Dan?"

        jenny "... And they're offering to pay me a boatload of money, if I can find a man to stream with."

        anon f_shock "!!!"
        anon f_worried "Kamu tidak bisa serius..."

        show jenny f_upset a_crossed with dissolve
        jenny "Kenapa tidak?"

        jenny "Stupid {b}Cedric{/b} won't do it, plus you and I have already... done stuff."

        anon "Not on camera we haven't!"

        jenny "Jangan jadi banci."

        anon "What if they figure out who we are?!"

        jenny "They won't."

        show jenny f_grin
        jenny "You're gonna wear a mask."

        anon @ f_skeptical "Hah?"

        show jenny f_upset
        jenny "Yeah, we just need to get you a ski mask or something."

        anon "It's the middle of summer..."

        anon "Where are we gonna find a ski mask?!"

        jenny "It doesn't have to be a ski mask, just-"

        show jenny a_facepalm with dissolve
        jenny "{i}*Sigh*{/i} Just {b}go to the mall{/b} and find {b}a mask{/b}!"

        jenny "Any {b}mask{/b} will do."

        show jenny a_hips with dissolve
        anon @ f_skeptical "Am I going to get paid for this?"

        jenny @ -m_talk "..."
        jenny "You get to touch me, that's payment enough."

        anon f_skeptical "No, I want a cut."

        show jenny f_angry
        jenny @ -m_talk "..."
        anon "You won't get that money without me..."

        jenny "Oh my god, FINE!"

        jenny "Fucking pain in my ass."

        anon f_normal "Bagus."

        jenny "Keluar saja!"

        hide jenny with dissolve
        jenny "And don't come back without {b}a mask{/b}!"

        show anon f_thinking a_thinking with dissolve
        anon @ -m_talk "(Hmm, aku ingin tahu apa yang dia rencanakan untuk streaming?)"

        pause
        anon @ -m_talk "(Saya harus {b}mendapatkan masker{/b} jika saya ingin mengetahuinya... )"

        anon @ -m_talk "(Saya harus {b}pergi ke mal dan mencarinya{/b}. )"

        hide anon with dissolve
    return

label jenny_bedroom_jenny_deliver_bad_monster:
    scene expression "backgrounds/location_home_jennybedroom_closeup_peek.jpg"
    show jenny b_bed_reading a_phone1 f_laugh
    with dissolve
    jenny "Can you believe that?!"

    pause
    show jenny f_happy
    jenny "Yeah, I told him how much money it was bringing in, but he's being a little bitch about it!"

    pause
    jenny "No, he won't do it."

    jenny @ f_laugh "Haha! Yeah, I know!"

    pause
    jenny "I dunno, I'll find someone eventually..."

    show anon with dissolve
    show jenny f_upset
    jenny "!!!"
    show jenny a_phone2 with dissolve
    jenny "I'm on the phone!"

    anon "I got you something."

    show jenny f_surprised
    jenny "Hah?"

    show jenny f_angry
    anon "A present."

    show jenny f_upset
    jenny "You bought me something?"

    anon "Ya."

    jenny "Was it expensive?"

    anon @ f_thinking a_thinking -m_talk "..."
    anon "Ya."

    show jenny f_happy a_phone1 with dissolve
    jenny "{b}Jane{/b}, I'm gonna have to call you back."

    pause
    jenny "Haha, yeah... I'm sure they would love that."

    pause
    jenny "I'll keep that in mind..."

    jenny "You're such a slut!"

    pause
    show jenny f_laugh
    jenny "Haha, bye!"

    show jenny f_upset b_bed_dressed a_down with dissolve
    pause
    jenny "Okay, this had better be good."

    show anon a_backpack f_looking_down with dissolve
    pause
    show anon a_toy3 f_normal
    show jenny f_surprised
    jenny "!!!" with hpunch
    jenny "I-is that a {b}Bad Monster{/b}?!"

    anon "Ya."

    jenny "How did you-"

    show jenny f_upset
    jenny "Why did you buy this for me?!"

    anon "Well, you-"

    show jenny f_angry
    jenny "Did you read my diary?!"

    anon f_surprised "A-apa?"

    anon f_worried "Tidak!"

    anon "You just had me buying sex toys for you and I heard this was the best one and..."

    pause
    anon f_skeptical "I didn't read your diary! Sheesh!"

    jenny "You better not have!"

    jenny "Give me that!"

    show jenny f_grin_down a_bed_dressed_hips_toy4b
    show anon a_idle f_worried
    with dissolve
    pause
    jenny "It's awesome..."

    show anon f_flirt
    jenny "They're gonna go nuts for this!"

    anon "Who's gonna-"

    show jenny f_upset
    jenny "Hmm?"

    jenny "Oh, uhh... Nobody!"

    jenny "Just, shut up and get out!"

    anon f_grumpy "You're not even gonna say thank you?"

    if M_jenny.get("dominance") <= 0:
        show jenny f_eyeroll
        jenny "Eh, bukan?"

        show jenny f_upset
        jenny "I know there's probably some creepy motive behind this..."

        show anon f_worried a_behind_head with dissolve
        anon "No there's not!"

        anon "Can't I just do something nice for you?"

        jenny "Yeah right, whatever."

    else:
        show jenny f_eyeroll
        jenny "Ugh, thank you."

        show jenny f_upset
        show anon f_normal a_behind_head
        anon "Terima kasih kembali."

    show jenny f_angry
    jenny "Sekarang keluar!"

    show anon f_sad_down a_idle with dissolve
    anon "{i}*Huh*{/i} Baik."

    hide anon with dissolve
    pause
    show jenny f_grin_down
    jenny "Hehehehehe!"

    scene black with fade
    $ player.go_to(L_home_hallway)
    scene expression player.location.background_blur with None
    show anon f_grumpy with dissolve
    anon @ -m_talk "( Typical bitchy result... )"

    pause
    anon f_grin @ -m_talk "( Oh well, maybe she'll make another video for her {b}CAMslut profile{/b}! )"

    anon @ -m_talk "( I'll just have to wait and {b}check it in the morning{/b}. )"

    hide anon with dissolve
    return

label upstairs_bedroom_jenny_figure_out_password:
    scene expression player.location.background_blur with None
    show anon f_surprised with dissolve
    anon @ -m_talk "( Alright, I've gotta be quiet here... )"

    anon @ -m_talk "( I just need to {b}log into her laptop{/b} and find her {b}CAMslut{/b} stuff. )"

    anon f_flirt_grin @ -m_talk "( Easy peasy... )"

    hide anon with dissolve
    return

label sis_bedroom_jenny_get_a_toy:
    scene expression player.location.background_blur with None
    show anon f_worried
    show jenny
    with dissolve
    anon "Alright, I'm here."

    anon "Apa yang kamu inginkan?"

    show jenny a_hips f_normal with dissolve
    jenny "I found another way to make money."

    jenny "WAY better than that stupid Sluttygram site."

    anon "Oke."

    anon "Apa itu?"

    jenny "None of your business, loser."

    anon @ -m_talk "..."
    return

label sis_bedroom_jenny_get_a_toy_submissive:
    show anon f_worried
    anon "{i}*Sigh*{/i} C'mon, {b}[jen_name]{/b}..."

    show jenny f_upset
    jenny "Would you just shut up and listen!"

    anon @ -m_talk "..."
    show jenny f_normal
    jenny "I need you to go to the mall and buy something for me."

    anon @ f_skeptical "Why does it always come down to money with you?"

    jenny "Umm, because you have nothing else to offer me?"

    jenny "It's not that big a deal, it's only one hundred dollars..."

    show anon f_surprised
    pause
    anon f_worried "Another one hundred?!"

    anon "I dunno, that's a lot of money!"

    show jenny f_upset
    jenny "If you buy me this, I'll take everything off for you."

    anon f_confused "You'll get completely naked?"

    jenny "For two minutes..."

    show jenny f_angry
    show anon f_surprised
    jenny "But no touching!"

    show jenny f_upset
    show anon f_thinking a_thinking with dissolve
    anon @ -m_talk "..."
    show anon f_skeptical a_idle with dissolve
    anon "Baiklah baiklah."

    anon "I guess that's worth one hundred."

    show anon f_worried
    show jenny f_eyeroll
    jenny "It's worth a lot more than one hundred!"

    show jenny f_upset
    jenny "You're lucky I'm feeling generous..."

    return

label sis_bedroom_jenny_get_a_toy_end:
    show anon f_worried
    anon "So what am I buying?"

    show jenny f_normal
    jenny "I need you to {b}go to the mall and look on the second floor for a store called Pink{/b}."

    anon "{b}Pink{/b}, huh?"

    anon "Oke..."

    jenny "The toy I want is called {b}The Electro Clit{/b}."

    anon "Toy?"

    anon "Aren't you a little old for toys?"

    show jenny f_upset
    jenny "It's a sex shop, dummy..."

    anon f_shock "!!!" with hpunch
    anon a_point_self f_worried "You expect me to go into a sex shop?!"

    anon a_idle "No freaking way!"

    show jenny f_grin
    jenny "Aww, is the little virgin afraid of a big scary sex shop?"

    anon "W-what, no..."

    anon "I just... Why can't you go?!"

    anon "I'll give you the money and you can-"

    show jenny f_eyeroll
    jenny "I have other stuff I need to do!"

    show jenny f_upset
    jenny "Just man up and go, doofus."

    anon "F-fine."

    show jenny f_eyeroll
    pause
    hide jenny with dissolve
    pause
    anon @ -m_talk "( I can't believe she's making me do this... )"

    anon f_tired a_facepalm "( Ugh, let's just get it over with. )"

    hide anon with dissolve
    return

label sis_bedroom_jenny_get_a_toy_dominant:
    show anon f_worried
    anon "Okay, see ya."

    show anon:
        flip
        xoffset -500
    with dissolve
    pause
    show jenny f_sad a_upset with dissolve
    jenny "No, wait!"

    show anon:
        unflip
        xoffset 0
    with dissolve
    show jenny f_angry_pouting a_crossed
    pause
    show jenny f_upset
    jenny "I don't want to say, it's embarrassing..."

    anon f_skeptical "Benar-benar?"

    anon "I don't think I've ever seen you embarrassed about anything before."

    show anon f_worried
    jenny "Can you just help me, please?"

    anon "{i}*Huh*{/i} Baik."

    anon "... But only because you asked me so nicely."

    show jenny f_eyeroll
    jenny "Yeah, yeah, whatever."

    show jenny f_upset
    jenny "I need you to go to the mall and buy something for me."

    anon @ f_skeptical "Why does it always come down to money with you?"

    jenny "Don't be an asshole, you know I need the money."

    jenny "It's not that big a deal, it's only one hundred dollars..."

    anon f_shock "That's a lot of money, {b}[jen_name]{/b}!"

    show anon f_surprised
    show jenny f_eyeroll
    jenny "Don't be stupid, one hundred dollars is nothing."

    show jenny f_upset
    anon f_skeptical "{i}*Sigh*{/i} What's in it for me?"

    jenny "I dunno, I guess... I'll take everything off for you?"

    anon "You'll get completely naked in front of me, but you won't tell me what you're planning for money?"

    show jenny f_angry
    jenny "You wanna see me naked or not?"

    show anon f_thinking a_thinking with dissolve
    anon @ -m_talk "..."
    show anon f_normal a_idle with dissolve
    anon "Alright, sure."

    anon f_flirt "... But I get to look as long as I want."

    show jenny f_eyeroll
    jenny "Ugh, fine... Within reason."

    show jenny f_upset
    jenny "... And don't even think about touching because that's not happening, perv!"

    anon "Ya, ya..."

    return

label jenny_bedroom_jenny_go_to_her_room_dominant:
    scene expression "location_home_jennybedroom_day_blur" with None
    show jenny f_upset:
        flip
        xoffset 500
    show anon f_worried
    with dissolve
    anon "Listen, {b}[jen_name]{/b} I wasn't trying to-"

    hide jenny
    show jenny f_grin_down b_pull1
    with dissolve
    pause
    show jenny b_pull2
    anon f_surprised_teeth "!!!" with hpunch
    show jenny b_pull3 with dissolve
    show jenny b_pull4 with dissolve
    pause
    show jenny b_groping a_hips f_upset with dissolve
    anon f_shock "A-apa yang kamu lakukan?"

    show anon f_surprised_low
    jenny "Tell me these aren't the hottest pair of tits you've ever seen?!"

    show anon f_worried_low
    anon "Y-ya..."

    show anon f_shy_low o_boner with {'master': dissolve}
    anon "{i}*Gulp*{/i} Those are really nice!"

    jenny "That's what I thought."

    pause
    show jenny f_surprised_down
    pause
    jenny "Fuck! That's..."

    pause
    show jenny f_eyeroll
    jenny "... I should have made you pay for this."

    show jenny f_upset
    anon f_worried_low "I'll pay you."

    show jenny f_surprised
    jenny "Hmm?"

    anon f_flirt_low "If you let me touch them."

    show jenny f_eyeroll
    jenny "Ya benar!"

    show jenny f_upset
    jenny "In your dreams, loser!"

    show anon f_worried_low -o_boner with {'master': dissolve}
    anon @ -m_talk "..."
    anon f_worried "Bagus."

    show anon:
        flip
        xoffset -500
    with dissolve
    pause
    show jenny f_sad
    hide anon with dissolve
    pause
    jenny "Tunggu!"

    show anon f_flirt_grin with dissolve
    pause
    show jenny f_upset
    jenny "Two hundred."

    anon f_worried "Apa?"

    jenny "Two hundred and you can touch them."

    anon f_flirt "Baiklah."

    show anon f_flirt_low
    show jenny f_eyeroll
    jenny "... I cannot believe I'm doing this."

    show jenny f_upset
    jenny "You're lucky I need the money."

    return

label jenny_bedroom_jenny_go_to_her_room_dominant_has_money:
    show anon a_money with dissolve
    anon "Di Sini."

    show jenny f_eyeroll
    jenny "I should have asked for three hundred..."

    show jenny f_upset
    anon f_snarky "Too late now."

    show anon f_flirt_low a_idle with dissolve
    if M_jenny.finished_state(S_jenny_go_to_her_room):
        show jenny f_grin_down b_pull1
        with dissolve
        pause
        show jenny b_pull2
        pause
        show jenny b_pull3 with dissolve
        show jenny b_pull4 with dissolve
        pause
        show jenny b_groping a_hips f_upset with dissolve
    jenny "Just hurry up."

    hide anon
    show jenny b_groping_touch_look f_upset
    with dissolve
    pause
    show jenny b_groping_touch_talk
    anon "Wah!"

    anon "They're so soft!"

    show jenny f_eyeroll b_groping_touch
    jenny "Well yeah, dummy."

    show jenny f_upset
    pause
    show jenny a_up f_sad with dissolve
    jenny "Mmm, be careful!"

    jenny "My nipples are sensitive!"

    pause
    show jenny b_groping_suck a_up_clench f_nipple2
    jenny "!!!" with hpunch
    show jenny f_nipple1
    jenny "I never said you could-"

    show jenny f_nipple2
    jenny "Ahhh!"

    pause
    jenny "Fffffuu-"

    pause
    show jenny f_angry b_cover
    show anon f_depressed
    with dissolve
    jenny "Stop!"

    jenny "It's too much, I can't..."

    pause
    jenny "Ugh, you're such a pervert!"

    anon f_normal "You liked it."

    jenny "N-no, I didn't!"

    anon @ f_laugh "Pembohong."

    jenny "Just get out."

    anon "Bagus."

    anon "Pleasure doing business with you, {b}[jen_name]{/b}."

    hide anon with dissolve
    jenny "Diam!"


    $ player.go_to(L_home_hallway)
    scene expression player.location.background_blur with None
    show anon f_flirt_grin with dissolve
    anon @ -m_talk "( Wow, she's got like, the best tits in the world. )"

    anon @ -m_talk "( I can't believe she's letting me touch them! )"

    anon @ -m_talk "( This is awesome! )"

    hide anon with dissolve
    return

label jenny_bedroom_jenny_go_to_her_room_dominant_no_money:
    show anon f_worried
    anon "I don't have two hundred."

    show jenny f_upset
    jenny "Ugh, seriously?!"

    jenny "Well, you're definitely not touching them for free!"

    anon "I'll give you what I've got."

    jenny "Mustahil!"

    jenny "If you think I'm letting you touch them for anything less than two hundred, you're nuts!"

    anon @ -m_talk "..."
    anon "{i}*Huh*{/i} Baik."

    anon "{b}Saya akan kembali dengan uangnya{/b}."

    jenny "Cepatlah, pecundang."

    jenny "Saya butuh uang itu!"

    anon "Ya, ya."

    hide anon
    hide jenny
    with dissolve
    return

label jenny_bedroom_jenny_go_to_her_room_submissive:

    scene expression "location_home_jennybedroom_day_blur" with None
    show jenny a_phone f_grin_down:
        flip
        xoffset 500
    show anon f_worried
    with dissolve
    anon "Listen, {b}[jen_name]{/b} I wasn't trying to-"

    hide jenny
    show jenny b_dressed a_hips f_upset
    with dissolve
    jenny "Just shut up..."

    jenny "I've got a proposition for you."

    anon "Okay, what?"

    show jenny f_grin
    jenny "You're a horny little loser, right?"

    anon a_behind_head f_tired "What?! N-no..."

    show jenny f_upset a_crossed with dissolve
    jenny "And I need money, so..."

    pause
    show jenny f_eyeroll
    jenny "... How about you pay me two hundred dollars and I let you look at my tits?"

    show jenny f_upset
    anon a_idle f_skeptical "Two hundred dollars?!"

    anon f_worried "I dunno, that's a lot..."

    jenny "Yeah, but we're talking like actual, real tits here."

    jenny "Not anime tits like you're used to, loser."

    show anon f_thinking a_thinking with dissolve
    anon @ -m_talk "..."
    anon f_snarky "Bagus."

    return

label jenny_bedroom_jenny_go_to_her_room_submissive_has_money:
    show anon f_worried a_money with dissolve
    anon "Di Sini."

    show anon f_normal a_idle
    show jenny f_grin_down a_money_counting
    with dissolve
    pause
    show jenny f_eyeroll a_hips with dissolve
    jenny "I should have asked for three hundred..."

    show jenny f_gross
    pause
    show jenny f_upset
    jenny "{i}*Huh*{/i}"

    label repeat_boobies:
    jenny "I hope you can appreciate how lucky you are."

    show jenny f_grin_down b_pull1 with dissolve
    pause
    show jenny b_pull2 with dissolve
    pause
    show anon f_surprised
    show jenny b_pull3 with dissolve
    show jenny b_pull4
    anon f_shock "!!!" with hpunch
    show jenny b_groping a_hips f_grin with dissolve
    show anon f_flirt_low o_boner with {'master': dissolve}
    anon "Wah..."

    jenny "Tuck your tongue back into your mouth, nerd!"

    pause
    show jenny f_surprised_down
    pause
    jenny "I... T-that's..."

    pause
    anon "They're so-"

    jenny f_grin "Beautiful."

    show anon f_surprised a_surprised_up_both with dissolve
    jenny "Aku tahu."

    pause
    hide anon
    show jenny f_surprised b_groping_touch1 a_up
    jenny "!!!" with hpunch
    show anon f_surprised a_surprised_up_both o_boner
    show jenny f_angry b_cover
    with dissolve
    jenny "Hey, no touching!"

    show jenny b_groping a_up_clench
    show anon f_worried a_behind_head -o_boner
    with dissolve
    anon "Sorry, I didn't mean to-"

    show jenny f_upset a_hips with dissolve
    jenny "Pathetic little losers don't get to touch!"

    show anon f_surprised a_idle with dissolve
    show jenny b_pull1 with dissolve
    jenny "I think that's enough..."

    show jenny b_dressed a_hips f_upset with dissolve
    anon f_grumpy "Ah, ayolah!"

    jenny "No, you've looked plenty."

    show jenny f_grin
    jenny "You want to look again, you know the price."

    anon f_worried "Two hundred?"

    jenny "Itu benar."

    show jenny f_upset
    jenny "Now get out."

    hide jenny with dissolve
    pause
    show anon f_sad_down with dissolve
    anon "Aduh, bung..."

    hide anon with dissolve
    pause

    $ player.go_to(L_home_hallway)
    scene expression player.location.background_blur with None
    show anon f_laugh with dissolve
    anon "( Wow, she's got like, the best tits in the world. )"

    show anon f_flirt_grin
    anon @ -m_talk "( I wish, I could have touched them... )"

    anon @ -m_talk "( Maybe next time? )"

    hide anon with dissolve
    return

label jenny_bedroom_jenny_go_to_her_room_submissive_no_money:
    show anon f_worried
    anon "Aku bahkan tidak punya dua ratus!"

    show jenny f_upset
    jenny "Yah, aku tidak akan menunjukkan payudaraku padamu dengan harga kurang dari dua ratus."

    jenny "Jadi sebaiknya Anda pergi dan mengambilnya jika Anda ingin melihat hal-hal ini..."

    anon f_sad_down "{i}*Huh*{/i} Baik."

    anon f_tired "{b}Saya akan kembali dengan uangnya{/b}."

    jenny "Cepatlah, pecundang."

    jenny "Saya butuh uang itu!"

    anon "Ya, ya."

    hide anon
    hide jenny
    with dissolve
    return

label jennys_bedroom_jenny_caught_snooping:
    scene expression player.location.background_blur with None
    show anon f_surprised
    show jenny f_angry a_hips
    with dissolve
    jenny "Apa-apaan ini, {b}[firstname]{/b}?!"

    show anon f_surprised_teeth a_surprised_up_both
    anon "!!!" with hpunch
    show anon a_idle
    if M_jenny.finished_state(S_jenny_snoop_nightstand) and player.has_item('jenny_panties'):
        show jenny f_upset
        jenny "Oh.{w=1} My.{w=1} God."

        show jenny f_angry
        jenny "ARE THOSE MY PANTIES?!"

        anon f_shock "T-tidak?"

        anon "aku tidak-"

        show anon f_surprised_teeth
        jenny "Save it, loser. Give them here!"

        $ player.remove_item("jenny_panties")
        $ player.inventory.remove_picked_up("jenny_panties")
        show jenny f_upset
        jenny "I suppose you just stumbled in here by accident, huh?"

    else:
        show jenny f_angry
        jenny "What are you doing in my room, you perverted little loser?!"

        show anon f_shock
        anon "T-tidak ada apa-apa!"

        show anon f_surprised_teeth
        show jenny f_upset
        jenny "Oh, yeah right. You just stumbled in here by accident, huh?"

    show anon f_sad_down a_behind_head with dissolve
    anon "Not exactly..."

    show anon f_tired with dissolve
    anon "{i}*Sigh*{/i} I was looking for your digital camera, okay?"

    jenny "Huh, why?!"

    pause
    show jenny f_grin
    jenny "Oh, I get it."

    jenny "You're so pathetic, you know that?"

    jenny "You'd rather sit in your room fapping to stolen pictures of me, than go out and find real a girlfriend."

    show anon f_worried a_idle with dissolve
    anon "T-tidak."

    jenny "Haha, ya benar!"

    show anon f_depressed
    anon "..."
    show jenny a_camera_give with dissolve
    jenny "Tell you what, I'll let you look at the pictures, okay?"

    anon f_surprised "Y-you will?"

    jenny "Tentu."

    show anon f_worried
    show jenny a_camera_back with dissolve
    with dissolve
    jenny "{b}Sixty bucks{/b}."

    anon "Apa?!"

    jenny "{b}Sixty bucks{/b} and you can look at them for two minutes."

    anon "Two minutes?!"

    anon f_skeptical "You're out of your mind."

    show jenny f_upset
    jenny "Hey, you're the pathetic one who's hard up to get his rocks off..."

    jenny "You want to see the sexy pics or not?"

    menu:
        "Fine. {color=7ff7}[[Submissive]{/color}":
            $ M_jenny.decrement("dominance")
            if player.has_money(60):
                show anon f_worried a_money with dissolve
                anon "Di Sini."

                hide anon
                show player 727 at left
                show jenny f_grin a_money
                with dissolve
                jenny "Hahaha! Oh my god, you're so pathetic!"

                jenny "You've got two minutes..."

            else:
                show anon f_depressed
                anon "I don't even have sixty dollars..."

                show jenny f_eyeroll
                jenny "{i}*Sigh*{/i} God, you're pathetic."

                show jenny f_upset
                pause
                jenny "Fine, just give me what you do have."

                if not player.has_money(1):
                    show anon b_dressed_bow f_tired with dissolve
                    anon "I don't have anything... Please can I just look?"

                    jenny "Pathetic."

                    jenny "You've got 30 seconds..."

                else:
                    show anon f_worried a_money2 with dissolve
                    jenny "You've got two minutes..."

            $ player.spend_money(60)
        "Screw you. {color=f77b}[[Dominant]{/color}":
            $ M_jenny.increment("dominance")
            show anon f_grumpy
            anon "I'm not paying you {b}sixty dollars{/b} for a couple stupid pictures..."

            show jenny f_angry
            jenny "Permisi?!"

            anon f_skeptical "Anda mendengar saya!"

            show jenny f_angry_pouting a_crossed with dissolve
            jenny "Hmph!"

            pause
            show jenny f_upset
            jenny "{b}Thirty bucks{/b}?!"

            anon f_angry "TIDAK!"

            show jenny f_gross
            jenny "Dengan serius?!"

            show jenny f_angry
            jenny "Grr, just get out!"

            anon f_skeptical "Apa?"

            show jenny a_upset with dissolve
            jenny "Get out of my fucking room before I tell my mom you're perving on me!"

            anon "Dengan senang hati."

            hide anon with dissolve
            show jenny f_angry_pouting a_crossed with dissolve
            jenny "( He's such a pain in my ass! )"


            $ player.go_to(L_home_hallway)
            scene expression player.location.background_blur with None
            show anon f_grumpy with dissolve
            anon @ -m_talk "( Damn, I really wanted to see those pictures but not so much that I'll let her walk all over me. )"

            anon f_flirt_grin @ -m_talk "( At least I found out she's got a diary and just how sexually frustrated she is. )"

            anon f_laugh "( Haha! )"

            hide anon with dissolve
            return
    show expression "backgrounds/location_home_jennybedroom_photo01.jpg" at Position (yoffset=110) with dissolve
    pause
    show expression "backgrounds/location_home_jennybedroom_photo02.jpg" at Position (yoffset=110) with dissolve
    pause
    show expression "backgrounds/location_home_jennybedroom_photo03.jpg" at Position (yoffset=110) with dissolve
    pause
    scene expression player.location.background_blur with None
    show anon f_surprised
    show jenny f_upset a_camera_look
    with dissolve
    jenny "Times up, loser!"

    show jenny a_hips with dissolve
    show anon f_confused
    if not player.has_money(1):
        anon "That wasn't even 30 seconds!"

    else:
        anon "That wasn't even two minutes!"

    show jenny f_grin
    jenny "Aww, poor little virgin..."

    show jenny f_upset
    jenny "Go whine to somebody who cares."

    hide jenny with dissolve
    jenny "And get the fuck outta my room, LOSER!"

    anon "Bagus!"

    hide anon with dissolve
    $ player.go_to(L_home_hallway)
    scene expression player.location.background_blur with None
    show anon f_grumpy with dissolve
    anon "( She's such a bitch! )"

    anon f_laugh "( Those pics were worth it though... )"

    hide anon with dissolve
    return

label jennys_bedroom_jenny_snoop_around:
    scene expression player.location.background_blur with None
    show anon f_worried with dissolve
    anon @ -m_talk "( Okay, I just need to {b}find that camera and get out of here as quickly as possible{/b}. )"

    anon @ -m_talk "( She probably keeps it- )"

    anon f_surprised @ -m_talk "( !!! )"
    anon @ -m_talk "( Is that a diary?! )"

    anon f_laugh "( Oh, I have to check that out! )"

    hide anon with dissolve
    return

label sis_bedroom_sis_not_in_room:
    scene jennybedroom
    show anon f_thinking with dissolve
    anon @ -m_talk "( Hmmm... )"

    anon "( She's not in her room. )"

    anon f_grin "( Maybe I can look around a bit! )"

    hide anon with dissolve
    return

label sis_bedroom_sis_sleeping:
    scene jennybedroom_clear
    anon "( {b}[jen_name]{/b}'s sleeping. )"

    anon "( I have to be real quiet, or she might hear me... )"

    anon "( ... Don't want to wake her up, or I'm dead! )"

    return

label bedtable_night:
    call expression game.dialog_select("jenny_bedroom_cannot_snoop")
    jump expression game.dialog_select("upstairs_bedroom_dialogue")

label desk02_locked_dialogue:
    scene expression game.timer.image("sisbedroom{}")
    show anon f_thinking
    anon "( I don't have the {b}password{/b} for her computer... )"

    $ game.main()

label sister_bedtable_panties:
    scene expression player.location.background_blur with None
    show anon f_worried with dissolve
    anon @ -m_talk "( Hmm, it's not in here... )"

    pause
    show anon f_confused
    anon @ -m_talk "( Are those her panties? )"

    hide anon with dissolve
    return

label siscomp_day:
    scene expression player.location.background_blur
    show player 98 at Transform(align=(-.53, 1.)) with dissolve
    player_name "( Hmm... Let's see if she left her computer on. )"

    player_name "( I wonder what I could find on here... )"

    show jenny f_angry at right
    if L_home_shower.is_here(M_jenny):
        show jenny b_towelhead
    with dissolve
    jenny "..."
    jenny "Can I help you with SOMETHING??!" with hpunch
    hide player
    show anon f_shock
    with Dissolve(.2)
    anon "!!!"
    show anon f_shy a_behind_head
    show jenny a_crossed f_gross
    with dissolve
    anon "Sorry!! I was just... Trying to see if your internet is working!!"

    anon "I can't seem to connect on my computer..."

    jenny "Don't fucking {b}touch{/b} my computer!!"

    show anon f_looking_down a_idle with dissolve
    jenny "Just ask me next time."

    show jenny f_gross
    anon f_sad_down "Tentu saja!"

    show anon f_surprised_teeth
    show jenny f_angry
    jenny "Now, get out of {b}MY ROOM{/b}!!!"

    hide anon
    hide jenny
    with dissolve
    return

label jennys_bedroom_bissette_roxxy_cheerleader_deal:
    scene jennybedroom
    show jenny f_upset
    show anon f_worried
    with dissolve
    anon "Hai, {b}[jen_name]{/b}."

    jenny "Apa yang kamu inginkan?"

    show jenny a_crossed with dissolve
    anon "I need your help with something..."

    show jenny f_grin
    jenny "How much are you paying me?"

    anon f_skeptical "I haven't even told you what it is yet!"

    show anon f_worried
    jenny "Hmm, good point... I should hear all the details before I set the price!"

    anon @ f_tired "{i}*Huh*{/i}"

    anon "There's this girl at school who needs help with her cheerleading routine."

    jenny "Is this some girl you're trying to bang?"

    anon @ f_skeptical "Huh? NO!"

    show jenny a_hips with dissolve
    jenny "Why not? Is she ugly?"

    anon @ f_skeptical "No, she's gorgeous, but a total bitch!"

    jenny "Hmm, I like her already."

    anon @ -m_talk "..."
    anon @ f_confused "So you'll help her with the routine?"

    jenny "Five hundred dollars."

    anon @ f_surprised -m_talk "What?! Are you nuts?"

    show jenny f_upset
    jenny "That's the price."

    jenny "Pay up or get out."

    anon @ f_skeptical "Couldn't you just help me out?"

    show jenny f_laugh
    jenny "Hahahaha, good one {b}[firstname]{/b}!"

    show jenny f_upset a_hips_asking with dissolve
    jenny "Five hundred dollars."

    anon f_skeptical "{i}*Huh*{/i} Baiklah!"

    show jenny a_crossed with dissolve


    return

label jennys_bedroom_bissette_roxxy_cheerleader_deal_no_money:
    anon "I'll come back when I've got the money..."

    hide anon
    hide jenny
    with dissolve
    return

label jennys_bedroom_bissette_roxxy_jenny_spying:
    $ persistent.cookie_jar["Roxxy"]["gallery"]["02_unlocked"] = True
    $ suffix = ""
    if M_roxxy.get("roxxy trailer sex"):
        $ suffix = "_sex"
    call expression game.dialog_select("jennys_bedroom_bissette_roxxy_jenny_spying_pre")
    if M_jenny.is_set("seen MCs penis"):
        call expression game.dialog_select("jennys_bedroom_bissette_roxxy_jenny_spying_seen_penis{}".format(suffix))
    else:
        call expression game.dialog_select("jennys_bedroom_bissette_roxxy_jenny_spying_havent_seen_penis{}".format(suffix))
    call expression game.dialog_select("jennys_bedroom_bissette_roxxy_jenny_spying_after")
    $ del suffix
    $ renpy.end_replay()
    return

label jennys_bedroom_bissette_roxxy_jenny_spying_pre:
    scene jennybedroom_peek_c
    show jenny b_bed_cheer a_down f_normal
    show old_roxxy 36 at Position (xpos=415,ypos=692)
    show old_roxxy_outfit cheer 41b
    show poms 41 zorder 665
    show xtra 41 zorder 666
    with dissolve
    roxxy "Thanks again for letting me borrow your old uniform."

    show old_roxxy 35
    jenny "Tidak masalah!"

    jenny "It doesn't fit me anyways."

    jenny "Shit, this college uniform barely fits..."

    show old_roxxy 37
    roxxy "Haha, yeah."

    show old_roxxy 36
    roxxy "It looks like your tits are gonna spill out, like, any second..."

    show old_roxxy 35
    show jenny f_laugh
    jenny "hehe!"

    show jenny f_normal
    jenny "... That's what I'm saying though! The judges totally give extra points for sex appeal."

    jenny "That's why I never wear a bra during competitions."

    show old_roxxy 36
    roxxy "Y-yeah, I never thought about it."

    roxxy "You're like, a total genius!"

    show old_roxxy 35
    jenny "Tell me something I don't know..."

    jenny "These ladies won me three consecutive state championships!"

    show old_roxxy 36
    roxxy "... They are really nice..."

    show old_roxxy 38
    jenny "Terima kasih!"

    show jenny f_sexy_down
    jenny "Yours are nice too."

    show old_roxxy 36
    roxxy "Yeah, but mine aren't as big as yours..."

    show old_roxxy 38
    jenny "Mmm, maybe not but I betcha they're perkier than mine."

    show old_roxxy 37
    roxxy "Hehe, maybe..."

    show old_roxxy 35
    jenny "Lemme have a look at those puppies."

    hide old_roxxy
    hide old_roxxy_outfit
    show jenny b_bed_cheer_roxxy_lift1
    with dissolve
    roxxy "Whoa!! What are you-{p=1}{nw}"

    show jenny b_bed_cheer_roxxy_lift2 with dissolve
    pause .1
    show jenny b_bed_cheer_roxxy_lift3 with dissolve
    pause .1
    show old_roxxy 34b at Position (xpos=380,ypos=692)
    show jenny b_bed_cheer a_down f_normal
    with dissolve
    jenny "Tenang!"

    jenny "It's just us girls here."

    show jenny f_sexy_down
    roxxy "..."
    show old_roxxy 34
    roxxy "I-I dunno..."

    show old_roxxy 34b
    jenny "Di Sini."

    show jenny b_bed_cheerlift f_normal_low with dissolve
    pause
    show jenny b_bed_cheerup a_surprised f_happy_down with dissolve
    jenny "See, nothing to be embarrassed about!"

    show jenny f_sexy_down
    show old_roxxy 40 at Position (xpos=415,ypos=692)
    show old_roxxy_outfit cheer 41d
    with dissolve
    roxxy "... Y-yeah, I guess..."

    hide old_roxxy
    hide old_roxxy_outfit
    show jenny b_bed_cheer_roxxy_touch1
    roxxy "!!!" with hpunch
    jenny "I was right, they are perkier than mine..."

    jenny "I'm kinda jealous!"

    show jenny b_bed_cheer_roxxy_touch2
    roxxy "... Terima kasih."

    show jenny b_bed_cheer_roxxy_touch1
    jenny "You've got cute little nipples too!"

    roxxy "..."
    show jenny f_normal
    jenny "Aww, she's shy!"

    show jenny b_bed_cheer_roxxy_touch2
    roxxy "aku tidak-"

    show jenny b_bed_cheer_roxxy_touch1
    jenny "So adorable!"

    jenny "Don't you wanna feel mine?"

    show jenny b_bed_cheer_roxxy_touch2
    roxxy "You want me to-"

    show jenny b_bed_cheer_roxxy_grab1 f_sexy_down
    roxxy "!!!" with hpunch
    jenny "See, not so bad..."

    show jenny b_bed_cheer_roxxy_grab2
    roxxy "Your skin is so soft..."

    show jenny b_bed_cheer_roxxy_grab1
    jenny "Saya tahu, kan?"

    jenny "It's this special lotion I use. I'll hook you up!"

    show jenny b_bed_cheer_roxxy_grab2
    roxxy "Thanks, {b}[jen_name]{/b}!"

    show old_roxxy 39 at Position (xpos=415,ypos=692)
    show jenny b_bed_cheerup a_down f_laugh
    show old_roxxy_outfit cheer 41d
    with dissolve
    jenny "Damn girl! You've got a bangin' body!"

    show jenny f_sexy_down
    show old_roxxy 40
    roxxy "You think the judges will notice?"

    show old_roxxy 39
    show jenny f_normal
    jenny "Benar sekali!"

    if M_roxxy.get("roxxy trailer sex"):
        jenny "I can't believe {b}[firstname]{/b} is hitting that!"

        show old_roxxy 40
        roxxy "Hehe, well, I really made him work for it."

        roxxy "He's a pretty tenacious guy..."

    else:
        jenny "I can see why that dweeb downstairs wants to hit that."

        show old_roxxy 40
        roxxy "I can't believe you two live together!"

        roxxy "You're so awesome, and he's such a dork!"

    show old_roxxy 39
    return

label jennys_bedroom_bissette_roxxy_jenny_spying_seen_penis:
    show jenny f_normal
    jenny "He's not so bad..."

    jenny "He can be pretty useful to have around."

    show old_roxxy 40
    roxxy "... Yeah, I guess he has been pretty helpful recently."

    show old_roxxy 39
    jenny "Also, just between you and me..."

    jenny "He's hung like a horse!"

    show old_roxxy 40
    roxxy "Really?! You mean you've seen his dick?"

    show old_roxxy 39
    jenny "Oh, I've seen it plenty of times."

    jenny "We do live together after all."

    show old_roxxy 40
    roxxy "I guess that's true..."

    roxxy "So it's big, huh?"

    show old_roxxy 39
    show jenny f_laugh
    jenny "Huge!"

    show jenny f_normal
    show old_roxxy 42
    roxxy "Menarik."

    show old_roxxy 39
    jenny "Is your boyfriend packing?"

    show old_roxxy 40
    roxxy "{b}Dexter{/b}?"

    show old_roxxy 42
    roxxy "Pfft."

    show old_roxxy 43 with dissolve
    show jenny f_laugh
    jenny "Ha ha ha!"

    show jenny f_normal
    show old_roxxy 39 with dissolve
    jenny "Tiny, eh? That's too bad."

    roxxy "..."
    jenny "Well, anyways... You ready to learn some moves?"

    show old_roxxy 37
    roxxy "Ya, ya!"

    show old_roxxy 39
    show jenny f_laugh
    jenny "Cool, let's do it!"

    return

label jennys_bedroom_bissette_roxxy_jenny_spying_havent_seen_penis:
    show jenny f_normal
    jenny "Saya tahu benar!"

    jenny "I tell everybody he's the maintenance boy..."

    show old_roxxy 37
    roxxy "Ha ha ha!"

    show old_roxxy 40
    roxxy "Yeah, my boyfriend threatens to kick his ass all the time."

    show old_roxxy 39
    jenny "You have a boyfriend?"

    show old_roxxy 40
    roxxy "Yah, agak..."

    roxxy "Let's just say, he thinks he's my boyfriend."

    show old_roxxy 39
    jenny "I like your style, {b}Roxxy{/b}!"

    show old_roxxy 40
    roxxy "Hehe, terima kasih!"

    show old_roxxy 39
    jenny "Is he packing?"

    show old_roxxy 40
    roxxy "Apa maksudmu?"

    show old_roxxy 39
    jenny "You know, down south..."

    jenny "Is he big?"

    show old_roxxy 42
    roxxy "Pfft..."

    show old_roxxy 43 with dissolve
    show jenny f_laugh
    jenny "He's small?!"

    show jenny f_normal
    show old_roxxy 40 with dissolve
    roxxy "Real tiny."

    show old_roxxy 39
    show jenny f_laugh
    jenny "Ha ha ha!"

    show jenny f_normal
    show old_roxxy 40
    roxxy "Yeah, I don't keep him around for the sex."

    show old_roxxy 39
    jenny "I wouldn't think so..."

    roxxy "..."
    jenny "Well, anyways... You ready to learn some moves?"

    show old_roxxy 37
    roxxy "Ya, ya!"

    show old_roxxy 39
    show jenny f_laugh
    jenny "Cool, let's do it!"

    return

label jennys_bedroom_bissette_roxxy_jenny_spying_seen_penis_sex:
    show jenny f_normal
    jenny "Yeah, he can be really stubborn..."

    jenny "He's resourceful though, I'll give him that."

    show old_roxxy 40
    roxxy "Plus, he's got that huge cock!"

    show old_roxxy 39
    jenny "I know right?!"

    jenny "He's hung like a freaking horse!"

    show old_roxxy 40
    roxxy "Whoa, wait... You mean you've seen it?"

    show old_roxxy 39
    jenny "Oh, I've seen it plenty of times."

    jenny "Kind of unavoidable really. Living in close proximity like this."

    show old_roxxy 40
    roxxy "Ya, menurutku itu masuk akal."

    roxxy "It must be annoying living with some random dude..."

    show old_roxxy 39
    show jenny f_laugh
    jenny "Hehe, I dunno. It has its perks."

    show jenny f_normal
    roxxy "..."
    jenny "Was your last boyfriend packing?"

    show old_roxxy 40
    roxxy "{b}Dexter{/b}?"

    show old_roxxy 42
    roxxy "Pfft."

    show old_roxxy 43 with dissolve
    show jenny f_laugh
    jenny "Ha ha ha!"

    show jenny f_normal
    show old_roxxy 39 with dissolve
    jenny "Tiny, eh? That's too bad."

    show old_roxxy 35e at Position (xoffset=-120, yoffset=100)
    roxxy "Yeah, he turned out to be a huge douchebag too."

    show old_roxxy 39
    jenny "Well, anyways... You ready to learn some moves?"

    show old_roxxy 37
    roxxy "Ya, ya!"

    show old_roxxy 39
    show jenny f_laugh
    jenny "Cool, let's do it!"

    return

label jennys_bedroom_bissette_roxxy_jenny_spying_havent_seen_penis_sex:
    show jenny f_normal
    jenny "Not hard enough, {b}Roxxy{/b}!"

    jenny "He'd have to kiss my feet and grovel like a dog before I let him in my panties..."

    show old_roxxy 37
    roxxy "Hahaha! Sheesh, you're a hardcore bitch, {b}[jen_name]{/b}!"

    show old_roxxy 40
    roxxy "Lucky for him, you aren't interested, huh?"

    roxxy "Otherwise, I could totally see him trying..."

    show old_roxxy 39
    jenny "... Yeah. Lucky for him..."

    jenny "... So, is he any good?"

    show old_roxxy 40
    roxxy "What do you mean? Like, in bed?"

    jenny "Ya."

    roxxy "He's amazing!"

    show old_roxxy 39
    jenny "Amazing? You're joking."

    show old_roxxy 40
    roxxy "No, I'm completely serious!"

    roxxy "He's like an idiot savant or something..."

    roxxy "... And he's got that massive cock!"

    show old_roxxy 39
    show jenny f_sad
    jenny "Huh? What do you mean by massive?"

    show old_roxxy 43b
    hide old_roxxy_outfit
    with dissolve
    roxxy "..."
    show old_roxxy 39
    show old_roxxy_outfit cheer 41d
    with dissolve
    show jenny f_normal
    jenny "You're joking!"

    show old_roxxy 40
    roxxy "Not even a little bit."

    show old_roxxy 39
    show jenny f_sad
    jenny "Astaga..."

    show old_roxxy 40
    roxxy "It's super crazy!"

    show old_roxxy 39
    show jenny f_laugh
    jenny "Ha ha ha!"

    show jenny f_normal
    show old_roxxy 40
    roxxy "I swear, he's like an orgasm machine!"

    show old_roxxy 39
    jenny "Menarik..."

    roxxy "..."
    jenny "Well, anyways... You ready to learn some moves?"

    show old_roxxy 37
    roxxy "Ya, ya!"

    show old_roxxy 39
    show jenny f_laugh
    jenny "Cool, let's do it!"

    return


label jennys_bedroom_bissette_roxxy_jenny_spying_after:
    scene black with fade
    scene hallway
    show anon f_flirt_grin with dissolve
    anon @ -m_talk "( Wow!!! )"

    anon f_laugh "( Maybe this wasn't such a bad idea after all! )"

    hide anon with dissolve
    return


label home_sisbedroom_picture2_dialogue:
    scene expression background(568, 432, 9) as stage
    show closeup_picture2
    pause
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
