label french_classroom_bissette_intro:
    scene french_class_c
    show anon with dissolve
    show bissette with dissolve
    bissette "Itu dia!"

    anon @ a_wave "Hai, {b}Nona Bissette{/b}!"

    bissette f_sad "Listen, {b}[firstname]{/b}, I know you've had some personal matters to take care of, and that's why you've been absent lately..."

    bissette "... But is everything okay?"

    anon f_worried @ f_worried_low "Yeah. I think I should be okay..."

    bissette "You're not the only one a bit behind, you know."

    anon f_shy @ a_behind_head "It's definitely the hardest class we have, I think."

    bissette f_normal "Well, if you ever need anything, let me know."

    anon "Terima kasih, {b}Nona Bissette{/b}."

    bissette @ f_laugh a_finger "Oh! That reminds me!"

    bissette "I'm implementing a new learning opportunity for those trying to catch up."

    anon "Oh ya?"

    bissette f_sexy "It'll be a bit more... One on one type of learning..."

    bissette @ a_hair "... And I'm hoping it will energize students."

    anon f_normal "Jadi begitu."

    bissette f_normal "Why don't you take your seat and I'll be discussing it in front of the class."

    anon "Oke."

    hide anon with {'master': dissolve}

    scene french_class_cs9
    show text _ ("{b}Miss Bissette{/b} had an announcement that day.\nShe planned on rewarding the student who showed the most improvement in class after the final quiz.\nShe even offered private tutoring to anyone that was interested.") as caption
    with fade
    pause

    scene studyclass02
    show text _ ("I spent the whole day trying to catch up to my studies...") as caption
    with fade
    pause

    scene studyclass03
    show text _ ("... Until the bell rang.") as caption
    with fade
    pause

    scene studyclass04
    show text _ ("I forgot how much French class makes me sleepy.\nIt was a struggle to focus on the lesson.") as caption
    with fade
    pause

    scene studyclass05
    show text _ ("But I always can count on my classmates to keep me awake...") as caption
    with fade
    pause

    scene studyclass06
    show text _ ("They have been picking on me lately...\nProbably, because I just came back and now I'm the center of attention...") as caption
    with fade
    pause

    scene studyclass07
    show text _ ("Don't get me wrong though. I can stand my ground...") as caption
    with fade
    pause

    scene studyclass08
    show text _ ("... But I guess this is just how school goes.\nWell, at least the day is over and I can go home now...") as caption
    with hpunch
    pause

    scene french_class_c
    show bissette:
        xoffset -200
    with fade
    bissette @ a_finger "Oh! And before you all leave."

    bissette "Any students interested in the after-school tutoring sessions, {b}come talk to me in my office or tomorrow in class{/b}."

    bissette @ f_laugh "Au revoir!"

    hide bissette with {'master': dissolve}
    return

label french_classroom_bissette_tutoring:
    scene french_class_c
    show player 5 with dissolve
    player_name "( I should speak with {b}Miss Bissette{/b} about private tutoring. )"

    player_name "( I'm gonna need help if I want to pass French class. )"

    hide player with dissolve
    return

label french_classroom_bissette_study:
    scene french_class_c
    show teacher 1 at right
    show player 14 at left
    with dissolve
    player_name "Okay, I'm ready to start the lesson, {b}Miss Bissette{/b}."

    show player 13
    show teacher 3
    bissette "Génial!"

    show teacher 2
    bissette "Stay after class and we will begin."

    show teacher 1
    show player 14
    player_name "Tentu saja."

    hide player
    hide teacher
    with dissolve

    scene studyclass02
    show text _ ("I spent the whole day trying to catch up to my studies...") as caption
    with fade
    pause

    scene studyclass03
    show text _ ("... Until the bell rang.") as caption
    with fade
    pause

    scene classroom_night
    show teacher 7 at right
    show desk 5 at Position (xpos = 400, ypos = 768)
    with fade
    bissette "Are you ready for our first lesson?"

    bissette "Alone."

    bissette "Together."

    show teacher 9
    show desk 6
    player_name "Eh, ya?"

    show desk 5
    show teacher 7
    bissette "Ah ah ah, parlez-vous Français?"

    show teacher 9
    show desk 6
    player_name "Oh! Umm, oui?"

    show desk 5
    show teacher 7
    bissette "Sangat bagus!"

    bissette "Now, have you looked at the assigned terms yet?"

    show teacher 9
    show desk 6
    player_name "Yeah, I looked them over."

    show desk 5
    show teacher 7
    bissette "Which ones are troubling you?"

    show teacher 9
    show desk 6
    player_name "Well, I'm not very good at pronunciation."

    show desk 4
    player_name "Like... How do you say this word?"

    show desk 3
    show teacher 7f at Position (xpos=300) with dissolve
    bissette "Ah, that's vélo or la bicyclette."

    bissette "It means bicycle."

    hide teacher
    show desk 8 at Position (xoffset=-29)
    with dissolve
    player_name "!!!"
    show desk 9 at Position (xoffset=-27) with dissolve
    bissette "Here, repeat after me {b}[firstname]{/b}."

    show desk 10 at Position (xoffset=-27) with dissolve
    bissette "Vi-loo."

    show desk 11 at Position (xoffset=-27)
    player_name "... Velow."

    show desk 10 at Position (xoffset=-27)
    bissette "No VI-loo."

    show desk 11 at Position (xoffset=-27)
    player_name "Vv... Velo."

    show desk 10 at Position (xoffset=-27)
    bissette "Almost, you just need to pronounce the e now."

    show desk 11 at Position (xoffset=-27)
    player_name "... Velo."

    show desk 10 at Position (xoffset=-27)
    bissette "Très bien, mon bel homme!"

    show desk 9 at Position (xoffset=-27) with dissolve
    bissette "You are learning very quickly."

    show desk 11 at Position (xoffset=-27) with dissolve
    player_name "Thanks, {b}Miss Bissette{/b}. You're such a good teacher!"

    show desk 9 at Position (xoffset=-27) with dissolve
    bissette "Ah, quel charmeur!"

    show desk 8 at Position (xoffset=-29) with dissolve
    bissette "Such a well-mannered young man."

    show desk 9 at Position (xoffset=-27) with dissolve
    bissette "Now, let's move on to the next word."

    scene black with fade
    pause 1
    scene classroom_night
    show teacher 7 at right
    show desk 1 at Position (xpos = 400, ypos = 768)
    with dissolve
    bissette "You did so well, {b}[firstname]{/b}, but it's getting late."

    show teacher 10
    bissette "We should call it a day, yes?"

    show teacher 9
    show desk 2
    player_name "Wow, is it that late already?"

    player_name "I totally lost track of time."

    show desk 1
    show teacher 7
    bissette "Oui, the time, it flies when you are having such fun!"

    bissette "You know, {b}[firstname]{/b}, I'm so happy you signed up for my tutoring."

    bissette "It fills me with joy, helping nice young students like yourself to succeed."

    show teacher 10
    bissette "It's why I became a French teacher."

    show teacher 9
    show desk 2
    player_name "Yeah, I'm lucky you're my teacher, {b}Miss Bissette{/b}."

    show desk 1
    show teacher 7
    bissette "Ohh, tu me flattes..."

    bissette "You are making me blush."

    bissette "Just keep practicing and I think you'll be caught up in no time."

    bissette "Who knows, you might even earn that special reward..."

    show teacher 9
    show desk 2
    player_name "Ya, Bu."

    show desk 1
    show teacher 7
    bissette "Now get home, {b}[firstname]{/b}."

    show teacher 10
    bissette "Au revoir!"

    show teacher 9
    show desk 2
    player_name "Goodnight, {b}Miss Bissette{/b}."

    hide desk
    hide teacher
    with dissolve
    return

label french_classroom_bissette_smith_report:
    scene french_class_c
    show teacher 4 at right
    show principal 28f at left
    with dissolve
    smith "{b}Miss Bissette{/b}, I was expecting your midterm report on my desk this morning."

    show principal 29f
    show teacher 15
    with dissolve
    bissette "Je suis désolée! It completely slipped my mind!"

    show teacher 4 with dissolve
    show principal 27f at Position (xoffset=70)
    smith "Yes, well, I want it in my hands by the end of the day!"

    show principal 28f with dissolve
    smith "... And there had better be an improvement over last term's grade point average!"

    smith "The city isn't going to keep funding us if our students are all failing their classes!"

    show principal 29f with dissolve
    show teacher 5
    bissette "Oui, {b}Madame Smith{/b}. I've devised a new method to inspire the students."

    bissette "Surely, it will raise their interest in the French class."

    show teacher 4
    show principal 27f at Position (xoffset=70)
    smith "Hah! You couldn't inspire a dog to bark..."

    show principal 29f
    show teacher 19
    bissette "Mais, madame... Surely you-"

    show teacher 18
    show principal 27f at Position (xoffset=70)
    smith "Just get me that report or I'll ship your smelly ass back to whatever French shithole you crawled out of!"

    show principal 28f with dissolve
    smith "Am I understood?!"

    show principal 29f with dissolve
    show teacher 5
    bissette "... O-oui, {b}Madame Smith{/b}."

    hide principal with dissolve
    show teacher 20
    pause
    show teacher 19 at center with dissolve
    bissette "Vieille chienne en colère!"

    show teacher 18f with dissolve
    pause
    show player 10 at left with dissolve
    player_name "{b}Nona Bissette{/b}?"

    show player 5
    show teacher 5 at right with dissolve
    bissette "Oh mon dieu!"

    show teacher 1
    show player 11
    player_name "..."
    show teacher 3
    bissette "{b}[firstname]{/b}, you frightened me!"

    show teacher 1
    show player 10
    player_name "Maaf..."

    show player 12
    player_name "Apakah semuanya baik-baik saja?"

    show teacher 4
    player_name "I could hear {b}Mrs. Smith{/b} from down the hall..."

    show player 5
    show teacher 5
    bissette "Oui. She is just wanting to see you students take more interest in the French."

    show teacher 4
    show player 12
    player_name "Well, she didn't have to be so mean about it."

    show player 5
    show teacher 3
    bissette "Oh, {b}[firstname]{/b}. You're always so sweet to me..."

    show teacher 17 zorder 1 with dissolve
    show player 11
    player_name "!!!" with hpunch
    show teacher 16
    bissette "You know, I've been wanting to speak with you about the next assignment for your tutoring sessions."

    show teacher 17
    player_name "{i}*Meneguk*{/i}"

    show player 10
    player_name "Alright, what did you have in mind?"

    show player 5
    show teacher 16
    bissette "Saya ingin Anda {b}menulis beberapa paragraf tentang makanan favorit Anda, dalam bahasa Prancis{/b}."

    bissette "Kalau begitu kita akan membahasnya bersama, ya?"

    show teacher 17
    show player 14
    player_name "Sounds good to me."

    show player 13
    show teacher 16
    bissette "... And if you write well..."

    bissette "Perhaps, I will be giving you a taste of my special reward, yes?"

    show teacher 17
    show player 14
    player_name "Y-yeah, okay!"

    show player 13
    show teacher 3 at center with dissolve
    bissette "Très bien! You had best be getting started then."

    bissette "Au revoir, {b}[firstname]{/b}!"

    hide teacher with dissolve
    show player 10
    player_name "I wonder what the reward could be?"

    show player 5
    player_name "..."
    show player 35 with dissolve
    player_name "... And what food should I write about?"

    show player 14 with dissolve
    player_name "{b}Time to visit the library{/b} again, I guess."

    player_name "That librarian was really helpful. Maybe she could find a book about {b}French food{/b} for me?"

    hide player with dissolve
    return

label french_classroom_bissette_hand_in_assignment:
    scene french_class_c
    show teacher 1 at right
    show player 14 at left
    with dissolve
    player_name "I finished the assignment!"

    player_name "I wrote about fromage."

    show player 13
    show teacher 2
    bissette "Oh! You like the French cheese?"

    show teacher 1
    show player 14
    player_name "All cheese really..."

    show player 13
    show teacher 2
    bissette "Hehe, you know what goes well with cheese, don't you?"

    show teacher 1
    show player 10
    player_name "... Umm, crackers?"

    show player 5
    show teacher 3
    bissette "No silly, French wine!"

    show teacher 12
    bissette "Maybe someday we could sample a bottle together?"

    bissette "But first we must continue practicing your French."

    bissette "Stay after class today, and we should have the room all to ourselves."

    bissette "Just you and I, yes?"

    show teacher 13
    show player 26
    player_name "Y-ya, Bu."

    show player 13
    show xtra 21 at left
    show teacher 2
    bissette "Oh, and before you sit down, add fromage to the blackboard."

    bissette "I'll have the other students write their favorites as well."

    hide player
    hide xtra 21
    with dissolve

    scene french_class_cs14
    show text _ ("I felt like I was actually getting pretty good with French.\nI was understanding more and more each day.\nThe private lessons with {b}Miss Bissette{/b} had definitely made the language more interesting.") as caption
    with fade
    pause

    scene studyclass02
    show text _ ("I spent the whole day trying to catch up to my studies...") as caption
    with fade
    pause

    scene studyclass03
    show text _ ("... Until the bell rang.") as caption
    with fade
    pause

    scene classroom_night
    show desk 12 at Position (xpos = 400, ypos = 768)
    with fade
    bissette "I'm really proud of your latest assignment."

    bissette "You're becoming quite... Fluent."

    show desk 13
    player_name "Yeah? I'm glad you liked it. I worked really hard on it."

    show desk 12
    bissette "I'm sure you did, mon bel homme."

    bissette "Are you ready for your next tutoring lesson?"

    show desk 13
    player_name "Ya."

    show desk 12
    bissette "Let's go over some more words then."

    scene black with fade

    scene classroom_night
    show desk 16 at Position (xpos = 400, ypos = 768)
    bissette "Your pronunciation is getting so good, {b}[firstname]{/b}."

    bissette "I think you have definitely earned it..."

    show desk 19 with dissolve
    bissette "... And I'm so proud of you."

    show desk 20 with dissolve
    bissette "Oh mon dieu!"

    bissette "All this new knowledge growing..."

    bissette "Ce qu'il est énorme ce lapin..."

    show desk 19 with dissolve
    player_name "..."
    show desk 14 with dissolve
    bissette "What's the matter, {b}[firstname]{/b}?"

    show desk 15
    player_name "What if someone..."

    show desk 14
    bissette "Aww, tellement mignon..."

    show desk 17 with dissolve
    bissette "Do not be worrying."

    show desk 18 with dissolve
    bissette "Di Sini."

    bissette "These should be taking your mind off your worries..."

    player_name "{i}*Meneguk*{/i}"

    show desk 24 with dissolve
    player_name "Y-ya..."

    show desk 25 with dissolve
    pause
    show desk 26 with dissolve
    bissette "Oh, oui! Joue avec mes seins, {b}[firstname]{/b}!"

    show desk 24 with dissolve
    player_name "You're sure {b}Mrs. Smith{/b} won't come in?"

    show desk 5 at Position (xoffset=-58)
    show teacher 10c at right
    with dissolve
    bissette "Oh non! J'ai oublié!"

    bissette "I forgot to turn in the midterm report!"

    bissette "Forgive me, {b}[firstname]{/b}. I'm afraid we must stop for today."

    show teacher 10b
    show desk 6 at Position (xoffset=-58)
    player_name "Okay, {b}Miss Bissette{/b}..."

    show desk 5 at Position (xoffset=-58)
    show teacher 10c
    bissette "We'll resume this next time, yes?"

    bissette "I'll have a new assignment waiting for you tomorrow."

    show teacher 10b
    show desk 6 at Position (xoffset=-58)
    player_name "Tentu saja, {b}Nona Bissette{/b}."

    show desk 5 at Position (xoffset=-58)
    show teacher 10
    bissette "Au revoir, mon petit lapin!"

    show teacher 9
    show desk 6 at Position (xoffset=-58)
    player_name "Au revoir."

    hide desk
    hide teacher
    with dissolve
    return

label french_classroom_bissette_poem_assignment:
    scene french_class_c
    show player 13 at left
    show teacher 2 at right
    with dissolve
    bissette "Halo, {b}[firstname]{/b}!"

    show teacher 1
    show player 14
    player_name "Bonjour, {b}Miss Bissette{/b}."

    show player 13
    show teacher 2
    bissette "Comment allez-vous?"

    show teacher 1
    show player 14
    player_name "Oh umm, I'm doing good."

    show player 13
    show teacher 3
    bissette "Luar biasa!"

    show teacher 2
    bissette "You're learning the French so quickly!"

    show teacher 1
    show player 14
    player_name "Yeah, I think your tutoring is really helping."

    show player 13
    show teacher 12
    bissette "Ah, we must continue with the lessons then, yes?"

    show teacher 13
    show player 14
    player_name "Saya ingin sekali!"

    show player 13
    show teacher 12
    bissette "I am thinking you will enjoy this next assignment..."

    show teacher 13
    show player 14
    player_name "Ah, benarkah?"

    show player 13
    show teacher 12
    bissette "Oui, beaucoup..."

    bissette "Are you familiar with French romance?"

    show teacher 13
    show player 10
    player_name "N-no, not really..."

    show player 11
    show teacher 16 zorder 1 with dissolve
    bissette "On apprend alors!"

    bissette "The French make the best lovers in all the world!"

    show teacher 17
    show player 26
    player_name "... Oh? I didn't know that..."

    show player 13
    show teacher 16
    bissette "Oh oui, {b}[firstname]{/b}, it is known!"

    bissette "So to give you insight into this... You are to be {b}writing a romantic poem en Français{/b}!"

    show teacher 17
    show player 10
    player_name "Err, I dunno, ma'am. I've never written anything like that before."

    player_name "I wouldn't even know how to begin..."

    show player 13
    show teacher 25 with dissolve
    bissette "Ridicule!"

    show teacher 26 with dissolve
    bissette "You're a natural, I have the faith in you, {b}[firstname]{/b}!"

    show teacher 27 with dissolve
    show player 14
    player_name "Heh. O-okay, {b}Miss Bissette{/b}."

    show player 13
    show teacher 25 with dissolve
    bissette "Très bien, mon bel homme!"

    show teacher 26 with dissolve
    bissette "I know you will write something that melts the heart!"

    show teacher 16 with dissolve
    bissette "Return to me when it is done."

    bissette "Perhaps you will finally earn the reward you've been seeking, yes?"

    show teacher 17
    show player 11
    player_name "{i}*Meneguk*{/i}"

    show player 26
    player_name "Y-yeah! Okay!"

    show player 13
    show teacher 16
    bissette "Ça m'excite!"

    show teacher 17
    show player 14
    player_name "I'll be back real soon, {b}Miss Bissette{/b}."

    show player 13
    show teacher 16
    bissette "Au revoir, {b}[firstname]{/b}."

    hide teacher with dissolve
    show player 29 with dissolve
    player_name "Wow!!!"

    player_name "Okay, I guess {b}I should head to the library{/b} and see what I can find about French poetry and romance."

    hide player with dissolve
    return

label french_classroom_bissette_hand_in_poem_assignment_pre:
    scene french_class_c
    show teacher 1 at right
    show player 386 at left
    with dissolve
    player_name "Here, {b}Miss Bissette{/b}. I finished the poem."

    show player 13 with dissolve
    show teacher 23 with dissolve
    bissette "Superbe!"

    bissette "Oh, comme c'est beau!"

    bissette "Yes, this will do nicely."

    bissette "The class is in for a treat."

    show teacher 24
    show player 10
    player_name "Huh? What do you mean?"

    show player 5
    show teacher 2 with dissolve
    bissette "Well, you are to be reciting it for the class, yes?"

    show teacher 1
    show player 11
    player_name "!!!" with hpunch
    show player 10
    player_name "Mustahil!"

    show player 11
    show teacher 12
    bissette "Quoi? Come now, {b}[firstname]{/b}."

    bissette "Your words are beautiful... It would be wrong not to share such a thing, yes?"

    show teacher 13
    show player 10
    player_name "Absolutely not! I'd be way too embarrassed!"

    show player 22
    show teacher 2
    bissette "Aww, do not be so self-conscious, {b}[firstname]{/b}."

    show teacher 11
    pause
    show teacher 2
    bissette "I know! I will be giving you a partner to read with!"

    bissette "This is less embarrassing, yes?"

    show teacher 1
    show player 12
    player_name "... Not really."

    show player 23
    show teacher 19
    bissette "{b}Roxxy{/b}, wake up!"

    show player 22
    show teacher 18
    roxxy "Hmm?"

    show teacher 19
    bissette "Fille paresseuse! Wake up, I said!"

    show teacher 18
    roxxy "Apa?!"

    show teacher 19
    bissette "Kemarilah!"

    show teacher 20
    pause
    pause
    show old_roxxy 27f at Position (xpos=500) with dissolve
    show player 24
    show teacher 19
    bissette "Since you cannot be bothered to write a poem for class, you will be reciting one with {b}[firstname]{/b} here."

    show teacher 18
    show old_roxxy 30f
    roxxy "Uhh, no I won't."

    show old_roxxy 29f
    show player 22
    show teacher 19
    bissette "Yes, you will!"

    show teacher 18
    show old_roxxy 30f
    roxxy "I don't care about this stupid assignment!"

    show old_roxxy 29f
    show teacher 19
    bissette "Quoi?! Comment oses-tu!"

    bissette "You will get up there and read or I will be giving you detention until the end of the term!"

    bissette "Comprenez vous?!"

    show teacher 20
    show old_roxxy 30f
    roxxy "Dengan serius?!"

    show old_roxxy 29f
    show teacher 19
    bissette "Now!"

    show teacher 18
    show old_roxxy 30f
    roxxy "Grrr, fine!"

    hide old_roxxy with dissolve
    show player 10
    player_name "Umm, {b}Miss Bissette{/b}?"

    show player 5
    show teacher 2
    bissette "Ya, {b}[firstname]{/b}?"

    show teacher 1
    show player 10
    player_name "I uhh, really don't want to do this..."

    show player 5
    show teacher 2
    bissette "Aww, but it is so beautiful..."

    show teacher 16 zorder 1 with dissolve
    bissette "Do it for me, mon bel homme!"

    show teacher 26 with dissolve
    bissette "... I'll give you a special reward if you do it..."

    show teacher 27
    show player 25
    player_name "{i}*Huh*{/i}"

    show player 24
    player_name "... Alright, I'll do it."

    show player 5
    show teacher 12 at center
    bissette "Sangat bagus!"

    bissette "I'm so proud!"

    show teacher 1
    hide player with dissolve
    show teacher 2
    bissette "Non non! En Français! Now let's begin!"

    hide teacher with dissolve

    scene french_class_cs11
    show text _ ("I wasn't excited to recite my poem in front of the class.\n... But {b}Roxxy{/b}'s involvement did actually help.\nNobody cared how sappy the poem was; not with {b}Roxxy{/b} stumbling over every other word.") as caption
    with fade
    pause

    scene french_class_cs13
    show text _ ("By the time we reached the end {b}Roxxy{/b} was beyond embarrassed.\nOur classmates were giggling at her poor pronunciation skills.\nShe was livid! I don't recall ever seeing her so angry...") as caption
    with fade
    pause
    return

label french_classroom_bissette_hand_in_poem_assignment_roxxy_sex:
    scene french_class_c
    show player 13 at Position (xpos=500)
    show old_roxxy 29f at left
    show teacher 2 at right
    with dissolve
    bissette "Sangat bagus!"

    bissette "{b}[firstname]{/b}, your French was perfect!"

    show teacher 1
    show player 14
    player_name "Terima kasih, {b}Nona Bissette{/b}."

    show player 13
    show teacher 19
    bissette "... And {b}Roxxy{/b}..."

    bissette "... Well, you tried."

    show teacher 18
    roxxy "Grrr..."

    show teacher 2
    bissette "Very well, that is it for today everybody."

    bissette "Remember to be {b}completing your homework{/b}, and I'll be seeing you tomorrow, yes?!"

    hide teacher
    with dissolve
    show player 25f with dissolve
    player_name "... {b}Roxxy{/b}, I'm sorry this-"

    show player 11f
    show old_roxxy 3f with dissolve
    roxxy "I HATE HER!!!"

    show old_roxxy 29f
    show player 10f
    player_name "... {b}Roxxy{/b}, seriously! You have to calm down..."

    show player 11f
    show old_roxxy 31f
    roxxy "CALM DOWN?!"

    roxxy "I'm not gonna calm down!"

    show old_roxxy 30f
    show player 24f
    roxxy "That mush mouth bitch gets some kind of sick pleasure out of embarrassing me!"

    roxxy "French skank!"

    roxxy "She's lucky I don't kick her ass right here and now!"

    show old_roxxy 29f
    show teacher 19 at right with dissolve
    bissette "Que se passe t-il?"

    bissette "What is all this yelling?!"

    show teacher 18
    show player 22
    show old_roxxy 30f
    roxxy "I cannot believe you made me do that!"

    roxxy "Do you know how embarrassed I am?!"

    show old_roxxy 29f
    show teacher 12
    bissette "Bah, don't be such a baby..."

    bissette "{b}[firstname]{/b} wrote a beautiful poem!"

    show teacher 19
    bissette "You should be apologizing to him for your clumsy reciting."

    show teacher 13
    show old_roxxy 31f
    roxxy "WHAT?! He's not the one you set up to look ridiculous!"

    show old_roxxy 3f
    show teacher 19
    bissette "Shush toi!!"

    bissette "It is not my fault you embarrass yourself with your poor French!"

    bissette "You are the one who refuses to do your studies!"

    show teacher 18
    show old_roxxy 30f
    roxxy "Grrrr!!!"

    roxxy "I won't forget this!"

    hide old_roxxy with dissolve
    show teacher 19
    bissette "Good! Remember it, as a reason to be taking your studies more seriously!"

    show teacher 18
    show player 25
    player_name "Wow, I've never seen her that mad before..."

    show player 5
    show teacher 12
    bissette "You should speak with her, {b}[firstname]{/b}."

    bissette "Teach her to be more in controlling of her temper..."

    show teacher 13
    show player 34
    player_name "..."
    show player 5
    show teacher 12
    bissette "... But first, we start your tutoring, yes?"

    show teacher 13
    show player 14
    player_name "Y-yeah! Okay!"

    show player 13
    show teacher 12
    bissette "Très bien! Come and sit with me!"

    scene black with fade
    return

label french_classroom_bissette_hand_in_poem_assignment_no_roxxy_sex:
    scene french_class_c
    show player 13 at Position (xpos=500)
    show old_roxxy 29f at left
    show teacher 2 at right
    with dissolve
    bissette "Sangat bagus!"

    bissette "{b}[firstname]{/b}, your French was perfect!"

    show teacher 1
    show player 14
    player_name "Terima kasih, {b}Nona Bissette{/b}."

    show player 13
    show teacher 19
    bissette "... And {b}Roxxy{/b}..."

    bissette "... Well, you tried."

    show teacher 18
    roxxy "Grrr..."

    show teacher 2
    bissette "Very well, that is it for today everybody."

    bissette "Remember to be {b}completing your homework{/b}, and I'll be seeing you tomorrow, yes?!"

    hide teacher with dissolve
    show player 25f with dissolve
    player_name "... {b}Roxxy{/b}, I'm sorry this-"

    show player 11f
    show old_roxxy 3f with dissolve
    roxxy "Diam!"

    show old_roxxy 29f
    show player 10f
    player_name "... I'm just trying to apolo-"

    show player 11f
    show old_roxxy 31f
    roxxy "I SAID SHUT YOUR MOUTH!"

    roxxy "I cannot believe she made me read that sappy bullshit in front of the entire class!"

    show old_roxxy 30f
    show player 24f
    roxxy "Ugh, and with YOU of all people!"

    roxxy "Disgusting!"

    roxxy "You're lucky I don't kick your ass right here and now!"

    show old_roxxy 29f
    show teacher 19 at right with dissolve
    bissette "Que se passe t-il?"

    bissette "What is all this yelling?!"

    show teacher 18
    show player 22
    show old_roxxy 30f
    roxxy "I cannot believe you made me do that!"

    roxxy "Do you know how embarrassing that was?!"

    show old_roxxy 29f
    show teacher 12
    bissette "Bah, don't be such a baby..."

    bissette "{b}[firstname]{/b} wrote a beautiful poem!"

    show teacher 19
    bissette "You should be apologizing to him for your clumsy reciting."

    show teacher 13
    show old_roxxy 31f
    roxxy "Apologize?! To him?! You're outta your damn mind!"

    show old_roxxy 3f
    show teacher 19
    bissette "Shush toi!!"

    bissette "It is not our fault you embarrass yourself with your poor French!"

    bissette "You are the one who refuses to do your studies!"

    show teacher 18
    show old_roxxy 30f
    roxxy "Grrrr!!!"

    roxxy "I won't forget this!"

    hide old_roxxy with dissolve
    show teacher 19
    bissette "Good! Remember it, as a reason to be taking your studies more seriously!"

    show teacher 18
    show player 25
    player_name "Wow, I've never seen her that mad before..."

    show player 5
    show teacher 12
    bissette "Do not concern yourself with her, {b}[firstname]{/b}."

    bissette "She'll get over this."

    show teacher 13
    show player 34
    player_name "..."
    show player 5
    show teacher 12
    bissette "Now, I think it's time we start your tutoring, yes?"

    show teacher 13
    show player 14
    player_name "Y-yeah! Okay!"

    show player 13
    show teacher 12
    bissette "Très bien! Come and sit with me!"

    scene black with fade
    return

label french_classroom_bissette_hand_in_assignment_intro_continue:
    scene studyclass02 with dissolve
    show text _ ("I spent the whole day trying to catch up to my studies...") as caption
    with fade
    pause

    scene studyclass03
    show text _ ("... Until the bell rang.") as caption
    with fade
    pause

    scene classroom_night
    show desk 16 at Position (xpos = 400, ypos = 768)
    with fade
    bissette "Your progress with the French is most impressive, {b}[firstname]{/b}."

    bissette "I think you will do very well on the big exam."

    show desk 15
    player_name "I hope so! I really need to pass this class."

    show desk 19 with dissolve
    bissette "Aww, mon bel homme..."

    show desk 20
    bissette "Do not be so anxious..."

    player_name "{i}*Meneguk*{/i}"

    show desk 16 with dissolve
    bissette "You know, I seem to recall promising you a special reward for reciting today, yes?"

    show desk 15
    player_name "Y-ya..."

    show desk 16
    bissette "Your poem really was beautiful, you know?"

    bissette "The French language was made for poetry. Don't you think?"

    show desk 15
    player_name "Y-ya, Bu."

    show desk 16
    bissette "I really liked the part you wrote about the kissing."

    show desk 15
    player_name "Oh... That part?"

    show desk 16
    bissette "Did you know the French kiss in a special way?"

    show desk 15
    player_name "Mmm... Huh? I mean, they do?"

    show desk 16
    bissette "Oui, they call it the French kiss and everything..."

    show desk 15
    player_name "Oh yeah, I've heard of that."

    show desk 16
    bissette "Have you tried the French kissing before?"

    return

label french_classroom_bissette_hand_in_poem_assignment_have_kissed:
    scene classroom_night
    show desk 15
    player_name "Y-yeah, a little bit."

    show desk 16
    bissette "Oh vraiment?"

    show desk 15
    bissette "You must show me what you know!"

    player_name "Benar-benar?"

    show desk 16
    bissette "Oui."

    show desk 27 at Position (xpos=342) with dissolve
    pause
    show desk 28 with dissolve
    pause
    show desk 31_32 with dissolve
    pause
    pause
    show desk 30
    bissette "{b}[firstname]{/b}!"

    bissette "I am most impressed!"

    bissette "Where did you learn to kiss like this?"

    show desk 29
    player_name "Oh, uhh... You know... Here and there..."

    show desk 30
    bissette "Hehe, fine. Keep your secrets. Just so long as you give me more kisses!"

    show desk 31_32 with dissolve
    pause
    pause
    return

label french_classroom_bissette_hand_in_poem_assignment_havent_kissed:
    scene classroom_night
    show desk 15 at Position (xpos=400)
    player_name "T-tidak..."

    show desk 16
    bissette "Oh, je dois t'apprendre!"

    show desk 15
    player_name "... You want to teach me?"

    show desk 16
    bissette "Oui."

    show desk 27 at Position (xpos=342) with dissolve
    pause
    show desk 28 with dissolve
    pause
    show desk 31_32 with dissolve
    pause
    pause
    show desk 30
    bissette "Très bien, {b}[firstname]{/b}..."

    bissette "You are a natural at this too it seems."

    show desk 29
    player_name "Y-yeah, thanks!"

    show desk 31_32 with dissolve
    pause
    pause
    return

label french_classroom_bissette_hand_in_poem_assignment_continue:
    scene classroom_night
    show desk 31_32 at Position (xpos=342)
    bissette "Hmm..."

    bissette "Mon bel homme..."

    bissette "You are getting me all excited..."

    player_name "{i}*Meneguk*{/i}"

    bissette "Perhaps we should be taking this-"

    show desk 33 with hpunch
    "{i}*Bzzt*{/i}"

    smith "{b}Miss Bissette{/b}!"

    "{i}*Bzzt*{/i}"

    "{i}*Bzzt*{/i}"

    smith "Where are you? Did you forget about our meeting?!"

    smith "Don't make me come down there and drag your scrawny ass to my office!"

    smith "GET UP HERE THIS INSTANT!"

    "{i}*Bzzt*{/i}"

    show desk 30
    bissette "Sacrebleu! What does she want now?!"

    bissette "{i}*Ahem*{/i} I'm sorry, {b}[firstname]{/b}. It seems we must cut this short once more."

    show desk 29
    player_name "It's alright, {b}Miss Bissette{/b}. I understand."

    show desk 31_32 with dissolve
    pause
    show desk 30
    bissette "Mmm, ta {b}bouche{/b} est magique!"

    show desk 29
    player_name "Hah?"

    show desk 30
    bissette "Your {b}mouth{/b} is magical!"

    show desk 29
    player_name "Oooh, {b}bouche{/b} means {b}mouth{/b}?"

    show desk 30
    bissette "Oui."

    show desk 27 with dissolve
    pause
    show teacher 10 at right
    show desk 5
    with dissolve
    bissette "I want you to {b}come to my office after class tomorrow{/b}."

    bissette "There's one more thing I want your help with before the exam."

    show teacher 9
    show desk 6
    player_name "Tentu saja."

    player_name "I'll see you tomorrow, {b}Miss Bissette{/b}."

    show desk 5
    show teacher 10
    bissette "Au revoir, mon bel homme."

    hide teacher with dissolve
    player_name "..."
    show desk 34
    player_name "Phew, that was awesome!"

    hide desk with dissolve
    return

label french_classroom_bissette_smith_final_report:
    scene french_class_c
    show teacher 1 at right
    show principal 27f at left
    show principal 27f at Position (xoffset=70)
    with dissolve
    smith "I don't know how you managed it but the grade point average is increasing."

    show principal 26f at Position (xoffset=70)
    show teacher 2
    bissette "I told you I could inspire them!"

    show teacher 1
    show principal 27f at Position (xoffset=70)
    smith "Yeah, well. Don't think it's an excuse to start slacking off!"

    show principal 26f at Position (xoffset=70)
    show teacher 2
    bissette "Don't worry, my students give me 110%%!"

    show player 14 at Position (xpos=500)
    player_name "Good morning, {b}Miss Bissette{/b}."

    show player 113
    player_name "... And {b}Mrs. Smith{/b}."

    show player 13
    show teacher 12
    bissette "Bonjour, {b}[firstname]{/b}."

    show teacher 13
    show player 114
    show principal 29f
    smith "Hmph."

    hide player with dissolve
    show principal 26f at Position (xoffset=70)
    show teacher 12
    bissette "... Some give me even more than 110%%!"

    show teacher 13
    show principal 29f
    smith "..."
    show principal 28f with dissolve
    smith "Just remember, I've got my eye on you!"

    hide principal
    hide teacher
    with dissolve
    return

label europe_map_dialogue:
    scene expression "backgrounds/location_school_french_map.jpg"
    player_name "..."
    player_name "Seems about right..."

    player_name "{b}Miss Bissette{/b} still hasn't noticed someone replaced her map of Yurup."

    pause
    $ A_europe.unlock()
    $ game.main()

label french_class_roxxy_lolipop_intro:
    scene french_class_c
    show old_roxxy 6f at Position (xpos=500)
    show teacher 19 at right
    with dissolve
    bissette "I hope you are to be having something for me today!"

    bissette "You cannot continue with the showing up empty-handed {b}Roxanne{/b}!"

    show teacher 18
    show old_roxxy 10f at Position (xoffset=9) with dissolve
    roxxy "Ugh, everyone calls me {b}Roxxy{/b}..."

    roxxy "Not {b}Roxanne{/b}!"

    show old_roxxy 6f with dissolve
    show teacher 5
    bissette "Why is this?"

    bissette "Your name is {b}Roxanne{/b}..."

    bissette "It is saying so in the school records!"

    show teacher 4
    show old_roxxy 7f
    roxxy "{i}*Huh*{/i}"

    show old_roxxy 5f
    roxxy "Look, I'll have my homework for you today, alright?!"

    show old_roxxy 10f at Position (xoffset=9) with dissolve
    roxxy "... Quit riding my ass, please!"

    show old_roxxy 6f with dissolve
    show teacher 18
    bissette "Hmm?"

    show teacher 19
    bissette "I am not riding anything..."

    show teacher 18
    show old_roxxy 7f
    roxxy "..."
    show teacher 19
    bissette "Just have your homework ready for class, yes?"

    show teacher 18
    show old_roxxy 11f at Position (xoffset=9) with dissolve
    roxxy "I said I'll have it!"

    show old_roxxy 9f at Position (xoffset=9)
    show teacher 19
    bissette "... Putain, mais quelle branleuse..."

    hide teacher with dissolve
    pause
    show player 13 at left
    show old_roxxy 10f at Position (xoffset=9)
    roxxy "Grr, stupid mush mouth..."


    show old_roxxy 7 at Position (xpos=600) with dissolve
    roxxy "!!!"
    show old_roxxy 10 at Position (xoffset=-9) with dissolve
    roxxy "You again!"

    show old_roxxy 3b with dissolve
    show player 11
    player_name "..."
    show old_roxxy 3c
    roxxy "Why does it seem like you're always around?!"

    show old_roxxy 3d
    show player 10
    player_name "I dunno?"

    player_name "It's not exactly a big school..."

    show player 5
    show old_roxxy 2
    roxxy "Well, I'm getting real sick of seeing your dorky-"

    show old_roxxy 1
    roxxy "..."
    show old_roxxy 1h
    roxxy "... Wait a second."

    roxxy "Do you have the {b}French homework{/b} for today?"

    show old_roxxy 1g
    show player 12
    player_name "... Ya."

    show player 5
    roxxy "..."
    show old_roxxy 47 with dissolve
    roxxy "{i}*Ehem*{/i}"

    show old_roxxy 48
    roxxy "Did I say dorky?"

    roxxy "'Cause what I meant to say was..."

    roxxy "... Handsome!"

    roxxy "Ya, itu dia!"

    show old_roxxy 47
    show player 11
    player_name "..."
    show old_roxxy 48
    roxxy "Have you been working out?"

    show old_roxxy 47
    show player 12
    player_name "Why are you acting weird?"

    show player 5
    roxxy "..."
    show player 12
    player_name "... Oh, I see."

    player_name "You want my {b}French homework{/b}."

    show player 90
    show old_roxxy 50b with dissolve
    pause
    show old_roxxy 50 with dissolve
    roxxy "Well, if you're offering..."

    show old_roxxy 49
    player_name "Hmph..."

    show player 30
    player_name "... And what do I get?"

    show player 90
    show old_roxxy 50
    roxxy "Uhh, the privilege of helping out the prettiest girl in school?"

    show old_roxxy 49
    player_name "..."
    show player 30
    player_name "You really think you're the prettiest girl in school?"

    show player 17
    player_name "Hah!"

    show old_roxxy 31
    roxxy "{i}*Gasp*{/i} Excuse me?!" with hpunch
    roxxy "... I'm gonna-"

    show old_roxxy 3d
    show player 12
    player_name "You're gonna what?!"

    show player 90
    show old_roxxy 29
    roxxy "..."
    show old_roxxy 3
    roxxy "Grr, are you gonna help me or not?!"

    show old_roxxy 29
    show player 35
    player_name "Hmm, I suppose I could let you copy my work."

    show player 34
    show old_roxxy 4
    return

label french_class_roxxy_lolipop_just_once:
    show player 12
    player_name "... But don't go thinking I'm gonna give you my work all the time."

    player_name "I might feel a little sorry for you, but it doesn't mean I'll let you walk all over me."

    show player 90
    show old_roxxy 2
    roxxy "Tch, YOU feel sorry for ME?!"

    show old_roxxy 1
    show player 10
    player_name "Well, you are on the verge of flunking out of school..."

    show player 5
    show old_roxxy 3c
    roxxy "Screw you, {b}[firstname]{/b}..."

    show old_roxxy 3d
    show player 11
    player_name "..."
    show player 10
    player_name "Do you want the {b}homework{/b} or not?"

    show player 5
    show old_roxxy 3
    roxxy "... Ya."

    show old_roxxy 3d
    show player 14
    player_name "... Say, \"Please.\""

    show player 13
    show old_roxxy 3c
    roxxy "!!!"
    show old_roxxy 3b
    roxxy "..."
    show player 12
    player_name "You know what... Forget it!"

    show player 90
    show old_roxxy 3
    roxxy "No, wait!"

    show old_roxxy 3b
    roxxy "..."
    show old_roxxy 3c
    roxxy "... Silakan."

    show old_roxxy 3d
    show player 12
    player_name "Please, what?"

    show player 90
    show old_roxxy 3
    roxxy "{i}*Huh*{/i}"

    show old_roxxy 3c
    roxxy "{i}Please{/i}, can I copy your homework."

    show old_roxxy 3b
    show player 4 with dissolve
    player_name "..."
    show player 12
    player_name "Ya baiklah."

    player_name "I'll go and {b}grab it out of my locker{/b}."

    player_name "Segera kembali."

    hide player with dissolve
    roxxy "..."
    show old_roxxy 3
    roxxy "Brengsek..."

    hide old_roxxy with dissolve
    return

label french_class_roxxy_lolipop_for_lolipop:
    show player 14
    player_name "If you give me your lollipop..."

    show player 13
    show old_roxxy 3c
    roxxy "Apa?"

    show old_roxxy 3d
    show player 14
    player_name "That lollipop that you were sucking on."

    show player 12
    player_name "Berikan padaku."

    show player 90
    show old_roxxy 10 at Position (xoffset=-9) with dissolve
    roxxy "..."
    show old_roxxy 11 at Position (xoffset=-9)
    roxxy "Dengan serius?"

    show old_roxxy 10 at Position (xoffset=-9)
    show player 17
    player_name "Ya."

    show player 13
    show old_roxxy 13 at Position (xoffset=-55) with dissolve
    roxxy "Uhh, that's really weird but okay..."

    show old_roxxy 12 at Position (xoffset=-55)
    show player 90
    player_name "..."
    show player 92
    player_name "It's not wet enough."

    show player 90
    show old_roxxy 13 at Position (xoffset=-55)
    roxxy "!!!"
    roxxy "Kamu menjijikkan!"

    show old_roxxy 12 at Position (xoffset=-55)
    show player 92
    player_name "Hey, you want the {b}homework{/b} or not?"

    show player 90
    roxxy "..."
    show old_roxxy 13 at Position (xoffset=-55)
    roxxy "Bagus!"

    show old_roxxy 7 with dissolve
    pause
    show old_roxxy 8 at Position (xoffset=-2) with dissolve
    pause
    show old_roxxy 12 at Position (xoffset=-55) with dissolve
    roxxy "Here ya go, perv!"

    show player 97
    show old_roxxy 3b
    with dissolve
    player_name "Terima kasih!"

    show player 93 with dissolve
    show player 94
    player_name "I'll go and {b}grab it out of my locker{/b}."

    player_name "Segera kembali."

    hide player with dissolve
    show old_roxxy 14
    roxxy "..."
    show old_roxxy 3c
    roxxy "Aneh..."

    hide old_roxxy with dissolve
    return

label frenchclassroom_roxxy_dexter_alcohol_fight:
    scene french_class_c
    show player 4 at left
    with dissolve
    player_name "(Hmm?)"

    show player 5 with dissolve
    player_name "( Is {b}Roxxy{/b} skipping class today? )"

    player_name "( That's not good, {b}Miss Bissette{/b} might have her expelled... )"

    show eve f_surprised a_cover with dissolve
    eve "{b}[firstname]{/b}!"

    show eve f_happy
    show player 14
    player_name "Hai, {b}Hawa{/b}."

    player_name "Ada apa?"

    show player 13
    eve "{b}Roxxy{/b} and {b}Dexter{/b} are going at it again on the {b}basketball court{/b}!"

    show player 11
    eve "C'mon, we're gonna miss it!"

    show player 10
    player_name "Lagi?!"

    player_name "Baiklah, ayo pergi."

    hide player
    hide eve
    with dissolve
    return

label frenchclassroom_roxxy_ask_exam_copy:
    scene french_class_c
    show old_roxxy 32 at right
    show teacher 2f at left
    with dissolve
    bissette "It is good your grades are finally improving, {b}Roxxy{/b}."

    bissette "... But I must remind you about the upcoming exams."

    bissette "They will make up a huge portion of your overall grade."

    bissette "If you fail to pass them, I fear we will have to suspend you from the cheerleading squad once more..."

    show teacher 3f
    bissette "Perhaps for good this time."

    show teacher 1f
    show old_roxxy 2b with dissolve
    roxxy "!!!"
    show teacher 2f
    bissette "You must be studying hard, yes?"

    bissette "The exam will cover all of the material we've learned this year."

    show teacher 3f
    bissette "Including the portions you neglected."

    show teacher 1f
    show old_roxxy 2c
    roxxy "... But-"

    roxxy "saya tidak..."

    show old_roxxy 3b
    show teacher 3f
    bissette "Ah ah ah!"

    bissette "Your time is wasted with this arguing, {b}Roxxy{/b}."

    show teacher 12f
    bissette "Better to spend your time studying, yes?"

    hide teacher with dissolve
    show old_roxxy 1o with dissolve
    pause
    show player 14 at left with dissolve
    player_name "Hey {b}Rox{/b}-"

    show player 11
    player_name "..."
    show player 10
    player_name "Apakah semuanya baik-baik saja?"

    player_name "You look kinda sad."

    show player 5
    show old_roxxy 3 with dissolve
    roxxy "Ugh, that mush mouth is gonna get me kicked off the team again!"

    show old_roxxy 3d
    show player 12
    player_name "Apa yang kamu bicarakan?"

    show player 5
    show old_roxxy 3
    roxxy "{b}Miss Bissette{/b}!"

    roxxy "If I don't pass her exam, they'll suspend from the cheerleading squad again."

    show old_roxxy 3d
    show player 12
    player_name "... I thought your grades were getting better?"

    show player 5
    show old_roxxy 2
    roxxy "Yeah, but I need to know the stuff we covered earlier this year."

    show old_roxxy 3c
    roxxy "What the hell am I going to do, {b}[firstname]{/b}?"

    roxxy "Cheerleading is the only part of school that I actually like."

    show old_roxxy 3d
    show player 10
    player_name "{b}Roxxy{/b}..."

    show player 5
    show old_roxxy 3
    roxxy "I can't exactly spend all my time studying either..."

    roxxy "... Not with everything that's been happening at home lately."

    show old_roxxy 32 with dissolve
    player_name "..."
    show old_roxxy 33
    roxxy "What am I going to do, {b}[firstname]{/b}?!"

    show old_roxxy 32
    show player 10
    player_name "Aku tidak tahu."

    show player 5
    show old_roxxy 33b
    pause
    show old_roxxy 32
    show player 4 with dissolve
    player_name "Hmm..."

    show player 35 with dissolve
    player_name "... Hey, wait a second!"

    player_name "Didn't your friends say something about {b}Mrs. Smith{/b} keeping copies of the exams in her house?"

    show player 13 with dissolve
    show old_roxxy 33
    roxxy "Hmm?"

    show old_roxxy 32
    show player 14
    player_name "{b}Becca{/b} and {b}Missy{/b}!"

    player_name "They were talking about it in the locker room the other day..."

    show player 13
    show old_roxxy 33
    roxxy "Were they?"

    roxxy "... I tend to ignore half of what those dumb skanks say."

    show old_roxxy 32
    show player 29 with dissolve
    player_name "Heh, I'm pretty sure that's what they were talking about."

    show player 13 with dissolve
    show old_roxxy 1l
    roxxy "... But you don't really think..."

    roxxy "I mean, it's gotta be made up, right?"

    show old_roxxy 1k
    show player 10
    player_name "Hmm, I dunno."

    player_name "{b}Mrs. Smith{/b} is a control freak after all."

    show player 14
    player_name "It's possible she keeps copies in her home."

    show player 13
    show old_roxxy 1g with dissolve
    roxxy "..."
    show old_roxxy 1h
    roxxy "Alright, I guess you'll just have to break in and find them for me..."

    show old_roxxy 1g
    show player 23
    player_name "What?! Me?!"

    show player 22
    show old_roxxy 2
    roxxy "Well, yeah!"

    show old_roxxy 1
    show player 12
    player_name "Mustahil!"

    player_name "It's your grades! You do it!"

    show player 90
    show old_roxxy 2c
    roxxy "You're gonna make me do it?!"

    show old_roxxy 2
    roxxy "I thought you were a real man..."

    show old_roxxy 1
    show player 5
    player_name "..."
    show old_roxxy 2
    roxxy "A real man wouldn't make the girl do dangerous stuff like that!"

    show old_roxxy 1
    show player 10
    player_name "Well, yeah but..."

    show old_roxxy 48 at Position (xoffset=-34) with dissolve
    show player 433
    roxxy "C'mon, {b}[firstname]{/b}. Please..."

    show old_roxxy 47 at Position (xoffset=-34)
    player_name "..."
    show old_roxxy 48 at Position (xoffset=-34)
    roxxy "Won't you be my Knight in Shinning armor one more time?!"

    show old_roxxy 47 at Position (xoffset=-34)
    show player 427
    player_name "aku uhh..."

    show player 434
    show old_roxxy 50c at Position (xoffset=-34) with dissolve
    roxxy "Just think about what {b}Becca{/b} and {b}Missy{/b} will say when I tell them how brave you are."

    roxxy "I can tell them all about it next time we're all at the beach together!"

    show old_roxxy 50 at Position (xoffset=-23) with dissolve
    roxxy "Remember the beach, {b}[firstname]{/b}?"

    roxxy "... Remember our little game of spin the bottle?"

    show old_roxxy 49 at Position (xoffset=-23)
    show player 427 with dissolve
    player_name "{i}*Gulp*{/i} Y-ya..."

    show player 434
    show old_roxxy 48 at Position (xoffset=-34)
    roxxy "You'll help me out, won't you?"

    show old_roxxy 47 at Position (xoffset=-34)
    show player 427 with dissolve
    player_name "Eh ya..."

    show player 434
    show old_roxxy 4 with dissolve
    roxxy "Hehehe! I knew you would!"

    roxxy "Terima kasih, {b}[firstname]{/b}!"

    show old_roxxy 1
    show player 24
    player_name "{i}*Huh*{/i}"

    show player 10
    player_name "I guess we should {b}head to her house this afternoon{/b}?"

    show player 5
    show old_roxxy 2c
    roxxy "Hah?!"

    show old_roxxy 2
    roxxy "No, that's a terrible idea!"

    show old_roxxy 1
    show player 12
    player_name "How is that a terrible idea?"

    player_name "She'll be here at school."

    show player 90
    show old_roxxy 2
    roxxy "You can't break into someone's house in broad daylight!"

    roxxy "The neighbors will call the cops on you for sure!"

    show old_roxxy 1
    show player 10
    player_name "Ya, tapi..."

    show player 5
    show old_roxxy 1b
    roxxy "You should break in {b}at night{/b}!"

    roxxy "{b}Mrs. Smith{/b} usually stays here late anyways, so you should have plenty of time."

    show old_roxxy 1
    show player 30
    player_name "Tunggu sebentar..."

    player_name "You are coming with me, right?"

    show player 90
    show old_roxxy 50 at Position (xoffset=-23) with dissolve
    roxxy "Pfft, this body wasn't built for running, {b}[firstname]{/b}..."

    show player 433
    roxxy "I'd just slow you down."

    show old_roxxy 49 at Position (xoffset=-23)
    show player 434
    player_name "..."
    show old_roxxy 48 at Position (xoffset=-34) with dissolve
    roxxy "Besides, a big strong man, like you..."

    roxxy "You don't need any help, do you?"

    show old_roxxy 47 at Position (xoffset=-34)
    show player 427
    player_name "... Nuh uh."

    show player 434
    show old_roxxy 2 with dissolve
    roxxy "Hehe, glad to hear it!"

    show old_roxxy 1
    show player 24
    player_name "{i}*Huh*{/i}"

    show player 10
    player_name "Okay then, I guess I will {b}break into Mrs. Smith's house tonight{/b}."

    show player 25
    player_name "... Alone."

    show player 5
    show old_roxxy 1b
    roxxy "You can do it, {b}[firstname]{/b}!"

    show old_roxxy 2
    roxxy "{b}Just don't forget the exams{/b}!"

    show old_roxxy 1
    show player 12
    player_name "Yeah, I won't."

    show player 90
    show old_roxxy 4
    roxxy "Semoga beruntung!"

    hide old_roxxy
    hide player
    with dissolve
    pause
    show player 37 with dissolve
    player_name "..."
    player_name "Whoa, did I really just agree to break into {b}Mrs. Smith{/b}'s house?!"

    show player 10 with dissolve
    player_name "How the hell did {b}Roxxy{/b} talk me into that?!"

    show player 4 with dissolve
    player_name "I remember thinking it was a bad idea and then..."

    show player 11 with dissolve
    pause
    show player 10
    player_name "payudara."

    show player 11
    pause
    show player 24
    player_name "She's crafty..."

    hide player with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
