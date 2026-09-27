label tattoo_parlor_bedroom_eve_clients_wake_up_grace:
    scene expression player.location.background_blur with None
    show anon f_worried with dissolve
    grace "Mm."

    anon "H-hello?"

    anon @ -m_talk "!!!"
    scene expression "backgrounds/location_tattoo_bedroom_cutscene05a.jpg" with fade
    grace "Nnnghh!"

    anon "{b}G-Grace{/b}?!"

    scene expression "backgrounds/location_tattoo_bedroom_cutscene05b.jpg" with fade
    grace "!!!" with hpunch
    grace "Apa yang-"

    scene expression player.location.background_blur with None
    show anon f_worried a_cover_boner3
    show grace b_shirt f_surprised a_shy zorder 1:
        xoffset 100
    with dissolve
    grace "{b}[firstname]{/b}?!"

    anon "I'm so sorry, I didn't mean-"

    grace "W-what are you doing here?"

    anon "I came to check on {b}Eve{/b} and {b}Odette{/b} told me to come up here and wake you guys..."

    eve "Hmm?"

    show eve b_pajamas f_tired zorder 0:
        xoffset -200
    with dissolve
    eve "{i}*Yawn*{/i} W-what's going on?"

    show grace f_sad_down
    anon f_shock a_behind_head "T-tidak ada apa-apa!"

    anon f_worried "aku tidak-"

    grace f_normal a_idle @ a_point "{b}[firstname]{/b} was worried about you and stopped by to say hello."

    eve f_happy @ f_laugh "Benar-benar?"

    anon "Y-ya?"

    eve "Aduh!"

    show anon f_surprised_down a_hug_eve_pajamas
    hide eve
    with dissolve
    eve "Manis sekali!"

    anon f_shy_down "Bagaimana perasaanmu?"

    show anon f_normal a_idle
    show eve b_pajamas f_happy:
        xoffset -200
    with dissolve
    with dissolve
    eve @ f_laugh "Really, really, REALLY hungover... Hehe!"

    show grace f_eyeroll
    anon "hehe."

    show grace f_tired
    eve "I think I just need a shower and I'll be right as rain."

    grace "Well, you'll have to get in line."

    grace "I'm going first."

    eve f_surprised_right "Apa?!"

    eve "Mustahil!"

    grace "Yes, way."

    show eve f_sad_right
    grace "I've got a business to run."

    grace f_sad_down "At least for the next few weeks, anyways..."

    show anon f_worried
    show eve f_sad
    hide grace with dissolve
    eve "Just don't use all the hot water!"

    anon "What did she mean by that?"

    eve "Oh, we haven't been getting many customers lately, and she's worried about money..."

    anon "Benar-benar?"

    eve f_sad_down "Ya."

    eve "She told me last night that she's thinking of picking up a second job."

    anon "B-but she works so much already!"

    eve f_sad "I know, I told her it's ridiculous..."

    eve "If anything, I should be getting a job and giving her money, but she refuses to let me help out!"

    anon "{i}*Sigh*{/i} There has to be something we can do?"

    eve "Not that I can think of..."

    anon f_thinking a_thinking @ -m_talk "Hmm."

    pause
    anon "She just needs more customers, right?"

    eve "Ya, saya kira."

    anon f_normal a_idle "What if we advertised a bit?"

    eve @ -m_talk "Hmm?"

    anon "Yeah, we could make some flyers for {b}Sugar Tats{/b} and hang them up around town."

    eve f_surprised "!!!"
    eve f_eyeroll a_wipe_tears "Oh my god, why didn't I think of that?!"

    hide eve with dissolve
    anon "So, it's a good idea?"

    eve "It's brilliant, {b}[firstname]{/b}!"

    show eve b_pajamas a_artpad f_happy with dissolve
    eve "C'mon, let's go in the living room and work on it while she's showering."

    anon "Baiklah."

    scene black with dissolve
    pause
    $ player.go_to(L_tattooparlor_apartment)
    scene expression player.location.background_blur with None
    show anon f_looking_down
    show eve b_pajamas a_artpad_show f_normal_down:
        xoffset -250
    with dissolve
    eve "Alright, I think we're really on to something here."

    eve "Bukan begitu?"

    show expression 'objects/closeup_artpad_01.png' as closeup with fade
    pause
    hide closeup with None
    show eve f_normal
    anon f_normal "Y-yeah, it looks really good."

    anon "Will your sister be okay giving people twenty percent off though?"

    eve "Hey, eighty percent is better than zero, which is pretty close to how many customers she's had recently..."

    anon "Saya harap Anda benar."

    eve a_artpad "Percayalah kepadaku."

    show grace with dissolve
    grace "Oh my god, I feel so much better!"

    grace "It's all yours, butthead."

    eve f_normal_right "Sudah waktunya!"

    eve "What were you, in there playing with yourself or something?!"

    grace f_tired @ f_surprised a_neck "T-tidak!"

    grace "I'm just moving slow because I was up all night taking care of SOMEBODY who can't hold their liquor..."

    eve @ f_laugh "Hehe, touché."

    eve f_normal "Alright, lemme hop in the shower, and then we'll make copies and start hanging them."

    anon "Tentu saja."

    grace f_suspicious "Apa yang sedang kamu kerjakan?"

    show anon f_worried
    eve f_surprised_right "N-nothing, just-"

    anon @ -m_talk "..."
    eve f_normal_right "... Something for school."

    grace "Oh?"

    eve "Yeah, I'll tell you about it later."

    hide eve with dissolve
    grace f_normal "Baiklah."

    pause
    grace f_sad "She's not in trouble or anything, is she?"

    anon f_normal "Tidak."

    grace @ f_eyeroll "Terima kasih Tuhan."

    grace "I don't think I could handle anything else."

    show grace f_sad_down
    pause
    grace f_uneasy a_neck "H-hey, about earlier..."

    anon f_surprised @ -m_talk "Hmm?"

    grace "You know, that thing I was doing... When you walked into {b}Eve{/b}'s bedroom?"

    anon f_worried a_behind_head "O-oh, don't worry about it."

    grace f_disgusted @ f_weary "No, no, I feel like I should explain..."

    grace "It wasn't anything weird or nothing."

    grace "aku hanya-"

    grace a_facepalm f_weary "It's been a while, since the last time I-"

    anon @ -m_talk "..."
    grace "I mean, I haven't dated anybody in a long time and I'm just a little, umm..."

    grace "Sexually frustrated, I guess."

    anon f_surprised "Seriously, it's cool."

    show grace f_uneasy a_neck with dissolve
    anon f_worried @ f_surprised "I'm not judging, believe me."

    grace "{b}Eve{/b} was out like a light and I just, sorta... Lost my head, you know?"

    anon "Y-yeah, I get it."

    grace "Just umm... Don't tell her about it, please."

    anon "saya tidak akan melakukannya."

    grace f_surprised a_sides @ a_idea "Oh god, don't tell {b}Odette{/b} either!"

    grace "If she finds out, I'll never hear the end of it..."

    anon "Saya berjanji."

    grace f_uneasy "Okay, phew."

    grace "Terima kasih, {b}[firstname]{/b}."

    anon "No, problem."

    grace a_idle f_normal "You wanna help me set up the shop while you wait on my sister?"

    anon "Tentu."

    grace @ f_laugh "Luar biasa!"

    grace "Just follow me downstairs."

    hide grace with dissolve
    pause
    anon f_sad_down a_facepalm "Tepat di belakangmu."

    scene black with dissolve
    pause
    $ player.go_to(L_tattooparlor_interior)
    scene expression player.location.background_blur
    show odette zorder 1:
        xoffset 100
    with None
    show anon:
        xoffset -100
    show grace f_surprised zorder 0:
        xoffset -150
    with dissolve
    odette "Well, good morning, sunshine!"

    grace f_surprised_back "You already set everything up?"

    odette "Yeah, call it an attempt to get back into your good graces after last night."

    grace f_tired a_crossed "Hmm!"

    show anon f_looking_down a_phone with dissolve
    grace f_tired_back "I can't believe you brought that fireball whiskey out!"

    odette f_normal "Oh c'mon, we were having so much fun..."

    grace "Yeah, until {b}Eve{/b} got sick!"

    grace "Then I had to babysit her for half the night and hold her hair while she puked her guts out!"

    odette f_sad a_sides "Ya, tapi-"

    grace "You always take things too far, {b}Odette{/b}!"

    odette "I'm sorry, okay?"

    odette @ a_shrug "I was just trying to get you out of this funk you've been in lately."

    grace "I'm not in a funk, {b}Odette{/b}..."

    grace "I don't need release, I need someone helping me!"

    odette @ f_eyeroll "You need to get laid..."

    show anon f_surprised
    grace f_angry_back "Goddamnit, don't start-"

    grace f_weary a_facepalm "{i}*Huh*{/i}"

    show anon f_surprised_low
    pause
    grace a_idle f_uneasy_back "Look, I appreciate you helping me this morning... Thank you for that."

    show anon f_worried_low
    odette @ -m_talk "..."
    grace "Now can we please just talk about something else?"

    odette f_sad "Yeah, fine."

    pause
    odette f_normal "You have a client scheduled in about one hour... After that, the day is empty."

    grace f_sad_back @ f_surprised_back "Christ, I hope we get some walk-ins!"

    odette "Yeah, this place has been dead recently."

    show eve a_artpad f_happy_right:
        flip
        xoffset 200
    with dissolve
    show anon a_idle f_normal with dissolve
    show grace f_normal
    eve "Itu dia!"

    eve "I was worried you'd left."

    anon "Nope, I was just helping your sister open the shop."

    eve f_disgusted "Thanks for the cold shower, by the way!"

    grace f_sexy "Call it payback for cleaning up your vomit last night."

    odette @ f_laugh "Haha!"

    eve @ f_eyeroll "Ugh, terserah."

    odette f_smirk "Next time just shower together."

    show anon f_surprised
    eve f_surprised "APA?!"

    show grace f_eyeroll
    odette "Then everyone gets hot water."

    show anon f_thinking a_thinking with dissolve
    show grace f_normal
    eve f_disgusted "Eww, gross!"

    odette f_shy "How is that gross?"

    eve "Umm, because she's my sister..."

    odette @ f_eyeroll a_shrug "Jadi?"

    odette @ a_point "You're just washing in there, right?"

    show grace f_sad_down
    odette f_smirk "It's not like I'm telling you to have sex with each other..."

    show anon f_flirt_grin a_idle with dissolve
    grace f_tired_back "Just drop it, {b}Odette{/b}."

    odette @ f_eyeroll "Sheesh, you two are so repressed!"

    show grace f_normal
    show anon f_normal
    eve f_angry "I am not repressed!"

    odette @ a_mock "Silakan."

    eve f_normal @ f_eyeroll "Apa pun."

    eve "{b}[firstname]{/b} and I are {b}heading to the mall{/b} to make some copies of something."

    odette a_idle "Oh, new drawing?"

    odette "Lemme see."

    eve "N-no, it's not a drawing..."

    grace @ f_suspicious "So what is it then?"

    eve f_happy @ f_laugh "It's a surprise."

    eve "You'll find out soon!"

    hide eve with dissolve
    eve "Ayo, {b}[firstname]{/b}!"

    show anon:
        flip
        xoffset -550
    with dissolve
    pause
    hide anon
    show anon f_worried:
        xoffset -100
    with dissolve
    anon @ a_wave "Ehh, I guess I'll see you later?"

    odette "Nanti, kawan."

    grace "Sampai jumpa, {b}[firstname]{/b}."

    hide anon with dissolve
    pause
    grace f_tired_back "I wish you'd quit calling him that!"

    odette @ f_eyeroll "Psh, you wanna see it just as much as I do, don't try and deny it!"

    grace f_angry_back @ a_upset "Diam!"

    scene black with dissolve
    pause
    $ player.go_to(L_tattooparlor)
    scene expression player.location.background_blur with None
    show anon
    show eve
    with dissolve
    anon "So, you wanna hit {b}the mall{/b}?"

    eve "Yup, we can make some copies and then hang a few there."

    anon "Kedengarannya bagus."

    hide anon
    hide eve
    with dissolve
    return

label tattoo_parlor_bedroom_eve_pot_cheerup:
    scene expression "backgrounds/location_tattoo_bedroom_cutscene03.jpg"
    anon "{b}Malam{/b}?"

    anon "Are you in here?"

    pause
    eve "{b}[firstname]{/b}?"

    scene expression player.location.background_blur with None
    show anon f_worried
    show eve b_pajamas f_sad_down a_wipe_tears
    eve "W-what are you doing here?"

    show eve f_sad a_idle
    anon "You didn't show up for school today..."

    anon "I was worried about you."

    eve "Oh."

    eve "Y-yeah, I started getting ready this morning and then... I..."

    anon "Apakah kamu baik-baik saja?"

    eve "{i}*Sniff*{/i} Y-yeah..."

    pause
    eve "I mean, I dunno..."

    pause
    eve "{i}*Sniff*{/i} No."

    anon "Apa yang terjadi?"

    eve "aku hanya-"

    pause
    eve a_hide "I screwed up really bad this time..."

    anon @ f_surprised_teeth "!!!"
    eve "{i}*Sniff*{/i} I'm such a fucking idiot and..."

    eve "... And now a bunch of people's lives are ruined and my sister is even further in debt!"

    anon "Hey c'mon, don't say stuff like that."

    eve o_tears a_cover "Kenapa tidak?"

    eve "{i}*Sniff*{/i} It's true!"

    show eve o_empty f_cry_down a_wipe_tears with dissolve
    pause
    show eve f_sad_down a_idle with dissolve
    anon f_thinking a_thinking "Okay, well first off, you're one of the smartest people I know..."

    anon f_worried a_idle "What happened the other night was just bad luck, that's all."

    pause
    anon f_normal "Secondly, nobody's life is ruined..."

    anon "I had to pay a little fine and {b}Ronda{/b} just got an earful from her dad..."

    eve f_sad "{i}*Sniff*{/i} R-really?"

    anon "Ya."

    anon "I mean, she can't jog in the park anymore but honestly, I think you did her a favor!"

    anon @ f_laugh "That girl is insane with all the exercising!"

    eve @ f_laugh "Hehe!"

    anon "Seriously, it's WAY too much!"

    show eve f_cry_down a_wipe_tears with dissolve
    anon "She needs to get a hobby or something..."

    eve f_nervous a_idle "Benar?"

    pause
    eve f_sad "{i}*Sniff*{/i} So you aren't mad at me?"

    anon "Tentu saja tidak!"

    anon "I was having a great time, before we stumbled into the cops!"

    eve f_nervous "Hehe, aku juga."

    pause
    anon @ f_brag_closed "Ah, itu mengingatkanku..."

    anon "You missed {b}Chad{/b} getting run out of school today!"

    eve f_surprised "Apa?!"

    anon "{b}Mrs. Smith{/b} and {b}Annie{/b} chased him out for stinking up the place!"

    anon "{b}Ronda{/b} and I watched the entire thing, it was hilarious."

    eve "They all still stink?!"

    show eve f_nervous
    anon @ f_laugh "Hehe, ya."

    anon "{b}Mrs. Smith{/b} was gagging, he smelled so bad!"

    eve f_laugh "Ha ha ha!"

    eve "Man, I wish I could have seen that..."

    show eve f_nervous
    anon "Ya, aku juga."

    pause
    show anon f_shy_down
    eve f_nervous_down @ a_wipe_tears "{i}*Mengendus*{/i}"

    anon f_shy "S-so, did you know {b}Odette{/b} is calling us Bonnie and Clyde now?"

    eve f_nervous @ f_eyeroll "Ugh, yeah... Sorry about that, she thinks she's funny..."

    anon f_normal "Hehe, tidak apa-apa."

    anon "It's kinda cool actually!"

    eve "Menurutmu begitu?"

    anon "Ya!"

    anon "I mean, c'mon, the most famous criminal couple in history!"

    anon "I'd look pretty dapper in a pinstripe suit holding a tommy gun, don't you think?"

    eve "Hah, yeah maybe..."

    eve "Not sure I could pull off the dress though."

    anon @ f_brag_closed "Oh, you totally could!"

    eve "Menurutmu?"

    anon "Tentu saja!"

    pause
    anon "But I have to warn you now... I'll be worthless in a gunfight."

    eve "Hmm, I guess I'll just have to protect you then, huh?"

    anon "Ya, tolong!"

    eve f_laugh "Ha ha ha!"

    anon @ f_laugh "Ha ha ha!"

    pause
    eve f_nervous "Man, I've been in here depressed all day and you cheered me up in minutes..."

    anon "That's a good thing, right?"

    hide eve
    show anon a_hug_eve_pajamas f_surprised_down
    anon "!!!"
    pause
    eve "Terima kasih, {b}[firstname]{/b}."

    show anon f_shy_down
    anon "Terima kasih kembali."

    pause
    anon @ -m_talk "( Wow, she smells really good! )"

    eve "You always know how to make me smile..."

    anon "I like making you smile."

    anon f_surprised_down @ -m_talk "( Uh oh, I'm starting to get hard again! )"

    pause
    eve "Uhh, {b}[firstname]{/b}?"

    eve "Is your phone in your pocket?"

    eve "'Cause something is poking me..."

    show eve b_pajamas f_confused
    show anon o_boner a_cover_boner f_surprised
    show expression "characters/anon/anon_arms_dressed_a_cover_boner.png"
    with dissolve
    anon "Uhh, yeah... Sorry about that!"

    show anon f_shy
    anon "Oh shoot, look at the time!"

    eve "Apakah kamu baik-baik saja?"

    anon "Y-yeah, totally... I just really should be getting home for dinner..."

    anon "I'll see you at school, okay?"

    eve "Wait a second... Was that your-"

    hide anon
    hide expression "characters/anon/anon_arms_dressed_a_cover_boner.png"
    with dissolve
    anon "Tell {b}Grace{/b} and {b}Odette{/b} bye for me, okay?!"

    eve f_sad_down "You don't have to-"

    scene black with fade
    pause
    $ player.go_to(L_tattooparlor)
    scene expression player.location.background_blur with None
    show anon o_boner a_cover_boner f_hurt
    show expression "characters/anon/anon_arms_dressed_a_cover_boner.png"
    with dissolve
    anon @ -m_talk "( Oh my god, why does this keep happening to me?! )"

    anon @ -m_talk "( It's like the stupid thing has a mind of its own! )"

    anon @ -m_talk "( Man, I hope she didn't notice... )"

    hide anon
    hide expression "characters/anon/anon_arms_dressed_a_cover_boner.png"
    with dissolve
    return

label tattoo_parlor_bedroom_eve_bathroom_break:
    scene expression player.location.background_blur with None
    show anon f_worried o_boner a_cover_boner
    show expression "characters/anon/anon_arms_dressed_a_cover_boner.png"
    with dissolve
    anon "{b}Malam{/b}?"

    anon "A-are you in here?"

    pause
    hide expression "characters/anon/anon_arms_dressed_a_cover_boner.png"
    show anon a_thinking f_thinking -m_talk
    anon "( Hmm, no answer... )"

    $ player.go_to(L_tattooparlor_bedroom)
    scene expression player.location.background_blur with None
    show anon f_worried o_boner a_cover_boner
    show expression "characters/anon/anon_arms_dressed_a_cover_boner.png"
    with dissolve
    anon "H-hello?"

    pause
    anon f_skeptical @ -m_talk "( Where the heck is she? )"

    hide anon
    hide expression "characters/anon/anon_arms_dressed_a_cover_boner.png"
    with dissolve
    return

label tattoo_parlor_bedroom_eve_visit_bedroom:
    scene expression player.location.background_blur with None
    show eve f_nervous
    show anon
    with dissolve
    eve "Here it is."

    anon @ f_surprised "Wow, that is a lot of band posters!"

    eve f_nervous_down "Y-yeah, I know... I get kind of obsessive when it comes to my music."

    anon f_normal "Tidak ada yang salah dengan itu."

    eve f_surprised "K-menurutmu?"

    anon @ f_laugh "Tentu saja!"

    anon "Who doesn't like music?"

    eve f_nervous "Yeah, I suppose you're right about that..."

    anon f_normal_high "What kind of bands are those?"

    eve "Punk and Grunge, mostly."

    anon f_normal "Ah, so you like rock music?"

    eve @ f_laugh "I LOVE rock music!"

    eve f_happy "{b}Grace{/b} and {b}Odette{/b} turned me onto it when I was little."

    anon "Heh, so all three of you like it, huh?"

    eve "Ya!"

    eve "{b}Grace{/b} is more into Classic Rock and {b}Odette{/b} prefers Gothic and Metal, but we listen to pretty much everything when we're together."

    anon "That's really cool, {b}Eve{/b}!"

    anon "Do you ever go to concerts or anything?"

    eve f_nervous "Mm, not really... I mean, I'd like to..."

    eve f_sad_down "... {b}Grace{/b} used to go all the time but since our parents died... We can't really afford it."

    anon f_worried "Itu menyebalkan!"

    eve "Ya."

    pause
    anon f_normal "Maybe you and I can go to one sometime?"

    eve f_surprised "!!!"
    eve "You'd really wanna go, with ME?"

    anon "Well, sure!"

    anon "I think that'd be fun!"

    eve f_happy "Y-yeah, okay!"

    eve @ f_laugh "I'd like that a lot!"

    pause
    show eve f_nervous
    pause
    show anon f_shy a_behind_head with dissolve
    show eve f_nervous_down
    pause
    show anon a_idle with dissolve
    anon "So, ehh... What else do you do around here?"

    eve f_nervous "Mmm, I dunno... I guess, I play video games sometimes..."

    anon f_surprised "You do?!"

    eve "Y-yeah, a little bit."

    anon f_normal "Luar biasa!"

    show eve f_surprised
    anon "What games do you have?!"

    eve f_nervous_down "Ehh, mostly girly stuff... You probably wouldn't-"

    show anon f_surprised_teeth_down
    pause
    show eve f_confused
    anon f_surprised "Is that {i}Street Kombat{/i}?!"

    show anon b_dressed_pickup with dissolve
    eve @ -m_talk "Hmm?"

    show anon b_dressed a_game1 f_surprised_low
    eve f_surprised "Y-yeah... Do you play?!"

    anon f_laugh "Apakah kamu bercanda?"

    anon "It's one of my favorites!"

    eve f_happy "Whoa, okay... We have to play, like right now!"

    anon f_flirt "You're on!"

    eve f_laugh "hehe!"


    scene location_tattoo_bedroom_cutscene01
    with fade
    anon "... Holy crap!"

    anon "I thought you only played a little bit?"

    anon "You are on an entirely different level than I am..."

    eve "Heh, yeah... I play quite a lot actually."

    anon "I can see that!"

    eve "You are so predictable with those fireballs, {b}[firstname]{/b}..."

    anon "What fireballs, I can't even get off the ground!"

    eve "Hehehe!!"

    pause
    eve "You really need to work on your footsies!"

    anon "What's a footsies?"

    eve "... Are you serious?"

    anon "..."
    eve "Haha, alright... Don't worry, I'll teach you!"


    scene location_tattoo_bedroom_cutscene02
    show text _ ("We spent the rest of the evening playing, with {b}Eve{/b} showing me all the tricks.\nShe was incredible!") as caption
    with fade
    pause
    hide caption with dissolve
    show text _ ("Even with her help and hours of playing, I never came close to beating her!") as caption with dissolve
    pause
    hide caption with dissolve
    show text _ ("I'm pretty sure she was taking it easy on me too...") as caption with dissolve
    pause
    scene expression player.location.background_closeup
    show eve b_sidebed f_happy a_controller:
        flip
        xoffset 400
    show anon b_sit a_controller
    with fade
    anon "What is that, 80-0?"

    eve @ f_laugh "Hehe, you're getting better though!"

    anon "Ya benar..."

    eve "C'mon, try a different character."

    eve "Balzog or Hondo maybe, they're super defensive and easy to learn..."

    anon "Ugh, I don't think that's going to he-"

    odette "What's going on in here?!" with hpunch
    show eve f_surprised_right
    anon f_surprised_left "!!!"
    scene expression player.location.background_blur with None
    show anon f_worried:
        flip
        xoffset -150
    show eve f_hood_remove a_facepalm zorder 1
    show odette f_smirk:
        flip
    with fade
    odette "You two had better put your pants back-"

    pause
    odette f_sad "Oh."

    show odette f_angry
    show eve f_angry a_hip with dissolve
    eve "{b}Odette{/b}, what the hell?!"

    odette "You're just sitting in here playing video games?"

    eve "Ya!!"

    odette f_eyeroll "Well, that's a let down..."

    show odette f_smirk
    anon @ -m_talk "..."
    eve "Apakah kamu menginginkan sesuatu?"

    odette "Hehe, your sister wanted me to tell you that it's getting late."

    odette "You should come help us close up, so your sister can get a decent night's sleep for once..."

    anon f_skeptical "Jam berapa sekarang?"

    odette "Almost eleven."

    anon f_surprised "Oh, crap... Really?!"

    show anon f_worried
    odette "Ya."

    eve f_nervous "We completely lost track of time."

    anon f_shy_left "Ya."

    anon "I should get home, {b}[deb_name]{/b} is probably worried about me."

    hide anon
    show anon:
        xoffset 300
    anon "Thanks for inviting me over, it was fun!"

    eve f_happy "Yeah, it was!"

    anon "See ya at school?"

    eve "Tentu saja!"

    hide anon
    show anon zorder 0:
        flip
        xoffset -150
    anon "Nice meeting you."

    odette "Mmhmm, come back soon, handsome!"

    anon f_shy "Hehe."

    hide anon with dissolve
    pause
    odette "So, you know he wants to hit it, right?"

    show eve f_surprised
    eve "Apa?!"

    eve f_sad "N-no he doesn't!"

    odette @ f_eyeroll "Girl, please..."

    eve "We're just friends, {b}Odette{/b}!"

    odette "Lie to yourself all you want but you can't fool me."

    pause
    odette "C'mon, let's go help your sister."

    hide odette
    hide eve
    with dissolve
    return

label tattoo_parlor_bedroom_pantie_collection:
    scene expression player.location.background_blur with None
    if player.location.is_here(M_eve) or (player.location.is_here(M_grace) and not M_eve.pregnancy.character_bedridden):
        show anon f_surprised with dissolve
        anon @ -m_talk "( I better not, she's right there! )"

    else:
        show anon f_shy_down a_panties_eve1 with dissolve
        anon @ -m_talk "( These are {b}Eve{/b}'s panties. )"

        anon @ -m_talk "( These certainly share her unique style... )"

        pause
        if M_somrak.finished_state(S_somrak_start):
            anon f_grin "( I bet {b}Master Somrak{/b} would like these. )"

            $ player.get_item("eve_panties")
        else:
            anon f_shy_down @ -m_talk "( I should hang them back where I found them. )"

        hide anon with dissolve
    $ game.main()
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
