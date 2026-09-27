label khadne_button_lab:
    $ renpy.dynamic(intimate=M_khadne.finished_state(S_kha01_lewd))

    if intimate:
        show anon a_wave behind khadne with {'master': dissolve}:
            align (1., 1.) xoffset 100 xzoom -1 zoom .95
        anon "Hey, {b}Khadne{/b}."

        khadne f_bored @ -m_talk "Hmm?"

        show anon a_sides
        with {'master': dissolve}
        khadne "Oh, hello, {b}[firstname]{/b}."

        khadne f_bored_down "Have you come for talking or is it break time?"


    elif not M_khadne.once('chat'):
        jump khadne_button_lab.intro
    else:

        show anon a_wave f_worried behind khadne with {'master': dissolve}:
            align (1., 1.) xoffset 100 xzoom -1 zoom .95
        anon "Halo lagi."

        khadne f_bored @ -m_talk "Hmm?"

        show anon a_sides
        with {'master': dissolve}
        khadne "Oh, it's you again."

        show khadne f_bored_down

    menu khadne_button_lab.choice:
        "Work?" if not intimate:
            jump khadne_button_lab.work

        "Settling in?" if intimate:
            jump khadne_button_lab.settle
        "Where are you from again?":

            jump khadne_button_lab.where
        "What's your story?":

            jump khadne_button_lab.story

        "Seks." if intimate:
            jump khadne_button_lab.sex
        "Saya harus pergi.":

            pass

    anon "Well, I'll leave you to it."

    anon "Take care of yourself, {b}Khadne{/b}."

    khadne @ -m_talk "Mhmm."

    return


label khadne_button_lab.first:
    anon f_flirt "So, I was thinking..."

    khadne @ -m_talk "Hmm?"

    anon "... Maybe we could both have some fun?"

    khadne f_confused "You mean... sex?"

    show anon f_flirt_grin o_boner
    with {'master': dissolve}
    anon @ -m_talk "Mhmm."

    show khadne a_up f_surprised_down
    with {'master': dissolve}
    pause
    khadne f_concerned "Oh, entahlah..."

    show anon f_worried
    khadne "... It always hurts... and you're..."

    khadne f_concerned_down "... S-so big."

    show anon a_surprised f_brag_down
    with {'master': dissolve}
    anon "Aku tahu."

    pause
    show anon a_handshake f_shy behind khadne:
        xoffset 250
    show khadne a_down f_concerned
    with {'master': dissolve}
    anon "But I'll be gentle."

    khadne @ -m_talk "..."
    show khadne f_concerned_down
    anon "And if you need me to slow down or stop, just say so and I will."

    show khadne f_concerned
    anon "Let me know how you're feeling, okay?"

    khadne "Anda akan melakukannya?"

    anon "Tentu saja."

    show khadne f_thinking_down
    pause
    khadne f_shy "Okay, we try."

    khadne "I trust you, {b}[firstname]{/b}."

    anon "You'll enjoy this, I promise."


    call scene_khadne_crates_sex
    $ unlock_scene('khadne', '02_unlocked', variant='first')

    scene expression background(576, 384, 2, l=L_warehouse_storage) as stage
    show anon a_sides f_shy:
        xoffset 100
    show khadne a_down b_shirt_disheveled f_horny behind anon

    if _return == 'inside':
        show anon b_dressed_catch_breath
        with fade
        anon "Haah... Haah..."

        show anon b_dressed
        with {'master': dissolve}
        anon "... How was that?"

        show anon a_empty b_empty f_surprised_low
        show khadne b_shirt_hug_anon_surprised:
            xoffset 100
        with {'master': dissolve}
        anon @ -m_talk "!!!"
    else:

        show khadne o_cum
        with fade
        anon "Heh, oops."

        show anon a_behind_head
        with {'master': dissolve}
        anon @ f_shy_low "Looks like I made a mess."

        pause
        show anon a_empty b_empty f_surprised_low
        show khadne b_shirt_hug_anon_surprised:
            xoffset 100
        with {'master': dissolve}
        anon @ -m_talk "!!!"
        khadne "Tidak apa-apa."

        show anon f_shy_low
        show khadne b_shirt_hug_anon
        with {'master': dissolve}
        khadne "Saya tidak keberatan."

        anon "Oh?"

        pause

    khadne "I didn't know it could feel like that."


    if _return == 'inside':
        show anon f_shy_low
        show khadne b_shirt_hug_anon
        with {'master': dissolve}

    anon "You liked it then?"

    khadne "Yes, very much."

    pause
    show anon a_sides b_dressed f_normal
    show khadne a_down b_shirt_disheveled f_horny:
        xoffset 0
    with {'master': dissolve}
    khadne "Can we do it again?!"

    anon f_surprised "W-what, now?"

    khadne @ -m_talk "Mhmm!"

    show anon a_rub f_shy
    with {'master': dissolve}
    anon "Eh, tidak."

    show khadne f_concerned
    with {'master': dissolve}
    pause
    show anon a_surprised_up_both f_worried_surprised
    with {'master': dissolve}
    anon "I mean, we can do it again, of course!"

    anon f_worried "Just, I need a little time..."

    show anon a_sides f_shy
    with {'master': dissolve}
    anon "... You know, to recuperate."

    khadne f_happy "Oh, hehe!"

    khadne "You come back soon then?"

    jump khadne_button_lab.resume


label khadne_button_lab.intro:
    show anon f_normal_low with dissolve:
        xoffset -210
    anon "Wow, you're working here too, huh?"

    show khadne b_casual_sit_turn f_confused
    with {'master': dissolve}
    pause
    show anon a_point f_normal:
        xoffset 400
    show khadne b_casual_sit
    with {'master': dissolve}
    anon "Man, you all really did a lot of work to this place..."

    hide anon
    with {'master': dissolve}
    pause
    show anon a_sides f_confused_back behind khadne:
        align (1., 1.) xoffset 100 xzoom -1 zoom .95
    with {'master': dissolve}
    anon "... Is this where you're distilling the alchohol?"

    khadne @ -m_talk "..."
    anon f_worried "You know, I'm surprised you all joined up with {b}Nadya{/b} after everything that happened..."

    anon "... None of you have homes to go back to?"

    khadne @ -m_talk "..."
    anon f_worried "Uhh, do you speak English?"

    show khadne a_clipboard f_bored_down
    with {'master': dissolve}
    khadne "Yes, little bit."

    khadne "{b}Katya{/b} teaches me."

    anon f_normal "Oh bagus."

    anon f_happy "I thought I might have been talking to myself there for a minute."

    pause
    anon f_worried "Hehe, ya."

    show anon a_shy_neck
    with {'master': dissolve}
    anon "So, ehh..."

    anon "... You'll have to forgive me, I'm not sure I got your name during all the commotion last time..."

    show anon a_handshake f_normal
    with {'master': dissolve}
    anon "... I'm {b}[firstname]{/b}."

    khadne "{b}Khadne{/b}."

    show anon a_sides f_confused
    with {'master': dissolve}
    anon "Cagney?"

    khadne f_annoyed "{b}Kad-Nee{/b}."

    show anon a_hands_up f_surprised
    with {'master': dissolve}
    anon "Whoa, alright... {b}Khadne{/b}."

    anon f_worried "Saya minta maaf."

    show khadne f_bored_down
    pause
    show anon a_sides
    with {'master': dissolve}
    pause
    anon @ f_confused "You don't talk much, do you, {b}Khadne{/b}?"

    show khadne a_lap f_annoyed
    with {'master': dissolve}
    khadne "{i}*Sigh*{/i} What are you wanting from me?"

    show anon a_rub f_shy
    with {'master': dissolve}
    anon "Hey, I'm just trying to be friendly."

    khadne f_sceptical "Why for?"

    anon f_confused "Why am I being friendly?"

    show anon a_sides
    with {'master': dissolve}
    khadne "Yes, why?!"

    anon "I dunno... I guess, because that's what people do?"

    khadne "Does {b}Nadya{/b} send you to spy on me?"

    show anon a_surprised f_surprised
    with {'master': dissolve}
    anon "Apa-"

    show anon a_up
    with {'master': dissolve}
    anon "Tidak!"

    show anon a_give_me f_shy
    with {'master': dissolve}
    anon "I just thought, maybe we could be friends... that's all."

    khadne f_confused "Mengapa?"

    show anon a_sides
    with {'master': dissolve}
    anon "Kenapa tidak?"

    khadne f_disgusted_down "Because I am not girl men use for talking."

    show khadne a_sad f_concerned_down
    with {'master': dissolve}
    khadne "Not me."

    anon f_skeptical "What the heck does that mean?"

    khadne "{i}*Sigh*{/i} It's-"

    show anon f_confused
    show khadne a_lap f_thinking_down
    with {'master': dissolve}
    khadne "What is word?!" (show_native="Chto takoye slovo?")
    pause
    khadne f_confused "Complicated?"

    show khadne a_lap f_annoyed
    with {'master': dissolve}
    khadne "Gah, you ask lot of question!"

    anon f_normal "Hehe, aku tahu."

    anon f_shy "Maaf."

    show anon a_point_back f_confused
    with {'master': dissolve}
    anon "I can stop bothering you, if you want?"

    show khadne f_sceptical
    pause
    khadne f_confused "Are you being true?"

    show anon a_sides
    with {'master': dissolve}
    anon "Hah?"

    khadne f_sceptical "You're not spy?"

    anon "Tidak."

    anon "Just a friendly guy trying to be nice to a pretty girl."

    pause
    show khadne a_clipboard f_bored_down
    with {'master': dissolve}
    khadne "American men are weird." (show_native="Amerikanskiye muzhchiny strannyye.")
    khadne "Baiklah."

    anon @ -m_talk "Hmm?"

    khadne f_bored "You can stay..."

    khadne f_sceptical "... But know that I watch you, okay?"

    khadne "Bukan urusan yang lucu!"

    anon "Y-ya, oke."

    show khadne f_bored_down
    jump khadne_button_lab.choice


label khadne_button_lab.lick:
    show anon a_undress_khadne3 b_bend f_happy_low:
        offset (234, 180)
    show khadne f_horny_down
    with {'master': dissolve}
    pause

    call scene_khadne_crates_lick.repeat
    $ unlock_scene('khadne', '01_unlocked', variant='repeat')

    scene expression background(576, 384, 2, l=L_warehouse_storage) as stage
    show anon a_wipe_mouth b_bend f_happy_low:
        offset (234, 180)
    show khadne a_up b_shirt_disheveled f_horny_down behind anon
    with fade
    khadne "Incredible..." (show_native="Neveroyatnyy...")
    show anon a_sides b_dressed f_shy:
        offset (100, 0)
    show khadne f_horny
    with {'master': dissolve}
    anon "Feeling better now?"

    show anon a_empty b_empty f_surprised_low
    show khadne b_shirt_hug_anon_surprised:
        xoffset 100
    with {'master': dissolve}
    anon @ -m_talk "!!!"
    khadne "Ya."

    show anon f_happy_low
    show khadne b_shirt_hug_anon
    with {'master': dissolve}
    pause
    show anon a_sides b_dressed f_normal
    show khadne a_down b_shirt_disheveled f_horny:
        xoffset 0
    with {'master': dissolve}
    khadne "Terima kasih, {b}[firstname]{/b}."

    khadne "You are wonderful man."

    show anon a_behind_head f_shy
    with {'master': dissolve}
    anon "{i}*Gulp*{/i} Eheh, you're welcome."

    show anon f_shy_left
    with {'master': dissolve}
    pause
    show anon a_sides f_shy
    with {'master': dissolve}
    anon "S-so?"

    anon f_confused "Back to work?"

    show khadne f_concerned_down
    pause
    khadne "Ya."

    show khadne f_concerned
    anon f_normal "Dingin."

    khadne f_confused "I will see you again soon?"

    anon "Tentu saja."

    show khadne f_happy
    pause
    khadne "Oke."

    show anon a_wave
    with {'master': dissolve}
    anon "Have a good rest of your day, {b}Khadne{/b}."

    show khadne a_idle:
        xoffset 550 xzoom -1
    hide anon
    with {'master': dissolve}
    khadne "Farewell, {b}[firstname]{/b}." (show_native="Proshchal'nyy privet, {b}[firstname]{/b}.")
    return 'afterglow'


label khadne_button_lab.settle:
    anon f_confused "All settled in?"

    khadne "Ya."

    khadne f_normal "But I would welcome opportunity to make new recipies."

    khadne f_confused "Perhaps you could speak with {b}Nadya{/b} about procurring new ingredients?"

    show anon a_surprised f_surprised
    with {'master': dissolve}
    anon "What, me?!"

    khadne f_normal "Ya."

    show anon a_sides f_confused
    with {'master': dissolve}
    anon "What makes you think she would listen to me?"

    show khadne a_lap f_confused
    with {'master': dissolve}
    khadne "You are her sex pet, no?"

    show anon a_surprised_up_both f_shock
    anon "!!!" with hpunch
    show anon a_surprised_up_both f_surprised
    with {'master': dissolve}
    anon "Sex pet?!"

    show anon a_up f_worried_surprised
    with {'master': dissolve}
    anon "Itu bukan-"

    pause
    show anon a_sides f_skeptical
    with {'master': dissolve}
    anon "Wait, who told you that?!"

    khadne f_bored "Everyone knows you are her favorite."

    khadne "She tell you fuck, you fuck."

    show khadne a_clipboard f_bored_down
    with {'master': dissolve}
    khadne "She tell you lick, you lick."

    anon f_annoyed @ -m_talk "..."
    khadne "She tell you suck {b}Svetlana{/b} feet and eat {b}Katya{/b} butthole, you say, \"Where to start?\""

    show anon a_point2
    with {'master': dissolve}
    anon "Oke, pertama-tama..."

    show khadne f_bored
    anon "... There is no butthole eating going on up in here."

    pause
    show anon a_crossed
    with {'master': dissolve}
    anon "And second, {b}Nadya{/b} and I are partners..."

    show khadne a_shrug f_eyeroll
    with {'master': dissolve}
    khadne "Okay, fine!"

    khadne f_normal "Partner."

    show anon f_worried
    show khadne a_lap
    with {'master': dissolve}
    khadne "Point is, she maybe listen to you."

    show anon a_behind_head f_worried_left
    with {'master': dissolve}
    anon "Ehh, not really."

    anon f_shy "When it comes to her business dealings, I'm really more like a silent partner."

    show anon a_sides
    show khadne a_clipboard f_bored_down
    with {'master': dissolve}
    khadne "Ugh, I'm so bored!" (show_native="Ugh, mne tak skuchno!")
    jump khadne_button_lab.choice


label khadne_button_lab.sex:
    anon f_normal "Break time sounds good!"

    khadne f_normal "Just let me check the stills before we go."

    anon "Tentu."

    show anon a_point_back
    show khadne f_horny_down
    with {'master': dissolve}
    anon "I'll meet you in the storage."

    hide anon
    with {'master': dissolve}
    khadne @ -m_talk "Mhmm."


    scene expression background(576, 384, 2, l=L_warehouse_storage) as stage
    show anon:
        xoffset 100
    with fade
    show khadne a_down b_casual f_happy behind anon with dissolve
    show anon a_empty b_empty f_surprised_low
    show khadne b_casual_hug_anon_surprised:
        xoffset 100
    with {'master': dissolve}
    khadne "MM."

    khadne "I'm so happy you come!"

    anon f_shy_low "Y-ya, aku juga."

    show khadne b_casual_hug_anon
    with {'master': dissolve}
    khadne "MM."

    show anon a_sides b_dressed f_normal
    show khadne a_down b_casual f_happy:
        xoffset 0
    with {'master': dissolve}
    anon "Wow, you're really into this..."

    khadne "Ya!"

    show khadne a_undress1 f_horny
    with {'master': dissolve}
    khadne "Now that I know how good it can be."

    show anon f_happy_low
    show khadne b_shirt_bend
    with {'master': dissolve}
    pause
    show anon f_flirt_grin
    show khadne a_down b_shirt
    with {'master': dissolve}

    menu:
        "cunnilingus.":
            jump khadne_button_lab.lick
        "Seks.":

            pass

    if not M_khadne.once('had_sex'):
        jump khadne_button_lab.first

    anon f_flirt "How about some sex this time?"

    khadne f_confused "Seks?"

    khadne f_horny "Ya, tolong."

    anon f_happy "Manis!"


    call scene_khadne_crates_sex.repeat
    $ unlock_scene('khadne', '02_unlocked', variant='repeat')

    scene expression background(576, 384, 2, l=L_warehouse_storage) as stage
    show anon a_sides f_shy:
        xoffset 100
    show khadne a_down b_shirt_disheveled f_horny behind anon

    if _return == 'inside':
        show anon b_dressed_catch_breath
        with fade
        anon "Haah... Haah..."

        show anon b_dressed
        with {'master': dissolve}
        anon "... How was that?"

        show anon a_empty b_empty f_surprised_low
        show khadne b_shirt_hug_anon_surprised:
            xoffset 100
        with {'master': dissolve}
        anon @ -m_talk "!!!"
        khadne "So wonderful!"

        show anon f_shy_low
        show khadne b_shirt_hug_anon
        with {'master': dissolve}
    else:

        show khadne o_cum
        with fade
        anon "Heh, oops."

        show anon a_behind_head
        with {'master': dissolve}
        anon "I made a mess again."

        pause
        show anon a_empty b_empty f_surprised_low
        show khadne b_shirt_hug_anon_surprised:
            xoffset 100
        with {'master': dissolve}
        anon @ -m_talk "!!!"
        khadne "Tidak apa-apa."

        show anon f_shy_low
        show khadne b_shirt_hug_anon
        with {'master': dissolve}
        khadne "Saya tidak keberatan."

        anon "Oh?"

        pause
        khadne "That was wonderful!"


    anon "Yeah, I enjoyed it too."

    pause
    show anon a_sides b_dressed f_normal
    show khadne a_down b_shirt_disheveled f_happy:
        xoffset 0
    with {'master': dissolve}
    khadne "You'll come back soon?"

    label khadne_button_lab.resume:
    anon "Ya, sepenuhnya."

    khadne f_horny "Benar sekali."

    pause
    show anon a_wave
    with {'master': dissolve}
    anon "Have a good rest of your day, {b}Khadne{/b}."

    show khadne a_idle f_happy:
        xoffset 550 xzoom -1
    hide anon
    with {'master': dissolve}
    khadne "Farewell, {b}[firstname]{/b}." (show_native="Proshchal'nyy privet, {b}[firstname]{/b}.")
    return 'afterglow'


label khadne_button_lab.story:
    anon f_confused "How did you come to be here?"

    khadne f_annoyed "That is not a nice story."

    anon f_worried "Well, you don't have to tell me if it makes you uncomfortable..."

    anon f_shy "... Only if you want to."

    pause
    show khadne a_lap f_confused
    with {'master': dissolve}
    khadne "Why you care about this?"

    show anon a_surprised
    with {'master': dissolve}
    anon "Well, I just-"

    anon "Find you interesting is all."

    show anon a_sides
    with {'master': dissolve}
    khadne "Interest in me?"

    anon @ -m_talk "Mhmm."

    show khadne f_normal
    pause
    show khadne a_clipboard f_bored_down
    with {'master': dissolve}
    khadne "You are strange man."

    anon f_normal "Saya?"

    khadne "Ya."

    khadne "I come from boring place."

    pause
    khadne "Very small."

    khadne "Tradition important."

    anon f_confused "Oh?"

    khadne f_annoyed "But not for me."

    khadne "I do not want fat husband and house full of baby..."

    khadne f_bored_down "... So I run away."

    anon f_surprised "Benar-benar?"

    khadne @ -m_talk "Mhmm."

    anon f_confused "Lalu apa yang terjadi?"

    khadne "Bad man drug and sell me to Bratva."

    show anon a_cannoli_gobble f_shock
    with {'master': dissolve}
    khadne "Then I am made slave and toy for pleasure."

    show anon a_sides f_worried_surprised
    with {'master': dissolve}
    anon "Oh benar."

    anon f_worried "Maaf."

    khadne f_normal "Mengapa?"

    khadne "You did not do these things."

    anon "Well, I know... but still... I'm sorry that those things happened to you."

    pause
    show khadne a_shrug
    with {'master': dissolve}
    khadne "Meh."

    show khadne a_clipboard f_bored_down
    with {'master': dissolve}
    khadne "It is past."

    khadne f_normal "Now I work for {b}Nadya{/b}."

    khadne "Girl who makes vodka."

    khadne f_happy "Tradition be damned."

    anon f_normal "Heh, good for you."

    khadne "Ya."

    pause
    show khadne a_clipboard f_bored_down
    with {'master': dissolve}
    khadne "If only it wasn't so boring!"

    jump khadne_button_lab.choice


label khadne_button_lab.vodka:
    anon f_confused "So what does {b}Nadya{/b} have you doing in here?"

    khadne "We make vodka."

    show anon a_rub f_shy
    with {'master': dissolve}
    anon "Well, yeah... I see that."

    show anon a_point2
    with {'master': dissolve}
    anon "But I mean, you specifically..."

    anon f_confused "... What do {i}you{/i} do?"

    show anon a_sides
    with {'master': dissolve}
    khadne f_bored "I make recipe for worker."

    khadne "They mash and distill."

    khadne "I watch and make certain there's no funny business."

    show khadne f_bored_down
    anon "Wait a second, this vodka is made using your recipe?"

    khadne "Ya."

    anon "Where'd you learn to do that?"

    khadne "Home."

    anon "You made vodka back home?"

    khadne "Tidak."

    khadne f_annoyed "My father and uncle make vodka."

    khadne "Recipe is family secret."

    show khadne f_annoyed_down
    anon "Ah, so they taught you?"

    khadne @ f_bored_down "Tidak."

    show khadne a_lap f_annoyed
    with {'master': dissolve}
    khadne "I just tell you, it family secret."

    anon "Yeah, but you're part of the family, aren't you?"

    khadne f_eyeroll "Yes, but I am girl."

    show khadne a_finger f_annoyed
    with {'master': dissolve}
    khadne "Father say:, \"{b}Khadne{/b}, girl does not make vodka!\""

    show anon a_surprised f_surprised
    show khadne a_clipboard f_bored_down
    with {'master': dissolve}
    anon "Apa?!"

    show anon a_sides f_confused
    with {'master': dissolve}
    anon "Kenapa?"

    show khadne a_shrug f_bored
    with {'master': dissolve}
    khadne "Because father say."

    anon @ -m_talk "..."
    show khadne a_clipboard f_bored_down
    with {'master': dissolve}
    anon "Well, that's not very progressive."

    show anon a_crossed f_thinking
    with {'master': dissolve}
    pause
    show anon a_frustrated f_confused
    with {'master': dissolve}
    anon "So how did you learn the recipe?"

    khadne f_bored "Uncle has loose lips when he drink too much arkhi."

    show anon a_sides
    show khadne a_lap
    with {'master': dissolve}
    khadne "Half the village learn recipe when he goes on a bender." (show_native="Half the village learn recipe when he's nazhratsya.")
    anon "Arkhi?"

    anon "Apa itu?"

    show khadne a_clipboard f_bored_down
    with {'master': dissolve}
    khadne "Is vodka made from yak milk."

    anon f_disgusted "Y-yak milk?"

    khadne @ -m_talk "Mhmm."

    anon f_worried "Itu menjijikkan!"

    jump khadne_button_lab.choice


label khadne_button_lab.where:
    anon f_confused "Where was it you said you were from?"

    khadne "Khakassia."

    khadne "I come from Khakassia."

    anon f_shy "See, I've never even heard of Khakassia..."

    anon f_confused "... It's part Russia?"

    khadne "Ya."

    anon f_shy "Dingin."

    pause
    show anon f_worried
    pause
    anon f_confused "But like, where in Russia?"

    khadne "Southern Siberia."

    anon "Siberia, huh?"

    anon f_normal "I bet it's real cold there."

    khadne "Hmm, not so bad as Northern Siberia."

    show anon a_behind_head f_shy
    with {'master': dissolve}
    anon "Well, yeah..."

    anon "... I sorta figured that."

    khadne f_bored "You ask silly questions..."

    show anon a_sides f_worried
    with {'master': dissolve}
    khadne "... I just give answer."

    show khadne f_bored_down
    anon @ -m_talk "..."
    jump khadne_button_lab.choice


label khadne_button_lab.work:
    if not M_khadne.once('chat_work'):
        jump khadne_button_lab.vodka

    anon f_confused "So, how's work?"

    khadne "Boring."

    anon "Oh?"

    khadne f_bored "I thought making vodka would be more fulfilling."

    show khadne a_lap
    with {'master': dissolve}
    khadne "It's very tedious."

    anon f_shy "Heh, yeah... work can be like that."

    show khadne a_clipboard f_bored_down
    with {'master': dissolve}
    jump khadne_button_lab.choice
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
