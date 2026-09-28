label church_first_visit:
    scene expression player.location.background_blur
    show player 11 with dissolve
    player_name "( The church is empty. )"
    player_name "( Looks like I missed Mass. )"
    player_name "( The sign on the way in said that it's celebrated each {b}weekend morning{/b}. )"
    hide player 11
    return

label church_first_mass:
    scene expression background(696, 416, 6.) as stage
    show keeves:
        xoffset -400
    show location_church_day_closeup_altar as altar:
        xoffset -420
    show angelica:
        xoffset 100
    with fade
    keeves "So like, we're the sheep, right?"
    keeves @ a_point "And God, he's like... Our shepherd, see?"
    pause
    keeves "He's trying to protect us from wolves and whatnot, while leading us down a path to greener pastures."
    keeves @ f_confused "Which I'm pretty sure is code for Heaven or something..."
    keeves f_happy "... And you definitely wanna go to Heaven, 'cause like, there's tons of hot babes there and cool dudes surfin' on clouds; plus nobody has to work anymore so you can just chill, all day!"
    keeves "We'll totally be like, cruisin' around with little angel wings, and eating corn dogs and nachos all day."
    keeves @ f_laugh a_rock "Heh, everything will be truly excellent!"
    pause
    keeves f_confused "So wait, what was I talking about again?"
    angelica "Communion, {b}Father{/b}."
    keeves f_happy @ f_laugh a_raise "Oh, yeah!"
    keeves "Totally."
    keeves f_normal "{i}*Ahem*{/i} We will not be having Communion this week as somebody, not gonna say who, got the munchies last night and dipped into the Communion wafers..."
    show angelica f_eyeroll
    pause
    show angelica f_normal
    keeves f_happy a_raise @ f_laugh "Heh, but don't worry!"
    keeves -a_raise @ a_point "I ordered a bunch more, and we'll continue those services next week with delicious wine and everything, cool?"
    pause
    keeves "Right."
    keeves f_confused "So uhh, we should probably move on to the passing around of the collection plate."
    keeves f_normal "{b}Sister Angelica{/b} is gonna do the honors and you all just, umm... Well, donate what you can but don't feel obligated."
    hide angelica with dissolve
    keeves f_happy "You know, 'cause, while God appreciates generosity and smiles down upon those that give, it is totally NOT a requirement!"
    pause
    keeves "You cannot buy your way into heaven... But you could probably get yourself a cloud closer to the heavenly slushie machine!"
    keeves a_raise "Heh, wheezin' the juice!"
    keeves -a_raise @ a_point "Heh, this guy knows what I'm talking about!"
    keeves "It will be most triumphant!"
    pause
    keeves "Oh, I also wanna remind all you dudes and dudettes, that confession will be available immediately following the service today."
    keeves "So feel free to swing by and unburden yourselves, okay?"
    pause
    keeves @ f_laugh a_rock "Excellent!"
    keeves "Now, let's close things out with a prayer, shall we?"
    scene expression player.location.background_blur
    show anon f_thinking a_thinking
    with fade
    anon @ -m_talk "( You know, I haven't been to church in a while, but I don't remember it being like this... )"
    anon @ -m_talk "( There's definitely something off about that priest. )"
    pause
    anon f_worried a_idle @ -m_talk "( I should {b}speak with him{/b} and investigate. )"
    hide anon with dissolve
    return

label church_mia_church_plan:
    scene church_full02_b
    show player 32 at Position (xoffset=68) with dissolve
    player_name "( {b}Helen{/b} is sitting in the front. )"
    show player 12 with dissolve
    player_name "( There must be a way to speak with her... )"
    player_name "( ... But I need to change my attire first. )"
    player_name "( Let's see if I can find one of those {b}priest outfits{/b} somewhere in the church... )"
    hide player with dissolve
    return

label church_mia_convince_helen:
    scene church_cs01
    show text _ ("The Mass was still ongoing.\n{b}Helen{/b} got up and headed towards the confessional...\n... Making her way inside.") as caption
    with fade
    pause

    scene church_cs02
    show text _ ("The priest left for a brief moment.\nNow is the perfect time to get close to her...\n... And change her mind about {b}Harold{/b}.") as caption
    with fade
    pause

    scene church_full03_b
    show player 30 at Position (xoffset=-1)
    show players robe
    with fade
    player_name "I need to {b}enter the confessional from the right side{/b}..."
    hide player
    hide players robe
    with dissolve
    return

label church_mia_return_priest_outfit:
    scene church_full02_b
    show player 33 at Position (xoffset=-1)
    show players robe
    with dissolve
    player_name "Perfect!"
    show player 106 at Position (xoffset=-1)
    player_name "..."
    show player 14 at Position (xoffset=-1)
    player_name "( I should leave and return this outfit where I found it... )"
    player_name "( ... Before someone notices... )"
    hide player
    hide players robe
    with dissolve
    return

label church_mia_nun_thoughts:
    scene expression player.location.background_blur
    show player 10 with dissolve
    player_name "( Damn... That was scary! )"
    player_name "( Now I have to do stuff for this nun... )"
    player_name "( ... I just hope she doesn't tell anyone about what I did. )"
    hide player with dissolve
    return

label church_mia_church_night_visit:
    scene expression player.location.background_blur
    show player 10 with dissolve
    player_name "( It's so quiet at night. )"
    player_name "( I'm not sure people are allowed in here this late. )"
    show player 12
    player_name "( Now, to go see {b}Sister Angelica{/b} and see what she wants... )"
    hide player with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
