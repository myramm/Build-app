init python:
    def unlock_scene(group, scene, variant=None):
        persistent.cookie_jar[group]['unlocked'] = True
        persistent.cookie_jar[group]['gallery'][scene] = True
        if variant is not None:
            persistent.cookie_jar[group] \
                .setdefault('variants', dict()) \
                .setdefault(scene, set()).add(variant)


    def report_scene(group, scene):
        opts = group.get('variants_available', {}).get(scene, ())
        
        if not persistent.eve_bulge_unlocked:
            opts = tuple(v for v in opts if v != 'trans')
        
        opts = len(opts)
        
        if opts < 2:
            return
        
        scene = scene.replace('label', 'unlocked')
        show = group.get('variants', {}).get(scene, ())
        
        return '{} / {}'.format(len(show), opts)


init python hide:
    def fix_cookie_jar_paths(cookie):
        idle = cookie["idle"]
        locked_idle = cookie["locked_idle"]
        idle = idle.split("/")
        locked_idle = locked_idle.split("/")
        gallery_image = cookie["gallery_image"].split("/")
        cookie["idle"] = "cookie_jar/" + idle[1]
        cookie["locked_idle"] = "cookie_jar/" + locked_idle[1]
        cookie["gallery_image"] = "cookie_jar/" + gallery_image[1]

    if persistent.cookie_jar is None:
        persistent.cookie_jar = {}
    else:
        for key, cookie in persistent.cookie_jar.items():
            fix_cookie_jar_paths(cookie)
            
            
            
            if 'variants_available' not in cookie:
                continue
            
            variants = cookie.get('variants')
            
            if not variants:
                cookie['unlocked'] = False
                continue
            
            gallery = cookie.get('gallery', ())
            for scene in gallery:
                gallery[scene] = bool(gallery[scene] and variants.get(scene, True))

    if "Debbie" not in persistent.cookie_jar:
        persistent.cookie_jar["Debbie"] = {"idle": "cookie_jar/cookie_jar_01.png",
                                           "locked_idle": "cookie_jar/cookie_jar_01_locked.png",
                                           "unlocked": False,
                                           "order": "01",
                                           "gallery": {},
                                           "gallery_image": "cookie_jar/cookie_jar_box_01_",
        }

    persistent.cookie_jar["Debbie"]["gallery_labels"] = {"01_label": "mom_spy",
                                                         "02_label": "replay_mom_panties",
                                                         "03_label": "mom_night_suck",
                                                         "04_label": "mom_midnight_swim",
                                                         "05_label": "debbie_car_sex",
                                                         "06_label": "mom_night_sex_replay",
                                                         "07_label": "shower_mom_sex_replay",
                                                         "08_label": "mom_couch_sex_replay",
                                                         "09_label": "mom_kitchen_replay",
                                                         "10_label": "mom_mc_sexvisit",
                                                         "11_label": "mom_sex_replay",
                                                         "12_label": "mom_basement_replay",
                                                         "13_label": "scene_debbie_diane_bedroom.replay",
    }

    if "Jenny" not in persistent.cookie_jar:
        persistent.cookie_jar["Jenny"] = {"idle": "cookie_jar/cookie_jar_02.png",
                                          "locked_idle": "cookie_jar/cookie_jar_02_locked.png",
                                          "unlocked": False,
                                          "order": "02",
                                          "gallery": {},
                                          "gallery_image": "cookie_jar/cookie_jar_box_02_",
        }

    persistent.cookie_jar["Jenny"]["gallery_labels"] = {"01_label": "hallway_jenny_hallway_eavesdropping",
                                                        "02_label": "jenny_taking_pictures_replay",
                                                        "03_label": "jenny_computer_video_ec",
                                                        "04_label": "jenny_computer_video_uv",
                                                        "05_label": "jenny_computer_video_bm",
                                                        "06_label": "hallway_jenny_caught_talking_to_camslut",
                                                        "07_label": "button_jenny_start_camshow_handjob",
                                                        "08_label": "entrance_jenny_catch_her_jilling",
                                                        "09_label": "sis_bedroom_jenny_start_camshow_blowjob",
                                                        "10_label": "bedroom_jenny_give_cunni",
                                                        "11_label": "sis_bedroom_jenny_cheerleader_sex",
                                                        "12_label": "jenny_mc_room_sex_on_sleep",
                                                        "13_label": "shower_jenny_blowjob_intro_first",
                                                        "14_label": "jenny_shower_sex_intro_replay",
                                                        "15_label": "button_jenny_fool_around_diningroom_first",
                                                        "16_label": "button_jenny_fool_around_pool_first",
                                                        "17_label": "jenny_bed_night_sex_intro",
                                                        "18_label": "movie_theatre_jenny_movie_date.replay",
                                                        "19_label": "scene_jenny_sex_pregnant.replay",
                                                        "20_label": "scene_jenny_solo_peephole.replay",
    }

    persistent.cookie_jar["Jenny"]["variants_available"] = {
        "20_label": ('anon', 'daddy')}

    if "Diane" not in persistent.cookie_jar:
        persistent.cookie_jar["Diane"] = {"idle": "cookie_jar/cookie_jar_03.png",
                                          "locked_idle": "cookie_jar/cookie_jar_03_locked.png",
                                          "unlocked": False,
                                          "order": "03",
                                          "gallery": {},
                                          "gallery_image": "cookie_jar/cookie_jar_box_03_",
        }

    persistent.cookie_jar["Diane"]["gallery_labels"] = {"01_label": "dianes_kitchen_diane_look_in_kitchen",
                                                        "02_label": "dianes_garden_diane_drunk_like_a_sailor",
                                                        "03_label": "kitchen_diane_dinner",
                                                        "04_label": "diane_cookiejar.paizuri",
                                                        "05_label": "diane_cookiejar.cucumber",
                                                        "06_label": "diane_cookiejar.breed",
                                                        "07_label": "diane_debbie_sex_start",
                                                        "08_label": "scene_diane_sex_milk.replay",
    }

    persistent.cookie_jar["Diane"]["variants_available"] = {
        "08_label": ('cow', 'naked')}


    if "Mrs Johnson" not in persistent.cookie_jar:
        persistent.cookie_jar["Mrs Johnson"] = {"idle": "cookie_jar/cookie_jar_04.png",
                                                "locked_idle": "cookie_jar/cookie_jar_04_locked.png",
                                                "unlocked": False,
                                                "order": "04",
                                                "gallery": {},
                                                "gallery_image": "cookie_jar/cookie_jar_box_04_",
        }

    persistent.cookie_jar["Mrs Johnson"]["gallery_labels"] = {"01_label": "mrsj_afterpoker_fun",
                                                              "02_label": "mrsj_private_yoga_perv_jenny_replay",
                                                              "03_label": "mrsj_erik_cunni_perv_jenny_replay",
                                                              "04_label": "mrsj_3some",
                                                              "05_label": "mrsj_private_yoga",
    }

    if "Mia" not in persistent.cookie_jar:
        persistent.cookie_jar["Mia"] = {"idle": "cookie_jar/cookie_jar_05.png",
                                        "locked_idle": "cookie_jar/cookie_jar_05_locked.png",
                                        "unlocked": False,
                                        "order": "05",
                                        "gallery": {},
                                        "gallery_image": "cookie_jar/cookie_jar_box_05_",
        }

    persistent.cookie_jar["Mia"]["gallery_labels"] = {"01_label": "telescope_mia_night_2",
                                                      "02_label": "telescope_mia_sister_spying",
                                                      "03_label": "mia_bedroom_sex",
    }

    if "Helen" not in persistent.cookie_jar:
        persistent.cookie_jar["Helen"] = {"idle": "cookie_jar/cookie_jar_06.png",
                                          "locked_idle": "cookie_jar/cookie_jar_06_locked.png",
                                          "unlocked": False,
                                          "order": "06",
                                          "gallery": {},
                                          "gallery_image": "cookie_jar/cookie_jar_box_06_",
        }

    persistent.cookie_jar["Helen"]["gallery_labels"] = {"01_label": "helen_baton_replay",
                                                        "02_label": "helen_bedroom_sex",
    }

    if "Angelica" not in persistent.cookie_jar:
        persistent.cookie_jar["Angelica"] = {"idle": "cookie_jar/cookie_jar_07.png",
                                             "locked_idle": "cookie_jar/cookie_jar_07_locked.png",
                                             "unlocked": False,
                                             "order": "07",
                                             "gallery": {},
                                             "gallery_image": "cookie_jar/cookie_jar_box_07_",
        }

    persistent.cookie_jar["Angelica"]["gallery_labels"] = {"01_label": "helen_sacrement_training_part2",
                                                           "02_label": "helen_final_sacrament",
                                                           "03_label": "helen_final_mc",
    }

    if "Ivy" not in persistent.cookie_jar:
        persistent.cookie_jar["Ivy"] = {"idle": "cookie_jar/cookie_jar_08.png",
                                        "locked_idle": "cookie_jar/cookie_jar_08_locked.png",
                                        "unlocked": False,
                                        "order": "08",
                                        "gallery": {},
                                        "gallery_image": "cookie_jar/cookie_jar_box_08_",
        }

    persistent.cookie_jar["Ivy"]["gallery_labels"] = {
        "01_label": "ivy_paizuri",
        "02_label": "ivy_blowjob",
        "03_label": "ivy_reverse_cowgirl",
        "04_label": "ivy_cowgirl",
        "05_label": "scene_ivy_vera.replay",
        "06_label": "scene_ivy_jane.replay"}

    if "June" not in persistent.cookie_jar:
        persistent.cookie_jar["June"] = {"idle": "cookie_jar/cookie_jar_09.png",
                                         "locked_idle": "cookie_jar/cookie_jar_09_locked.png",
                                         "unlocked": False,
                                         "order": "09",
                                         "gallery": {},
                                         "gallery_image": "cookie_jar/cookie_jar_box_09_",
        }

    persistent.cookie_jar["June"]["gallery_labels"] = {"01_label": "june_cosplay_replay",
    }

    if "Cassie" not in persistent.cookie_jar:
        persistent.cookie_jar["Cassie"] = {"idle": "cookie_jar/cookie_jar_10.png",
                                           "locked_idle": "cookie_jar/cookie_jar_10_locked.png",
                                           "unlocked": False,
                                           "order": "10",
                                           "gallery": {},
                                           "gallery_image": "cookie_jar/cookie_jar_box_10_",
        }

    persistent.cookie_jar["Cassie"]["gallery_labels"] = {"01_label": "medic_room_cassie_replay",
    }

    if "Roz" not in persistent.cookie_jar:
        persistent.cookie_jar["Roz"] = {"idle": "cookie_jar/cookie_jar_11.png",
                                        "locked_idle": "cookie_jar/cookie_jar_11_locked.png",
                                        "unlocked": False,
                                        "order": "11",
                                        "gallery": {},
                                        "gallery_image": "cookie_jar/cookie_jar_box_11_",
        }

    persistent.cookie_jar["Roz"]["gallery_labels"] = {"01_label": "scene_roz_sex",
                                                      "02_label": "elevator_priya_check_pregnax",
                                                      "03_label": "scene_roz_blowjob",
    }

    if "Aqua" not in persistent.cookie_jar:
        persistent.cookie_jar["Aqua"] = {"idle": "cookie_jar/cookie_jar_12.png",
                                         "locked_idle": "cookie_jar/cookie_jar_12_locked.png",
                                         "unlocked": False,
                                         "order": "12",
                                         "gallery": {},
                                         "gallery_image": "cookie_jar/cookie_jar_box_12_",
        }

    persistent.cookie_jar["Aqua"]["gallery_labels"] = {"01_label": "aqua_sex_replay",
                                                       "02_label": "aqua_succ_replay",
    }

    if "Rump" not in persistent.cookie_jar:
        persistent.cookie_jar["Rump"] = {"idle": "cookie_jar/cookie_jar_13.png",
                                         "locked_idle": "cookie_jar/cookie_jar_13_locked.png",
                                         "unlocked": False,
                                         "order": "13",
                                         "gallery": {},
                                         "gallery_image": "cookie_jar/cookie_jar_box_13_",
        }

    persistent.cookie_jar["Rump"]["gallery_labels"] = {"01_label": "rump_hscene_replay",
    }

    if "Judith" not in persistent.cookie_jar:
        persistent.cookie_jar["Judith"] = {"idle": "cookie_jar/cookie_jar_14.png",
                                            "locked_idle": "cookie_jar/cookie_jar_14_locked.png",
                                            "unlocked": False,
                                            "order": "14",
                                            "gallery": {},
                                            "gallery_image": "cookie_jar/cookie_jar_box_14_",
        }

    persistent.cookie_jar["Judith"]["gallery_labels"] = {"01_label": "boys_lockerroom_judith_changing",
                                                         "02_label": "judith_toilet_replay",
    }

    if "Bissette" not in persistent.cookie_jar:
        persistent.cookie_jar["Bissette"] = {"idle": "cookie_jar/cookie_jar_15.png",
                                             "locked_idle": "cookie_jar/cookie_jar_15_locked.png",
                                             "unlocked": False,
                                             "order": "15",
                                             "gallery": {},
                                             "gallery_image": "cookie_jar/cookie_jar_box_15_",
        }

    persistent.cookie_jar["Bissette"]["gallery_labels"] = {"01_label": "french_classroom_bissette_assignment_replay",
                                                           "02_label": "bissettes_office_night_visit_replay",
    }

    if "Dewitt" not in persistent.cookie_jar:
        persistent.cookie_jar["Dewitt"] = {"idle": "cookie_jar/cookie_jar_16.png",
                                           "locked_idle": "cookie_jar/cookie_jar_16_locked.png",
                                           "unlocked": False,
                                           "order": "16",
                                           "gallery": {},
                                           "gallery_image": "cookie_jar/cookie_jar_box_16_",
        }

    persistent.cookie_jar["Dewitt"]["gallery_labels"] = {"01_label": "dewitts_office_dewitt_office_reward",
                                                         "02_label": "guitar_hero_minigame_talent_show_pass",
                                                         "03_label": "dewitt_office_dewitt_night_visit",
    }

    if "Ross" not in persistent.cookie_jar:
        persistent.cookie_jar["Ross"] = {"idle": "cookie_jar/cookie_jar_17.png",
                                         "locked_idle": "cookie_jar/cookie_jar_17_locked.png",
                                         "unlocked": False,
                                         "order": "17",
                                         "gallery": {},
                                         "gallery_image": "cookie_jar/cookie_jar_box_17_",
        }

    persistent.cookie_jar["Ross"]["gallery_labels"] = {"01_label": "button_ross_found_model.replay",
                                                       "02_label": "ross_hscene_replay",
    }

    if "Okita" not in persistent.cookie_jar:
        persistent.cookie_jar["Okita"] = {"idle": "cookie_jar/cookie_jar_18.png",
                                          "locked_idle": "cookie_jar/cookie_jar_18_locked.png",
                                          "unlocked": False,
                                          "order": "18",
                                          "gallery": {},
                                          "gallery_image": "cookie_jar/cookie_jar_box_18_",
        }

    persistent.cookie_jar["Okita"]["gallery_labels"] = {"01_label": "science_classroom_okita_has_glasses_int_pass",
                                                        "02_label": "okitas_office_okita_xray_perving",
                                                        "03_label": "button_okita_tinkered_belt",
                                                        "04_label": "okitas_office_extract_cum",
                                                        "05_label": "okita_pre_hscene_repeatable",
    }

    if "Anna" not in persistent.cookie_jar:
        persistent.cookie_jar["Anna"] = {"idle": "cookie_jar/cookie_jar_19.png",
                                         "locked_idle": "cookie_jar/cookie_jar_19_locked.png",
                                         "unlocked": False,
                                         "order": "19",
                                         "gallery": {},
                                         "gallery_image": "cookie_jar/cookie_jar_box_19_",
        }

    persistent.cookie_jar["Anna"]["gallery_labels"] = {"01_label": "anna_yoga_lesson",
    }

    if "Roxxy" not in persistent.cookie_jar:
        persistent.cookie_jar["Roxxy"] = {"idle": "cookie_jar/cookie_jar_20.png",
                                          "locked_idle": "cookie_jar/cookie_jar_20_locked.png",
                                          "unlocked": False,
                                          "order": "20",
                                          "gallery": {},
                                          "gallery_image": "cookie_jar/cookie_jar_box_20_",
        }

    persistent.cookie_jar["Roxxy"]["gallery_labels"] = {
        "01_label": "roxxy_shower_replay",
        "02_label": "jennys_bedroom_bissette_roxxy_jenny_spying",
        "03_label": "roxxy_locker_rub_hscene_replay",
        "04_label": "roxxy_massage_hscene_replay",
        "05_label": "roxxy_locker_fuck_hscene_replay",
        "06_label": "roxxy_bedroom_fuck_hscene_replay",
        "07_label": "beach_roxxy_solo_replay",
        "08_label": "beach_mc_4some_roxxy_replay",
        "09_label": "scene_roxxy_boobjob.replay",
        "10_label": "scene_roxxy_blowjob.replay"}

    persistent.cookie_jar["Roxxy"]["variants_available"] = {
        "09_label": ('first', 'repeat')}

    if "Latina Twins" not in persistent.cookie_jar:
        persistent.cookie_jar["Latina Twins"] = {"idle": "cookie_jar/cookie_jar_21.png",
                                                 "locked_idle": "cookie_jar/cookie_jar_21_locked.png",
                                                 "unlocked": False,
                                                 "order": "21",
                                                 "gallery": {},
                                                 "gallery_image": "cookie_jar/cookie_jar_box_21_",
        }

    persistent.cookie_jar["Latina Twins"]["gallery_labels"] = {"01_label": "latinas_dialogue_shower",
                                                               "02_label": "latinas_shower_dialogue",
    }

    if "Jane" not in persistent.cookie_jar:
        persistent.cookie_jar["Jane"] = {"idle": "cookie_jar/cookie_jar_22.png",
                                         "locked_idle": "cookie_jar/cookie_jar_22_locked.png",
                                         "unlocked": False,
                                         "order": "22",
                                         "gallery": {},
                                         "gallery_image": "cookie_jar/cookie_jar_box_22_",
        }

    persistent.cookie_jar["Jane"]["gallery_labels"] = {"01_label": "backroom_dialogue",
    }

    if "Annie" not in persistent.cookie_jar:
        persistent.cookie_jar["Annie"] = {"idle": "cookie_jar/cookie_jar_23.png",
                                          "locked_idle": "cookie_jar/cookie_jar_23_locked.png",
                                          "unlocked": False,
                                          "order": "23",
                                          "gallery": {},
                                          "gallery_image": "cookie_jar/cookie_jar_box_23_",
        }

    persistent.cookie_jar["Annie"]["gallery_labels"] = {"01_label": "principals_office_annie_trouble",
                                                        "02_label": "art_minigame_done_dialogue",
    }

    if "Eve" not in persistent.cookie_jar:
        persistent.cookie_jar["Eve"] = {"idle": "cookie_jar/cookie_jar_24.png",
                                          "locked_idle": "cookie_jar/cookie_jar_24_locked.png",
                                          "unlocked": False,
                                          "order": "24",
                                          "gallery": {},
                                          "gallery_image": "cookie_jar/cookie_jar_box_24_",
        }

    persistent.cookie_jar["Eve"]["gallery_labels"] = {"01_label": "guitar_hero_minigame_karaoke_pass",
                                                      "02_label": "tattoo_parlor_tent_eve_voyeurism_follow_tent_replay",
                                                      "03_label": "eve_sex_jerk_intro",
                                                      "04_label": "eve_69",
                                                      "05_label": "eve_sex_front_intro",
                                                      "06_label": "eve_sex_back_intro_replay",
                                                      "07_label": "scene_eve_sex_wake.replay",
                                                      "08_label": "scene_eve_sex_shower.replay",

    }

    persistent.cookie_jar["Eve"]["variants_available"] = {
        "07_label": ('cis', 'cis anal', 'trans'),
        "08_label": ('cis', 'trans')}

    if "Crystal" not in persistent.cookie_jar:
        persistent.cookie_jar["Crystal"] = {"idle": "cookie_jar/cookie_jar_26.png",
                                            "locked_idle": "cookie_jar/cookie_jar_26_locked.png",
                                            "unlocked": False,
                                            "order": "26",
                                            "gallery": {},
                                            "gallery_image": "cookie_jar/cookie_jar_box_26_",
        }

    persistent.cookie_jar["Crystal"]["gallery_labels"] = {
        "01_label": "crystal_hscene_replay",
        "02_label": "scene_crystal_sex_trailer.replay"}

    if "Micoe" not in persistent.cookie_jar:
        persistent.cookie_jar["Micoe"] = {"idle": "cookie_jar/cookie_jar_27.png",
                                          "locked_idle": "cookie_jar/cookie_jar_27_locked.png",
                                          "unlocked": False,
                                          "order": "27",
                                          "gallery": {},
                                          "gallery_image": "cookie_jar/cookie_jar_box_27_",
        }

    persistent.cookie_jar["Micoe"]["gallery_labels"] = {"01_label": "micoe_bj_scene",
        }

    if "Daisy" not in persistent.cookie_jar:
        persistent.cookie_jar["Daisy"] = {"idle": "cookie_jar/cookie_jar_30.png",
                                          "locked_idle": "cookie_jar/cookie_jar_30_locked.png",
                                          "unlocked": False,
                                          "order": "28",
                                          "gallery": {},
                                          "gallery_image": "cookie_jar/cookie_jar_box_30_",
        }

    persistent.cookie_jar["Daisy"]["gallery_labels"] = {
        "01_label": "daisy_sex_breed_start",
        "02_label": "scene_daisy_sex_yard.replay",
        "03_label": "scene_daisy_sex_loft.replay"}

    if "Grace" not in persistent.cookie_jar:
        persistent.cookie_jar["Grace"] = {"idle": "cookie_jar/cookie_jar_32.png",
                                          "locked_idle": "cookie_jar/cookie_jar_32_locked.png",
                                          "unlocked": False,
                                          "order": "29",
                                          "gallery": {},
                                          "gallery_image": "cookie_jar/cookie_jar_box_32_",
        }

    persistent.cookie_jar["Grace"]["gallery_labels"] = {
        "01_label": "grace_odette_sex_massage_repeat",
        "02_label": "scene_grace_sex_apt.replay"}

    if "Odette" not in persistent.cookie_jar:
        persistent.cookie_jar["Odette"] = {"idle": "cookie_jar/cookie_jar_33.png",
                                          "locked_idle": "cookie_jar/cookie_jar_33_locked.png",
                                          "unlocked": False,
                                          "order": "30",
                                          "gallery": {},
                                          "gallery_image": "cookie_jar/cookie_jar_box_33_",
        }

    persistent.cookie_jar["Odette"]["gallery_labels"] = {
        "01_label": "odette_repeat_sex_bike",
        "02_label": "odette_massage_sex_switcheroo",
        "03_label": "scene_odette_sex_crypt.replay",
        "04_label": "scene_odette_blowjob.replay",
        "05_label": "scene_odette_paizuri.replay",
        "06_label": "scene_odette_couch_back.replay"}

    persistent.cookie_jar["Odette"]["variants_available"] = {
        "04_label": ('roof', 'shop'),
        "06_label": ('back', 'anal')}

    if "Consuela" not in persistent.cookie_jar:
        persistent.cookie_jar["Consuela"] = {"idle": "cookie_jar/cookie_jar_34.png",
                                          "locked_idle": "cookie_jar/cookie_jar_34_locked.png",
                                          "unlocked": False,
                                          "order": "31",
                                          "gallery": {},
                                          "gallery_image": "cookie_jar/cookie_jar_box_34_",
        }

    persistent.cookie_jar["Consuela"]["gallery_labels"] = {"01_label": "scene_consuela_blowjob.replay",
                                                           "02_label": "scene_consuela_sex_counter.replay",
                                                           "03_label": "scene_consuela_sex_stairs.replay",
                                                           "04_label": "scene_consuela_sex_floor.replay",
        }

    if "josie" not in persistent.cookie_jar:
        persistent.cookie_jar["josie"] = {
            "idle": "cookie_jar/cookie_jar_37.png",
            "locked_idle": "cookie_jar/cookie_jar_37_locked.png",
            "unlocked": False,
            "order": "32",
            "gallery": {},
            "gallery_image": "cookie_jar/cookie_jar_box_37_"}

    persistent.cookie_jar["josie"]["gallery_labels"] = {
        "01_label": "scene_josie_blowjob.replay",
        "02_label": "scene_josie_sex.replay",
        "03_label": "scene_josie_sex_chair.replay",
        "04_label": "scene_josie_sex_desk.replay"}
    persistent.cookie_jar["josie"]["variants_available"] = {
        "02_label": ('morning', 'afternoon')}

    if "tina" not in persistent.cookie_jar:
        persistent.cookie_jar["tina"] = {
            "idle": "cookie_jar/cookie_jar_38.png",
            "locked_idle": "cookie_jar/cookie_jar_38_locked.png",
            "unlocked": False,
            "order": "33",
            "gallery": {},
            "gallery_image": "cookie_jar/cookie_jar_box_38_"}

    persistent.cookie_jar["tina"]["gallery_labels"] = {
        "01_label": "scene_tina_sex_lounge.replay",
        "02_label": "scene_tina_sex_office.replay"}
    persistent.cookie_jar["tina"]["variants_available"] = {
        "01_label": ('first', 'repeat')}

    if "maria" not in persistent.cookie_jar:
        persistent.cookie_jar["maria"] = {
            "idle": "cookie_jar/cookie_jar_36.png",
            "locked_idle": "cookie_jar/cookie_jar_36_locked.png",
            "unlocked": False,
            "order": "34",
            "gallery": {},
            "gallery_image": "cookie_jar/cookie_jar_box_36_"}

    persistent.cookie_jar["maria"]["gallery_labels"] = {
        "01_label": "scene_maria_sex_storage.replay",
        "02_label": "scene_maria_blowjob.replay",
        "03_label": "scene_maria_sex_kitchen.replay",
        "04_label": "scene_maria_sex_bedroom.replay"}
    persistent.cookie_jar["maria"]["variants_available"] = {
        "01_label": (True, False, 'plus'),
        "03_label": ('normal', 'pregnant')}

    if "iwanka" not in persistent.cookie_jar:
        persistent.cookie_jar["iwanka"] = {
            "idle": "cookie_jar/cookie_jar_39.png",
            "locked_idle": "cookie_jar/cookie_jar_39_locked.png",
            "unlocked": False,
            "order": "34",
            "gallery": {},
            "gallery_image": "cookie_jar/cookie_jar_box_39_"}

    persistent.cookie_jar["iwanka"]["gallery_labels"] = {
        "01_label": "scene_iwanka_blowjob.replay",
        "02_label": "scene_iwanka_sex.replay",
        "03_label": "scene_iwanka_hentai.replay"}
    persistent.cookie_jar["iwanka"]["variants_available"] = {
        "01_label": ('basement', 'bedroom', 'yacht'),
        "02_label": ('bedroom', 'first', 'yacht')}

    if "melonia" not in persistent.cookie_jar:
        persistent.cookie_jar["melonia"] = {
            "idle": "cookie_jar/cookie_jar_40.png",
            "locked_idle": "cookie_jar/cookie_jar_40_locked.png",
            "unlocked": False,
            "order": "34",
            "gallery": {},
            "gallery_image": "cookie_jar/cookie_jar_box_40_"}

    persistent.cookie_jar["melonia"]["gallery_labels"] = {
        "01_label": "scene_melonia_sex.replay"}
    persistent.cookie_jar["melonia"]["variants_available"] = {
        "01_label": ('first', 'repeat')}

    if "liu" not in persistent.cookie_jar:
        persistent.cookie_jar["liu"] = {
            "idle": "cookie_jar/cookie_jar_41.png",
            "locked_idle": "cookie_jar/cookie_jar_41_locked.png",
            "unlocked": False,
            "order": "34",
            "gallery": {},
            "gallery_image": "cookie_jar/cookie_jar_box_41_"}

    persistent.cookie_jar["liu"]["gallery_labels"] = {
        "01_label": "scene_liu_sex_bedroom.replay",
        "02_label": "scene_liu_sex_office.replay"}
    persistent.cookie_jar["liu"]["variants_available"] = {
        "01_label": ('first', 'repeat')}

    if "nadya" not in persistent.cookie_jar:
        persistent.cookie_jar["nadya"] = {
            "idle": "cookie_jar/cookie_jar_42.png",
            "locked_idle": "cookie_jar/cookie_jar_42_locked.png",
            "unlocked": False,
            "order": "34",
            "gallery": {},
            "gallery_image": "cookie_jar/cookie_jar_box_42_"}

    persistent.cookie_jar["nadya"]["gallery_labels"] = {
        "01_label": "scene_nadya_blowjob.replay",
        "02_label": "scene_nadya_sex_office.replay",
        "03_label": "scene_nadya_sex_cargo.replay"}

    if "becca" not in persistent.cookie_jar:
        persistent.cookie_jar["becca"] = {
            "idle": "cookie_jar/cookie_jar_25.png",
            "locked_idle": "cookie_jar/cookie_jar_25_locked.png",
            "unlocked": False,
            "order": "25",
            "gallery": {},
            "gallery_image": "cookie_jar/cookie_jar_box_25_"}

    persistent.cookie_jar["becca"]["gallery_labels"] = {
        "01_label": "beach_becca_solo_replay",
        "02_label": "beach_mc_4some_becca_replay",
        "03_label": "scene_becca_sex_bedroom.replay"}

    if "missy" not in persistent.cookie_jar:
        persistent.cookie_jar["missy"] = {
            "idle": "cookie_jar/cookie_jar_43.png",
            "locked_idle": "cookie_jar/cookie_jar_43_locked.png",
            "unlocked": False,
            "order": "43",
            "gallery": {},
            "gallery_image": "cookie_jar/cookie_jar_box_43_"}

    persistent.cookie_jar["missy"]["gallery_labels"] = {
        "01_label": "beach_missy_solo_replay",
        "02_label": "beach_mc_4some_missy_replay"}

    if "sara" not in persistent.cookie_jar:
        persistent.cookie_jar["sara"] = {
            "idle": "cookie_jar/cookie_jar_44.png",
            "locked_idle": "cookie_jar/cookie_jar_44_locked.png",
            "unlocked": False,
            "order": "44",
            "gallery": {},
            "gallery_image": "cookie_jar/cookie_jar_box_44_"}

    persistent.cookie_jar["sara"]["gallery_labels"] = {
        "01_label": "scene_sara_terry.replay"}

    if "katya" not in persistent.cookie_jar:
        persistent.cookie_jar["katya"] = {
            "idle": "cookie_jar/cookie_jar_45.png",
            "locked_idle": "cookie_jar/cookie_jar_45_locked.png",
            "unlocked": False,
            "order": "45",
            "gallery": {},
            "gallery_image": "cookie_jar/cookie_jar_box_45_"}

    persistent.cookie_jar["katya"]["gallery_labels"] = {
        "01_label": "scene_katya_sex_desk_side.replay"}
    persistent.cookie_jar["katya"]["variants_available"] = {
        "01_label": ('first', 'repeat')}

    if "khadne" not in persistent.cookie_jar:
        persistent.cookie_jar["khadne"] = {
            "idle": "cookie_jar/cookie_jar_46.png",
            "locked_idle": "cookie_jar/cookie_jar_46_locked.png",
            "unlocked": False,
            "order": "46",
            "gallery": {},
            "gallery_image": "cookie_jar/cookie_jar_box_46_"}

    persistent.cookie_jar["khadne"]["gallery_labels"] = {
        "01_label": "scene_khadne_crates_lick.replay",
        "02_label": "scene_khadne_crates_sex.replay"}
    persistent.cookie_jar["khadne"]["variants_available"] = {
        "01_label": ('first', 'repeat'),
        "02_label": ('first', 'repeat')}

    if "svetlana" not in persistent.cookie_jar:
        persistent.cookie_jar["svetlana"] = {
            "idle": "cookie_jar/cookie_jar_47.png",
            "locked_idle": "cookie_jar/cookie_jar_47_locked.png",
            "unlocked": False,
            "order": "47",
            "gallery": {},
            "gallery_image": "cookie_jar/cookie_jar_box_47_"}

    persistent.cookie_jar["svetlana"]["gallery_labels"] = {
        "01_label": "scene_svetlana_furnace_blowjob.replay",
        "02_label": "scene_svetlana_furnace_cowgirl.replay"}
    persistent.cookie_jar["svetlana"]["variants_available"] = {
        "01_label": ('first', 'repeat'),
        "02_label": ('first', 'repeat')}

    if "yoyo" not in persistent.cookie_jar:
        persistent.cookie_jar["yoyo"] = {
            "idle": "cookie_jar/cookie_jar_48.png",
            "locked_idle": "cookie_jar/cookie_jar_48_locked.png",
            "unlocked": False,
            "order": "48",
            "gallery": {},
            "gallery_image": "cookie_jar/cookie_jar_box_48_"}

    persistent.cookie_jar["yoyo"]["gallery_labels"] = {
        "01_label": "scene_yoyo_truck_cowgirl.replay"}
    persistent.cookie_jar["yoyo"]["variants_available"] = {
        "01_label": ('first', 'repeat')}


    for cname, cookie in persistent.cookie_jar.items():
        for cookie_count in range(len(cookie["gallery_labels"].keys())):
            cookie_unlock_name = "{:02}_unlocked".format(cookie_count + 1)
            if cookie_unlock_name not in cookie["gallery"]:
                persistent.cookie_jar[cname]["gallery"][cookie_unlock_name] = False
        if 'variants_available' in cookie:
            var = cookie.setdefault('variants', dict())
            for k in cookie['variants_available']:
                var.setdefault(k.replace('_label', '_unlocked'), set())

    if 'Becca & Missy' in persistent.cookie_jar:
        data = persistent.cookie_jar.pop('Becca & Missy')
        remap = {"01_unlocked": ('missy', '01_unlocked'),
                 "02_unlocked": ('becca', '01_unlocked'),
                 "03_unlocked": ('missy', '02_unlocked'),
                 "04_unlocked": ('becca', '02_unlocked')}
        for k, (g, s) in remap.items():
            if k in data['gallery']:
                unlock_scene(g, s)

    try:
        remap = {'solo': False, 'tony': True}
        data = persistent.cookie_jar['maria']['variants']
        data['01_unlocked'] = set(remap[k] if k in remap else k
                                  for k in data['01_unlocked'])
    except:
        pass

    try: 
        cookie = persistent.cookie_jar['josie']
        v = cookie['variants']['02_unlocked']
        v.discard('evening')
        cookie['gallery']['02_unlocked'] = bool(v)
    except:
        pass

    ver = persistent.cookie_jar_version or (0, 0, 0)

    if ver < (0, 20, 16):
        cookie = persistent.cookie_jar['iwanka']
        v = cookie['variants']['02_unlocked']
        if 'first' not in v:
            v.clear()
        
        update = (('iwanka', 2), ('liu', 1), ('melonia', 1), ('tina', 1))
        
        for group, scene in update:
            cookie = persistent.cookie_jar[group]
            scene = '{:02}_unlocked'.format(scene)
            
            if cookie['gallery'].get(scene) and not cookie['variants'][scene]:
                unlock_scene(group, scene, variant='first')

    if ver < app.version:
        persistent.cookie_jar_version = app.version


label replay_INITS(replay_label, replay_cookie):
    python:
        firstname = persistent.firstname or 'Anon'
        jen_name = store.jen_name
        deb_name = store.deb_name
        player = Player(firstname)
        game = Game()
        fsm_data = FSMData()

    call INIT_INVENTORY_ITEMS

    define player_name = Character('[firstname]', color="#6f96f1")

    python:
        player.location = L_home_bedroom
        player.pregnancy_chance = 0.0
        properties =  {
            "firstname": firstname,
            "jen_name": jen_name,
            "deb_name": deb_name,
            "player": player,
            "game": game,
            "player_name": player_name,
            "fsm_data": fsm_data,
            "location_data": LocationData.new_location_data(),
        }
        for iter_str, iter_var in list(locals().iteritems()):
            if ("M_" in iter_str or "S_" in iter_str or "T_" in iter_str or \
                "L_" in iter_str or iter_str.startswith("erik_") or iter_str.startswith("mrsj_")):
                new_var = iter_var
                if iter_str in ('M_anon', 'M_melonia'):
                    new_var._cleared_states.update({k: True for k in new_var._states.keys()})
                properties[iter_str] = new_var


    $ renpy.call_replay(Game.dialog_select(replay_label), properties)
    call screen character(replay_cookie)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
