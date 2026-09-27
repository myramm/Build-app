label dia03_give_pizzeria_interior:
    call tony_button_stage
    show anon with dissolve:
        flip
    tony "Well, hey there, champ."

    tony "You're just in time."

    tony "I got some pies here in need of delivery with your name on 'em."

    anon f_worried "Oh, umm... Actually-"

    show anon a_backpack f_shy_down with dissolve
    pause
    show anon a_milk_cartons_small f_normal with dissolve
    tony f_suspicious @ a_point "Whatchu got there?"

    anon "Milk delivery for you."

    tony f_normal @ a_frustrated "What, you're workin' two jobs now?"

    tony "Am I not payin' you enough?"

    anon @ f_worried "N-no, no... It's not like that."

    anon "I'm just helping out my friend."

    tony f_suspicious "Your friend?"

    anon "Yeah, the milk business is hers."

    tony "Your friend is {b}Auntie Diane{/b}?!"

    tony "The lady on the label?"

    anon @ f_laugh "Ya."

    tony f_normal @ f_laugh a_belly "Tidak bercanda?"

    tony "What a small world..."

    pause
    tony @ a_finger_up "I dunno what kind of cows your friend is usin' but her milk is amazin'!"

    tony "Our food has gone to a whole 'nother level since we started usin' it."

    anon "Hehe, I'm sure {b}Diane{/b} will be happy to hear that."

    tony f_suspicious @ a_wave "I'm not jokin', champ."

    tony @ a_point "You tell her, that next time, I'm gonna triple my order."

    anon "Hehe, oke."

    anon "Umm, where should I put this?"

    tony f_normal "Oh, right. One second..."

    show tony f_suspicious a_whisper with dissolve:
        unflip
        xoffset -400
    tony "Hey, {b}Maria{/b}!"

    tony "Getcha butt up here for a second!"

    show tony f_normal a_idle with dissolve
    pause
    show maria b_magic f_annoyed behind counter:
        flip
        xoffset -200
    with dissolve
    maria "{i}*Sigh*{/i} Why you always gotta interrupt me when I'm foldin' calzones, {b}Tony{/b}?"

    show maria f_normal
    if M_anon.finished_state(S_ano11_bone):
        maria "Oh, hey there, {b}[firstname]{/b}."

    else:
        maria "Oh, hey there, kid."

    maria "Whatchu got there?"

    tony "He brought us the milk order."

    maria f_confused "What, you're workin' two jobs now?"

    if M_anon.finished_state(S_ano11_bone):
        maria f_annoyed "You better give the boy a raise, {b}Tony{/b}!"

        maria "I don't want him workin' nowhere else."

        tony "Calm down, darlin'."

    else:
        maria "Are we not payin' you enough?"

        tony "That's what I asked him!"

    show tony with dissolve:
        flip
        xoffset 0
    anon "It's my friend's business."

    anon "I'm just giving her a hand."

    maria f_normal "Oh."

    maria "Well, that's sweet of ya."

    maria "Come with me to the back and I'll show you where it goes."

    hide maria with dissolve
    anon "Yup, right behind you."

    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
