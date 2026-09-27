init -20 python hide:

    json_file = renpy.file("scripts/data/items.json")
    store.items = json.load(json_file)
    json_file.close()


    json_file = renpy.file("scripts/data/achievements.json")
    store.achievements_json = json.load(json_file)
    json_file.close()


    json_file = renpy.file("scripts/data/dating.json")
    store.dating_data = json.load(json_file)
    json_file.close()


    json_file = renpy.file("scripts/data/default_keymap.json")
    store.default_keymap = json.load(json_file)
    json_file.close()


    json_file = renpy.file("scripts/data/furnishings.json")
    store.furnishings = json.load(json_file)
    json_file.close()


    json_file = renpy.file("scripts/data/location_sounds.json")
    store.location_sounds = json.load(json_file)
    json_file.close()

init -8 python:

    T_all_sleep = Trigger()
    T_all_tick = Trigger()
    T_all_school_entrance = Trigger()
    T_all_on_load = Trigger()
    T_player_woke_up = Trigger()
    T_all_new_week = Trigger()

label INIT_GAME:
    python:
        store.temp_game = Game()
        for attribute, value in [(k, v) for k, v in game.__dict__.items() if k not in ["website_address", "CA_FILE"]]:
            try:
                store.temp_game.__dict__[attribute] = value
            except KeyError:
                pass
        game = store.temp_game
        store.temp_inventory = Inventory()
        store.temp_player = Player()
        for k, v in player.inventory.__dict__.items():
            try:
                store.temp_inventory.__dict__[k] = v
            except KeyError:
                pass
        for k, v in player.__dict__.items():
            if k == "inventory":
                store.temp_player.inventory = store.temp_inventory
            else:
                try:
                    store.temp_player.__dict__[k] = copy(v)
                except KeyError:
                    pass
        player = copy(store.temp_player)
    return

label INIT_GLOBAL:
    call INIT_INVENTORY_ITEMS
    call INIT_GAME
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
