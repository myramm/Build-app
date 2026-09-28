label iwanka_pregnancy_notify:
    scene expression player.location.background
    "{i}*Brrrzzzt* *Brrrzzzt*{/i}"

    scene expression background(288, 368, 3.5, l=L_rump_second) as underlay:
        xoffset -400
    show iwanka a_phone f_excited:
        xoffset -500

    $ renpy.dynamic(stage=player.location.background_phone)
    show expression stage as stage
    show anon f_confused with dissolve:
        flip
    anon @ -m_talk "Hmm?"

    if not M_iwanka.once('number_known'):
        anon a_phone f_normal_low "It's {b}Iwanka{/b}."
        show anon a_phone_talk f_normal with dissolve:
            unflip
            xoffset 500
    else:

        anon a_phone f_thinking_down "I don't recognize this number..."
        show anon a_phone_talk f_confused with dissolve:
            unflip
            xoffset 500

    show expression stage as stage at phoneleft with phoneleft.show
    anon "Hello?"
    iwanka "Hey, {b}[firstname]{/b}."
    anon "Who is this?"
    iwanka @ f_laugh "Oh em gee!"
    iwanka "Don't you recognize your girlfriend's voice?"
    anon f_worried "Ehh..."
    iwanka "It's {b}Iwanka{/b}, you dork!"
    anon f_surprised "{b}Iwanka{/b}?!"
    pause
    anon f_shy "That's umm... I mean, I knew it was you..."
    iwanka @ -m_talk "Mhmm."
    iwanka "Whatever, listen..."
    iwanka f_bored "... You know all that really awesome sex we've been having?"
    anon "Yeah?"
    iwanka "Well, I'm pregnant."
    anon f_surprised @ f_shock "!!!"
    anon "You're pregnant?!"
    iwanka "Yeah."
    pause
    iwanka f_smirk "But don't freak out or anything, I'm taking care of it."
    anon f_worried "Wait, what does that mean?"
    anon "Are you getting rid of it?"
    iwanka @ f_laugh "Well, duh!"
    iwanka f_bored "I don't want a baby..."

    menu:
        "Okay, phew!":
            jump iwanka_pregnancy_notify.relief
        "Why not?":

            pass

    anon f_worried "Why not?"
    iwanka f_annoyed "Are you joking?"
    iwanka "Have you ever seen a woman with a baby at a party?"
    anon "No."
    iwanka "It's fucking tragic!"
    iwanka "I don't wanna be like that."
    pause
    iwanka f_concerned "Plus, I grew up with {b}Melonia{/b}!"
    iwanka "I'm definitely not equipped to be a good mother!"

    menu:
        "It's your decision.":
            jump iwanka_pregnancy_notify.defer
        "You're being silly.":

            pass

    anon f_shy "You're being silly."
    anon "You'll be a fine mother, {b}Iwanka{/b}."
    pause
    iwanka "How can you be sure?"
    anon "Look at it this way... {b}Melonia{/b} basically taught you everything not to do, right?"
    iwanka f_suspicious "Yeah?"
    anon "So just do the opposite of what she would do."
    pause
    iwanka f_excited "I never thought about it like that..."
    iwanka @ f_laugh "You know, a baked potato would have been a better mother than her."
    anon f_normal "And I'll be there to help whenever you need me."
    iwanka "You promise?"
    anon "Of course."

    if not player.has_required_chr(6):
        jump iwanka_pregnancy_notify.later

    iwanka f_normal "I can't believe I'm considering this..."
    anon "Think about it, {b}Iwanka{/b}."
    anon "A baby that's half you and half me."
    iwanka f_excited "It would be cool to have a little version of myself running around."
    iwanka "I could take her shopping and teach her how to manipulate boys..."
    anon "Yeah, or it could be a little boy."
    iwanka "No, it's gonna be a girl."
    iwanka "I decided."
    anon "Heh, I don't think it works like that..."
    iwanka f_annoyed "It's a girl, {b}[firstname]{/b}!"
    iwanka "End of story."
    anon @ f_worried -m_talk "..."
    anon "So we're doing this?"
    $ display.toast(chr_pass)
    iwanka f_excited @ f_laugh "Yeah, you convinced me."
    anon "Awesome!"
    iwanka "Meet me at the yacht later to celebrate?"
    anon "Of course!"
    show anon f_looking_down a_phone with dissolve
    show expression stage as stage with {'master': phoneleft.hide}
    "{i}*Beep*{/i}"
    pause
    anon f_grin @ -m_talk "( I can't believe it... )"
    anon @ -m_talk "( I'm gonna be a father! )"
    anon @ -m_talk "( This is so exciting! )"
    hide anon with dissolve
    return True


label iwanka_pregnancy_notify.defer:
    anon f_worried "It's your decision."
    anon "If you're sure?"
    iwanka f_excited "I am."
    pause
    iwanka "I'll take care of it and you can just meet me at the yacht later, okay?"
    anon "{i}*Sigh*{/i} Yeah, okay."
    iwanka "Goodbye, {b}[firstname]{/b}."
    show anon f_looking_down a_phone with dissolve
    show expression stage as stage with {'master': phoneleft.hide}
    "{i}*Beep*{/i}"
    pause
    anon f_sad_down @ -m_talk "( Damn. )"
    hide anon with dissolve
    return


label iwanka_pregnancy_notify.later:
    iwanka f_concerned "N-no, this is too soon!"
    anon f_worried "{b}Iwanka{/b}, I really think-"
    $ display.toast(chr_fail)
    iwanka "Sorry, {b}[firstname]{/b}."
    iwanka "I've made up my mind."
    anon @ -m_talk "..."
    iwanka "Perhaps some time down the road but not now."
    anon "Alright."
    iwanka f_normal "I'll take care of it and you can just meet me at the yacht later, okay?"
    anon "{i}*Sigh*{/i} Yeah, okay."
    iwanka "Goodbye, {b}[firstname]{/b}."
    show anon f_looking_down a_phone with dissolve
    show expression stage as stage with {'master': phoneleft.hide}
    "{i}*Beep*{/i}"
    pause
    anon f_sad_down @ -m_talk "( Damn. )"
    hide anon with dissolve
    return


label iwanka_pregnancy_notify.relief:
    anon f_shy "Okay, phew!"
    anon "Yeah, we are definitely not ready to be parents!"
    iwanka f_excited "I agree."
    pause
    iwanka f_smirk "Let's just keep things the way they are, yeah?"
    anon "Sounds good."
    iwanka "And maybe pull out from now on?"
    anon "Heh, you got it."
    iwanka "Meet me at the yacht later?"
    anon "Sure thing."
    show anon f_looking_down a_phone with dissolve
    show expression stage as stage with {'master': phoneleft.hide}
    "{i}*Beep*{/i}"
    pause
    anon @ -m_talk "( That takes care of that. )"
    hide anon with dissolve
    return


label iwanka_pregnancy_notify.repeat:
    scene expression player.location.background
    "{i}*Brrrzzzt* *Brrrzzzt*{/i}"

    scene expression background(288, 368, 3.5, l=L_rump_second) as underlay:
        xoffset -400
    show iwanka a_phone f_excited:
        xoffset -500

    $ renpy.dynamic(stage=player.location.background_phone)
    show expression stage as stage
    show anon f_confused with dissolve:
        flip
    anon @ -m_talk "Hmm?"
    anon a_phone f_normal_low "It's {b}Iwanka{/b}."
    show anon a_phone_talk f_normal with dissolve:
        unflip
        xoffset 500
    show expression stage as stage at phoneleft with phoneleft.show
    anon "Hello?"
    iwanka "Hey, {b}[firstname]{/b}."
    anon f_worried "Is everything okay?"
    iwanka "Well, kinda..."
    pause
    iwanka f_bored "... You know how we had all that awesome sex and then I got pregnant?"
    anon "Yeah?"
    iwanka "Well, it happened again."
    anon f_surprised "!!!"
    anon "You're pregnant?!"
    iwanka "Yeah."
    anon f_normal "We're gonna have another baby?!"
    iwanka "I mean, unless you don't want another one..."
    anon f_shy "N-no, I definitely want another one!"
    anon "This is amazing news!"
    iwanka "Yeah, I thought you'd be happy."
    anon "Aren't you?"
    iwanka "Psh, yeah... Totally..."
    iwanka @ f_eyeroll "I get to spend another nine months sober... Awesome!"
    show anon f_worried
    pause
    iwanka "So, I'll catch you later at the {b}yacht{/b}?"
    anon "Yeah, I'll be there."
    show anon f_looking_down a_phone with dissolve
    show expression stage as stage with {'master': phoneleft.hide}
    "{i}*Beep*{/i}"
    pause
    anon f_grin @ -m_talk "( I can't believe it... )"
    anon @ -m_talk "( I'm gonna be a father! )"
    anon @ -m_talk "( This is so exciting! )"
    hide anon with dissolve
    return True


label iwanka_pregnant_labor_1:
    scene expression player.location.background_blur
    show anon f_normal with dissolve
    anon "Looks like I got a text."
    hide anon with dissolve
    return


label iwanka_pregnant_labor_2:
    scene expression player.location.background_blur
    if player.location != L_map:
        show anon f_surprised a_phone with dissolve
    anon "{b}Iwanka{/b} is having the baby?!"
    anon "Holy crap!"
    pause
    anon "I'd better head to {b}the clinic{/b} to check on them."
    if player.location != L_map:
        hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
