label harold_button_office:
    return


label harold_button_office.photo:
    hide old_harold
    hide player
    show harold
    show anon
    anon f_normal "I found this photo."
    show anon f_looking_down a_backpack with dissolve
    harold f_normal @ -m_talk "Hmm?"
    anon f_normal a_box_attic_photo "It was hidden in that box of evidence you guys returned to us."
    show anon a_idle
    show harold a_attic_box_photo f_surprised_down
    with dissolve
    pause
    harold f_normal_closed "You're kidding me..."
    anon "Nope."
    harold f_concerned "{i}*Sigh*{/i} How did the techs miss this?!"
    harold a_idle "I'll take it back down there right away."
    harold "Thanks for bringing it to my attention."
    anon f_surprised "Wait, that's it?"
    harold @ f_suspicious "What do you mean?"
    anon "I just brought you evidence of {b}Mayor Rump{/b}'s involvement with Russian mob activities!"
    harold f_normal "Ehh, it's really not much to go on, kid."
    anon f_angry a_frustrated "Are you kidding me?"
    anon "That guy on the right is the Russian mob boss!"
    harold @ f_suspicious "How do you know that?"
    anon a_sides "It doesn't matter how I know it, I just do!"
    anon "Now are you gonna do something with this or not?!"
    harold a_hips "Whoa, kid... Calm down."
    harold "Even if you're right, and this is the man in charge of this illegal organization... A single picture with him and the mayor isn't enough to go on."
    harold "I can't just go accusing a respected politician like {b}Ronald Rump{/b} without some damn good evidence."
    anon "This is a joke."
    anon "{b}Tony{/b} was right, this police force is useless."
    harold "{b}Tony{/b} who?"
    anon @ f_surprised "Never mind."
    anon a_idle "Good day, detective."
    hide anon with dissolve
    harold f_concerned "Well, hold on a second..."
    pause
    harold "{b}[firstname]{/b}?!"
    pause
    harold f_normal_closed a_sides "{i}*Sigh*{/i}"

    $ player.go_to(L_police_front)
    scene expression player.location.background_blur with fade
    show anon f_angry with dissolve
    anon @ -m_talk "( What a complete waste of time! )"
    pause
    anon @ -m_talk "( And now I lost the picture of {b}Rump{/b} and the mob boss! )"
    anon @ f_hurt -m_talk "( Grr! )"
    anon @ -m_talk "( At least I still have the key to the lockbox.)"
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
