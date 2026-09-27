label kha01_lewd_khadne:
    show khadne a_empty b_casual_sit_sad f_sad
    show khadne_arms_casual_sit_sad_a_sad as arms:
        xoffset 200
    with None
    show anon f_normal_low behind khadne:
        xoffset -200
    with {'master': dissolve}
    anon "Umm... {b}Khadne{/b}?"

    show khadne a_sad b_casual_sit_turn f_concerned
    hide arms
    with {'master': dissolve}
    khadne @ -m_talk "Hmm?"


    if M_khadne.get('chat', False):
        show khadne a_empty b_casual_sit_sad f_sad
        show khadne_arms_casual_sit_sad_a_sad as arms:
            xoffset 200
        with {'master': dissolve}
        khadne "Oh, hello {b}[firstname]{/b}."

        anon f_worried_low "I heard about the incident..."

        show anon:
            xoffset 0 xzoom -1 yalign 1. zoom .95
        with {'master': dissolve}
        anon "... How are you holding up?"

        khadne "Bad."

        pause
    else:

        khadne f_confused "Apa yang kamu lakukan disini?!"

        anon "{b}Nadya{/b} sent me."

        show anon a_up f_surprised_low
        show khadne a_empty b_casual_sit_sad f_sad
        show khadne_arms_casual_sit_sad_a_sad as arms:
            xoffset 200
        with {'master': dissolve}
        khadne "Ah."

        khadne "She sends you to replace me?"

        show anon a_sides f_worried_low:
            xoffset 0 xzoom -1 yalign 1. zoom .95
        with {'master': dissolve}
        anon "Tidak."

        show anon f_worried
        show khadne a_down b_casual_sit f_confused
        hide arms
        with {'master': dissolve}
        khadne "Kill me?"

        show anon a_surprised_up f_surprised
        with {'master': dissolve}
        anon "Apa?!"

        show anon a_surprised_up_both
        with {'master': dissolve}
        anon "No, no, nothing like that!"

        show khadne b_casual_sit_up f_annoyed
        with {'master': dissolve}
        khadne "I am not go back to Khakassia!"

        show anon a_hands_up f_worried_surprised
        with {'master': dissolve}
        anon "Whoa, calm down."

        show khadne f_sceptical
        anon "Silakan."

        show khadne f_concerned
        anon "Sit."

        show anon f_worried_low
        show khadne a_empty b_casual_sit_sad f_sad
        show khadne_arms_casual_sit_sad_a_sad as arms:
            xoffset 200
        with {'master': dissolve}
        pause
        show anon a_sides
        with {'master': dissolve}
        anon "Just, tell me what happened."


    khadne "I am failure!"

    anon "Hey, that's not true."

    show anon f_surprised_low
    khadne "It is!"

    show anon f_worried_low
    khadne "{b}Nadya{/b} gives me chance to make vodka and I blow up laboratory!"

    anon "That was just an accident."

    anon "Accidents happen."

    show anon f_worried
    show khadne a_down b_casual_sit f_concerned
    hide arms
    with {'master': dissolve}
    khadne "No, my father was right..."

    khadne "... Girl only good for one thing."

    show anon f_worried_low
    show khadne a_empty b_casual_sit_sad f_sad
    show khadne_arms_casual_sit_sad_a_sad as arms:
        xoffset 200
    with {'master': dissolve}
    khadne "And I'm not even good for that!"

    show anon a_khadne_shoulder_sad
    with {'master': dissolve}
    anon "Hei, ayolah..."

    khadne "The men always chooses {b}Katya{/b} or {b}Svetlana{/b} first..."

    khadne "... Never me."

    show anon f_worried_surprised_low
    khadne "It's because I am ugly."

    anon f_worried_low "You're not ugly, {b}Khadne{/b}."

    show anon f_worried_surprised_low
    khadne "saya!"

    anon "Listen to me!"

    show anon a_khadne_shoulder f_worried
    show khadne a_down b_casual_sit f_concerned behind anon
    hide arms
    with {'master': dissolve}
    anon "You are not ugly."

    anon "And you {i}can{/i} definitely make vodka."

    anon f_shy "That's why {b}Nadya{/b} sent me here..."

    anon "... Because she wants to make certain you keep brewing."

    khadne f_confused "She do?"

    anon "Heh, yes... She do."

    anon "She told me your vodka is the best she's ever tasted."

    khadne f_concerned_down "But I blow up lab!"

    anon "True..."

    anon "... But you didn't mean to, did you?"

    khadne f_concerned "Tidak."

    anon "See, it was just an accident."

    pause
    show anon a_frustrated f_confused
    with {'master': dissolve}
    anon "What happened anyway?"

    khadne f_annoyed_down "Ugh, one of the stills get clogged."

    show anon a_sides f_shy
    show khadne a_ball
    with {'master': dissolve}
    khadne f_normal "Pressure builds up inside and I was sleeping instead of watching."

    show khadne a_boom f_surprised
    with {'master': dissolve}
    khadne "Boom."

    show khadne f_normal
    anon "Jadi begitu."

    show anon a_thinking f_thinking
    show khadne a_down
    with {'master': dissolve}
    pause
    show anon a_sides f_confused
    with {'master': dissolve}
    anon "How come you were brewing so late in the evening?"

    khadne f_confused "Because what else do I do?"

    anon "I dunno... Get a hobby."

    show khadne f_sceptical
    anon "Go out and explore the town."

    khadne f_confused "Explore America?"

    khadne "Mengapa?"

    show anon a_surprised f_surprised
    with {'master': dissolve}
    anon "Mengapa?!"

    show anon a_sides f_happy
    with {'master': dissolve}
    anon "That's a silly question..."

    khadne f_sceptical @ -m_talk "..."
    anon "... Because there's lots of interesting things out there to see and do!"

    khadne "Seperti apa?"


    $ renpy.dynamic(opts=set())
    menu kha01_lewd_khadne.choice:
        set opts
        "The beach.":

            jump kha01_lewd_khadne.beach
        "The park.":

            jump kha01_lewd_khadne.park
        "The sports center.":

            jump kha01_lewd_khadne.arena
        "The bar.":

            pass

    anon f_normal "There's a pretty popular bar in town."

    anon "Lots of people there in the evenings."

    khadne f_bored "I work in distillery, full of vodka."

    khadne f_confused "Why I go bar?"

    anon f_shy "You know, to socialize."

    khadne "What is socialize?"

    anon "Interact with other people."

    anon "Make some new friends."

    anon f_happy "Maybe you'll meet a nice boy?"

    anon f_worried "Err, or a girl even?"

    anon f_shy "Depending on what you're into..."

    khadne f_concerned "They would not want me."

    show anon f_worried_surprised_low
    show khadne a_empty b_casual_sit_sad f_sad
    show khadne_arms_casual_sit_sad_a_sad as arms:
        xoffset 200
    with {'master': dissolve}
    khadne "No one ever wants me."


    menu:
        "Itu tidak benar!":
            show anon a_khadne_shoulder_sad f_flirt_low behind khadne
            with {'master': dissolve}
            anon "I'd want you."

            show anon a_khadne_shoulder f_shy
            show khadne a_down b_casual_sit f_sceptical behind anon
            hide arms
            with {'master': dissolve}
            khadne "You only say so because {b}Nadya{/b} make you."

            anon f_worried_surprised "No, I'm serious."

            show khadne f_concerned_down
            anon f_shy "I think you're very pretty."

            khadne @ -m_talk "..."
            khadne "It does not matter."

            show anon f_worried
            khadne "I am no good at pleasing people."

            khadne "They all say so."

        "Apa yang membuatmu mengatakan itu?":

            anon f_worried_low @ f_confused_low "Why would you think that?"

            khadne "I'm no good at pleasing people."

            show anon f_worried
            show khadne a_down b_casual_sit f_concerned
            hide arms
            with {'master': dissolve}
            khadne "Everyone say so."

            pause
            khadne f_concerned_down "Even if they do choose me, they never do so twice."


    anon "You make it sound sound like an obligation..."

    anon f_confused "... Do you even enjoy having sex?"

    khadne f_concerned "Mmm, not really..."

    khadne "... But {b}Svetlana{/b} says that not so important."

    anon "Well, that might be part of the problem right there."

    show anon a_thinking f_thinking
    with {'master': dissolve}
    pause
    show anon:
        xoffset 600 xzoom 1 yalign 1.
    with {'master': dissolve}
    pause
    show anon:
        xoffset 100 xzoom -1 yalign 1.
    with {'master': dissolve}
    pause
    show anon f_happy_surprised
    with {'master': dissolve}
    pause
    show anon a_sides f_happy
    with {'master': dissolve}
    anon "Bisakah kita mencoba sesuatu?"

    khadne f_sceptical @ -m_talk "Hmm?"

    anon "I'd like to try and help you."

    show anon a_give_me f_shy
    with {'master': dissolve}
    anon "But you'll have to trust me."

    khadne f_thinking_down @ -m_talk "..."
    show khadne a_down b_casual behind stool:
        xoffset 156 xzoom -1 zoom .95 yalign 1.
    with {'master': dissolve}
    pause
    show khadne a_up f_concerned
    with {'master': dissolve}
    pause
    show anon a_empty behind khadne
    show khadne a_hold_hand f_concerned_down
    with {'master': dissolve}
    anon "Ikutlah denganku."

    show anon b_empty f_happy:
        xoffset 600 xzoom 1 yalign 1.
    show khadne b_casual_dragged_anon f_concerned behind anon:
        xoffset 200 xzoom 1 yalign 1.
    with {'master': dissolve}
    khadne "Where we go?"

    hide anon
    hide khadne
    with {'master': dissolve}
    anon "To find a little privacy."


    scene expression background(576, 384, 2, l=L_warehouse_storage) as stage
    with fade
    show anon a_empty b_empty f_happy:
        xoffset -386 xzoom -1
    show khadne b_casual_dragged_anon f_surprised behind anon:
        xzoom -1
    with {'master': dissolve}
    pause
    show anon a_surprised b_dressed
    show khadne a_down b_casual:
        xzoom 1
    with {'master': dissolve}
    anon "Hmm, this'll do."

    show anon a_sides:
        xoffset 80 xzoom 1
    with {'master': dissolve}
    khadne f_confused "Okay, now what?"

    anon "Now I'm going to make you feel good."

    show anon a_undress_khadne1 b_bend f_shy:
        offset (234, 180)
    show khadne a_up f_surprised_down
    with {'master': dissolve}
    khadne "Oh, I dunno, I-"

    show anon f_shy_up
    khadne "No one has ever-"

    anon "Aku tahu."

    anon "But I'd like to try..."

    anon "... If you'll let me?"

    khadne f_concerned_down "B-baiklah."

    show anon a_undress_khadne2 f_shy_low
    show khadne b_shirt_leg
    with {'master': dissolve}
    pause
    show anon a_undress_khadne3 f_shy_down
    show khadne b_shirt
    with {'master': dissolve}
    pause

    call scene_khadne_crates_lick
    $ unlock_scene('khadne', '01_unlocked', variant='first')

    scene expression background(576, 384, 2, l=L_warehouse_storage) as stage
    show anon a_wipe_mouth b_bend f_happy_low:
        offset (234, 180)
    show khadne a_up b_shirt f_shy_down behind anon
    with fade
    khadne "Incredible..." (show_native="Neveroyatnyy...")
    anon f_shy_up "Cukup bagus, ya?"

    show anon a_undress_khadne3
    show khadne a_down
    with {'master': dissolve}
    khadne "I didn't know it-"

    show anon a_sides b_dressed f_shy:
        offset (100, 0)
    show khadne f_shy
    with {'master': dissolve}
    anon "Kamu baik-baik saja?"

    show anon a_empty b_empty f_surprised_low
    show khadne b_shirt_hug_anon_surprised:
        xoffset 100
    with {'master': dissolve}
    anon @ -m_talk "!!!"
    khadne "Haah... Haah..."

    anon f_worried_surprised_low "You're shaking!"

    khadne "I'm good..."

    khadne "... Just need a moment."

    show anon f_shy_low
    show khadne b_shirt_hug_anon
    with {'master': dissolve}
    anon "Heh, sure."

    anon "Take your time."

    pause
    khadne "T-thank you."

    anon "Terima kasih kembali."

    pause
    show anon a_sides b_dressed f_shy
    show khadne a_down b_shirt f_shy:
        xoffset 0
    with {'master': dissolve}
    khadne "Is that supposed to happen every time?"

    anon f_confused "What, the orgasm?"

    khadne f_happy "Ore-gasm?"

    anon f_shy "That was your first one, huh?"

    khadne "Ya."

    anon "I had a feeling..."

    khadne @ f_confused "So, it is?"

    anon f_confused @ -m_talk "Hmm?"

    khadne "Supposed to happen?"

    anon f_normal "Heh, well one would hope so..."

    anon "... There are a lot of factors but..."

    anon "... With the proper mindset and adequate stimulation..."

    pause
    show anon a_frustrated f_happy
    with {'master': dissolve}
    anon "... Boom."

    khadne f_laugh "Hehehe!"

    show anon a_sides
    show khadne a_boom
    with {'master': dissolve}
    khadne @ f_happy "Boom!"

    anon f_laugh "hehe!"

    show khadne a_down f_shy
    with {'master': dissolve}
    khadne "Can we do that again?"

    anon f_worried "What, now?"

    khadne "Ya."

    anon "Ehh..."

    anon f_shy "... I suppose."

    show anon a_undress_khadne3 b_bend f_shy_up:
        offset (234, 180)
    show khadne f_shy_down
    with {'master': dissolve}
    anon "But let's try and be quick, okay?"

    anon "{b}Nadya{/b} is waiting on me."

    khadne "Yes, quickly." (show_native="Da, bystro.")
    show anon a_jaw_out f_worried_low behind khadne
    with {'master': dissolve}
    pause

    scene expression background(576, 384, 2, l=L_warehouse_storage) as stage
    show anon a_jaw_in f_hurt:
        xoffset 100
    show khadne a_down b_shirt_disheveled f_shy_down
    with longfade
    pause
    show anon a_sides f_shy
    with {'master': dissolve}
    anon "Jadi..."

    show khadne f_shy
    anon "... Feeling better now?"

    khadne "Mmm, da."

    khadne "Body is like pudding."

    anon f_normal "Pudding, huh?"

    khadne f_happy "I think I sleep very well tonight."

    anon "Saya senang mendengarnya."

    pause
    anon f_confused "And about the brewing?"

    khadne f_concerned "If {b}Nadya{/b} wishes me to continue, then I will..."

    anon f_shy "You're a good brewer {b}Khadne{/b}..."

    anon "... Everyone can see that but you..."

    anon f_normal "... Have faith in yourself!"

    khadne f_happy "I will try."

    anon "Bagus."

    khadne f_concerned "Uhh, I will... see you, again?"

    anon "Of course, I'll be around."

    anon "We can have some more fun, yeah?"

    khadne f_shy "Yes, I like that."

    anon "Dingin."

    pause
    show anon a_wave
    with {'master': dissolve}
    anon "I'll see you soon then."

    show khadne a_idle f_happy:
        xoffset 550 xzoom -1
    hide anon
    with {'master': dissolve}
    khadne "Farewell, {b}[firstname]{/b}." (show_native="Proshchal'nyy privet, {b}[firstname]{/b}.")
    return


label kha01_lewd_khadne.arena:
    anon f_confused "You like sports?"

    khadne f_confused @ -m_talk "Hmm?"

    anon f_normal "There's always something going on at the arena."

    anon "Football, basketball, soccer..."

    khadne "Soccer?"

    show anon a_surprised
    with {'master': dissolve}
    anon "Yeah, you know... kicking the ball around."

    khadne f_sceptical "But kicking {i}is{/i} football."

    show anon a_behind_head f_shy
    with {'master': dissolve}
    anon "Oh, ehh... not here in America..."

    anon "... We call it soccer."

    khadne f_bored "That's dumb."

    show anon a_rub
    with {'master': dissolve}
    anon "You like European football then?"

    khadne f_annoyed "Ugh, no."

    khadne "Sports are boring."

    show anon a_sides f_skeptical
    with {'master': dissolve}
    anon @ -m_talk "..."
    show anon a_frustrated f_annoyed
    with {'master': dissolve}
    anon "Then why do you care what we call-"

    pause
    show anon a_sides f_unimpressed
    with {'master': dissolve}
    anon "Anda tahu, sudahlah."

    jump kha01_lewd_khadne.choice


label kha01_lewd_khadne.beach:
    anon f_normal "You could go check out the beaches."

    anon "There's a ton of them in Summerville."

    khadne f_bored "Ehh, I cannot swim."

    anon f_worried "Oh."

    anon f_shy "Well, you could learn..."

    show anon a_khadne_shoulder f_happy
    with {'master': dissolve}
    anon "... See, there's a hobby!"

    show anon f_shy
    pause
    show anon a_sides f_worried
    with {'master': dissolve}
    anon "Tidak?"

    khadne @ -m_talk "..."
    jump kha01_lewd_khadne.choice


label kha01_lewd_khadne.park:
    anon f_normal "There's lots of beautiful country around here."

    anon "Maybe go hiking in the woods near the park?"

    khadne f_confused "Alone?"

    khadne f_concerned "I get eaten by bear!"

    anon f_shy "Heh, I'm pretty sure there aren't any bears in Summerville."

    khadne f_confused "You know this for certain?"

    anon f_worried "Yah, tidak... tapi-"

    show anon a_surprised_shoulders f_surprised_teeth
    show khadne b_casual_sit_up f_annoyed
    with {'master': dissolve}
    khadne "I hate bears!"

    show anon a_surprised f_surprised
    with {'master': dissolve}
    khadne f_bored "No hiking."

    show anon a_sides f_worried
    with {'master': dissolve}
    anon "Benar."

    anon "Okay then."

    show khadne b_casual_sit
    with {'master': dissolve}
    anon "No hiking."

    jump kha01_lewd_khadne.choice
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
