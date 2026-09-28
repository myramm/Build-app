label popup_test:
    call popup ('alpha')

    call popup ('sleep')

    call popup ('map')

    $ pt_items = items.keys()
    while pt_items:
        call popup ('give', Item(pt_items.pop(0)))

    $ pt_locs = list(v for k, v in store.__dict__.items() if k.startswith('L_') and v not in (L_home_bedroom, L_diane_barn_building))
    while pt_locs:
        $ pt_loc = pt_locs.pop(0)
        if L_map in pt_loc.parents:
            call popup ('location', pt_loc)

    $ pt_areas = [L_home_attic, L_pool_medicroom, L_erikhouse_mrsjroom, L_home_mombedroom]
    while pt_areas:
        call popup ('area', pt_areas.pop(0))

    $ pt_stats = ['chr', 'dex', 'int', 'str']
    while pt_stats:
        $ pt_stat = pt_stats.pop(0)
        call popup (pt_stat, False)
        call popup (pt_stat, True)

    $ pt_minis = popup.minigame.data.keys()
    while pt_minis:
        $ pt_mini = pt_minis.pop(0)
        call popup ('minigame', pt_mini)

    $ pt_features = popup.feature.data.keys()
    while pt_features:
        $ pt_feature = pt_features.pop(0)
        call popup ('feature', pt_feature)

    $ pt_scenes = popup.scene.data.keys()
    while pt_scenes:
        $ pt_scene = pt_scenes.pop(0)
        call popup ('scene', pt_scene)

    call popup ('bugs', False)
    call popup ('bugs', True)

    call popup ('computer', False)
    call popup ('computer', True)

    call popup ('cat')
    call popup ('larry')
    call popup ('valve')

    call popup ('earn', 550)
    call popup ('poor')

    "fin"

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
