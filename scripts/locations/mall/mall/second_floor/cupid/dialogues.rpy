label cupid_daisy_get_new_flowers:
    scene expression player.location.background_blur
    show player 11 with dissolve
    player_name "( Whoa. )"

    player_name "( I wasn't expecting such a huge selection of flowers... )"

    pause
    show player 13
    player_name "( I should {b}see if they have any sunflowers for Daisy{/b}. )"

    hide player with dissolve
    return

label cupid_mom_cupid_store:
    scene expression player.location.background_blur
    show player 5 at left
    show old_debbie 165f at Position(xpos=0.5, ypos=1.0)
    with dissolve
    debbie "Wah!"

    show old_debbie 166f
    debbie "Look at all the pretty things!"

    show old_debbie 165 at Position(xpos=0.75, ypos=1.0) with dissolve
    debbie "Isn't it wonderful, {b}[firstname]{/b}?!"

    show old_debbie 164
    player_name "..."
    show player 10
    player_name "I dunno {b}[deb_name]{/b}, it seems pretty girly in here..."

    show player 5
    show old_debbie 165
    debbie "Well, yeah..."

    show old_debbie 166
    debbie "But I AM a girl, sweetheart."

    show old_debbie 164
    debbie "..."
    show old_debbie 165
    debbie "Besides, you're obviously starting to become more interested in girls."

    show old_debbie 167 at right with dissolve
    debbie "... And if you want to keep one you'll have to start getting acquainted with places like this!"

    show old_debbie 164 at Position(xpos=0.9, ypos=1.0) with dissolve
    show player 10
    player_name "Benar-benar?"

    show player 5
    show old_debbie 166
    debbie "Hehe, tentu saja!"

    show old_debbie 165
    debbie "Why don't you help me pick something out. It'll be good practice for you!"

    show player 10
    show old_debbie 164
    player_name "Practice?"

    show player 5
    show old_debbie 166
    debbie "Ya!"

    show old_debbie 165
    debbie "{b}[firstname]{/b}, {b}gift giving{/b} is a very important part of {b}dating{/b}."

    show player 43
    show old_debbie 164
    player_name "Yeah, I know that, {b}[deb_name]{/b}!"

    show player 5
    show old_debbie 165
    debbie "Okay, well... Pretend that you're dating me."

    show old_debbie 164
    player_name "..."
    show player 12
    player_name "Kamu serius?"

    show player 11
    show old_debbie 166
    debbie "Hehe, yesss!"

    show old_debbie 165
    debbie "If you were dating me... What kind of gift do you think I'd like?"

    show player 10
    show old_debbie 164
    player_name "Hmm, saya tidak yakin."

    show player 11
    show old_debbie 165
    debbie "Well, take a look around, and see if you can find something!"

    debbie "I'll be waiting over here."

    show player 10
    show old_debbie 164
    player_name "Baiklah."

    hide old_debbie with dissolve
    show player 4 at Position(xpos=0.375, ypos=1.0) with dissolve
    player_name "( What would {b}[deb_name]{/b} like? )"

    player_name "( ... )"
    player_name "( A {b}necklace{/b} maybe? )"

    hide player with dissolve
    return

label necklace_display_mom_choose_gift:
    scene expression player.location.background_blur
    show player 4 zorder 0 at left
    player_name "Yeah, a necklace could definitely work."

    player_name "But which one?"

    show player 492
    show xtra 33 zorder 1 at Position(xpos=0.295, ypos=0.749)
    with dissolve
    player_name "... No. Too gaudy."

    show xtra 32 with dissolve
    player_name "Hmm, no... This one is too childish for her, I think."

    show xtra 31 with dissolve
    player_name "Oh, this one looks like her!"

    player_name "Itu sempurna!"

    player_name "Now, let's see if she agrees!"

    hide xtra
    hide player
    with dissolve
    $ player.get_item("pearl_necklace")
    call popup ('give', 'pearl_necklace')
    return

label necklace_display_repeat:
    scene expression player.location.background_blur
    call popup ('alpha')
    return

label cupid_dressroom_mom_dressing_room:
    scene expression background(712, 400, 3.5, l=L_cupid) as stage
    show player 10 at Position(xpos=0.2) with dissolve
    player_name "{b}[deb_name]{/b}, you alright in there?"

    player_name "What's taking so long?"

    show player 11
    debbie "Actually, sweetie, could you come in here for a second?"

    player_name "..."
    show player 10
    player_name "You want me to come in there?!"

    show player 11
    debbie "Ya, tolong."

    show player 10
    player_name "... Oke."

    show player 11
    hide player with dissolve


    scene expression L_cupid_dressroom.background

    show old_debbie 169 zorder 1 at Position(xpos=0.65, ypos=1.0)
    show mneck 1 zorder 2 at Position(xpos=0.65, ypos=0.535)
    show player 10 at Position(xpos=0.35, ypos=1.0) with dissolve
    player_name "Ada apa?"

    show player 11
    show old_debbie 168
    debbie "Oh, I got the necklace snagged on something and I can't get it to unclasp."

    debbie "Could you give me a hand?"

    show player 10
    show old_debbie 169
    player_name "T-tentu saja."

    show player 228b zorder 2 at Position(xpos=0.475, ypos=1.0)
    show old_debbie 178 zorder 1 at Position(xpos=0.60, ypos=1.0)
    hide mneck 1
    with dissolve

    debbie "Oh!"

    show old_debbie 177b
    debbie "..."
    show old_debbie 178b
    debbie "Oh my..."

    show player 228c
    show old_debbie 177b
    player_name "Apa itu?"


    show old_debbie 178b
    show player 228d
    debbie "{i}*Ahem*{/i} N-nothing sweetheart."

    debbie "Can you see where it's snagged?"

    show player 228c
    show old_debbie 177b
    player_name "Yup, I see it. Just hold still one second."

    show player 228d
    player_name "..."
    show player 228c
    player_name "Man, you really got it stuck."

    show player 228d
    debbie "..."
    show player 228c
    player_name "Almoooost..."

    player_name "Got iiiit..."

    show player 228d
    player_name "..."
    show old_debbie 179
    debbie "Hehehe."

    show player 228c
    player_name "What's so funny?"

    show player 228d
    show old_debbie 178
    debbie "N-nothing. It's silly."

    show player 228c
    show old_debbie 177
    player_name "Oh c'mon, tell me."

    show player 228d
    show old_debbie 178
    debbie "I'm just thinking about that movie we watched the other night."

    show player 228c
    show old_debbie 177
    player_name "That cheesy romance flick?"

    show player 228d
    show old_debbie 178
    debbie "Y-ya."

    show player 228c
    show old_debbie 177
    player_name "Bagaimana dengan itu?"

    show player 228d
    show old_debbie 178
    debbie "There was a scene just like this... Remember?"

    show old_debbie 177
    player_name "..."
    show player 228c
    player_name "Oh ya!"

    player_name "He helped the girl out with her necklace, and then he-"

    show player 227d at Position(xpos=0.35, ypos=1.0) with dissolve
    player_name "{i}*Meneguk*{/i}"

    show player 227c
    player_name "Kissed her."

    show player 227d
    show old_debbie 178
    debbie "Eh ya."

    show player 228d at Position(xpos=0.475, ypos=1.0) with dissolve
    debbie "Have you kissed a girl yet, {b}[firstname]{/b}?"

    show player 228c
    show old_debbie 177
    player_name "... Tidak."

    show player 228d
    debbie "..."
    show old_debbie 179
    debbie "Well, that's okay, sweetheart! There's nothing wrong with that."

    show old_debbie 177
    player_name "..."
    show old_debbie 178
    debbie "Would you like to try?"

    show player 227c at Position(xpos=0.35, ypos=1.0) with dissolve
    show old_debbie 177
    player_name "Kamu serius?"

    show player 227d
    show old_debbie 178
    debbie "Well, yeah... I suppo-"

    hide player
    hide old_debbie
    show old_debbie 180b
    with dissolve

    debbie "( !!! )"

    show old_debbie 180
    pause
    show old_debbie 181
    debbie "Hmm..."

    show old_debbie 182
    pause

    debbie "... Wow."

    debbie "Sweetie, we can't... I-I mean I shouldn't have..."

    hide old_debbie
    show player 5 at Position(xpos=0.35, ypos=1.0)
    show old_debbie 169b zorder 1 at Position(xpos=0.65, ypos=1.0)
    show mneck 1 zorder 2 at Position(xpos=0.65, ypos=0.535)
    with dissolve
    player_name "..."
    debbie "..."
    show player 10
    player_name "I'm sorry, {b}[deb_name]{/b}."

    show player 5
    show old_debbie 168
    debbie "NO! No... It's me, I shouldn't have let myself..."

    show old_debbie 169b
    debbie "..."
    show old_debbie 168
    debbie "{i}*Ahem*{/i} W-why don't you just see about getting that necklace unstuck."

    show old_debbie 169b
    player_name "..."
    show player 10
    player_name "Y-yeah, sure thing, {b}[deb_name]{/b}."

    show player 228b zorder 2 at Position(xpos=0.475, ypos=1.0)
    show old_debbie 177 zorder 1 at Position(xpos=0.60, ypos=1.0)
    hide mneck 1
    with dissolve
    pause
    player_name "..."
    pause

    show player 492 zorder 3 at Position(xpos=0.35, ypos=1.0)
    show xtra 31 zorder 4 at Position(xpos=0.4575, ypos=0.749)
    show old_debbie 169b zorder 1 at Position(xpos=0.65, ypos=1.0)
    with dissolve
    player_name "There we go, all fixed."

    show player 493
    debbie "..."
    show old_debbie 168
    debbie "Terima kasih sayang."

    debbie "Why don't you go put the necklace back in its display case."

    debbie "I'll be out in just a moment..."

    show player 492
    show old_debbie 169b
    player_name "Ya baiklah."

    hide player
    hide xtra
    with dissolve
    debbie "..."
    show old_debbie 164b with dissolve
    debbie "( Oh god... I can't believe I just did that! )"

    debbie "( The poor thing is having a hard enough time as it is. )"

    debbie "( What in the world was I thinking... )"

    hide old_debbie with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
