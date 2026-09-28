label ano07_hint_josie:
    if M_anon.is_state(S_ano07_mech):
        jump ano07_hint_josie.help

    if M_anon.is_state(S_ano07_find):
        jump ano07_hint_josie.find

    if M_anon.is_state(S_ano07_give):
        jump ano07_hint_josie.give

    if M_anon.is_state(S_ano07_perk):
        jump ano07_hint_josie.perk

    return


label ano07_hint_josie.help:
    anon f_normal "About those private photos."
    josephine f_normal "Have you spoken with {b}Jiang{/b} about my little problem?"
    anon f_worried "I'm still working on that..."
    pause
    anon f_normal "You said he's the head mechanic here at the dealership?"
    josephine @ a_point_back "Yeah, he should be {b}in the garage{/b} behind me."
    anon "Alright, I'll speak with him."
    hide anon with dissolve
    return


label ano07_hint_josie.find:
    anon f_normal "About those private photos."
    josephine f_normal "Have you spoken with {b}Jiang{/b} about my little problem?"
    anon f_worried "Yes, I think he's going to help."
    anon @ f_unimpressed -m_talk "( But only once I find his lucky tool bag! )"
    pause
    anon f_normal "I'm sure we'll have those photos erased in no time."
    josephine f_concerned "Yeah..."
    anon "I'll be back as soon as I have news."
    hide anon with dissolve
    return


label ano07_hint_josie.give:
    anon f_normal "About those private photos."
    josephine f_surprised "You got them?!"
    anon f_worried "Not yet, but I'm on my way to check in with {b}Jiang{/b} now."
    show josephine f_angry_up
    anon @ f_shy -m_talk "( Lucky tool bag in tow! )"
    pause
    josephine f_concerned "Well? What are you waiting for?"
    anon "N-nothing. Be right back!"
    hide anon with dissolve
    return


label ano07_hint_josie.perk:
    anon f_shy_low "About those private photos."
    josephine @ -m_talk "..."
    show anon f_worried_low
    pause
    anon f_unimpressed @ a_wave "{b}Josephine{/b}! The photos?"
    josephine f_angry_down "Dude, stream."
    josephine "Shh."
    show josephine f_normal_down
    anon "Ugh."
    anon @ -m_talk "( I guess I'll tell her the good news later... )"
    hide anon with dissolve
    return


label ano07_perk_josie:
    show josephine:
        xoffset 100
    show anon with dissolve:
        xoffset 100
    anon "I deleted those photos off {b}Kim{/b}'s phone for you."
    show josephine b_dressed f_surprised with fastdissolve:
        xoffset 0
    josephine "No way!"
    josephine "Really?"
    anon "Yup."
    anon "It's all taken care of."
    josephine f_shy "Holy shit."
    josephine "I can't believe you actually pulled it off!"
    pause
    josephine "I guess, I owe you big time..."
    pause
    josephine f_sexy "Heh, whatever shall I do to repay you?"
    anon "Well, I still need help finding that car for my-"
    josephine "Come with me!"
    show xtra3 as counter behind josephine
    show anon b_pulling5 f_worried_left behind josephine:
        xoffset -152
    show josephine b_empty:
        xoffset -768
    with {'master': dissolve}
    anon "What the-"
    hide anon
    hide josephine
    with dissolve

    $ player.go_to(L_dealership_lounge)
    scene expression background(472, 360, 1.8) with fade
    show josephine a_hips f_sexy
    show anon f_worried
    with dissolve
    anon "What's going on?"
    josephine "I'm giving you your reward, duh!"
    anon "Ehh, okay?"

    if M_josie.peeked:
        josephine "Wait a second."
        josephine f_concerned "You didn't look at the photos, did you?"

        menu:
            "Yeah, a little.":

                anon "Yeah, a little."
                josephine f_angry "Ugh, seriously?"
                anon f_shy @ a_behind_head "I couldn't help it."
                anon "I was curious."
                josephine a_crossed "Well, I WAS going to reward you with a private show but since you already rewarded yourself..."
                anon f_worried "I'm really sorry."
            "What?! Of course not!":

                anon f_shy "What?! Of course not!"
                show anon f_grin
                josephine @ -m_talk "..."
                josephine f_angry a_crossed "You liar!"
                anon f_worried "Huh?"
                josephine "You're totally lying to me right now!"
                anon "N-no, I'm not..."

        josephine @ f_eyeroll "Whatever, dude."
        josephine "It's too bad cause I was feeling generous enough to let you go hands on..."
        anon f_sad_down "Aww, man!"
        josephine "Maybe next time you'll-"
    else:

        josephine "Now bear in mind that I'm only doing this because you helped me out today and I'm literally dying of boredom at this job..."
        anon f_confused "Doing what, exactly?"
        josephine a_flash2 @ a_flash1 "What do you think about these, bowl cut?"
        anon f_shock "!!!"
        anon f_flirt_low "T-those are very nice."
        josephine "Right?"
        pause
        josephine "You wanna touch them?"
        anon f_shy "{i}*Gulp*{/i} Are you sure?"
        josephine "Of course I'm sure, I offered, didn't I?"
        anon f_flirt_low "Yeah, okay."
        show anon b_empty:
            xoffset 357
            yoffset 22
        show josephine b_dressed_fondle a_idle
        with dissolve
        pause
        anon "Wow, they're so perky!"
        josephine f_concerned "What the hell are you doing?"
        show josephine a_squeeze1 with dissolve
        anon f_worried "Huh?"
        josephine "They aren't radio knobs, you know?!"
        anon f_worried_low "Oh, uhh... Sorry."
        show josephine a_idle f_normal with dissolve
        show anon f_flirt_low
        pause
        anon "I love your nipples, they're so tiny and cute!"
        josephine "Well, I'm not sure I appreciate the tiny remark but I'll concede the cute thing..."
        pause
        josephine "You wanna tast-"

    show anon b_dressed a_up f_surprised behind josephine:
        flip
        xoffset -150
        yoffset 0
    if not M_josie.peeked:
        show josephine b_dressed a_flash2 f_surprised
    with dissolve
    sato "{b}Josephine{/b}!!!"
    show anon a_sides f_surprised_teeth
    if not M_josie.peeked:
        show josephine a_cover
    with dissolve
    josephine f_concerned "Daddy?!"
    show sato f_angry a_hips with dissolve:
        flip
    sato "What the hell are you doing in here!"
    josephine a_hips "Oh, dear."
    josephine "You've caught me red-handed, again..."
    josephine "Is there no end to my depravity?!"
    josephine "You'll definitely have to fire me this tim-"
    sato "This is not your scheduled break period, young lady!"
    show anon f_confused
    show josephine f_surprised m_talk
    pause
    josephine "T-that's what you're mad about?!"
    if M_josie.peeked:
        josephine "I was just about to let this customer feel me up and you're angry that I'm not at the front desk!"
    else:
        josephine "I was letting this customer feel me up and you're angry that I'm not at the front desk!"
    show josephine -m_talk
    sato "I don't have time for your jokes right now, {b}Josephine{/b}!"
    show anon f_worried
    josephine "But I-"
    sato "You have responsibilities to this company and I expect you to take them seriously!"
    show josephine a_crossed f_pouting with dissolve
    sato "Now get your butt back downstairs and see that our customer's needs are taken care of this instant!"
    josephine @ -m_talk "..."
    sato "I mean it!"
    josephine f_angry "Fine!"
    hide josephine with dissolve
    pause
    sato f_confused "I'm terribly sorry about that, sir."
    sato "If you wouldn't mind heading back down to the showroom, I assure you, my daughter will be happy to assist you..."
    anon f_skeptical "Umm, thanks?"
    sato f_smiling "It's my pleasure, sir."
    hide sato with dissolve
    pause
    anon f_worried "Weird."
    hide anon with dissolve
    return


label ano07_sale_josie:
    show anon with dissolve
    label ano07_sale_josie.anon:
    anon f_normal @ f_grin a_point "One car, please!"
    josephine b_dressed f_normal "This is the cheapest car we have at the moment."
    josephine "The Mini Vulva."
    anon f_surprised "The mini-what?!"
    josephine "It's very popular with customers of the female persuasion."
    josephine "It has a retail value of eleven thousand and five hundred."
    anon "Eleven thousand?!"
    anon "That's a bit much, isn't it?"
    josephine "The lowest I can let it go for is six thousand."
    josephine "But with your trade in we can do forty-five hundred."
    anon f_worried "Forty-five hundred, huh?"
    anon "I might be able to swing that..."
    josephine "So, you want it or not?"
    show anon f_thinking a_thinking with dissolve

    menu:
        "Yes. ($4,500)":
            jump ano07_sale_josie.deal
        "Maybe later.":

            pass

    anon a_thinking f_worried "I'll have to think about it."
    josephine @ f_eyeroll "Great."
    hide josephine
    show josephine b_dressed_sleeping behind anon
    show anon f_worried_low
    with {'master': dissolve}
    josephine "Take your time, bowl cut."
    josephine "It's not like I'm going anywhere..."
    hide anon with dissolve
    return


label ano07_sale_josie.deal:
    if player.has_money(4500):
        anon f_normal a_idle "I'll take it!"
        josephine @ f_eyeroll "Super."
        show anon a_money with dissolve
        pause
        show anon a_idle with dissolve
        josephine "My father will be so proud..."
        anon "Oh, c'mon... It wasn't that bad."
        josephine @ f_eyeroll "Eugh."
        josephine "Just take your little car and beat it, would ya, bowl cut?"
        josephine "I've got work I'm trying not to do."
        show josephine f_normal_down a_phone with dissolve
        anon "Alright."
        anon "Well, thanks again!"
        hide anon with dissolve
        return 'compact_key'
    else:
        anon f_worried "I'll be back to get it as soon as I have the money."
        josephine @ f_eyeroll "Great."
        show josephine f_normal_down a_phone
        show anon f_worried_low
        with {'master': dissolve}
        josephine "It's not like I'm going anywhere..."
        hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
