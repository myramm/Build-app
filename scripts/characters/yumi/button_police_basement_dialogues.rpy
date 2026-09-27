label yumi_police_basement_dialogue_pre:
    scene police_c_3 with None
    show old_yumi 2 at right
    show player 1 at left
    with dissolve
    yumi "Hello, are you a visitor or are you here to post bail?"

    show old_yumi 1
    return

label yumi_police_basement_dialogue_donuts:
    show player 14 at left
    show old_yumi 1 at right
    player_name "I know you only recently started working with him..."

    show old_yumi 3
    player_name "... But would you happen to know what kind of donuts {b}Harold{/b} likes?"

    show player 1
    show old_yumi 4
    yumi "Hah?"

    yumi "Mengapa kamu bertanya?"

    show old_yumi 1
    show player 14
    player_name "Oh, I'm... Trying to get him to like me."

    show player 1
    show old_yumi 2
    yumi "Huh. That's... Strange."

    show player 14
    show old_yumi 1
    player_name "I know, but I'm friends with his daughter and-"

    show player 11
    show old_yumi 2
    yumi "You don't need to explain. I think I got the picture."

    show player 1
    yumi "Well, every time we visit the donut shop... He puts {b}[harold_topping]{/b} on the top of his donuts."

    show player 14
    show old_yumi 1
    player_name "Benar-benar?"

    show player 1
    show old_yumi 2
    yumi "Yeah, he always gets that topping."

    show player 17
    show old_yumi 1
    player_name "Okay, thanks for helping me!"

    show player 1
    show old_yumi 2
    yumi "Tidak masalah!"

    return

label yumi_police_basement_dialogue_harold:
    show player 12
    player_name "Tahukah Anda di mana {b}Harold{/b} berada?"

    player_name "Aku perlu berbuat salah... Kembalikan sesuatu padanya!"

    show player 5
    show old_yumi 4
    yumi "You know, I saw him just this morning!"

    yumi "He looked... Off... And smelled like alcohol..."

    show old_yumi 3
    show player 10
    player_name "Alcohol?!"

    show player 11
    show old_yumi 4
    yumi "Yeah, but don't tell anyone!"

    yumi "The poor guy's been having problems with his wife."

    yumi "I just don't get it, you know? He's such a nice guy..."

    yumi "... I think he deserves better, that's for sure!"

    show old_yumi 3
    show player 12
    player_name "You don't know where he went after this morning, do you?"

    show player 5
    show old_yumi 4
    yumi "Hmm... I'm not sure, but he took his car."

    show old_yumi 3
    show player 35
    player_name "So he went for a drive somewhere..."

    show player 14
    player_name "... Alright, thanks!"

    hide player
    hide old_yumi
    with dissolve
    return

label yumi_police_basement_dialogue_leave:
    show player 14 at left
    show old_yumi 1 at right
    player_name "I'm just here to visit someone."

    show old_yumi 2
    show player 1
    yumi "Sure. Make sure you leave your backpack in the bin, and stay behind the line."

    yumi "There's no touching allowed."

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
