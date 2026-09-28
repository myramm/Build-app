label liu_button_bedroom:
    show anon a_wave with dissolve
    anon "Hey, {b}Liu{/b}."
    show anon a_sides f_worried_surprised
    show liu b_robe_hair f_happy behind anon
    with {'master': dissolve}
    liu "Hey, {b}[firstname]{/b}."
    anon f_worried -m_talk "S- Sorry, I didn't mean to make you get up!"
    liu "Don't worry, it was time I streched my legs anyway."
    show anon a_idle f_normal with dissolve

    menu liu_button_bedroom.choice:
        "Dad's money." if M_anon.is_state(S_ano28_cash):
            jump ano28_cash_liu_money
        "What were you reading?":

            jump liu_button_bedroom.novels
        "I love what you've done with the place.":

            jump liu_button_bedroom.decor
        "Sex":

            jump liu_button_bedroom.sex
        "I'll see you later.":

            pass

    show liu a_sides f_worried with {'master': dissolve}
    liu "Leaving so soon?"
    show anon a_behind_head f_shy with {'master': dissolve}
    anon "Yeah, I've got things to do."
    liu f_worried_down "Aww, okay..."
    show liu b_robe_hug
    show anon b_empty f_surprised
    with dissolve
    pause
    show anon f_shy
    liu "You'll come back again, yeah?"
    show anon a_beer_cheer b_dressed behind liu
    show liu a_cover b_robe_hair f_worried:
        xoffset -300
    with {'master': dissolve}
    anon "Of course."
    liu "Bye, {b}[firstname]{/b}."
    anon "Later, {b}Liu{/b}."
    hide anon with dissolve
    return


label liu_button_bedroom.book:
    anon "What's this one about?"
    show liu a_sides f_surprised with {'master': dissolve}
    liu "You really wanna know?"
    anon "Yeah, I do."
    show liu f_nervous o_blush with {'master': dissolve}
    liu "Oh, umm... Okay."
    show liu f_nervous_down with dissolve:
        xoffset 575
        xzoom -1
    pause .3
    show anon a_surprised f_surprised_low
    show liu b_robe_bend
    with dissolve
    pause
    show anon a_sides f_flirt
    show liu a_book b_robe_hair f_happy_down_back
    with dissolve
    pause .3
    show anon f_normal
    show liu f_nervous:
        xoffset 0
        xzoom 1
    with {'master': dissolve}
    liu "It's about this baker's daughter in eighteenth century China, who has a passion for baking."
    liu "And people come from all over the country to taste her delicious sweet buns."
    anon f_happy "Mmm, I love sweet buns!"
    liu "Hehe, me too."
    pause
    show liu f_worried -o_blush with {'master': dissolve}
    liu "But then one day her father has a heart attack and dies..."
    anon f_surprised "Oh, no!"
    liu "... And her evil step mother sells her hand in marriage to a rival baker."
    liu f_annoyed "This big fat disgusting pig of a man, named Dong Zhuo."
    anon f_thinking_down @ -m_talk "( Hmm, this is starting to remind me of someone... )"
    liu "He keeps her chained to the oven in his kitchen and forces her to bake sweet buns all day, with no breaks."
    show anon f_shock with hpunch
    pause
    anon f_worried "That's awful!"
    liu "Yes."
    liu "He gets very rich off her delicious buns and every night, this poor woman cries herself to sleep, dreaming of the day she will be free of him."
    anon "Then what happens?"
    liu f_normal "One day, a mysterious stranger arrives in town and asks the baker if he would be willing to sell him the recipe."
    liu f_worried "Of course, the baker refuses and mocks the stranger... \"What could a wretch like you have to offer a man such as me?\""
    anon f_surprised "He insulted the stranger?!"
    liu @ -m_talk "Mhmm."
    show anon f_worried
    liu "The stranger said, \"Indeed, I have nothing that could equal the value of your delicious sweet buns recipe...\""
    liu f_happy "But he knew the baker's greed was great, and so he offered him a wager instead."
    show anon f_confused
    liu "\"If you can knock me down, I'll give you my sword...\""
    liu "The stranger held up his katana, made of the finest steel; it's handle wrapped in luxurious silk."
    liu "\"...and if you can't, you'll share your secret.\""
    show anon f_disgusted
    liu f_gross "The fat man licked his lips, hungrily."
    liu f_curious "\"All I need do is knock you down?\""
    show anon f_happy
    liu f_nervous "He laughed, knowing he outweighed the stranger thrice over... and accepted the wager."
    anon f_normal "I have a feeling he's going to regret that."
    liu f_happy "Indeed."
    liu "You see, it turns out, the mysterious stranger was none other than Zhang Yan, a notorious bandit king, and one of the greatest fighters in the region."
    anon f_worried "Uh oh."
    liu "The baker tried and tried to knock the man down, but he never once succeeded."
    show anon a_pocket with {'master': dissolve}
    liu "Hours later, covered in sweat, the baker finally admitted defeat."
    liu f_annoyed "\"But the last laugh is mine!\" he shouted. \"For you see, my secret is that I do not know the recipe!\""
    show anon f_surprised
    liu f_confused "\"How can this be?\" the stranger asked."
    liu f_ashamed_down "The baker bade him enter his kitchen and gaze upon the poor woman, chained to her oven."
    liu f_normal "Immediately, Zhang Yan fell to his knees, overwhelmed by her beauty and baking skills."
    liu f_happy "\"Sweet lady, I am humbled to be in your presence!\""
    liu "\"Your delicious sweet buns are the envy of all other baked goods!\""
    liu "The baker scoffed at the display, and Zhang Yan whirled, enraged at the state of the poor woman."
    show anon f_shock
    liu "He buried his katana in the fat man's chest before carrying the woman out of there."
    anon f_brag "Whoa, awesome!"
    show liu a_mouth_cover f_laugh with {'master': dissolve}
    liu "Hehe, yeah."
    show liu a_book f_happy with {'master': dissolve}
    liu "That's my favorite part!"
    anon "Then what happens?"
    liu f_normal "I'm not sure yet."
    liu "Right now, they've only just arrived at his bandit camp and..."
    show anon f_confused
    show liu f_nervous_down o_blush:
        xoffset 575
        xzoom -1
    with {'master': dissolve}
    liu "... Ummm..."
    show anon f_confused_low
    show liu b_robe_bend
    with dissolve
    show anon f_confused
    show liu a_sides b_robe_hair f_nervous_lipbite_back
    with dissolve
    pause
    show liu a_shy with {'master': dissolve}:
        xoffset 0
        xzoom 1
    liu f_nervous "... They've just made love... for the first time."
    anon f_normal "Well, I can see why you like it."
    liu f_happy "You can?"
    anon "Yeah."
    anon "You'll have to let me know how it ends."
    liu f_happy_excited_closed "O-okay, I will!"
    liu f_nervous_down "You're such a wonderful man, {b}[firstname]{/b}!"
    anon "And you're a wonderful woman, {b}Liu{/b}."
    show liu f_happy -o_blush with {'master': dissolve}
    jump liu_button_bedroom.choice


label liu_button_bedroom.decor:
    show anon f_normal_high with dissolve
    pause
    anon "You've really improved the vibe in here!"
    show anon f_normal
    liu f_happy "Heh, thanks!"
    show liu a_hips f_annoyed
    with {'master': dissolve}
    liu "Hopefully one day I can get rid of that stupid statue too..."
    show anon f_disgusted with {'master': dissolve}:
        xoffset -500
        xzoom -1
    liu "... It's so freaking heavy!"
    show anon f_confused with {'master': dissolve}:
        xoffset 0
        xzoom 1
    anon "I could try and move it, if you want?"
    show liu a_sides f_normal with {'master': dissolve}
    liu "No, no... I'll call some movers or something."
    show anon with dissolve:
        xoffset -500
        xzoom -1
    pause
    anon "Well, at least you made some improvements to it."
    show anon f_laugh
    liu f_laugh "Hehehe!"
    anon "Hahaha!"
    show anon f_normal with dissolve:
        xoffset 0
        xzoom 1
    liu f_happy "Yeah, it's nice having all his toys gone..."
    liu f_gross "... And that dreadful bomb replica, eugh!"
    jump liu_button_bedroom.choice


label liu_button_bedroom.novels:
    show anon a_point f_normal with {'master': dissolve}
    anon "What's that you were reading?"
    show anon a_idle
    show liu f_nervous_back o_blush
    with {'master': dissolve}
    liu "Oh, umm... heh, it's nothing."
    anon f_confused @ -m_talk "Huh?"
    liu f_nervous "I'd rather not say."
    anon "How come?"
    liu a_shy "Because... it's embarrassing!"
    anon "Embarrassing?"
    pause
    anon f_brag "Ah, c'mon... You can tell me."
    show liu f_nervous_lipbite
    pause
    liu f_nervous "You promise you won't laugh?"
    anon "I promise."
    show liu f_nervous_lipbite
    pause
    liu f_nervous "I like to read..."
    pause
    liu f_nervous_back "... Cheesy romance novels."
    anon a_behind_head f_confused "Cheesy romance novels?"
    liu f_nervous "Y-yeah."
    show liu -o_blush
    show anon a_sides f_normal
    with dissolve

    menu:
        "What is this one about?":
            jump liu_button_bedroom.book
        "There's nothing wrong with that.":

            pass

    anon "Lots of people enjoy those."
    show liu a_mouth_cover f_laugh with {'master': dissolve}
    liu "Yeah, but I REALLY enjoy them..."
    anon "Oh?"
    show liu a_sides f_worried_down with {'master': dissolve}
    liu "Heh, all those years living with {b}Kim{/b}..."
    show liu a_cover f_worried
    with {'master': dissolve}
    liu "... These books were the only excitement I ever had."
    anon f_worried "Yeah, that's not surprising."
    liu f_ashamed_down @ -m_talk "..."
    anon a_idle f_normal "You'll have to tell me about them sometime."
    show liu a_shy f_surprised with {'master': dissolve}
    liu "Really?"
    anon "Sure, I'd be interested to learn more about them."
    liu f_nervous "Y-yeah, okay."
    liu f_happy "I'd like that."
    jump liu_button_bedroom.choice


label liu_button_bedroom.sex:
    $ renpy.dynamic(bedroom=player.location == L_liu_bedroom)

    liu "Is something on your mind?"
    anon f_confused @ -m_talk "Hmm?"
    liu "You're thinking about something... I can see it in your eyes."
    anon f_shy "Heh, you... actually."
    show liu f_curious o_blush with {'master': dissolve}
    liu "Me?"
    anon f_flirt "I'm thinking about how much I'd like to slide you out of that robe..."
    show liu f_sexy_lipbite
    pause

    if bedroom:
        liu f_sexy a_undress1 "You mean..."
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
        with {'master': dissolve}
        liu "... Like this?"
        show liu f_sexy_lipbite
    else:

        show anon f_shy_high
        hide liu
        with {'master': dissolve}
        liu f_sexy "You mean..."

        scene expression background(768, 384, 2) as stage
        show liu a_undress1 b_robe_hair f_sexy_lipbite
        with fade
        pause .1
        show liu a_undress2 b_robe_open with dissolve
        pause .1
        show liu a_undress3 b_naked_hair with dissolve
        pause .1
        show liu a_undress4 with {'master': dissolve}
        liu f_sexy "... Like this?"
        show liu a_sides f_sexy_lipbite
        with dissolve
        pause
        show anon a_sides f_shy_low o_boner of_blush with {'master': dissolve}

    anon f_shy -m_talk @ -m_talk "Mhmm."
    liu a_hips f_sexy "Now what?"

    menu:
        "Let's take this to the bedroom." if not bedroom:
            pass
        "Let's take this to the bed." if bedroom:
            pass

    show anon behind liu:
        xoffset 350
    show liu f_surprised
    with fastdissolve
    show anon a_empty f_flirt_low o_empty:
        xoffset 500
    show liu b_naked_anon_arms f_shocked:
        xoffset 500
    liu "Oh!" with hpunch
    liu f_laugh "Hehehe!"
    liu f_happy "I love it when you do this!"
    anon f_shy_low "Yeah?"
    liu f_sexy "It makes me so wet for you."
    show liu f_sexy_lipbite
    anon f_normal_low "Aww, jeez..."
    show liu f_laugh
    anon f_happy_low "... To the love making!"
    hide anon
    hide liu
    with {'master': dissolve}
    liu "Hehe!"

    scene expression game.timer.image('location_liu_bedroom_bed_after{}')
    show anon b_liu_naked f_shy_high
    show liu b_bed_naked_kiss
    with fade
    pause
    show liu b_bed_naked_sit with dissolve
    liu "Oh, you make me so happy, {b}[firstname]{/b}!"
    show liu b_bed_naked_kiss with dissolve
    liu "Mmm."
    pause
    show liu b_bed_naked_sit with dissolve
    liu "I'm so glad you came into my life!"
    anon "Yeah, me too."
    show liu b_bed_naked_kiss with dissolve
    pause

    call scene_liu_sex_bedroom.repeat
    $ unlock_scene('liu', '01_unlocked', variant='repeat')

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
    anon "I should probably get going."
    liu "Already?"
    show liu a_undress3 b_naked_disheveled
    with {'master': dissolve}
    anon "Yeah, I've got a lot of things I still need to take care of..."
    show liu a_undress2 b_robe_disheveled_open f_happy_closed
    with {'master': dissolve}
    anon "... But I'll see you again soon."
    show liu a_undress1 b_robe_disheveled f_happy
    with {'master': dissolve}
    liu "You promise?"
    show anon f_flirt
    show liu a_shy
    with {'master': dissolve}
    anon "Of course."
    hide anon
    show liu b_robe_disheveled_kiss:
        xoffset 75
    with dissolve
    liu "Mmm."
    pause
    show anon a_sides b_dressed behind liu:
        xoffset 75
    show liu b_robe_disheveled:
        xoffset -225
    with {'master': dissolve}
    liu "I'll be waiting."
    anon "Bye, {b}Liu{/b}."
    hide anon with dissolve
    return 'afterglow'
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
