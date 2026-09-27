label daisy_button_garden:
    scene expression background(752, 512, 2.8) as stage
    show daisy b_naked_behind_pickup
    show anon f_shy_low behind daisy with dissolve
    daisy "{i}*Humming*{/i}"

    pause
    anon f_normal_low "Hey, {b}Daisy{/b}."

    show anon f_normal
    show daisy b_naked_behind_look f_curious
    with {'master': dissolve}
    daisy @ -m_talk "Hmm?"

    anon "Whatcha doing?"

    show daisy b_naked_flowers f_normal
    with {'master': dissolve}
    daisy "Oh, hey, {b}[firstname]{/b}!"

    daisy "I'm looking for pretty flowers."

    anon f_normal "Oh ya?"



    return


label daisy_button_garden.sex:
    hide player
    show anon behind daisy
    with {'master': dissolve}

    if not M_daisy.once('garden_sex'):
        jump daisy_button_garden.first

    anon "I don't supposed you'd want to take a break for a bit, and umm... You know..."

    show anon f_shy_down
    daisy f_shy @ -m_talk "Hmm?"

    pause
    show daisy f_low
    pause
    daisy "Oh, I see..."

    daisy f_normal "... You wanna play hide the weasel?!"

    anon a_shy_neck f_shy "Uhh, ya."

    anon f_confused "Jika tidak apa-apa?"

    daisy "Of course it's okay!"

    show anon a_sides f_happy
    with {'master': dissolve}
    daisy "I like having sex with you, {b}[firstname]{/b}!"

    show daisy b_naked_behind_look f_happy
    with {'master': dissolve}
    daisy "But once you're done you have to help me pick flowers, okay?"

    anon "Y-yeah, I can totally do that!"


    call scene_daisy_sex_yard.repeat
    $ unlock_scene('Daisy', '02_unlocked')

    scene expression background(752, 512, 2.8) as stage
    show anon a_remove_shorts f_shy_down
    show daisy a_front b_naked_shy
    with fade
    daisy "Now you have to help me pick flowers, remember?"

    show anon a_sides f_normal
    with {'master': dissolve}
    anon "Of course, {b}Daisy{/b}... I'd like that."

    show anon f_happy
    show daisy a_up b_naked
    with {'master': dissolve}
    daisy "Hore!!"

    show anon f_grin
    hide daisy
    with {'master': dissolve}
    daisy "{i}*Humming*{/i}"

    anon @ -m_talk "( She's so adorable. )"

    return 'afterglow'


label daisy_button_garden.first:
    daisy "You wanna help me pick flowers?!"

    anon "Uhh, tentu saja."

    daisy "Yay!!!"

    show anon f_shy_low
    show daisy b_naked_behind_pickup
    with {'master': dissolve}
    daisy "I like yellow flowers the best because they smell like sunshine..."

    daisy "... But {b}Diane{/b} says I shouldn't play favorites or it will make the other flowers jealous."

    anon @ -m_talk "Mhmm."

    show anon o_boner
    with {'master': dissolve}
    daisy "White flowers smell like rain, so if I get both yellow and white, my loft starts to smell like morning sunshine after a rainy day..."

    daisy "... And I like that!"

    anon "Eh ya."

    show daisy b_naked_behind_look f_curious
    with {'master': dissolve}
    pause 1
    show daisy b_naked_flowers f_sad
    with {'master': dissolve}
    daisy "{b}[firstname]{/b}!!!"

    show anon a_surprised f_confused
    with {'master': dissolve}
    anon @ -m_talk "Hmm?"

    daisy "You're not listening to me!"

    show anon a_sides f_worried
    with {'master': dissolve}
    anon "Oh, I'm sorry, {b}Daisy{/b}..."

    anon "... I was just a little distracted by-"

    show anon f_shy_down
    pause
    show daisy f_surprised_low
    pause
    daisy f_low "Oh, begitu."

    show anon a_behind_head f_shy of_blush
    with {'master': dissolve}
    daisy f_normal "You need to use my hidey-hole again, huh?"

    anon "Err, I uhh..."

    daisy "It's okay, {b}[firstname]{/b}... I like using my floogina to help you."

    show anon a_sides f_confused -of_blush
    with {'master': dissolve}
    anon "{i}Va{/i}-gina, {b}Daisy{/b}."

    daisy "{i}Va{/i}-gina."

    show anon f_normal
    daisy f_normal "Hehe, that's such a silly word!"

    show daisy b_naked_behind_look f_happy
    with {'master': dissolve}
    daisy "Okay, I'm ready!"

    show anon a_surprised f_surprised
    with {'master': dissolve}
    anon "W-wait, you mean right here?!"

    show anon:
        xoffset -500
        xzoom -1
    with {'master': dissolve}
    daisy @ -m_talk "Mhmm."

    show anon:
        xoffset 0
        xzoom 1
    with {'master': dissolve}
    daisy "You can't pick flowers with a sick weasel, silly!"

    show anon a_shy_neck f_shy
    with {'master': dissolve}
    anon "Right, uhh... Yeah, okay."


    call scene_daisy_sex_yard
    $ unlock_scene('Daisy', '02_unlocked')

    scene expression background(752, 512, 2.8) as stage
    show anon a_remove_shorts f_shy_down
    show daisy a_front b_naked_shy
    with fade
    daisy "We should do this out here more often, don't you think?"

    show anon a_sides f_normal
    with {'master': dissolve}
    anon "Tentu saja."

    daisy f_laugh "hehe!"

    pause
    daisy f_normal "Now you have to help me pick flowers, remember?"

    anon "Of course, {b}Daisy{/b}... I'd like that."

    show daisy a_up b_naked f_laugh
    with {'master': dissolve}
    daisy "Hore!!"

    show anon f_happy
    show daisy a_sides f_normal
    with {'master': dissolve}
    daisy "Come on and I'll show you where my favorites grow!"

    show anon a_point
    with {'master': dissolve}
    anon "Lead the way."

    show anon a_idle
    hide daisy
    with {'master': dissolve}
    daisy "{i}*Humming*{/i}"

    anon f_grin @ -m_talk "( She's so adorable. )"

    return 'afterglow'
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
