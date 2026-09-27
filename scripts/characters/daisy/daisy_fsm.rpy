init -1 python:
    M_daisy = Machine(
        'daisy',
        default_loc=[[L_NULL, L_NULL, L_NULL, L_NULL]],
        vars={
            'sex speed': .3,
            'veggie pizza': False,
            'change angle': False,
            'daisy_breed_first_time': True},
        default_outfit="naked",
        home_birth=True,
        default_pregnancy_schedule={
            '':                LocationSchedule(L_diane_barn_interior),
            '_pregnant_bump':  LocationSchedule(L_diane_barn_interior),
            '_pregnant_belly': LocationSchedule(L_diane_barn_interior),
            '_baby_twins':     LocationSchedule(L_diane_barn_interior),
            '_baby_girl':      LocationSchedule(L_diane_barn_interior),
            '_baby_boy':       LocationSchedule(L_diane_barn_interior),
            '_labor':          LocationSchedule(L_diane_barn_interior)})

init -3 python:
    T_daisy_intro = Trigger()
    T_daisy_view_statue = Trigger()
    T_daisy_awaken_statue = Trigger()
    T_daisy_checked_on_cow = Trigger()

    T_daisy_named_herself = Trigger()

    T_daisy_find_food = Trigger()
    T_daisy_eaten_pizza = Trigger()

    T_daisy_flower_bad_news = Trigger()
    T_daisy_gave_new_flowers = Trigger()
    T_daisy_milked = Trigger()

    T_daisy_caught_breeding = Trigger()
    T_daisy_end = Trigger()
    T_daisy_sex = Trigger()

init python:

    S_daisy_start = State()
    S_daisy_assembled_statue = State()
    S_daisy_viewed_statue = State()
    S_daisy_awakened_statue = State()

    S_daisy_picking_flowers = State(delay=3)

    S_daisy_pizza_craving = State(delay=2)
    S_daisy_get_pizza = State()

    S_daisy_dead_flowers = State(delay=2)
    S_daisy_get_new_flowers = State()
    S_daisy_need_milking = State()

    S_daisy_diane_breeding = State(delay=1)
    S_daisy_caught_breeding = State()
    S_daisy_caught_breeding_aftermath = State()

    S_daisy_end = State()
    S_daisy_sex = State()


    S_daisy_start.add(T_daisy_intro, S_daisy_assembled_statue, actions=["setdefaultoutfit", "naked"])
    S_daisy_assembled_statue.add(T_daisy_view_statue, S_daisy_viewed_statue)
    S_daisy_viewed_statue.add(T_daisy_awaken_statue, S_daisy_awakened_statue,
                                actions=["setdefaultloc", [[L_diane_barn_interior, L_diane_barn_interior, L_diane_barn_interior, L_diane_barn_interior]],
                                ]
                             )
    S_daisy_awakened_statue.add(T_daisy_checked_on_cow, S_daisy_picking_flowers)

    S_daisy_picking_flowers.add(T_daisy_named_herself, S_daisy_pizza_craving)
    S_daisy_pizza_craving.add(T_daisy_find_food, S_daisy_get_pizza, actions=["unlocklocation", L_pizzeria_exterior])
    S_daisy_get_pizza.add(T_daisy_eaten_pizza, S_daisy_dead_flowers, actions=["set", "veggie pizza"])

    S_daisy_dead_flowers.add(T_daisy_flower_bad_news, S_daisy_get_new_flowers)
    S_daisy_get_new_flowers.add(T_daisy_gave_new_flowers, S_daisy_need_milking)
    S_daisy_need_milking.add(T_daisy_milked, S_daisy_diane_breeding)

    S_daisy_diane_breeding.add(T_daisy_caught_breeding, S_daisy_caught_breeding)
    S_daisy_caught_breeding.add(T_all_sleep, S_daisy_caught_breeding_aftermath)
    S_daisy_caught_breeding_aftermath.add(T_daisy_end, S_daisy_end, actions=(
        'exec', A_more_girl_than_cow.unlock))
    S_daisy_end.add(T_daisy_sex, S_daisy_sex, actions=(
        'clear', ('player', 'is_virgin'),
        'setdefaultloc', [[L_diane_barn_interior, L_diane_barn,
                           L_diane_barn_interior, L_diane_barn_interior]]))

    M_daisy.add(S_daisy_start, S_daisy_assembled_statue, S_daisy_viewed_statue,
               S_daisy_awakened_statue, S_daisy_picking_flowers, S_daisy_get_pizza,
               S_daisy_pizza_craving, S_daisy_dead_flowers, S_daisy_get_new_flowers,
               S_daisy_need_milking, S_daisy_diane_breeding, S_daisy_caught_breeding,
               S_daisy_caught_breeding_aftermath, S_daisy_end, S_daisy_sex)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
