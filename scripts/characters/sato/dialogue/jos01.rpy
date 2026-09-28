label jos01_spot_sato:
    if M_rump.state is None:
        jump jos01_spot_sato.ronald

    if M_kim.state is None:
        jump jos01_spot_sato.kim

    jump jos01_spot_sato.yoyo


label jos01_spot_sato.ronald:
    show sato f_smiling a_empty:
        xoffset -77
    show rump f_smirk a_handshake_sato:
        xzoom -1
    show kim f_smirk:
        xoffset 100
    rump "Oh, most definitely."
    rump "The wife's been very pleased with it."
    show sato a_idle
    show rump a_idle
    with dissolve
    rump "It's a quality machine to be sure."
    sato "That's so good to hear, {b}Mr. Rump{/b}!"
    sato "I can't tell you how much we appreciate your business!"
    rump @ a_finger "Oh, you can show your appreciation this fall with your vote."
    sato "Of course, sir!"
    sato "You can count on me."
    rump "That's what I like to hear, {b}Mr. Sato{/b}."
    rump "You know, this is the guy you should really be thanking!"
    show rump a_handshake_kim:
        xoffset 142
    show kim a_empty behind rump:
        xoffset 50
    with dissolve
    rump "He's quite the salesman!"
    show kim a_rub:
        xoffset 100
    show rump a_idle:
        xoffset 0
    with dissolve
    kim "Oh, you too kind, {b}Mr. Mayor{/b}."
    rump "Please, {b}Kimmy{/b}... Call me {b}Ronald{/b}."
    kim "Very werr, {b}Ronard{/b}."
    rump "I wonder if you'd give me a moment alone with my new friend here, {b}Mr. Sato{/b}?"
    sato "Oh, certainly, sir!"
    sato "I'll just be right over there at the front desk, should you require anything..."
    rump "Thanks."
    hide sato with dissolve
    pause .5
    show kim a_wave with dissolve:
        xoffset -100
    kim a_idle @ a_wave "Come, we go tark in garage."
    kim "More private."
    hide rump
    hide kim
    with dissolve

    scene expression background(240, 480, 6.) as stage
    show anon f_skeptical
    with fade
    anon @ -m_talk "( Hmm? )"
    anon @ -m_talk "( The mayor is friends with {b}Kim{/b}? )"
    anon @ -m_talk "( Something fishy is going on here... )"
    pause
    anon @ -m_talk "( ... And where is {b}Josephine{/b}? )"
    pause
    anon f_grin @ -m_talk "( I should investigate. )"
    hide anon with dissolve
    return


label jos01_spot_sato.kim:
    show kim f_angry behind sato
    show sato a_paper_show f_angry:
        xoffset 200
        xzoom -1
    sato "Our sales numbers are down almost seventy percent!"
    show sato a_phone_pocket with {'master': dissolve}
    kim m_talk "I terr you arready, {b}Mr. Sato{/b}!"
    show sato a_hips with {'master': dissolve}
    kim f_baby_cry -m_talk "{b}Mayor Rump{/b} go jair!"
    kim "We must wait for new dear with big crient!"
    sato a_crossed f_confused "How long is that going to take?!"
    sato "The regional manager will be here any second and he's going to want answers!"
    kim a_rub f_smirk "It's okay, you terr him big crient start buying rots of cars very soon."
    kim a_counter_raised "{b}Kim{/b} number one, best saresman!"
    kim a_idle "Never fair!"
    sato f_angry @ -m_talk "Hmph."
    pause
    sato a_idle f_normal "Well, I'd suggest you start making calls to this {i}big client{/i} right away..."
    sato "... And tell him to hurry, because our jobs may very well depend on it!"
    kim a_scare f_baby_cry "Y-yes, {b}Kim{/b} go see them now!"
    kim a_rub f_normal "No worries."
    sato "I am worried, {b}Kim{/b}."
    sato "I'm very worried."
    show kim f_baby_cry
    pause
    show kim f_surprised
    sato "Go."
    kim f_baby_cry "Y-yes, {b}Kim{/b} fix... You see!"
    kim f_smirk "{b}Kim{/b} number one!"
    hide kim
    show sato f_angry:
        xoffset -300
        xzoom 1
    with {'master': dissolve}
    kim "Best saresman!"
    show sato a_facepalm f_angry_closed with {'master': dissolve}
    kim "Never fair!"
    hide sato with dissolve

    scene expression background(240, 480, 6.) as stage
    show anon f_brag
    with fade
    anon @ -m_talk "( Looks like {b}Kim{/b} is having a hard time now that {b}Rump{/b} is behind bars... )"
    anon @ f_grin -m_talk "( ... I bet {b}Josephine{/b} is loving that! )"
    pause
    anon f_confused @ -m_talk "( Hmm? )"
    anon @ -m_talk "( Speaking of {b}Josephine{/b}, where is she? )"
    anon @ -m_talk "( She has to be here somewhere... )"
    hide anon with dissolve
    return


label jos01_spot_sato.yoyo:
    show sato f_smiling:
        xoffset 200
        xzoom -1
    show yoyo
    yoyo "Thanks again for job, {b}Mr. Sato{/b}."
    yoyo "{b}Kim{/b} is very excited for opportunity."
    sato "Oh, it's my pleasure, dear."
    sato "Your brother brought in a lot of business for us..."
    sato "... So it was the least I could do."
    pause
    sato f_normal "I was so sorry to hear about what happened."
    yoyo "Yes, it make quite a stink back home in Korea."
    yoyo "Our famiry insisted {b}Kim{/b} come and repair the damage done to our reputation."
    sato a_hips f_smiling "Oh, I know all about family embarrassment... Believe you me."
    sato "Heh, I get a whole heap of that from my daughter!"
    yoyo @ -m_talk "..."
    sato f_sad @ -m_talk "..."
    sato "You know, because she umm..."
    show sato a_idle with {'master': dissolve}
    yoyo @ -m_talk "..."
    sato f_sad_down "... W-well, her mother passed... And we uhh..."
    yoyo @ -m_talk "..."
    sato "... Haven't really recov-"
    show sato f_surprised
    pause
    sato f_sad "Err, Nevermind."
    sato "Heh, that's not really important."
    pause
    sato "{i}*Gulp*{/i} You uhh, speak to your brother then?"
    sato "Is he doing well?"
    yoyo "He is currentry incarcerated in American prison."
    sato f_uneasy "Y-yes, of couse... I just meant to say, if there's anything I can do... Just-"
    yoyo a_stop "No, is okay."
    yoyo "Ret us move forward and focus on future endeavors."
    show yoyo a_idle with {'master': dissolve}
    sato f_normal "Right, of course."
    yoyo "You say, regionar manager come today?"
    sato @ f_confused -m_talk "Hmm?"
    sato "Oh, yes... But ehh, that's just a routine visit... Nothing to be concerned about."
    yoyo "On the contrary, {b}Kim{/b} berieve routine visit is opportunity to better dearership."
    show sato f_confused
    yoyo "One shourd arways strive to make good impression, especiarry to those who weird great power."
    sato f_sad "Umm, yeah... That's very sound advice."
    yoyo "Perhaps you wourd arrow {b}Kim{/b} to speak with him?"
    yoyo "I have many ideas that could improve our sares numbers..."
    yoyo "... And a feminine touch often better recieved by man in high station."
    sato f_confused "Y-you want to meet with him?"
    yoyo @ f_quizzical "If it is not too much troubre?"
    sato f_normal "Umm, no... It's no trouble."
    sato f_smiling "I'd be glad to introduce you."
    yoyo "Very good."
    yoyo "If you'rr excuse me?"
    yoyo "{b}Kim{/b} rike to go and freshen up before regionar manager come."
    sato "Y-yes, of course."
    show sato f_confused_low
    show yoyo b_dressed_bow
    with {'master': dissolve}
    pause
    show sato f_confused
    yoyo b_dressed "Thank you."
    hide yoyo
    show sato f_uneasy:
        xoffset -300
        xzoom 1
    with {'master': dissolve}
    sato f_uneasy "{i}*Gulp*{/i} Wow... Okay."
    hide sato with dissolve

    scene expression background(240, 480, 6.) as stage
    show anon a_surprised f_shock
    with fade
    anon @ -m_talk "( That's {b}Kim{/b}'s sister?! )"
    anon a_sides f_worried @ -m_talk "( I have a bad feeling about this... )"
    anon f_thinking @ -m_talk "( ... And where's {b}Josephine{/b}?! )"
    anon f_confused @ -m_talk "( I don't see her anywhere! )"
    anon @ -m_talk "( I should investigate. )"
    return


label jos01_find_sato:
    show anon with dissolve
    anon "Hello?"
    sato f_smiling "Greetings and welcome to-"
    sato f_normal "Oh, it's you again."
    sato "Look, I'm afraid my daughter can't play with you today... We're very busy!"
    anon f_worried "Play with me?"
    sato "Or whatever it is you crazy kids do..."
    sato "We have a very important man visiting us today and I don't want her pulling any shenanigans!"
    anon "Oh kay..."
    sato "Come back another day."
    pause
    hide anon with dissolve

    scene expression background(240, 480, 6.) as stage with fade
    show anon a_thinking f_thinking with dissolve:
        flip
        xoffset -400
    anon @ -m_talk "( Hmm, I guess that explains why {b}Josephine{/b} isn't at the front desk... )"
    anon @ -m_talk "( She has to be around here somewhere, perhaps {b}I should look for her{/b}? )"
    hide anon with dissolve
    return


label jos01_find_sato.repeat:
    scene expression background(240, 480, 6.) as stage
    show anon f_worried with dissolve:
        xoffset 300
    anon @ -m_talk "( No, he's not going to tell me where {b}Josephine{/b} is. )"
    anon @ -m_talk "( She has to be around here somewhere, perhaps I should {b}look for her{/b}? )"
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
