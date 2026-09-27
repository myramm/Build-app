init 90 python:

    background_names = {}
    for location in store.locations.values():
        if callable(location._background):
            continue
        formatter = "backgrounds/location_{}".format(location._bg)+ "{}{}{}.jpg"
        possible_periods = ("_christmas", "_halloween", "")
        possible_times = ("_morning", "_afternoon", "_day", "_evening", "_night", "_any")
        possible_attrs = ("", "_blur", "_closeup")
        background_names[location] = []
        for period in possible_periods:
            for time in possible_times:
                for attr in possible_attrs:
                    imagename = formatter.format(period, time, attr)
                    img = imagename[len("backgrounds/location_"):-4]
                    image = Image(imagename)
                    if Game.can_show(imagename):
                        background_names[location].append((img, imagename))
                    elif attr == "_blur" and Game.can_show(formatter.format(period, time, "")):
                        background_names[location].append((img, '(blur) ' + formatter.format(period, time, "")))


image map_base_day = "map/map_base.jpg"
image map_base_day_blur = im.Blur("map/map_base.jpg", 1.7)
image map_base_night_blur = im.Blur("map/map_base_night.jpg", 1.7)

image school_frontyard_weekend_day_blur = im.Blur("backgrounds/location_school_frontyard_weekend_day.jpg", 1.7)
image school_assembly_hall_closeup_floor = ConditionSwitch(
    'M_dewitt.between_states(S_dewitt_paint_trail, S_dewitt_erik_get_beer)',
    'location_school_assembly_hall_closeup_floor_graffiti',
    'True',
    'location_school_assembly_hall_closeup_floor')

image tattoo_parlor_garage_party_blur = im.Blur("backgrounds/location_tattoo_garage_evening_party.jpg", 1.7)
image tattoo_parlor_fireescape_party_blur = im.Blur("backgrounds/location_tattoo_garagetop_evening_party.jpg", 1.7)
image tattoo_parlor_roof_party_blur = im.Blur("backgrounds/location_tattoo_rooftop_evening_party.jpg", 1.7)
image tattoo_parlor_alley_party_blur = im.Blur("backgrounds/location_tattoo_alley_evening_party.jpg", 1.7)
image tattoo_parlor_front_crowd_blur = "backgrounds/location_tattoo_day_crowd_blur.jpg"
image tattoo_parlor_interior_crowd_blur = im.Blur('backgrounds/location_tattoo_indoor_day_crowd.jpg', 1.7)



image mc_locker = "backgrounds/location_school_locker_mc_day.jpg"
image mc_locker_night = "backgrounds/location_school_locker_mc_night.jpg"
image erik_locker = "backgrounds/location_school_locker_erik_day.jpg"
image erik_locker_night = "backgrounds/location_school_locker_erik_night.jpg"
image location_diane_garden_cutscene12 = "backgrounds/location_diane_garden_cutscene12_[M_diane.outfit.get].jpg"
image location_diane_garden_cutscene12b = "backgrounds/location_diane_garden_cutscene12b_[M_diane.outfit.get].jpg"


image dianeentrance = "backgrounds/location_diane_entrance_day.jpg"
image dianebedroom = "backgrounds/location_diane_bedroom_day.jpg"
image dianebedroom_b = "backgrounds/location_diane_bedroom_day_blur.jpg"
image dianebedroom_closeup = "backgrounds/location_diane_bedroom_closeup.jpg"
image dianebed = "backgrounds/location_diane_bedroom_bed.jpg"
image diane_masturbate 1 = "backgrounds/location_diane_kitchen_vegies01.jpg"
image diane_masturbate 2 = "backgrounds/location_diane_kitchen_vegies01b.jpg"
image dianekitchen1 = "backgrounds/location_diane_kitchen_day.jpg"
image dianekitchen = "backgrounds/location_diane_kitchen_day_blur.jpg"
image dianekitchen_closeup = "backgrounds/location_diane_kitchen_closeup.jpg"
image garden_firsttime_01 = "backgrounds/location_diane_garden_cutscene01.jpg"
image garden_firsttime_02 = "backgrounds/location_diane_garden_cutscene02.jpg"
image milking 1 = "backgrounds/location_diane_shed_closeup.jpg"
image pump_object = "objects/item_pump2.png"
image shed = "backgrounds/location_diane_shed01_day.jpg"
image shed_night = "backgrounds/location_diane_shed01_night.jpg"
image shed_blur_night = "backgrounds/location_diane_shed01_night_blur.jpg"
image shed_closeup 1 = "backgrounds/location_diane_shed_closeup.jpg"
image shed_closeup 2 = "backgrounds/location_diane_shed_closeup02.jpg"
image shed_closeup 3 = "backgrounds/location_diane_shed_closeup03.jpg"
image garden_close = "backgrounds/location_diane_garden_close_day_blur.jpg"
image garden = "backgrounds/location_diane_garden_day_blur.jpg"
image garden_dead = "backgrounds/location_diane_garden_dead_day_blur.jpg"
image garden_night = "backgrounds/location_diane_garden_night_blur.jpg"
image garden_dead_night = "backgrounds/location_diane_garden_dead_night_blur.jpg"
image garden_event01 = "backgrounds/location_diane_garden_cutscene03.jpg"
image library_shelf = "backgrounds/location_library_shelf_day.jpg"


image awesomo_tag = "backgrounds/location_park_awesomo.jpg"


image basketball_b = "backgrounds/location_basketball_day_blur.jpg"
image basketball_night_b = "backgrounds/location_basketball_night_blur.jpg"


image location_beach_island_blur = "backgrounds/location_beach_island_day_blur.jpg"
image location_beach_island = "backgrounds/location_beach_island_day.jpg"


image church = "backgrounds/location_church_day.jpg"
image church_c = "backgrounds/location_church_closeup.jpg"
image church_confession = "backgrounds/location_church_confession_day.jpg"
image church_stairs_night = "backgrounds/location_church_stairs_night.jpg"
image church_cs01 = "backgrounds/location_church_cutscene01.jpg"
image church_cs02 = "backgrounds/location_church_cutscene02.jpg"
image church_nun_night_c = "backgrounds/location_church_nun_night_closeup.jpg"
image church_full01_b = im.Blur("backgrounds/location_church_full01_day.jpg", 1.7)
image church_full02_b = im.Blur("backgrounds/location_church_full02_day.jpg", 1.7)
image church_full03_b = im.Blur("backgrounds/location_church_full03_day.jpg", 1.7)
image church_nun_night_hs_1 = "backgrounds/location_church_nun_night_hscene_01.jpg"
image church_nun_night_hs_2 = "backgrounds/location_church_nun_night_hscene_02.jpg"
image note_01_c = "objects/closeup_note01.png"


image donut_c = "backgrounds/location_donut_closeup.jpg"


image erikhouse = "backgrounds/location_erik_house_day_blur.jpg"
image erikhouse_night = "backgrounds/location_erik_house_night_blur.jpg"
image eriks_backyard_c = "backgrounds/location_erik_house_backyard_closeup.jpg"
image eriks_backyard_b = "backgrounds/location_erik_house_backyard_day_blur.jpg"
image eriks_backyard_night = "backgrounds/location_erik_house_backyard_night.jpg"
image eriks_backyard_night_b = "backgrounds/location_erik_house_backyard_night_blur.jpg"
image eriks_room_c = "backgrounds/location_erik_house_bedroom_day_closeup.jpg"
image eriks_room_night_c = "backgrounds/location_erik_house_bedroom_night_closeup.jpg"
image erik_entrance_c = "backgrounds/location_erik_house_inside_day_closeup.jpg"
image erik_entrance_night_c = "backgrounds/location_erik_house_inside_night_closeup.jpg"
image erik_indoors = "backgrounds/location_erik_house_inside_day_blur.jpg"
image erik_basement_cabinet = "backgrounds/location_erik_basement_cabinet.jpg"
image erik_basement_c = "backgrounds/location_erik_basement01_closeup.jpg"
image erik_cutscene = "backgrounds/location_erik_basement_cutscene.jpg"
image erik_basement_back_c = "backgrounds/location_erik_basement_back_closeup.jpg"
image erik_house_bedroom = "backgrounds/location_erik_house_bedroom_day.jpg"
image erik_house_bedroom_b = "backgrounds/location_erik_house_bedroom_day_blur.jpg"
image erik_house_bedroom_night = "backgrounds/location_erik_house_bedroom_night.jpg"
image erik_house_bedroom_night_b = "backgrounds/location_erik_house_bedroom_night_blur.jpg"
image erik_inside = "backgrounds/location_erik_house_inside_day.jpg"
image erik_inside_b = "backgrounds/location_erik_house_inside_day_blur.jpg"
image erik_inside_night = "backgrounds/location_erik_house_inside_night.jpg"
image erik_inside_night_b = "backgrounds/location_erik_house_inside_night_blur.jpg"
image erik_house_cs02 = "backgrounds/location_erik_house_cutscene02.jpg"
image erik_house_cs03 = "backgrounds/location_erik_house_cutscene03.jpg"
image erik_house_cs04 = "backgrounds/location_erik_house_cutscene04.jpg"
image erik_house_cs05 = "backgrounds/location_erik_house_cutscene05.jpg"
image erik_house_upstairs_night_c01 = "backgrounds/location_erik_house_upstairs_night_closeup.jpg"
image erik_house_upstairs_night_c02 = "backgrounds/location_erik_house_upstairs_night_closeup2.jpg"
image erik_house_night_cops = "backgrounds/location_erik_house_night_cops.jpg"
image door_thief_night = "objects/object_door_70_thief_night.png"
image erik_upstairs = "backgrounds/location_erik_house_upstairs_day.jpg"
image erik_upstairs_b = "backgrounds/location_erik_house_upstairs_day_blur.jpg"
image erik_upstairs_night = "backgrounds/location_erik_house_upstairs_night.jpg"
image erik_upstairs_night_b = "backgrounds/location_erik_house_upstairs_night_blur.jpg"
image erik_upstairs_night_c = "backgrounds/location_erik_house_upstairs_night_closeup.jpg"
image erik_upstairs_night_c2 = "backgrounds/location_erik_house_upstairs_night_closeup2.jpg"
image erik_upstairs_night_c3 = "backgrounds/location_erik_house_upstairs_night_closeup3.jpg"
image under_eriks_bed = "backgrounds/location_erik_house_bedroom_under_day.jpg"
image under_eriks_bed_night = "backgrounds/location_erik_house_bedroom_under_night.jpg"
image erik_basement_cs2 = "backgrounds/location_erik_basement_cutscene2.jpg"
image erik_basement_back_b_01 = "backgrounds/location_erik_basement_back_blur_01.jpg"
image erik_basement_back_b_02 = "backgrounds/location_erik_basement_back_blur_02.jpg"
image erik_basement_back_b_03 = "backgrounds/location_erik_basement_back_blur_03.jpg"



image forest = "backgrounds/location_forest_day.jpg"
image forest_b = "backgrounds/location_forest_day_blur.jpg"
image forest_night = "backgrounds/location_forest_night.jpg"
image forest_night_b = "backgrounds/location_forest_night_blur.jpg"
image forest_closeup = "backgrounds/location_forest_closeup.jpg"
image forest_dirt1 = "backgrounds/location_forest_dirt1.jpg"
image forest_dirt2 = "backgrounds/location_forest_dirt2.jpg"
image forest_dirt3 = "backgrounds/location_forest_dirt3.jpg"
image forest_altar = "backgrounds/location_forest_altar_cutscene_day.jpg"
image forest_altar_night = "backgrounds/location_forest_altar_cutscene_night.jpg"


image yoga_room = "backgrounds/location_gym_yoga_day_blur.jpg"
image yoga_room_night = "backgrounds/location_gym_yoga_night_blur.jpg"
image yoga_front = "backgrounds/location_gym_yoga_front.jpg"
image lifting = "backgrounds/location_gym_bench.jpg"
image training = "backgrounds/location_gym_day.jpg"
image training_b = "backgrounds/location_gym_day_blur.jpg"
image training_c = "backgrounds/location_gym_day_closeup.jpg"
image training_night = "backgrounds/location_gym_night.jpg"
image training_night_b = "backgrounds/location_gym_night_blur.jpg"
image training_night_c = "backgrounds/location_gym_night_closeup.jpg"


image hospital_first_night_b = "backgrounds/location_hospital_first_night_blur.jpg"
image hospital_second_b = "backgrounds/location_hospital_second_day_blur.jpg"
image hospital_second_night_b = "backgrounds/location_hospital_second_night_blur.jpg"
image hospital_desk = "backgrounds/location_hospital_desk.jpg"
image hospital_lock = "backgrounds/location_hospital_lock.jpg"
image hospital_bed = "backgrounds/location_hospital_bed.jpg"
image hospital_bed_night = "backgrounds/location_hospital_bed_night.jpg"
image hospital_phone = "backgrounds/location_hospital_phone.jpg"
image hospital_phone = "backgrounds/location_hospital_phone.jpg"


image library = "backgrounds/location_library_day_blur.jpg"
image librarydesk = "backgrounds/location_library_desk.jpg"
image library_meeting = "backgrounds/location_library_meeting_day.jpg"
image library_meeting_c = "backgrounds/location_library_meeting_closeup.jpg"
image backroom02 = "backgrounds/location_library_backroom02.jpg"
image backroom03 = "backgrounds/location_library_backroom03.jpg"
image book_01 = "objects/object_book_01.png"
image book_02 = "objects/object_book_02.png"
image book_03 = "objects/object_book_03.png"
image book_01_c = "objects/closeup_book_01.png"
image book_02_c = "objects/closeup_book_02.png"
image book_03_c = "objects/closeup_book_03.png"
image book_04_c = "objects/closeup_book_04.png"
image book_05_c = "objects/closeup_book_05.png"
image book_06_c = "objects/closeup_book_06.png"
image book_07_c = "objects/closeup_book_07.png"


image mall = "backgrounds/location_mall_day_blur.jpg"
image mall_closeup = "backgrounds/location_mall_closeup.jpg"
image mall_comic_lucha_blur = im.Blur('backgrounds/location_mall_comic_lucha_day.jpg', 1.7)
image mall_toilets_event_b = "backgrounds/location_mall_washroom_event_blur.jpg"
image comic = "backgrounds/location_mall_comic_any.jpg"
image massage_room = "backgrounds/location_pink_massage.jpg"
image massage_room_closeup = "backgrounds/location_pink_massage_closeup.jpg"
image movie_lobby = "backgrounds/location_mall_movie_lobby.jpg"
image movie_options = "backgrounds/location_mall_movie_options.jpg"
image movie = "backgrounds/location_mall_movie.jpg"
image location_mall_upstairs = "backgrounds/location_mall_upstairs_day.jpg"
image location_mall_upstairs_blur = "backgrounds/location_mall_upstairs_day_blur.jpg"


image bedroom_sex2 = "backgrounds/location_home_bedroom_sex02.jpg"
image bedroom_desk = "backgrounds/location_home_bedroom_desk.jpg"
image studybedroom01 = "backgrounds/location_home_bedroom_cutscene_study_01.jpg"
image studybedroom02 = "backgrounds/location_home_bedroom_cutscene_study_02.jpg"


image dream_debbie 1 = "backgrounds/location_home_dream_debbie_01.jpg"
image dream_debbie 2 = "backgrounds/location_home_dream_debbie_02.jpg"
image dream_debbie 3 = "backgrounds/location_home_dream_debbie_03.jpg"
image dream_debbie_04 = "backgrounds/location_home_dream_debbie_04.jpg"
image dream_debbie_05 = "backgrounds/location_home_dream_debbie_05.jpg"


image home_hallway_cutscene = "backgrounds/location_home_hallway_cutscene.jpg"
image attic = "backgrounds/location_home_attic_day_blur.jpg"
image attic_night = "backgrounds/location_home_attic_night_blur.jpg"
image home_attic_cs = "backgrounds/location_home_attic_cutscene.jpg"
image home_backyard = "backgrounds/location_home_backyard_day.jpg"
image home_backyard_b = "backgrounds/location_home_backyard_day_blur.jpg"
image home_backyard_night = "backgrounds/location_home_backyard_night.jpg"
image home_backyard_night_b = "backgrounds/location_home_backyard_night_blur.jpg"
image backyard_night_c = "backgrounds/location_home_backyard_night_closeup.jpg"
image home_diningroom_night_c = "backgrounds/location_home_dining_night_closeup.jpg"
image home_diningroom_cs01 = "backgrounds/location_home_dining_cutscene1.jpg"
image home_front_mechanic_night_b = "backgrounds/location_home_front_mechanic_night_blur.jpg"
image home_front_mechanic_night = "backgrounds/location_home_front_mechanic_night.jpg"
image home_front_mechanic_b = "backgrounds/location_home_front_mechanic_day_blur.jpg"
image home_front_mechanic = "backgrounds/location_home_front_mechanic_day.jpg"
image home_garage = "backgrounds/location_home_garage_day_blur.jpg"
image home_garage_closeup = "backgrounds/location_home_garage_closeup.jpg"
image home_garage_night = "backgrounds/location_home_garage_night_blur.jpg"
image car_interior = "backgrounds/location_car.jpg"
image car_interior bj = "backgrounds/location_car_bj.jpg"
image car_interior kiss = "backgrounds/location_car_kiss.jpg"
image mailbox_item04_c = "objects/object_mailbox_item04_closeup.png"
image home_basement = "backgrounds/location_home_basement_day.jpg"
image home_basement_c = "backgrounds/location_home_basement_day_closeup.jpg"
image home_basement_night = "backgrounds/location_home_basement_night.jpg"
image home_basement_sex_01 = "backgrounds/location_home_basement_sex.jpg"
image home_basement_sideview = "backgrounds/location_home_basement_sideview.jpg"
image home_basement_cutscene = "backgrounds/location_home_basement_cutscene.jpg"
image home_tv_channel_01 = "buttons/tv_channel_01.png"
image home_tv_channel_02 = "buttons/tv_channel_02.png"
image home_tv_channel_03 = "buttons/tv_channel_03.png"
image home_tv_channel_04 = "buttons/tv_channel_04.png"
image home_tv_channel_05 = "buttons/tv_channel_05.png"
image home_tv_channel_06 = "buttons/tv_channel_06.png"
image home_tv_channel_06b = "buttons/tv_channel_06b.png"
image home_tv_channel_07 = "buttons/tv_channel_07.png"
image home_tv_channel_08 = "buttons/tv_channel_08.png"
image home_tv_channel_09 = "buttons/tv_channel_09.png"
image home_tv_channel_10 = "buttons/tv_channel_10.png"
image home_livingroom = "backgrounds/location_home_livingroom_day.jpg"
image home_livingroom_b = "backgrounds/location_home_livingroom_day_blur.jpg"
image home_livingroom_c = "backgrounds/location_home_livingroom_day_closeup.jpg"
image home_livingroom_night = "backgrounds/location_home_livingroom_night.jpg"
image home_livingroom_night_b = "backgrounds/location_home_livingroom_night_blur.jpg"
image home_livingroom_night_c = "backgrounds/location_home_livingroom_couch_night_closeup.jpg"
image home_livingroom_couch01 = "backgrounds/location_home_livingroom_couch01.jpg"
image home_livingroom_couch02 = "backgrounds/location_home_livingroom_couch02.jpg"
image home_diningroom = "backgrounds/location_home_diningroom_day.jpg"
image home_diningroom_night = "backgrounds/location_home_diningroom_night.jpg"
image homekitchen = "backgrounds/location_home_kitchen_day_blur.jpg"
image homekitchen_closeup = "backgrounds/location_home_kitchen_day_closeup.jpg"
image homekitchen_secret = "backgrounds/location_home_kitchen_secret.jpg"
image bedroom_cs01 = "backgrounds/location_home_bedroom_cutscene01.jpg"
image bedroom_cs03 = "backgrounds/location_home_bedroom_cutscene03.jpg"
image bedroom_cs04 = "backgrounds/location_home_bedroom_cutscene04.jpg"
image sleeping = "backgrounds/location_home_bedroom_sleeping.jpg"
image hallway = "backgrounds/location_home_hallway_day_blur.jpg"
image hallway_night = "backgrounds/location_home_hallway_night_blur.jpg"
image shower_cutscene1 = "backgrounds/location_home_bathroom_cutscene01.jpg"
image shower_cutscene2 = "backgrounds/location_home_bathroom_cutscene02.jpg"
image shower06a = "backgrounds/location_home_shower_06a.jpg"
image shower06b = "backgrounds/location_home_shower_06b.jpg"
image shower06c = "backgrounds/location_home_shower_06c.jpg"
image shower06d = "backgrounds/location_home_shower_06d.jpg"
image shower_closeup = "backgrounds/location_home_shower_closeup.jpg"
image cutting_grass_01 = "backgrounds/location_home_grass_cutscene_01.jpg"
image cutting_grass_02 = "backgrounds/location_home_grass_cutscene_02.jpg"
image cutting_grass_03 = "backgrounds/location_home_grass_cutscene_03.jpg"
image dining_room = "backgrounds/location_home_dining_day.jpg"
image dining_room_night = "backgrounds/location_home_dining_night.jpg"
image dining_room_lights = "backgrounds/location_home_dining.jpg"
image bedroom_sex_05 = "backgrounds/location_home_bedroom_sex05.jpg"
image jennybedroom_peek_c = "backgrounds/location_home_jennybedroom_closeup_peek.jpg"
image home_garage_cs1 = "backgrounds/location_home_garage_cutscene01.jpg"
image home_garage_cs2 = "backgrounds/location_home_garage_cutscene02.jpg"



image mia_house_helen_night_b = "backgrounds/location_mia_house_helen_night_blur.jpg"
image mia_house_helen_c_night = "backgrounds/location_mia_house_helen_night_closeup.jpg"
image mia_house_helen_c = "backgrounds/location_mia_house_helen_day_closeup.jpg"
image mia_house_helen_sneak = "backgrounds/location_mia_house_helen_sneak.jpg"
image mia_house_helen_window0 = "backgrounds/location_mia_house_helen_closed.jpg"
image mia_house_helen_window1 = "backgrounds/location_mia_house_helen_window1.jpg"
image mia_house_helen_window2 = "backgrounds/location_mia_house_helen_window2.jpg"
image mia_house_helen_window3 = "backgrounds/location_mia_house_helen_window3.jpg"
image mia_house_helen_bed1 = "backgrounds/location_mia_house_helen_bed1.jpg"
image mia_house_helen_closed_c = "backgrounds/location_mia_house_helen_closed_closeup.jpg"
image mia_bedroom_c = "backgrounds/location_mia_bedroom_closeup.jpg"
image miahouse = "backgrounds/location_mia_day_blur.jpg"
image mia_indoors = "backgrounds/location_mia_house_day_blur.jpg"
image mia_bedroom = "backgrounds/location_mia_bedroom_day_blur.jpg"
image mia_bedroom_closeup = "backgrounds/location_mia_bed.jpg"
image mia_bed_sex = "backgrounds/location_mia_bed_sex.jpg"
image mia_sneak01 = "backgrounds/location_mia_cutscene01.jpg"
image mia_sneak02 = "backgrounds/location_mia_cutscene02.jpg"
image mia_bedroom_strip01 = "backgrounds/location_mia_bedroom_strip01.jpg"
image mia_bedroom_strip02 = "backgrounds/location_mia_bedroom_strip02.jpg"
image mia_bedroom_strip03 = "backgrounds/location_mia_bedroom_strip03.jpg"
image mia_bedroom_strip04 = "backgrounds/location_mia_bedroom_strip04.jpg"
image mia_house_upstairs_b = "backgrounds/location_mia_house_upstairs_day_blur.jpg"
image mia_house_upstairs_night_b = "backgrounds/location_mia_house_upstairs_night_blur.jpg"
image mia_house_office_night_b = "backgrounds/location_mia_house_office_night_blur.jpg"
image mia_house_statue = "backgrounds/location_mia_house_statue_day.jpg"
image mia_house_locked_night = "backgrounds/location_mia_house_locked_night.jpg"
image mia_house_locked_night_b = "backgrounds/location_mia_house_locked_night_blur.jpg"
image mia_house_locked_c = "backgrounds/location_mia_house_locked_closeup.jpg"
image mia_house_cs01 = "backgrounds/location_mia_house_cutscene01.jpg"
image key3 = "objects/item_key3.png"
image object_bed_11 = "objects/object_bed_11.png"


image help_debbie_kitchen_cutscene = "backgrounds/location_home_cutscene01.jpg"
image help_debbie_mc_home_cutscene = "backgrounds/location_home_cutscene02.jpg"
image help_debbie_basement_cutscene = "backgrounds/location_home_cutscene03.jpg"
image debbie_cuddle = "backgrounds/location_home_debbie_cuddle.jpg"
image debbie_peek_sequence_1 = "backgrounds/location_home_debbiepeak_day01.jpg"
image debbie_peek_sequence_1_night = "backgrounds/location_home_debbiepeak_night01.jpg"
image debbie_peek_sequence_2 = "backgrounds/location_home_debbiepeak_day02.jpg"
image debbie_peek_sequence_3 = "backgrounds/location_home_debbiepeak_day03.jpg"
image location_debbiebed01 = "backgrounds/location_home_debbiebed01.jpg"
image location_debbiebed02 = "backgrounds/location_home_debbiebed02.jpg"
image location_debbiebed03 = "backgrounds/location_home_debbiebed03.jpg"
image location_debbiebed04 = "backgrounds/location_home_debbiebed04.jpg"
image location_debbiebed05 = "backgrounds/location_home_debbiebed05.jpg"
image debbie_drawer = "backgrounds/location_home_debbiedrawer_day.jpg"
image debbie_drawer_night = "backgrounds/location_home_debbiedrawer_night.jpg"
image debbie_bedroom = "backgrounds/location_home_debbiebedroom_nobasket_day_blur.jpg"
image debbie_bedroom_night = "backgrounds/location_home_debbiebedroom_night_blur.jpg"
image debbie_bedroom_closeup = "backgrounds/location_home_debbiesidebed_day.jpg"
image debbie_bedroom_closeup2 = "backgrounds/location_home_debbiesidebed_day02.jpg"
image debbie_bedroom_closeup_sex = "backgrounds/location_home_debbiesidebed_sex.jpg"
image debbienote = "objects/object_note_01.png"


image mrsj_ball = "backgrounds/location_erik_house_closeup.jpg"
image mrsj_ball_night = "backgrounds/location_erik_house_night_closeup.jpg"


image park = "backgrounds/location_park_day_blur.jpg"
image park_bench = "backgrounds/location_park_bench_night.jpg"
image park_fountain = "backgrounds/location_park_fountain_day.jpg"
image park_fountain_night = "backgrounds/location_park_fountain_night.jpg"
image park_bushes_b = "backgrounds/location_park_bushes_day_blur.jpg"
image park_bushes_night_b = "backgrounds/location_park_bushes_night_blur.jpg"


image pier = "backgrounds/location_pier_day_blur.jpg"
image pier_night = "backgrounds/location_pier_night_blur.jpg"
image pier_closeup = "backgrounds/location_pier_day_closeup.jpg"
image pier_closeup_night = "backgrounds/location_pier_night_closeup.jpg"
image pier_board = "backgrounds/location_pier_board_day.jpg"
image pier_board_night = "backgrounds/location_pier_board_night.jpg"
image location_pier_running = "backgrounds/location_pier_cutscene01.jpg"


image police_board = "backgrounds/location_police_board.jpg"
image police_c_1 = "backgrounds/location_police_closeup01.jpg"
image police_c_2 = "backgrounds/location_police_closeup02.jpg"
image police_c_3 = "backgrounds/location_police_closeup03.jpg"
image police_office_picture = "backgrounds/location_police_office_picture.jpg"
image police_cell = im.Crop("backgrounds/location_police_cell.jpg", (0, 0, 1024, 768))
image police_cell_c_02 = "backgrounds/location_police_cell_closeup02.jpg"
image police_cell_inside_cs1 = "backgrounds/location_police_cell_inside_cutscene1.jpg"
image police_cell_inside_cs2 = "backgrounds/location_police_cell_inside_cutscene2.jpg"
image police_cell_inside_cs3 = "backgrounds/location_police_cell_inside_cutscene3.jpg"
image police_cell_inside_zoom = "backgrounds/location_police_cell_inside_zoom.jpg"
image police_cell_inside_splash = "backgrounds/location_police_cell_inside_splash.jpg"
image police_cell_inside_fight1 = "backgrounds/location_police_cell_inside_fight1.jpg"
image police_cell_inside_fight2 = "backgrounds/location_police_cell_inside_fight2.jpg"


image pool = "backgrounds/location_pool_day_blur.jpg"
image pool_night = "backgrounds/location_pool_night_blur.jpg"
image pool_water_night = "backgrounds/location_pool_night_water.jpg"
image pool_night02 = "backgrounds/location_pool_night02_blur.jpg"
image pool_night03 = "backgrounds/location_pool_night03_blur.jpg"
image pool_night04 = "backgrounds/location_pool_night04_blur.jpg"
image pool_night05 = "backgrounds/location_pool_night05_blur.jpg"
image changeroom01 = "backgrounds/location_pool_changeroom01.jpg"
image changeroom03 = "backgrounds/location_pool_changeroom03.jpg"
image poolcutscene01 = "backgrounds/location_pool_cutscene01.jpg"
image poolcutscene01b = "backgrounds/location_pool_cutscene02.jpg"
image rescued = "backgrounds/location_pool_ground.jpg"


image art_classroom = "backgrounds/location_school_art_day.jpg"
image art_classroom_b = "backgrounds/location_school_art_day_blur.jpg"
image art_classroom_c = "backgrounds/location_school_art_day_closeup.jpg"
image art_classroom_night = "backgrounds/location_school_art_night.jpg"
image art_classroom_night_b = "backgrounds/location_school_art_night_blur.jpg"
image tattoo_cs01 = "backgrounds/location_tattoo_cutscene01.jpg"
image school_art_cs01 = "backgrounds/location_school_art_cutscene01.jpg"
image school_art_tattoos = "backgrounds/location_school_art_tattoos.jpg"
image music_classroom = "backgrounds/location_school_music_day.jpg"
image music_classroom_b = "backgrounds/location_school_music_day_blur.jpg"
image music_classroom_c = "backgrounds/location_school_music_closeup.jpg"
image music_classroom_night = "backgrounds/location_school_music_night.jpg"
image music_classroom_night_b = "backgrounds/location_school_music_night_blur.jpg"
image science_classroom = "backgrounds/location_school_science_day.jpg"
image science_classroom_b = "backgrounds/location_school_science_day_blur.jpg"
image science_classroom_c = "backgrounds/location_school_science_day_closeup.jpg"
image science_classroom_night = "backgrounds/location_school_science_night.jpg"
image science_classroom_night_b = "backgrounds/location_school_science_night_blur.jpg"
image location_school_science_closeup = "backgrounds/location_school_science_day_closeup.jpg"
image school_science_c02 = "backgrounds/location_school_science_closeup02.jpg"
image school_lounge_b = "backgrounds/location_school_lounge_day_blur.jpg"
image locker_mark = "buttons/locker_list_02.png"
image principle_drawer = "backgrounds/location_school_office_drawer_day.jpg"
image cult_event 1 = "backgrounds/location_school_night_walk01.jpg"
image cult_event 2 = "backgrounds/location_school_night_walk02.jpg"
image cult_event 3 = "backgrounds/location_school_night_walk03.jpg"
image cult_event 4 = "backgrounds/location_school_night_walk04.jpg"
image cult_event 5 = "backgrounds/location_school_lefthall_night_walk01.jpg"
image cult_event 6 = "backgrounds/location_school_lefthall_night_walk02.jpg"
image girl_lockerroom = "backgrounds/location_school_locker_room_broken_day.jpg"
image outside_school_night02a = "backgrounds/location_school_outside_school_night_cutscene01.jpg"
image outside_school_night02b = "backgrounds/location_school_outside_school_night_cutscene02.jpg"
image outside_school_night02c = "backgrounds/location_school_outside_school_night_cutscene03.jpg"
image studyclass01 = "backgrounds/location_school_french_custcene01.jpg"
image studyclass02 = "backgrounds/location_school_french_custcene02.jpg"
image studyclass03 = "backgrounds/location_school_french_custcene03.jpg"
image studyclass04 = "backgrounds/location_school_french_custcene04.jpg"
image studyclass05 = "backgrounds/location_school_french_custcene05.jpg"
image studyclass06 = "backgrounds/location_school_french_custcene06.jpg"
image studyclass07 = "backgrounds/location_school_french_custcene07.jpg"
image studyclass08 = "backgrounds/location_school_french_custcene08.jpg"
image school_office1_b = "backgrounds/location_school_office1_day_blur.jpg"
image school_office2_b = "backgrounds/location_school_office2_day_blur.jpg"
image school_office3_b = "backgrounds/location_school_office3_day_blur.jpg"
image school_office4_b = "backgrounds/location_school_office4_day_blur.jpg"
image location_school_office3_closeup_sex = "backgrounds/location_school_office3_closeup_sex_day.jpg"
image toilet_stall = "backgrounds/location_school_locker_room_broken_stall_day.jpg"
image toilet_stall_night = "backgrounds/location_school_locker_room_broken_stall_night.jpg"
image lockershowers = "backgrounds/location_school_lockershowers_day_blur.jpg"
image cafeteria_b = "backgrounds/location_school_cafeteria_day_blur.jpg"
image stairs = "backgrounds/location_school_second_day_blur.jpg"
image school_computer_b = "backgrounds/location_school_computer_day_blur.jpg"
image lefthall_day = "backgrounds/location_school_lefthall_day_blur.jpg"
image lefthall_night = "backgrounds/location_school_lefthall_night_blur.jpg"
image locker = "backgrounds/location_school_locker_room_day_blur.jpg"
image locker_night = "backgrounds/location_school_locker_room_night_blur.jpg"
image locker_closeup = "backgrounds/location_school_locker_room_closeup.jpg"
image locker_empty = "backgrounds/location_school_locker_room_empty_day.jpg"
image locker_empty_b = "backgrounds/location_school_locker_room_empty_day_blur.jpg"


image office_clear = "backgrounds/location_school_office_day.jpg"
image classroom = "backgrounds/location_school_french_day_blur.jpg"
image classroom_night = "backgrounds/location_school_french_night_blur.jpg"
image gym = "backgrounds/location_school_gym_day_blur.jpg"
image school_fight_cs1 = "backgrounds/location_school_cutscene01.jpg"
image school_fight_cs2 = "backgrounds/location_school_cutscene02.jpg"
image french_class_c = "backgrounds/location_school_french_closeup.jpg"
image computer_room_printer_c = "backgrounds/location_school_computer_closeup_printer.jpg"
image computer_room_c = "backgrounds/location_school_computer_closeup.jpg"
image french_class_cs1 = "backgrounds/location_school_french_custcene01.jpg"
image french_class_cs2 = "backgrounds/location_school_french_custcene02.jpg"
image french_class_cs3 = "backgrounds/location_school_french_custcene03.jpg"
image french_class_cs4 = "backgrounds/location_school_french_custcene04.jpg"
image french_class_cs5 = "backgrounds/location_school_french_custcene05.jpg"
image french_class_cs6 = "backgrounds/location_school_french_custcene06.jpg"
image french_class_cs7 = "backgrounds/location_school_french_custcene07.jpg"
image french_class_cs8 = "backgrounds/location_school_french_custcene08.jpg"
image french_class_cs9 = "backgrounds/location_school_french_cutscene09.jpg"
image french_class_cs10 = "backgrounds/location_school_french_cutscene10.jpg"
image french_class_cs11 = "backgrounds/location_school_french_cutscene11.jpg"
image french_class_cs13 = "backgrounds/location_school_french_cutscene13.jpg"
image french_class_cs14 = "backgrounds/location_school_french_cutscene14.jpg"
image dexter_locker_c = "backgrounds/location_school_locker_dexter_day.jpg"
image dexter_locker_night_c = "backgrounds/location_school_locker_dexter_night.jpg"
image latinas_shower_cs01 = "backgrounds/location_school_lockershowers_cutscene01.jpg"
image latinas_shower_cs02 = "backgrounds/location_school_lockershowers_cutscene02.jpg"
image latinas_shower_cs03 = "backgrounds/location_school_lockershowers_cutscene03.jpg"
image french_office_sex_c_day = "backgrounds/location_school_office1_closeup_sex_day.jpg"
image french_office_sex_c_night = "backgrounds/location_school_office1_closeup_sex_night.jpg"
image french_office_c_day = "backgrounds/location_school_office1_day_closeup.jpg"
image french_office_c_night = "backgrounds/location_school_office1_night_closeup.jpg"
image coach_locker_cs1 = "backgrounds/location_school_gym_cutscene01.jpg"
image coach_locker_cs2 = "backgrounds/location_school_gym_cutscene02.jpg"
image coach_locker_peek_overlay = "backgrounds/location_school_gym_office_peek_overlay.jpg"
image coach_locker_peek = "backgrounds/location_school_gym_office_peek.jpg"
image coach_office_day_b = "backgrounds/location_school_gym_office_day_blur.jpg"
image coach_office_night_b = "backgrounds/location_school_gym_office_night_blur.jpg"
image music_class_cs01 = "backgrounds/location_school_music_cutscene01.jpg"
image music_class_cs02 = "backgrounds/location_school_music_cutscene02.jpg"
image music_class_cs03 = "backgrounds/location_school_music_cutscene03.jpg"
image music_class_cs04 = "backgrounds/location_school_music_cutscene04.jpg"
image music_class_cs05 = "backgrounds/location_school_music_cutscene05.jpg"
image music_class_cs06 = "backgrounds/location_school_music_cutscene06.jpg"
image music_checkout_form = "objects/closeup_card_music01.png"
image locker_judith = "backgrounds/location_school_locker_judith_day.jpg"
image lefthall_c = "backgrounds/location_school_lefthall_closeup.jpg"
image flute = "objects/object_flute_01.png"
image dewitt_office_c_day = "backgrounds/location_school_office2_day_closeup.jpg"
image dewitt_office_c_night = "backgrounds/location_school_office2_night_closeup.jpg"
image dewitt_office_twerk_day = "backgrounds/location_school_office2_Sex_twerk_day.jpg"
image dewitt_office_twerk_night = "backgrounds/location_school_office2_Sex_twerk_night.jpg"
image school_right_hall_b = "backgrounds/location_school_right_hall_day_blur.jpg"
image smith_office_spying = "backgrounds/location_school_office_spying.jpg"
image outside_smith_office = "backgrounds/location_school_third_sideview_day.jpg"
image outside_smith_office_night = "backgrounds/location_school_third_sideview_night.jpg"
image school_hall_third_floor_b = "backgrounds/location_school_third_day_blur.jpg"
image school_hall_third_floor_night_b = "backgrounds/location_school_third_night_blur.jpg"
image assembly_hall_paint01_c = "backgrounds/location_school_assembly_hall_closeup_paint01.jpg"
image assembly_hall_podium_paint = "backgrounds/location_school_assembly_hall_podium_paint.jpg"
image assembly_hall_cs01 = "backgrounds/location_school_assembly_hall_cutscene01.jpg"
image assembly_hall_cs02 = "backgrounds/location_school_assembly_hall_cutscene02.jpg"
image assembly_hall_cs03 = "backgrounds/location_school_assembly_hall_cutscene03.jpg"
image assembly_hall_cs04 = "backgrounds/location_school_assembly_hall_cutscene04.jpg"
image assembly_hall_cs05 = "backgrounds/location_school_assembly_hall_cutscene05.jpg"
image assembly_hall_cs06 = "backgrounds/location_school_assembly_hall_cutscene06.jpg"
image assembly_hall_cs07 = "backgrounds/location_school_assembly_hall_cutscene07.jpg"
image assembly_hall_paint02_c = "backgrounds/location_school_assembly_hall_closeup_paint02.jpg"
image assembly_hall_podium_c = "backgrounds/location_school_assembly_hall_closeup_podium.jpg"
image assembly_hall_c = "backgrounds/location_school_assembly_hall_closeup_podium.jpg"
image smith_office_night_b = "backgrounds/location_school_office_night_blur.jpg"
image assembly_hall_talentshow = "backgrounds/location_school_assembly_hall_talentshow.jpg"
image smith_office_cs01 = "backgrounds/location_school_office_cutscene01.jpg"
image under_podium = "backgrounds/location_school_assembly_hall_under.jpg"
image dewitt_office_sex_day = "backgrounds/location_school_office2_Sex_day.jpg"
image dewitt_office_sex_night = "backgrounds/location_school_office2_Sex_night.jpg"
image dewitt_podium_bj = "backgrounds/location_school_assembly_hall_sex.jpg"
image gym_c = "backgrounds/location_school_gym_closeup.jpg"
image bissette_office_sex_chair_c_night = "backgrounds/location_school_office1_closeup_sex_chair_night.jpg"
image bissette_office_sex_chair_c_day = "backgrounds/location_school_office1_closeup_sex_chair_day.jpg"
image dewitt_office_bj_day = "backgrounds/location_school_office2_bj_day.jpg"
image dewitt_office_bj_night = "backgrounds/location_school_office2_bj_night.jpg"
image paint_trail_01 = Image("objects/object_paint_trail_01.png", xoffset = 140)
image paint_trail_02 = Image("objects/object_paint_trail_02.png", xoffset = 200, yoffset = -140)
image paint_trail_03 = Image("objects/object_paint_trail_03.png", xoffset = -50, yoffset = -78)
image paint_trail_04 = Image("objects/object_paint_trail_04.png", xoffset = -375, yoffset = -110)
image boys_locker_room_backpack_day_b = "backgrounds/location_school_locker_room_backpack_day_blur.jpg"


image jennybedroom_bed = "backgrounds/location_home_jennybedroom_bed.jpg"
image jennycam1 = "backgrounds/location_home_jennybedroom_cam1.jpg"
image jenny_webcam2 = "backgrounds/location_home_jennybedroom_cam2.jpg"
image jennybedroom = "backgrounds/location_home_jennybedroom_day_blur.jpg"
image jennybedroom_clear = "backgrounds/location_home_jennybedroom_night.jpg"
image jennybedroom_night = "backgrounds/location_home_jennybedroom_night_blur.jpg"
image jennybedroom_c_2 = "backgrounds/location_home_jennybedroom_closeup02.jpg"
image bedside01 = "backgrounds/location_home_jennytable.jpg"


image tattoo_indoor_b = "backgrounds/location_tattoo_indoor_day_blur.jpg"


image windowerikmorning01 = "backgrounds/location_telescope_erik_morning01.jpg"
image windowerikmorning02 = "backgrounds/location_telescope_erik_morning02.jpg"
image windowerikday 1 = "backgrounds/location_telescope_erik_day01.jpg"
image windowerikday 2 = "backgrounds/location_telescope_erik_day02.jpg"
image windowerikday 3a = "backgrounds/location_telescope_erik_day03a.jpg"
image windowerikday 3b = "backgrounds/location_telescope_erik_day03b.jpg"
image windowerikday 3c = "backgrounds/location_telescope_erik_day03c.jpg"
image windowerikday 3d = "backgrounds/location_telescope_erik_day03d.jpg"
image windowerikday 3e = "backgrounds/location_telescope_erik_day03e.jpg"
image windowerikday 3f = "backgrounds/location_telescope_erik_day03f.jpg"
image windowerikday 3g = "backgrounds/location_telescope_erik_day03g.jpg"
image windowerikday 3h = "backgrounds/location_telescope_erik_day03h.jpg"
image windowerikday 3i = "backgrounds/location_telescope_erik_day03i.jpg"
image windowerikday 3j = "backgrounds/location_telescope_erik_day03j.jpg"
image windowerikday 3k = "backgrounds/location_telescope_erik_day03k.jpg"
image windowerikday 3l = "backgrounds/location_telescope_erik_day03l.jpg"
image windowerikday 3m = "backgrounds/location_telescope_erik_day03m.jpg"
image windowerikday 4a = "backgrounds/location_telescope_erik_day04a.jpg"
image windowerikday 4b = "backgrounds/location_telescope_erik_day04b.jpg"
image windoweriknight01 = "backgrounds/location_telescope_erik_night01.jpg"
image windoweriknight02 = "backgrounds/location_telescope_erik_night02.jpg"
image windowmiamorning01 = "backgrounds/location_telescope_mia_morning01.jpg"
image windowmiamorning02 = "backgrounds/location_telescope_mia_morning02.jpg"
image windowmiaday 1 = "backgrounds/location_telescope_mia_day01.jpg"
image windowmiaday 2 = "backgrounds/location_telescope_mia_day02.jpg"
image windowmiaday 3 = Animation(
    "backgrounds/location_telescope_mia_day03a.jpg",
    0.5,
    "backgrounds/location_telescope_mia_day03b.jpg",
    0.5)
image windowmianight01 = "backgrounds/location_telescope_mia_night01.jpg"
image windowmianight02 = "backgrounds/location_telescope_mia_night02.jpg"
image windowmianight03a = "backgrounds/location_telescope_mia_night03a.jpg"
image windowmianight03b = "backgrounds/location_telescope_mia_night03b.jpg"
image windowmianight03c = "backgrounds/location_telescope_mia_night03c.jpg"
image windowmianight03d = "backgrounds/location_telescope_mia_night03d.jpg"
image windowmrsjmorning01 = "backgrounds/location_telescope_mrsj_morning01.jpg"
image windowmrsjmorning01b = "backgrounds/location_telescope_mrsj_morning01b.jpg"
image windowmrsjmorning01c = "backgrounds/location_telescope_mrsj_morning01c.jpg"
image windowmrsjmorning01d = "backgrounds/location_telescope_mrsj_day02.jpg"
image windowmrsjday01 = "backgrounds/location_telescope_mrsj_day01.jpg"
image windowmrsjday02 = "backgrounds/location_telescope_mrsj_day02.jpg"
image windowmrsjday 3a = "backgrounds/location_telescope_mrsj_day03a.jpg"
image windowmrsjday 3b = "backgrounds/location_telescope_mrsj_day03b.jpg"
image windowmrsjday 3c = "backgrounds/location_telescope_mrsj_day03c.jpg"
image windowmrsjday 3c-d = Animation(
    "backgrounds/location_telescope_mrsj_day03c.jpg",
    0.5,
    "backgrounds/location_telescope_mrsj_day03d.jpg",
    0.5)
image windowmrsjday 4a = "backgrounds/location_telescope_mrsj_day04a.jpg"
image windowmrsjday 4b = "backgrounds/location_telescope_mrsj_day04b.jpg"
image windowmrsjday 4c = "backgrounds/location_telescope_mrsj_day04c.jpg"
image windowmrsjnight01 = "backgrounds/location_telescope_mrsj_night01.jpg"
image windowmrsjnight02 = "backgrounds/location_telescope_mrsj_night02.jpg"
image windowmrsjnight03 = "backgrounds/location_telescope_mrsj_night03.jpg"
image windowmrsjnight04 = "backgrounds/location_telescope_mrsj_night04.jpg"
image windowbackyardday01 = "backgrounds/location_telescope_backyard_day01.jpg"
image windowbackyardday02 = "backgrounds/location_telescope_backyard_day02.jpg"
image windowbackyardday03 = "backgrounds/location_telescope_backyard_day03.jpg"
image windowbackyardday04 = "backgrounds/location_telescope_backyard_day04.jpg"
image windowbackyardnight01 = "backgrounds/location_telescope_backyard_night01.jpg"
image windowbackyardnight02a = "backgrounds/location_telescope_backyard_night02a.jpg"
image windowbackyardnight02b = "backgrounds/location_telescope_backyard_night02b.jpg"
image windowbackyardnight02c = "backgrounds/location_telescope_backyard_night02c.jpg"
image windowhelenmorning01 = "backgrounds/location_telescope_helen_morning01.jpg"
image windowhelenday01 = "backgrounds/location_telescope_helen_day01.jpg"
image windowhelennight01 = "backgrounds/location_telescope_helen_night01.jpg"
image windowhelennight02 = "backgrounds/location_telescope_helen_night02.jpg"
image telescope_caught 1 = "backgrounds/location_home_bedroom_caught_01.jpg"
image telescope_caught 2 = "backgrounds/location_home_bedroom_caught_02.jpg"
image telescope_caught 3 = "backgrounds/location_home_bedroom_caught_03.jpg"
image telescope_caught 4 = "backgrounds/location_home_bedroom_caught_04.jpg"


image trailer_interior_c = "backgrounds/location_trailer_day_closeup.jpg"
image trailer_interior_c_night = "backgrounds/location_trailer_night_closeup.jpg"
image trailer_counter = "characters/crystal/crystal_sex_anim_overlay.png"
image trailer_counter_night = "characters/crystal/crystal_sex_anim_overlay_night.png"


image treehouse = "backgrounds/location_treehouse_day.jpg"
image treehouse_b = "backgrounds/location_treehouse_day_blur.jpg"
image treehouse_night = "backgrounds/location_treehouse_night.jpg"
image treehouse_night_b = "backgrounds/location_treehouse_night_blur.jpg"
image treehouse_inside = "backgrounds/location_treehouse_inside_day.jpg"
image treehouse_inside_b = "backgrounds/location_treehouse_inside_day_blur.jpg"
image treehouse_inside_night = "backgrounds/location_treehouse_inside_night.jpg"
image treehouse_inside_night_b = "backgrounds/location_treehouse_inside_night_blur.jpg"




image lair_seasucc = "backgrounds/location_lair_seasucc.jpg"




image office = ConditionSwitch(
    "not M_ross.is_set('smith office painting')", "backgrounds/location_school_office_day_blur.jpg",
    "True", "backgrounds/location_school_office_painting_day_blur.jpg",
    )
image office_night = ConditionSwitch(
    "not M_ross.is_set('smith office painting')", "backgrounds/location_school_office_night_blur.jpg",
    "True", "backgrounds/location_school_office_painting_night_blur.jpg",
    )



image weightlifting03 = ConditionSwitch(
    "not L_gym.is_here(M_kevin)", "backgrounds/location_gym_minigame04c_solo.jpg",
    "player.stats.str() >= 7", "backgrounds/location_gym_minigame04c_heavy.jpg",
    "player.stats.str() >= 3", "backgrounds/location_gym_minigame04c_medium.jpg",
    "True", "backgrounds/location_gym_minigame04c.jpg")

image weightlifting04 = ConditionSwitch(
    "not L_gym.is_here(M_kevin)", "backgrounds/location_gym_minigame04d_solo.jpg",
    "True", "backgrounds/location_gym_minigame04d.jpg")



image location_trailer_bedroom_day = ConditionSwitch(
    "M_roxxy.finished_state(S_roxxy_get_oil)", "backgrounds/location_trailer_bedroom_trophy_day.jpg",
    "True", "backgrounds/location_trailer_bedroom_day.jpg",
    )

image location_trailer_bedroom_night = ConditionSwitch(
    "M_roxxy.finished_state(S_roxxy_get_oil)", "backgrounds/location_trailer_bedroom_trophy_night.jpg",
    "True", "backgrounds/location_trailer_bedroom_night.jpg",
    )

image location_trailer_bedroom_day_blur = ConditionSwitch(
    "M_roxxy.finished_state(S_roxxy_get_oil)", "backgrounds/location_trailer_bedroom_trophy_day_blur.jpg",
    "True", "backgrounds/location_trailer_bedroom_day_blur.jpg",
    )

image location_trailer_bedroom_night_blur = ConditionSwitch(
    "M_roxxy.finished_state(S_roxxy_get_oil)", "backgrounds/location_trailer_bedroom_trophy_night_blur.jpg",
    "True", "backgrounds/location_trailer_bedroom_night_blur.jpg",
    )



image coach_locker = Composite(
    (1024, 768),
    (0,0), ConditionSwitch("game.timer.is_dark()", "backgrounds/location_school_locker_coach_night.jpg", "True", "backgrounds/location_school_locker_coach_day.jpg"),
    (431,62), ConditionSwitch("M_bissette.is_state(S_bissette_roxxy_pom_poms) and not player.has_item('pompoms')", "objects/object_pompom_01.png", "True", Null()),
    )

image eve_locker = Composite(
    (1024, 768),
    (0,0), ConditionSwitch("game.timer.is_dark()", "backgrounds/location_school_locker_eve_night.jpg", "True", "backgrounds/location_school_locker_eve_day.jpg"),
    (316,457), ConditionSwitch("M_ross.is_set('talked with chad') and not player.has_picked_up_item('eve_drawing')", "objects/object_drawing_01.png", "True", Null()),
    )

image old_mia_locker = Composite(
    (1024, 768),
    (0,0), ConditionSwitch("game.timer.is_dark()", "backgrounds/location_school_locker_mia_night.jpg", "True", "backgrounds/location_school_locker_mia_day.jpg"),
    )

image ronda_locker = Composite(
    (1024, 768),
    (0,0), ConditionSwitch("game.timer.is_dark()", "backgrounds/location_school_locker_ronda_night.jpg", "True", "backgrounds/location_school_locker_ronda_day.jpg"),
    )

image dexter_locker = Composite(
    (1024, 768),
    (0,0), ConditionSwitch("game.timer.is_dark()", "backgrounds/location_school_locker_dexter_night.jpg", "True", "backgrounds/location_school_locker_dexter_day.jpg"),
    (725,540), ConditionSwitch("M_bissette.is_set('dexters book search') and not player.has_item('quick_mafs')", ConditionSwitch("game.timer.is_dark()", "objects/object_book_02_night.png", "True", "objects/object_book_02.png"), "True", Null()),
    )

image old_kevin_locker = Composite(
    (1024, 768),
    (0,0), ConditionSwitch("game.timer.is_dark()", "backgrounds/location_school_locker_kevin_night.jpg", "True", "backgrounds/location_school_locker_kevin_day.jpg"),
    )

image annie_locker = Composite(
    (1024, 768),
    (0,0), ConditionSwitch("game.timer.is_dark()", "backgrounds/location_school_locker_annie_night.jpg", "True", "backgrounds/location_school_locker_annie_day.jpg"),
    )

image old_roxxy_locker = Composite(
    (1024, 768),
    (0,0), ConditionSwitch("game.timer.is_dark()", "backgrounds/location_school_locker_roxxy_night.jpg", "True", "backgrounds/location_school_locker_roxxy_day.jpg"),
    )

image judith_locker = Composite(
    (1024, 768),
    (0,0), ConditionSwitch("game.timer.is_dark()", "backgrounds/location_school_locker_judith_night.jpg", "True", "backgrounds/location_school_locker_judith_day.jpg"),
    (394,607), ConditionSwitch("M_okita.is_state(S_okita_picture_taken) and not player.has_item('judith_glasses')", "objects/object_glasses_01.png", "True", Null()),
    (584,406), ConditionSwitch("M_dewitt.is_state(S_dewitt_judith_locker_search) and not player.has_item('broken_flute')", "objects/object_flute_01.png", "True", Null()),
    )



image libraryshelf = Composite(
    (1024, 768),
    (0,0), "library_shelf",
    (742,416), "buttons/book_01.png",
    (190,453), ConditionSwitch("M_bissette.get_state() == S_bissette_get_dictionary and not player.has_item(\"french_dictionary\")", "buttons/book_04.png", "True", Null()),
    (234,110), ConditionSwitch("not M_diane.finished_state(S_diane_check_bookshelf)", "buttons/book_02.png", "True", Null()),
    (406,440), ConditionSwitch("M_erik.is_state(S_erik_learn_fetch, S_erik_learn_get_kamasutra)" , "buttons/book_03.png", "True", Null()),
    (836,108), ConditionSwitch("not player.has_item(\"old_book\")", "buttons/book_05.png", "True", Null()),
    )


image bedroom = ConditionSwitch(
    "M_player.get('pc_fixed')", "backgrounds/location_home_bedroom_day_blur.jpg",
    "True", "backgrounds/location_home_bedroom_broken_day_blur.jpg",
    )
image bedroom_night = ConditionSwitch(
    "M_player.get('pc_fixed')", "backgrounds/location_home_bedroom_night_blur.jpg",
    "True", "backgrounds/location_home_bedroom_broken_night_blur.jpg",
    )


image hospital_cabinet_filled = Composite(
    (1024,768),
    (0,0), "backgrounds/location_hospital_cabinet_any.jpg",
    (98,173), "objects/object_pharmacy_01.png",
    (486,207), "objects/object_pharmacy_02.png",
    (770,226), "objects/object_pharmacy_03.png",
    (148,469), "objects/object_pharmacy_04.png",
    (596,466), "objects/object_pharmacy_06.png",
    (732,457), "objects/object_pharmacy_07.png",
    )
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
