label park_dewitt_douches_meet_up:
    scene expression player.location.background_closeup
    show eve f_happy zorder 1:
        xoffset -400
    show player 12 at left
    with dissolve
    player_name "Alright, I'm here. What's this idea you had?"
    show player 5
    eve "Well, we need help to clean the auditorium for the talent show, right?"
    show player 10
    player_name "Yeah."
    show player 5
    eve "Say hello to the help."
    show tyrone:
        xoffset -50
    show chad:
        xoffset 100
    with dissolve
    tyrone "What up, crackajack?"
    show player 12
    player_name "Whoa. You mean these guys are gonna help us clean?"
    show player 5
    chad @ a_open "That's right! What, you think just 'cause we gangsta, we can't do a little charity work from time to time?"
    show player 10
    player_name "Well no, I didn't mean-"
    show player 11
    tyrone "Good, 'cause you'd be right! Hahaha!"
    show player 12
    player_name "Okay, I'm officially confused."
    show player 5
    eve "Heh, they're gonna help us."
    eve "... But we'll have to do something for them too."
    show player 14
    player_name "Oh, I see."
    show player 12
    player_name "What do they want?"
    show player 5
    chad "You gotta {b}get us some forties{/b}, yo!"
    show player 10
    player_name "Eh, forties?"
    show player 5 with None
    show eve f_angry:
        flip
        xoffset 250
    with dissolve
    eve "No forties! I told you cans!"
    chad "Pssh, fine! Whatever."
    show eve f_happy:
        unflip
        xoffset -400
    with dissolve
    eve "They just want us to {b}get them some beer{/b}."
    show player 10
    player_name "What?! I'm not old enough to buy beer!"
    show player 5
    eve @ f_eyeroll "Well, yeah. I know that!"
    eve "Doesn't your buddy have some?"
    show player 12
    player_name "Huh?"
    show player 5
    eve f_confused "That guy with the karaoke machine! {b}Evan{/b}?"
    show player 12
    player_name "You mean {b}Erik{/b}?"
    show player 5
    eve f_happy @ f_laugh "Yeah, that guy!"
    eve "{b}He had a bunch of beer there at his place{/b}!"
    show player 37 with dissolve
    player_name "Ah, man."
    show player 38 with dissolve
    player_name "... They're gonna help us clean the entire thing, right?"
    show player 5 with dissolve
    tyrone "That's the idea, dummy."
    show player 4 with dissolve
    player_name "..."
    show player 12 with dissolve
    player_name "Fine, I'll see what I can do."
    player_name "I'll {b}meet you guys in the auditorium tomorrow{/b} for the cleanup!"
    show player 5
    eve "I'll make sure they hold up their end."
    hide eve
    hide chad
    hide tyrone
    with dissolve
    show player 10
    player_name "I should talk to {b}Erik{/b} about {b}taking some of Mr. Johnson's beer{/b}."
    return

label park_douches_intro:
    scene expression player.location.background_blur with None
    show anon f_worried at anon_versus
    show chad f_happy
    show chico f_cocky:
        chico_back
    show tyrone f_smirk:
        flip
        xoffset 200
    with dissolve
    tyrone "Man, you just all about them sleazy ass chickenheads, ain't ya?"
    chico "What can I say, I'm a simple man."
    tyrone "A simple man that's about to get the clap..."
    show chico f_normal
    chad @ f_laugh "Haha!!"
    chico "Nah, homie. She's clean."
    tyrone "Please."
    tyrone "I know that bitch and she's anything but clean!"
    chico @ -m_talk "..."
    tyrone "I wouldn't fuck her with {b}Chad{/b}'s dick..."
    chad @ f_laugh "Haha, yeah!"
    chad "He wouldn't even fuck her with my dick!"
    tyrone @ f_angry "Shut up, {b}Chad{/b}!"
    chad f_normal_down @ -m_talk "..."
    chico f_cocky "I'm just saying, the girl is talented."
    chico @ f_laugh "She had me cumming in like thirty seconds!"
    show chad f_happy
    tyrone "Heh, it ain't got nothin' to do with talent... That's experience, is what that is!"
    tyrone "She dun sucked half the dicks in town, man!"
    chico "Tsk, whatever..."
    pause
    anon @ a_wave "{i}*Ahem*{/i}"
    show tyrone f_angry with dissolve:
        unflip
        tyrone_front
    chico f_angry "Tch, what do you want, punk?"
    chad f_normal "Yeah, what do you want?!"
    tyrone "You come to hang out with the cool kids?"
    show tyrone f_smirk
    anon "No."
    anon "I want you guys to stop giving {b}Eve{/b} a hard time."
    tyrone "Oh, really?"
    chico f_cocky "Hah, look at him trying to be all hard."
    chad f_happy @ f_laugh "Haha!"
    anon f_tired "{i}*Sigh*{/i} Seriously, what's it gonna take to get you guys to back off?"
    tyrone @ f_normal "You want us to leave your little girlfriend alone?"
    tyrone @ a_point "You gotta beat us in a battle."
    anon f_worried a_up "Man, I'm not trying to fight you guys..."
    tyrone "I ain't talking about no fight!"
    tyrone @ f_laugh "Rap battles, beotch!"
    anon a_idle f_surprised @ a_behind_head "Rap battle?!"
    tyrone "Yeah, that's right!"
    show tyrone a_mic_throw
    show anon b_dressed_blocking
    with dissolve
    pause
    show tyrone a_idle
    show anon b_dressed f_sad_down
    with dissolve
    anon "!!!"
    show anon f_worried
    anon "Uhh, I dunno..."
    chico f_normal "Yo, c'mon homie, this fool don't know nothing about spittin' rhymes!"
    chad "For real dawg, this scrub can't rap."
    tyrone "Hold on now, he dun walked up in here like he's got big brass balls... I wanna see him back it up!"
    anon @ -m_talk "..."
    tyrone @ a_point "You ain't gonna puss out now, are ya?"
    anon f_skeptical "Fine, I'll battle you."
    show anon b_dressed_pickup with dissolve
    show chad f_happy
    chico @ f_eyeroll -m_talk "Tch."
    show anon f_worried b_dressed a_mic with dissolve
    tyrone "Heh, nah man... You ain't earned the right to battle me!"
    tyrone "You gotta get through my boys first."
    tyrone a_hands_rub @ a_point "I'm King Kong up in this bitch!"
    chad "Hah yeah, King fuckin' Kong!"
    tyrone a_idle f_angry "Man, shut the fuck up, {b}Chad{/b}."
    show chad f_normal_down
    tyrone "Shit."
    chad "Oh, my bad, dawg."
    anon @ f_skeptical "Alright then, who's first?"
    show chad f_happy
    show chico:
        chico_front
    show tyrone f_smirk behind chico:
        tyrone_back
    with dissolve
    chico f_angry @ a_signs "Yo, I'ma take care of this sorry motherfucker."
    tyrone "Haaaah, now that's what I'm talking about!"
    chico a_mic "Pay attention, bitch!"
    return

label park_douches_greet:
    scene expression player.location.background_blur with None
    show anon f_worried at anon_versus
    show chad
    show chico:
        chico_back
    show tyrone:
        tyrone_front
    with dissolve
    tyrone "Hey, look who's back."
    if player.stats.chr() > 6:
        tyrone "You ready to take on the big dawg?"
        chad "You're 'bout to get roasted, homie."
        anon "I'm ready."
    elif player.stats.chr() > 3:
        chad "Sup, dawg?"
        chad f_happy "You ready to battle?"
    else:
        chico "Man, not this fool again..."
        chad "You're wasting your time, dawg!"
    return

label park_douches_rematch_1:
    anon f_normal "I choose to Rap Battle!"
    tyrone f_smirk "That's what I'm talking 'bout!"
    tyrone "You ready for the rematch, {b}Chico{/b}?"
    show chico f_cocky:
        chico_front
    show tyrone behind chico:
        tyrone_back
    with dissolve
    chico a_mic "Piece of cake, homie."
    chico @ a_signs "This cracker ain't getting past me!"
    tyrone "Spin it!"
    return

label park_douches_rematch_2:
    anon "I choose to rap battle!"
    tyrone f_smirk "You're going up against {b}Chad{/b} now."
    show chad:
        chad_front
    show tyrone behind chad:
        tyrone_middle
    show chico behind chad
    with dissolve
    chad @ a_open "That's right, dawg!"
    chad "Prepare to feel the wrath of {b}Chad{/b}!"
    chico @ f_eyeroll "Eugh, fuckin' white boys..."
    tyrone @ f_laugh "Hahaha!"
    chad f_angry a_mic "Hit it!"
    return

label park_douches_rematch_3:
    anon "I choose to rap battle!"
    tyrone f_smirk "Let's get this shit started then!"
    tyrone "You might wanna take notes..."
    chad "Get him, {b}Tyrone{/b}!"
    tyrone a_mic "Spin it up!"
    return

label park_douches_rematch_4:
    anon "I choose to rap battle!"
    tyrone f_smirk "Let's get this shit started then!"
    tyrone "You might wanna-"
    show tyrone f_surprised
    anon "I'm going first this time."
    show tyrone f_smirk
    chad f_happy @ f_laugh a_open "Oh snap!"
    tyrone "Alright, if that's the way you want it."
    tyrone "Let's hear what you got."
    return

label park_douches_respect:
    scene expression player.location.background_blur with None
    show anon at anon_versus
    show chad f_happy
    show chico f_cocky:
        chico_back
    show tyrone:
        tyrone_front
    with dissolve
    tyrone "Yo, what up?"
    chico "Sup, homie?"
    tyrone f_smirk @ a_point "You here to battle?"
    anon @ f_laugh "Heh, nah."
    chad "Aww, c'mon dawg... You gotta defend that title!"
    anon "Maybe some other time."
    tyrone "Suit yourself."
    return

label park_douches_dismiss:
    if player.stats.chr() < 10:
        anon "Never mind."
        show tyrone f_normal
        chico f_angry "That's what I thought!"
        chico @ a_signs "Get lost, puta!"
        chad f_angry "Yeah, get lost!"
        hide anon with dissolve
    else:
        anon @ a_wave "I'll catch you guys later."
        tyrone "Alright, dawg."
        tyrone "Peace."
    return

label park_douches_battle_1:
    chico f_angry a_mic_speak "{i}You think you can stand up to me white bread?{/i}"
    chico "{i}We ain't even started and you already dead!{/i}"
    chico "{i}You come up in here, thinking you tough;{/i}"
    chico "{i}Let's hear it then, bitch, I'm calling your bluff!{/i}"
    chico f_cocky "{i}You ain't got no rhymes and now your ass is frying;{/i}"
    chico "{i}I'ma send you back home to yo mamma, crying!{/i}"
    show anon f_worried
    show tyrone f_smirk
    show chad f_happy
    show chico a_mic
    with dissolve
    chad "Oooh, dayum!"
    tyrone "Alright, alright... Pretty good, for a start."
    tyrone "You gotta top it now, you ready?"
    anon "Y-yeah, okay."
    tyrone "Spin that shit up!"
    return

label park_douches_battle_1_pass:
    show anon f_snarky a_mic_speak
    show chad f_normal
    show chico f_cocky
    show tyrone f_normal
    with fade
    anon "{i}Is that all you got {b}Chico{/b}, making fun of my race?{/i}"
    anon "{i}This ain't a battle for me, you can't even keep pace!{/i}"
    anon "{i}It's hard to listen to your words, when you dressed like a clown...{/i}"
    anon "{i}... And white bread here's 'bout to burn your ass down.{/i}"
    anon "{i}So run along home now, you sorry-ass skater...{/i}"
    anon "{i}... And tell your momma not to worry, I'll be coming 'round later.{/i}"
    show chad f_happy
    show chico f_angry
    show tyrone f_smirk
    show anon f_normal a_mic with dissolve
    chad @ f_laugh "HAHAHAAH!"
    tyrone "Not bad, white boi."
    chad "He totally got you, dawg!"
    chico "Man, shut up, {b}Chad{/b}!"
    chico "He just got lucky, is all..."
    tyrone "Nah, that was legit!"
    anon "Thanks man."
    tyrone "You still got a long way to go if you wanna challenge me but it's a start."
    tyrone "{b}Swing by another night and we'll go again{/b}."
    anon "Alright."
    hide anon with dissolve
    return

label park_douches_battle_2:
    chico f_angry a_mic_speak "{i}What you doing here, bitch? Ain't your ass had enough?{/i}"
    chico "{i}Better hold on to something, shit's 'bout to get rough.{/i}"
    chico "{i}This is our turf, fool and you can't hang with our brand.{/i}"
    chico "{i}My rhymes slicing so deep, that you can't even stand.{/i}"
    chico "{i}Dunno whatchu were thinking, in way over your head.{/i}"
    chico f_cocky "{i}Your pants filling with shit, man, I think it's time that you fled.{/i}"
    show anon f_worried
    show tyrone f_smirk
    show chad f_happy
    show chico a_mic with dissolve
    chad "Oooh, dayum!"
    tyrone "Alright, alright... Pretty good, for a start."
    tyrone "You gotta top it now, you ready?"
    anon "Y-yeah, okay."
    tyrone "Spin that shit up!"
    return

label park_douches_battle_2_pass:
    show anon f_snarky a_mic_speak
    show chad f_normal
    show chico f_cocky
    show tyrone f_normal
    with fade
    anon "{i}Hate to break it to you, dawg, but I'm here to stay.{/i}"
    anon "{i}So either learn to accept it or get out of my way!{/i}"
    anon "{i}You keep trying to spit these rhymes that cut deep...{/i}"
    anon "{i}... But all of your words come out simple and cheap.{/i}"
    anon "{i}Learn your place, {b}Chico{/b} quick and remember to bow.{/i}"
    show chad f_happy
    anon "{i}Recognize my skills, this is my park now.{/i}"
    show tyrone f_smirk
    show chico f_angry
    show anon f_normal a_mic with dissolve
    chad "Yo, that was lit!"
    tyrone "Not bad, white boi."
    chico "It was alright."
    tyrone "Nah, that was legit!"
    anon "Thanks man."
    tyrone "You still got a long way to go if you wanna challenge me but you're getting closer."
    tyrone "{b}Swing by another night and we'll go again{/b}."
    anon "Alright."
    hide anon with dissolve
    return

label park_douches_battle_3:
    chico f_angry a_mic_speak "{i}Oh, you think you're hot shit, 'cause you beat me twice?{/i}"
    chico "{i}What you don't realize is, I was just being nice.{/i}"
    chico "{i}But the gloves are off now and I'm ready to rumble.{/i}"
    chico "{i}When I put on some pressure, you'll do nothing but crumble.{/i}"
    chico "{i}So put up your dukes, bitch, and try not to balk.{/i}"
    chico f_cocky "{i}By the time I'm finished, your girl will be sucking my cock.{/i}"
    show anon f_worried
    show tyrone f_smirk
    show chico a_mic with dissolve
    chad f_happy @ f_laugh "Oooh, dayum!"
    tyrone "Alright, alright... Pretty good, for a start."
    tyrone "You gotta top it now, you ready?"
    anon "Y-yeah, okay."
    tyrone "Spin that shit up!"
    return

label park_douches_battle_3_pass:
    show anon f_snarky a_mic_speak
    show chad f_normal
    show chico f_cocky
    show tyrone f_normal
    with fade
    anon "{i}I didn't just beat you, I left you in shambles.{/i}"
    anon "{i}Spitting these rhymes that you just can't handle.{/i}"
    anon "{i}You think that you can scare me, bitch? Give it a whirl.{/i}"
    anon "{i}Keep on trying to fight me, but sorry, I don't hit girls.{/i}"
    anon "{i}Now look at you cower, coming undone at the seams...{/i}"
    anon "{i}You couldn't get with my girl, even in your wet dreams!{/i}"
    show chad f_happy
    show chico f_angry
    show tyrone f_smirk
    show anon f_normal a_mic with dissolve
    chad @ f_laugh "HAHAHAAH!"
    chico "Goddamnit..."
    tyrone "Heh, I think he's got your number {b}Chico{/b}."
    chico "Nah man, fuck that..."
    chico "I'ma get this coward next time!"
    tyrone "Pfft, if you say so..."
    tyrone "You still got a long way to go if you wanna challenge me but you're getting closer."
    tyrone "{b}Swing by another night and we'll go again{/b}."
    anon "Alright."
    hide anon with dissolve
    return

label park_douches_battle_4:
    chico f_angry a_mic_speak "{i}I'm sick of you, homie... I'ma smoke you tonight!{/i}"
    chico "{i}Roll you up with papers and set you alight!{/i}"
    chico "{i}These lyrics cut deep and my rap is 'bout to get gory!{/i}"
    chico "{i}Your little run here was cute but this is the end of that story.{/i}"
    chico "{i}You ain't getting past me, bitch! Put it out of your head.{/i}"
    chico "{i}Best you get on home now, before you wind up dead.{/i}"
    show anon f_worried
    show tyrone f_smirk
    show chico a_mic with dissolve
    chad f_happy "Oooh, dayum!"
    tyrone "Alright, alright... Pretty good, for a start."
    tyrone "You gotta top it now, you ready?"
    anon "Y-yeah, okay."
    tyrone "Spin that shit up!"
    return

label park_douches_battle_4_pass:
    show anon f_snarky a_mic_speak
    show chad f_normal
    show chico f_cocky
    show tyrone f_normal
    with fade
    anon "{i}Again with the threats? Seems all you want to do scrap...{/i}"
    anon "{i}But I guess that makes sense, because clearly you can't rap.{/i}"
    anon "{i}I'm glad this is over, I can't take one more peep...{/i}"
    anon "{i}Your rhymes are so bad that they put me to sleep!{/i}"
    anon "{i}You should be embarrassed, dawg. That's all I'm gonna say...{/i}"
    anon "{i}This wasn't a battle, it was child's play.{/i}"
    show chico f_angry
    show tyrone f_smirk
    show anon f_normal a_mic with dissolve
    chad f_happy @ f_laugh "HAHAHAAH!"
    chico "Yo, fuck you whitey!"
    tyrone f_normal "Hey, don't be like that..."
    tyrone "Take your L with some fucking dignity, man."
    chico "Tch, whatever..."
    tyrone f_smirk "{b}[firstname]{/b} is ready to move up the ranks!"
    tyrone "You still gotta get through {b}Chad{/b} before you can take me on..."
    chad "Yeah, you gotta get through me next, dawg!"
    tyrone "{b}Swing by another night and we'll go again{/b}."
    anon "Alright."
    hide anon with dissolve
    return

label park_douches_battle_5:
    chad f_angry a_mic_speak "{i}I know we just met, and you'll have my attention,{/i}"
    chad "{i}But please hold the line, while I break with convention.{/i}"
    show chad with dissolve:
        flip
        xoffset 260
    chad "{i}What happened {b}Chico{/b}? You oughta ended this dude,{/i}"
    show chico f_angry
    chad "{i}Know what? Never mind. Sit back, listen, get clued.{/i}"
    show chad with dissolve:
        unflip
        chad_front
    chad "{i}Thank you for holding, now please make it quick?{/i}"
    chad a_open "{i}Wait, what am I saying? Not interested. *Click!*{/i}"
    show tyrone f_smirk
    show chad f_happy a_idle with dissolve
    chico f_normal "Man, I dunno how you so good at rhymin', but you can't trash talk for shit..."
    tyrone "Relax, {b}Chico{/b}... He's just getting started."
    chico f_cocky "Pfft, whatever homie."
    tyrone f_normal "You gotta top it now, you ready?"
    anon "Y-yeah, okay."
    tyrone f_smirk "Spin that shit up!"
    return

label park_douches_battle_5_pass:
    show anon f_snarky a_mic_speak
    show chad f_normal
    show chico f_cocky
    show tyrone f_smirk
    with fade
    anon "{i}What's up with that skit? You a call center rep?{/i}"
    anon "{i}You know you're battling me, right? Okay? Yep?{/i}"
    anon "{i}Won't try to deny it, your rhyme game is strong,{/i}"
    anon "{i}I almost understand how these fools thought you belong.{/i}"
    anon "{i}But that trash-tier trash talk, I just can't condone.{/i}"
    anon "{i}Got a rebuke? Save it. Leave it after the tone.{/i}"
    show chico f_cocky
    show anon f_normal a_mic with dissolve
    chad a_crossed "Damn."
    tyrone "Alright, alright."
    chico "He got you, {b}Chad{/b}."
    tyrone "Yeah, it's pretty close but I'ma have to give the win to the new blood."
    chad f_normal_down a_idle @ a_open "Man, that's wack!"
    chico "You should be wiping the floor with him, homie..."
    chad "Yeah, I know..."
    chad "Tch, shit!"
    tyrone "{b}Swing by another night and we'll go again{/b}."
    anon "Alright."
    hide anon with dissolve
    return

label park_douches_battle_6:
    chad f_angry a_mic_speak "{i}School's back in session, now haul it to class,{/i}"
    chad "{i}You failin' harder than me, and I'm high on grass!{/i}"
    chad "{i}What's stolen your focus? What's on your mind?{/i}"
    chad "{i}Little blue riding hood and her disappointing behind?{/i}"
    chad "{i}Take a breath, look around, I think you might find,{/i}"
    chad "{i}Your hand's lockin' up, and you're startin' t' go blind!{/i}"
    show chad f_happy a_mic with dissolve
    chico f_cocky "Man, I dunno how you so good at rhymin' but you can't trash talk for shit..."
    tyrone "Relax, {b}Chico{/b}... He's just getting started."
    chico "Pfft, whatever homie."
    tyrone f_normal "You gotta top it now, you ready?"
    anon "Y-yeah, okay."
    tyrone f_smirk "Spin that shit up!"
    return

label park_douches_battle_6_pass:
    show anon f_snarky a_mic_speak
    show chad f_normal
    show chico f_cocky
    show tyrone f_smirk
    with fade
    anon "{i}Hearing that, I'm not sure, I'm the visually impaired,{/i}"
    anon "{i}But maybe neither are you, with the way that you stared.{/i}"
    anon "{i}Conflicting words and actions, your mind's a hot mess,{/i}"
    anon "{i}How you've made it this far in life, is anyone's guess.{/i}"
    anon "{i}And don't worry {b}Chad{/b}, of brain cells, I've plenty,{/i}"
    anon "{i}Oh shit, you're gonna be late, it's almost 4:20!{/i}"
    show chico f_cocky
    show anon f_normal a_mic with dissolve
    chad f_normal_down a_crossed "Damn."
    tyrone "Alright, alright."
    chico "Those were both shitty... If I'm being honest."
    show chad f_angry
    tyrone "Yeah, it's pretty close."
    tyrone "I'ma give the win to the new blood."
    chad f_normal a_idle @ a_open "Man, that's wack!"
    chico "You should be wiping the floor with him, homie..."
    chad f_normal_down "Yeah, I know..."
    chad "Tch, shit!"
    tyrone "{b}Swing by another night and we'll go again{/b}."
    anon "Alright."
    hide anon with dissolve
    return

label park_douches_battle_7:
    chad f_angry a_mic_speak "{i}I'm steppin' up the raps, you can't hold a candle,{/i}"
    chad "{i}Look at this fool, standin' there in his sandals.{/i}"
    chad "{i}It's proper depressing, you look stuck in a rut,{/i}"
    chad "{i}Alone, tragically pining, after Blue's butt.{/i}"
    chad "{i}If your face was less serious it might even be funny,{/i}"
    chad "{i}Right now this ain't fun, feels like kicking a bunny.{/i}"
    show chad f_happy a_mic with dissolve
    chico f_cocky "Man, I dunno how you so good at rhymin' but you can't trash talk for shit..."
    tyrone @ f_laugh "Hahaha!"
    chico "It's painful to watch this shit..."
    tyrone f_normal "You gotta top it now, you ready?"
    anon "Y-yeah, okay."
    tyrone f_smirk "Spin that shit up!"
    return

label park_douches_battle_7_pass:
    show anon f_snarky a_mic_speak
    show chad f_normal
    show chico f_cocky
    show tyrone f_smirk
    with fade
    anon "{i}{b}Chad{/b}, please. For all our sakes stop.{/i}"
    anon "{i}Here, let me humor you: hop, hop-hop.{/i}"
    anon "{i}I feel bad you can't chill, be more laissez-faire,{/i}"
    anon "{i}And drop this weird obsession with {b}Eve{/b}'s derrière.{/i}"
    anon "{i}And my sandals? Really? I thought you'd aim higher,{/i}"
    anon "{i}Than a desperate last stab at my seasonal attire.{/i}"
    anon "{i}So it's been fun in your class, shame your raps were bad,{/i}"
    anon "{i}I graduated this school, it's over, goodbye {b}Chad{/b}.{/i}"
    show chico f_cocky
    show anon f_normal a_mic with dissolve
    chad f_normal_down "Damn."
    tyrone "Alright, alright."
    chico "I can't take much more of this."
    tyrone "Yeah, I think it's time to bring out the big guns."
    tyrone "You're facing me next time, scrub!"
    chad f_happy @ a_open "Whoo, you in trouble now {b}[firstname]{/b}..."
    tyrone "{b}Swing by another night, and we'll get it started{/b}!"
    anon "Alright."
    hide anon with dissolve
    return

label park_douches_battle_8:
    tyrone f_angry a_mic_speak "{i}Stop where you are! Yo, freeze! Assume the position!{/i}"
    tyrone "{i}You bein' arrested, charged with undue ambition!{/i}"
    tyrone "{i}You lookin' to roll up, to chew through my crew?{/i}"
    tyrone @ f_smirk "{i}And all this you're doing, so we stop hasslin' Blue?{/i}"
    tyrone "{i}Mad respect dawg, but that shit ain't happ'nin',{/i}"
    tyrone "{i}This our park, and you not up to battlin'.{/i}"
    show chad f_happy
    show tyrone f_smirk a_mic with dissolve
    chico f_cocky "Dayum!"
    chad @ a_open "That was killer, dawg!"
    tyrone "You think you can top it?"
    anon "Y-yeah, okay."
    tyrone "Let's hear it!"
    return

label park_douches_battle_8_pass:
    show anon f_snarky a_mic_speak
    show chad f_normal
    show chico f_normal
    show tyrone f_smirk
    with fade
    anon "{i}I was expectin' the worst, hopin' for the best,{/i}"
    anon "{i}But that shit was a joke, color me: unimpressed.{/i}"
    anon "{i}{b}Chico{/b}? {b}Chad{/b}? What up? This guy's your leader?{/i}"
    anon "{i}What was the requirement? Giver and receiver?{/i}"
    anon "{i}This park's already mine, this battle's a stomp,{/i}"
    anon "{i}I'll leave you guys alone for your next three-way romp!{/i}"
    show chico f_cocky
    show chad f_happy
    show anon f_normal a_mic with dissolve
    chad @ a_open "Whoo!"
    chico "Alright, that was pretty good..."
    tyrone "Yeah, not bad at all, kid!"
    tyrone "I wanna hear more!"
    tyrone "{b}Swing by another night and we'll go again{/b}."
    anon "Alright."
    hide anon with dissolve
    return

label park_douches_battle_9:
    tyrone a_mic_speak "{i}Well shit, man. I misjudged you. I'll grant that concession,{/i}"
    tyrone f_angry "{i}But you out of your league, this ain't no poetry slam session.{/i}"
    tyrone "{i}That landlady's quite somethin', but she seems so alone,{/i}"
    tyrone f_smirk "{i}Think she'd be tempted to go down my bone?{/i}"
    tyrone "{i}And that chick that you live with? Yeah, she's got that look,{/i}"
    tyrone "{i}You know the one. You can be our own personal cuck.{/i}"
    tyrone "{i}Fry us up something nice, on a bright Saturday morn,{/i}"
    tyrone "{i}Then sit in the corner, and watch us make porn.{/i}"
    show chad f_happy
    show tyrone a_mic with dissolve
    chico f_cocky "Dayum!"
    chad "That was killer, dawg!"
    tyrone f_normal "You think you can top it?"
    anon "Y-yeah, okay."
    tyrone f_smirk "Let's hear it!"
    return

label park_douches_battle_9_pass:
    show anon f_snarky a_mic_speak
    show chad f_normal
    show chico f_normal
    show tyrone f_smirk
    with fade
    anon "{i}Feel my cold steel, you've left me lyrically triggered,{/i}"
    anon "{i}Whatever you were expectin', it ain't what you figured.{/i}"
    anon "{i}That feeling alone? Naw, dawg, that's you. You projectin',{/i}"
    anon "{i}Desperately not wantin' to feel what you're suspectin'.{/i}"
    anon "{i}That you sit here, in this park, day after day,{/i}"
    anon "{i}Fightin' ever so hard, to keep boredom at bay.{/i}"
    anon "{i}Tryin' not to succumb to that existential dread,{/i}"
    anon "{i}That you're alone, no one cares, that you're better off dead.{/i}"
    anon "{i}You wish you had even one person give a shit,{/i}"
    anon "{i}But is it any wonder when you act like this dick?{/i}"
    anon "{i}The jealously is palpable, hell it's goddamn stiflin',{/i}"
    anon "{i}Yet you unload at loved ones like it's jelly-filled triflin'.{/i}"
    anon "{i}This sad little trio, taunting others for kicks,{/i}"
    anon "{i}Stuck in stasis, all alone; the most tragic of cliques.{/i}"
    anon "{i}Never doing anything but hanging out in this park,{/i}"
    anon "{i}Wondering whatever to do with a future so stark.{/i}"
    pause
    anon "{i}The light's gone out, your mind's a gaping chasm,{/i}"
    anon "{i}Stood there, straight up unable to fathom.{/i}"
    anon "{i}Allow me to assist with a simple, \"Oh yes he did!\"{/i}"
    anon "{i}But hey, take it easy, nothin' personnel{#sic}, kid.{/i}"
    show chico f_cocky
    show anon f_normal a_mic with dissolve
    chad f_happy @ f_laugh "Whoo!"
    chico "Alright, that was pretty good..."
    tyrone "Yeah, not bad at all, kid!"
    tyrone "I wanna hear more!"
    tyrone "{b}Swing by another night and we'll go again{/b}."
    anon "Alright."
    hide anon with dissolve
    return

label park_douches_battle_10:

    return

label park_douches_battle_10_pass:
    show anon f_snarky a_mic_speak
    show chad
    show chico
    show tyrone f_smirk
    with fade
    anon "{i}I'ma stop you right there, it's clear that you're done.{/i}"
    anon "{i}You're straight outta raps, and I got a ton.{/i}"
    anon "{i}So I'll take your boat and sail to rap sea.{/i}"
    anon "{i}Undefeated and undisputed, the best MC.{/i}"
    anon "{i}I've defeated your crew and now you bow,{/i}"
    anon "{i}Look at me bitch, I'm the captain now.{/i}"
    show chad f_happy
    show chico f_cocky
    show anon f_normal a_mic with dissolve
    tyrone @ f_laugh "Hahaha!"
    tyrone "Alright, alright, you win..."
    chad "That was dope!"
    tyrone "Right?"
    tyrone "I like this kid."
    chico @ f_eyeroll "Man, he's aight..."
    tyrone "You can hang out with us whenever you want, you feel me?"
    anon "Do that mean you guys gonna leave my friend alone?"
    tyrone f_normal "Who?"
    pause
    tyrone a_hands_rub "Little blue riding hood?"
    chad @ f_laugh "Haha!"
    anon "Her name is {b}Eve{/b}..."
    tyrone f_smirk a_idle "Yeah, whatever man."
    tyrone "We'll leave your girl alone."
    anon "Good."
    tyrone "Just come by and spit some rhymes with us again sometime, alright?"
    anon "We'll see."
    hide anon with dissolve
    return

label park_douches_battle_fail:
    show anon f_sad_down
    show chad f_angry
    show chico f_cocky
    show tyrone f_smirk
    with fade
    anon "Crap."
    chico "Heh, pathetic."
    show anon f_worried
    chad "See, I knew this was a waste of time!"
    if player.stats.chr() < 7:
        show tyrone:
            tyrone_front
        show chad:
            chad_middle
        show chico behind tyrone:
            chico_back
        with dissolve
    tyrone @ a_point "That was some weak shit, man..."
    tyrone "You need to get up on out of here!"
    anon @ a_point_self "No, wait... Let me try again!"
    chico f_angry "You don't get no fucking redos in a rap battle man."
    chico "Get lost!"
    anon f_sad_down @ -m_talk "..."
    anon f_worried "Fine, but I'm coming back tomorrow!"
    tyrone f_normal "Tch, whatever man..."
    hide anon with dissolve
    return

label park_douches_eve_tuuku_with_douches_repeat:
    scene expression player.location.background_closeup with None
    show chad
    show chico:
        xoffset 100
    show tyrone:
        xoffset -125
    show anon f_worried:
        xoffset -100
    show tuuku f_confused a_hips:
        flip
        xoffset 100
    with dissolve
    tuuku "Lambs Bread?"
    tuuku "Super Sour?"
    tuuku "Purple Princess?"
    tuuku "L.A. Confidential?"
    chad "Yo, he's gotta be making this shit up!"
    tuuku "Martian Candy?"
    tuuku "Platinum Jack?"
    tuuku "White Diamond?"
    anon @ -m_talk "( I should probably focus on my part in this prank. )"
    anon @ -m_talk "( Now where are {b}their backpacks{/b} at? )"
    hide anon with dissolve
    return

label park_douches_eve_tuuku_with_douches_first:
    scene expression player.location.background_closeup with None
    show chad
    show chico:
        xoffset 100
    show tyrone f_smirk:
        xoffset -125
    show anon f_worried:
        xoffset -100
    show tuuku f_happy:
        flip
        xoffset 100
    with dissolve
    tuuku "You really need to branch out more fellas..."
    tyrone "Tsk, nah man."
    tyrone "You know I only smoke that Kryptonite OG!"
    chico "Yeah, that shit's the bomb!!!"
    tuuku "There's so many other strains though, and they all give you a different high!"
    tuuku "Don't you wanna try some Cherry Kush or Blue Haze?"
    chad "Is it really blue?"
    tuuku f_confused @ -m_talk "Hmm?"
    chad "You said Blue Haze... Is it really blue?"
    tuuku "What, like the color?"
    chad "Yeah?"
    show tyrone f_angry:
        flip
        xoffset 300
    with dissolve
    show tuuku f_happy
    tyrone @ a_point "Man, of course it ain't blue!"
    tyrone "The fuck is wrong with you?!"
    chad f_angry "Man, how am I supposed to know?!"
    show tyrone:
        unflip
        xoffset -150
    tyrone "What else you got?"
    show chad f_normal
    tuuku "Hmm, Cali Gold?"
    tyrone "Ahh, hell no."
    tyrone "That shit gave me the squirts last time."
    show tuuku f_laugh
    chad @ f_normal_down "Pfft, I'm pretty sure that was the burrito you got at the gas station, dawg."
    tyrone "Man, shut up!"
    tuuku f_confused "Bullrider?"
    tyrone f_normal "Nah."
    tuuku "Exodus?"
    tyrone "Nuh uh."
    show anon f_surprised
    tuuku "Asian Fantasy?"
    chico "Jesus, how many strains you got?!"
    tuuku "Grape Ape?"
    tuuku "Flaming Dragon?"
    tuuku "Lemon Skunk?"
    chad @ f_laugh "Hahaha!"
    anon f_worried @ -m_talk "( I should probably focus on my part in this prank. )"
    anon @ -m_talk "( Now where are {b}their backpacks{/b} at? )"
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
