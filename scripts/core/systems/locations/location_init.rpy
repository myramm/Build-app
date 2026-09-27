init -3 python:
    L_map = Location("Town Map", locked=True)
    L_NULL = Location("NULL", locked=True)

    L_apt        = Location('Apartments', background='apt_front', parents=L_map, ref=True, locked=True)
    L_apt_lobby  = Location('Lobby', background='apt_lobby', parents=L_apt, ref=True)
    L_apt_lift   = Location('Elevator', background='apt_lift',  parents=L_apt_lobby, ref=True)
    L_apt_hall1  = Location('First Floor', background='apt_hall1', parents=L_apt_lobby, ref=True)
    L_apt_hall2  = Location('Second Floor', background='apt_hall2', parents=L_apt_lift, ref=True)
    L_apt_hall3  = Location('Third Floor', background='apt_hall3', parents=L_apt_lift, ref=True)
    L_apt_other  = Location('Unknown', parents=L_apt, ref=True) 

    L_liu_lounge = Location('Livingroom', background='liu_lounge', parents=L_apt_hall2, ref=True, locked=True)
    L_liu_bedroom = Location('Bedroom', background=liu_bedroom_bg, parents=L_liu_lounge, ref=True)

    L_maria_lounge = Location('Livingroom', background='maria_lounge', parents=L_apt_hall3, ref=True, locked=True)
    L_maria_bedroom = Location('Bedroom', background='maria_bedroom', parents=L_maria_lounge, ref=True)

    L_tina_lounge = Location('Livingroom', background='tina_lounge', parents=L_apt_hall3, ref=True, locked=True)
    L_tina_bed2 = Location('Becca\'s Room', background='tina_becca_bedroom', parents=L_tina_lounge, ref=True, locked=True)


    L_school_front = Location("School Frontyard", background="school_frontyard", parents=L_map, locked=True, background_fn=school_frontyard_background)
    L_school_hall = Location("School Hall", background="school", parents=L_school_front)

    L_school_frenchclassroom = Location("French Classroom", background="school_french", parents=L_school_hall)
    L_school_scienceclassroom = Location("Science Classroom", background="school_science", parents=L_school_hall)
    L_school_musicclassroom = Location("Music Classroom", background="school_music", parents=L_school_hall)
    L_school_track = Location("School Courtyard", background="school_gym", parents=L_school_hall)
    L_school_lefthallway = Location("School Left Hallway", background="school_lefthall", parents=L_school_hall)
    L_school_floor2 = Location("School Second Floor", background="school_second", parents=L_school_hall)
    L_school_righthallway = Location("School Right Hallway", background="school_right_hall", parents=L_school_hall)
    L_school_locker_MC = Location("School Locker", background="school_locker_mc", parents=L_school_hall)

    L_school_girlsroom = Location("School Girl's Lockerroom", background="school_locker_room_broken", parents=L_school_lefthallway, locked=True)
    L_school_boysroom = Location("Boy's Lockerroom", background="school_locker_room", parents=L_school_lefthallway)
    L_school_locker_roxxy = Location("Roxxy's Locker", background="school_locker_roxxy", parents=L_school_lefthallway, locked=True)
    L_school_locker_judith = Location("Judith's Locker", background="school_locker_judith", parents=L_school_lefthallway, locked=True)
    L_school_artclassroom = Location("Art Classroom", background="school_art", parents=L_school_lefthallway)
    L_school_utilitycloset = Location("Utility Closet", background="", parents=L_school_lefthallway, locked=True)

    L_school_shower = Location("Boy's Locker Shower", background="school_lockershowers", parents=L_school_boysroom)
    L_school_stall = Location("Bathroom Stall", background="school_locker_room_broken_stall", parents=L_school_girlsroom)

    L_school_assemblyhall = Location("Assembly Hall", background="school_assembly_hall", parents=L_school_righthallway, background_fn=school_assemblyhall_background)
    L_school_bridgetoffice = Location("Coach Bridget's Office", background="school_gym_office", parents=L_school_righthallway)
    L_school_locker_annie = Location("Annie's Locker", background="school_locker_annie", parents=L_school_righthallway, locked=True)
    L_school_locker_eve = Location("Eve's Locker", background="school_locker_eve", parents=L_school_righthallway, locked=True)
    L_school_locker_dexter = Location("Dexter's Locker", background="school_locker_dexter", parents=L_school_righthallway, locked=True)
    L_school_locker_erik = Location("Erik's Locker", background="school_locker_erik", parents=L_school_righthallway, locked=True)
    L_school_locker_kevin = Location("Kevin's Locker", background="school_locker_kevin", parents=L_school_righthallway, locked=True)
    L_school_locker_ronda = Location("Ronda's Locker", background="school_locker_ronda", parents=L_school_righthallway, locked=True)
    L_school_locker_mia = Location("Mia's Locker", background="school_locker_mia", parents=L_school_righthallway, locked=True)

    L_school_computerlab = Location("Computer Lab", background="school_computer", parents=L_school_floor2)
    L_school_cafeteria = Location("Cafeteria", background="school_cafeteria", parents=L_school_floor2)
    L_school_teacherslounge = Location("Teacher's Lounge", background="school_lounge", parents=L_school_floor2)
    L_school_floor3 = Location("School Third Floor", background="school_third", parents=L_school_floor2)

    L_school_bissetteoffice = Location("Mrs Bissette's Office", background="school_office1", parents=L_school_floor3)
    L_school_dewittoffice = Location("Mrs Dewitt's Office", background="school_office2", parents=L_school_floor3)
    L_school_rossoffice = Location("Mrs Ross' Office", background="school_office3", parents=L_school_floor3)
    L_school_okitaoffice = Location("Mrs Okita's Office", background="school_office4", parents=L_school_floor3)
    L_school_smithoffice = Location("Principal Smith's Office", background="school_office", parents=L_school_floor3)


    L_diane_yard = Location("Diane's Front Yard", background="diane_front", parents=L_map, locked=True)
    L_diane_garden = Location("Diane's Garden", background="diane_garden", parents=L_diane_yard, background_fn=dianes_garden_background)
    L_diane_home = Location("Diane's Lobby", background="diane_entrance", parents=L_diane_yard, locked=True)
    L_diane_kitchen = Location("Diane's Kitchen", background="diane_kitchen", parents=[L_diane_garden, L_diane_home], locked=True)
    L_diane_bedroom = Location("Diane's Bedroom", background="diane_bedroom", parents=L_diane_home)
    L_diane_shed = Location("Diane's Shed", background="diane_shed01", parents=L_diane_garden, locked=True)


    L_diane_barn_building = Location("Diane's Barn Building", background="barn_build_frontyard", parents=L_map)
    L_diane_barn = Location("Diane's Barn", background="barn_frontyard", parents=L_map)
    L_diane_barn_interior = Location("Diane's Barn Interior", background="barn", parents=L_diane_barn)
    L_diane_barn_garden = Location("Diane's Barn Garden", background="barn_garden", parents=L_diane_barn)


    L_home = Location("Home Front", background="home_front", parents=L_map)
    L_home_mailbox = Location("Mailbox", background="player_mailbox", parents=L_home)
    L_home_garage = Location("Garage", background="home_garage", parents=L_home)
    L_home_car = Location("Car Engine", background="home_garage_car", parents=L_home_garage)
    L_home_entrance = Location("Entrance", background="home_entrance", parents=L_home)
    L_home_kitchen = Location("Kitchen", background="home_kitchen", parents=L_home_entrance)
    L_home_diningroom = Location("Dining Room", background="home_diningroom", parents=L_home_kitchen)
    L_home_backyard = Location("Backyard", background="home_backyard", parents=L_home_diningroom)
    L_home_livingroom = Location("Living Room", background="home_livingroom", parents=L_home_entrance)
    L_home_basement = Location("Basement", background="home_basement", parents=L_home_livingroom)
    L_home_mombedroom = Location("Master Bedroom", background="home_debbiebedroom", parents=L_home_livingroom, locked=True)
    L_home_hallway = Location("Hallway", background="home_hallway", parents=L_home_entrance)
    L_home_shower = Location("Shower", background="home_shower", parents=L_home_hallway)
    L_home_attic = Location("Attic", background="home_attic", parents=L_home_hallway, locked=True)
    L_home_sisbedroom = Location("Upstairs Bedroom", background="home_jennybedroom", parents=L_home_hallway, locked=True, background_fn=upstairs_bedroom_background)
    L_home_bedroom = Location("Bedroom", background="home_bedroom", parents=[L_home_hallway, L_map])


    L_erikhouse = Location("Erik's House", background="erik_house", parents=L_map, locked=True)
    L_erikhouse_mailbox = Location("Erik's Mailbox", background="erik_mailbox", parents=L_erikhouse)
    L_erikhouse_backyard = Location("Erik's Backyard", background="erik_house_backyard", parents=L_erikhouse)
    L_erikhouse_entrance = Location("Erik's House Entrance", background="erik_house_inside", parents=[L_erikhouse, L_erikhouse_backyard])
    L_erikhouse_basement = Location("Erik's Basement", background="erik_basement01", parents=L_erikhouse_entrance)
    L_erikhouse_backroom = Location("Erik's Basement Backroom", background="erik_basement_back", parents=L_erikhouse_basement)
    L_erikhouse_aquarium = Location("Erik's Aquarium", background="erik_basement_aquarium", parents=L_erikhouse_backroom)
    L_erikhouse_erikroom = Location("Erik's Room", background="erik_house_bedroom", parents=L_erikhouse_entrance)
    L_erikhouse_mrsjroom = Location("Mrs Johnson's Room", background="erik_house_upstairs", parents=L_erikhouse_entrance)


    L_miahouse = Location("Mia's House", background="mia", parents=L_map, locked=True)
    L_miahouse_mailbox = Location("Mia's Mailbox", background="mia_mailbox", parents=L_miahouse, background_fn=mias_mailbox_background)
    L_miahouse_entrance = Location("Mia's House Entrance", background="mia_house", parents=L_miahouse, background_fn=mias_house_entrance_background)
    L_miahouse_upstairs = Location("Mia's House Upstairs", background="mia_house_upstairs", parents=L_miahouse_entrance)
    L_miahouse_miaroom = Location("Mia's Bedroom", background="mia_bedroom", parents=L_miahouse_upstairs)
    L_miahouse_helensbedroom = Location("Helen's Bedroom", background="mia_house_helen", parents=L_miahouse_upstairs)
    L_miahouse_haroldsoffice = Location("Harold's House Office", background="mia_house_office", parents=L_miahouse_upstairs)
    L_miahouse_lockedroom = Location("Helen's Locked Room", background="mia_house_locked", parents=L_miahouse_upstairs)


    L_church_front = Location("Church Front", background="church_outside", parents=L_map, locked=True)
    L_church = Location("Church", background="church", parents=L_church_front, background_fn=church_background)
    L_church_confessional_right = Location("Church Confessional Right", background="church_confession", parents=L_church)
    L_church_confessional_left = Location("Church Confessional Left", background="church_confession", parents=L_church)
    L_church_stairs = Location("Church Stairs", background="church_stairs", parents=L_church)
    L_church_bell = Location("Church Cloister Bell", background="church_bell", parents=L_church_stairs)
    L_church_angelica = Location("Angelica's Room", background="church_nun", parents=L_church_stairs)
    L_church_graveyard = Location("Church Graveyard", background="church_graveyard", parents=L_church_front, background_fn=church_graveyard_background)
    L_church_crypt = Location('Crypt', background='crypt', parents=L_church_graveyard, ref=True)


    L_forest = Location("Forest", background="forest", parents=L_map, locked=True)
    L_waterfall = Location("Waterfall", background="forest_waterfall", parents=L_forest)
    L_cave = Location("Cave", background="forest_cave", parents=L_waterfall)


    L_gym_front = Location("Gym Front", background="gym_front", parents=L_map, locked=True)
    L_gym = Location("Gym", background="gym", parents=L_gym_front)
    L_yoga_room = Location("Yoga Room", background="gym_yoga", parents=L_gym)


    L_mall_parking_lot = Location("Mall Parking Lot", background="mall_frontyard", parents=L_map, locked=True)
    L_mall = Location("Mall", background="mall", parents=L_mall_parking_lot, background_fn=mall_background)
    L_movie_theatre = Location("Movie Theatre", background="mall_movie_main", parents=L_mall)
    L_mall_toilets = Location("Mall Toilets", background="mall_washroom", parents=L_mall, background_fn=mall_toilets_background)
    L_mall_toilets_stall = Location("Mall Toilets Stall", background="mall_washroom_stall", parents=L_mall_toilets)
    L_comicstore = Location("Comic Store", background="mall_comic", parents=L_mall, background_fn=comic_store_background)
    L_consumr = Location("Consumr", background="mall_consumr", parents=L_mall)
    L_mall_floor2 = Location("Mall Second Floor", background="mall_upstairs", parents=L_mall)
    L_mall_photobooth = Location("Mall Photo Booth", background="mall_upstairs_booth", parents=L_mall_floor2)
    L_cupid = Location("Cupid", background="mall_cupid", parents=L_mall_floor2)
    L_cupid_dressroom = Location("Cupid Dressingroom", background="mall_cupid_stall", parents=L_cupid)
    L_pink = Location("Pink", background="pink", parents=L_mall_floor2, background_fn=mall_pink_background)


    L_donutshop = Location("Donut Shop", background="donut", parents=L_map, locked=True)
    L_donutshop_interior = Location("Donut Shop Interior", background="donut_inside", parents=L_donutshop)


    L_pizzeria_exterior = Location("Pizzeria Exterior", background="pizza_outside", parents=L_map, locked=True)
    L_pizzeria_interior = Location("Pizzeria Interior", background="pizza", parents=L_pizzeria_exterior)
    L_pizzeria_kitchen = Location("Pizzeria Kitchen", background="pizza_kitchen", parents=L_pizzeria_interior, background_fn=pizzeria_kitchen_background)
    L_pizzeria_storage = Location("Pizzeria Storage", background="pizza_storage", parents=L_pizzeria_kitchen)


    L_trailerpark = Location("Trailer Park", background="trailer_park", parents=L_map, locked=True)
    L_trailer = Location("Trailer", background="trailer", parents=L_trailerpark)
    L_trailer_shack = Location("Trailer Shack", background="trailer_shack", parents=L_trailerpark)
    L_trailer_tractor = Location("Tractor", background="trailer_tractor", parents=L_trailerpark)
    L_trailer_shootingrange = Location("Shooting Range", background="trailer_tractor", parents=L_trailer_tractor)
    L_trailer_shack_interior = Location("Trailer Shack Interior", background="trailer_shack_inside", parents=L_trailer_shack, locked=True)
    L_trailer_interior = Location("Trailer Interior", background="trailer_interior", parents=L_trailerpark)
    L_trailer_bedroom = Location("Trailer Bedroom", background="trailer_bedroom", parents=L_trailer_interior, background_fn=trailer_bedroom_background)


    L_treehouse = Location("Treehouse", background="treehouse", parents=L_map, locked=True)
    L_treehouse_ladder = Location("Treehouse Ladder", background="treehouse_ladder", parents=L_treehouse)
    L_treehouse_interior = Location("Treehouse Interior", background="treehouse_inside", parents=L_treehouse_ladder)


    L_police_front = Location("Police Parking Lot", background="police_frontyard", parents = L_map, locked=True)
    L_police_lobby = Location("Police Lobby", background="police_lobby", parents=L_police_front)
    L_police_office = Location("Police Office", background="police_office", parents=L_police_lobby)
    L_police_basement = Location("Police Basement", background="police_basement", parents=L_police_lobby, background_fn=police_basement_background)


    L_hospital = Location("Hospital", background="hospital_front", parents=L_map, locked=True)
    L_hospital_lobby = Location("Hospital Lobby", background="hospital_first", parents=L_hospital)
    L_hospital_elevator = Location("Hospital Elevator", background="hospital_elevator", parents=L_hospital_lobby)
    L_hospital_basement = Location("Hospital Basement", background= "hospital_basement", parents=L_hospital_elevator, locked=True)
    L_hospital_lab = Location("Hospital Laboratory", background= "hospital_lab", parents=L_hospital_basement, locked=True)
    L_hospital_floor2 = Location("Hospital 2nd Floor", background="hospital_second", parents=L_hospital_elevator)
    L_hospital_room = Location("Hospital 2nd Floor Room", background="hospital_room", parents=L_hospital_floor2)
    L_hospital_room_bathroom = Location("Hospital 2nd Floor Bathroom", background="hospital_bathroom", parents=L_hospital_room)
    L_hospital_storageroom = Location("Hospital Storage Room", background="hospital_storage", parents=L_hospital_floor2)
    L_hospital_storagecabinet = Location("Hospital Storage Cabinet", background="hospital_cabinet", parents=L_hospital_storageroom)
    L_hospital_floor3 = Location("Hospital 3rd Floor", background="hospital_third", parents=L_hospital_elevator)
    L_hospital_recovery1 = Location("Recovery Room", background="hospital_baby", parents=L_hospital_floor3)
    L_hospital_recovery2 = Location("Recovery Room", background="hospital_baby", parents=L_hospital_floor3)
    L_hospital_recovery3 = Location("Recovery Room", background="hospital_baby", parents=L_hospital_floor3)
    L_hospital_recovery4 = Location("Recovery Room", background="hospital_baby", parents=L_hospital_floor3)
    L_hospital_recovery1.display_name += ' #1'
    L_hospital_recovery2.display_name += ' #2'
    L_hospital_recovery3.display_name += ' #3'
    L_hospital_recovery4.display_name += ' #4'


    L_library_front = Location("Library Front", background="library_front", parents=L_map, locked=True)
    L_library = Location("Library", background="library", parents=L_library_front)
    L_library_bookshelf = Location("Library Bookshelf", background="library_shelf", parents=L_library)
    L_library_backroom = Location("Library Backroom", background="library_backroom", parents=L_library, background_fn=library_backroom_background)
    L_library_meetingroom = Location("Library Meeting Room", background="library_meeting", parents=L_library) 


    L_park = Location("Park", background="park", parents=L_map, locked=True)
    L_park_fountain = Location("Park Fountain", background="park_fountain", parents=L_park)
    L_park_bushes = Location("Park Bushes", background="park_bushes", parents=L_park)
    L_park_bushesbag = Location("Park Bushes Bag", background="park_bag", parents=L_park_bushes)


    L_tattooparlor = Location("Tattoo Parlor", background="tattoo", parents=L_map, locked=True, background_fn=tattoo_parlor_front_background)
    L_tattooparlor_interior = Location("Tattoo Parlor Interior", background="tattoo_indoor", parents=L_tattooparlor, background_fn=tattoo_parlor_interior_background)
    L_tattooparlor_garage = Location("Tattoo Parlor Garage", background="tattoo_garage", parents=L_tattooparlor, locked=True, background_fn=tattoo_parlor_garage_background)
    L_tattooparlor_fire_escape = Location("Tattoo Parlor Fire Escape", background="tattoo_garagetop", parents=L_tattooparlor_garage, background_fn=tattoo_parlor_fireescape_background)
    L_tattooparlor_roof = Location("Tattoo Parlor Roof", background="tattoo_rooftop", parents=L_tattooparlor_fire_escape, background_fn=tattoo_parlor_roof_background, locked=True)
    L_tattooparlor_apartment = Location("Tattoo Parlor Apartment", background="tattoo_apartment", parents=L_tattooparlor_fire_escape)
    L_tattooparlor_bedroom = Location("Tattoo Parlor Bedroom", background="tattoo_bedroom", parents=L_tattooparlor_apartment)
    L_tattooparlor_bathroom = Location("Tattoo Parlor Bathroom", background="tattoo_bathroom", parents=L_tattooparlor_bedroom)
    L_tattooparlor_alley = Location("Tattoo Parlor Alleyway", background="tattoo_alley", parents=L_tattooparlor, background_fn=tattoo_parlor_alley_background)
    L_tattooparlor_tent = Location("Tattoo Parlor Tent", background="tattoo_tent", parents=L_tattooparlor_roof)


    L_dealership = Location("Dealership", background="dealership_front", parents=L_map, locked=True)
    L_dealership_showroom = Location("Dealership Showroom", background="dealership_indoor", parents=L_dealership)
    L_dealership_garage = Location("Dealership Garage", background="dealership_garage", parents=L_dealership_showroom)
    L_dealership_lounge = Location("Dealership Lounge", background="dealership_lounge", parents=L_dealership_showroom)
    L_dealership_office = Location("Dealership Office", background="dealership_office", parents=L_dealership_showroom)


    L_beachhouse_front = Location("Beach House Front", background="beach_house", parents=L_map, locked=True)
    L_beachhouse_entrance = Location("Beach House Entrance", background="beach_house_entrance", parents=L_beachhouse_front)
    L_beachhouse_kitchen = Location("Beach House Kitchen", background="beach_house_kitchen", parents=L_beachhouse_entrance)
    L_beachhouse_bedroom = Location("Beach House Bedroom", background="beach_house_bedroom", parents=L_beachhouse_entrance)
    L_beachhouse_patio = Location("Beach House Patio", background="beach_house_patio", parents=L_beachhouse_bedroom)


    L_beach = Location("Beach", background="beach", parents=[L_map, L_beachhouse_kitchen], locked=True)
    L_beach_water = Location("Beach Water", background="beach_water", parents=L_beach)
    L_beach_showers = Location("Beach Showers", background="beach_shower", parents=L_beach_water)
    L_beach_cabin = Location("Beach Cabin", background="beach_cabin", parents=L_beach_water)
    L_beach_tower = Location("Beach Tower", background="beach_tower", parents=L_beach)
    L_beach_island = Location("Beach Island", background="beach_island", parents=L_beach)
    L_beach_island_chest = Location("Treasure Chest", background="beach_treasure", parents=L_beach_island)


    L_smith_front = Location("Smith's Frontyard", background="smith_frontyard", parents=L_map, locked=True)
    L_smith_entrance = Location("Smith's Entrance", background="smith_entrance", parents=L_smith_front)
    L_smith_hallway = Location("Smith's Hallway", background="smith_hallway", parents=L_smith_entrance)
    L_smith_bedroom = Location("Smith's Bedroom", background="smith_bedroom", parents=[L_smith_hallway, L_smith_front])
    L_smith_basement = Location("Smith's Basement", background="smith_basement", parents=L_smith_entrance, locked=True)


    L_annie_front = Location("Annie's House Front", background="annie_frontyard", parents=L_map, locked=True)
    L_annie_livingroom = Location("Annie's House Livingroom", background="annie_livingroom", parents=L_annie_front)
    L_annie_daycare = Location("Annie's House Daycare", background="annie_daycare", parents=L_annie_front)


    L_boat_bridge = Location("Boat Bridge", background="boat", parents=L_map, locked=True)
    L_boat_cabin = Location("Boat Cabin", background="boat_interior", parents=L_boat_bridge)


    L_rump_front = Location("Mayor Rump's Frontyard", background="rump_front", parents=L_map, locked=True)
    L_rump_lobby = Location("Mayor Rump's Lobby", background="rump_entrance", parents=L_rump_front, locked=True)
    L_rump_kitchen = Location("Mayor Rump's Kitchen", background="rump_kitchen", parents=L_rump_lobby)
    L_rump_back = Location("Mayor Rump's Backyard", background="rump_backyard", parents=L_rump_kitchen)
    L_rump_master = Location("Mayor Rump's Bedroom", background="rump_bedroom", parents=L_rump_lobby)
    L_rump_second = Location("Iwanka Rump's Bedroom", background="rump_iwanka", parents=L_rump_lobby)
    L_rump_office = Location("Mayor Rump's Office", background="rump_office", parents=L_rump_lobby, locked=True)


    L_bank = Location("Bank", background="bank_frontyard", parents=L_map, locked=True)
    L_bank_lobby = Location("Lobby", background=bank_lobby_bg, parents=L_bank, ref=True)
    L_bank_hallway = Location("Hallway", background="bank_hallway", parents=L_bank_lobby, ref=True, locked=True)
    L_bank_office = Location("Back Office", background="bank_office", parents=L_bank_hallway, ref=True)
    L_bank_cubicle = Location("Manager's Office", background="bank_office_cubicle", parents=L_bank_office, ref=True)
    L_bank_basement = Location("Basement", background="bank_basement", parents=L_bank_hallway, ref=True)
    L_bank_vault = Location("Vault", background="bank_vault", parents=L_bank_basement, ref=True)


    L_pool = Location("Pool", background="pool", parents=L_map, locked=True)
    L_pool_medicroom = Location("Medic Room", background="pool_changeroom02", parents=L_pool, locked=True)


    L_warehouse = Location("Warehouse", background="warehouse", parents=L_map, locked=True)
    L_warehouse_bushes = Location("Bushes", background="warehouse_bush", parents=L_warehouse, ref=True)
    L_warehouse_cargo = Location("Loading Dock", background=warehouse_cargo_bg, parents=L_warehouse, ref=True)
    L_warehouse_depot = Location("Depot", background=warehouse_depot_bg, parents=L_warehouse, ref=True)
    L_warehouse_furnace = Location("Furnace", background="warehouse_furnace", parents=L_warehouse_depot, ref=True)
    L_warehouse_lab = Location("Laboratory", background=warehouse_lab_bg, parents=L_warehouse_depot, ref=True)
    L_warehouse_office = Location("Office", background="warehouse_office", parents=L_warehouse_depot, ref=True)
    L_warehouse_storage = Location("Storage", background=warehouse_storage_bg, parents=L_warehouse_lab, ref=True)
    L_warehouse_sewer = Location("Sewer", background="warehouse_sewers", parents=L_warehouse_furnace, ref=True)


    L_basketball_court = Location("Basketball Court", background="basketball", parents=L_map, locked=True)
    L_hill = Location("Hill", background="hill", parents=L_map, locked=True)
    L_lair = Location("Lair", background="lair", parents=L_map, locked=True)
    L_pier = Location("Pier", background="pier", parents=L_map, locked=True)

    store.locations = {}
    for loc, loc_name in [(l, lname) for lname, l in globals().items() if lname.startswith("L_")]:
        loc.var_name = loc_name
        if loc.ref is True:
            loc.ref = loc_name[2:]
        store.locations[loc.var_name] = loc
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
