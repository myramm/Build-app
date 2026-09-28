label comic_store_bought_cyclone_mask:
    scene expression player.location.background_blur
    show player 736 with dissolve
    player_name "( Yeah, this should work great for {b}[jen_name]'s camshows{/b}. )"
    player_name "( I should {b}meet her in her room{/b} and see what she thinks. )"
    hide player with dissolve
    return

label comic_store_june_cosplay_started:
    scene expression player.location.background_blur
    show player 14 with dissolve
    player_name "Looks like they have some costumes hanging on the wall."
    player_name "I should have a look at them..."
    player_name "... Maybe they have those orc cosplay pieces."
    hide player with dissolve
    return

label comic_store_erik_vr_needed:
    scene expression player.location.background_blur
    show player 35 with dissolve
    player_name "( They must have the things {b}Erik{/b} wanted in here somewhere. )"
    show player 12 with dissolve
    player_name "( Maybe in those shelves by the counter? )"
    hide player with dissolve
    return

label comic_store_first_visit:
    scene expression player.location.background_blur
    show lily f_laugh
    show player 1 at left with dissolve
    lily "Hi!"
    show lily f_normal
    lily "First time visiting Cosmic Cumics?"
    show player 29
    player_name "Umm... Yeah! I didn't know this place existed..."
    show player 1
    lily "Yeah, we just opened recently!"
    show player 2
    player_name "Oh, cool!"
    player_name "You guys sell video games, too?"
    show lily f_laugh
    show player 1
    lily "Of course."
    show lily f_normal
    lily "We sell a variety of products ranging from video games, comic books, figurines, posters and collectibles!"
    show player 2
    player_name "Oh. So... Nerd stuff..."
    show lily f_laugh
    show player 1
    lily "Yup!"
    lily "Have a look around, and let me know if you need help with anything!"
    hide lily
    hide player
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
