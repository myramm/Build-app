label combat(variant, transition=fade, **kwargs):
    python hide:
        config.skipping = None
        renpy.dynamic(_skipping=False)

    if renpy.has_image('combat_{}_splash'.format(variant)):
        python hide:
            if isinstance(transition, (list, tuple)):
                level = kwargs.get('level', 1)
                skill = kwargs.get('skill', 0)
                renpy.dynamic(transition=transition[level <= skill])

        scene combat_splash with transition
        show combat_versus
        pause

    if game.cheat_mode:
        menu:
            "Play":
                pass
            "Cheat":
                return True

    python hide:
        renpy.dynamic(_rollback=False, quick_menu=False)
        rv = renpy.roll_forward_info()

        if rv is None or not renpy.game.after_rollback:
            rv = renpy.call_in_new_context('combat.interact', **kwargs)

        renpy.checkpoint(rv)
        store._return = rv

    return _return


label combat.interact(gui=True, hint='master', level=1, limit=math.inf, skill=0):
    python hide:
        from store.combat import Entity

        atk_hp = len(renpy.get_available_image_attributes(
            'combat_{}_atk'.format(variant)))
        def_hp = len(renpy.get_available_image_attributes(
            'combat_{}_def'.format(variant)))

        renpy.dynamic(anon=Entity(def_hp, hue=48),
                      enemy=Entity(min(atk_hp, limit)))

    scene combat_scene
    show screen minigame_combat_hint(_layer=hint)
    show combat_idle as fight

    if gui:
        show screen minigame_combat(enemy, anon, flip=gui == flip)

    python:
        with suppress(Exception):
            gui = renpy.game.context().dynamic_stack[-1]['gui']

    with fade
    pause .3

    while anon.hp and enemy.hp:
        if anon.hp < anon.max or enemy.hp < enemy.max:
            show combat_idle as fight with dissolve

        show screen qte(level, enemy.dmg, skill=skill) with dissolve
        call screen empty()
        hide screen qte

        if not _return:
            $ anon.hit()
            show combat_def as fight
        else:
            $ enemy.hit()
            show combat_atk as fight

        with fastdissolve
        pause 1

    return enemy.hp == 0


image combat_dimitri_vs_left = 'combat_dexter_vs_left'

image combat_atk = 'combat_[variant]_atk [enemy.dmg]'
image combat_def = 'combat_[variant]_def [anon.dmg]'
image combat_idle = 'combat_[variant]_idle'
image combat_scene = 'combat_[variant]_scene'

image combat_versus:
    contains:
        align (.5, 1.)
        .6
        'combat_vs'
    contains:
        '#fffa'
        alpha 0
        .5
        linear .1 alpha 1
        linear .1 alpha 0
    contains:
        'combat_{}_vs_left'.format(variant)
        xpos -1.
        yalign 1.
        easein_quart .6 xpos 0.
    contains:
        'combat_{}_vs_right'.format(variant)
        xanchor 1.
        xpos 2.
        yalign 1.
        easein_quart .6 xpos 1.
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
