init -100 python:
    def check_name():
        if store.firstname == 'PUBLICSAVE':
            try:
                renpy.run(ShowMenu('name'))
            except renpy.game.JumpException as e:
                store.firstname = persistent.firstname
                unlock_all_scenes()

    config.after_load_callbacks += [check_name]


label game_main:
    $ player.location.hide_screen()
    $ player.location.call()
    $ game.main()

label splashscreen:
    if not config.developer:
        show splash_logo
        with dissolve
        pause 1
        hide splash_logo
        with dissolve

        show screen splash
        with dissolve
        $ ui.interact()
        hide screen splash
        with dissolve

    if config.rollback_enabled and not persistent.rollback_warned:
        $ renpy.call_in_new_context('warn.rollback')
        $ persistent.rollback_warned = True
    else:
        $ persistent.rollback_warned = config.rollback_enabled

    return

label main_menu:
    call screen main_menu()
    return

label game_menu:
    if renpy.has_screen(_game_menu_screen):
        $ renpy.call_screen(_game_menu_screen, *args, **kwargs)
        jump _noisy_return
    jump expression _game_menu_screen

label after_load:
    if not hasattr(store, 'game'):
        return

    $ config.mouse = None
    $ renpy.dynamic(sav=util.version(savegame_version))

    call INIT_INVENTORY_ITEMS
    call INIT_GAME

    python hide:
        if sav < app.version:
            lib = triggers.copy()
            
            if sav < (0, 20, 5):
                
                lib.update({'T_ano11_wait': T_ano11_done,
                            'T_ano11_tony': T_ano12_init,
                            'T_ano11_zoom': T_ano12_zoom})
            
            if sav < (0, 20, 8):
                
                lib.update({'T_jos01_rump': T_jos01_spot})
                
                fsm_data.machine_triggers = [
                    (m, lib[str(t)]) for m, t in fsm_data.machine_triggers
                    if str(t) in lib]
            
            fsm_data.machine_triggers = [
                (m, lib[t._name]) for m, t in fsm_data.machine_triggers
                if t._name in lib]

    $ orphaned_states()
    $ load_fsm_data()

    python:
        Machine.machine_trigger(T_all_on_load)
    python:
        logger.info("Game Unpacked : {} // CWD : {}".format(is_game_unpacked(), os.getcwd()))
        if config.developer:
            locations_label_check()
            locations_background_names_check()
            machines_label_check()
        logger.info("RETURN STACK INFO")
        logger.info(repr(renpy.get_return_stack()))


    python hide:
        if sav < (0, 19, 5):
            try:
                del store.dating_systems
                del store.outfit_managers
                del store.pregnancy_managers
                del store.temp_pms
            except:
                pass
            
            
            if M_june.is_state(S_june_cosplay_ready):
                if player.has_item('orcette_cosplay'):
                    M_june.trigger(T_june_cosplay_bought)
            
            
            interval = (S_roxxy_trailer_park_trouble, S_roxxy_shut_down_lab)
            if M_roxxy.between_states(*interval):
                M_roxxy.set('trailer foreclosed', True)
            
            
            dom = M_diane.outfit
            setdefault = dom.set_default_outfit_schedule
            setdefault([['dressed'] * 4])
            if M_diane.finished_state(S_diane_d9_intro):
                setdefault([['shirtless'] * 4])
            if M_diane.finished_state(S_diane_couch_crashing):
                setdefault([['shirtless'] * 2 + ['nightgown'] * 2])
            if M_diane.finished_state(S_diane_milk_production_increase):
                setdefault([['cow'] * 2 + ['nightgown'] * 2])
            dom.bind_outfit_to_location(L_home_livingroom, 'nightgown')
            dom.bind_outfit_to_location(L_diane_shed, 'shirtless')
            
            
            L_rump_lobby.lock()
            
            
            if L_hospital_floor3.locked:
                L_hospital_floor3.unlock()
                L_hospital_basement.lock()

        if sav < (0, 20, 0):
            
            L_bank.lock()
            L_bank_lobby.unvisit()
            L_dealership.lock()
            L_dealership.unvisit()
            L_dealership_showroom.unvisit()
            L_pizzeria_exterior.lock()
            L_pizzeria_exterior.unvisit()
            L_warehouse.lock()
            L_warehouse.unvisit()
            
            
            player.transport_level = 1 if player.transport_level else 0
            
            
            if M_debbie.finished_state(S_debbie_overheard):
                take = ('breeding_guide',
                        'milk_2x2z1y',
                        'milk_2x3z1y',
                        'milk_9x9z2y',
                        'milk_sample',
                        'mysterious_statue_1',
                        'package',
                        'pump',
                        'veggie_pizza',
                        'water_glass')
                
                for item in take:
                    player.inventory.remove_item(item)
                    player.inventory.remove_picked_up(item)
                
                if M_daisy.finished_state(S_daisy_start):
                    player.inventory.get_item('mysterious_statue_2')
                    player.inventory.get_item('mysterious_statue_3')
                
                M_daisy.reset()
                M_debbie.reset()
                M_diane.reset()
                
                game.skip_first_day()

        if sav < (0, 20, 1):
            
            if not M_anon.finished_state(S_ano02_thug) \
                and player.has_picked_up_item('beach_house_key'):
                player.inventory.remove_item('beach_house_key')
                player.inventory.remove_picked_up('beach_house_key')
                player.inventory.money += 5000

        if sav < (0, 20, 5):
            
            if (M_anon.is_state(S_ano12_dark) or game.timer.is_dow(6)) \
                and player.location in L_pizzeria_exterior.get_all_children():
                player.go_to(L_pizzeria_exterior)
            
            
            if M_jenny.pregnancy.is_pregnant and not (M_jenny.fertile and
                                                      M_anon.finished_state(S_ano02_thug)):
                M_jenny.pregnancy.abort_baby()
            
            
            M_tina.pregnancy.abort_baby()
            M_tina.outfit.is_naked = False
            
            
            L_boat_bridge.lock()
            L_boat_bridge.unvisit()
            L_rump_front.lock()
            L_rump_front.unvisit()
            L_rump_lobby.lock()
            L_rump_lobby.unvisit()
            L_rump_office.lock()
            L_rump_office.unvisit()
            
            
            L_bank_hallway.lock()
            L_bank_hallway.unvisit()
            
            
            L_liu_lounge.lock()
            L_maria_lounge.lock()
            
            
            if not M_anon.finished_state(S_ano10_init):
                L_tina_lounge.lock()
                L_tina_lounge.unvisit()
            
            
            if player.has_picked_up_item('thotbot'):
                player.inventory.remove_item('thotbot')
                player.inventory.remove_picked_up('thotbot')
                player.inventory.money += 1000
            
            
            M_consuela.reset()
            M_thotbot.reset()
            
            
            try:
                crush = fsm_data.machine_triggers.index(('roxxy', T_roxxy_get_oil))
                learn = fsm_data.machine_triggers.index(('anon', T_ano10_tina))
                M_tina.set('becca_crush', crush < learn)
            except ValueError:
                pass
            
            
            ts = M_jenny.get('jenXX_lite_ivy')
            if isinstance(ts, tuple):
                M_jenny.set('jenXX_lite_ivy', ts[0] * 4 + ts[1])
            
            
            work = 'apron' if 3 <= M_maria.pregnancy.stage < 5 else 'dressed'
            M_maria.outfit.set_default_outfit_schedule(
                [[work, work, 'casual', 'casual']] * 6 +
                [['casual', 'casual', 'casual', 'casual']])
            
            
            if 3 <= M_tina.pregnancy.stage < 5:
                M_tina.outfit.set_default_outfit_schedule(
                    [['dressed', 'dressed', 'naked', 'naked'],
                     ['naked'] * 4])
            elif 5 <= M_tina.pregnancy.stage:
                M_tina.outfit.set_default_outfit_schedule('casual')
            else:
                M_tina.outfit.set_default_outfit_schedule(
                    [['dressed', 'dressed', 'casual', 'casual'],
                     ['casual'] * 4])
            
            
            if M_anon.finished_state(S_ano10_tina):
                Machine.trigger(T_ano10_tina, from_load=M_tina, force_save=True)
                Machine.trigger(T_all_sleep, from_load=M_tina, force_save=True)

        if sav < (0, 20, 6):
            
            if not M_consuela.finished_state(S_con04_hint):
                M_consuela.outfit.is_naked = False
                M_consuela.outfit.set_default_outfit_schedule(
                    [['dressed', 'dressed', 'hospital', 'hospital']])
            
            
            if M_jenny.finished_state(S_jenny_diary_clue):
                M_jenny.set('fertile', True)
            
            
            if not hasattr(game.timer, '_seed'):
                game.timer._seed = random.random()
            
            
            codex = ((S_roxxy_fight_dexter,                4),
                     (S_roxxy_picnic_done,                 3),
                     (S_roxxy_return_to_school,            2),
                     (S_roxxy_dexter_confront,             1))
            
            care = next((c for s, c in codex if M_roxxy.finished_state(s)), 0)
            M_roxxy.set('roxxy relationship', care)
            
            
            codex = ((S_jenny_diary_clue,                 31),
                     (S_jenny_hallway_talk,               30),
                     (S_jenny_end,                        29),
                     (S_jenny_movie_date,                 28),
                     (S_jenny_want_some_breakfast,        27),
                     (S_jenny_cheerleader_sex,            26),
                     (S_jenny_bedroom_intrusion,          25),
                     (S_jenny_give_cunni,                 23),
                     (S_jenny_start_camshow_blowjob,      22),
                     (S_jenny_catch_her_jilling,          21),
                     (S_jenny_pissed_at_handjob,          20),
                     (S_jenny_start_camshow_handjob,      19),
                     (S_jenny_spy_on_mia_telescope,       18),
                     (S_jenny_caught_talking_to_camslut,  17),
                     (S_jenny_talked_to_cedric,           16),
                     (S_jenny_deliver_bad_monster,        15),
                     (S_jenny_new_video_notice,           14),
                     (S_jenny_helping_with_breakfast,     13),
                     (S_jenny_bring_toy_back,             12),
                     (S_jenny_get_a_toy,                  11),
                     (S_jenny_go_to_her_room,              9),
                     (S_jenny_caught_snooping,             8),
                     (S_jenny_sluttygram_pics,             7),
                     (S_jenny_hallway_eavesdropping,       6),
                     (S_jenny_debbie_altercation,          3))
            
            page = next((p for s, p in codex if M_jenny.finished_state(s)), 2)
            M_jenny.set('diary_progress', page)
            
            remap = ((1, 'jenny_debbie_acknowlegement', 'diary_extra_debbie'),
                     (2, 'jenny_pregnant_page',         'diary_extra_pregnant'),
                     (3, 'jenny_kid_page',              'diary_extra_baby'))
            
            for i, old, new in remap:
                val = M_jenny._vars.pop(old, None)
                if val:
                    M_jenny.set(new, (min(M_jenny.diary_progress, val + 1), i))
            
            fsm_data.update_vars(M_jenny)

        if sav < (0, 20, 8):
            
            if M_odette.is_state(S_ode00_init) and not M_grace.sex_1st_time:
                Machine.trigger(T_ode00_init, from_load=M_odette, force_save=True)
                Machine.trigger(T_all_sleep, from_load=M_odette, force_save=True)
            
            
            if M_anon.finished_state(S_ano21_init):
                expiry = (14 - M_melonia.pregnancy.days_elapsed) * 4 - game.timer._tod
                if expiry:
                    M_rump.move(L_police_basement, expiry)

        if sav < (0, 20, 10):
            
            if M_anon.finished_state(S_ano10_tina):
                Machine.trigger(T_ano10_tina, from_load=M_becca, force_save=True)
            if M_becca.get('becca beach sex'):
                Machine.trigger(T_bec00_solo, from_load=M_becca, force_save=True)
            if M_becca.is_state(S_bec00_done):
                Machine.trigger(T_all_sleep, from_load=M_becca, force_save=True)
            
            
            if M_becca.get('becca beach sex'):
                M_becca.set('taken_dick', True)
            if M_missy.get('missy beach sex'):
                M_missy.set('taken_dick', True)
            
            
            M_eve.set_can_talk_flags([True] * 4)
            
            
            if M_jenny.finished_state(S_jenny_movie_date):
                unlock_scene('Jenny', '18_unlocked')

        if sav < (0, 20, 11):
            
            if M_jenny.pregnancy.number_of_babies > 0 or M_jenny.pregnancy.stage > 2:
                if M_jenny.is_state(S_jenny_necklace_rebutal):
                    Machine.trigger(T_jen0m_hook, from_load=M_jenny, force_save=True)

        if sav < (0, 20, 12):
            
            if machines['maria'] is not M_maria:
                store.savegame_version = '0.20.11'
                renpy.save('0-20-12-maria-sync')
                renpy.load('0-20-12-maria-sync')
                return
            
            
            if M_tony.watches:
                M_tony.set('watches', 'plus')

        if sav < (0, 20, 14):
            
            if not M_daisy.get('daisy_breed_first_time'):
                M_daisy.trigger(T_daisy_sex)

        if sav < (0, 20, 15):
            
            if M_nadya.finished_state(S_nad01_lewd):
                Machine.trigger(T_nad01_lewd, from_load=M_katya, force_save=True)
                Machine.trigger(T_nad01_lewd, from_load=M_khadne, force_save=True)
                Machine.trigger(T_nad01_lewd, from_load=M_svetlana, force_save=True)
                S_kat00_done._delay = 0
                Machine.trigger(T_all_sleep, from_load=M_katya, force_save=True)
                Machine.trigger(T_all_sleep, from_load=M_svetlana, force_save=True)

        if sav < (0, 20, 16):
            
            if M_yoyo.get('met', None):
                Machine.trigger(T_yoy00_hook, from_load=M_yoyo, force_save=True)

        if sav < app.version:
            renpy.call_in_new_context('warn.migrate')

        store.savegame_version = config.version

        if hasattr(store, '_new_content') and _new_content:
            game.cheat_mode = False
            game.timer._seed = random.random()
            player.inventory.money = 200
            player.inventory.savings = 250000
            player.name = persistent.firstname
            player.stats._chr = 7
            player.stats._dex = 10
            player.stats._int = 9
            player.stats._str = 8
            store.cheating = False
            store.firstname = persistent.firstname
            store.location_seed = random.randint(0, sys.maxint)
            M_park_douches.set('met', True)
            renpy.call_in_new_context('recap')
            del store._new_content
            avoid = {}
            try:
                check = (
                    
                    ('iwanka', (2,)),
                    ('liu', (1,)),
                    ('melonia', (1,)),
                    ('Odette', (3,)),
                    ('tina', (1,)),
                    ('yoyo', (1,)))
                for k, s in check:
                    c = persistent.cookie_jar[k]['gallery']
                    v = persistent.cookie_jar[k].get('variants', {})
                    for n in s:
                        key = '{:02}_unlocked'.format(n)
                        avoid[(k, key)] = (c[key], v.get(key, None))
                
                
                unlock = (('iwanka', 2), ('liu', 1), ('melonia', 1), ('tina', 1))
                for k, s in unlock:
                    key = '{:02}_unlocked'.format(s)
                    avoid[(k, key)][1].add('first')
            except:
                pass
            
            unlock_all_scenes()
            
            for (c, k), (g, v) in avoid.items():
                chr = persistent.cookie_jar[c]
                chr['gallery'][k] = g or bool(v)
                if v is not None:
                    chr['variants'][k] = v
                chr['unlocked'] = any(chr['gallery'].values())
            
            if not persistent.eve_bulge_unlocked:
                for v in persistent.cookie_jar['Eve']['variants'].values():
                    if len(v) > 1:
                        v.discard('trans')

    return

define config.load_failed_label = 'after_failed_load'

label after_failed_load:
    $ logger.warning('Load operation failed!')

    if hasattr(store, 'player'):
        $ logger.info('Attempting save recovery...')
        call _after_load
        $ renpy.run(MoveTo(player.location))

    $ logger.error('Unable to recover save, exiting to main menu.')
    scene black
    call popup ('Error loading save')
    $ renpy.run(MainMenu())
    return

label start_clean:
    $ cheating = False
    jump start

label start_cheat:
    $ cheating = True
    jump start

label start:
    $ game = Game(language)
    $ nadya_name = "???"
    $ josephine_name = "???"
    $ firstname = config.replay_scope["firstname"] = persistent.firstname
    if "jackhammer" in firstname.lower():
        $ A_the_jackhammer.unlock()
    $ player = Player(firstname)
    call INIT_GLOBAL
    $ fsm_data = FSMData()
    $ reset_machines_to_init_state()
    $ location_data = LocationData()
    python:
        for location in store.locations.values():
            if location._locked:
                location.locked = True
    $ player.go_to(L_home_bedroom)
    $ game.possibly_in_shower = [M_jenny, M_debbie]
    $ game.sleep_lock = True
    python:
        savegame_version = config.version

        movedpiece = 0
        piecelist = [[0,0],[-60,580],[830,580],[830,580],[830,580],[-60,580],
                     [830,580],[-60,580],[830,580],[-60,580],[830,580],[-60,580],
                     [830,580],[-60,580],[-60,580],[-60,580],[830,580],[830,580],
                     [-60,580],[-60,580],[830,580],[830,580],[-60,580]]
        time_count = 5

    python:
        orphaned_states()
        if cheating:
            game.cheat_mode = True
            player.get_money(999979, show_ui_message=False)
            player.stats.max_all()
        if persistent.skip_intro:
            game.skip_first_day()
            renpy.call("sleep_lock_check")
            renpy.jump("bedroom_dialogue")
    call expression game.dialog_select("intro_dialogue")
    jump bedroom_dialogue

label intro_dialogue:
    stop music fadeout 2
    scene black
    pause .5

    play music "<loop 79>audio/music_sad.ogg" loop fadein 1.0
    $ playSound("<loop 5 to 179>audio/ambience_rain1.ogg")
    scene intro_01
    show text _ ("March 3rd, on a rainy afternoon.\nMy father's funeral. I can't believe he's really gone.\nHe died from a work related accident at the age of 40. Leaving me all alone with no family to speak of...") as caption
    with dissolve
    pause

    scene black with dissolve
    pause .5

    $ playSound("<loop 3 to 94>audio/ambience_rain2.ogg", multi=True)
    scene intro_02
    show text _ ("Circumstances surrounding his death have been found {i}suspicious{/i} by the police.\nThey were at our house for an entire week, bombarding me with questions to which I had no answers.\nNo {i}conclusive{/i} evidence has been found and the knowledge that my father will get no {i}justice{/i} weighs heavily upon me.") as caption
    with dissolve
    pause

    scene intro_02b
    show text _ ("Luckily, my father's lifelong friend has taken me in and given me a room in her home.\nShe's a kind woman, with a big home, and only her daughter living there with her...") as caption
    with fade
    pause

    scene black with dissolve
    pause .5

    $ playSound("<loop 5 to 181>audio/ambience_rain3.ogg")
    scene intro_03
    show text _ ("The night of the funeral, I overheard her reminiscing about my father in the kitchen.\nShe eventually broke down and said she didn't know what to do.\nIt seems my father had gotten involved with some real bad people who were now pressuring her to cover his {b}debts{/b}.") as caption
    with dissolve
    pause

    scene black with dissolve
    pause .5

    stop music fadeout 2
    $ playSound("<loop 7 to 114>audio/ambience_suburb.ogg")
    scene intro_04
    show text _ ("Now a month later, things are finally starting to settle down.\nI've gotten used to my new living arrangement and today will be my first day back at college.\nIt'll be nice to see my friends again.") as caption
    with dissolve
    pause
    hide caption with dissolve
    show text _ ("There are {i}3 things{/i} I have to take care of before the end of the semester.\n1) - {b}I need to earn some money and help pay off my father's debts{/b}.\n2) - {b}I have to uncover the truth about my father's murder{/b}.\n3) - {b}I have to find a date for the Sorority Ball{/b}.") as caption with dissolve
    pause

    $ playSound()
    scene black with dissolve
    pause .5
    return

label new_context_screen(interface, images):
    $ player.location.call_screen(interface, images)

label new_context_manual_label(new_context_screen):
    $ renpy.call_screen(new_context_screen)

label new_context_main:
    $ game.main()
    return

label new_context_label(label):
    jump expression dialog_select(label)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
