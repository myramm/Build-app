label scene_sara_terry:
    scene location_beach_tower_sex
    show location_beach_tower_sex_overlay as bench
    call scene_sara_terry.animation
    terry "Oh, you heavenly harpy!"
    anon "( !!! )"
    terry "Calypso 'erself would be envious of yer charms."
    sara "Mhmm!"
    anon "( {b}C-captain Terry{/b}??? )"
    pause
    terry "Tossin' like the sea in a storm!"
    sara "Jibe ho, my love!"
    terry "Rack the starboard oars..."
    $ M_sara.set('sex speed', 1. / 14)
    terry "... Hard to port!"
    pause
    anon "( What the heck- )"
    terry "She's about to blow!"
    sara "Bring her into port, captain!"
    $ M_sara.set('sex speed', 1. / 16)
    terry "Oh, she's cummin'!"
    pause
    terry "Load the guns!"
    anon "( I'm really happy for them but this is some super weird sex talk... )"
    anon "( ... Let me just grab this and... )"

    scene location_beach_tower_floor
    with fade
    terry "OOOHHH, I'M CLUB HAULIN'!!!"
    anon "( ... Oh kay, it's definitely time to go!! )"
    return


label scene_sara_terry.animation:
    $ M_sara.set('sex speed', 1. / 12)
    show sara_sex_terry behind bench
    with fade
    return


label scene_sara_terry.replay:
    jump scene_sara_terry
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
