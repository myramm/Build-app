label jos01_find_kim:
    show kim:
        xoffset 100
    show rump f_angry:
        flip
        xoffset 200
    with fade
    rump "You want to tell me why I'm getting phone calls from my associate, saying you disrespected his daughter?"
    kim f_curious @ -m_talk "Hmm?"
    rump "He says she came in here the other day, looking to purchase a car, and you wouldn't help her?"
    kim f_normal "That's not true!"
    kim "I terr her, she want custom car, I must make order."
    kim "Take coupre weeks before come."
    rump f_normal @ a_hand "Yes, but he says you were very rude to her..."
    kim f_angry "Tsk, she big baby!"
    kim "Throw tantrum in store, I no have time for changing rittre girr diapers!"
    kim f_smirk @ f_laugh a_rub "Huehuehue!"
    rump f_angry @ a_finger "This is not a laughing matter, {b}Kim{/b}."
    show kim f_normal
    rump "My associate is a very serious man and he does not respond well to disrespect."
    rump "He'd have sent men here to do you harm, had I not stepped in."
    kim f_angry @ f_baby_cry "Whaaa?!"
    kim "They threaten {b}Kim{/b}?!"
    rump f_normal "You're lucky you've proven yourself to be a valuable asset thus far."
    rump "But I'm warning you now, you are far from irreplaceable."
    rump "Do you understand?"
    kim f_normal "Yes, yes... {b}Kim{/b} understand."
    kim @ a_wave "I meant no disrespect."
    rump "The girl will be returning here next week and you WILL have a car waiting for her, along with an apology."
    rump "Do I make myself clear?"
    kim "Y-yes, of course, {b}Mr. Rump{/b}!"
    kim "{b}Kim{/b} prepare car and make big time aporogy."
    rump "Very good."
    pause
    rump "Now that's settled, I'd like to speak with you about the growing needs of our enterprise here in Summerville."
    rump "Why don't you swing by my estate later this evening and we'll discuss the details, hmm?"
    rump f_smirk "Bring that beautiful wife of yours along... We'll all go for a dip in the hot tub."
    kim f_smirk "Wirr {b}Mrs. Rump{/b} be joining us?"
    rump "Most definitely."
    kim "Oh, {b}Kim{/b} rike sound of that..."
    kim "We come."
    rump "Wonderful."
    rump "I'll let my guards know you're expected."
    show rump f_normal with dissolve:
        unflip
        xoffset -400
    pause
    show rump with dissolve:
        flip
        xoffset 100
    rump @ a_finger "Oh, one more thing..."
    kim f_curious @ -m_talk "Hmm?"
    rump "Gather up any paperwork your boss has on our dealings over the past twelve months, and dispose of them."
    rump "Things are going to be heating up very soon and I don't want a paper trail."
    kim f_smirk "Yes, of course."
    kim "{b}Records upstairs, in office{/b}."
    kim "{b}Kim{/b} dear with them."
    rump "Don't let me down, {b}Kim{/b}."
    show kim b_dressed_bow with dissolve
    kim "Never, {b}Mr. Rump{/b}."
    hide rump
    show kim b_dressed
    with dissolve
    pause .5
    hide kim with dissolve

    scene expression background(560, 480, 3) as stage
    show anon f_worried
    with fade
    anon @ -m_talk "( Hmm, is it possible that {b}Mayor Rump{/b} is doing business with the Russian mob? )"
    anon @ -m_talk "( It certainly sounds that way from the conversation I just overheard... )"
    anon @ -m_talk "( I should {b}head upstairs to the office and see about finding that paperwork{/b} they were discussing. )"
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
