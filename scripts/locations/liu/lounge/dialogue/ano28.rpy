label ano28_clue_liu_lounge:
    scene location_apt_hall2_204_closeup as stage
    show location_apt_hall2_204_closeup_door1 as door behind stage
    show location_apt_hall2_204_closeup as doorframe:
        crop (768, 0, 256, 768)
        right
    show anon a_knock with dissolve
    "{i}*Ketuk* *Ketuk*{/i}"

    show anon a_sides with dissolve
    pause
    show anon a_wave
    show location_apt_hall2_204_closeup_door2 as door
    with dissolve
    show liu a_sides b_robe_hair f_surprised behind doorframe with {'master': dissolve}
    liu "{i}*Terkesiap*{/i}"

    show anon f_surprised
    liu "{b}[firstname]{/b}!!"

    show anon a_empty b_empty f_disgusted_wince
    show liu b_robe_hug:
        xoffset 0
    anon @ -m_talk "Oof!" with hpunch
    show anon f_shy of_blush with {'master': dissolve}
    anon "H-hei."

    show anon a_sides b_dressed
    show liu a_shy b_robe_hair f_happy:
        xoffset -70
    with dissolve
    liu f_nervous "Won't you come inside?"

    hide liu with dissolve
    anon f_flirt "Tentu saja."

    hide anon with dissolve

    scene expression background(768, 384, 2) as stage
    show liu a_shy b_robe_hair f_happy
    with fade
    show anon a_sides f_shy_low of_blush with dissolve
    anon f_shy_low "Wow, look at you..."

    show liu f_nervous_lipbite_back
    anon "... That robe is..."


    scene expression game.timer.image('location_liu_lounge_close{}')
    show liu b_robe_front1 f_normal_down
    with fade
    anon "... Wow."

    liu f_normal "Y-you like it?"

    anon "Saya menyukainya!"

    liu "Hehe, really?"

    anon "You look amazing!"

    pause
    anon "Show it off for me a little..."

    show liu b_robe_front2 with dissolve
    liu "What, like this?"

    anon "Ya."

    anon "Sama seperti itu."

    pause
    anon "Beautiful."

    liu f_normal_down "hehe!"


    scene expression background(768, 384, 2) as stage
    show anon a_sides f_shy_low o_boner of_blush
    show liu a_shy b_robe_hair
    with fade
    liu f_nervous "I was just warming the kettle for tea."

    liu "Would you like to sit and have some?"

    show liu f_surprised_down
    anon "Tea, huh?"

    anon f_flirt "You know, there's a lot of things I'd like to do with you right now..."

    show liu f_sexy_lipbite
    anon "... But sitting for tea is pretty far down the list."

    liu f_sexy "Oh?"

    pause
    liu "And what do you want to do with me?"

    anon "I've got several ideas, actually..."

    anon "... Most of which start with sliding you out of that robe."

    show liu f_sexy_lipbite
    pause
    liu f_sexy a_undress1 "Maksudmu..."

    show anon a_surprised_up f_surprised_low
    show liu a_undress2 b_robe_open
    with dissolve
    pause .1
    show anon f_normal_low m_talk
    show liu a_undress3 b_naked_hair
    with dissolve
    pause .1
    show anon f_flirt_low
    show liu a_undress4
    with dissolve
    pause .1
    show anon a_sides f_shy_low
    show liu a_sides
    with dissolve
    liu "... Seperti ini?"

    show liu f_sexy_lipbite
    anon f_shy -m_talk @ -m_talk "{i}*Gulp*{/i} Mhmm."

    liu a_hips f_sexy "Sekarang apa?"

    anon f_flirt "N-now we need to get you into the bedroom."

    liu a_timid f_nervous_down "Oh ya?"

    show anon f_flirt_grin
    pause
    anon f_flirt "Oh ya."

    show anon:
        xoffset 350
    show liu f_surprised
    with fastdissolve
    show anon a_empty f_flirt_low o_empty:
        xoffset 500
    show liu b_naked_anon_arms f_shocked:
        xoffset 500
    liu "Whoa!!!" with hpunch
    liu f_laugh "hehe!"

    pause
    liu f_normal "You're stronger than you look!"

    anon f_shy_low "Oh, please... you're light as a feather."

    liu f_happy_down_back "Heh, that's nice of you to say."

    pause
    liu f_worried "I'm not used to this kind of excitement, you know?"

    liu "You make me feel... wanted."

    anon f_flirt_low "Oh, I definitely want you."

    show liu f_happy
    anon "You're a very desirable woman, {b}Liu{/b}."

    show liu f_sexy_lipbite
    pause
    liu f_sexy "And I want you, {b}[firstname]{/b}..."

    liu "... Take me any way you want."

    anon f_normal_low "Aduh, astaga..."

    show liu f_laugh
    anon f_happy_low "... Untuk bercinta!"

    hide anon
    hide liu
    with {'master': dissolve}
    liu "hehe!"


    scene expression game.timer.image('location_liu_bedroom_bed_after{}')
    show anon b_liu_naked f_shy_high
    show liu b_bed_naked_kiss
    with fade
    pause
    show liu b_bed_naked_sit with dissolve
    liu "I'm so happy you're back in my bed, {b}[firstname]{/b}!"

    show liu b_bed_naked_kiss with dissolve
    liu "MM."

    pause
    show liu b_bed_naked_sit with dissolve
    liu "It's all I've thought about since that day you chased my husband away!"

    anon "You are so beautiful, {b}Liu{/b}!"

    show liu b_bed_naked_kiss with dissolve
    pause

    call scene_liu_sex_bedroom.first
    $ unlock_scene('liu', '01_unlocked', variant='first')

    scene expression background(480, 384, 2.5, l=L_liu_bedroom) as stage
    show anon b_dressed_changing2:
        xoffset -350
        xzoom -1
    with fade
    show anon a_towel b_shorts f_looking_down with dissolve
    show anon b_dressed_changing with dissolve
    show anon a_sides b_dressed f_normal with dissolve
    pause
    show anon a_idle b_dressed with {'master': dissolve}:
        xoffset 150
        xzoom 1
    anon "Heh, I'm glad we got to finish this time."

    show liu a_undress3 b_naked_disheveled
    with {'master': dissolve}
    liu "Ya, aku juga."

    show liu a_undress2 b_robe_disheveled_open f_happy_closed
    with {'master': dissolve}
    liu "We can do this anytime you want, now that my bastard husband is gone."

    show liu a_undress1 b_robe_disheveled f_happy
    with {'master': dissolve}
    liu "Thank you for that."

    show anon f_flirt
    show liu a_shy
    with {'master': dissolve}
    anon "It was my pleasure, {b}Liu{/b}."

    pause
    liu a_shy f_curious "So I will see you again, right?"

    anon f_normal "Ya, tentu saja."

    anon "You've got my number."

    liu f_happy_closed "Saya bersedia."

    show liu f_happy
    pause
    liu f_nervous_down "But you can always come by, you know?"

    liu f_nervous "Or come and see me at the bank, if you want."

    anon "Okay, cool."

    anon "Saya akan."

    show anon a_wave
    show liu f_happy
    with dissolve
    pause
    show anon a_sides with dissolve:
        xoffset -400
        xzoom -1
    pause .25
    anon f_surprised_low "Hey, isn't that-"

    show liu a_sides f_confused_down
    show anon b_dressed_pickup:
        xoffset -500
    with dissolve
    liu @ -m_talk "Hmm?"

    show liu f_curious
    show anon b_dressed a_painting_hold f_confused:
        xoffset -400
    with dissolve
    pause
    show anon f_normal_left
    liu f_worried "Oh, yeah... that's the painting {b}Frank{/b}-"

    liu "Err, I mean, the painting your father sent me."

    show anon f_normal:
        xoffset 100
        xzoom 1
    with dissolve
    anon "You want me to hang it up for you?"

    liu f_nervous "N-no, you don't have to do that... you've already done so much, I wouldn't want-"

    anon "It's fine, I don't mind."

    liu f_worried "Kamu tidak?"

    anon "I'm actually kinda excited to see it."

    pause
    anon f_flirt "If it reminded him of you, it must be really beautiful."

    liu f_sexy "Aww, {b}[firstname]{/b}... you're too good to me."

    anon f_normal "Let's check it out."


    scene location_liu_bedroom_cutscene01
    show text _ ("I tore at the wrapping like a kid on christmas day, eager to feel some small connection with my father once again.") as caption
    with fade
    pause
    hide caption with dissolve
    show text _ ("But it seemed he had one last surprise in store for me.") as caption with dissolve
    pause

    scene expression background(480, 384, 2.5, l=L_liu_bedroom) as stage
    show anon b_dressed a_painting_hold f_surprised_down:
        xoffset 100
    show liu a_sides b_robe_disheveled f_normal_down
    with fade
    liu @ -m_talk "Hmm?"

    liu "Something fell out."

    anon "Apa itu?"

    show liu b_robe_bend with dissolve
    pause
    show anon f_surprised_low
    show liu a_envelope b_robe_disheveled f_surprised_down
    with dissolve
    liu f_surprised "It's a letter."

    anon f_surprised "From my father?!"

    show anon b_dressed_pickup with {'master': dissolve}
    liu f_confused_down @ -m_talk "Mhmm."

    show anon a_sides b_dressed f_surprised_low
    show liu a_envelope_open
    with dissolve
    pause .2
    show liu a_letter with dissolve
    pause
    liu "\"Dear Liu,\""

    liu "\"You have been both a blessing and an anchor to me these past months, as I traversed these dark and troubled waters.\""

    show anon f_worried
    liu f_worried_down "\"I'm truly sorry that I could not return your affections and it pains me deeply to see how you suffer each day at the hands of your pig-headed, weasel of a husband.\""

    liu "\"In another time, another life, who knows? ... Things might have been different for us.\""

    liu f_ashamed_down "Oh, {b}Frank{/b}..."

    show liu f_worried
    anon f_surprised "Is that it?"

    liu "No, there's more."

    show anon f_worried
    liu f_worried_down "\"All I can do now is leave you this painting.\""

    show anon f_shy
    show liu f_nervous_down o_blush
    with {'master': dissolve}
    liu "\"May it always be a reminder that you are a beautiful and compassionate woman, who is deserving of love.\""

    liu "\"I know that one day you will find what you're looking for.\""

    show anon f_shy_down of_blush
    show liu f_nervous
    with {'master': dissolve}
    pause
    liu f_nervous_down "\"And now I hope you'll forgive me for asking one last favor of you.\""

    show liu f_confused_down -o_blush
    with {'master': dissolve}
    liu "\"I fear my end is rapidly approaching and that, because of my stupidity and poor judgement, my friends and family will fall on hard times in the wake of my passing.\""

    show anon f_worried -of_blush
    with {'master': dissolve}
    liu f_worried_down "\"There's nothing I can do to warn them or even soften the blow without putting their lives at risk.\""

    show anon f_worried_surprised
    pause
    show anon f_surprised
    liu "\"But if you could just pass one message on to my son, I would forever be grateful to you.\""

    show liu f_worried
    anon "A message?!"

    show liu f_worried_down
    liu "\"Take care of yourself, {b}Liu{/b}.\""

    liu f_worried "\"With love, {b}Frank{/b}.\""

    pause
    anon "W-what's the message?"

    liu f_worried_down "Hmm..."

    pause
    liu f_confused "... \"My legacy lies with The Dink.\""

    show anon f_confused
    pause
    liu f_curious "What the heck is a Dink?"

    anon f_worried "It's the name of our old fishing boat."

    liu "{b}Frank{/b} owned a fishing boat?"

    anon f_worried_low "It's just a tiny little thing... barely big enough for two people."

    anon f_worried "But he built it together with my grandfather when he was little."

    liu f_nervous "Aww, that's really sweet."

    anon f_confused "I wonder what he meant by, \"My Legacy\"?"

    show liu f_confused_down
    pause
    anon f_thinking @ -m_talk "Hmm."

    liu f_worried "That's all he wrote."

    anon f_confused "I need more time to think on it."

    pause
    show anon b_dressed_pickup
    show liu a_envelope_open f_nervous_down
    with {'master': dissolve}
    anon "C'mon, let's get this painting hung up."

    show anon a_painting_hold b_dressed f_grin
    show liu a_envelope f_normal
    with {'master': dissolve}
    liu f_happy "Y-ya, oke."


    scene location_liu_bedroom_frame_closeup with longfade
    anon "Wow, this really is a beautiful painting!"

    liu "Yeah, it really is."

    pause
    anon "It suits you."

    pause

    scene expression background(464, 392, 5, l=L_liu_bedroom) as stage
    show anon b_dressed a_sides f_normal:
        xoffset 150
    show liu b_robe_disheveled a_sides f_happy:
        xoffset -150
    with fade
    anon "And I'm sure my father was right."

    anon "You're gonna find what you're looking for someday."

    liu f_sexy "Maybe I already have."

    anon f_happy "Ya mungkin."

    hide anon
    show liu b_robe_disheveled_kiss:
        xoffset 75
    with dissolve
    liu "MM."

    pause

    scene expression background(l=L_apt, o=1) as stage with longfade
    show anon f_thinking_down with dissolve
    anon @ -m_talk "( I can't believe I didn't think to check {b}Liu{/b}'s painting for clues earlier... )"

    anon f_normal @ -m_talk "( ... Of course {b}Dad{/b} would hide something there! )"

    anon @ -m_talk "( Just like the {b}Rump{/b} photo from the evidence box. )"

    pause
    anon f_confused @ -m_talk "( But I'm not sure I know what he means by: \"My legacy lies with The Dink\"."

    pause
    anon @ -m_talk "( Maybe I should go check it out? )"

    anon f_normal @ -m_talk "( {b}Dad{/b} always stored the boat in our back yard {b}near my old tree house{/b}... )"

    anon @ -m_talk "( It's still there as far as I know. )"

    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
