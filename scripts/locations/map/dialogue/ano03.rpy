label ano03_init_town_map:
    scene location_mugging_cutscene01 with fade
    anon "Man, it's a scorcher today..."
    anon "... Thank goodness for that ocean breeze."
    pause

    scene location_mugging_cutscene02
    anon "!!!" with hpunch

    scene location_mugging_cutscene03 with fade
    anon "W-what the-"
    dimitri "Well, hello there."
    dimitri "Little bunny."
    pause

    scene location_mugging_closeup
    show anon f_surprised_teeth a_sides
    show igor:
        xoffset -100
    show dimitri f_grin:
        xoffset 100
    with fade
    dimitri "This bad day for you, I think."
    show anon with dissolve:
        xoffset -50
    anon f_worried "I-"
    dimitri "{b}Igor{/b}."
    dimitri "Have you met little bunny yet?"
    igor f_curious "He doesn't look like bunny..."
    dimitri @ f_eyeroll "Tsk, don't ruin moment."
    dimitri f_normal a_point "I'm doing bit here."
    igor "Bunny is furry, {b}Dimitri{/b}..."
    igor a_bunny "... With big ears and bush tail."
    dimitri a_idle @ a_out "I know what bunny is, idiot!"
    dimitri "Just go and hold the boy!"
    igor a_idle "Y-yes, {b}Dimitri{/b}."
    igor @ a_point "No funny business or I break you in half, understand?"
    anon "P-please, I didn't do anything..."
    show igor a_hold_mc behind anon:
        xoffset -300
    show anon b_empty f_choked_shock:
        xoffset -300
    anon "!!!" with hpunch
    pause
    show anon f_choked_surprised_teeth
    dimitri "Yes, this is true."
    dimitri f_grin "You do nothing."
    dimitri "I tell you to give nice lady message, did I not?"
    show dimitri with dissolve:
        xoffset 50
    dimitri f_normal "We want."
    show dimitri with dissolve:
        xoffset 0
    dimitri "Our money."
    dimitri "Back."
    anon @ f_choked_shock "!!!"
    dimitri "Not half."
    dimitri "Not quarter."
    dimitri f_angry "WE WANT ALL OF IT!"
    anon f_choked_hurt @ -m_talk "..."
    dimitri "DO YOU HEAR ME?!"
    anon f_choked_hurt @ f_choked_shock "Y-yes!"
    dimitri "TALK LOUDER, LITTLE BUNNY!"
    anon f_choked_surprised_teeth @ f_choked_shock "YES!!!"
    pause
    show igor f_grin
    dimitri "See {b}Igor{/b}, I tell you..."
    dimitri a_talk "Yip, yip, yip!"
    dimitri "Just like his papa."
    show dimitri a_idle with dissolve
    igor @ f_laugh "You're right, {b}Dimitri{/b}."
    igor "Little bunny is good name for him."
    igor "We should make him hop for us."
    pause
    igor "You want I should feed you a carrot little bunny?"
    anon f_choked_hurt @ -m_talk "..."
    dimitri "Alright, enough funny business!"
    dimitri "Search him."
    igor "Yes, {b}Dimitri{/b}."
    show igor a_hold_mc_pocket with dissolve
    anon f_choked_surprised_teeth "!!!"
    pause
    igor a_hold_mc_pocket "Oh, look what I find!"
    dimitri "How much?"
    if player.has_money(1):
        show igor a_hold_mc_money
    else:
        show igor a_hold_mc
    with dissolve
    igor f_curious "Ehh."
    show anon f_choked_hurt
    pause
    igor f_disgust_down "Looks like not so much..."
    if player.has_money(1):
        dimitri f_angry "Tsk, give it here."
        show igor a_hold_mc
        show dimitri a_money_count
        with dissolve
    dimitri "Next time I ask {b}Raz{/b} to give me someone who can count past ten!"
    show igor f_angry:
        flip
        xoffset 0
    show anon:
        flip
        xoffset 0
    with dissolve
    igor "Hey, shaddup!"
    igor "I can count past ten!"
    dimitri "Not with your shoes on, you can't..."
    igor "That's not-"
    show igor f_curious
    pause
    igor "Ehh, I don't get it."
    dimitri "Because you need toes to count past ten..."
    igor @ -m_talk "..."
    dimitri f_eyeroll "Ugh, never mind."
    dimitri f_angry "Is this all you have?"
    anon @ f_choked_shock "Y-yes."
    igor "He lies!"
    igor f_disgust_down a_hold_mc_pocket "There something else in here."
    pause
    anon f_choked_surprised_teeth "!!!" with hpunch
    igor "What is this, huh?"
    igor "Feels like big roll of monies..."
    anon @ f_choked_shock "T-that's my-"
    igor f_curious "Hmm, is kind of squishy..."
    anon @ f_choked_shock "M-my-"
    dimitri f_normal "{b}Igor{/b}, are you grabbing his dick right now?"
    igor f_normal "Ehh?"
    pause
    anon @ f_choked_shock "You are!"
    show anon b_punch f_hurt behind igor:
        xoffset -250
    show igor a_hand_look f_disgust_down
    show dimitri
    with dissolve
    igor "Eugh!"
    show anon a_sides b_dressed f_surprised_teeth with dissolve
    pause
    dimitri f_grin @ f_laugh "Hahahaah!!!"
    dimitri @ a_point "Gaaaaaaaay."
    igor f_angry a_fist "Shaddup!"
    igor "I'm not gay."
    igor a_hand_look f_disgust_down "{i}*Sigh*{/i} Give me hand sanitizer."
    dimitri "We don't have time for hand sanitizer..."
    igor f_angry "There is always time for hand sanitizer!"
    igor a_hand_show "I have dick on my hand, {b}Dimitri{/b}!"
    dimitri f_angry "We are in middle of work!"
    igor "Arrghh!"
    dimitri "Don't be such baby."
    igor a_idle "I am not baby!"
    pause
    igor "You're baby."
    dimitri f_angry "What you say?!"
    igor f_normal @ f_normal_closed "N-nothing."
    dimitri "That's right, nothing!"
    dimitri "Focus on the job!"
    dimitri f_thinking "Now, where were we?"
    igor "Ehh, \"break something\"... I think?"
    dimitri f_grin "Ahh, yes."
    dimitri "We must break something."
    anon @ f_shock "You don't have to do that..."
    dimitri f_thinking "But what to break?"
    pause
    dimitri f_normal "Which hand is little bunny's favorite hand?"
    anon f_hurt @ f_shock "P-please?"
    dimitri f_grin "You no have answer?"
    dimitri "We break both then."
    dimitri f_normal "Nice lady must know we mean business."
    dimitri a_out "Give us rest of money."
    dimitri "No more-"

    scene location_mugging_cutscene04
    show text _ ("{i}*SCCCRREEEEEEEECH*{/i}") as caption
    with fade
    pause
    hide caption with dissolve
    show text _ ("I was so terrified that I didn't even hear the van pull up.") as caption with dissolve
    pause

    scene location_mugging_cutscene05
    show text _ ("{b}Tony{/b} might not have looked like a hero...") as caption
    with fade
    pause
    hide caption with dissolve
    show text _ ("... But he was definitely mine that day.") as caption with dissolve
    pause

    scene location_mugging_closeup
    show anon f_surprised a_sides
    show igor:
        flip
        xoffset 300
    show dimitri:
        flip
        xoffset -150
    show tony f_angry b_casual:
        xoffset 150
    with fade
    tony "What the hell is going on here?"
    show anon f_worried
    dimitri "Nothing that concerns you."
    dimitri "Go back to your pizza deliveries."
    tony f_normal @ f_laugh "Haah!"
    tony "I recognize that shitty accent."
    tony "From Russia with love, huh?"
    tony "{b}Raz{/b} must be real hard up if he's got you out here shaking kids down for their lunch money..."
    dimitri "I said this does not concern you, fat boy!"
    dimitri "Drive away now or things get ugly."
    tony @ -m_talk "Hmm."
    tony "You don't know who I am, do ya?"
    show tony a_unbutton1 with dissolve
    dimitri "I don't care who you are!"
    dimitri "We'll make you corpse if you don't-"
    show tony a_unbutton2 with dissolve
    dimitri "!!!"
    pause
    tony @ -m_talk "Mmhmm."
    tony "Know who I am now, dontcha?"
    dimitri "You don't want to be involved in this..."
    tony "Heh, you think yer a scary guy, huh?"
    tony "Let me tell you something..."
    tony f_angry a_idle "You don't know scary."
    tony "I've seen things that would make you curl up in a ball and cry 'til yer eyes bleed."
    dimitri @ -m_talk "..."
    tony "Maybe you'd like me to show you a couple of these things, huh?"
    igor f_curious "I do not wish to see these things, {b}Dimitri{/b}..."
    dimitri "Shut up, idiot!"
    igor f_normal "You want I should punch him?"
    dimitri "No."
    pause
    dimitri "We go now."
    dimitri "Inform {b}Raz{/b} of our new friend here, meddling in our affairs."
    tony f_normal "Yeah, you do that."
    tony "Tell him I said hello."
    dimitri "This isn't over, fat boy."
    hide dimitri
    hide igor
    with dissolve
    show tony a_wave with dissolve:
        flip
        xoffset 450
    tony "Das vidania, bitches."
    pause
    show tony f_suspicious -a_wave with dissolve:
        unflip
        xoffset 150
    tony "You alright, kiddo?"
    show anon a_rub with dissolve
    anon "Y-yeah."
    tony "What the hell do those dirty Ruskies want with you?"
    anon "I uhh, they seem to be under the impression that my father stole from them..."
    tony "Huh."
    tony "Did he?"
    anon "I don't know, sir."
    tony "Well, he was real fuckin' stupid if he did."
    tony "Those guys are animals!"
    tony "They'll snuff your entire family out, and they won't bat an eye doin' it neither."
    anon @ -m_talk "..."
    tony "You better tell your old man to give it back and take his medicine."
    tony "Maybe he'll still be capable of feedin' himself when they're done."
    anon f_sad_down "M-my dad is dead..."
    tony f_sad "Tsk, aww shit."
    tony "I'm sorry, kid."
    pause
    tony "They're putting the screws on you and your mama now, huh?"
    anon f_worried "Y-yeah, the lady that takes care of me."
    tony "{i}*Sigh*{/i} Christ... that's rough."
    pause
    anon "C-could I... ask who you are?"
    anon "Those guys crapped their pants when you showed them that tattoo."
    tony f_normal "Haha, they did, didn't they?"
    tony @ f_laugh "Hahahaha!"
    pause
    tony "Ahh, who I am is not important."
    tony @ a_point "For now, just call me {b}Tony{/b}, capisce?"
    anon "Yeah, okay."
    pause
    anon f_normal "Thank you, for your help {b}Tony{/b}."
    anon "Is there anything I can do to repay you?"
    tony "Heh, you wanna repay me, huh?"
    pause
    tony "What's ya name?"
    anon "{b}[firstname]{/b}."
    tony "Well, {b}[firstname]{/b}... you got a job?"
    anon f_worried @ a_behind_head "Not really."
    tony "I own a little pizza joint, just down the road."
    tony "Why don't you swing by tomorrow, and we'll talk some more, yeah?"
    anon f_normal "Okay, sure."
    tony "Good."
    tony "Now run along home, huh?"
    tony "I got work to do."
    anon @ a_wave "Thanks again."
    tony "Ehh, get out of here!"
    hide anon with dissolve
    show tony f_smirk
    pause
    tony "Heh, nice kid."

    $ player.go_to(L_home_entrance)
    scene expression player.location.background_blur
    show jenny f_upset a_hips:
        flip
        xoffset -50
    with fade
    show anon b_dressed_catch_breath with dissolve:
        flip
        xoffset 100
    anon "Haah... Haah..."
    jenny "What the heck is wrong with you?"
    anon "Where's... {b}[deb_name]{/b}?"
    jenny "How should I know?"
    jenny "{b}[deb_name]{/b}!!!"
    debbie "Yes, dear?"
    jenny "{b}[firstname]{/b} needs you!"
    show debbie f_sad behind jenny with dissolve:
        flip
        xoffset 250
    debbie "What's the matter?"
    show anon b_dressed f_worried o_neck_bruise with dissolve
    anon "You are not going to believe what just happened!"
    jenny "What, did you just find out the pathetic virgin convention is coming to town or something?"
    debbie "{i}*Gasp*{/i} What happened to your neck?"
    show jenny f_surprised
    show debbie f_surprised
    anon "Those goons stopped me while I was walking home today."
    debbie a_mouth_shock "Oh my god!"
    show debbie b_robe_hug_mc:
        xoffset 100
    show anon b_empty f_worried o_empty
    show jenny f_sad
    debbie "A-are you okay?"
    anon "Yeah, I'm fine {b}[deb_name]{/b}."
    pause
    show anon b_dressed o_neck_bruise:
        flip
    show debbie b_robe f_sad a_front:
        xoffset 250
    with dissolve
    anon "I mean, they took a bunch of money off me..."
    anon "... And threatened to break my hands."
    show debbie f_surprised a_mouth_shock with dissolve
    jenny "Holy shit."
    jenny "Seriously?"
    anon f_normal "Yeah, but then this big Italian guy showed up out of nowhere, and I don't know who he was, but he scared those Russians away real quick!"
    anon @ f_laugh "It was amazing!!"
    jenny "Russians?"
    anon "Oh, yeah... I found out they're Russian."
    anon "And they work for someone named {b}Raz{/b}."
    debbie a_nervous f_sad @ -m_talk "..."
    jenny f_gross "{b}[deb_name]{/b}?"
    jenny f_concerned "Are you alright?"
    debbie "{i}*Sniff*{/i} I can't believe they-"
    anon "The Italian guy wants to see me tomorrow at his pizza restaurant!"
    anon "I think he wants to offer me a job."
    jenny f_grin "Pfft, you're going to be a pizza delivery boy?"
    anon "What's wrong with that?"
    jenny @ f_eyeroll "Nothing, it's perfect for you..."
    anon f_unimpressed "Ugh, just-"
    anon "Shut up and listen, will you?"
    jenny a_idle f_angry_pouting @ -m_talk "..."
    anon f_normal "The point is, maybe this guy can help us!"
    anon "I mean, those Russians were really terrified of him!"
    jenny f_upset "Which means he's probably an even bigger criminal than they are..."
    anon f_worried "Oh..."
    anon "... I didn't think about that."
    jenny @ f_eyeroll "Of course you didn't..."
    anon "What do you think, {b}[deb_name]{/b}?"
    debbie f_crying_closed "Those bastards lied to me..."
    anon "{b}[deb_name]{/b}?"
    show jenny f_concerned
    anon "What's going on with you?"
    debbie "{i}*Sniff*{/i} I-"
    pause
    debbie a_facepalm "I paid them."
    jenny "You what?!"
    anon "Y-you couldn't have paid them..."
    jenny f_upset "Weren't they asking you for a million dollars?!"
    jenny a_hips "We don't have that kind of money!"
    debbie a_front f_sad "N-no, I-"
    debbie "I offered them two hundred and fifty thousand..."
    anon f_shock "!!!" with hpunch
    jenny f_surprised "!!!"
    pause
    jenny "We don't have that kind of money either!!!"
    show jenny f_concerned
    anon f_worried "How could you?"
    show debbie f_crying_closed a_facepalm with dissolve
    anon "The police told you specifically not to do that!"
    debbie "Y-yeah, but-"
    debbie "{i}*Sniff*{/i} They just keep calling and then the threats... and now-"
    pause
    debbie f_sad "I just wanted to keep you kids safe."
    debbie a_front "They said they would give me more time."
    debbie "That they would leave you two out of it."
    anon "{b}[deb_name]{/b}..."
    show debbie b_robe_hug_mc:
        xoffset 100
    show anon b_empty f_worried o_empty
    with dissolve
    pause
    jenny f_upset a_idle "Where did you get the money?"
    pause
    jenny "{b}[deb_name]{/b}?!"
    show debbie b_robe:
        xoffset 250
    show anon b_dressed o_neck_bruise
    with dissolve
    debbie "I took out a loan."
    anon @ -m_talk "..."
    jenny "They don't just give out two-hundred-and-fifty-thousand-dollar loans to recently widowed women with no jobs..."
    debbie "I-"
    debbie f_crying_closed "{i}*Sniff*{/i}"
    debbie "I used the house as collateral."
    jenny f_surprised "!!!"
    jenny "You put up the house?!?!"
    show debbie a_facepalm with dissolve
    anon @ -m_talk "..."
    jenny "You can't just-"
    pause
    jenny f_upset "We're gonna lose it!"
    debbie f_sad a_front "No."
    jenny @ f_eyeroll "We'll be living on the street in three months time."
    debbie "It's not going to come to that."
    jenny f_angry "Yes, it is!!"
    jenny "What, you think the bank isn't gonna come collect?!"
    debbie @ a_facepalm "I'll figure something out."
    jenny f_upset @ f_eyeroll "Yeah, right."
    jenny "Unbelievable."
    hide jenny with dissolve
    debbie "{i}*Sniff*{/i}"
    debbie "I'm so sorry, sweetie."
    debbie "Please, don't hate me."
    show debbie b_robe_hug_mc:
        xoffset 100
    show anon b_empty f_worried o_empty
    with dissolve
    anon "I don't hate you, {b}[deb_name]{/b}..."
    pause
    anon "We'll sort it out."
    debbie "I'm so stupid."
    anon "You're not stupid."
    debbie "Yes, I am."
    anon "I'm going to find a way to fix this."
    pause
    debbie "Ungh, I think I'm gonna be sick..."
    show debbie b_robe f_crying_closed a_facepalm:
        xoffset 250
    show anon b_dressed o_neck_bruise
    with dissolve
    anon "{b}[deb_name]{/b}?"
    debbie "What are we gonna do, {b}[firstname]{/b}?"
    anon "Okay, you're looking really pale..."
    anon "I think maybe you should go lay down."
    anon @ a_point_back "C'mon, let's get you to bed."
    hide debbie
    hide anon
    with dissolve
    debbie "I'm so sorry..."
    anon "Shh, it's alright, {b}[deb_name]{/b}."

    $ game.timer.tick(3)
    $ player.go_to(L_home_bedroom)
    scene expression player.location.background_blur with fade
    show anon f_tired o_neck_bruise with dissolve:
        xoffset 300
    anon @ -m_talk "( Man, what a crap day. )"
    anon @ -m_talk "( {b}[deb_name]{/b} finally fell asleep. )"
    anon @ -m_talk "( I've never seen her like that before... )"
    pause
    anon @ -m_talk "( I don't know what we're gonna do, those Russians are really making things hard on us and now we owe two hundred and fifty thousand dollars to the bank! )"
    anon @ -m_talk "( We've gotta come up with that money, or we lose the house. )"
    pause
    anon @ -m_talk "( {i}*Sigh*{/i} What the heck are we gonna do? )"
    pause
    anon @ -m_talk "( The only glimmer of hope right now is {b}Tony{/b}... I should definitely go and see him tomorrow. )"
    pause
    anon @ -m_talk "( Maybe I can {b}talk to someone down at the bank{/b} too? )"
    anon @ -m_talk "( It's worth a try. )"
    pause
    show anon f_yawn a_yawn with dissolve
    pause
    anon f_tired a_sides @ -m_talk "( Whatever, I'm too tired to think. )"
    anon @ -m_talk "( I'll sort it out tomorrow. )"
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
