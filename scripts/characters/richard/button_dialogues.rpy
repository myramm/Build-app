label button_richard_intro_day:
    show player 14 at left
    show richard
    with dissolve
    player_name "Hey, {b}Richard{/b}."

    show player 13
    show richard f_confused
    richard "Oh no, {b}Lucy{/b} didn't order another batch of that milk, did she?"

    show player 12
    player_name "Hah?"

    show player 10
    player_name "No, I was just in the neighborhood and I thought-"

    show player 5
    show richard f_phone
    richard "Thank god!"

    show richard f_normal
    richard "I swear that woman has no concept of money."

    pause
    richard "{i}*Sigh*{/i} Now what is it that you want?"

    return

label button_richard_intro_night:
    show player 10 at left
    show richard
    with dissolve
    player_name "Hey, {b}Richard{/b}."

    show player 5
    show richard f_angry
    richard "What are you doing here kid?"

    richard "Can't you see I'm trying to relax in the privacy of my own home?!"

    show player 10
    player_name "I err..."

    player_name "Saya minta maaf."

    show player 5
    pause
    show richard f_phone
    richard "{i}*Huh*{/i}"

    show richard f_normal
    richard "Apa yang kamu inginkan?"

    return

label button_richard_take_it_easy_lucy:
    show player 10 at left
    show richard f_normal
    player_name "Why are you always so strict with your wife?"

    show player 5
    show richard f_angry
    richard "What did you say?!"

    pause
    richard "That's none of your business, is it?"

    show player 10
    player_name "I just..."

    player_name "She seems like a real nice lady, and she's trying very hard to-"

    show player 5
    show richard f_normal
    richard "Hah! That's real easy for you to say, kid."

    show richard f_angry
    richard "You're not the one she's putting in the poor house with all her stupid daycare ideas!"

    show player 12
    player_name "Y-ya, tapi-"

    show player 5
    richard "I'm out here busting my hump, every day, trying to start something real!"

    richard "I've got enough problems without adding your mouth to the list."

    richard "So unless you've got real business with me, I suggest you move on."

    return

label button_richard_hows_the_business:
    show player 10 at left
    show richard f_normal
    player_name "How's your carpentry business going?"

    show player 5
    richard "Why, do you have a lead on some work for me?!"

    show player 10
    player_name "N-no, not really..."

    show player 5
    show richard f_phone
    richard "Ugh, figures."

    show richard f_normal
    richard "Business is progressing."

    richard "Slowly."

    show player 14
    player_name "Well, any progress is good progress, right?"

    show player 13
    richard "Ya, saya kira."

    richard "Still, after all these years, I really thought I'd be further along."

    show player 5
    return

label button_richard_nothing_day:
    show player 10 at left
    show richard f_normal
    player_name "I don't need anything."

    player_name "Maaf mengganggumu."

    show player 5
    richard "Eh ya."

    hide player
    hide richard
    with dissolve
    return

label button_richard_nothing_night:
    show player 10 at left
    show richard f_normal
    player_name "I don't need anything."

    show player 5
    show richard f_angry
    richard "Well, beat it then!"

    show richard f_normal
    richard "{b}Tool Time{/b} is starting up any second and I don't wanna miss any of the jokes!"

    show player 11
    player_name "..."
    hide player
    hide richard
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
