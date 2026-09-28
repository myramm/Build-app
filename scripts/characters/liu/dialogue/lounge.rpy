label liu_button_lounge:
    show anon b_dressed_floor behind table with dissolve:
        xoffset -230
    liu "I'm having green tea with honey."
    liu "It's very healthy."
    show liu a_hold
    show liu_overlay_o_tea_table_pot as table
    with dissolve
    pause
    liu f_happy "Would you like some?"

    menu liu_button_lounge.choice:
        "Dad's money." if M_anon.is_state(S_ano28_cash):
            jump liu_button_lounge.backpack
        "Yeah, sure.":

            jump liu_button_lounge.tea
        "I love you in that kimono!":

            jump liu_button_lounge.kimono
        "Sex.":

            jump liu_button_lounge.sex
        "I'll see you later.":

            pass

    anon "I'll see you later."
    liu f_worried "Leaving so soon?"
    anon f_shy "Yeah, I've got things to do."
    liu f_worried_down "Aww, okay..."
    hide anon
    hide liu
    with dissolve

    scene expression background(400, 400, 2) as stage
    show anon b_empty f_shy_low
    show liu b_robe_hug behind anon:
        xoffset 0
    with fade
    pause
    liu "You'll come back again, yeah?"
    show anon a_beer_cheer b_dressed f_normal behind liu
    show liu b_robe_hair:
        xoffset -300
    with {'master': dissolve}
    anon "Of course."
    liu f_happy "Bye, {b}[firstname]{/b}."
    anon "Later, {b}Liu{/b}."
    hide anon with dissolve
    return


label liu_button_lounge.backpack:
    anon f_worried_left "Pants!"
    show liu f_confused
    anon f_worried "I left my backpack by the door, two seconds!"
    hide anon with dissolve

    scene expression background(216, 384, 4.5) as stage
    show anon a_backpack1 f_looking_down
    with fade
    show liu b_robe_hair f_worried behind anon with dissolve
    liu "What is it?!"
    show anon f_normal
    jump ano28_cash_liu_money


label liu_button_lounge.kimono:
    anon f_flirt "I love you in that kimono!"
    liu f_curious "Yeah?"
    anon @ -m_talk "Mhmm."
    liu f_sexy "Perhaps I should model it again for you?"

    menu:
        "Yes, please!":
            jump liu_button_lounge.model
        "Maybe later?":

            pass

    anon f_worried "I don't want your nice tea to get cold."
    liu f_worried_down "Oh, yes... That's good thinking!"
    show anon a_tea_drink f_drink
    show liu a_drink f_drink
    with dissolve
    pause
    show anon a_down f_normal
    show liu a_down f_happy
    with {'master': dissolve}
    anon "Mmm, delicious."
    jump liu_button_lounge.choice


label liu_button_lounge.model:
    anon "Definitely!"
    liu f_laugh "Heh, anything for you, {b}[firstname]{/b}!"
    show anon f_shy_high
    hide liu
    with dissolve

    scene expression game.timer.image('location_liu_lounge_close{}')
    show liu b_robe_front1 f_normal
    with fade
    liu "Like this?"
    anon "You are so beautiful!"
    liu f_normal_down "{b}[firstname]{/b}!!"
    liu "You're making me blush!"
    anon "C'mon, baby... show it off for me a little..."
    liu b_robe_front2 f_normal "Heh, like this?"
    anon "Yes."
    anon "Just like that."
    pause
    anon "Oh my gosh, you're so sexy!"
    liu "Hehe!"

    scene expression game.timer.image('location_liu_lounge_tea{}')
    show anon b_dressed_floor f_shy_high:
        xoffset -230
    show liu_overlay_o_tea_table_pot as table
    with fade
    show anon f_flirt
    show liu b_robe_tea f_happy behind table
    with dissolve
    liu "Thank you, {b}[firstname]{/b}."
    liu "You always make me so good about myself."
    anon f_normal "As well you should."
    anon f_happy "You are gorgeous!"
    liu "Hehe!"
    jump liu_button_lounge.choice


label liu_button_lounge.sex:
    jump liu_button_bedroom.sex


label liu_button_lounge.tea:
    anon "Oooh, yes please!"
    show anon f_normal_low
    show liu a_give
    with {'master': dissolve}
    liu "Here you go."
    show anon a_tea_hold f_normal
    show liu a_down
    with dissolve
    anon "Thanks."
    show anon a_tea_drink f_thinking_down with dissolve
    pause
    show anon a_down f_surprised with {'master': dissolve}
    anon "Wow, that's delicious!"
    liu f_happy "Heh, thank you."
    show anon f_normal
    liu "My mother used to make it for me when I was a child, it was her favorite."
    anon "That's neat!"
    pause
    anon f_confused "Say, do you ever think about getting in touch with your parents?"
    show liu f_nervous
    anon "You know, now that {b}Kim{/b} is out of the picture..."
    liu "Umm, not really..."
    show anon f_worried
    liu f_worried_down "... I don't think they have a phone or anything so, contacting them wouldn't be easy."
    anon f_shy "You could try writing them."
    show liu f_worried
    anon "I bet your mother would love to hear that you're doing so well now."
    liu f_nervous "Heh, you're so sweet, {b}[firstname]{/b}."
    liu f_happy "Perhaps I should try and write a letter to them..."
    anon "Yeah, I think so."
    anon f_normal "It would be good for you to reconnect, even if it's just by letter."
    jump liu_button_lounge.choice
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
