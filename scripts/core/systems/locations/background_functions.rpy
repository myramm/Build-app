init -5 python:
    def default_bg_fn(*args, **kwargs):
        return None

    def upstairs_bedroom_background(blur=False):
        if blur:
            if L_home_sisbedroom.is_here(M_jenny) and not M_jenny.talking:
                if game.timer.is_day():
                    return "backgrounds/location_home_jennybedroom_jenny_day_blur.jpg"
                elif game.timer.is_evening():
                    return "backgrounds/location_home_jennybedroom_jenny_evening_blur.jpg"
                else:
                    return None
            else:
                return None
        else:
            return None

    def mall_pink_background(blur=False):
        if blur:
            if M_jenny.between_states(S_jenny_get_a_toy, S_jenny_bring_toy_back):
                return "backgrounds/location_pink_soldout_blur.jpg"
            else:
                return None
        else:
            return None

    def mall_background(blur=False):
        if blur:
            if M_jenny.is_state(S_jenny_get_a_mask) and game.timer.is_day():
                return "backgrounds/location_mall_day_crowd_blur.jpg"
            else:
                return None
        else:
            return None

    def police_basement_background(blur=False):
        if blur:
            if L_police_basement.is_here(M_yumi):
                return 'backgrounds/location_police_basement_any_blur_yumi.jpg'
            else:
                return None
        else:
            return None

    def library_backroom_background(blur=False):
        if blur:
            if False and game.timer.is_day():
                return 'backgrounds/location_library_backroom_day_hd_cam.jpg'
            else:
                return None
        else:
            return None

    def school_frontyard_background(blur=False):
        if game.timer.is_weekend():
            if blur:
                if game.timer.is_day():
                    return "school_frontyard_weekend_day_blur"
            else:
                if game.timer.is_day():
                    return "backgrounds/location_school_frontyard_weekend_day.jpg"
        else:
            return None

    def school_assemblyhall_background(blur=False):
        if blur:
            return None
        else:
            if M_dewitt.is_state([S_dewitt_paint_trail, S_dewitt_check_up, S_dewitt_eve_meet_up, S_dewitt_erik_get_beer]):
                return "backgrounds/location_school_assembly_hall_paint.jpg"
            elif M_dewitt.is_state([S_dewitt_attend_talent_show, S_dewitt_talent_show]):
                return "backgrounds/location_school_assembly_hall_talentshow.jpg"
            else:
                return None

    def home_bedroom_background(blur=False):
        if blur:
            return
        else:
            if M_player.get('pc_fixed'):
                return game.timer.image("backgrounds/location_home_bedroom{}.jpg")
            else:
                return game.timer.image("backgrounds/location_home_bedroom_broken{}.jpg")

    def comic_store_background(blur=False):
        if blur:
            if M_jenny.between_states(S_jenny_get_a_mask, S_jenny_come_back_camshow):
                return 'mall_comic_lucha_blur'
        else:
            if M_jenny.between_states(S_jenny_get_a_mask, S_jenny_come_back_camshow):
                return "backgrounds/location_mall_comic_lucha_day.jpg"
        return

    def mall_toilets_background(blur=False):
        if not blur:
            if game.rump_n_cunt:
                return "backgrounds/location_mall_washroom_event.jpg"
        return

    def dianes_garden_background(blur=False):
        if blur:
            if M_diane.is_state(S_diane_get_bug_spray, S_diane_clear_bug_infested_garden):
                if game.timer.is_day():
                    return "backgrounds/location_diane_garden_dead_day_blur.jpg"
                else:
                    return "backgrounds/location_diane_garden_dead_night_blur.jpg"
        else:
            return

    def mias_house_entrance_background(blur=False):
        if not blur:
            if M_mia.get("harold left") and game.timer.is_dark():
                return "backgrounds/location_mia_house_without_night.jpg"

    def mias_mailbox_background(blur=False):
        return None 

    def helens_bedroom_background(blur=False):
        if not blur:
            if M_helen.is_state(S_helen_master_servant_fun):
                return "backgrounds/location_mia_house_helen_closed.jpg"

    def church_background(blur=False):
        if game.timer.is_weekend() and game.timer.is_morning():
            if blur:
                bgs = ('church_full01_b',
                           'church_full02_b',
                           'church_full03_b')
            else:
                bgs = ('location_church_full01_day',
                           'location_church_full02_day',
                           'location_church_full03_day')
            if player.location.is_here(M_helen, M_harold):
                return bgs[0]
            elif player.location.is_here(M_helen):
                return bgs[1]
            else:
                return bgs[2]

    def tattoo_parlor_front_background(blur=False):
        if M_eve.is_state(S_eve_clients_tattooshop_crowd, S_eve_clients_take_care_clients) and blur:
            return "tattoo_parlor_front_crowd_blur"

    def tattoo_parlor_interior_background(blur=False):
        if M_eve.is_state(S_eve_clients_tattooshop_crowd, S_eve_clients_take_care_clients) and game.timer.is_day():
            if blur:
                return "tattoo_parlor_interior_crowd_blur"
            else:
                return "backgrounds/location_tattoo_indoor_day_crowd.jpg"

    def tattoo_parlor_garage_background(blur=False):
        if blur:
            if M_eve.party_in_progress and game.timer.is_date(date=Date(tod=2, dow=5)):
                return "tattoo_parlor_garage_party_blur"
        else:
            if M_eve.party_in_progress and game.timer.is_date(date=Date(tod=2, dow=5)):
                return "backgrounds/location_tattoo_garage_evening_party.jpg"

    def tattoo_parlor_fireescape_background(blur=False):
        if blur:
            if M_eve.party_in_progress and game.timer.is_date(date=Date(tod=2, dow=5)):
                return "tattoo_parlor_fireescape_party_blur"
        else:
            if M_eve.party_in_progress and game.timer.is_date(date=Date(tod=2, dow=5)):
                return "backgrounds/location_tattoo_garagetop_evening_party.jpg"

    def tattoo_parlor_roof_background(blur=False):
        if blur:
            if M_eve.party_in_progress and game.timer.is_date(date=Date(tod=2, dow=5)):
                return "tattoo_parlor_roof_party_blur"
        else:
            if M_eve.party_in_progress and game.timer.is_date(date=Date(tod=2, dow=5)):
                return "backgrounds/location_tattoo_rooftop_evening_party.jpg"

    def tattoo_parlor_alley_background(blur=False):
        if blur:
            if M_eve.party_in_progress and game.timer.is_date(date=Date(tod=2, dow=5)):
                return "tattoo_parlor_alley_party_blur"
        else:
            if M_eve.party_in_progress and game.timer.is_date(date=Date(tod=2, dow=5)):
                return "backgrounds/location_tattoo_alley_evening_party.jpg"

    def trailer_bedroom_background(blur=False):
        if not blur and M_roxxy.finished_state(S_roxxy_get_oil):
            if game.timer.is_dark():
                return "backgrounds/location_trailer_bedroom_trophy_night.jpg"
            else:
                return "backgrounds/location_trailer_bedroom_trophy_day.jpg"

    def pizzeria_kitchen_background(blur=False):
        if blur and M_anon.is_state(S_ano11_prep) and game.timer.is_day():
            return im.Blur(im.FactorScale(im.Crop(
                im.Composite(
                    (config.screen_width, config.screen_height),
                    (0, 0), 'backgrounds/location_pizza_kitchen_day.jpg',
                    (385, 313), 'objects/object_door_126_patch.png'),
                (350, 296, 342, 256)), 3.5), 1.7)

    def church_graveyard_background(blur=False):
        if blur and game.timer.is_night() and game.timer.is_fullmoon():
            return im.Blur(im.Composite(
                    (config.screen_width, config.screen_height),
                    (0, 0), L_church_graveyard.background,
                    (0, 0), 'backgrounds/location_church_graveyard_night_fullmoon.png'), 1.7)

    def bank_lobby_bg():
        if game.timer.is_date(dow=1, tod=0):
            return 'bank_lobby_empty'
        return 'bank_lobby'

    def liu_bedroom_bg():
        if M_anon.finished_state(S_ano24_done):
            return 'liu_bedroom_after'
        return 'liu_bedroom'

    def warehouse_cargo_bg():
        if M_anon.finished_state(S_ano27_done):
            return 'warehouse_storage_vodka'
        return 'warehouse_storage'

    def warehouse_depot_bg():
        if M_anon.finished_state(S_ano27_done):
            return 'warehouse_main_vodka'
        if M_anon.finished_state(S_ano27_yolo):
            return 'warehouse_main_bodies'
        return 'warehouse_main'

    def warehouse_lab_bg():
        if M_anon.finished_state(S_ano27_done):
            return 'warehouse_drugs_vodka'
        return 'warehouse_drugs'

    def warehouse_storage_bg():
        if M_anon.finished_state(S_ano27_done):
            return 'warehouse_hostage_vodka'
        return 'warehouse_hostage'
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
