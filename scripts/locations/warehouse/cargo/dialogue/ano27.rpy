label ano27_jabb_warehouse_cargo:
    scene location_warehouse_sewers_cutscene_03
    show text _ ("After a few minutes of relieved celebration...") as caption
    with fade
    pause
    hide caption with dissolve
    show text _ ("... Or traumatized crying, if you wanna be a dick about it.") as caption with dissolve
    pause
    hide caption with dissolve
    show text _ ("I was finally ready to soldier on and began my ascent into the warehouse proper.") as caption with dissolve
    pause

    scene location_warehouse_sewers_cutscene_04
    show text _ ("I breathed a sigh of relief at finding {b}Nadya{/b}'s intel to be accurate.") as caption
    with fade
    pause
    hide caption with dissolve
    show text _ ("The next step was finding a way to get {b}Harold{/b} and {b}Tony{/b} inside the building.") as caption with dissolve
    pause
    hide caption with dissolve
    show text _ ("Hopefully her henchman {b}Jab{/b} would know the best way to proceed.") as caption with dissolve
    pause

    scene expression background() with fade
    show anon f_disgusted o_sewage with dissolve:
        flip
    anon @ -m_talk "( There is nothing that could ever make me want to go back down there! )"
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
