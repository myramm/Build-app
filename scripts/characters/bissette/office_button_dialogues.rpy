label bissette_dialogue_office_bissette_roxxy_exam_convince:
    show teacher 1 at right
    show player 10 at left
    with dissolve
    player_name "What was I supposed to be doing again?"
    show player 5
    show teacher 5
    bissette "As-tu oublié?"
    bissette "You must {b}convince Roxxy to show up for the exam{/b}."
    bissette "Otherwise, the grade point average of the entire class will suffer."
    show teacher 4
    show player 14
    player_name "Oh, right!"
    player_name "Don't worry, {b}Miss Bissette{/b}! I'm on it!"
    return

label bissette_dialogue_office_bissette_roxxy_convinced:
    show teacher 1 at right
    show player 10 at left
    with dissolve
    player_name "{b}Miss Bissette{/b}?"
    show player 13
    show teacher 5
    bissette "Oui?"
    show teacher 4
    show player 14
    player_name "I convinced {b}Roxxy{/b} to show up for the test!"
    show player 13
    show teacher 2
    bissette "Truly?!"
    show teacher 1
    show player 17
    player_name "Yup!"
    show teacher 25 zorder 1 with dissolve

    bissette "Tu me sauves la vie!"
    show teacher 26 with dissolve
    bissette "Whatever would I do without you?!"
    show teacher 27 with dissolve
    show player 29 with dissolve
    player_name "Heh, it's no big deal..."
    show player 13
    show teacher 16
    with dissolve
    bissette "Now be sure to study the words we learned over your past assignments, yes?"
    show teacher 17
    show player 14
    player_name "I will! Don't worry!"
    show player 13
    show teacher 16
    bissette "Très bien! Next class we will have the test."
    show teacher 17
    show player 14
    player_name "Alright, {b}Miss Bissette{/b}!"
    return

label bissette_dialogue_office_intro:
    show teacher 3 at right
    show player 13 at left
    with dissolve
    bissette "Bonjour, {b}[firstname]{/b}!"
    show teacher 1
    show player 14
    player_name "Hello, {b}Miss Bissette{/b}."
    show player 13
    show teacher 2
    bissette "What can I help with?"
    show teacher 1
    return

label bissette_dialogue_office_bissette_wine_sampling:
    player_name "I'm excited to taste that wine, {b}Miss Bissette{/b}."
    show player 13
    show teacher 12
    bissette "J'ai hâte également!"
    bissette "You will be tasting many things tonight, yes?"
    show teacher 13
    show player 29 with dissolve
    player_name "{i}*Gulp*{/i} Y-yeah..."
    show player 14
    show teacher 3
    bissette "Très bien, I'll be seeing you in my office this evening then."
    show teacher 13
    show player 14 with dissolve
    player_name "See you there!"
    return

label bissette_dialogue_office_leave:
    show player 14
    player_name "I don't think I need anything right now."
    show player 13
    show teacher 2
    bissette "Très bien!"
    show teacher 1
    show player 36 with dissolve
    player_name "Bye!"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
