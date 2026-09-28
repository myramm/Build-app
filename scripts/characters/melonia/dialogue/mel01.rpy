label mel01_init_melonia:
    show melonia f_disgusted_down:
        flip
        xoffset 350
    show anon f_worried with dissolve:
        xoffset -100
    melonia "Eugh, this hot tub is disgusting!"
    melonia "What in the hell has that new pool boy been doing?!"
    show melonia f_annoyed with dissolve:
        unflip
        xoffset -250
    pause
    melonia "There you are!"
    anon "Ehh."
    melonia @ a_point_back "Care to explain why my hot tub hasn't been cleaned yet?!"
    anon a_behind_head "I umm-"
    melonia f_confused "And where's your uniform?!"
    anon "Ehh."
    anon "Is the uniform really necessary, ma'am?"
    melonia f_annoyed "Of course it's necessary!"
    anon a_sides "I'm kind of uncomfortable-"
    melonia "Don't question me, {b}Hector{/b}!"
    melonia "You will go and speak with {b}Ricky{/b} about it the second you're finished cleaning!"
    anon "What if, instead-"
    melonia a_crossed @ f_yell "Not one more word, {b}Hector{/b}!"
    anon f_sad_down @ -m_talk "..."
    melonia a_point_back "I want this hot tub scrubbed and filtered right this instant!"
    melonia a_point_down "And tomorrow morning, you WILL be here on time and in the proper uniform..."
    melonia a_idle "... Is there an understanding between us?!"
    anon "{i}*Sigh*{/i} Y-yes, ma'am."
    show melonia a_crossed with dissolve
    pause
    melonia "I realize it's your first day but nevertheless, I expected better from you, {b}Hector{/b}."
    anon @ -m_talk "..."
    show anon f_surprised
    melonia "Now get it done!"
    hide melonia
    show anon:
        flip
        xoffset -600
    with dissolve
    pause
    anon f_worried @ -m_talk "( Well that wasn't a very auspicious start. )"
    pause
    show anon f_worried_low with dissolve:
        unflip
        xoffset 200
    anon @ -m_talk "( I have no idea how to clean a hot tub... )"
    anon @ -m_talk "( ... I should {b}speak with Ricky{/b} and see if he can lend me a hand. )"
    hide anon with dissolve
    return


label mel01_more_melonia:
    scene expression background(768, 368, 4.) as stage
    show location_rump_backyard_jacuzzi_overlay as hottubback:
        yoffset 140
    show melonia b_jacuzzi:
        yoffset 155
    show location_rump_backyard_jacuzzi_overlay as hottub:
        yoffset 155
    show anon f_worried_low with dissolve
    melonia "{b}Hector{/b}?"
    melonia f_annoyed "What are you still doing here?"
    anon "Just checking to see if you need anything."
    melonia "I'm fine."
    melonia f_normal "{b}Ricky{/b} is attending to my needs."
    anon "R-right, okay."
    melonia f_annoyed "Head home for the day, I'm done with you."
    anon f_sad_down a_sides "Of course, ma'am."
    melonia "And make sure this hot tub stays clean!"
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
