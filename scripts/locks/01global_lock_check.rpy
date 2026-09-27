label global_lock_check(destination=None):
    if destination is None:
        jump game_main

    $ renpy.dynamic(motion=(player.location, destination))

    call global_lock_check.router (destination)

    if _return:
        $ game.main()
        return

    python:
        for lock_check_label in ModManager.get_lock_check_labels():
            renpy.call_in_new_context(lock_check_label, destination)
        player.location.hide_screen()
        player.go_to(destination)
        destination.call()

    return


label global_lock_check.router(destination):

    if destination in L_map.children and player.location == L_map:
        jump map_lock_check

    elif destination in L_annie_front.get_all_children_inclusive():
        jump anniehouse_lock_check

    elif destination in L_apt.get_all_children_inclusive():
        jump apt_lock_check

    elif destination in L_bank.get_all_children_inclusive():
        jump bank_lock_check

    elif destination in L_beachhouse_front.get_all_children_inclusive():
        jump beach_house_lock_check

    elif destination in L_church_front.get_all_children_inclusive():
        jump church_lock_check

    elif destination in L_dealership.get_all_children_inclusive():
        jump dealership_lock_check

    elif destination in L_diane_barn.get_all_children_inclusive() or destination == L_diane_barn_building:
        jump diane_house_lock_check
    elif destination in L_diane_yard.get_all_children_inclusive():
        jump diane_house_lock_check

    elif destination in L_donutshop.get_all_children_inclusive():
        jump donut_shop_lock_check

    elif destination in L_erikhouse.get_all_children_inclusive():
        jump erikhouse_lock_check

    elif destination in L_gym_front.get_all_children_inclusive():
        jump gym_lock_check

    elif destination in L_home.get_all_children_inclusive():
        jump home_lock_check

    elif destination in L_hospital.get_all_children_inclusive():
        jump hospital_lock_check

    elif destination in L_library_front.get_all_children_inclusive():
        jump library_lock_check

    elif destination in L_mall_parking_lot.get_all_children_inclusive():
        jump mall_lock_check

    elif destination in L_miahouse.get_all_children_inclusive():
        jump miahouse_lock_check

    elif destination in L_park.get_all_children_inclusive():
        jump park_lock_check

    elif destination in L_pizzeria_exterior.get_all_children_inclusive():
        jump pizzeria_lock_check

    elif destination in L_police_front.get_all_children_inclusive():
        jump police_lock_check

    elif destination in L_rump_front.get_all_children_inclusive():
        jump rump_lock_check

    elif destination in L_school_front.get_all_children_inclusive():
        jump school_lock_check

    elif destination in L_treehouse.get_all_children_inclusive():
        jump treehouse_lock_check

    elif destination in L_tattooparlor.get_all_children_inclusive():
        jump tattoo_parlor_lock_check

    elif destination in L_trailerpark.get_all_children_inclusive():
        jump trailer_lock_check

    elif destination in L_warehouse.get_all_children_inclusive():
        jump warehouse_lock_check

    elif destination == L_map:
        jump map_destination_lock_check

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
