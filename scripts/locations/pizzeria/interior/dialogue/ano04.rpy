label ano04_tony_pizzeria_interior:
    scene expression player.location.background_closeup
    show tony f_angry:
        xoffset -100
    show maria f_angry:
        flip
        xoffset -150
    show xtra 12 as counter
    with fade
    tony "Look, that Gino was a lazy bum..."

    tony "I should have canned his ass months ago."

    maria @ f_eyeroll "Ya, tidak apa-apa."

    maria "I coulda told ya that after his first day, {b}Tony{/b}..."

    maria @ a_point "It don't change the fact that we need more than two people to run this place!"

    tony "{i}*Sigh*{/i} I know, darlin'... I'm sorry!"

    tony "I'm gonna find somebody soon, okay?"

    maria a_crossed "We should just go back to being dine in or pick up only."

    tony "We're not doin' that!"

    tony "Deliveries bring in too much money."

    maria "Well then, you better start locking the door when you leave to make deliveries."

    maria "I can't keep workin' the kitchen and the counter at the same time..."

    maria "My feet are killin' me!"

    pause
    maria "And besides, what if someone came in here lookin' to make trouble, eh?"

    maria "What am I supposed to do then, all by my lonesome?"

    tony "I don't know, sell 'em a pizza?"

    maria @ a_whatever "That ain't funny, {b}Tony{/b}!"

    tony "Tsk, come on..."

    tony "Ain't nobody comin' in here lookin' for trouble!"

    tony "We left all that business behind us."

    maria "I'm talkin' about somebody tryin' to rob the place, you dunce!"

    show anon with dissolve:
        flip
    tony "Ugh, sheesh {b}Maria{/b}, you worry too much!"

    maria "No, you don't worry enough!"

    show maria f_annoyed
    show anon f_worried
    maria @ a_whatever "Tch, I'm not arguin' no more."

    maria "I got pizzas to make."

    hide maria with dissolve
    show tony with {'master': dissolve}:
        xoffset -250
    tony "That's the spirit darlin'."

    tony "You make them pizzas!"

    tony "I'll find somebody real soon, I promise."

    maria "Whatever, {b}Tony{/b}!"

    tony "Everything's gonna be great, you'll see."

    pause
    show tony f_normal with dissolve:
        flip
        xoffset 0
    tony "Oh hey, speak of the devil!"

    tony "You're still breathin', eh?"

    anon f_shy "Yeah, heh."

    anon "I'm still breathing."

    anon f_normal "Thanks to you."

    tony "Ahh, don't mention it."

    tony "I'm happy to help, buddy."

    pause
    tony "You here about the job?"

    anon "Oh, umm... Yeah, I am."

    anon "Assuming it's still available?"

    tony f_normal @ f_laugh "Well, of course it's still available..."

    tony "Were you not payin' attention when ya walked in here?"

    tony @ a_point_back "My wife is all up in my ass about hiring a new delivery boy."

    anon f_surprised @ a_point "That was your wife?"

    show tony f_smirk_wink a_point with dissolve
    pause
    tony f_normal a_idle "That's right, buddy."

    tony "Nice, eh?"

    anon f_normal "Very."

    tony "She's a firecracker too, I tell ya what..."

    tony "You play your cards right and work real hard for me, you're gonna end up with one just like her..."

    anon "I'll definitely work hard for you, sir."

    tony "Atta' boy!"

    tony "I knew you was an enterprising young man the second I laid eyes on ya."

    tony "Now, I want ya to hurry along and get these pizzas delivered, capisce?"

    anon @ f_laugh a_salute "Ya, tuan!"

    tony "What kind of vehicle you got?"

    anon f_worried "V-vehicle?"

    anon "I don't own a vehicle."

    tony "Apa?"

    tony "You're old enough to drive, ain't ya?"

    anon "Yeah, but I can't afford-"

    tony "You got a bike?"


    menu:
        "Ya." if player.transport_level:
            anon f_normal "Yes, I do have a bike."

            tony "Ahh, well... That'll do for now."

            tony "Ambil pizza ini dan lihat pizza tersebut diantar ke tempat yang tepat."

            tony @ f_suspicious "Jangan main-main sekarang, kamu dengar aku?"

            anon "saya tidak akan melakukannya."

            tony "Ketika kamu kembali, aku akan membayarmu dengan sangat baik."

            anon "Terima kasih, {b}Tony{/b}."

            anon @ a_wave "Saya akan kembali dalam sekejap, Anda akan lihat."

            tony @ f_laugh "Ahh, pergi dari sini, dasar bodoh!"

            hide anon with dissolve
            return True
        "Tidak.":

            pass

    anon "Tidak."

    tony f_suspicious "Jesus, kid."

    tony "You certainly ain't getting a girl like my {b}Maria{/b}, walkin' around town like a bum!"

    show tony f_normal_down a_pocket with dissolve
    pause 1
    tony a_money_count "Now let's see here..."

    anon f_surprised "A-apa yang kamu-"

    tony a_money f_normal "I want you to {b}take this down to the mall and buy yourself a nice bicycle{/b}."

    show anon a_money
    show tony a_idle
    with dissolve
    anon "Sungguh?"

    tony "Yeah, for real."

    show anon f_normal a_idle with dissolve
    tony "Now hurry up, will ya?"

    tony "I need these pizzas delivered today."

    anon @ f_laugh "Ya, tuan!"

    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
