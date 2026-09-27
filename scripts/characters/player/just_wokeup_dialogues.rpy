label player_jenny_sleepover_mcbedroom:
    scene expression "backgrounds/location_home_bedroom_cutscene19.jpg" with fade
    pause
    scene expression "backgrounds/location_home_bedroom_cutscene20.jpg" with dissolve
    player_name "!!!"
    scene expression "backgrounds/location_home_bedroom_cutscene21.jpg" with dissolve
    player_name "Anda akan pergi?"

    if M_jenny.get("jenny_girlfriend_first_time"):
        $ M_jenny.set('jenny_girlfriend_first_time', False)
        scene expression "backgrounds/location_home_bedroom_cutscene15b.jpg" with dissolve
        jenny "Yeah, the sun is up which means your time is over."

        scene expression "backgrounds/location_home_bedroom_cutscene15.jpg"
        player_name "Oh."

        scene expression "backgrounds/location_home_bedroom_cutscene15b.jpg"
        jenny "Besides, {b}[deb_name]{/b} will be awake soon and I don't want her finding me in here."

        scene expression "backgrounds/location_home_bedroom_cutscene15.jpg"
        player_name "Did you sleep okay?"

        scene expression "backgrounds/location_home_bedroom_cutscene15b.jpg"
        jenny "I did, actually."

        jenny "In spite of your crazy loud snoring."

        scene expression "backgrounds/location_home_bedroom_cutscene15.jpg"
        player_name "Apa?!"

        player_name "I don't snore!"

        scene expression "backgrounds/location_home_bedroom_cutscene15b.jpg"
        jenny "Heh, whatever."

        scene expression "backgrounds/location_home_bedroom_cutscene15.jpg"
        player_name "Can we do this again?"

        scene expression "backgrounds/location_home_bedroom_cutscene15b.jpg"
        jenny "Sure, as long as you're paying."

        scene expression "backgrounds/location_home_bedroom_cutscene15.jpg"
        player_name "Tapi-"

        scene expression "backgrounds/location_home_bedroom_cutscene15b.jpg"
        jenny "Nanti, pecundang."

    else:
        scene expression "backgrounds/location_home_bedroom_cutscene15b.jpg" with dissolve
        jenny "Yeah, {b}[deb_name]{/b} will be up soon."

        scene expression "backgrounds/location_home_bedroom_cutscene15.jpg"
        player_name "Oh baiklah."

        scene expression "backgrounds/location_home_bedroom_cutscene15b.jpg"
        jenny "Remember to come by {b}my room{/b} this afternoon for our show."

        scene expression "backgrounds/location_home_bedroom_cutscene15.jpg"
        player_name "Alright, I will."

    scene black with dissolve
    return

label player_jenny_sleepover_sisbedroom:
    scene expression player.location.background_blur
    show jenny b_panties a_hips f_upset
    show anon b_underwear f_normal
    with fade
    anon "Good morning!"

    show jenny f_eyeroll
    jenny "Ya, ya..."

    show jenny f_upset
    jenny "Get lost, I need a shower."

    anon f_skeptical "Sheesh, that's it?"

    anon "You're not a very fun person to wake up next to..."

    jenny "Nah, apa yang kamu ingin aku lakukan?!"

    jenny "Fix you breakfast or something?"

    jenny "Get real."

    anon f_worried "I would never ask you to do that, {b}[jen_name]{/b}..."

    anon f_laugh "... I've tasted your cooking, it's awful."

    show anon f_grin
    show jenny f_eyeroll a_crossed with dissolve
    jenny "Persetan denganmu!"

    show jenny f_upset
    anon f_laugh "Hahaah!"

    hide anon with {'master': dissolve}
    jenny f_gross "Brengsek."


    $ player.go_to(L_home_hallway)
    scene expression background(360, 360, 4.) as stage with fade
    show anon a_rub b_underwear f_surprised_teeth_down with dissolve:
        flip
        xoffset -200
    anon @ -m_talk "( Ooops! I completely forgot my clothes! )"

    anon a_idle f_normal @ -m_talk "( I should have another set in my room... )"

    hide anon with dissolve
    return

label bedroom_sis_webcam_show:
    show anon f_thinking a_thinking with dissolve
    anon @ -m_talk "Hmm..."

    anon @ -m_talk "( I wonder what {b}[jen_name]{/b} is doing right now. )"

    anon f_flirt @ -m_talk "( Maybe I could {b}connect to her webcam from my computer{/b}... )"

    hide anon with dissolve
    return

label bedroom_dewitt_make_replacement_guitar:
    if game.timer.is_dark():
        show anon with dissolve
        player_name "I think I have everything I need to make my fake guitar."

        anon f_thinking a_thinking "I need to remember to assemble it in the garage tomorrow."

        hide anon with dissolve
    else:
        show anon with dissolve
        player_name "I think I have everything I need to make my fake guitar."

        player_name "I should {b}head back to the garage{/b} so I can start working on it."

        hide anon with dissolve
    return

label bedroom_sis_telescope_1:
    show anon f_thinking a_thinking with dissolve
    anon @ -m_talk "( I wonder what {b}Erik{/b} is doing right now. )"

    anon @ -m_talk "( I should use my {b}telescope{/b} and see what he's up to... )"

    hide anon with dissolve
    return

label bedroom_sis_telescope_2:
    show anon f_thinking a_thinking with dissolve
    anon @ -m_talk "( I wonder what {b}Mia{/b} is doing right now. )"

    anon @ -m_talk "( I should use my {b}telescope{/b} and see what she's up to... )"

    hide anon with dissolve
    return

label bedroom_sis_telescope_3:
    show anon f_thinking a_thinking with dissolve
    anon @ -m_talk "( I wonder what {b}Mrs. Johnson{/b} is doing right now. )"

    anon @ -m_talk "( I should use my {b}telescope{/b} and see what she's up to... )"

    hide anon with dissolve
    return

label bedroom_master_somrak_training:
    show anon f_thinking a_thinking with dissolve
    anon @ -m_talk "( I wonder if {b}Master Somrak{/b} is ready to train me again. )"

    hide anon with dissolve
    return

label bedroom_roxxy_spin_bottle:
    scene expression player.location.background_blur
    show anon with dissolve
    anon "{b}Roxxy{/b} and the girls wanted me to {b}visit the beach this afternoon{/b}."

    anon "I should {b}head there now{/b}!"

    hide anon with dissolve
    return

label bedroom_roxxy_spin_bottle_no_goldschwagger:
    scene expression player.location.background_blur
    show anon f_thinking a_thinking with dissolve
    anon @ -m_talk "( I also still need to {b}talk to Captain Terry about GoldSchwagger for Becca{/b}. )"

    hide anon with dissolve
    return

label ano01_init_wakeup:
    scene expression player.location.background_blur with dissolve
    show anon f_grin with dissolve
    anon @ -m_talk "( I feel so free this morning! )"

    anon f_thinking a_thinking @ -m_talk "( What shall I do today? )"

    hide anon with dissolve
    return

label ano01_cops_wakeup:
    scene expression player.location.background_blur with dissolve
    "{i}*Ding Dong*{/i}"

    show anon f_thinking a_thinking with dissolve
    anon @ -m_talk "( Was that the doorbell? )"

    anon @ -m_talk "( Who could be here this early in the morning? )"

    anon f_grin @ -m_talk "( I'm the man of the house now, I should probably check it out. )"

    hide anon with dissolve
    return

label ano02_food_wakeup:
    scene expression player.location.background_blur
    show anon f_grin with dissolve:
        xoffset 300
    anon @ -m_talk "( Hmm, something smells really good! )"

    anon f_normal @ -m_talk "( {b}[deb_name]{/b} must be making breakfast downstairs. )"

    anon @ -m_talk "( I should go say good morning to her. )"

    hide anon with dissolve
    return

label ano04_init_wakeup:
    scene expression player.location.background_blur
    show anon with dissolve
    anon @ -m_talk "( I should really go and {b}meet up with that guy who rescued me{/b}. )"

    anon @ -m_talk "( He might be able to help us with these Russians, and even if he can't, he mentioned something about a job for me... )"

    pause
    anon f_worried @ -m_talk "( On the other hand, {b}[deb_name]{/b} seems really worried about this loan she took out with the bank. )"

    anon f_thinking a_thinking @ -m_talk "( My time might be better spent heading down to {b}Saga Financial{/b} and sorting things out. )"

    anon @ -m_talk "( I'm sure {b}one of Dad's old coworkers will help me{/b} and I might be able to learn more about what he got mixed up in. )"

    pause
    anon @ -m_talk "( Then again, it might be unwise to keep this {b}Tony{/b} guy waiting... )"

    anon f_normal a_idle @ -m_talk "( I should head there first. )"

    hide anon with dissolve

    $ player.go_to(L_pizzeria_exterior)
    scene expression player.location.background_blur with fade
    show anon with dissolve
    anon @ -m_talk "( Here it is. Tony's Pizza. Summerville's premier pizza establishment. )"

    hide anon with dissolve
    return


label ano04_init_wakeup.delay:
    scene expression player.location.background_blur
    show anon with dissolve
    anon @ -m_talk "( I should really go and {b}thank that guy who rescued me{/b} yesterday. )"

    anon f_thinking @ -m_talk "( The pizza place is closed on Sundays though... )"

    anon f_normal @ -m_talk "( I guess I'll go see him tomorrow instead. )"

    hide anon with dissolve
    return


label jos01_init_wakeup:
    scene expression L_home_bedroom.background
    "{i}*Brrrzzzt* *Brrrzzzt*{/i}"


    scene expression background(608, 512, 3.8, l=L_dealership_showroom) as underlay:
        xoffset -400
    show josephine a_phone_talk f_concerned:
        xoffset -500
    show xtra3 as counter at right:
        xoffset -400

    $ renpy.dynamic(stage=background(560, 320, 2.5, l=L_home_bedroom))
    show expression stage as stage
    show anon f_confused with dissolve:
        flip
    anon @ -m_talk "Hmm?"

    anon a_phone f_thinking_down "Saya tidak mengenali nomor ini..."

    show anon a_phone_talk f_skeptical with dissolve:
        unflip
        xoffset 500
    show expression stage as stage at phoneleft with phoneleft.show
    anon "Halo?"

    josephine "Halo?"

    pause
    anon "Who is thi-"

    josephine f_bored "Bowl cut, is that you?"

    anon f_surprised "{b}Yosephine{/b}?"

    anon f_worried "How did you get my number?"

    josephine "Umm, you wrote it on the paperwork for the cars you bought..."

    anon "Oh."

    anon f_normal "Benar."

    josephine @ f_eyeroll "Duh."

    show anon f_unimpressed
    pause
    anon f_normal "Apakah Anda memerlukan sesuatu?"


    josephine "I was kinda hoping you might wanna hang out... Or something?"

    anon f_skeptical "Hang out?"

    josephine f_sexy "Ya."

    josephine "You know, at the dealership?"

    pause
    josephine f_bored "Dude, I am so bored!"

    anon f_worried "Ehh, entahlah..."

    josephine f_concerned "C'mon, please!"

    anon "I have some stuff planned and-"

    pause
    josephine f_sexy "I'll suck your dick again!"

    anon f_surprised_teeth "!!!"
    anon f_flirt @ f_thinking "Well, I suppose I could swing by for a little bit..."

    josephine "Luar biasa!"

    josephine "I'll see you soon!"

    show josephine a_phone with dissolve
    show expression stage as stage with {'master': phoneleft.hide}
    "{i}*Bip*{/i}"

    anon f_worried "Halo?"

    pause
    anon "{b}Yosephine{/b}?"

    pause
    anon a_phone f_flirt_low "{i}*Sigh*{/i} Okay, I guess, I need to {b}visit the dealership{/b} again..."

    hide anon with dissolve
    return


label ano13_init_wakeup:
    scene expression player.location.background_blur
    show anon f_hurt a_rub with dissolve
    anon @ -m_talk "( Ugh, I feel like I've got monkeys in my head... )"

    pause
    anon @ -m_talk "( The only thing I have to show for last night's recon mission is a few bruises and a splitting headache. )"

    anon f_tired a_sides @ -m_talk "( {b}Tony{/b}'s gonna be pissed I went without him too. )"

    pause
    anon a_thinking f_thinking @ -m_talk "( Still, I'd best {b}go and fill him in{/b} on what I saw. )"

    anon @ -m_talk "( Maybe he'll have some ideas on how to proceed... )"

    hide anon with dissolve
    return


label ano21_init_wakeup:
    scene expression player.location.background_blur
    show anon f_thinking with dissolve
    anon @ -m_talk "( {b}Harold{/b} said he'd talk to me today about the Russians. )"

    show anon a_thinking with dissolve
    pause
    anon @ -m_talk "( I should swing by the {b}precinct{/b} and {b}speak with him{/b}. )"

    hide anon with dissolve
    return


label ano25_init_wakeup:
    scene expression player.location.background_blur
    show anon with dissolve
    anon @ -m_talk "( {b}Liu promised to meet me at Tony{/b}'s so we can come up with a plan to get that briefcase. )"

    anon @ f_grin -m_talk "( {b}She's probably waiting for me at the pizzeria{/b}... )"

    anon @ -m_talk "( ... I should head over there quickly. )"

    hide anon with dissolve
    return


label ano25_init_wakeup.wait:
    scene expression player.location.background_blur
    show anon with dissolve
    anon @ -m_talk "( {b}Liu promised to meet me at Tony{/b}'s so we can come up with a plan to get that briefcase. )"

    anon @ f_worried -m_talk "( The pizzeria isn't open on Sundays though... )"

    anon @ -m_talk "( ... So, I guess it'll have to wait until tomorrow. )"

    hide anon with dissolve
    return


label ano28_init_wakeup:
    scene intro_04
    show text _ ("Things quickly returned to normalcy following the events at the warehouse that night.") as caption
    with fade
    pause
    hide caption with dissolve
    show text _ ("The police took all the credit for the mobs downfall, of course, but in the grand scheme of things, I didn't really mind.") as caption with dissolve
    pause
    hide caption with dissolve
    show text _ ("I had seen justice done for my father and saved my friends from Raz and his Russian goons.") as caption with dissolve
    pause
    hide caption with dissolve
    show text _ ("There was still the not so small matter of [deb_name]'s debt to deal with, but at least the threat of violence was off the table.") as caption with dissolve
    pause

    scene location_home_bedroom_cutscene23
    with fade
    pause
    anon "If only I'd found that money you stole from the mob."

    pause
    anon "{i}*Sigh*{/i} Oh well."

    anon "At least I have a job now and can help {b}[deb_name]{/b} make payments..."

    pause
    anon "... Who knows?"

    anon "{b}[jen_name]{/b} might even step up and make some contributions."


    if M_jenny.finished_state(S_jenny_cheerleader_sex):
        anon "Now that she's raking in all that camshow money."

    else:
        anon "If she ever gets a job, that is."


    pause
    anon "But don't worry, {b}Dad{/b}..."

    anon "... We'll figure something out."

    pause
    anon "I'll take care of them from now on."

    anon "Saya berjanji."


    scene location_home_bedroom_cutscene22a
    with fade
    debbie "{b}[firstname]{/b}?!"


    scene location_home_bedroom_cutscene22b
    show location_home_bedroom_cutscene22a:
        crop (0, 0, 512, 768)
    with {'master': dissolve}
    anon "Hmm?"

    hide location_home_bedroom_cutscene22a
    show anon cutscene22b
    show debbie cutscene22b
    with {'master': dissolve}
    debbie "Are you still sleeping, sweetie?"

    anon "No, I'm awake."

    anon "What's up, {b}[deb_name]{/b}?"

    debbie "Breakfast is almost ready..."

    anon "Oh?"

    debbie "... You wanna come down?"

    anon "Y-ya, tentu saja."


    if M_debbie.finished_state(S_debbie_night_visit_three):
        debbie "Maybe afterwards we'll have a shower and I'll help you wash your back?"

        anon "Heh, I'd love that."

        debbie "Well, get your cute butt downstairs then!"

    else:

        debbie "Well, you better hurry then if you don't want it getting cold."


    anon "Saya akan segera ke sana."

    show location_home_bedroom_cutscene22a:
        crop (0, 0, 512, 768)
    with dissolve
    pause

    scene expression player.location.background_blur with fade
    show anon a_thinking f_thinking with {'master': dissolve}:
        xoffset -250
        xzoom -1
    anon @ -m_talk "{i}*Mengendus*{/i}"

    show anon a_sides f_grin with {'master': dissolve}
    anon @ -m_talk "( Mmm, I can smell it already! )"

    anon @ -m_talk "( I'd better hurry down. )"

    hide anon with dissolve
    return


label nad01_init_wakeup:
    scene location_home_bedroom_cutscene13 with fade
    pause

    scene location_home_bedroom_cutscene14b
    debbie "AHH!!!" with hpunch

    scene expression background(560, 320, 2.5) as stage
    show anon b_dressed_changing2:
        xoffset -250
        xzoom -1
    with fastfade
    anon "{b}[deb_name]{/b}?!"

    show anon b_dressed_changing with {'master': dissolve}
    debbie "OH MY GOD, GET AWAY FROM ME!"

    show anon a_surprised b_dressed f_shock with {'master': dissolve}
    anon @ -m_talk "( What the heck is going on down there?! )"

    hide anon with fastdissolve
    return


label jen0m_init_wakeup:
    scene location_home_bedroom_visit_jenny_preg
    show anon b_visit_morning_relax f_sleep
    with fade
    pause
    show location_home_bedroom_visit_door_01 as door behind anon
    show jenny b_door_dressed_pregnant_belly behind anon
    with {'master': dissolve}
    pause
    show location_home_bedroom_visit_door_02 as door
    show jenny b_door_open_dressed_pregnant_belly
    with {'master': dissolve}
    jenny "Hey, it's time to get up."

    pause
    jenny f_annoyed "{b}[firstname]{/b}?"

    pause
    show jenny b_dressed_pregnant_belly f_upset:
        xzoom -1
        yoffset 50
        zoom .78
    with {'master': dissolve}
    pause
    show jenny a_upset
    jenny "Hey!!!" with hpunch
    show anon b_visit_morning_sit f_tired
    with {'master': dissolve}
    anon @ -m_talk "Hmm?!"

    show jenny a_crossed
    with {'master': dissolve}
    jenny "Get up."

    anon "Ugh, {b}[jen_name]{/b}?"

    anon "W-what time is it?"

    jenny f_confused "Entahlah..."

    jenny "... Early?"

    show jenny f_upset
    anon f_unimpressed "Yeah, too early."

    show anon b_visit_morning_relax f_sleep
    show jenny a_upset f_angry
    with {'master': dissolve}
    pause
    jenny "I mean it, {b}[firstname]{/b}, get out of the bed!"

    anon "{i}*Sigh*{/i} Or, you could come get in the bed with me and we'll both get a few more hours sleep?"

    show jenny a_sides f_eyeroll
    with {'master': dissolve}
    jenny "Ugh, in your dreams..."

    show jenny f_upset
    with {'master': dissolve}
    pause
    show jenny a_touch f_concerned_low
    with {'master': dissolve}
    jenny "... Besides, I couldn't even if I wanted to."

    show anon b_visit_morning_sit f_unimpressed
    with {'master': dissolve}
    pause
    anon f_tired "Apa maksudmu?"

    jenny "My back hurts too fucking much and your satanic little spawn is just resting right on top of my bladder!"

    anon f_flirt "Well, come lay down and I'll massage your back."

    show jenny f_upset
    anon "Maybe it'll help?"

    show anon f_surprised_teeth
    show jenny a_upset f_angry
    jenny "I don't want a massage, {b}[firstname]{/b}!" with hpunch
    jenny "I want you to get your stupid ass out of bed and come eat breakfast."

    show jenny a_sides f_upset
    with {'master': dissolve}
    anon f_confused "What, why?"

    jenny f_normal "Because you and I are doing a show this afternoon."

    anon f_surprised @ -m_talk "Hah?!"

    jenny f_sexy @ -m_talk "..."
    anon "You can't be serious!"

    jenny "Oh, I'm very serious."

    anon f_confused "You wanna have sex... on camera..."

    anon f_surprised "... While you're pregnant?"

    jenny f_upset @ f_eyeroll "Duh."

    anon f_worried "Tapi-"

    jenny f_normal "I looked up some pregnancy shows online last night..."

    show jenny a_touch f_grin_down
    with {'master': dissolve}
    jenny "... And it turns out, those horny losers pay out the nose for it!"

    anon "Y-ya, tapi-"

    jenny f_happy "This one bitch made almost five thousand dollars in thirty minutes... I counted."

    show anon f_surprised
    jenny "And she was just teasing with some light masturbation!"

    jenny f_sexy "Imagine the killing we'll make with full on sex!"

    anon f_worried @ f_worried_surprised "I'm not sure I want to stream while you're pregnant with my baby, {b}[jen_name]{/b}..."


    if M_jenny.get('dominance') <= 0:
        show jenny a_sides f_upset
        with {'master': dissolve}
        jenny "I don't recall asking what you want!"

        anon f_surprised "Hah?!"

        jenny "This is a golden opportunity and you're not pussing out on me now!"

        anon f_worried_surprised @ -m_talk "..."
        jenny "We're having sex on camera for money this afternoon and you're gonna like it!"

        anon "But {b}[jen_name]{/b}... don't you think it's a bad idea to involve-"

        show anon f_shy_cringe
        show jenny a_upset f_angry
        jenny "End of story!!" with hpunch
        show anon f_surprised_teeth
        show jenny b_door_open_dressed_pregnant_belly f_yell:
            reset
            xzoom 1
        with {'master': dissolve}
        jenny "Now get your ass up and downstairs!"

        jenny "You're doing all the heavy lifting for the show today."

        show anon f_disgusted_wince
        hide door
        hide jenny
        "{i}*Slam*{/i}" with hpunch
        show anon f_frown_down
        with {'master': dissolve}
        pause
        anon "{i}*Huh*{/i}"

        anon @ -m_talk "( I don't understand how someone can be that big a bitch and still be so hot... )"

        anon @ -m_talk "( ... It's not fair. )"

    else:

        show jenny a_sides f_confused
        with {'master': dissolve}
        jenny "Hah?"

        jenny "You mean you don't wanna have sex with me?!"

        anon f_confused "No, that's not it..."

        show jenny f_upset
        anon "... I just don't wanna stream it online."

        show jenny a_touch f_concerned_low
        with {'master': dissolve}
        jenny "Why, because I look like a big fat whale?!"

        anon f_surprised "Apa-"

        anon f_worried_surprised "No!!"

        show jenny a_cry f_happy_closed
        with {'master': dissolve}
        jenny "Yes I do!!"

        jenny "I knew this stupid baby was gonna ruin my perfect body..."

        jenny "... And now here we are..."

        show anon f_shock
        jenny "... I'm hideous!"

        anon f_worried "{b}[jen_name]{/b}, you're not hideous..."

        anon f_shy "... If anything, you're even more sexy because it's my child in there."

        anon "I just don't think we should-"

        show anon f_worried_surprised
        jenny "LIAR!!"

        show anon f_frown_down
        with {'master': dissolve}
        pause
        show jenny f_happy
        anon @ -m_talk "..."
        pause
        show jenny f_happy_closed
        anon f_shy "Alright, I'll do it... just-"

        anon "... Please, don't cry."

        show jenny a_touch f_concerned
        with {'master': dissolve}
        jenny "Anda akan melakukannya?"

        anon "Ya."

        jenny f_sexy "Bagus."

        show anon f_surprised
        jenny f_normal "Then get your ass downstairs and eat something because you're doing most of the work once we start."

        anon f_skeptical "Tunggu sebentar..."

        show jenny b_door_open_dressed_pregnant_belly:
            reset
            xzoom 1
        with {'master': dissolve}
        anon "... Were you fake crying just now?!"

        jenny f_smirk "Maaaaaaaybe."

        anon f_annoyed "{b}[jen_name]{/b}, what the hell..."

        hide door
        hide jenny
        with {'master': fastdissolve}
        jenny "Ha ha ha!"

        pause
        show anon f_frown_down
        with {'master': dissolve}
        pause
        anon "{i}*Huh*{/i}"

        anon @ -m_talk "( That was a dirty trick... )"

        anon @ -m_talk "( ... And I fell for it, hook, line, and sinker. )"


    anon f_sad @ -m_talk "( Well, there's no way I'm getting back to sleep now. )"


    scene expression background(560, 320, 2.5) as stage
    show anon b_underwear_yawn:
        xoffset -250
        xzoom -1
    with fade
    anon "{i}*Menguap*{/i}"

    show anon b_underwear f_worried_down
    with dissolve
    pause
    show anon b_dressed_changing2
    with dissolve
    pause
    show anon a_towel b_shorts
    with dissolve
    pause
    show anon b_dressed_changing
    with dissolve
    pause
    show anon a_sides b_dressed
    with {'master': dissolve}
    anon f_tired @ -m_talk "( {b}[jen_name] should be waiting for me at the breakfast table{/b}. )"

    anon f_tired_happy @ -m_talk "( Hopefully, {b}[deb_name]{/b} made something good. )"

    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
