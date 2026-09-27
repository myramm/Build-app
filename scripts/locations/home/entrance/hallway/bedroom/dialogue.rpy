label bedroom_eve_clients_hangover_wakeup:
    scene expression player.location.background_blur
    show anon f_tired with dissolve
    anon @ -m_talk "( Eugh, why did I drink so much last night? )"

    anon a_rub @ -m_talk "( My head is killing me... )"

    pause
    anon a_idle @ -m_talk "( Hmm, I wonder how {b}Eve{/b} is doing? )"

    anon @ -m_talk "( I should {b}swing by her house and check on her{/b}. )"

    hide anon with dissolve
    return

label bedroom_jenny_pregnant_and_peeing:
    scene expression player.location.background_blur
    show anon f_worried with dissolve
    anon "Wow, do I ever have to pee!"

    hide anon with dissolve
    anon "Oh, man! Oh, man!"


    scene black with dissolve
    pause .5

    scene expression L_home_shower.background_blur
    show jenny b_towel a_pregnant_touch f_gross:
        flip
        xoffset 500
    with dissolve
    pause
    jenny "{i}*Sigh*{/i} Pregnancy fucking blows..."

    show anon f_worried with dissolve
    pause
    show anon f_surprised_low a_surprised_up_both with dissolve
    anon "!!!"
    hide jenny
    show jenny b_towel a_pregnant_touch f_gross
    show anon f_worried a_rub
    with dissolve
    anon "Eh, h-hi {b}[jen_name]{/b}..."

    anon "Bagaimana perasaanmu?"

    show anon f_surprised_teeth
    show jenny f_angry
    jenny "Pregnant!"

    jenny "Apa yang kamu inginkan?"

    anon f_worried "Umm, I just-"

    jenny "... And you had better not say sex because I'm telling you right now, I will sit on your tiny little head and squash it like a fucking cantaloupe!"

    anon "N-no, I really need-"

    jenny "Just look at what you did to me!"

    jenny "I swear, I'm never having sex again after this shit!"

    show anon a_idle with dissolve
    anon "{b}[jen_name]{/b}, please-"

    show anon f_surprised_teeth_down
    show jenny f_gross
    jenny "No, don't bother begging... It's not going to work!"

    jenny "How am I supposed to feel sexy, looking like an over inflated birthday balloon?!"

    anon f_shock "{b}[jen_name]{/b}, stop talking!!!"

    show anon f_surprised_teeth
    show jenny f_surprised
    pause
    show jenny f_gross
    jenny "What is your problem?!"

    show anon f_shock a_surprised_up_both with dissolve
    anon "I need to pee!!!"

    show anon f_surprised_teeth_down a_surprised
    show jenny f_surprised
    jenny "O-oh..."

    show jenny f_angry
    show anon f_surprised_teeth
    jenny "Well, why didn't you just say so?!"

    show jenny f_eyeroll
    jenny "Astaga."

    show jenny f_gross
    jenny "Move it!"

    hide jenny with dissolve
    pause
    anon f_worried @ -m_talk "( Man, I thought her mood was bad before pregnancy... )"

    show anon f_grin a_thinking with dissolve
    anon @ -m_talk "( I hope the kid doesn't come out with horns! )"

    hide anon with dissolve
    return

label bedroom_jenny_weird_relationship:
    scene expression player.location.background_blur
    show anon f_worried
    anon @ -m_talk "( Hmm, I just don't understand {b}[jen_name]{/b}... )"

    anon @ -m_talk "( Why is she so weird about our relationship? )"

    show anon f_thinking a_thinking with dissolve
    pause
    show anon f_worried a_idle with dissolve
    anon @ -m_talk "( I should {b}talk to her about it{/b}... )"

    anon @ -m_talk "( {b}She's usually downstairs eating breakfast{/b} in the morning. )"

    hide anon with dissolve
    return

label bedroom_jenny_bedroom_intrusion_1:
    scene expression "backgrounds/location_home_bedroom_cutscene13.jpg" with fade
    pause
    scene expression "backgrounds/location_home_bedroom_cutscene13b.jpg" with dissolve
    pause
    jenny "Psst, {b}[firstname]{/b}..."

    scene expression "backgrounds/location_home_bedroom_cutscene15.jpg"
    player_name "!!!"
    player_name "Watsa-"

    player_name "Sial, {b}[jen_name]{/b}..."

    scene expression "backgrounds/location_home_bedroom_cutscene15b.jpg"
    jenny "Hehehehe!"

    scene expression "backgrounds/location_home_bedroom_cutscene15.jpg"
    player_name "{i}*Sigh*{/i} You really gotta stop doing this."

    scene expression "backgrounds/location_home_bedroom_cutscene15b.jpg"
    jenny "Aww, poor baby..."

    jenny "Hurry up, {b}breakfast is ready{/b}."

    scene expression "backgrounds/location_home_bedroom_cutscene15.jpg"
    player_name "Jadi?"

    scene expression "backgrounds/location_home_bedroom_cutscene15b.jpg"
    jenny "So trust me, you're going to need your strength today."

    scene expression "backgrounds/location_home_bedroom_cutscene15.jpg"
    player_name "Maksudnya itu apa?"

    scene expression "backgrounds/location_home_bedroom_cutscene15b.jpg"
    jenny "It means, get up, loser!"

    scene expression "backgrounds/location_home_bedroom_cutscene15.jpg"
    player_name "..."
    scene expression "backgrounds/location_home_bedroom_cutscene15b.jpg"
    jenny "C'mon, {b}get your ass downstairs{/b}!"

    scene expression "backgrounds/location_home_bedroom_cutscene16.jpg" with dissolve
    player_name "Ugh!"

    return

label bedroom_jenny_bedroom_intrusion_2:
    scene expression player.location.background_blur with fade
    show anon f_worried with dissolve
    anon "I guess I should {b}get downstairs and see what she's going on about{/b}..."

    hide anon with dissolve
    return

label bedroom_jenny_give_cunni:
    if store._in_replay is not None:
        $ player.location = L_home_bedroom
        scene expression "backgrounds/location_home_bedroom_telescope_window.jpg" with None
        $ game.timer.tick(0)
        show jenny b_telescope_rub
        show anon b_telescope_laying_back f_worried
        pause
    anon "So what, you're just going to start masturbating, right here in my room?"

    show jenny f_telescope_normal b_telescope_rub_look with dissolve
    jenny "Hehe, why not?"

    show jenny b_telescope_rub with dissolve
    jenny "It's nothing you haven't seen before..."

    anon "Y-ya, tapi-"

    pause
    show jenny b_telescope a_down with dissolve
    jenny "Actually, you're right."

    jenny "Why masturbate when I could just as easily have you snack on my box?"

    anon "Hah?!"

    show jenny b_telescope_undress with dissolve
    pause
    show anon f_surprised
    show jenny b_telescope_standing_panties f_grin with dissolve
    if M_mrsj.finished_state(S_mrsj_cupid_report):
        jenny "She's putting on a show for you and you're going to return the favor."

    else:
        jenny "I want what she's getting and you're going to give it to me."

    if M_jenny.get("dominance") <= 0:
        anon f_worried "Saya?"

        jenny "Ya."

        jenny "Ayolah, pecundang!"

        jenny "Aku akan mengotori wajah bodohmu itu!"

    else:
        anon "Ah, benarkah?"

        jenny "Ya."

        anon "Mungkin jika Anda bertanya kepada saya dengan baik."

        show jenny f_gross_down
        jenny "Ugh, kamu masih terpaku pada omong kosong itu?!"

        show anon f_skeptical
        if randomizer() > 50:
            anon "Jika Anda ingin kembali melakukan masturbasi, sesuaikan diri Anda..."

        else:
            anon "Aku bukan bocah pencambukmu, {b}[jen_name]{/b}..."

        jenny "Grr, kamu sungguh menyebalkan!"

        jenny "Bagus."

        show jenny f_angry_pouting
        pause
        show jenny f_eyeroll
        jenny "{b}[firstname]{/b}, maukah kamu menjilat vaginaku?"

        show jenny f_gross_down
        anon @ f_laugh "Haha, tentu saja!"

        pause
        jenny "Ayolah!"

    jump jenny_cunni_repeat

label bedroom_jenny_perv_on_tammy_notice:
    scene expression player.location.background_blur
    show anon f_grin with dissolve
    anon @ -m_talk "( Hmm, I wonder if {b}Mrs. Johnson{/b} is doing her morning yoga routine? )"

    anon @ -m_talk "( I can usually see her through my {b}telescope{/b}. )"

    hide anon with dissolve
    return

label bedroom_jenny_morning_visit:
    scene expression "backgrounds/location_home_bedroom_cutscene13.jpg" with fade
    pause
    scene expression "backgrounds/location_home_bedroom_cutscene14.jpg" with hpunch
    jenny "Hey, wake up loser!"

    scene expression "backgrounds/location_home_bedroom_cutscene15.jpg" with dissolve
    player_name "Hmm?"

    player_name "C'mon {b}[jen_name]{/b}, not this again..."

    scene expression "backgrounds/location_home_bedroom_cutscene15b.jpg"
    jenny "What are you doing today?!"

    scene expression "backgrounds/location_home_bedroom_cutscene15.jpg"
    player_name "I dunno... Sleeping?"

    scene expression "backgrounds/location_home_bedroom_cutscene15b.jpg"
    jenny "Ya benar."

    jenny "{b}Come to my room this afternoon{/b}."

    jenny "My fans want another show."

    scene expression "backgrounds/location_home_bedroom_cutscene15.jpg"
    player_name "Ugh, fine... Just go away!"

    scene expression "backgrounds/location_home_bedroom_cutscene15b.jpg"
    jenny "Don't be snippy, asshole!"

    scene expression "backgrounds/location_home_bedroom_cutscene16.jpg" with dissolve
    pause
    scene expression "backgrounds/location_home_bedroom_cutscene15b.jpg" with dissolve
    jenny "{b}My room, this afternoon{/b}!"

    scene expression "backgrounds/location_home_bedroom_cutscene15.jpg"
    player_name "I said, okay!"

    player_name "Astaga."

    scene expression "backgrounds/location_home_bedroom_cutscene15b.jpg"
    jenny "Hahahaah!"

    scene expression player.location.background_blur with None
    show player 7 at left
    with dissolve
    pause
    show player 101 with dissolve
    player_name "( I guess I'd better {b}swing by [jen_name]'s room this afternoon{/b}. )"

    pause
    player_name "( I wonder what she has planned this time? )"

    hide player with dissolve
    return

label bedroom_jenny_pissed_at_handjob:
    scene expression player.location.background_blur
    show anon f_thinking a_thinking with dissolve
    anon @ -m_talk "( Hmm, I wonder if {b}[jen_name]{/b} is still pissed at me? )"

    anon @ -m_talk "( She's probably {b}downstairs eating breakfast{/b} right now. )"

    anon @ -m_talk "( Maybe I should go and {b}talk to her{/b}? )"

    hide anon with dissolve
    return

label bedroom_jenny_spy_on_mia_telescope:
    scene expression player.location.background_blur
    show anon f_flirt with dissolve
    anon "Hmm, I wonder what {b}Mia{/b} is doing this morning?"

    anon "I can usually see her through {b}my telescope{/b}."

    hide anon with dissolve
    return

label bedroom_jenny_buy_bad_monster:
    scene expression player.location.background_blur
    show anon f_thinking a_thinking with dissolve
    anon @ -m_talk "( Hmm, if I get {b}[jen_name]{/b} a new toy, I bet she'll save a new video to her {b}CAMslut{/b} page. )"

    anon @ -m_talk "( Didn't she mention one named {b}Bad Monster{/b} in her {b}diary{/b}? )"

    show anon f_tired_happy with dissolve
    if player.has_item('badmonster'):
        anon @ -m_talk "( I should see if she wants the one I got from {b}Pink{/b}! )"

    else:
        anon @ -m_talk "( I should {b}go to Pink and get one for her{/b}! )"

    hide anon with dissolve
    return

label bedroom_jenny_checked_for_new_video:
    scene expression player.location.background_blur with None
    show anon f_thinking a_thinking with dissolve
    anon @ -m_talk "( Hmm, maybe there's a limit to how many she can save? )"

    anon @ -m_talk "( That would make sense, the saved ones are mostly promotional after all... )"

    anon @ -m_talk "( Just another way to draw in more subscribers. )"

    pause
    show anon f_grin a_idle with dissolve
    anon @ -m_talk "( I bet if I {b}bought her a new toy{/b} she'd make a new video! )"

    anon @ -m_talk "( Didn't she mention one named {b}Bad Monster{/b} in her {b}diary{/b}? )"

    if player.has_item('badmonster'):
        anon f_flirt @ -m_talk "( I should see if she wants the one I got from {b}Pink{/b}! )"

    else:
        anon @ -m_talk "( I should {b}go to Pink and get one for her{/b}! )"

    hide anon with dissolve
    return

label bedroom_jenny_new_video_notice:
    scene expression player.location.background_blur
    show anon f_flirt with dissolve
    anon @ -m_talk "( I haven't checked {b}[jen_name]{/b}'s CAMslut profile in a while... )"

    anon @ -m_talk "( I wonder if she's saved any {b}new videos{/b}? )"

    hide anon with dissolve
    return

label bedroom_jenny_hack_computer_notice:
    scene expression player.location.background_blur with None
    show anon f_tired_happy with dissolve
    anon @ -m_talk "( Hmm, this might be a good time to check on {b}[jen_name]{/b}. )"

    anon @ -m_talk "( If she's asleep, I should be able to {b}log into her laptop and snoop around{/b}. )"

    hide anon with dissolve
    return

label bedroom_jenny_snoopin_laptop_notice:
    scene expression player.location.background_blur
    show anon a_thinking f_thinking with dissolve
    anon @ -m_talk "( Hmm, there has to be some way I can figure out what {b}[jen_name]{/b} is doing for that money? )"

    pause
    show anon a_idle f_normal with dissolve
    anon @ -m_talk "( She might have written something down in that {b}diary of hers{/b}... )"

    anon @ -m_talk "( I just have to {b}wait until she's showering{/b} and then I can {b}sneak into her room{/b} again and check it. )"

    hide anon with dissolve
    return

label bedroom_jenny_get_a_toy:
    scene expression "backgrounds/location_home_bedroom_cutscene13.jpg" with fade
    jenny "{b}[firstname]{/b}!"

    anon "{i}*ZZzz*{/i}..."

    scene expression "backgrounds/location_home_bedroom_cutscene14.jpg"
    jenny "HEY DOOFUS!" with hpunch
    anon "!!!"
    scene expression "backgrounds/location_home_bedroom_cutscene15.jpg" with dissolve
    anon "Apa yang-"

    anon "What's your problem?!"

    scene expression "backgrounds/location_home_bedroom_cutscene15b.jpg"
    jenny "I need you for something."

    scene expression "backgrounds/location_home_bedroom_cutscene15.jpg"
    anon "Can't it wait?!"

    anon "I'm trying to sleep!"

    scene expression "backgrounds/location_home_bedroom_cutscene15b.jpg"
    jenny "No, it can't wait."

    jenny "Hurry up, loser!"

    scene expression "backgrounds/location_home_bedroom_cutscene13.jpg" with dissolve
    anon "( Ugh, I'm so tired... )"

    scene expression "backgrounds/location_home_bedroom_cutscene14.jpg" with fastdissolve
    jenny "Don't go back to sleep either!"

    jenny "Get up, put some pants on, and get your lazy ass in gear!"

    scene expression "backgrounds/location_home_bedroom_cutscene15.jpg" with dissolve
    anon "Yeah, yeah... I'm coming."

    anon "Astaga."

    scene expression "backgrounds/location_home_bedroom_cutscene16.jpg" with dissolve
    anon "{i}*Menguap*{/i}"

    anon "This had better be worth it..."

    return

label bedroom_jenny_pics_afterthought:
    scene expression player.location.background_blur
    show anon f_grin with dissolve
    anon @ -m_talk "( Man, those pictures of {b}[jen_name]{/b} were so hot! )"

    anon @ -m_talk "( I wish I could get another look at them... )"

    pause
    show anon a_thinking f_thinking with dissolve
    anon @ -m_talk "( Hmm, you know what? )"

    anon @ -m_talk "( {b}I think she leaves her bedroom door unlocked while she's showering{/b}. )"

    show anon f_tired_happy with dissolve
    anon @ -m_talk "( I could {b}sneak in and find her camera{/b}, if I'm quick. )"

    show anon f_normal
    pause
    anon @ -m_talk "( I just need to {b}wait until she's in the shower{/b}. )"

    hide anon with dissolve
    return

label bedroom_jenny_breakfast_notice:
    scene expression player.location.background_blur
    show anon with dissolve
    anon "Wow, something smells delicious!"

    anon "{b}[deb_name]{/b} must be cooking breakfast downstairs."

    anon "{b}I should go check it out{/b}!"

    hide anon with dissolve
    return

label bedroom_diane_breeding_candidate:
    scene expression player.location.background_blur
    show player 14 with dissolve
    player_name "Last night was crazy!"

    player_name "I wonder if {b}Diane{/b} has already left?"

    player_name "I should {b}check for her downstairs, she's usually in the kitchen with [deb_name]{/b}."

    hide player with dissolve
    return


label bedroom_diane_barn_news:
    scene expression player.location.background_blur
    show player 34 with dissolve
    diane "Dance with me!!"

    debbie "{b}Diane{/b}!"

    pause
    show player 35
    player_name "What the heck is going on down there?"

    show player 34
    debbie "Ha ha ha!"

    show player 12
    player_name "I should {b}go check it out{/b}."

    hide player with dissolve
    return

label bedroom_diane_debbie_dinner:
    scene expression player.location.background_blur
    show player 5 with dissolve
    debbie "{b}[firstname]{/b}?!"

    debbie "Are you still sleeping?!"

    player_name "Hmm?"

    show player 10
    player_name "Sounds like {b}[deb_name]{/b} needs me..."

    show player 9 at Position (xoffset=40) with dissolve
    pause
    show player 10 with dissolve
    player_name "I should go see what she wants."

    hide player with dissolve
    return

label bedroom_diane_get_augmentation:
    scene expression player.location.background_blur
    show player 5f with dissolve
    "{i}*Ketuk* *Ketuk*{/i}"

    show player 10f
    player_name "Hah?"

    show player 5f
    debbie "{b}[firstname]{/b}?"

    debbie "May I speak with you for a second?"

    show player 14f
    player_name "Yeah, come on in, {b}[deb_name]{/b}."

    show player 13f at right with dissolve
    pause
    show old_debbie 1f at left with dissolve
    show player 14f
    player_name "Selamat pagi."

    show player 13f
    show old_debbie 2f
    debbie "Good morning, sweetie."

    show old_debbie 1f
    show player 14f
    player_name "Ada apa?"

    show player 13f
    show old_debbie 2f
    debbie "Well, I just got off the phone with {b}Diane{/b}."

    show old_debbie 1f
    show player 11f
    player_name "!!!"
    show player 10f
    player_name "{i}*Gulp*{/i} What did she have to say?"

    show player 5f
    show old_debbie 3f
    debbie "Oh, she just couldn't stop raving about how great you're doing with her garden!"

    show old_debbie 1f
    show player 10f
    player_name "Benar-benar?"

    show player 5f
    show old_debbie 2f
    debbie "Yeah, and apparently you've been helping her out with a new business venture too?"

    show old_debbie 1f
    show player 17f
    player_name "Heh, yeah. A little bit."

    show player 13f
    show old_debbie 2f
    debbie "I didn't even know she had started a new business..."

    show old_debbie 1f
    player_name "..."
    show player 10f
    player_name "Did she say anything else?"

    show player 5f
    show old_debbie 2f
    debbie "Hmm."

    debbie "Oh, uhh..."

    debbie "She wanted me to tell you, not to worry about your little incident..."

    show old_debbie 1f
    show player 11f
    player_name "!!!"
    show old_debbie 13f
    debbie "Did something happen?"

    show old_debbie 14bf
    show player 24f
    player_name "... Yeah, kinda."

    player_name "..."
    show old_debbie 13f
    debbie "Well, don't leave me in suspense!"

    show old_debbie 14bf
    show player 25f
    player_name "Uhh, I'd rather not talk about it... If that's alright?"

    show player 24f
    show old_debbie 13f
    debbie "Of course it's alright, sweetie."

    debbie "We don't have to."

    show old_debbie 14bf
    show player 5f
    player_name "..."
    show old_debbie 2f
    debbie "Anyways, she apparently got another big client for her business, and she could really use your help."

    debbie "I think she's going to offer you a raise."

    show old_debbie 1f
    show player 12f
    player_name "A raise?"

    show player 5f
    show old_debbie 3f
    debbie "Hehe, ya!"

    hide player
    show old_debbie 4bf at right
    with dissolve
    debbie "Oh, you're just growing up so fast!"

    debbie "I'm so proud of you, sweetie!"

    show old_debbie 5f
    player_name "T-terima kasih, {b}[deb_name]{/b}."

    show old_debbie 2f at left
    show player 13f at right
    with dissolve
    debbie "You'd better get over there!"

    show old_debbie 1f
    show player 14f
    player_name "Yeah, I guess I'd better."

    hide player
    hide old_debbie
    with dissolve
    return

label bedroom_mc_start_just_wokeup:
    scene expression game.timer.image("bedroom{}") with fade
    show anon b_underwear_yawn with dissolve:
        xoffset 250
    anon "{i}*Menguap*{/i}"

    show anon b_dressed_changing with dissolve
    anon "Ugh... I hate getting up early."

    anon b_dressed a_phone f_worried_low @ -m_talk "( No text messages from {b}Erik{/b}. Maybe he's still sleeping. )"

    anon f_grin a_idle @ -m_talk "( I'll stop by his house on the way to school. )"

    hide anon with dissolve
    return

label bedroom_mc_weekday_just_wokeup:
    scene expression game.timer.image("bedroom{}") with fade
    show player 7 with dissolve
    player_name "{i}*Menguap*{/i}"

    show player 8 with dissolve
    window hide
    pause
    show player 9 with dissolve
    player_name "( I should get ready for school... )"

    hide player with dissolve
    return

label bedroom_mc_weekend_just_wokeup:
    scene expression game.timer.image("bedroom{}") with fade
    show player 7 with dissolve
    player_name "{i}*Menguap*{/i}"

    show player 8 with dissolve
    window hide
    pause
    show player 9 with dissolve
    player_name "( What should I do this weekend... )"

    hide player with dissolve
    return

label bedroom_erik_bullying:
    scene black with dissolve
    debbie "Sayang?"

    pause
    debbie "Wake up, sweetie."

    scene expression game.timer.image("bedroom{}") with dissolve
    show old_debbie 14f at left
    show player 101bf at right
    with dissolve
    player_name "Huh? {b}[deb_name]{/b}? What time is it?"

    show player 100bf
    show old_debbie 13f
    debbie "{b}Mrs. Johnson{/b} is at the door asking to see you."

    show old_debbie 14f
    show player 101bf
    player_name "{b}Mrs. Johnson{/b}? For me?"

    show player 100bf
    show old_debbie 13f
    debbie "She hasn't said much, but she wants to talk with you before you head out for the day."

    show old_debbie 14f
    show player 101bf
    player_name "Oh. Okay. Let me get dressed and I'll be down soon."

    show player 100bf
    show old_debbie 13f
    debbie "Baiklah..."

    show old_debbie 14f
    pause
    show old_debbie 13f
    debbie "Is there anything I need to know about, {b}[firstname]{/b}?"

    show old_debbie 14f
    player_name "..."
    show player 101bf
    player_name "I have no idea why she's here either, {b}[deb_name]{/b}."

    show player 100bf
    debbie "..."
    show old_debbie 13f
    debbie "Ok, sweetie."

    hide old_debbie
    hide player
    with dissolve
    return

label bedroom_mia_tattoo_idea:
    scene expression game.timer.image("bedroom{}")
    show anon f_thinking with dissolve
    anon @ -m_talk "( I have to make something nice for {b}Mia{/b}'s tattoo idea. )"

    anon @ -m_talk "Hmm..."

    anon @ -m_talk "( Perhaps, I can {b}use one of the easels in art class{/b}! )"

    anon @ -m_talk "( I can use it to come up with a nice design for her. )"

    if game.timer.is_night():
        show anon b_dressed_changing3 with dissolve
        pause .4
        show anon a_towel b_shorts f_shy_down with dissolve
        pause .2
        show anon b_dressed_changing2 with dissolve
        pause .4
        anon b_underwear_yawn "{i}*Menguap*{/i}"

        anon a_idle b_underwear f_tired @ -m_talk "I should sleep."

    else:
        anon f_grin @ -m_talk "( Now that feels like a plan, bedroom brain-power at work! )"

    hide anon with dissolve
    call popup ('feature', 'easel')
    return

label bedroom_mia_strip_aftermath_grounded:
    scene expression game.timer.image("bedroom{}")
    show player 24 with dissolve
    player_name "( I can't believe I won't be able to see {b}Mia{/b} anymore. )"

    show player 25
    player_name "( Her parents don't trust me. )"

    show player 35
    player_name "( Perhaps I can make it up to them somehow... )"

    hide player with dissolve
    return

label bedroom_mia_concerning_visit:
    scene expression game.timer.image("bedroom{}")
    show player 4 with dissolve
    pause
    show player 30 at Position (xoffset=-6) with dissolve
    player_name "( I wonder how {b}Mia{/b} is doing. )"

    show player 12 at Position (xoffset=-6)
    player_name "( It's been a few days, and I haven't heard anything from her... )"

    player_name "( ... Perhaps I should visit her and see how she's doing... )"

    hide player with dissolve
    return

label bedroom_mia_urgent_message:
    scene expression game.timer.image("bedroom{}")
    show player 12 with dissolve
    player_name "Hah?"

    show player 9 at Position (xoffset=40) with dissolve
    pause
    show player 14 with dissolve
    player_name "( Looks like I got a text message... )"

    hide player with dissolve
    return

label bedroom_mia_angelicas_impatience:
    scene expression player.location.background_blur
    show player 55f at Position (xoffset=-12) with dissolve
    player_name "{i}*Menguap*{/i}"

    show player 56f with dissolve
    player_name "( I should get ready for- )"

    show player 11f
    "{i}*Ketuk* *Ketuk*{/i}"

    show old_debbie 2f at left
    show player 13f
    with dissolve
    debbie "Hun?"

    debbie "There's someone downstairs who's here for you."

    show old_debbie 1f
    show player 30f
    player_name "{b}Erik{/b}?"

    show player 11f
    show old_debbie 2f
    debbie "No, sweetie. It's a lady!"

    debbie "She says you two have spoken before..."

    show old_debbie 1f
    show player 10f
    player_name "Apa?"

    player_name "But who-"

    show player 5f
    show old_debbie 2f
    debbie "She's waiting downstairs. Why don't you {b}get dressed and come down{/b}."

    hide old_debbie with dissolve
    show player 12f
    player_name "A lady?!"

    show player 4f at Position (xoffset=-6) with dissolve
    player_name "Hah..."

    hide player with dissolve
    return

label bedroom_mia_angelicas_home_visit:
    scene expression player.location.background_blur
    show player 13f at right
    show old_debbie 2f at left
    debbie "Sayang?"

    show old_debbie 1f
    show player 17f
    player_name "Good morning, {b}[deb_name]{/b}."

    show player 13f
    show old_debbie 2f
    debbie "Pagi."

    debbie "That nice lady from the other day is downstairs again."

    show old_debbie 1f
    show player 11f
    player_name "..."
    show player 12f
    player_name "Siapa?"

    show player 5f
    show old_debbie 3f
    debbie "Come on now, sleepyhead. The nun is here again."

    show old_debbie 1f
    show player 22f
    player_name "!!!"
    debbie "Hurry up so you can meet her downstairs."

    hide old_debbie with dissolve
    show player 10f
    player_name "What is she going to want now?"

    hide player with dissolve
    return

label bedroom_mia_angelicas_final_home_visit:
    scene expression player.location.background_blur
    show player 55f at Position (xoffset=-12) with dissolve
    player_name "{i}*Menguap*{/i}"

    show player 56f with dissolve
    player_name "I should get ready for-"

    show player 11f
    "{i}*Ketuk* *Ketuk*{/i}"

    show old_debbie 2f at left
    show player 13f
    with dissolve
    debbie "Hun?"

    debbie "That nun is here again..."

    show old_debbie 1f
    show player 30f
    player_name "Lagi?"

    show player 24f
    pause
    show old_debbie 13f
    debbie "I've been meaning to ask..."

    debbie "What exactly are you doing for the church?"

    show old_debbie 14f
    show player 11f
    player_name "..."
    show old_debbie 13f
    debbie "I mean, I'm surprised to see a nun visiting so much..."

    show old_debbie 14bf
    show player 29f at Position (xoffset=-35) with dissolve
    player_name "Yeah, um... Everything is... Fine."

    player_name "She's just... Got me running errands."

    player_name "( Yeah, heh... Heh... )"

    show player 3f at Position (xoffset=-35)
    show old_debbie 14f
    debbie "..."
    show old_debbie 13f
    debbie "Well, at least you're doing something good for the community..."

    show player 5f with dissolve
    show old_debbie 2f
    debbie "I suppose I shouldn't be worried."

    show old_debbie 3f
    debbie "What harm could come from you spending time at church?"

    hide old_debbie with dissolve
    show player 11f
    player_name "..."
    show player 37f at Position (xoffset=-41) with dissolve
    player_name "( You have no idea... )"

    hide player with dissolve
    return

label bedroom_mom_overheard:
    scene expression game.timer.image("bedroom{}")
    show player 34 with dissolve
    player_name "{i}*Distant voice*{/i}"

    show player 35
    player_name "( Is that {b}[deb_name]{/b} on the phone? )"

    show player 12
    player_name "( ... She sounds like she's mad... Is she yelling? )"

    show player 10
    player_name "( I should go see if she's okay. )"

    hide player with dissolve
    return

label bedroom_mom_movie_afterthoughts:
    scene expression game.timer.image("bedroom{}")
    show player 5
    player_name "Well, that was super awkward!"

    player_name "There is no way she didn't notice..."

    player_name "I mean, she didn't say anything..."

    player_name "... But it definitely got uncomfortable."

    show player 11
    player_name "I hope {b}[deb_name]{/b} isn't upset with me..."

    player_name "..."
    show player 24
    player_name "Ugh, I'll worry about it tomorrow. Right now, I need some sleep."

    hide player with dissolve
    return

label bedroom_mom_afterthoughts_two:
    scene location_home_bedroom_night_blur
    show player 13
    player_name "( That was really hot! )"

    player_name "( {b}[deb_name]{/b}'s nipples taste so good... )"

    player_name "( ... And she got wet enough to soak through onto my shorts! )"

    show player 5
    player_name "( ... )"
    player_name "( She kinda freaked out there at the end though. )"

    player_name "( Should I have apologized more? )"

    player_name "( ... )"
    show player 13
    player_name "( No sense worrying about it now. I should get some sleep. )"

    hide player with dissolve
    return

label bedroom_mom_note:
    scene expression game.timer.image("bedroom{}")
    show player 7 with dissolve
    player_name "{i}*Menguap*{/i}"

    show player 101 with dissolve
    player_name "I should sleep."

    hide player with dissolve
    return

label bedroom_mom_note_just_wokeup:
    scene expression player.location.background_blur
    show player 7 with dissolve
    player_name "{i}*Menguap*{/i}"

    show player 11
    player_name "!!!"
    show player 10
    player_name "Someone left a {b}note{/b} on my computer screen?"

    hide player with dissolve
    return

label bedroom_mom_chores:
    scene expression player.location.background_blur
    show player 4 with dissolve
    if randomizer() < 50:
        player_name "I wonder if {b}[deb_name]{/b} needs help around the house."

        player_name "I should go ask her..."

    else:
        player_name "I wonder if {b}[deb_name]{/b} needs my help with anything else..."

    hide player with dissolve
    return

label bedroom_mom_search_panties:
    scene expression player.location.background_blur
    show player 4 with dissolve
    player_name "( I can't stop thinking about the other day down in the basement... )"

    player_name "( {b}[deb_name]{/b} really seemed to be enjoying that massage. )"

    player_name "( Her legs are so soft and shapely... )"

    show player 11
    player_name "( Come to think of it. The lotion was in her panty drawer. )"

    player_name "( I'd like to take a closer look at that! )"

    show player 13
    player_name "( Maybe now is a good time. )"

    hide player with dissolve
    return

label bedroom_mom_kissing_practice:
    scene expression player.location.background_blur
    show player 4 with dissolve
    player_name "I keep having naughty dreams involving {b}[deb_name]{/b}."

    player_name "It's driving me nuts!"

    show player 5
    player_name "..."
    player_name "I should probably {b}talk to her{/b} about it..."

    hide player with dissolve
    return

label bedroom_bissette_french_food_assignment:
    scene expression game.timer.image("bedroom{}")
    show player 12 with dissolve
    player_name "I should do my French assignment."

    show player 14
    player_name "I have everything I need to finish it, now."

    hide player with dissolve
    return

label bedroom_sis_couch_1:
    scene expression game.timer.image("bedroom{}")
    show player 10 with dissolve
    player_name "( I hear someone in the hallway... Is that {b}[jen_name]{/b}'s door? )"

    show player 4
    player_name "( I wonder if she's up to something. )"

    hide player with dissolve
    return

label bedroom_sis_couch_3:
    scene expression game.timer.image("bedroom{}")
    show player 4 with dissolve
    player_name "( I wonder if there's a {b}new porn video{/b} on TV tonight. )"

    show player 26
    player_name "( I should try and check it out while everyone's sleeping... )"

    hide player with dissolve
    return

label pc_homework:
    if M_bissette.is_state(S_bissette_french_food_assignment):
        call expression game.dialog_select("bedroom_bissette_french_food_assignment_after")
        $ M_bissette.trigger(T_bissette_do_assignment)
        $ game.timer.tick()

    elif M_bissette.is_state(S_bissette_do_poem_assignment):
        call bedroom_bissette_do_poem_assignment
        $ player.get_item('usb')
        call popup ('give', 'usb')
        $ game.timer.tick()
        $ M_bissette.trigger(T_bissette_do_assignment)
    else:

        scene expression game.timer.image("bedroom{}")
        if M_bissette.between_states(S_bissette_find_food_book, [S_bissette_got_dexters_eriks_books, S_bissette_got_eriks_martinez_books, S_bissette_got_martinez_eriks_books]):
            call expression game.dialog_select("bedroom_bissette_find_books")
        else:

            call expression game.dialog_select("bedroom_no_school_work")
    $ game.main()

label bedroom_bissette_french_food_assignment_after:
    if not game.timer.is_dark():
        scene studybedroom01
    else:
        scene studybedroom02
    show text _ ("The book was everything someone would ever want to know about cheese.\nEverything from making, to preparing, cooking and eating all kinds of cheeses...\n... But I eventually managed to piece a few paragraphs together that should please {b}Miss Bissette{/b}.") as caption
    with fade
    pause
    return

label bedroom_bissette_do_poem_assignment:
    if not game.timer.is_dark():
        scene studybedroom01
    else:
        scene studybedroom02
    show text _ ("Writing that poem proved to be quite difficult.\n... I seemed to be having a hard time keeping my focus.\nBut after a several hours and few... Breaks. I finally managed to put something on paper!") as caption
    with fade
    pause

    scene expression game.timer.image("bedroom{}")
    show player 511
    with fade
    player_name "Akhirnya!"

    player_name "I hope this is good enough to impress {b}Miss Bissette{/b}..."

    player_name "I just need to {b}print it in the computer lab and hand it in{/b}."

    hide player with dissolve
    return

label bedroom_bissette_find_books:
    show player 73 with dissolve
    player_name "( I first need to {b}get the right book{/b} before I can finish my homework... )"

    player_name "( I can probably find it at the local {b}library{/b}. )"

    hide player with dissolve
    return

label bedroom_no_school_work:
    show player 1 with dissolve
    player_name "( I don't have any school work. )"

    hide player with dissolve
    return

label mia_midnight_text:
    call expression game.dialog_select("mia_midnight_text_dialogue")
    $ M_mia.trigger(T_mia_message)
    $ game.main()

label mia_midnight_text_dialogue:
    scene expression player.location.background_blur
    show player 442 with dissolve
    player_name "{b}Mia{/b}?! Asking... For help?"

    player_name "What is this all about?"

    player_name "Is she in trouble?"

    show player 443
    player_name "..."
    show player 442
    player_name "Maybe I should {b}go see her now{/b}... Just to make sure she's alright."

    hide player with dissolve
    return

label mia_urgent_text:
    call expression game.dialog_select("mia_urgent_text_dialogue")
    $ M_mia.trigger(T_mia_message)
    $ game.main()

label mia_urgent_text_dialogue:
    scene expression game.timer.image("bedroom{}")
    show player 10 with dissolve
    player_name "She can't find her dad?"

    player_name "I'd better go see what's going on..."

    hide player with dissolve
    return

label bed_locked:
    scene expression game.timer.image("bedroom{}")
    show player 10 with dissolve
    player_name "( I still have something I need to do before I can sleep... )"

    hide player 10 with dissolve
    $ game.main()

label bedroom_check_on_mom:
    scene expression game.timer.image("bedroom{}")
    show player 10 with dissolve
    player_name "( I should really go check on {b}[deb_name]{/b}... )"

    hide player 10 with dissolve
    $ game.main()

label bedroom_sleeping_jerk_off_roxxy:
    $ M_player.set("sex speed", .4)
    scene expression game.timer.image("backgrounds/location_home_bedroom_jerk{}.jpg")
    show player 496c_496d_496e_496d_496c zorder 0 at Position(xpos=0.3375, ypos=0.875)
    show jerkbubble zorder 1 at Position(xpos=0.6, ypos=1.0) with dissolve
    pause
    show old_roxxy dream 1 zorder 2 at Position(xpos=0.735, ypos=0.85) with dissolve
    pause
    show old_roxxy dream 2 with dissolve
    roxxy "Mmm, hello {b}[firstname]{/b}..."

    roxxy "I'm so happy you came to watch me cheer!"

    show old_roxxy dream 1 with dissolve
    player_name "..."
    show old_roxxy dream 2 with dissolve
    roxxy "I just can't keep my mind off you lately..."

    roxxy "You've been so helpful, I think you deserve a reward!"

    roxxy "I know, how about a special routine, for your eyes only?"

    roxxy "Would you like that, {b}[firstname]{/b}?"

    show old_roxxy dream 1 with dissolve
    $ M_player.set("sex speed", .3)
    show player 496c_496d_496e_496d_496c
    player_name "You bet I would!"

    show old_roxxy dream 2 with dissolve
    roxxy "Hehe, well, you just lay back and enjoy the show!"

    roxxy "Keep stroking that big cock for me, {b}[firstname]{/b}!"

    show old_roxxy dream 3 with dissolve
    $ M_player.set("sex speed", .2)
    show player 496c_496d_496e_496d_496c
    roxxy "Gimme a C!"

    "C!"

    roxxy "Gimme a U!"

    "U!"

    roxxy "Gimme a M!"

    "M!"

    show player 496f
    roxxy "What's that spell?!"

    show player 496g
    player_name "HNNGGG!!!" with flash
    roxxy "Yay!!!"

    show player 496h
    hide jerkbubble
    hide old_roxxy dream
    player_name "Haah... Haaa..."

    player_name "Uuuhh man, I'm covered..."

    pause
    player_name "{b}Roxxy{/b} is so hot!"

    return

label bedroom_sleeping_jerk_off_jenny:
    $ M_player.set("sex speed", .4)
    scene expression game.timer.image("backgrounds/location_home_bedroom_jerk{}.jpg")
    $ M_player.set("sex speed", M_player.get("sex speed") / 2)
    show player 496c_496d_496e_496d_496c zorder 0 at Position(xpos=0.3375, ypos=0.875) with None
    show jerkbubble zorder 1 at Position(xpos=0.6, ypos=1.0)
    show jenny b_dream01 f_dream zorder 2
    with dissolve
    jenny "Halo, {b}[firstname]{/b}!"

    jenny "I know I can be mean sometimes..."

    show jenny b_dream02 with dissolve
    jenny "... But you know I really want you, right?"

    show jenny f_empty
    player_name "Anda melakukannya?"

    show jenny f_dream
    jenny "Mmhmm, I want you so bad!"

    show jenny f_empty
    pause
    show jenny f_dream
    jenny "I wanna ride that big..."

    jenny "Thick..."

    jenny "Hard..."

    show jenny f_empty
    player_name "Ya Tuhan!"

    show jenny f_dream
    jenny "Cock!"

    show jenny f_empty
    show player 496g with flash
    player_name "HNNGGG!!!"

    show player 496h
    hide jerkbubble
    hide jenny
    with dissolve
    player_name "Haah... Haah..."

    player_name "Uuuhh man, I'm covered..."

    return

label bedroom_sleeping_jerk_off_diane:
    $ M_player.set("sex speed", .4)
    scene expression game.timer.image("backgrounds/location_home_bedroom_jerk{}.jpg")
    $ M_player.set("sex speed", M_player.get("sex speed") / 2)
    show player 496c_496d_496e_496d_496c zorder 0 at Position(xpos=0.3375, ypos=0.875) with None
    show jerkbubble zorder 1 at Position(xpos=0.6, ypos=1.0)
    show diane b_dream1 zorder 2:
        xoffset 250
        yoffset 300
    with dissolve
    diane "Hello, handsome."

    diane "I was hoping you'd come by today."

    diane "Mmm, my vegetables just aren't enough for me, {b}[firstname]{/b}..."

    diane "I want to feel that big, thick, cock of yours..."

    player_name "Anda melakukannya?"

    diane "Oh ya!"

    pause
    show diane b_dream2 with dissolve
    diane "Itu dia, kawan."

    diane "Tend my special garden!"

    pause
    diane "I need your seed."

    diane "Please, {b}[firstname]{/b}!"

    player_name "Ya Tuhan!"

    pause
    diane "Please, I need it so bad!"

    diane "Fill me up!!!"

    show player 496g with flash
    player_name "HNNGGG!!!"

    show player 496h
    hide jerkbubble
    hide diane
    with dissolve
    player_name "Haah... Haah..."

    pause
    player_name "Shoot... It's everywhere..."

    return

label bedroom_sleeping_jerk_off_debbie:
    $ M_player.set("sex speed", .4)
    scene expression game.timer.image("backgrounds/location_home_bedroom_jerk{}.jpg")
    show player 496 zorder 0 at Position(xpos=0.3375, ypos=0.875)
    pause
    show player 496b
    player_name "... {b}[deb_name]{/b} is so beautiful."

    player_name "I just can't stop thinking about it."

    player_name "... About her."

    player_name "Mmm, god, I want her so bad!"

    show player 496c
    show jerkbubble zorder 1 at Position(xpos=0.6, ypos=1.0) with dissolve
    pause
    show old_debbied 1 zorder 2 at Position(xpos=0.735, ypos=0.85) with dissolve
    pause
    show old_debbied 2
    debbie "Well, hello there..."

    show old_debbied 1
    $ M_player.set("sex speed", M_player.get("sex speed") / 2)
    show player 496c_496d_496e_496d_496c
    show old_debbied 2
    debbie "Oh gosh... Is that for me?"

    debbie "... It's so big!"

    show old_debbied 1
    pause
    show old_debbied 2
    debbie "... And thick!"

    show old_debbied 3 with dissolve
    debbie "Mmm, are you gonna give it to me?"

    $ M_player.set("sex speed", M_player.get("sex speed") / 2)
    show player 496c_496d_496e_496d_496c
    debbie "Berikan padaku, {b}[firstname]{/b}!"

    $ M_debbie.set("sex speed", M_debbie.get("sex speed") / 1)
    show old_debbied 4_5
    $ M_player.set("sex speed", M_player.get("sex speed") / 2)
    show player 496c_496d_496e_496d_496c
    pause
    show player 496f
    player_name "OH!"

    show player 496g with flash
    player_name "HHHNNNGGGG, HHuuuUUHH!!"

    show player 496h
    hide jerkbubble
    hide old_debbied
    player_name "Haaaah... Haaaah..."

    player_name "Uuuhh man, I'm covered..."

    return

label bedroom_sleeping_jerk_off_eve:
    $ M_player.set("sex speed", .2)
    scene expression game.timer.image("backgrounds/location_home_bedroom_jerk{}.jpg")
    show player 496c_496d_496e_496d_496c zorder 0 at Position(xpos=0.3375, ypos=0.875) with None
    show jerkbubble zorder 1 at Position(xpos=0.6, ypos=1.0)
    show eve b_dream1 zorder 2
    with dissolve
    eve "{i}*Gasp*{/i}, {b}[firstname]{/b}?!"

    eve "A-are you trying to spy on me?"

    pause
    eve "It's alright if you are."

    anon "Dia?"

    if not M_eve.finished_state(S_eve_voyeurism_follow_tent) or not M_eve.get("biggus_dickus"):
        show eve b_dream2 with dissolve
    else:
        show eve b_dream2_alt with dissolve
    eve "I want you to see me!"

    pause
    eve "Mmm, I'm so hot for you, {b}[firstname]{/b}!"

    anon "Ya Tuhan!"

    eve "I need your dick so bad!"

    eve "Please, give it to me!"

    show player 496g
    anon "HNNGGG!!!" with flash
    show player 496h
    hide jerkbubble
    hide eve
    with dissolve
    anon "Haah... Haah..."

    anon "Uuuhh man, I'm covered..."

    return

label bedroom_sleeping_jerk_off_mia:
    $ M_player.set("sex speed", .4)
    scene expression game.timer.image("backgrounds/location_home_bedroom_jerk{}.jpg")
    show player 496 zorder 0 at Position(xpos=0.3375, ypos=0.875)
    pause
    show player 496b
    player_name "{b}Mia{/b} is so cute!"

    player_name "I can't wait to see her again..."

    pause
    player_name "... That cute body of hers."

    player_name "Hmm..."

    show player 496c
    show jerkbubble zorder 1 at Position(xpos=0.6, ypos=1.0) with dissolve
    pause
    show old_miad 1 zorder 2 at Position(xpos=0.735, ypos=0.8) with dissolve
    pause
    show old_miad 2
    mia "Hai, {b}[firstname]{/b}!"

    show old_miad 1
    pause
    show old_miad 2
    mia "Wow, I've never seen one of those before!"

    $ M_player.set("sex speed", M_player.get("sex speed") / 2)
    show player 496c_496d_496e_496d_496c
    mia "Are they all that big?!"

    show old_miad 1
    pause
    show old_miad 2
    mia "I was really hoping you would be my first, {b}[firstname]{/b}."

    show old_miad 1
    $ M_player.set("sex speed", M_player.get("sex speed") / 2)
    show player 496c_496d_496e_496d_496c
    pause
    show old_miad 2
    mia "Do you think it will fit?"

    mia "... In my..."

    show old_miad 1
    $ M_player.set("sex speed", M_player.get("sex speed") / 2)
    show player 496c_496d_496e_496d_496c
    pause
    show old_miad 2
    mia "... In my pussy?"

    show player 496f
    player_name "OH!"

    show player 496g with flash
    player_name "HHHNNNGGGG, HHuuuUUHH!!"

    show player 496h
    hide jerkbubble
    hide old_miad
    player_name "Haaaah... Haaaah..."

    player_name "Uuuhh man, I'm covered..."

    return

label bedroom_sleeping_debbie_movie_night:
    scene expression game.timer.image("bedroom{}")
    show player 101b with dissolve
    player_name "I think I heard {b}[deb_name]{/b} doing something downstairs."

    hide player with dissolve
    return

label bedroom_sleeping_debbie_sleepover:
    scene expression game.timer.image("bedroom{}")
    show player 101b with dissolve
    player_name "Maybe I should sleep next to {b}[deb_name]{/b} tonight."

    player_name "She did say I could go visit her at night if I wanted to..."

    hide player with dissolve
    return

label bedroom_erik_thief_noise:
    scene location_home_bedroom_cutscene01 with fade
    pause
    "{i}*Thump*{/i}"

    scene bedroom_cs03 with dissolve
    "{i}*Thump* *Thump*{/i}"

    player_name "..."
    scene bedroom_cs04 with dissolve
    player_name "What is that noise?"

    scene bedroom_night with fade
    show player 101bf with dissolve
    player_name "( Sounds like it's coming from outside. )"

    player_name "( ... From {b}Erik{/b}'s yard, maybe? )"

    show player 100bf

    menu:
        "Use the telescope.":
            pass
        "Go back to sleep.":
            show player 101f
            player_name "( It's probably just some animal. )"

            player_name "( I need to get to sleep... )"

            hide player with dissolve
            return

    show player 101bf
    player_name "( I should probably go have a look. )"

    show player 100f
    player_name "Hmm..."

    show player 101bf
    player_name "( I'll just take a quick peek through my telescope. )"

    hide player

    scene windowbackyardnight02a
    with fade
    player_name "?!?!"
    player_name "What the..."


    scene windowbackyardnight02b
    player_name "( Is that someone sneaking into {b}Erik{/b}'s yard?! )"

    player_name "( That's the burglar I've been hearing about in the news! )"


    scene windowbackyardnight02c
    player_name "..."
    player_name "( Is he going into {b}Erik{/b}'s house?! )"


    scene bedroom_night
    show player 101bf
    with fade
    player_name "( This is bad! )"

    player_name "( What if {b}Erik{/b} and {b}Mrs. Johnson{/b} are in danger? )"

    player_name "( I should {b}go outside and see what he's doing in Erik's yard{/b}. )"

    hide player with dissolve

    scene black with fade
    return True

label bedroom_erik_bully_tired:
    scene expression game.timer.image("bedroom{}")
    show player 12 with dissolve
    player_name "( Man... What a day. )"

    show player 17
    player_name "( I guess the training at the gym is starting to pay off! )"

    pause
    show player 12
    player_name "( {b}Dexter{/b} is never going to let this go. )"

    player_name "( ... I'm gonna need all the training I can get! )"

    show player 8 with dissolve
    pause
    show player 7 with dissolve
    player_name "{i}*Menguap*{/i}"

    show player 101 with dissolve
    player_name "( I'd better get some sleep. )"

    hide player with dissolve
    return

label bedroom_sleeping_dewitt_eve_karaoke:
    scene expression game.timer.image("bedroom{}")
    show player 14 with dissolve
    player_name "I'm supposed to {b}meet Eve over at Erik's house tonight{/b}!"

    show player 30
    player_name "Sleep will have to wait."

    hide player with dissolve
    return

label bedroom_sleeping_dewitt_school_sneak_mission:
    scene expression game.timer.image("bedroom{}")
    show player 10 with dissolve
    player_name "Tonight, I was going to sneak into school with {b}Erik{/b}."

    player_name "I can't go to bed yet."

    hide player with dissolve
    return

label bedroom_sleeping_mia_midnight_call:
    scene location_home_bedroom_cutscene01 with dissolve
    player_name "{i}*ZZzz*{/i}..."

    "{i}*Bzzt*{/i}!"

    player_name "..."
    "{i}*Bzzzzzzt*{/i}!"

    scene bedroom_cs04 with dissolve
    player_name "Hah?"

    player_name "Is that my phone?"

    scene black with fade
    pause
    scene bedroom_night
    show player 7 with dissolve
    pause
    show player 101
    player_name "Someone's texting me?"

    player_name "I should see who it is..."

    hide player with dissolve
    return

label bedroom_sleeping_debbie_solo_dream:
    scene dream_debbie_04 with fade:
        ypos -707
        linear 4.0 ypos 0
    debbie "Hmm..."

    debbie "Oh, that feels wonderful, sweetie."

    player_name "..."
    player_name "Oh, {b}[deb_name]{/b}..."

    debbie "I want you {b}[firstname]{/b}!"

    debbie "I want you inside me so bad!"

    player_name "{i}*Meneguk*{/i}"

    player_name "Benar-benar?"

    debbie "You have no idea! Give me that big, hard cock, {b}[firstname]{/b}!"

    debbie "Please, I need it!"

    player_name "..."
    debbie "Do it now! Hurry! I can't wait any longer!"

    scene dream_debbie_05 with dissolve:
        ypos 0
    pause
    player_name "Hnnggg!!" with flash
    pause
    scene dream_debbie_05 with flash:
        ypos 0
        linear 4.0 ypos -475
    player_name "... Oooooh..."

    pause

    scene location_home_bedroom_cutscene06 with fade
    pause
    scene location_home_bedroom_cutscene07
    player_name "..."
    scene location_home_bedroom_cutscene08
    player_name "Ya ampun..."

    pause
    scene location_home_bedroom_cutscene09
    pause
    player_name "aku membuat kekacauan..."

    player_name "... But holy crap, that was intense..."

    player_name "It all felt so real!"

    player_name "Arrgghh, I'm really losing it!"

    player_name "I just can't stop thinking about her!"

    player_name "I want to hold her and kiss her so bad..."

    player_name "Maybe I should try {b}talking to {b}[deb_name]{/b} about kissing{/b}?"

    player_name "She seemed kind of into it at first, when I kissed her in the mall..."

    player_name "Hmm, it's risky but I think it's worth a shot!"

    player_name "I might go nuts if I don't do something..."

    player_name "... But first I should clean up and get some more sleep."

    return

label bedroom_sleeping_debbie_night_visit:
    scene location_home_bedroom_cutscene01 with dissolve
    player_name "{i}*ZZzz*{/i}..."

    scene location_home_bedroom_cutscene02 with dissolve
    debbie "( ... )"
    debbie "( I can't fall asleep. )"

    debbie "( Ever since I watched him masturbate... )"

    debbie "( I can't stop thinking about his- )"

    debbie "( I just... )"

    debbie "( ... )"
    define fadehold = Fade(0.5, 1.0, 0.5)

    scene location_home_bedroom_sex01
    show debbies 1
    with dissolve
    debbie "( I can't believe I'm having these thoughts... )"

    debbie "( It's one thing for him to be having them. He's just a young man. )"

    debbie "( ... But I'm old enough to know better! )"

    show debbies 2
    debbie "( He doesn't really want me! It's just a silly crush! )"

    debbie "( I'm old enough to be his mother! )"

    debbie "( ... But the way he makes me feel. )"

    show debbies 3
    debbie "( The way he looks at me with those hungry eyes... )"

    show debbies 4
    debbie "( ... Mmm, I need to see it... )"

    show debbies 5
    debbie "( Just a peek. )"

    show debbies 6
    debbie "( ... )"
    show debbies 7_8
    pause 4
    show debbies 6
    debbie "( It's just so big... )"

    show debbies 7_8
    debbie "( ... And it's getting bigger. )"

    debbie "( Mmm... )"

    show debbies 9
    pause
    show debbies 10
    debbie "( I have to see it! )"

    debbie "( Oh, it's so thick... )"

    show debbies 11
    debbie "( !!! )"
    show debbies 12
    debbie "{i}*Terkesiap*{/i}!"

    debbie "( It's so unbelievable! )"

    debbie "( {i}*Sigh*{/i} What am I going to do? )"

    debbie "( I just can't get this cock out of my head! )"

    debbie "( ... )"
    debbie "( It's been so long since I've felt one... )"

    debbie "( ... And I miss it so much. )"

    debbie "( It's not so bad for me to touch it... Just a little bit. Right? )"

    debbie "( Surely, it's uncomfortable for him. Just look at how hard it is! )"

    show debbies 13
    pause
    show debbies 14
    pause
    debbie "( ... So hard... )"

    debbie "( ... And thick. )"

    show debbies 13
    debbie "..."
    show debbies 13_14
    pause
    debbie "( Oh, god. What am I doing?! )"

    debbie "..."
    debbie "( I'm stroking his cock! )"

    debbie "( Hah... His big, juicy- )"

    debbie "( Just like he was stroking it for me earlier. )"

    pause
    debbie "( He says he wants me... He wants me so bad that he masturbates while thinking about me! )"

    debbie "( Mmm... )"

    debbie "( He wants to fuck me with this- )"

    show debbies 12
    debbie "( ... )"
    show debbies 20
    debbie "( What's wrong with me?! )"

    show debbies 21
    debbie "( Oh, god! )"

    debbie "( I need to get out of here! )"

    debbie "( ... Walk away, {b}[deb_name]{/b}! )"

    show debbies 22 at Position(xpos = 544, ypos = 768)
    player_name "Hmm?"

    show debbies 23
    player_name "( What- )"

    player_name "( ... Was that? )"

    show debbies 24 at Position(xpos = 512, ypos = 768)
    player_name "( Hmm, it's nothing. )"

    return

label bedroom_sleeping_debbie_night_visit_two:
    label mom_night_suck:
        scene location_home_bedroom_cutscene01 with dissolve
    player_name "{i}*ZZzz*{/i}..."

    scene location_home_bedroom_cutscene02 with dissolve
    pause
    scene location_home_bedroom_sex01
    show debbies 1
    with dissolve
    debbie "( What am I doing here again?! )"

    debbie "( Why can't I stop thinking about his cock?! )"

    debbie "( I just keep imagining it inside me! )"

    show debbies 2
    debbie "( ... )"
    debbie "( ... Maybe {b}Diane{/b} is right; perhaps I should just relax and let myself go. )"

    debbie "( Those hungry looks he gives me... )"

    debbie "( Mmm, I'm getting wet just thinking about it... )"

    show debbies 3
    debbie "( I have to see it again! )"

    show debbies 4
    debbie "( ... )"
    show debbies 5
    debbie "( Oh, this is so wrong... What are you doing, {b}[deb_name]{/b}? )"

    show debbies 6
    debbie "( It's even bigger than I remember... )"

    show debbies 7_8
    pause 4
    show debbies 6
    debbie "( Mmm and it's growing again... )"

    show debbies 7_8
    debbie "( ... So {b}hard{/b}. )"

    debbie "( ... )"
    debbie "( ... Maybe I could just take a peek... )"

    show debbies 9
    pause
    show debbies 10
    debbie "( ... I mean, it has to be uncomfortable for him. )"

    debbie "( I'm just helping him relax... That's all. )"

    show debbies 11
    debbie "( !!! )"
    show debbies 12
    debbie "..."
    debbie "( Oh, Lord help me! )"

    debbie "( Mmm... )"

    show debbies 13
    debbie "( I just can't resist touching it! )"

    debbie "( It feels so good in my hands... )"

    show debbies 13_14
    debbie "( It's so thick... )"

    debbie "( ... And juicy. )"

    debbie "( ... )"
    debbie "( It's been so long... )"

    debbie "( I want... )"

    debbie "( I want to taste it! )"

    show debbies 15
    debbie "( I NEED to taste it! )"

    debbie "( Just for a second! That couldn't hurt, right? )"

    show debbies 16_17
    debbie "( Yes!! )"

    debbie "( Oh god, I've missed this so much! )"

    debbie "( I'm so horny! )"

    show debbies 18
    player_name "{i}*Moan*{/i}"

    show debbies 19
    debbie "( !!! )" with hpunch
    debbie "( Oh crap! He's waking up... )"

    debbie "( ... )"
    show debbies 20
    debbie "( What am I doing?! )"

    debbie "( I can't let him see me like this! )"

    show debbies 21
    debbie "( I have to get out of here! )"

    show debbies 22 at Position(xpos = 544, ypos = 768)
    player_name "Hmm?"

    show debbies 23
    player_name "What's-"

    player_name "( ... Was that? )"

    show debbies 24 at Position(xpos = 512, ypos = 768)
    player_name "( ... )"
    player_name "( I guess it was nothing... )"

    $ renpy.end_replay()
    return

label bedroom_sleeping_debbie_midnight_noises:
    scene bedroom_cs01 with fade
    "Hahaha..."

    "{i}*SPLASH*{/i}"

    scene bedroom_cs03 with dissolve
    player_name "..."
    scene bedroom_cs04
    player_name "Who is making all that noise outside?"

    scene bedroom_cs03
    player_name "..."
    player_name "......"
    scene bedroom_cs01 with dissolve
    pause
    "{i}*SPLASH*{/i}"

    scene bedroom_cs04 with dissolve
    player_name "What is going on?"


    scene bedroom_night
    show player 101b
    with dissolve
    player_name "Maybe, I should go check to see what's going on."

    player_name "Sounds like whoever is outside isn't going to stop any time soon."

    show player 8 with dissolve
    return

label bedroom_sleeping_debbie_night_visit_three:
    $ M_debbie.set("sex speed", .175 / .75)
    scene location_home_bedroom_cutscene01 with dissolve
    player_name "{i}*ZZzz*{/i}..."

    scene location_home_bedroom_cutscene02 with dissolve
    pause
    scene location_home_bedroom_sex01
    show debbies 1
    with dissolve
    debbie "( Oh... )"

    debbie "( I'm here... )"

    show debbies 3
    debbie "( What am I doing! )"

    show debbies 4
    debbie "( WHAT AM I DOING!!! )"

    show debbies 5
    debbie "( Mmm! )"

    debbie "( There it is! )"

    show debbies 6
    debbie "( Oh, I want it so bad... )"

    show debbies 7_8
    debbie "( Get hard for me, sweetie... )"

    debbie "( Please... )"

    show debbies 6
    pause
    show debbies 9
    pause
    show debbies 10
    debbie "( ... )"
    show debbies 11
    debbie "( !!! )"
    show debbies 12
    debbie "..."
    debbie "( Oh, I'm burning up... I need it!!! )"

    show debbies 15
    debbie "( Mmm. )"

    $ M_debbie.set("sex speed", M_debbie.get("sex speed") / .75)
    show debbies 16_17
    debbie "( Oh! So good! )"

    debbie "( I miss this taste so much! )"

    player_name "( Mmm. )"

    debbie "{i}*Menyeruput*{/i}"

    show debbies 19
    player_name "Hmm?"

    show debbies 20b
    player_name "What's-"

    show debbies 20c at Position(xpos=0.53, ypos=1.0) with dissolve
    player_name "... {b}[deb_name]{/b}?"

    show debbies 20d
    debbie "It's alright, {b}[firstname]{/b}, it's me."

    show debbies 20c
    player_name "... Oke."

    player_name "But what's going-"

    show debbies 20d
    debbie "Shhh..."

    show debbies 20c
    player_name "{b}[deb_name]{/b}? What are you-"

    show debbies 20e with dissolve
    debbie "Hush, sweetie, just relax and let yourself go..."

    player_name "..."


    debbie "Oh, I need it, {b}[firstname]{/b}!"

    debbie "I need that big cock inside of me!!!"

    show debbies 20f at Position(xpos=0.5, ypos=1.0) with dissolve
    player_name "{i}*Meneguk*{/i}"

    debbie "I tried..."

    debbie "I tried so hard to resist."

    debbie "... But I just can't!"

    show debbies 20g with dissolve
    debbie "Please, don't think less of me..."

    pause
    show debbies 20h with hpunch

    player_name "... Ooohh!!"

    debbie "Haaaaaaaah!"

    $ M_debbie.set("sex speed", M_debbie.get("sex speed") / 1.75)
    show debbies 20h_20i_20j_20k_20l_20m_20n_20o
    debbie "Oh god!!"

    pause
    debbie "Oh, it's even better than I imagined!"

    player_name "Oh, {b}[deb_name]{/b} this feels so good!"

    $ M_debbie.set("sex speed", M_debbie.get("sex speed") / 2)
    show debbies 20h_20i_20j_20k_20l_20m_20n_20o
    debbie "Haah! {b}[firstname]{/b}! Oh, {b}[firstname]{/b}!"

    debbie "aku akan keluar!"

    show debbies 20h with flash
    debbie "AAHHH!!"


    player_name "... You're shaking! Are you alright, {b}[deb_name]{/b}?!"

    debbie "Haaah... Haaaah..."

    debbie "... Don't worry, sweetie."

    show debbies 20h_20i_20j_20k_20l_20m_20n_20o
    debbie "Keep going! Fuck, this is so good!"

    player_name "..."
    debbie "Give it to me!!"

    $ M_debbie.set("sex speed", M_debbie.get("sex speed") / 1.5)
    show debbies 20h_20i_20j_20k_20l_20m_20n_20o
    debbie "OOOH YES!!!"

    debbie "That's it, baby!!"

    debbie "Give me that fat cock!"

    return

label bedroom_sleeping_debbie_night_visit_three_loop:
    menu:
        "Terus berlanjut." if keep_going < 2:
            $ keep_going += 1
            if M_debbie.get("change angle"):
                show expression AnimatedImage("debbies", [170,171,172,173,174,175,176,177], M_debbie) as debbies
            else:

                show expression AnimatedImage("debbies", ["20h","20i","20j","20k","20l","20m","20n","20o"], M_debbie) as debbies
            pause
            jump expression game.dialog_select("bedroom_sleeping_debbie_night_visit_three_loop")

        "Change angle." if keep_going < 2:
            $ keep_going += 1
            if not M_debbie.get("change angle"):
                $ M_debbie.set("sex speed", .15)
                $ M_debbie.set("change angle", True)
                hide debbies
                scene bedroom_sex_05
                show expression AnimatedImage("debbies", [170,171,172,173,174,175,176,177], M_debbie) as debbies
                with fade
            else:

                $ M_debbie.set("sex speed", ((.175 / .75) / 3) / 1.5)
                $ M_debbie.set("change angle", False)
                hide debbies
                scene location_home_bedroom_sex01
                show expression AnimatedImage("debbies", ["20h","20i","20j","20k","20l","20m","20n","20o"], M_debbie) as debbies
                with fade
            pause
            jump expression game.dialog_select("bedroom_sleeping_debbie_night_visit_three_loop")
        "Cum.":

            call expression game.dialog_select("bedroom_sleeping_debbie_night_visit_three_cum_pre")


            if M_player.is_set("pet cat"):
                scene location_home_bedroom_sleeping4 with fade
            else:
                scene location_home_bedroom_sleeping2 with fade

            if not _in_replay:
                call popup ('sleep')

            call expression game.dialog_select("bedroom_sleeping_debbie_night_visit_three_cum_after")
    $ renpy.end_replay()
    $ persistent.cookie_jar["Debbie"]["unlocked"] = True
    $ persistent.cookie_jar["Debbie"]["gallery"]["10_unlocked"] = True
    $ M_debbie.trigger(T_debbie_midnight_fun)
    call sleep_lock_check
    $ M_player.set("just wokeup", False)
    $ game.main()

label bedroom_sleeping_debbie_night_visit_three_cum_pre:
    player_name "Oh, {b}[deb_name]{/b}... I'm gonna..."

    player_name "... I'm gonna!!"

    debbie "Don't stop!! Don't-"

    $ M_debbie.set("sex speed", M_debbie.get("sex speed") / .075)
    scene location_home_bedroom_sex01
    show debbies 20p_20q
    with flash
    player_name "HHNNGGG!!!!!"


    debbie "AAAAAAAAHHHH!!!"

    pause
    show debbies 20h

    player_name "{i}*Panting*{/i}"


    debbie "Hmm..."

    show debbies 20r with dissolve
    debbie "..."
    show debbies 20s with dissolve
    debbie "Oh gosh..."

    show debbies 20t
    player_name "Itu luar biasa!"

    show debbies 20s
    debbie "Hehe, it really was..."

    debbie "..."
    debbie "I'm so sorry, sweetheart!"

    debbie "I shouldn't have done this..."

    show debbies 20t
    player_name "What?! No, don't say that!"

    debbie "..."
    player_name "I wanted this too!"

    show debbies 20s
    debbie "... You did?"

    show debbies 20t
    player_name "You have no idea! It's practically all I can think about!"

    show debbies 20s
    debbie "... Really?"

    show debbies 20t
    player_name "Ya!"

    player_name "Aku cinta kamu, {b}[deb_name]{/b}!"

    show debbies 20s
    debbie "I... I love you too, {b}[firstname]{/b}!"

    debbie "..."
    debbie "Nobody has ever made me cum like that before!"

    show debbies 20t
    player_name "Never?"

    show debbies 20s
    debbie "Never. That orgasm was crazy!"

    show debbies 20t
    player_name "Sorry I didn't last very long..."

    show debbies 20s
    debbie "No, you did great, sweetheart! Especially for our first time!"

    show debbies 20t
    player_name "... First time?"

    debbie "..."
    player_name "Can we do this again, {b}[deb_name]{/b}?"

    show debbies 20s
    debbie "Oh, sweetie, are you sure that's what you want?"

    show debbies 20t
    player_name "Of course!!!"

    player_name "{b}[deb_name]{/b}, I've never wanted anything more!"

    show debbies 20s
    debbie "Oh gosh..."

    debbie "I hate to admit it but I feel the same way!"

    debbie "..."
    debbie "Alright, sweetie..."

    debbie "... But we can only be naughty when no one else is around!"

    debbie "And you can't tell ANYBODY! Especially not {b}[jen_name]{/b}!"

    debbie "Do you understand?!"

    show debbies 20t
    player_name "Ya."

    show debbies 20s
    debbie "{b}[firstname]{/b}, I'm serious! You cannot tell a soul about this!"

    show debbies 20t
    player_name "I won't, {b}[deb_name]{/b}. I promise."

    show debbies 20s
    debbie "Anak baik."

    debbie "{i}*Menguap*{/i}"

    debbie "Oh, I'm exhausted now."

    show debbies 20t
    player_name "Ya, aku juga."

    show debbies 20s
    debbie "Mmm, I could fall asleep right here."

    show debbies 20t
    player_name "You should, {b}[deb_name]{/b}."

    show debbies 20s
    debbie "I guess it would be alright. So long as I get out of here before {b}[jen_name]{/b} wakes up."


    scene location_home_bedroom_cutscene_sleep
    show text _ ("{b}[deb_name]{/b} and I had finally slept together.") as caption
    with fade
    pause
    hide caption with dissolve
    show text _ ("It had been spectacular! All of our pent up anxieties evaporated in an instant!") as caption with dissolve
    pause
    hide caption with dissolve
    show text _ ("Our worries disappeared as she drifted off to sleep in my arms.") as caption with dissolve
    pause
    hide caption with dissolve
    show text _ ("... We awoke the next morning feeling better than either of us could ever remember.") as caption with dissolve
    pause
    return

label bedroom_sleeping_debbie_night_visit_three_cum_after:

    scene location_home_bedroom_sex04
    show debbies 20u
    pause
    show debbies 20v
    player_name "{b}[deb_name]{/b}?"

    show debbies 20u
    player_name "..."
    show debbies 20v
    player_name "{b}[deb_name]{/b}, wake up."

    show debbies 20u
    debbie "Hmm?"

    show debbies 20x
    debbie "{i}*Yawn*{/i} Is it morning already?"

    show debbies 20w
    player_name "Saya khawatir demikian."

    show debbies 20x
    debbie "Oh, I slept like a log..."

    show debbies 20w
    player_name "Heh, yeah, me too."

    show debbies 20x
    debbie "Mmm, alright. I suppose I'd better get out of here before {b}[jen_name]{/b} wakes up."

    show debbies 20w
    player_name "You sure you don't want to fool around a bit more?"

    show debbies 20x
    debbie "Hehe, don't tempt me, sweetie. That cock of yours is hard to say no to."

    show debbies 20w
    player_name "I'll never get tired of hearing that!"

    show debbies 20x
    debbie "Come and find me later, okay?"

    scene black with fade
    return

label bedroom_sleeping_debbie_smith_dream:
    scene dream_debbie 1 at Position(ypos=1475) with fade
    debbie "Good morning, sweetie."

    debbie "It's me, {b}[deb_name]{/b}."

    player_name "{b}[deb_name]{/b}?"

    player_name "Where are we?"

    debbie "It's okay. Everything will be alright..."

    debbie "Let me take care of you."

    scene dream_debbie 1_2:
        linear 5.0 ypos -707
    player_name "{b}[deb_name]{/b}..."

    player_name "What are you doing..."

    debbie "... It's okay... I just want you to feel good..."

    player_name "{b}[deb_name]{/b}... That feels amazing!"

    scene dream_debbie 3
    player_name "( !!! )" with hpunch
    smith "{b}[firstname]{/b}!!!"

    scene dream_debbie 3:
        ypos -707
        linear 1.0 ypos 0
    smith "What are you doing here?!?"

    smith "Are you... SLEEPING?!"

    smith "Get to class NOW or I'm sending your ass to DETENTION!"

    scene black with fade
    pause .2
    scene expression game.timer.image("bedroom{}")
    show player 264
    with dissolve
    player_name "{i}*Menguap*{/i}"

    show player 265 with dissolve
    player_name "( !!! )"
    show player 266
    player_name "( That was such a strange dream! )"

    player_name "( {b}[deb_name]{/b} and I were doing things, and she was naked! )"

    player_name "( Then {b}Mrs. Smith{/b}... )"

    show player 267 with hpunch
    player_name "( !!! )"
    show player 268
    player_name "( Is this normal?! )"

    player_name "( I've never had those kinds of dreams with {b}[deb_name]{/b} before... )"

    hide player with dissolve
    return

label bedroom_debbie_sleepover_pre:
    $ M_debbie.set("sex speed", .12)
    scene location_home_bedroom_sex01 with fade
    show debbies 1
    player_name "( ... )"
    debbie "Sayang?"

    debbie "Aww, did you fall asleep waiting on me?"

    player_name "( ... )"
    show debbies 3
    pause
    show debbies 4
    pause
    show debbies 5
    pause
    show debbies 6
    debbie "... Wake up, sweetie."

    $ M_debbie.set("sex speed", .09)
    show debbies 7_8
    debbie "Hmm..."

    show debbies 6
    pause
    show debbies 9
    pause
    show debbies 10
    debbie "( ... )"
    show debbies 11
    debbie "( !!! )"
    show debbies 12
    pause
    show debbies 20b
    debbie "{b}[firstname]{/b}?"

    player_name "... Hmm?"

    show debbies 20c at Position(xpos=0.53, ypos=1.0) with dissolve
    player_name "... {b}[deb_name]{/b}?"

    player_name "Crap, I fell asleep, didn't I?"

    show debbies 20d
    debbie "Hehe, that's okay, sweetie."

    show debbies 20c
    player_name "Did you still wanna- ?"

    show debbies 20e with dissolve
    debbie "Shh, we don't want to wake {b}[jen_name]{/b}!"

    player_name "Oh! ... Yeah, sorry."

    show debbies 20f at Position(xpos=0.5, ypos=1.0) with dissolve
    debbie "hehe..."

    debbie "It's alright, you're just excited. I'm excited too!"

    debbie "I could hardly wait for {b}[jen_name]{/b} to get in bed."

    show debbies 20g with dissolve
    player_name "Oh wow, {b}[deb_name]{/b}, you're sopping wet!"

    debbie "I told you I was excited."

    show debbies 20h with dissolve
    debbie "Hmm..."

    debbie "Now, let's not waste time... Give it to me, sweetie!"

    $ M_debbie.set("sex speed", .06)
    show expression AnimatedImage("debbies", ["20h","20i","20j","20k","20l","20m","20n","20o"], M_debbie) as debbies
    $ animated = True
    return

label bedroom_debbie_sleepover:
    call expression game.dialog_select("bedroom_debbie_sleepover_pre")
    $ M_debbie.set("change angle", False)
    jump expression game.dialog_select("bedroom_debbie_sleepover_loop")

label bedroom_debbie_sleepover_loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                if M_debbie.get("change angle"):
                    scene bedroom_sex_05
                    show expression AnimatedImage("debbies", [170,171,172,173,174,175,176,177], M_debbie) as debbies
                    with dissolve
                else:
                    scene location_home_bedroom_sex01
                    show expression AnimatedImage("debbies", ["20h","20i","20j","20k","20l","20m","20n","20o"], M_debbie) as debbies
                    with dissolve
                $ animated = True
            pause 5
            call expression game.dialog_select("bedroom_debbie_sleepover_hscene_dialog")
            pause 3
        else:

            $ pose_counter = 0
            if M_debbie.get("change angle"):
                scene bedroom_sex_05
                $ pose_list = [170,171,172,173,174,175,176,177]
            else:
                scene location_home_bedroom_sex01
                $ pose_list = ["20h","20i","20j","20k","20l","20m","20n","20o"]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "debbies {}".format(pose_list[pose_counter]) as debbies at Position(xalign = 0.0, yoffset = 0)
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call expression game.dialog_select("bedroom_debbie_sleepover_hscene_dialog")
        $ animcounter += 1
    call screen bedroom_debbie_sleepover_options

label bedroom_debbie_sleepover_hscene_dialog:
    if animcounter == 0 and randomizer() < 50:
        debbie "Ahh!!!{p=1}{nw}"

        debbie "Oh {b}[firstname]{/b}, it's so deep!{p=2}{nw}"

        debbie "You like it when I squeeze you with my pussy?{p=2}{nw}"

        player_name "Ya Tuhan, ya!{p=1}{nw}"

        debbie "{b}[firstname]{/b}!{p=1}{nw}"

    elif animcounter == 0 and randomizer() > 50:
        debbie "Oh yes!!!{p=1}{nw}"

        debbie "That's it, baby! Fuck my pussy!{p=2}{nw}"

        debbie "Mmm, you like that?{p=1}{nw}"

        player_name "Oh yeah, {b}[deb_name]{/b}!{p=1}{nw}"

        debbie "Faster, baby!{p=1}{nw}"

    if animcounter == 2 and randomizer() < 50:
        debbie "Oh god, that's good!{p=1}{nw}"

        debbie "Who's my naughty boy?{p=1}{nw}"

        player_name "Mmm, I am...{p=1}{nw}"

        debbie "That's right, baby! Fuck me harder!{p=2}{nw}"

        player_name "Uuhh!! You like this hard cock, {b}[deb_name]{/b}?{p=2}{nw}"

        debbie "Aaahh!! Yes! Yesss! YESSSSSS!!{p=1}{nw}"

        debbie "Give it to meeeeee!{p=1}{nw}"

    return

label bedroom_debbie_sleepover_cum:
    call expression game.dialog_select("bedroom_debbie_sleepover_cum_dialogue")

    if M_player.is_set("pet cat"):
        scene location_home_bedroom_sleeping4 with fade
    else:
        scene location_home_bedroom_sleeping2 with fade

    call popup ('sleep')
    call sleep_lock_check
    $ M_player.set("just wokeup", False)

    if randomizer() < 70 and not M_debbie.is_state(S_debbie_do_her_again):
        call expression game.dialog_select("bedroom_debbie_sleepover_after_random_70")
    else:

        call expression game.dialog_select("bedroom_debbie_sleepover_after_not_random")
        if M_debbie.is_state(S_debbie_do_her_again):
            call expression game.dialog_select("bedroom_debbie_sleepover_after_not_basement_sex")
            $ M_debbie.trigger(T_debbie_reromp)
        hide player with dissolve
    $ game.main()

label bedroom_debbie_sleepover_cum_dialogue:
    player_name "... Oh!"

    player_name "{b}[deb_name]{/b}, I'm gonna..."

    debbie "Do it, baby! Come inside me!"

    $ M_debbie.set("sex speed", .4)
    scene location_home_bedroom_sex01
    show debbies 20p_20q
    with flash
    player_name "Uhhhuh!!!"

    debbie "Hnnngg!!"

    debbie "AAAAHHhh!!!"

    player_name "Shh! You're gonna wake {b}[jen_name]{/b}!"

    player_name "..."
    show debbies 20h with dissolve
    debbie "Huhhh, huhhh, huhhh..."

    show debbies 20r with dissolve
    pause
    show debbies 20s with dissolve
    debbie "Oh {b}[firstname]{/b}... That was..."

    show debbies 20t
    player_name "Mind-blowing?"

    show debbies 20s
    debbie "Phew... Yes!"

    debbie "Mmm, I can't feel my legs."

    pause
    debbie "... I love you, {b}[firstname]{/b}."

    show debbies 20t
    player_name "I love you too, {b}[deb_name]{/b}. You're the best!"

    show debbies 20s
    debbie "Hah, thanks, sweetie."

    return

label bedroom_debbie_sleepover_after_random_70:
    scene location_home_bedroom_sex04
    show debbies 20u
    pause
    show debbies 20v
    player_name "Wake up, {b}[deb_name]{/b}."

    show debbies 20u
    debbie "Hmm..."

    show debbies 20w
    player_name "The sun is up."

    show debbies 20x
    debbie "Good morning, sweetie."

    show debbies 20w
    player_name "You sleep alright?"

    show debbies 20x
    debbie "... You kidding? After getting fucked like that, I slept great!"

    show debbies 20w
    player_name "Heh, me too..."

    debbie "..."
    show debbies 20x
    debbie "I should probably get out of here before {b}[jen_name]{/b} gets up."

    show debbies 20w
    player_name "Ya..."

    show debbies 20x
    debbie "Thanks for a great night, {b}[firstname]{/b}! I love you!"

    show debbies 20w
    player_name "I love you too, {b}[deb_name]{/b}!"

    scene black with fade
    return

label bedroom_debbie_sleepover_after_not_random:
    scene location_home_bedroom_day_blur
    show player 7
    pause
    show player 8
    pause
    show player 1
    player_name "..."
    show player 2
    player_name "Hmm, {b}[deb_name]{/b} must have woken before me and snuck out..."

    player_name "Phew, what a night! I slept like a baby..."

    return

label bedroom_debbie_sleepover_after_not_basement_sex:
    show player 10
    player_name "Hmm, what is that note on my computer monitor?"

    player_name "... Did {b}[deb_name]{/b} leave that?"

    return

label tired_bedroom_dialogue:
    scene expression game.timer.image("bedroom{}")
    show player 55 with dissolve
    player_name "{i}*Menguap*{/i}"

    show player 56
    player_name "( I'm too tired for that... )"

    hide player 56
    $ game.main()

label M6_note:
    call expression game.dialog_select("M6_note_dialogue")
    $ M_debbie.trigger(T_debbie_read_note)
    $ game.main()

label M6_note_dialogue:
    scene expression game.timer.image("bedroom{}")
    show debbienote at Position (ypos=650) with dissolve
    pause
    hide debbienote with dissolve
    show player 11 with dissolve
    player_name "( {b}[deb_name]{/b} needs help with the laundry? )"

    player_name "( I should go see what it's about. )"

    hide player with dissolve
    return

label pet_cat:
    scene expression game.timer.image("bedroom{}")
    show cat 14 with dissolve
    player_name "Hey there, [cat_name]!"

    show cat 12
    if randomizer() < 33:
        cat "{i}*Meow*{/i}"

    elif randomizer() < 66:
        cat "{i}*Prrrr*{/i}"

    else:
        cat "{i}*Brrrep*{/i}"

    show cat 15 at Position(xoffset = -7)
    pause
    show cat 14
    if randomizer() < 15:
        player_name "Who's a good kitty?!"

    elif randomizer() < 30:
        player_name "You just gonna sleep all day?"

    elif randomizer() < 45:
        player_name "What did you do today, huh?"

    elif randomizer() < 60:
        player_name "You cute little fuzzball."

    elif randomizer() < 75:
        player_name "Aww, snuggles for kitty!"

    elif randomizer() < 85:
        player_name "Hey, watch it with those claws!"

    elif randomizer() < 93:
        player_name "I should get you a toy, huh?"

    else:
        player_name "I just love petting my pussy..."

    show cat 16
    pause
    hide cat with dissolve
    $ game.main()

label cookies:
    scene expression game.timer.image("bedroom{}")
    show expression "objects/closeup_cookies.png" at left with dissolve
    player_name "( A box of my favorite cookies! )"

    player_name "( I should keep them in my backpack in case I get hungry. )"

    hide expression "objects/closeup_cookies.png" with dissolve
    call popup ('give', 'cookies')
    $ game.main()

label bedroom_anon_too_tired:
    scene expression player.location.background_blur
    show anon f_tired with dissolve
    anon @ -m_talk "( I'm so tired right now, I'd better go to bed... )"

    hide anon with dissolve
    return

label bedroom_anon_no_time:
    scene expression player.location.background_blur
    show anon f_looking_down with dissolve
    anon @ -m_talk "( No time for that right now, there's things I need to do. )"

    hide anon with dissolve
    return

label home_bedroom_drawing2_dialogue:
    scene expression background(656, 376, 7.5) as stage
    show closeup_drawing_02
    anon "This is the drawing {b}Eve{/b} made for me the night we kissed for the first time."

    anon "What a great memory."

    pause
    return


label home_bedroom_picture3_dialogue:
    scene expression background(656, 376, 7.5) as stage
    show closeup_picture3
    pause
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
