label tony_button_baby:
    show anon with dissolve:
        flip
    if randomizer() > 80:
        tony "So then, I looked the cocksucker right in his face and told him, \"Forgiveness is between you and god.\""
        tony "\"I'm just here to arrange the meetin'.\""
        tony @ f_laugh "Hahahaah!!"
        tony "Boy, he shit his pants then... Lemme tell ya!"
    elif randomizer() > 60:
        tony "So then, Luigi tells the guy, \"I came here to crack skulls and eat ciabatta sandwiches\"..."
        tony "... \"And I'm all outta ciabatta sandwiches.\""
        tony @ f_laugh "Hahahaah!!"
        tony "That douchebag shut his mouth real quick after that..."
    elif randomizer() > 40:
        tony "So then, I says, \"Yeah, I'll take ya to the bank\"..."
        tony "... \"The fuckin' blood bank!\""
        tony "Bang, bang, bang!"
        tony @ f_laugh "Hahahaah!!"
        tony "Took 'em hours to clean his brains outta the carpet!"
        tony "That's why you always take 'em somewhere with hardwood floors..."
    elif randomizer() > 20:
        tony "So then, Luigi says, \"You're still dangerous\"..."
        tony "... \"But you can be my wingman anytime!\""
        tony "And then I says, \"Bullshit!\"..."
        tony "... \"You can be mine!\"."
        tony @ f_laugh "Hahahaah!!"
        tony "You shoulda seen his face!"
    else:
        tony "So then, I says, \"Say hello to my little friend!\""
        tony "Bang, bang, bang!"
        tony @ f_laugh "Hahahaah!!"
        tony "Dumb bastards didn't know what hit 'em!"

    menu tony_button_baby.choice:
        "What are you doing?":

            jump tony_button_baby.stories
        "{b}Where's Maria{/b}?":

            jump tony_button_baby.maria
        "I'll leave you be.":

            pass

    anon f_normal a_wave "I'll leave you be."
    tony f_normal "There's some deliveries on the counter for ya."
    anon "Thanks!"
    hide anon with dissolve
    return


label tony_button_baby.maria:
    anon f_normal "{b}Where's Maria{/b}?"
    tony f_normal "She's in the back, cookin' up a storm."
    anon "Alright."
    tony "Give her my love, eh?"
    anon "Sure thing."
    tony @ f_smirk_wink "And don't make too much noise!"
    pause
    tony "I don't want any customers hearin' you two..."
    hide anon with dissolve
    return


label tony_button_baby.stories:
    anon f_normal "What are you doing?"
    tony f_normal @ -m_talk "Hmm?"
    tony "Oh, I was just tellin' some stories from the old days..."
    anon "To the baby?"
    tony @ f_laugh "Yeah."
    pause
    tony f_sad "Too much?"
    anon f_shy a_behind_head "Ehh."
    anon "I'm just worried it's a little.... Nightmare inducing..."
    show anon a_idle with dissolve
    tony f_normal "Pfft, it ain't like I'm tellin' ghost stories..."
    tony "This is stuff that really happened!"
    anon "Maybe stick to children's tales?"
    anon "I'll get you a book or something..."
    tony "Heh, You do that."
    jump tony_button_baby.choice
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
