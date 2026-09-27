label ano18_yell_rump_kitchen:
    scene expression background(944, 440, 6., l=L_rump_lobby)
    show anon with dissolve
    anon @ f_thinking a_thinking -m_talk "{i}*Mengendus*{/i}"

    anon @ -m_talk "( Hmm, this must be the kitchen. )"

    rump "This is just unacceptable and I won't stand for it."

    anon f_surprised @ -m_talk "( !!! )"
    show anon b_dressed_catch_breath with dissolve
    pause .5

    scene expression background(712, 408, 3.5, l=L_rump_kitchen)
    show rump f_angry
    show consuela b_dressed_mop f_annoyed_down:
        flip
    with dissolve
    rump "I'm the most important man in this shitty little town and that means I have appearances to maintain..."

    rump @ a_finger "One of which is an immaculate home, {b}Consuela{/b}!"

    consuela "It's already clean..." (show_native="Ya esta limpio...")
    rump "Are you the right person for this job?"

    consuela "S-si, {b}Mister Rump{/b}."

    rump "'Cause I've got no problem sending you back to whatever third world shithole you crawled out of!"

    consuela f_sad_down @ f_sad "No, please!"

    consuela "saya membersihkan."

    rump "You know, there's fifty million women on the other side of that border who would kill to be in your position."

    show consuela f_eyeroll
    pause
    show consuela f_annoyed_down
    pause
    rump f_suspicious "Where's the new uniform I bought you?"

    show consuela b_dressed f_sad a_work3 with dissolve
    consuela "U-uniform?"

    pause
    consuela a_show_clothes "I wear."

    rump f_angry "That's not the one I bought."

    consuela f_annoyed a_hips "You would have me dress like a stripper!" (show_native="¡Me harías vestir como una stripper!")
    consuela "Do I look like a whore to you?!" (show_native="¿Te parezco una puta?")
    rump @ a_yell "ENGLISH, {b}Consuela{/b}!"

    consuela "I no wear."

    consuela "Show too much."

    rump "You will wear it!"

    show consuela f_sad
    rump @ f_lips a_finger "Remind me, who the boss is here, {b}Consuela{/b}?"

    consuela "Y-you boss, {b}Mister Rump{/b}..."

    rump "That's right, I'm the boss!"

    rump "I make the rules here, I own you!"

    consuela f_angry "Own me?!" (show_native="¿Poseerme?")
    consuela "You do not own me, you disgusting old man!" (show_native="¡No me posees, viejo cochino!")
    rump f_suspicious "Apa itu tadi?"

    consuela f_sad @ f_sad_down "Please, no."

    consuela "{b}Mister Rump{/b}, I no wear."

    rump f_angry @ f_smirk "Heh, it's cute that you think you have a say in this..."

    show consuela f_sad_down
    rump "Either wear the uniform I bought for you or wear nothing at all, the choice is yours."

    consuela f_angry "You're a pig!" (show_native="¡Eres un cerdo!")
    rump @ a_finger "Goddamnit, ENGLISH!!"

    consuela f_sad_down @ -m_talk "..."
    rump @ f_eyeroll "If you're going to sneak your way into our country and be a drain on our economy, the least you can do is learn the fucking language!"

    consuela f_sad "{i}*Sigh*{/i} I wear."

    show consuela b_dressed_mop f_sad_down:
        unflip
        xpos -500
    with dissolve
    consuela "Tomorrow."

    rump "Itu lebih baik."

    pause
    show rump f_smirk
    pause
    rump f_suspicious "Is {b}Ricardo{/b} working today?"

    show consuela b_dressed f_sad:
        flip
        xpos 0
    with dissolve
    consuela "Eh?"

    rump "{b}R-I-C-A-R-D-O{/b}?"

    consuela @ f_smirk "Oh, eh... Si, he trim bushes."

    show consuela b_dressed_mop f_annoyed_down with dissolve
    rump "The ones in the back?"

    consuela "Si, {b}Mister Rump{/b}."

    rump f_suspicious "Didn't he just trim those the other day?!"

    consuela "Your wife probably wanted to leer at him some more..." (show_native="Tu esposa quiere mirarlo...")
    rump f_normal "Go and tell him I want the car washed instead."

    consuela "Si, {b}Mister Rump{/b}."

    show consuela b_dressed f_annoyed with dissolve
    consuela "I tell."

    hide consuela with dissolve
    pause
    rump @ a_yell "You know you're lucky I'm such a gracious boss!"

    pause
    rump f_smirk "And that you were born with such a delicious booty..."


    scene expression background(944, 440, 6., l=L_rump_lobby)
    show anon f_worried
    with fade
    anon @ -m_talk "( Wow, that poor woman. )"

    anon @ -m_talk "( It seems {b}Mayor Rump{/b} is kind of an asshole when he's out of the public eye... )"

    anon @ -m_talk "( At least it looks like the coast is clear now. )"

    anon f_grin @ -m_talk "( I wonder what other secrets this place holds? )"

    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
