label tony_button_pizzeria:
    if game.timer.is_day():
        show anon with dissolve:
            flip
        if randomizer() > 75:
            show tony a_fists
        elif randomizer() > 50:
            show tony a_frustrated
        elif randomizer() > 25:
            show tony a_wave
        else:
            show tony a_point
        with dissolve
        if M_anon.finished_state(S_ano11_bone):
            tony "'Ey, there's my guy!"
            show anon f_grin
            tony a_idle "How ya doin', champ?!"
        else:
            tony "'Ey there, champ!"
            show anon f_grin
            tony a_idle "You ready to deliver some pizza?"
        show anon f_normal
    else:
        show anon with dissolve
        if M_anon.finished_state(S_ano11_bone) and not M_maria.pregnancy:
            tony "'Ey there, champ!"
            tony "If you're lookin' for {b}Maria{/b}, she's in the store room."
        else:
            tony "You're still here?"
            tony "You should head on home."

    label tony_button_pizzeria.choice:
    if M_anon.finished_state(S_ano11_bone):
        menu:
            "Lockbox." if M_anon.is_state(S_ano14_tony):
                jump ano14_tony_tony_lockbox

            "Order pizza." if game.timer.is_day():
                jump tony_dialogue_order

            "Need help?" if game.timer.is_dark():
                jump tony_button_pizzeria.help
            "Your tattoo?":

                jump tony_button_pizzeria.tattoo

            "{b}Maria{/b} around?" if game.timer.is_day():
                jump tony_button_pizzeria.curious

            "{b}Maria{/b} around?" if game.timer.is_dark() and M_maria.pregnancy.stage > 4:
                jump tony_button_pizzeria.babies
            "How did you and {b}Maria{/b} meet?":

                jump tony_button_pizzeria.maria

            "I should go." if game.timer.is_day():
                pass

            "Just checking in." if game.timer.is_dark():
                pass
    else:

        menu:
            "You bet!" if game.timer.is_day():
                jump tony_button_pizzeria.deliver

            "Order pizza." if game.timer.is_day():
                jump tony_dialogue_order

            "Need help?" if game.timer.is_dark():
                jump tony_button_pizzeria.help

            "Italian Mafia." if M_anon.finished_state(S_ano06_cook):
                jump tony_button_pizzeria.italians

            "Your tattoo?" if not M_anon.finished_state(S_ano06_cook):
                jump tony_button_pizzeria.tattoo
            "The Russians.":

                jump tony_button_pizzeria.russians

            "How did you and {b}Maria{/b} meet?" if M_maria.met:
                jump tony_button_pizzeria.maria

            "Adoption?" if M_anon.between_states(S_ano08_work, S_ano10_tony):
                jump tony_button_pizzeria.adoption

            "Any information yet?" if M_anon.between_states(S_ano08_work, S_ano10_tony):
                jump tony_button_pizzeria.info

            "I should go." if game.timer.is_day():
                pass

            "Good night." if game.timer.is_dark():
                pass

    if game.timer.is_day():
        if M_anon.finished_state(S_ano11_bone):
            anon f_normal "I should go."
            tony f_normal "Ahh, alright, champ."
            anon "I'll see you later?"
            tony "You bet."
        else:
            anon f_normal "Actually, I have a few other things I need to take care of right now..."
            tony f_normal "What, you're leaving?"
            anon "Y-yeah, but I'll be back real soon."
            anon "I promise."
            tony "Tsk, make it quick, will ya?"
            tony @ f_laugh a_belly "These pizzas are gettin' cold!"
            anon "Yes, sir!"
    else:
        if M_anon.finished_state(S_ano11_bone):
            anon f_normal "Just checking in."
            tony f_normal "No need to worry about me."
            tony "Get on home to your ma, eh?"
            tony "I'll see ya tomorrow."
        else:
            anon f_normal @ a_wave "Good night."
            tony f_normal a_idle @ a_wave "See you tomorrow, champ."

    hide anon with dissolve
    return


label tony_button_pizzeria.adoption:
    anon f_normal "So, you're thinking about adoption?"
    tony f_suspicious @ f_eyeroll a_frustrated "Oh great, now you're gonna start bustin' my balls about adoption too?"
    anon @ f_worried "No, I just think {b}Tina{/b} made some decent points..."
    anon "You would know exactly what they're going through."
    tony f_sad "Yeah, I dunno about that..."
    tony "I'm sure the system has changed quite a bit over these past thirty years..."
    tony "... And even if it hasn't, it don't change the fact that I'd rather raise {b}Maria{/b}'s kids than some stranger's I never met."
    pause
    tony "Maybe that makes me a bad person but it's how I feel."
    anon "No, it doesn't make you a bad person, {b}Tony{/b}."
    pause
    anon @ f_confused "So you'd rather go the sperm bank route?"
    tony "Yeah but {b}Maria{/b} don't wanna hear nothin' about it."
    pause
    anon "So what are you gonna do then?"
    tony "Beats me."
    tony "It's something her and I will have to figure out after we've dealt with your little Russian problem..."
    jump tony_button_pizzeria.choice


label tony_button_pizzeria.babies:
    anon f_normal "Where's {b}Maria{/b}?"
    show tony f_normal
    if M_maria.pregnancy.baby_gender == 'boy':
        tony "The little one was gettin' cranky so she took him on home."
        tony "I just hope he sleeps through the night this time..."
    elif M_maria.pregnancy.baby_gender == 'girl':
        tony "The little one was gettin' cranky so she took her on home."
        tony "I just hope she sleeps through the night this time..."
    else:
        tony "The little ones were gettin' cranky so she took 'em on home."
        tony "I just hope they sleep through the night this time..."
    jump tony_button_pizzeria.choice


label tony_button_pizzeria.curious:
    anon f_normal "{b}Maria{/b} around?"
    tony f_suspicious "Yeah, of course."
    tony @ a_point_back "She's in the kitchen, like usual."
    tony f_smirk @ a_frustrated "Why ya askin'?"
    anon f_shy @ a_behind_head "Oh, I was... Uhh-"
    anon "{i}*Ahem*{/i} Just curious."
    tony @ a_belly f_laugh "Hah, curious he says..."
    tony "Just don't be too loud, eh?"
    tony @ a_point f_smirk_wink "Don't want the customers hearin'."
    anon @ -m_talk "..."
    jump tony_button_pizzeria.choice


label tony_button_pizzeria.deliver:
    anon f_normal "You bet!"
    tony f_normal @ f_laugh "That's what I like to hear!"
    tony @ a_point "I've got some pies sittin' right over there on the counter; cooked up nice and rarin' to go!"
    tony @ f_smirk "Make sure you get 'em to the right place, capisce?"
    anon @ a_salute f_grin "Yes, sir!"
    hide anon with dissolve
    tony "Attaboy!"
    tony @ a_finger_up "You're going straight to the top, champ."
    return


label tony_button_pizzeria.help:
    anon f_normal "Need help?"
    tony f_normal "Nah, sweepin' relaxes me."
    tony "I got this."
    anon "Alright."
    jump tony_button_pizzeria.choice


label tony_button_pizzeria.info:
    anon f_normal "Any information yet?"
    tony f_suspicious "Look, I know you're eager..."
    tony "... But Eddie can be a real slippery bastard when he don't wanna be found."
    anon f_worried @ -m_talk "..."
    tony "I promise, you'll be the first person to know the second I hear from him."
    tony f_normal @ a_point "Just keep doin' what you're doin', champ."
    tony "Every pizza you deliver helps {b}Maria{/b} and I more than you know."
    anon f_normal "Yeah, okay."
    jump tony_button_pizzeria.choice


label tony_button_pizzeria.italians:
    anon f_worried "What do you know about the Italian Mafia?"
    tony f_sad a_sides "Heh, {b}Maria{/b} warned me she spilled the beans on that."
    anon "So it's true then?"
    tony "Yeah, it's true."
    pause
    anon "How did you get mixed up with the mob, {b}Tony{/b}?"
    tony f_suspicious "Well, it's not like there was a whole lot of opportunities out there for orphan boys with no education..."
    tony "After the orphanage sent us packin', we were forced to do whatever we could to keep a roof over our heads and food in our bellies."
    anon @ -m_talk "..."
    tony "It was only a matter of time 'til we fell into crime."
    anon @ -m_talk "..."
    tony f_sad "So, what do you wanna know?"

    menu tony_button_pizzeria.mob:
        "How did you join?":

            jump tony_button_pizzeria.join
        "Have you killed people?":

            jump tony_button_pizzeria.kill
        "The tattoo?":

            jump tony_button_pizzeria.trinacria
        "Why did you quit?":

            jump tony_button_pizzeria.quit
        "That's enough.":

            pass

    anon f_normal "I don't need to hear any more."
    tony f_normal a_idle "Alright, good."
    jump tony_button_pizzeria.choice


label tony_button_pizzeria.join:
    anon f_worried "How did you join?"
    tony f_suspicious "Oh, that was Luigi's doin'."
    tony "He used to ride the subway back and forth, pickpocketin' folks."
    tony "And one day he got caught with his hand in Lorenzo Rossi's pocket."
    anon @ f_confused "Who's Lorenzo Rossi?"
    tony "He was a bookie for the mob boss."
    anon "Oh."
    tony @ a_frustrated "Yeah, Luigi thought he was a dead man, for sure..."
    tony "... But then the guy up and offers him a job instead!"
    anon "Really?"
    tony "Yup."
    tony "Luigi decided he'd rather be an employee than a dead man, so he took it."
    anon "Makes sense."
    pause
    tony "Then a few weeks later, he brought me into the fold."
    anon @ f_surprised "Just like that?"
    tony "Yeah, more or less."
    tony "I had to prove I could handle myself first; but you know me..."
    tony f_normal @ f_smirk_wink a_fists "That wasn't no problem."
    pause
    anon "You didn't have any reservations about joining up?"
    tony f_suspicious "Oh, I had tons of 'em!"
    tony "But then you get a glimpse of how lucrative organized crime can be and your reservations fly right out the window, know what I mean?"
    anon @ -m_talk "..."
    tony "I knew it was my chance to carve out somethin' nice for {b}Maria{/b} and myself."
    tony "Make a decent life for us and ours, ya know?"
    jump tony_button_pizzeria.mob


label tony_button_pizzeria.kill:
    anon f_worried "Have you killed people?"
    tony f_suspicious "Sheesh, you're just divin' right into it, eh?"
    tony "You know, the mafia's business isn't about killin' people, champ."
    tony "It's more about extortin' 'em."
    tony @ a_money "They want money; not blood."
    anon @ -m_talk "..."
    tony @ a_fists "Violence is just a byproduct."
    anon "So, is that a yes?"
    tony f_sad "{i}*Sigh*{/i} Kid, I did what I had to do to survive."
    tony "It was ugly business and I've been party to some real awfulness."
    tony f_sad_down "Things I gotta live with for the rest of my days."
    pause
    tony f_sad "Things you might think you wanna know about... But trust me, champ... You don't."
    anon @ -m_talk "..."
    tony "Can you understand what I'm sayin'?"
    anon "Y-yeah, I guess..."
    tony f_suspicious @ a_point_under "Good, 'cause I really don't wanna go into that stuff with you."
    jump tony_button_pizzeria.mob


label tony_button_pizzeria.maria:
    anon f_normal "How did you and {b}Maria{/b} meet?"
    tony f_normal a_heart @ f_laugh a_point "Ahh, now there's a story worth tellin'!"
    tony "{b}Maria{/b} and I met when we was kids back in Brooklyn."
    anon "You guys are from Brooklyn?"
    tony a_idle @ a_finger_up "Yeah, that's right."
    tony "You see, she came from a well-to-do family."
    tony "Her father owned this fancy restaurant over on the east side and her ma used to volunteer at the orphanage where I grew up."
    anon "Oh?"
    tony "You know, servin' food to all us street rats and patchin' up our clothes."
    tony "That kinda thing."
    tony @ f_smirk_wink a_frustrated "She was a real generous woman, {b}Maria{/b}'s ma and the apple didn't fall far from the tree."
    pause
    tony "So you see, one day she brings {b}Maria{/b} down to the orphanage with her..."
    tony "And they're both cookin' up a storm, makin' the whole place smell wonderful."
    pause
    tony "I mean, she couldn't have been more than thirteen at the time, but she was a fuckin' savant in the kitchen, even then!"
    tony f_smirk_closed a_heart "Phew, lemme tell ya... I was smitten the second I saw her."
    tony f_normal a_idle @ f_smirk_wink "Then I tasted her cannolis."
    tony "I told her right then and there I was gonna marry her someday."
    anon f_surprised "Really?!"
    tony @ -m_talk "Mhmm."
    anon f_normal "What did she say?"
    tony "Ahh, she turned red as a beet and then told me to shut my piehole."
    anon "You mean, she didn't like you back?"
    tony "Nah, she just... Well-"
    pause
    tony "The good ones make you work for it, champ."
    tony @ f_smirk_wink "Remember that."
    pause
    anon "So you two have been together for a long time then?"
    tony "Almost thirty years."
    anon "That's wonderful, {b}Tony{/b}."
    tony "Ain't it?"
    tony @ a_point_back "{i}*Sigh*{/i} Man, it took a long time to convince her father I was worth a damn..."
    anon "He didn't approve?"
    tony f_suspicious @ a_wave "Ahh, of course not!"
    tony "I was just some nobody without a cent in my pocket."
    tony "He knew I wasn't good enough for his daughter."
    anon "But you proved him wrong?"
    tony f_normal @ f_smirk_wink "Well, you could say that..."
    tony "I got myself a job, makin' decent money, and saved every cent I had for three years."
    tony "Then I bought a nice little place on the east side and asked her father for his approval."
    anon "And?"
    tony @ f_laugh a_belly "Heh, the tough old bastard broke two of my ribs and fractured my eye socket."
    anon f_surprised "!!!"
    anon "For real?!"
    tony f_sad "I never was good enough for him..."
    show anon f_worried
    tony f_normal @ a_finger_up "... But I was good enough for her, and that's what matters."
    tony @ f_smirk_wink "Remember that, champ."
    anon f_normal "Y-yeah, okay {b}Tony{/b}."
    pause
    tony @ a_frustrated "Sheesh, listen to me."
    tony "Gabbin' on like an old lady in a hair salon."
    tony "What do you say we get those pizzas delivered, eh?"
    jump tony_button_pizzeria.choice


label tony_button_pizzeria.quit:
    anon f_worried "Why did you quit?"
    tony f_sad "Eh, twenty years of extortin' people starts to wear on a person, you know?"
    tony "I couldn't do it no more."
    tony "Then Luigi died and I realized that everyone I came up with was either in the ground or in prison."
    pause
    tony "We packed up, grabbed {b}Tina{/b} and her girl, and got the hell outta there."
    tony "Decided to try the quiet life for a while."
    anon f_normal "So you opened up a pizzeria?"
    tony f_normal "Heh, why not, eh?"
    tony "{b}Maria{/b} loves cookin' and there ain't many restaurants in this little town."
    anon "That's true."
    jump tony_button_pizzeria.mob


label tony_button_pizzeria.russians:
    anon f_worried "About those Russians..."
    tony f_suspicious "What about 'em?"
    anon "I'm curious how you know them?"
    tony "Ehh, that's a long story, champ..."
    tony "Let's just say I've had dealings with them in the past, okay?"
    anon "Alright."
    anon "You mentioned someone named {b}Raz{/b}..."
    anon "Who is he?"
    tony "{b}Raz{/b} is their boss."
    anon "How does that work?"
    tony "What do you mean?"
    anon "I mean, since when do criminals have bosses?"
    tony "They're Bratva, kid."
    anon @ f_skeptical "Bratva?"
    tony "Russian mafia."
    anon f_surprised "!!!"
    tony "Surely, you know what mafia is, don'tcha?"
    anon f_worried "Y-yeah, I think so."
    pause
    anon "What are the Russian mafia doing in Summerville?"
    tony "Pfft, hell if I know..."
    tony "... But whatever they're doin', it ain't good."
    tony "I'll tell you that for free."
    tony "You'd be wise to steer well clear of 'em."
    jump tony_button_pizzeria.choice


label tony_button_pizzeria.tattoo:
    anon @ a_point "Your tattoo..."
    tony f_suspicious "You wanna know about the tattoo, eh?"
    anon "Yes, sir."
    pause
    anon f_worried "U-unless, you don't want to tell me?"
    pause
    anon "Sorry, I don't mean to pry or noth-"
    tony f_sad "Ahh, it's alright, champ."
    tony "I can't fault ya for bein' curious."
    pause
    tony "It's just not something I usually discuss with people I've only recently become acquainted with."
    anon "I understand."
    tony f_smirk "Maybe if I got to know you better..."
    anon "Y-yeah, okay."
    tony f_normal "For now, let's just say it's a remnant from a past life, capisce?"
    anon f_skeptical "Past life?"
    tony f_suspicious "What, you think I've always been a pizza peddler?"
    tony a_belly @ f_normal_down a_frustrated "Jesus, look at me..."
    tony "Of course you think that."
    show tony a_idle with dissolve
    anon f_worried "That's not-"
    tony f_smirk "I didn't always look like a fat Italian plumber, you know..."
    tony f_normal @ f_laugh "In fact, I used to be quite virile!"
    anon f_normal @ f_laugh "Really?"
    tony f_suspicious "Ya, really!"
    tony a_fists @ a_point "I'll have you know, I still got a few good fights left in me."
    tony "So don't push your luck, wise guy."
    anon f_surprised a_up "Whoa, I wasn't-"
    tony a_belly f_normal @ f_laugh "Hah!"
    tony a_idle "Relax, champ."
    tony @ f_smirk_wink "I'm just bustin' ya balls."
    anon f_worried a_behind_head @ -m_talk "..."
    tony "Why are you always so twitchy all the time, eh?"
    anon f_sad_down a_idle "I dunno."
    tony f_suspicious "You're like a scared little rabbit or something..."
    anon "I'm sorry."
    tony f_normal @ f_laugh "And stop apologizin' all the time!"
    tony "The ladies hate that kinda thing, you know?"
    anon "Y-yeah."
    tony f_angry a_fists "They want a man with some backbone, yeah?!"
    anon @ -m_talk "..."
    tony "Someone they can rely on to take care of 'em."
    tony f_suspicious a_idle "Didn't your papa teach ya that?"
    anon "Not really."
    tony f_sad a_frustrated "Jesus."
    if L_pizzeria_interior.is_here(M_tony):
        show tony a_mc_hip_single:
            xoffset 32
        show tony_arms_dressed_a_mc_shoulder_single:
            flip
            xoffset 32
    else:
        show tony a_mc_hip_single:
            xoffset -32
        show tony_arms_dressed_a_mc_shoulder_single:
            xoffset -32
    with dissolve
    tony "Well, don'tcha worry, champ."
    show anon f_shy
    tony f_normal "Uncle {b}Tony{/b} is gonna teach ya everything you need to know."
    pause
    show tony f_smirk_closed a_finger_up:
        xoffset 0
    hide tony_arms_dressed_a_mc_shoulder_single
    with {'master': dissolve}
    tony "But first, you gotta deliver these pizzas."
    tony f_normal a_frustrated "Capisce?"
    anon @ a_salute "Yes, sir."
    show tony a_idle with dissolve
    jump tony_button_pizzeria.choice

label tony_button_pizzeria.trinacria:
    anon f_normal "So about the tattoo."
    tony f_normal "Oh, that?"
    show tony b_casual a_unbutton1 with dissolve
    pause 1
    tony a_unbutton2 "Heh, it's the Trinacria, champ."
    tony "A Sicilian symbol that's older than dirt."
    tony a_unbutton1 "Lots of the mob guys got it."
    show tony b_dressed a_idle with dissolve
    anon f_skeptical "I see."
    jump tony_button_pizzeria.mob
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
