label josie_button_lounge:
    show josephine a_phone f_normal_down
    show anon f_shy_low with dissolve
    anon "Hey, what's going on?"
    josephine f_angry_down "Shh!"
    anon f_surprised_low "{b}Josephine{/b}?"
    josephine "Shut up, I'm watching my favorite streamer!"
    anon f_worried_low "Oh, umm... Okay?"
    show josephine f_normal_down

    label josie_button_lounge.choice:
    menu:
        "Private photos." if M_anon.is_state(S_ano07_perk):
            jump ano07_hint_josie
        "Who is your favorite streamer?":

            jump josie_button_lounge.stream
        "You wanna make out?":

            if M_anon.finished_state(S_ano09_blow):
                jump josie_button_lounge.invite
            jump josie_button_lounge.flirt

        "Blowjob?" if M_anon.finished_state(S_ano09_blow):
            jump josie_button_lounge.blowjob

        "Sex?" if M_josie.finished_state(S_jos02_init):
            jump josie_button_lounge.sex
        "See ya.":

            pass

    anon f_shy_low "See ya."
    josephine @ -m_talk "..."
    show anon f_worried_low
    pause
    anon f_unimpressed @ a_wave "I said, goodbye {b}Josephine{/b}!"
    josephine f_angry_down "Dude, stream."
    josephine "Shh."
    show josephine f_normal_down
    anon "Ugh."
    hide anon with dissolve
    return


label josie_button_lounge.blowjob:
    anon f_flirt_low "Don't suppose you feel in a giving mood?"
    josephine a_phone f_normal_down "Not now, {b}[firstname]{/b}."
    josephine "I'm watching my stream."
    anon f_worried_low "C'mon, it'll be more fun than some stupid art stream."
    josephine @ f_eyeroll "Pfft, for you maybe..."
    josephine "Try again later."
    anon f_sad_down "Ugh, fine."
    return


label josie_button_lounge.flirt:
    anon f_flirt_low "You wanna make out?"
    josephine f_angry_down "Are you nuts?!"
    josephine "It's stream time, go away!"
    anon f_unimpressed_low "Alright, sheesh."
    show josephine f_normal_down
    jump josie_button_lounge.choice


label josie_button_lounge.invite:
    anon f_flirt_low "You wanna make out?"
    josephine "What are you, twelve years old?"
    show anon f_confused_low
    pause
    josephine "It's stream time, go away!"
    anon f_unimpressed_low "Alright, sheesh."
    jump josie_button_lounge.choice


label josie_button_lounge.sex:
    anon f_shy_low "Want to have sex?"
    josephine f_concerned @ -m_talk "Hmm?"
    josephine "Dude, It's stream time!"
    josephine f_normal_down "Have a seat and watch with me."
    show anon f_worried_low

    if not M_josie.once('sex_chair'):
        jump chat_josie_sex_chair

    menu:
        "Pants off?":
            jump chat_josie_sex_chair.repeat
        "Bring it.":

            pass

    show anon a_point f_flirt_low
    with {'master': dissolve}
    anon "Or you could just bring it with you?"
    pause
    show josephine f_annoyed
    pause
    show anon a_sides f_grin_low
    with {'master': dissolve}
    pause
    josephine f_eyeroll "Ugh, fine."
    show josephine a_undress1 f_normal_down
    show anon b_flour f_looking_down behind josephine:
        offset (-100, 110)
    with dissolve
    pause
    show anon b_shirt od_dick4 f_flirt a_sides:
        yoffset 0
    show josephine b_undershirt a_undress2 f_normal_down:
        offset (-370, 0)
    with slowdissolve
    pause
    show josephine a_idle with dissolve
    pause
    show anon f_flirt_low
    show josephine b_topless
    with dissolve
    pause
    show josephine b_topless_undress5 with dissolve
    pause
    show anon f_surprised_down
    show josephine b_topless_undress6
    with dissolve
    pause
    show anon f_flirt
    show josephine b_naked a_phone f_normal_down
    with dissolve
    pause
    anon f_worried @ -m_talk "..."
    anon "Are you gonna get on the table or-"
    josephine f_concerned @ -m_talk "Hmm?"
    josephine f_normal @ f_eyeroll "Oh, right."
    josephine "Sorry."
    hide josephine with dissolve
    show anon f_worried:
        flip
        xoffset -600
    with {'master': dissolve}
    josephine "Ready when you are, bowl cut."
    anon f_unimpressed "Stop calling me that!!"
    hide anon with {'master': dissolve}
    josephine "Hehe!"

    call scene_josie_sex.afternoon
    $ unlock_scene('josie', '02_unlocked', variant='afternoon')

    scene expression background(496, 384, 2.75) as stage
    show anon b_flour f_looking_down:
        flip
        yoffset 110
    show josephine b_naked a_phone f_normal_down:
        flip
        xoffset 150
    with fade
    josephine @ -m_talk "..."
    show anon b_dressed f_unimpressed with dissolve:
        yoffset 0
    anon "And you're back on the phone again..."
    josephine f_concerned "What, we're done, aren't we?"
    anon "Yeah, I suppose."
    show josephine f_normal_down
    pause
    josephine f_sexy_down @ f_sexy "My song request is coming up next..."
    pause
    anon "I'll see you later, {b}Josephine{/b}."
    josephine "See ya, {b}[firstname]{/b}."
    hide anon with dissolve
    return 'afterglow'


label josie_button_lounge.stream:
    anon f_shy_low "Who is your favorite streamer?"
    josephine @ -m_talk "Hmm?"
    josephine "Oh, he's this dorky Somalian guy named {b}DarkCookie{/b}."
    josephine "He's creating this fan-funded adult game, and he streams himself creating art for it pretty much every day around {b}2PM EST{/b}."
    anon f_surprised_low "Every day?"
    josephine "Well, usually not on the weekends."
    josephine "... Or if he's sick."
    josephine @ f_laugh "Which is like, ALL THE TIME!"
    anon f_skeptical @ -m_talk "..."
    josephine "It's kinda crazy actually."
    josephine @ f_laugh "I think Bubble Boy might have a better immune system than him."
    anon f_shy_low "And he's your favorite streamer?"
    josephine @ -m_talk "Mhmm."
    anon "Why?"
    josephine "I dunno, I just like trolling him."
    anon "Oh, the trolling thing again..."
    josephine "Plus, the chat is full of thirsty boys who are gullible as shit."
    josephine "They're like, constantly sending me dick pics..."
    josephine "I have a huge collection."
    anon f_surprised_low "You have a huge collection of dick pics?"
    josephine "Totally."
    anon f_flirt_low "And you enjoy that?"
    josephine "Not really."
    show anon f_surprised_teeth_low
    pause 1
    anon f_worried_low "Sorry, I don't get the appeal."
    josephine "Yeah, I guess it's kinda hard to explain..."
    anon f_shy_low "Well, whatever floats your boat."
    josephine "Oh look, he's doing a poll!"
    josephine "I love these."
    pause
    josephine @ f_laugh "Pfft, hahahaah!"
    josephine "Why does he hate the Queen of England so much?!"
    show anon f_worried_low
    pause
    josephine f_angry_down "Oh god, not {i}Kung Fu Fighting{/i} again..."
    josephine "I'm so sick of this song!"
    anon "Right, well... Enjoy."
    josephine "Please, skip it!"
    show josephine f_normal_down
    jump josie_button_lounge.choice


label chat_josie_sex_chair:
    anon "... Don't you ever get bored of that?"
    josephine f_confused "Umm, no?"
    pause
    show josephine a_phone_show f_sexy
    with {'master': dissolve}
    josephine "Look, he's drawing boobies today."
    show anon a_surprised f_surprised_low
    with {'master': dissolve}
    anon "Oh my god!!"
    anon "Is that girl pregnant?"
    show anon a_sides
    with {'master': dissolve}
    josephine @ f_laugh "Hehe, yeah."
    anon f_disgusted_low "It looks like she swallowed a bean bag chair!"
    josephine "I think it's supposed to be exaggerated for comedic effect..."
    anon f_worried_low "Geez, I hope so."
    show josephine a_phone f_sexy_down
    with {'master': dissolve}
    josephine "... Or possibly she's incubating a walrus in there?"
    josephine "Honestly, with him... it could be either one."
    anon "Eww."
    show anon f_disgusted_low
    josephine f_sexy "See, it's surprisingly entertaining!"
    josephine "Come sit down."
    show anon a_thinking f_thinking
    show josephine f_sexy_down
    with {'master': dissolve}
    anon @ -m_talk "Hmm?"
    show anon a_point f_confused_low
    with {'master': dissolve}
    anon "Can we watch it with our pants off?"
    show josephine f_annoyed
    pause
    show anon a_sides f_happy_low
    with {'master': dissolve}
    anon "I mean, I'll totally watch it... if we can..."
    anon "... You know."
    pause
    show anon f_grin_low
    with {'master': fastdissolve}
    pause
    josephine f_eyeroll "{i}*Sigh*{/i} Alright, fine."
    josephine f_bored_down "Just slide my panties down."
    anon f_happy_low "Sweet!"
    jump chat_josie_sex_chair.tail


label chat_josie_sex_chair.repeat:
    show anon a_sides f_confused_low
    with {'master': dissolve}
    anon "Can we watch it with our pants off?"
    show josephine f_annoyed
    josephine "I knew you were going to say that..."
    pause
    show anon f_grin_low
    with {'master': fastdissolve}
    pause
    josephine "{i}*Sigh*{/i} Alright, fine."
    josephine "Just slide my panties down."
    anon f_happy_low "Sweet!"
    jump chat_josie_sex_chair.tail


label chat_josie_sex_chair.tail:
    call scene_josie_sex_chair.repeat
    $ unlock_scene('josie', '03_unlocked')
    $ renpy.dynamic(where=_return)

    call josie_button_stage
    show josephine a_phone f_normal_down
    show anon b_shirt_undress_bottom
    with fade
    pause
    show anon a_remove_shorts b_dressed f_shy_down
    with {'master': dissolve}
    anon "So uhh..."
    show anon a_sides b_dressed f_normal_low
    with {'master': dissolve}

    if where == 'outside':
        anon "... You do realize you have cum all over your back, yeah?"
    else:
        anon "... That was fun!"

    josephine @ -m_talk "Mhmm."
    show anon f_confused_low
    pause
    anon "You're not even listening to me right now, are you?"
    josephine @ -m_talk "Mhmm."
    show anon f_worried_low
    pause
    anon "Right."
    show anon f_unimpressed_low
    pause
    show anon a_wave
    with {'master': dissolve}
    anon "Well, see ya later... I guess."
    josephine @ -m_talk "Mhmm."
    hide anon
    with {'master': dissolve}
    pause
    josephine f_sexy_down "Oh my god, he's drawing poop again!"
    show josephine a_phone_show f_sexy
    with {'master': dissolve}
    josephine "You gotta check this-"
    show josephine f_confused
    pause
    show josephine a_phone
    with {'master': dissolve}
    josephine "{b}[firstname]{/b}?!"
    return 'afterglow'
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
