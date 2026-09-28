label melonia_button_garden:
    return


label melonia_button_garden.intro0:
    show anon f_worried with dissolve
    anon "Excuse me, {b}Mrs. Rump{/b}?"
    melonia f_annoyed "Are you finished cleaning the hot tub?"
    anon "No, ma'am."
    melonia @ f_eyeroll "Ugh, then what do you want?"
    return


label melonia_button_garden.intro1:
    show anon f_worried with dissolve
    melonia "Are you finished cleaning the hot tub?"
    anon "No, ma'am."
    show melonia f_annoyed
    pause
    melonia "You know, {b}Hector{/b}..."
    melonia "Just because I'm paying you for sex now, doesn't mean you can shirk your other responisibilities."
    show anon f_unimpressed
    pause
    anon "I thought we were finished with all that \"Hector\" nonsense?"
    melonia f_smirk "Heh, keep this hot tub clean and I'll call you whatever you want."
    return


label melonia_button_garden.outro0:
    jump melonia_button_common.outro0


label melonia_button_garden.outro1:
    jump melonia_button_common.outro1


label melonia_button_garden.suggest:
    anon f_flirt "Want to have sex?"
    melonia f_smirk "Mmm, you read my mind."
    melonia "Let's head up to my bedroom."
    show layer master:
        ease 1.6 xpos 485
    with None
    show melonia b_swimsuit_pulling_anon:
        flip
        xoffset -960
    show anon b_empty f_flirt o_melonia_pulling:
        flip
        xoffset -530
    with dissolve
    anon "Yes, ma'am."

    scene location_rump_bedroom_bed_closeup
    show melonia f_smirk b_swimsuit_hatless
    show anon f_flirt
    with fade
    melonia "I'm so glad my husband hired you!"
    show anon f_flirt_low
    show melonia f_smirk_down a_remove_shall1
    with dissolve
    pause
    show melonia a_remove_shall2 with dissolve
    pause
    show melonia a_remove_shall3 with dissolve
    pause
    show melonia a_remove1 f_smirk_down with dissolve
    pause
    show melonia b_swimsuit_remove2 with dissolve
    pause
    show melonia b_swimsuit_remove3 with dissolve
    show melonia b_swimsuit_remove4 with dissolve
    pause
    show melonia b_swimsuit_bottom a_idle with dissolve
    pause
    show melonia b_swimsuit_bottom a_remove_bottom1 with dissolve
    pause
    show melonia b_swimsuit_bottom_remove2 with dissolve
    pause
    show melonia b_naked_sexy f_smirk with dissolve
    pause
    jump melonia_button_bedroom.sex
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
