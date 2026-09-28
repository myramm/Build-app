label ano27_free_warehouse_lab:
    scene expression background(824, 488, 10, l=L_warehouse_depot) as stage
    harold "Alright, just take it slow..."
    show harold a_gun_down b_tanktop with {'master': dissolve}:
        xoffset 200
        xzoom -1
    harold "... There's no telling what could be around the next corner."
    show anon a_sides f_worried behind harold with {'master': dissolve}:
        xoffset 25
    anon "{b}[deb_name]{/b} and {b}[jen_name]{/b}, I hope."
    harold "Me too, son."
    tony "Hey, you guys smell that?"
    show anon f_confused:
        xoffset -475
        xzoom -1
    show tony a_pipe_hold_shoulder b_casual f_suspicious behind anon:
        xoffset -200
        xzoom -1
    with {'master': dissolve}
    anon @ -m_talk "Hmm?"
    show tony a_pipe_nose with {'master': dissolve}
    tony "Somethin' reeks!"
    show anon f_unimpressed
    harold f_concerned "Yeah, now that you mention it-"
    show tony a_pipe_hold_shoulder with {'master': dissolve}
    anon "Haha, guys..."
    anon "... Next time, why don't you two crawl through the sewage drain and I'll wait outside for the signal?"
    pause
    show anon f_worried with {'master': dissolve}:
        xoffset 25
        xzoom 1
    anon "I tried my best to clean it off but all I had was a towe-"
    show harold a_gun_side_halt with dissolve
    pause
    harold "No, that's not it."
    show harold a_gun_down with {'master': dissolve}
    tony f_smirk "Although you do stink, champ."
    show anon f_unimpressed:
        xoffset -475
        xzoom -1
    show harold f_eyeroll
    with dissolve
    pause
    harold f_concerned "This is like, a strong chemical smell..."
    anon f_sad_down "Honestly, that could still be me..."
    anon "... There was an awful lot of mystery mush in that tunnel."
    show anon f_confused
    tony "Is it really a mystery though?"
    show harold:
        xoffset 300
        xzoom -1
    with {'master': dissolve}
    tony "I mean, it {i}was{/i} a sewage drain..."
    show anon f_disgusted
    hide harold
    with {'master': dissolve}
    tony "... It's a pretty safe assumption you were crawling through-"
    show anon b_punch f_shy_cringe m_talk:
        crop (0, 0, 1024, 768)
        xoffset -450
    show tony f_surprised_down
    with {'master': dissolve}
    anon "Stop!"
    show anon b_puke_hold -m_talk with dissolve
    pause
    show anon b_punch f_worried_high
    show tony f_normal_down
    with {'master': dissolve}
    anon "Please."
    anon "I don't wanna think about it."
    tony f_laugh "Heh!"
    show anon b_dressed f_disgusted:
        xoffset -475
    show tony f_smirk
    with {'master': dissolve}
    tony "Don't worry, champ."
    tony "It's nothin' a good shower won't fix."
    pause
    show tony f_sad_down with {'master': dissolve}
    tony "Eh, I wouldn't mention anything to {b}Maria{/b} about your little poopy adventure though..."
    anon f_thinking_down "Yeah, way ahead of you on that thought."
    tony f_laugh "Haha!"
    show anon f_normal with {'master': dissolve}:
        xoffset 25
        xzoom 1
    anon "{b}Maria{/b} is {b}Tony{/b}'s wife... I'm sure you remember her from the-"
    show tony f_normal
    anon f_surprised "{b}Harold{/b}?!"
    anon "Oh, crap... he's gone!"
    show anon b_dressed f_worried:
        xoffset -475
        xzoom -1
    show tony f_smirk
    with {'master': dissolve}
    tony f_smirk "Ah, we better hurry and catch up to him..."
    tony "... Don't want that putz gettin' in a scrap without us!"
    show anon with {'master': dissolve}:
        xoffset 25
        xzoom 1
    anon "Right."
    hide anon
    hide tony
    with {'master': dissolve}
    anon "{b}Harold{/b}, wait up!"

    scene expression background(224, 456, 4) as stage
    show harold a_gun_side b_tanktop f_surprised:
        xoffset 125
        xzoom -1
    with fade
    anon "There he is!"
    anon "{b}Harold{/b}?"
    show anon a_sides behind harold with {'master': dissolve}:
        xoffset -50
    anon "Hey, man... why'd you take off on us like-"
    anon f_shock "!!!"
    tony "Why are you guys stopping?"
    show tony a_pipe_hold_shoulder b_casual f_question behind harold with {'master': dissolve}:
        xoffset -250
        xzoom -1
    tony "What's the big-"
    show tony f_surprised m_talk
    pause

    scene location_warehouse_attack_cutscene23 with hpunch
    "..."
    tony "... Oh, shit."
    "..."
    anon "{i}*Gulp*{/i} They're all staring at us."
    tony "That's a lotta half-naked broads!"
    "..."
    anon "W-what do we do?!"
    tony "You're askin' me?"
    anon "I mean, shouldn't we like, help them... or something?"
    tony "Do they need help?"
    "..."

    scene expression background(224, 456, 4) as stage
    show anon f_worried:
        xoffset -540
        xzoom -1
    show tony a_pipe_hold_shoulder b_casual:
        xoffset -250
        xzoom -1
    show harold a_gun_side b_tanktop f_surprised:
        xoffset 125
        xzoom -1
    with fade
    anon "Well, I don't know, man... they're obviously being forced to work here against their will!"
    show anon:
        xoffset -50
        xzoom 1
    with {'master': dissolve}
    anon "We can't just leave them here, can we?"
    pause
    anon "{b}Harold{/b}, do something!"
    harold @ -m_talk "..."
    show anon_arms_dressed_a_surprised_up_both as arms behind harold:
        crop (250, 0, 774, 768)
        offset (250, -24)
    anon "{b}Harold{/b}!"
    show anon_arms_dressed_a_surprised_up_both as arms:
        linear .1 alpha 0
    show harold:
        ease .05 yoffset 10
        easein_bounce .25 yoffset 0
    show tony f_laugh
    harold "Huh?!"
    hide arms
    show harold f_concerned:
        xoffset -300
        xzoom 1
    show tony f_normal
    with {'master': dissolve}
    harold "What?"
    anon "Do something."
    harold f_embarrassed "R-right."
    show harold f_concerned with {'master': dissolve}:
        xoffset 125
        xzoom -1
    harold "{i}*Ahem*{/i} Ehh, I don't suppose any of you girls speak English, huh?"
    pause
    show svetlana f_concerned behind harold with {'master': dissolve}:
        xoffset -120
    svetlana "Da, I do."
    harold "Oh, good."
    show khadne f_concerned_down behind svetlana:
        xoffset 50
    show katya f_concerned_down:
        xoffset 175
    with {'master': dissolve}
    svetlana "Are you why all the shootings are happen?"
    pause
    svetlana "Where is Mikhail and Alexi?"
    show anon f_confused
    show harold f_suspicious
    show tony f_question
    tony "Michael and who?!"
    svetlana f_annoyed "Mikhail... and Alexi!"
    pause
    show harold f_concerned
    svetlana "The girls are needing food soon."
    show anon f_worried
    pause
    show svetlana a_point_back with {'master': dissolve}
    svetlana "And {b}Katya{/b} needs make use of toilet."
    show anon f_worried_left
    tony f_suspicious "I can't understand a word she's sayin'..."
    show anon f_worried_surprised
    show harold a_gun_side_stop:
        xoffset -375
        xzoom 1
    show svetlana a_idle
    show tony f_surprised
    with {'master': dissolve}
    harold "Shh, let me handle it."
    show anon f_worried
    show tony f_sad
    show svetlana a_crossed f_glaring
    with dissolve
    pause
    show harold a_gun_side f_concerned behind svetlana with {'master': dissolve}:
        xoffset 125
        xzoom -1
    harold "Ma'am, my name is {b}Harold{/b}."
    harold "This is {b}[firstname]{/b}."
    harold f_smirk "And the fat one with the bad manners is {b}Tony{/b}."
    show anon f_laugh
    show katya a_cover_mouth f_laugh
    show tony f_angry
    show svetlana f_laugh
    with {'master': dissolve}
    katya @ -m_talk "{i}*Snort*{/i}"
    show anon f_shy_left
    show katya f_happy
    show svetlana f_happy
    tony "Hey, who you callin' fat, baldy?!"
    show anon f_shy
    show katya a_idle
    with {'master': dissolve}
    harold f_normal "May I ask your name?"
    katya f_confused "What do they want?" (show_native="Chego oni khotyat?")
    show svetlana a_idle f_normal with {'master': dissolve}:
        xoffset 425
        xzoom -1
    svetlana "They want to know our names." (show_native="Oni khotyat uznat' nashi imena.")
    show khadne f_concerned_back
    show anon f_confused
    show tony f_sad
    katya "Why?" (show_native="Zachem?")
    khadne f_concerned "They are playing a trick on us." (show_native="Oni khotyat nas obmanut'.")
    katya f_concerned @ -m_talk "!!!"
    show khadne f_concerned_down
    katya "Let's just go back to working!" (show_native="Davayte luchshe vernomsya k rabote!")
    svetlana f_concerned "I don't think it's a trick..." (show_native="Ne dumayu, chto tut kakoy-to podvokh...")
    show katya f_concerned_down
    pause
    show svetlana with {'master': dissolve}:
        xoffset -120
        xzoom 1
    svetlana "I am called {b}Svetlana{/b}."
    show anon f_shy
    show tony f_question
    harold f_embarrassed "Okay, {b}Svetlana{/b}..."
    show svetlana f_normal
    harold "... It's nice to meet you."
    pause
    show svetlana a_point_back with {'master': dissolve}
    svetlana "This is {b}Katya{/b} and {b}Khadne{/b}."
    show khadne f_concerned
    anon f_confused "{b}Khadne{/b}?"
    show svetlana a_idle with {'master': dissolve}
    svetlana "Da."
    svetlana "She is Khakas."
    show khadne f_concerned_down
    anon "What does that mean?"
    pause
    svetlana "Is not important."
    pause
    svetlana f_curious "They sent you?"
    show tony f_suspicious
    harold f_suspicious @ -m_talk "Hmm?"
    harold "Who?"
    svetlana f_frowning "Crap." (show_native="Blyat.")
    svetlana f_concerned "How you say?"
    svetlana "Ehh, bad men..."
    show svetlana a_front
    with {'master': dissolve}
    svetlana "... Make us slave."
    anon "Your captors?"
    show anon f_shy
    show svetlana a_idle f_happy
    with {'master': dissolve}
    svetlana "Da."
    show harold f_normal
    svetlana f_concerned "Mikhail and Alexei."
    show tony f_normal
    pause
    svetlana f_happy "Captors."
    show anon f_shy_left
    show harold f_worried_right_up
    tony f_smirk "I wouldn't be too concerned about Mikhail and his girlfriend Alexei..."
    show tony a_pipe_point_back
    with {'master': dissolve}
    tony "... They're most likely bleedin' out on the floor of that warehouse back there."
    show anon f_shy
    show harold f_worried
    show svetlana a_point_front f_curious
    with {'master': dissolve}
    svetlana "You shoots them?"
    show anon f_shy_left
    show harold a_facepalm f_normal_closed
    show tony a_pipe_hold_shoulder
    with {'master': dissolve}
    tony "Oh, yeah... we shoots 'em alright."
    show svetlana a_sides f_surprised
    with {'master': dissolve}
    tony "Heh."
    show anon f_shy
    show harold a_gun_side f_worried
    with {'master': dissolve}
    svetlana "This is true?"
    harold "I'm afraid so."
    pause
    show svetlana f_smirk with {'master': dissolve}:
        xoffset 425
        xzoom -1
    svetlana "The fat one says the assholes are dead." (show_native="Tolstyak skazal, chto eti urody mertvy.")
    show katya a_cover_mouth f_surprised
    show khadne f_surprised
    with {'master': dissolve}
    katya "They killed them?!" (show_native="Oni ikh ubili?!")
    svetlana "It appears so." (show_native="Vykhodit, tak.")
    khadne f_confused "And now we belong to them?" (show_native="I teper' my prinadledzhim im?")
    katya f_concerned "We do?" (show_native="Neuzheli?")
    show katya a_idle
    with {'master': dissolve}
    katya "Is that what they said?!" (show_native="Oni tak i skazali?")
    show anon f_worried
    show tony f_sad
    show svetlana a_idle f_annoyed
    with {'master': dissolve}
    svetlana "If you will shut up for a second, I will ask them!" (show_native="Yesli vy zatknotes' na sekundu, to ya ikh sproshu!")
    show khadne f_concerned
    katya f_concerned_down "Y-yes, of course." (show_native="D-da, konechno.")
    katya "Sorry, {b}Svet{/b}." (show_native="Prosti, {b}Sveta{/b}")
    show svetlana f_concerned with {'master': dissolve}:
        xoffset -120
        xzoom 1
    svetlana "So we are to be working for you now?"
    show anon f_surprised
    show tony f_surprised
    harold f_surprised "What?!"
    harold "N-no, it's not like that."
    anon f_worried "We're here to rescue you!"
    show tony f_sad
    svetlana f_curious "Rescue?"
    show harold f_worried
    pause
    svetlana "What this mean, rescue?"
    harold f_embarrassed "It means we're setting you free."
    pause
    harold "Ehh, no more slavery."
    svetlana f_concerned "You send us back to Russia?"
    harold f_suspicious "Oh, umm... I suppose... if that's what you want?"
    svetlana f_annoyed "Of course is not what I want!"
    show harold f_surprised
    svetlana "They make slave of me in Russia!"
    show anon f_surprised_teeth
    harold "Whoa, I-"
    show anon f_worried
    harold "Y-you can always ask for asylum here in the United States..."
    harold f_normal "... I'm sure given the circumstances, it'll be granted."
    svetlana f_curious "I stay in America?"
    anon f_shy "Yes, if you'd like."
    pause
    svetlana f_happy "Da."
    svetlana "America is home of free and land of brave, yes?"
    tony f_normal "You're damn right it is."
    khadne f_confused "What are they saying now?" (show_native="A teper' chto oni govoryat?")
    show svetlana with {'master': dissolve}:
        xoffset 425
        xzoom -1
    svetlana "They say we are no longer slaves." (show_native="Chto my bol'she ne rabyni.")
    show khadne f_concerned
    katya f_surprised @ -m_talk "!!!"
    show khadne f_concerned_back
    katya "They are sending us home?!" (show_native="Nas otpravyat domoy?!")
    show khadne f_concerned
    svetlana f_annoyed "You would go back to the place that makes a slave of you?!" (show_native="Ty khochesh' obratno tuda, gde tebya prevratili v rabynyu?!")
    katya f_concerned @ -m_talk "..."
    khadne "What other choice do we have?" (show_native="A u nas yest' vybor?")
    svetlana f_happy "I will stay here, in America." (show_native="Ya ostanus' tut, v Amerike.")
    show khadne f_surprised
    katya f_surprised "We can do that?!" (show_native="A tak mozhno?!")
    svetlana "That's what they told me." (show_native="Oni tak skazali.")
    show katya f_normal
    khadne f_confused "Where will we live?" (show_native="I gde my budem zhit'?")
    show svetlana with {'master': dissolve}:
        xoffset -120
        xzoom 1
    svetlana "Da, we live where?"
    harold f_suspicious @ -m_talk "Hmm?"
    harold "Oh, umm..."
    harold f_normal "I don't know, actually... I mean, I'm sure we'll find you a temporary dwelling until something more permanent can be found."
    svetlana f_curious "Temporary?"
    svetlana "What this mean?"
    harold f_concerned "Oh, man... umm..."
    anon "We'll find you a place to live."
    show harold a_facepalm f_normal_closed
    show tony f_smirk
    with {'master': dissolve}
    svetlana "You?"
    anon "No, him."
    show harold a_gun_side f_worried
    with {'master': dissolve}
    harold "{i}*Sigh*{/i} Y-yeah, I'll see it gets taken care of."
    harold "Temporary lodgings until you girls learn English and find gainful employment."
    svetlana "Employ... ment?"
    anon "A job."
    anon "That pays you money."
    show svetlana f_normal:
        xoffset 425
        xzoom -1
    show tony f_normal
    with {'master': dissolve}
    svetlana "They will find us a work in America." (show_native="Nam podberut rabotu v Amerike.")
    show katya f_concerned
    khadne "So we {i}are{/i} to be slaves then?" (show_native="Znachit, my {i}ostanemsya{/i} rabynyami?")
    svetlana f_annoyed "No, stupid... work that pays!" (show_native="Net, dura... normal'nuyu rabotu, za kotoruyu platyat!")
    show katya a_cover_mouth f_surprised
    show khadne f_normal
    with {'master': dissolve}
    katya @ -m_talk "!!!"
    pause
    show katya a_idle f_happy
    show khadne f_normal_back
    show svetlana f_happy
    with {'master': dissolve}
    katya "We will be people again?" (show_native="S nami snova budut obrashchat'sya kak s lyud'mi?")
    show khadne f_normal
    show svetlana a_point_back
    with {'master': dissolve}
    svetlana "You should thank them."
    show anon f_surprised
    show harold f_surprised
    show katya b_bottom_run
    show svetlana behind harold
    with {'master': dissolve}
    harold "Whoa!!"
    hide katya
    show harold b_tanktop_hug f_surprised_down
    show svetlana a_sides:
        xoffset -120
        xzoom 1
    with {'master': dissolve}
    harold "O-okay..."
    show anon f_laugh
    show harold f_worried_right_up
    tony f_smirk "Aww, that's nice!"
    show anon f_normal
    show katya f_happy_high:
        xoffset -280
    show harold b_tanktop f_smirk_down
    with {'master': dissolve}
    katya "You are a wonderful men!" (show_native="Vy zamechatel'nyye lyudi!")
    pause
    show svetlana a_idle f_annoyed with {'master': dissolve}:
        xoffset 425
        xzoom -1
    svetlana "Well, don't just stand there you idiots!" (show_native="Ne stoyte stolbom, idiotki!")
    show harold f_smirk
    show khadne f_surprised
    svetlana "Let's show some gratitude to our saviors!" (show_native="Proyavim blagodarnost' nashim spasitelyam!")

    scene location_warehouse_attack_cutscene24 with fade
    tony "Now this is what I'm talkin' about!"
    tony "See champ, I told ya to start actin' like a man and good things would happen, didn't I?"
    anon "Y-yeah, you did."
    tony "That's right ladies..."
    tony "... Your heroes have arrived."
    anon "{i}*Gulp*{/i} H-hello."
    harold "This is getting a little out of hand, don't you think?"
    tony "Oh, relax cupcake and let the girls hug ya!"
    tony "You know, ya'd probably get a lot more of this kinda thing if you cops weren't so shit at your jobs all the time..."
    harold "Very funny."
    "..."
    harold "Aren't we kinda wasting time here?"
    harold "Your friends are still missing, ya know..."
    anon "Oh, crap... you're right!"
    anon "E-excuse me, ladies."

    scene expression background(712, 440, 2.5) as stage
    show svetlana a_crossed f_happy:
        xoffset -50
    with fade
    show anon a_sides f_worried with dissolve:
        xoffset 250
    anon "Hey, {b}Svetlana{/b}?"
    svetlana @ -m_talk "Hmm?"
    anon "I'm looking for my friends..."
    anon "... They were brought here earlier tonight by-"
    svetlana f_curious "American girls?"
    show harold a_gun_side b_tanktop f_concerned behind svetlana with {'master': dissolve}:
        xoffset -150
        xzoom -1
    anon "Yes."
    svetlana f_concerned "{b}Dimitri{/b} drag them to back room."
    show harold f_worried
    show svetlana a_point_front:
        xoffset 500
        xzoom -1
    with {'master': dissolve}
    svetlana "There."
    show anon a_point with {'master': dissolve}
    anon "You're sure?"
    show svetlana a_sides with {'master': dissolve}
    svetlana f_concerned_back "Da."
    svetlana f_concerned "{b}Dimitri{/b} always takes girls back there when he feels like playing his little games." (show_native="{b}Dmitriy{/b} chasto uvodit s soboy devushek, kogda khochet razvlech'sya.")
    show anon a_sides f_confused
    with {'master': dissolve}
    svetlana f_frowning "Most don't ever come back." (show_native="Bol'shinstvo ne vozvrashchalis'.")
    pause
    show anon:
        xoffset -250
        xzoom -1
    show harold f_concerned
    show svetlana f_timid
    with {'master': dissolve}
    pause
    anon f_annoyed "C'mon, {b}Tony{/b}!"
    tony "Alright, alright!"
    hide anon with {'master': dissolve}
    tony "Sorry, ladies... Daddy has more rescuin' to do."
    show harold f_normal with {'master': dissolve}:
        xoffset 210
    pause
    show svetlana a_crossed with {'master': dissolve}:
        xoffset -50
        xzoom 1
    harold "You should take your girls outside and wait for the cavalry to arrive."
    svetlana f_curious "Cavalry?"
    harold "Police officers."
    harold "They should be here any minute."
    svetlana f_annoyed "Outside?!"
    svetlana "Is cold!"
    harold f_embarrassed "I think I saw some fur coats back in the warehouse."
    harold "Take whatever you want, okay?"
    svetlana f_smirk "Da, we take."
    svetlana "Thank you, policeman."
    show harold f_concerned:
        xoffset -290
        xzoom 1
    show svetlana a_idle:
        xoffset -675
    with {'master': dissolve}
    svetlana "Come with me ladies!" (show_native="Damy, idom za mnoy!")
    show harold a_facepalm f_normal_closed
    show svetlana a_up
    with {'master': dissolve}
    svetlana "Let's take everything valuable from here!" (show_native="Davayte zaberom otsyuda vso tsennoye!")
    hide svetlana with dissolve
    pause
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
