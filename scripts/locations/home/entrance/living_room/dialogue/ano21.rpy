label ano21_news_home_lounge:
    $ renpy.dynamic(diane=M_diane.where in (L_home_livingroom, L_home_mombedroom))

    scene location_home_livingroom_couch08
    show location_home_livingroom_couch08b as couch
    show jenny b_front_couch_bored f_front_cuddle_bored

    if diane:
        show diane b_front_couch_watching f_normal_forward

    show debbie b_front_couch_watching f_normal_forward
    show anon b_front_behind_couch f_front_happy_low behind couch with dissolve
    anon "What's going on in here?"

    debbie @ -m_talk "Hmm?"

    debbie f_normal "Oh, we're just watching the news sweetie."

    debbie f_surprised "Did you know they arrested the mayor?"

    anon f_front_forward "Yeah, I heard."

    debbie "Human trafficking, drugs, murder..."

    debbie "... How could anyone do such awful things?"

    show debbie f_sad

    if diane:
        diane f_annoyed "Well, I for one am not surprised."

        diane "Those politicians are all scumbags."

        show diane f_normal_forward

    jenny "Can we watch something else, please?"

    debbie "Hah?!"

    debbie "No, we cannot watch something else!"

    debbie "This is big news and I wanna hear about it."

    jenny f_front_cuddle_annoyed_right "Ugh, but {i}Pretty Little Deceivers{/i} is on!"


    if diane:
        diane f_annoyed_right "You actually watch that crap?"

        jenny "It's not crap, it's awesome!"

        debbie "Please, don't start arguing, you two..."


    scene location_home_tv_night
    show tv_channel_11:
        xoffset 87
        yoffset 108
    with fade
    jon "... Several offshore accounts containing millions of dollars."

    jon "The trial which is already garnering national attention is set to take place in the coming weeks."

    jon "{b}Mr. Rump{/b} could be facing up to eighty years in prison if he's convicted."

    jenny "Sucks to be him!"


    scene location_home_livingroom_couch08
    show location_home_livingroom_couch08b as couch
    show jenny b_front_couch_bored f_front_cuddle_bored

    if diane:
        show diane b_front_couch_watching f_normal_forward

    show debbie b_front_couch_watching f_normal_forward
    show anon b_front_behind_couch f_front_forward behind couch
    with fade
    anon "I'm pretty sure he deserves it."

    debbie "I wonder how his poor family is taking this?"

    jenny "Siapa yang peduli?"

    debbie f_sad "It wouldn't hurt you to show a little bit of empathy, you know?"


    if diane:
        diane f_smirk "Are you sure about that?"

        diane "She might burst into flames."

        show diane f_smirk_right
        jenny @ f_front_cuddle_annoyed_right "Ha, ha, very funny..."


    debbie "What if it was me getting sent away to prison for life, how would you feel then?"


    if diane:
        show diane f_normal

    jenny "Umm, fine because that's a ridiculous question."

    jenny "Pretty sure you've never done a single illegal thing in your entire life!"

    debbie "Pfft, I have too!"

    jenny "Ya, terserah."


    if diane:
        diane f_normal_forward @ f_annoyed "Jaywalking doesn't count, {b}[deb_name]{/b}..."


    anon f_front_tired_forward "I think I'm gonna head up to bed."

    debbie "Sudah?"

    anon f_front_tired_low "Yeah, I'm really tired."

    debbie "But you haven't had dinner, sweetie..."

    anon "Tidak apa-apa."

    anon "I'll just have a big breakfast tomorrow or something."

    debbie "Apa kamu yakin?"

    debbie f_normal "I can fix you something, really, I don't mind."


    if diane:
        diane f_annoyed "Just let the kid get some sleep, {b}[deb_name]{/b}..."

        show debbie f_sad
    else:
        anon "I'm sure, thanks."


    anon "Selamat malam."


    if diane:
        diane f_smirk_right_up "Good night, stud."


    debbie f_normal "Sweet dreams, sweetie."

    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
