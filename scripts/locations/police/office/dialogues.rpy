label police_office_mia_clues_summary:
    scene expression "backgrounds/location_police_office_missing_blur.jpg"
    show player 35 with dissolve
    player_name "( Okay, so he's taking time off... )"

    if M_mia.get("questioned yumi") != 'skip':
        player_name "( ... And went for a drive this morning already drunk! )"

    else:
        player_name "( ... And was in such bad-shape {b}Earl{/b} thought he might be quitting! )"

    show player 12
    player_name "Hmm..."

    player_name "( I need more clues. )"

    player_name "( Maybe I should {b}check his desk{/b}... )"

    hide player with dissolve
    return

label police_office_mia_harold_gift:
    scene police_c_2
    show player 13 at left
    show old_harold 2 at right
    with dissolve
    harold "Hai!"

    show old_harold 1
    show player 14
    player_name "Hi, sir!"

    player_name "Umm... I have something for you."

    show player 13
    show old_harold 3
    harold "Something for me?"

    show old_harold 1
    show player 12
    player_name "Well, it's from {b}Mia{/b}..."

    player_name "... She said she found this at home and wanted you to have it."

    show player 239_240 with dissolve
    pause
    show player 447 with dissolve
    show old_harold 4
    harold "!!!"
    show old_harold 33 at Position (xpos=1017)
    show player 13
    with dissolve
    harold "My old Aviators..."

    show old_harold 32
    show player 14
    player_name "She thought you should have them."

    show player 13
    show old_harold 35
    harold "Thanks, I... It's been a while..."

    show old_harold 34
    show player 14
    player_name "I think you should wear them again!"

    show player 13
    show old_harold 33
    harold "Saya akan memikirkannya."

    show old_harold 34
    show player 14
    player_name "Well, I'd better get going."

    show player 13
    show old_harold 33
    harold "Umm... Would you do something quick for me before you leave?"

    show old_harold 34
    show player 14
    player_name "Sure, what is it?"

    show player 13
    show old_harold 33
    harold "Just {b}tell Yumi that we need a status update on an inmate transfer{/b}..."

    harold "... She should be in the basement."

    show old_harold 34
    show player 14
    player_name "Okay, I'll tell her."

    show player 13
    show old_harold 35
    harold "Thanks again, kiddo."

    hide player
    hide old_harold
    with dissolve
    return

label police_office_mia_convince_harold:
    scene police_c_2 with fade
    show player 14 at left
    show earl f_eat a_donut_eat
    with dissolve
    player_name "Hello, Officer {b}Earl{/b}!"

    show player 13
    earl a_idle f_normal @ a_idle f_annoyed "Hello... What was your name again?"

    show player 10
    player_name "{b}[firstname]{/b}, I'm in your daughter's class."

    show player 5
    earl "Oh, yeeeeeeah."

    earl f_annoyed "What do you need?"

    show earl f_eat a_donut_eat with dissolve
    show player 12
    player_name "Well, I was hoping to find {b}Harold{/b} here. Is he around?"

    show player 13
    show earl f_normal a_idle with dissolve
    earl "He just went out on patrol but should be back soon."

    earl "I can hardly finish my donut box, and he's back at his desk..."

    earl "... And I eat FAST!"

    earl "Anyway... The guy hasn't cracked a case in a long time. I'm not sure he has it in him anymore."

    show earl f_eat a_donut_eat with dissolve
    show player 12
    player_name "Benar-benar?"

    show player 5
    show earl f_tired a_idle with dissolve
    earl "I think when I got promoted instead of him, it took the wind out of his sails."

    pause
    earl f_normal @ f_laugh "Hey... I'm all out of donuts!"

    show player 13
    earl "Listen, kid. I gotta make a quick trip and resupply. I get feisty if my blood sugar dips."

    earl "And you don't want to meet a feisty {b}Earl{/b}."

    earl "{b}Harold{/b} should be back soon. Stick around!"

    hide earl with dissolve
    show player 12
    player_name "Hah..."

    player_name "( {b}Harold{/b} hasn't been doing well at work, and lost a promotion... )"

    show player 10
    player_name "( He's getting grief at home and at work. )"

    show player 5
    pause
    show player 13
    show old_harold 2 at Position (xpos=762) with dissolve
    harold "Halo, {b}[firstname]{/b}."

    harold "What are up to today?"

    show old_harold 1
    show player 14
    player_name "{b}Mia{/b} wanted me to ask you to join {b}Helen{/b} and her for dinner on the weekend."

    show player 13
    show old_harold 29
    harold "..."
    show old_harold 30 at right with dissolve
    harold "Well... I would love to see them..."

    harold "I wish I had the time too, but..."

    show player 5
    hide old_harold
    show old_harold 26 at Position (xpos=762)
    with dissolve
    harold "I have a lot of work. I've got a lot of cases to solve lately."

    harold "My oldest case is starting to stand out to my chief."

    harold "I was assigned the notorious night bandit case."

    harold "I've been catching heat lately for my lack of results on the whereabouts of the missing goods..."

    show old_harold 25
    if M_larry.finished_state(S_larry_start):
        show old_harold 26
        harold "... And {b}Larry{/b} isn't giving up the location of the goods either..."

        show old_harold 25
        show player 12
        player_name "Saya akan berbicara dengannya. Saya kenal istrinya."

        player_name "Jika saya tidak bisa mengetahui lokasinya, mungkin saya bisa menghubungi {b}Ny. Johnson{/b} untuk membantu kami."

    else:
        show player 12
        if M_erik.finished_state(S_erik_thief_chase):
            show player 12
            player_name "I've heard the news. I've actually seen the thief around my house a lot lately."

            show old_harold 29
            player_name "He is always sneaking into my neighbor's, {b}Mrs. Johnson{/b}, yard."

            show player 5
            show old_harold 3
            harold "Really? Until now, we've only had reports of him near the park."

            show old_harold 1
        else:
            player_name "I've heard the news."

            show player 5
            show old_harold 24
            harold "Yeah, they love to keep a running commentary on how long he's been at large."

            show old_harold 26
            harold "We received some reports of sightings over near the park, but they never panned out."

            show old_harold 25
        show player 12
        player_name "Oke, saya akan memeriksa petunjuknya juga."


    show player 13
    show old_harold 2
    harold "Terima kasih, {b}[firstname]{/b}."

    show old_harold 6
    harold "I'd better get back to work. If I ever want to solve some cases and free up some time away from work."

    show old_harold 1
    show player 14
    player_name "Talk to you later, {b}Harold{/b}."

    hide old_harold with dissolve
    if M_larry.finished_state(S_larry_start):
        show player 12
        player_name "( Sounds like I need to help him find where {b}Larry{/b} hid the stolen goods. )"

        show player 10
        player_name "( Otherwise, he's never gonna have time to go to dinner with {b}Mia{/b} and {b}Helen{/b}. )"

        show player 12
        player_name "( I should stop down to the jail cells and see him. )"

        player_name "( Maybe he'll tell me where the stolen goods are. )"

    else:
        show player 12
        player_name "( Sounds like I need to help him find the thief's stolen goods. )"

        show player 10
        player_name "( Otherwise, he's never gonna have time to go to dinner with {b}Mia{/b} and {b}Helen{/b}. )"

        show player 12
        if M_erik.finished_state(S_erik_thief_chase):
            player_name "( I'd better keep an eye on {b}Mrs. Johnson{/b}'s backyard at night. )"

            player_name "( There was something else too... Oh, right! )"

        player_name "( {b}Harold{/b} mentioned the thief was spotted in the park. )"

    show player 5
    pause
    show player 30
    player_name "( {b}Earl{/b} is still not back. )"

    show player 33
    player_name "( I wonder how many donuts he goes through each day... )"

    hide player
    with dissolve
    return

label police_office_mia_return_goods:
    scene police_c_2 with fade
    show player 453 at right
    show old_harold 2f at left
    with dissolve
    harold "Hai, {b}[firstname]{/b}."

    show old_harold 1f
    show player 454
    player_name "Hai, {b}Harold{/b}!"

    show player 453
    show old_harold 3f
    harold "What's with the big bag you got with you?"

    show old_harold 1f
    show player 454
    player_name "It's something I found in the park..."

    player_name "... I think you might want to see this."

    show player 453
    show old_harold 4f
    harold "Oh ya?"

    show old_harold 1f
    show player 454
    player_name "Have a look!"

    show player 13f
    show old_harold 47
    with dissolve
    harold "!!!"
    show old_harold 49 with dissolve
    harold "... Those are..."

    harold "... All the stolen items!!"

    show old_harold 48
    if M_larry.finished_state(S_larry_msg_done):
        show player 14f
        player_name "{b}Larry{/b} actually told me where it was."

        player_name "He said he had been stashing all the stolen goods in the park."

    else:
        show player 17f
        player_name "It was right where you said it would be!"

        show player 13f
        show old_harold 49
        harold "Itu tadi?"

        show old_harold 48
        show player 14f
        player_name "You mentioned the burglar was sighted in the park a lot."

        player_name "I did some checking around and found it tucked away behind some bushes next to a white tree."

    show player 453 at right
    show old_harold 2f at left
    pause
    show player 13f
    show old_harold 49
    harold "I'm impressed {b}[firstname]{/b}. You did a great job!"

    show old_harold 48
    show player 17f
    player_name "Oh don't thank me. I wouldn't have found it if you didn't collect the clues."

    show player 14f
    player_name "If anyone asks me about it, it was Officer {b}Harold{/b} that made the find!"

    show player 13f
    show old_harold 49
    harold "Oh, you're too generous."

    show old_harold 48
    show earl:
        xoffset -300
    show old_yumi 11 at Position (xpos=700)
    with dissolve
    yumi "What do you have there, partner?"

    show old_yumi 10
    earl "Looks like his dirty laundry bag."

    earl @ f_laugh "{i}*Snort*{/i} Hee-uck-uck-uck."

    show old_harold 49
    harold "Not quite, {b}Earl{/b}. Those are all the stolen goods from the night burglar!"

    show old_harold 48
    earl "Shiiieeeeet!"

    show old_yumi 11
    yumi "Congratulations, sir!"

    show old_yumi 10
    earl @ f_laugh "I... I knew I could always count on you, {b}Harold{/b}!"

    show old_harold 49
    harold "Thanks guys. I really didn't do much though."

    show old_harold 48
    show player 14f
    player_name "{b}Harold{/b}'s just being modest!"

    show player 13f
    earl "So, what are all the retrieved items?"

    show old_harold 49
    harold "Lots of valuables... I think everything that was reported stolen is in here."

    hide old_harold
    show earl b_dressed_hug_harrold
    show harold b_empty f_embarrassed:
        flip
        xoffset -62
    with dissolve
    earl "Wow! I didn't think you had it in you lately, {b}Harold{/b}!"

    earl "But you solved one of the most high profile cases in recent years!"

    earl @ f_laugh "You'll surely get a promotion out of finding all the stolen items! Heck, you deserve a promotion!"

    "{i}*Grumble* *Gurgle*{/i}"

    earl f_eat "Woah... My belly is growling... All this excitement made me extra hungry!"

    earl @ f_laugh "I need to find me a donut!"

    hide earl
    hide harold
    show old_harold 48 at left
    with dissolve
    show old_yumi 11
    yumi "Congratulations again, {b}Harold{/b}."

    show old_yumi 10
    show old_harold 49
    harold "Thanks, {b}Yumi{/b}."

    show old_harold 50
    hide old_yumi
    show player 11f
    with dissolve
    harold "!!!"
    show old_harold 48
    show old_yumi 12 at Position (xpos=500)
    with dissolve
    yumi "..."
    show old_yumi 13 at Position (xoffset=12) with dissolve
    yumi "Well... I... Uh... Better get back to my cell duties."

    hide old_yumi with dissolve
    show old_harold 2f at Position (xpos=9) with dissolve
    show player 13f
    harold "That... Felt great."

    harold "I haven't felt this appreciated in a long time..."

    harold "Thank you, {b}[firstname]{/b}, for helping me out with this."

    show old_harold 1f
    show player 14f
    player_name "It was mostly luck, really."

    show player 13f
    show old_harold 2f
    harold "Ahhh..."

    harold "I think I'm going to start spending more time on my patrols now."

    harold "You know... Actually try and solve my other cases instead of trying to just make it through the day."

    show old_harold 1f
    show player 14f
    player_name "Good for you {b}Harold{/b}. I'm glad you feel better."

    player_name "I know I always feel good after accomplishing something at school."

    show player 17f
    player_name "{b}Mia{/b} and {b}Helen{/b} will be proud to hear you solved the case too!"

    show player 13f
    show old_harold 25f
    pause
    show old_harold 2f
    harold "Tell you what. I'll attend that dinner after all."

    harold "I feel like a weight's been lifted my shoulders now that people's valuables have been found."

    harold "I'll call them shortly and make dinner plans... I'll actually have something to tell them about!"

    show old_harold 1f
    show player 14f
    player_name "I'm glad it all worked out in the end, {b}Harold{/b}."

    show player 13f
    pause
    show player 36f with dissolve
    player_name "Well, I'll see you later."

    show player 13f with dissolve
    show old_harold 2f
    harold "Selamat tinggal, {b}[firstname]{/b}."

    hide old_harold
    hide player
    with dissolve
    return

label police_harolds_desk:
    call expression game.dialog_select("police_harolds_desk_dialogue")
    $ M_mia.trigger(T_harold_photo_clue)
    $ game.main()

label police_harolds_desk_dialogue:
    scene police_c_2
    show player 109
    show old_harold_desk at right
    with dissolve
    pause
    show player 108
    player_name "( Nothing much here. )"

    show player 108f with dissolve
    player_name "( I was hoping to find some notes and some- )"

    player_name "Hah..."

    player_name "( Is that an old picture of him? )"

    call screen harolds_desk
    scene police_office_picture
    player_name "( Is that... {b}Helen{/b} and {b}Harold{/b}?! )"

    player_name "( Wow... They look SO different... And so much happier! )"

    player_name "..."
    player_name "( Where is that location? )"

    player_name "( It looks like... Maybe {b}Raven Hill{/b}? )"

    player_name "Hah."

    player_name "( They probably used to hang out there a lot... )"

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
