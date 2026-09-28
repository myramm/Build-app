label mom_cupid_outing_choose_gift:
    show player 5 at left with dissolve
    show old_debbie 165 at Position(xpos=.75, ypos=1.0) with dissolve
    debbie "Did you find something, sweetheart?"
    show player 10
    show old_debbie 164
    player_name "I'm still looking."
    show player 5
    show old_debbie 166
    debbie "Hehe, okay!"
    show old_debbie 165
    debbie "Don't look so serious. It's easy! Just find something you think I'll like..."
    show old_debbie 164
    pause
    hide old_debbie with dissolve
    show player 4 at Position(xpos=0.5, ypos=1.0) with dissolve
    player_name "( ... )"
    player_name "( Something {b}[deb_name]{/b} would like? )"
    player_name "( A necklace perhaps? )"
    return

label mom_cupid_outing_show_necklace:
    show player 492 zorder 0 at left
    show xtra 31 zorder 1 at Position(xpos=0.295, ypos=0.749)
    with dissolve
    show old_debbie 164 at Position(xpos=0.75, ypos=1.0) with dissolve
    player_name "Okay, {b}[deb_name]{/b}. How about this?"
    hide xtra
    show player 1 with dissolve
    show old_debbie 170 at Position(xpos=0.7, ypos=1.0) with dissolve
    show old_debbie 172
    debbie "Oh, {b}[firstname]{/b}... What a beautiful {b}necklace{/b}."
    show old_debbie 170
    show player 14
    player_name "You really like it?"
    show player 13
    show old_debbie 171
    debbie "I do! You have great taste, sweetie."
    show old_debbie 170
    show player 14
    player_name "Heh, thanks, {b}[deb_name]{/b}!"
    show player 13
    show old_debbie 173 at Position(xpos=0.775, ypos=1.0)
    pause 1
    show old_debbie 174 at Position(xpos=0.7, ypos=1.0)
    pause 1
    show old_debbie 175
    pause 2
    show old_debbie 164 zorder 1 at Position(xpos=0.75, ypos=1.0)
    show mneck 1 zorder 2 at Position(xpos=0.7475, ypos=0.535)
    pause
    show old_debbie 165
    debbie "Well?"
    show player 14
    show old_debbie 164
    player_name "... Hmm?"
    show player 13
    show old_debbie 166
    debbie "How do I look?"
    show player 14
    show old_debbie 164
    player_name "You look beautiful, {b}[deb_name]{/b}!"
    show player 13
    show old_debbie 166
    debbie "Aww... Thanks, sweetheart."
    show old_debbie 164
    debbie "Hmm..."
    show old_debbie 165
    debbie "Where's a mirror when you need one?"
    show old_debbie 164
    player_name "..."
    show player 14
    player_name "There's probably one in the dressing room..."
    show player 13
    show old_debbie 165
    debbie "Good thinking, sweetie!"
    debbie "I'll be right back."
    hide old_debbie
    hide mneck
    with dissolve
    show player 14
    player_name "Okay."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
