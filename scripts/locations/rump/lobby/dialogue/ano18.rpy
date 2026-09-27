label ano18_rage_rump_lobby:
    scene expression background(688, 464, 4.65)
    show rump:
        flip
    show bodyguard
    rump "What part of, \"Nobody goes in my office.\" did you not understand?"

    bodyguard a_defensive "Sir, it was just-"

    rump a_point_lips "Look at me when I say this, you blockhead!"

    show bodyguard a_idle with dissolve
    rump f_lips "NOBODY."

    rump "GOES."

    rump "IN MY OFFICE."

    show rump f_normal a_idle with dissolve
    bodyguard "I'm sorry, sir... It was just a precautionary security sweep."

    rump f_angry @ a_point_lips "NOBODY!!!"

    bodyguard "Y-ya, tuan."

    rump f_suspicious "How did you even get past the lock?"

    bodyguard "Your daughter let me in..."

    rump f_angry "{b}Iwanka{/b} let you in?!"

    show rump with dissolve:
        unflip
        xoffset -500
    rump "Grr, I told {b}Melonia{/b} it was a bad idea to give her the code!"

    rump a_finger "{b}MELONIA{/b}!!!"

    hide rump with dissolve
    pause
    bodyguard a_relief "{i}*Fiuh*{/i}"

    hide bodyguard with dissolve
    rump "Where the hell is my wife?!"

    pause
    show anon f_skeptical with dissolve:
        flip
    anon @ -m_talk "( Wow, he's really protective of his office... )"

    anon @ -m_talk "( I wonder what he's hiding in there? )"

    show anon f_thinking a_thinking with dissolve
    pause
    anon @ -m_talk "( The guard said that {b}Iwanka{/b} let him inside. )"

    anon f_flirt a_idle @ f_laugh -m_talk "( Maybe she'll do the same for me? )"

    anon @ -m_talk "( I should {b}speak with her{/b} about it. )"

    hide anon with dissolve
    return


label ano18_flee_rump_lobby:
    scene expression player.location.background_blur
    show anon with dissolve
    melonia "Ugh, I must have left it back in my room."

    anon f_surprised "( !!! )"
    iwanka "Well, hurry up."

    anon @ -m_talk "( Oh crap, she's coming back! )"

    anon @ -m_talk "( What do I- )"

    show melonia with dissolve
    pause
    melonia f_annoyed "Who the hell are you?!"

    anon f_worried a_behind_head "aku uhh..."

    melonia f_normal "Are you Juan's replacement?"

    anon @ f_confused "Juan?"

    melonia "You're not as handsome as I'd hoped..."

    anon "aku uhh..."

    melonia f_annoyed "Don't tell me you can't speak English either?"

    anon f_sad_down @ -m_talk "..."
    melonia "ARE."

    melonia "YOU."

    melonia "HERE."

    melonia "TO CLEAN THE HOT TUB?!"

    anon f_worried a_idle "I can speak English just fine, ma'am."

    melonia "Well then, answer my question!"

    pause
    anon f_sad_down "Y-ya."

    anon "I'm here to clean the hot tub."

    show anon f_worried
    melonia f_normal @ -m_talk "Hmm."

    pause
    melonia "What's your name?"

    anon "{b}[firstname]{/b}."

    melonia f_annoyed "{b}[firstname]{/b}?!"

    melonia "Well, that's not going to do."

    melonia f_normal @ -m_talk "Hmm."

    pause
    melonia "I think I'll call you..."

    melonia f_smirk "{b}Hector{/b}!"

    anon @ f_skeptical "{b}Hektor{/b}?"

    melonia "It's got a nice ring to it, don't you think?"

    anon @ -m_talk "..."
    melonia "{b}Hector{/b}, where's your staff badge?"

    anon "Staff badge?"

    melonia f_normal "Yeah, so you can get in and out of the estate without the meathead guards hassling you?"

    anon "I didn't receive one."

    melonia @ f_eyeroll "Ugh, typical."

    melonia "Tunggu."

    hide melonia with dissolve
    anon f_surprised @ -m_talk "( Is she seriously just going to hand me a badge that grants free rein inside the estate? )"

    anon f_worried @ f_laugh "( That's convenient. )"

    show melonia a_badge with dissolve
    melonia "Di Sini."

    show melonia a_idle
    with dissolve
    anon "T-terima kasih."

    melonia "Don't lose it!"

    hide melonia with dissolve
    anon "I won't!"

    melonia "Oh!"

    show melonia with dissolve
    melonia "I almost forgot."

    melonia "Go speak with the gardener, {b}Ricardo{/b}, about getting yourself a uniform."

    melonia @ a_point "Because whatever the hell this is, isn't working for me."

    anon f_sad_down "O-oke."

    hide melonia with dissolve
    pause
    anon f_worried @ -m_talk "( What's wrong with my clothes? )"

    anon @ -m_talk "( This {b}staff badge{/b} will make things a lot easier! )"

    anon @ -m_talk "( I can finally snoop around this place without worrying about the guards. )"

    pause
    anon @ -m_talk "( I could also try and do something to help that poor maid, {b}Consuela{/b}. )"

    anon @ -m_talk "( The mayor's wife seems to want her gone. )"

    anon @ -m_talk "( Maybe I should start with her? )"

    hide anon with dissolve
    call popup ('give', 'staff_badge')
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
