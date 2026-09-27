label confessional_right_mia_priest_act_pre:
    scene church_confession
    show player 5f at Position (xpos=795)
    show players robe f at Position (xpos=794)
    show helen 16 at Position (xpos=300)
    with dissolve
    helen "Forgive my family, Father, for they have sinned. It has been seven days since my last confession."

    show helen 15
    helen "..."
    show helen 13
    helen "{b}Father{/b}? Are you there?"

    show helen 12
    show player 23f
    player_name "{i}*Cough*{/i}"

    show player 10f
    player_name "Yes... I uhh... I am listening..."

    show player 5f
    show helen 16
    helen "O Lord, I am heartily sorry for the way my family has offended you..."

    helen "... By my husband failing our marriage... And my daughter's whorish behavior..."

    helen "I've tried feverishly to make them see their errors."

    helen "I've instructed them that they were headed to hell if they didn't change."

    helen "... But it seems they've lost the holy path and succumbed to darkness."

    show helen 14
    helen "What should I do, {b}Father{/b}?"

    show helen 15
    return

label confessional_right_mia_priest_act_pray:
    show player 10f
    player_name "Perhaps you could... Err... Pray?"

    show player 22f
    show helen 12
    helen "..."
    show helen 13
    helen "Pray?"

    show helen 12
    show player 10f
    player_name "Tentu!"

    show player 22f
    show helen 13
    helen "I don't quite see how this will help my family, {b}Father{/b}."

    helen "Something must be done! Something must change for them to recognize their sinful and vile behavior."

    show helen 12
    show player 21f
    player_name "Err... The Lord works in mysterious ways!"

    show player 22f
    helen "..."
    show helen 14
    helen "Okay... I will do what I can, {b}Father{/b}."

    show helen 16
    helen "Please ask the Lord to forgive them and could you pray for them too?"

    show helen 15
    show player 10f
    player_name "Sure! Shouldn't be a big deal!"

    show player 5f
    show helen 12
    helen "..."
    show helen 14
    helen "And what, dear {b}Father{/b}, would you have your faithful servant do as penance in my family's stead?"

    show helen 12
    show player 10f
    player_name "Err... Ummm... Two prayers will suffice?"

    show player 5f
    helen "..."
    show helen 13
    helen "Terima kasih..."

    hide helen with dissolve
    show player 24f
    player_name "Damn, I got too nervous..."

    player_name "... I need to try again later, with more confidence."

    hide players robe
    show player 444f
    with dissolve
    pause
    hide player with dissolve
    return

label confessional_right_mia_priest_act_change:
    show player 12f
    player_name "Perhaps it is {b}you{/b} who needs to change, in order for them to return to the path..."

    show player 5f
    show helen 14
    helen "Me?! ... But I've done everything right. I..."

    show helen 12
    show player 12f
    player_name "Yes, you've done a good job pointing out their flaws, but what about your own?"

    player_name "I have yet to hear about your wrong doing. You can't be perfect?"

    show player 5f
    show helen 15
    helen "..."
    show helen 14
    helen "{i}*Huh*{/i}"

    show helen 16
    helen "Maybe you're right, {b}Father{/b}."

    helen "I... May have... Gone too far..."

    show helen 14
    helen "It's just they don't seem to understand their peril... Like I do..."

    helen "I do it, because I love them..."

    show helen 15
    show player 10f
    player_name "You can still redeem yourself!"

    show player 5f
    show helen 14
    helen "Redeem? But what could I do?"

    show helen 15
    show player 12f
    player_name "Maybe you could try to be more accepting of your husband..."

    player_name "... And give your daughter some freedom to grow!"

    show player 10f
    player_name "They don't need to be suffocated by God's rules, instead show them how much you love them, like God loves everyone."

    player_name "You can't control everyone... But you can change yourself."

    show player 5f
    show helen 14
    helen "You're right... I will do what I can, {b}Father{/b}."

    show helen 15
    show player 14f
    player_name "Now, go out and show some compassion and forgiveness just as the Lord forgives you."

    show player 13f
    show helen 16
    helen "Thank you for your insight... And forgiveness..."

    show helen 15
    show player 17f
    player_name "Tidak masalah!"

    show helen 12
    helen "..."
    show player 21f
    player_name "Err... Umm... Have a blessed day."

    show player 13f
    show helen 16
    helen "What would you have me do as penance, {b}Father{/b}?"

    show helen 15
    show player 12f
    player_name "Two prayers will suffice as your Penis... Err... Penance."

    show player 22f
    show helen 12
    pause
    show helen 16
    show player 13f
    helen "Terima kasih..."

    hide helen
    hide player
    hide players robe
    with dissolve
    return

label confessional_right_empty:
    scene church_confession
    show player 43f at Position(xpos=760)
    with dissolve
    player_name "( Cool! )"

    player_name "( I've never been on this side of the confessional. )"

    show player 4f
    player_name "Hmm..."

    show player 14f
    player_name "( Looks the same as the other side, actually. )"

    player_name "( I should get out of here... )"

    hide player
    hide church_confession
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
