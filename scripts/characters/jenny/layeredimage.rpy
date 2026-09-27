init:
    $ jenny_clothing_options = ['b_groping_naked_touch', 'b_groping_naked_suck', 'b_groping_naked_finger', 'b_groping_suck', 'b_groping_touch', 'b_dressed', 'b_dressed_magic', 'b_empty', 'b_wet', 'b_towelhead', 'b_towel_pregnant_bump', 'b_towel_pregnant_belly', 'b_towel', 'b_tied', 'b_swimsuit_pregnant_bump', 'b_swimsuit_pregnant_belly', 'b_swimsuit', 'b_shower_soaping', 'b_shower_soaping2', 'b_shower_soaping1', 'b_shower', 'b_pull1_wet', 'b_pull1', 'b_pantieless', 'b_panties', 'b_naked_turned', 'b_naked', 'b_groping_touch_talk', 'b_groping_touch_look', 'b_groping_touch1', 'b_groping_touch2', 'b_groping_touch3', 'b_groping_suck_pre', 'b_groping_suck1', 'b_groping_suck2', 'b_groping_suck3', 'b_groping_naked_touch_talk', 'b_groping_naked_touch_look', 'b_groping_naked_touch1', 'b_groping_naked_touch2', 'b_groping_naked_touch3', 'b_groping_naked_suck_pre', 'b_groping_naked_suck1', 'b_groping_naked_suck2', 'b_groping_naked_suck3', 'b_groping_naked_finger1', 'b_groping_naked_finger2', 'b_groping_naked_finger3', 'b_groping_naked_cover', 'b_groping_naked', 'b_groping', 'b_dressed_pulling1', 'b_dressed_pulling2', 'b_dressed_pregnant_bump', 'b_dressed_pregnant_belly', 'b_cover', 'b_cheer_showoff', 'b_cheer_dress3', 'b_cheer', 'b_casual', 'b_jersey_pregnant_belly', 'b_naked_pregnant_belly', 'b_naked_pregnant_belly_pull1']
    $ jenny_unique_options = ['b_sleep_side_grope_hump_shirtup','b_sleep_side_grope_shirtup','b_sleep_side_naked','b_visit_sit_naked','b_visit_sit','b_visit_after','b_telescope_rub_look','b_telescope','b_sleep_turn_shirtup','b_sleep_turn','b_sleep_side_shirtup','b_sleep_side_grope','b_sleep_side_grope2_shirtup','b_sleep_side_grope2_hump_shirtup','b_sleep_side_grope2','b_sleep_side_grope1_shirtup','b_sleep_side_grope1','b_sleep_side','b_sleep_after','b_shower_kneeling','b_shower_cumshot','b_shower_butt1','b_front_undies','b_front_kiss_talk','b_front_cuddle','b_front','b_cam_intro']

init python:


    renpy.image('jenny_arms_a_empty', 'ground.png')
    renpy.image('jenny_body_b_empty', 'ground.png')
    renpy.image('jenny_face_f_empty', 'ground.png')
    renpy.image('jenny_face_talk_f_empty', 'ground.png')


    renpy.image('jenny_face_talk_f_laugh', 'jenny_face_f_laugh')
    renpy.image('jenny_face_talk_f_cheeks_surprised', 'jenny_face_f_cheeks_surprised')
    renpy.image('jenny_face_talk_f_angry_pouting', 'jenny_face_f_angry_pouting')
    renpy.image('jenny_face_talk_f_nipple1', 'jenny_face_f_nipple1')
    renpy.image('jenny_face_talk_f_nipple2', 'jenny_face_f_nipple2')
    renpy.image('jenny_face_talk_f_nipple3', 'jenny_face_f_nipple3')
    renpy.image('jenny_face_talk_f_front_eyeroll', 'jenny_face_f_front_eyeroll')
    renpy.image('jenny_face_talk_f_front_laugh', 'jenny_face_f_front_laugh')
    renpy.image('jenny_face_talk_f_angry_pouting_top', 'jenny_face_f_angry_pouting_top')
    renpy.image('jenny_face_talk_f_sleep_side_wake', 'jenny_face_f_sleep_side_wake')
    renpy.image('jenny_face_talk_f_telescope_surprised', 'jenny_face_f_telescope_surprised')
    renpy.image('jenny_face_talk_f_telescope_laugh', 'jenny_face_f_telescope_laugh')
    renpy.image('jenny_face_talk_f_cheeks_angry', 'jenny_face_f_cheeks_angry')
    renpy.image('jenny_face_bed_pussy_talk_f_nipple2', 'jenny_face_bed_pussy_f_nipple2')
    renpy.image('jenny_face_bed_pussy_talk_f_nipple3', 'jenny_face_bed_pussy_f_nipple3')
    renpy.image('jenny_face_talk_f_front_lip_down', 'jenny_face_f_front_lip_down')
    renpy.image('jenny_face_talk_f_front_cum', 'jenny_face_f_front_cum')
    renpy.image('jenny_face_bed_back_look_talk_f_surprised', 'jenny_face_bed_back_look_f_surprised')
    renpy.image('jenny_face_talk_f_sleep_side_sleeping', 'jenny_face_f_sleep_side_sleeping')
    renpy.image('jenny_face_talk_f_sleep_side_enjoy', 'jenny_face_f_sleep_side_enjoy')
    renpy.image('jenny_face_talk_f_sleep_side_rolleye', 'jenny_face_f_sleep_side_rolleye')


    renpy.image('jenny_face_f_front_lip', 'jenny_face_talk_f_front_lip')

layeredimage jenny:

    yanchor config.screen_height
    ypos 1.
    xanchor config.screen_width
    xpos 1.


    group overlay_under_body:
        attribute o_under_body_empty default null
        attribute o_under_body_laptop "characters/jenny/layeredimage/jenny_overlay_o_laptop.png"


    group body auto:
        attribute b_dressed default
        attribute b_dressed_magic 'jenny_body_b_dressed[M_jenny.pregnancy]'
        attribute b_empty null
        attribute b_groping_touch "jenny_body_b_groping_touch"

        attribute b_groping_suck "jenny_body_b_groping_suck"

        attribute b_groping_naked_touch "jenny_body_b_groping_naked_touch"

        attribute b_groping_naked_suck "jenny_body_b_groping_naked_suck"

        attribute b_groping_naked_finger "jenny_body_b_groping_naked_finger"

        attribute b_shower_scene_d_rub "jenny_body_b_shower_scene_d_rub"

        attribute b_shower_scene_e_rub "jenny_body_b_shower_scene_e_rub"

        attribute b_bed_pussy "jenny_body_b_bed_pussy"

        attribute b_shower_soaping "jenny_body_b_shower_soaping"

        attribute b_shower_butt "jenny_body_b_shower_butt"

        attribute b_front_kiss "jenny_body_b_front_kiss"

        attribute b_sleep_side_grope "jenny_body_b_sleep_side_grope"

        attribute b_sleep_side_grope_shirtup "jenny_body_b_sleep_side_grope_shirtup"

        attribute b_sleep_side_grope_hump_shirtup "jenny_body_b_sleep_side_grope_hump_shirtup"

        attribute b_towel "characters/jenny/layeredimage/jenny_body_b_towel[M_jenny.pregnancy.to_string].png"
        attribute b_couch_clit "jenny_body_b_couch_clit"

        attribute b_magic_sit_stand_dressed "jenny_body_b_magic_sit_stand_dressed"

        attribute b_dressed_tied_boob_grab


    group mouth prefix 'm':
        attribute talk null

    group face:
        attribute f_normal default null







    group face if_not 'm_talk' if_all 'b_magic_sit_stand_dressed':
        attribute f_normal "jenny_face_f_magic_sit_stand_normal"

        attribute f_sexy "jenny_face_f_magic_sit_stand_sexy"

        attribute f_grin "jenny_face_f_magic_sit_stand_grin"

        attribute f_laugh "jenny_face_f_magic_sit_stand_laugh"

        attribute f_eyeroll "jenny_face_f_magic_sit_stand_eyeroll"

        attribute f_upset "jenny_face_f_magic_sit_stand_upset"

        attribute f_angry "jenny_face_f_magic_sit_stand_angry"

        attribute f_phone_upset "jenny_face_f_magic_sit_stand_phone_upset"

        attribute f_gross "jenny_face_f_magic_sit_stand_gross"

        attribute f_surprised "jenny_face_f_magic_sit_stand_surprised"

        attribute f_sad "jenny_face_f_magic_sit_stand_sad"



    group face if_not 'm_talk' if_any jenny_clothing_options auto


    group face if_not 'm_talk' if_any ['b_dressed_tied'] auto:
        offset (-156, 115)


    group face if_not 'm_talk' if_any ['b_dressed_tied_recoil'] auto:
        offset (-96, 125)


    group face if_not 'm_talk' if_any ['b_dressed_tied_boob_grab', 'b_dressed_untying'] auto:
        offset (-186, 125)


    group face if_not 'm_talk' if_any ['b_dressed_hold_anon_arm'] auto:
        offset (-267, 42)


    group face if_not 'm_talk' if_any ['b_pool_plunge2'] auto:
        offset (-92, 225)
        zoom .76


    group face if_not 'm_talk' if_all 'b_pool_edge' auto:
        offset (-74, 216)
        zoom .76


    group face if_not 'm_talk' if_any ['b_pool_hair', 'b_pool_cover', 'b_pool', 'b_pool_plunge1'] auto:
        offset (-74, 251)
        zoom .76


    group face if_not 'm_talk' if_any ['b_naked_bed_bellytype', 'b_naked_bed_belly', 'b_dressed_bed_bellytype', 'b_dressed_bed_belly'] auto:
        offset (-421, 195)


    group face if_not 'm_talk' if_any ['b_bed_tied', 'b_bed_panties', 'b_bed_naked', 'b_bed_dressed', 'b_bed_cheerup', 'b_bed_cheerlift', 'b_bed_cheer_roxxy_touch2', 'b_bed_cheer_roxxy_touch1', 'b_bed_cheer_roxxy_lift3', 'b_bed_cheer_roxxy_lift2', 'b_bed_cheer_roxxy_lift1', 'b_bed_cheer_roxxy_grab2', 'b_bed_cheer_roxxy_grab1', 'b_bed_cheer'] auto:

        offset (2, -48)


    group face if_not 'm_talk' if_any ['b_breakfast_dressed', 'b_breakfast_dressed_pregnant_belly', 'b_breakfast_dressed_pregnant_bump', 'b_dinner_casual'] auto:
        offset (129, 144)
        xzoom -.76
        yzoom .76


    group face if_not 'm_talk' if_all 'b_gown_bed' auto:
        offset (138, 61)


    group face if_not 'm_talk' if_any ['b_breakfast_gettingup', 'b_breakfast_gettingup_pregnant_belly'] auto:
        offset (231, 96)
        xzoom -.76
        yzoom .76


    group face if_not 'm_talk' if_any ['b_breakfast_standing', 'b_breakfast_standing_panties_down', 'b_breakfast_standing_pregnant_belly'] auto:
        offset (102, 12)
        xzoom -.76
        yzoom .76


    group face if_not 'm_talk' if_all 'b_breakfast_leaning' auto:
        offset (259, 170)
        xzoom -.76
        yzoom .76


    group face if_not 'm_talk' if_any ['b_bed_back_tied', 'b_bed_back_naked'] auto:
        offset (10, -2)


    group face if_not 'm_talk' if_all 'b_bed_reading' auto:
        offset (143, 62)


    group face if_not 'm_talk' if_all 'b_groping_naked_squirt' auto:
        offset (-11, 10)


    group face if_not 'm_talk' if_all 'b_groping_naked_orgasm' auto:
        offset (-23, 66)


    group face if_not 'm_talk' if_any ['b_bed_side', 'b_jersey_bed_side'] auto:
        offset (19, 127)
        xzoom -1


    group face if_not 'm_talk' if_any ['b_bed_side_laptop', 'b_jersey_bed_side_laptop'] auto:
        offset (-477, 133)


    group face if_not 'm_talk' if_all 'b_bed_front_sit' auto:
        offset (-118, -133)


    group face if_not 'm_talk' if_all 'b_bed_front_laying' auto:
        offset (-230, 70)


    group face if_not 'm_talk' if_all 'b_couch_sit' auto:
        offset (240, 107)
        zoom .69


    group face if_not 'm_talk' if_all 'b_bed_pussy' auto variant 'bed_pussy':
        attribute f_sexy_down "jenny_face_bed_pussy_f_sexy_down"

        attribute f_nipple2 "jenny_face_bed_pussy_f_nipple2"

        attribute f_nipple3 "jenny_face_bed_pussy_f_nipple3"



    group face if_not 'm_talk' if_all 'b_bed_pussy1' auto:
        offset (-191, 2)


    group face if_not 'm_talk' if_all 'b_bed_pussy2' auto:
        offset (-223, 9)


    group face if_not 'm_talk' if_any ['b_telescope_standing_panties', 'b_telescope_standing'] auto:
        offset (240, -134)
        zoom .82


    group face if_not 'm_talk' if_any ['b_bed_jersey', 'b_bed_jersey_belly', 'b_bed_jersey_boobs'] auto:
        offset (-381, -32)


    group face if_not 'm_talk' if_any ['b_bed_jersey_boobs_back'] auto:
        offset (129, -28)
        xzoom -1


    group face if_not 'm_talk' if_any ['b_jersey_bed_climb'] auto:
        offset (-410, 3)


    group face if_not 'm_talk' if_any ['b_jersey_bed_mount'] auto:
        align (.5, .5)
        offset (-419, -6)
        rotate -12.75






    group face if_not 'm_talk' if_all 'b_cheer_side' auto variant 'bed_back_look':
        offset (170, 138)


    group face if_not 'm_talk' if_any ['b_front_couch_bored'] auto:
        offset (-392, -55)


    group face if_not 'm_talk' if_any ['b_shower_back', 'b_shower_back_creampie'] auto variant 'bed_back_look':
        offset (-22, 137)


    group face if_not 'm_talk' if_any jenny_unique_options auto:
        attribute f_empty null


    group face if_not 'm_talk' if_any ['b_bed_back_look'] auto variant 'bed_back_look'


    group face if_not 'm_talk' if_any ['b_door_dressed_pregnant_belly', 'b_door_open_dressed_pregnant_belly'] auto variant 'bedroom_door'







    group face if_all ['m_talk', 'b_magic_sit_stand_dressed']:
        attribute f_grin "jenny_face_talk_f_magic_sit_stand_grin"

        attribute f_normal "jenny_face_talk_f_magic_sit_stand_normal"

        attribute f_sexy "jenny_face_talk_f_magic_sit_stand_sexy"

        attribute f_eyeroll "jenny_face_f_magic_sit_stand_eyeroll"

        attribute f_upset "jenny_face_talk_f_magic_sit_stand_upset"

        attribute f_angry "jenny_face_talk_f_magic_sit_stand_angry"

        attribute f_phone_upset "jenny_face_talk_f_magic_sit_stand_phone_upset"

        attribute f_gross "jenny_face_talk_f_magic_sit_stand_gross"

        attribute f_sad "jenny_face_talk_f_magic_sit_stand_sad"

        attribute f_laugh "jenny_face_f_magic_sit_stand_laugh"

        attribute f_surprised "jenny_face_f_magic_sit_stand_surprised"



    group face if_all 'm_talk' if_any jenny_clothing_options auto variant 'talk'


    group face if_all 'm_talk' if_any ['b_dressed_tied'] auto variant 'talk':
        offset (-156, 115)


    group face if_all 'm_talk' if_any ['b_dressed_tied_recoil'] auto variant 'talk':
        offset (-96, 125)


    group face if_all 'm_talk' if_any ['b_dressed_tied_boob_grab', 'b_dressed_untying'] auto variant 'talk':
        offset (-186, 125)


    group face if_all 'm_talk' if_any ['b_dressed_hold_anon_arm'] auto variant 'talk':
        offset (-267, 42)


    group face if_all 'm_talk' if_any ['b_pool_plunge2', 'b_pool_plunge1'] auto variant 'talk':
        offset (-92, 225)
        zoom .76


    group face if_all ['m_talk', 'b_pool_edge'] auto variant 'talk':
        offset (-74, 216)
        zoom .76


    group face if_all 'm_talk' if_any ['b_pool_hair', 'b_pool_cover', 'b_pool'] auto variant 'talk':
        offset (-74, 251)
        zoom .76


    group face if_all 'm_talk' if_any ['b_naked_bed_bellytype', 'b_naked_bed_belly', 'b_dressed_bed_bellytype', 'b_dressed_bed_belly'] auto variant 'talk':
        offset (-421, 195)


    group face if_all 'm_talk' if_any ['b_bed_tied', 'b_bed_panties', 'b_bed_naked', 'b_bed_dressed', 'b_bed_cheerup', 'b_bed_cheerlift', 'b_bed_cheer_roxxy_touch2', 'b_bed_cheer_roxxy_touch1', 'b_bed_cheer_roxxy_lift3', 'b_bed_cheer_roxxy_lift2', 'b_bed_cheer_roxxy_lift1', 'b_bed_cheer_roxxy_grab2', 'b_bed_cheer_roxxy_grab1', 'b_bed_cheer'] auto variant 'talk':

        offset (2, -48)


    group face if_all 'm_talk' if_any ['b_breakfast_dressed', 'b_breakfast_dressed_pregnant_belly', 'b_breakfast_dressed_pregnant_bump', 'b_dinner_casual'] auto variant 'talk':
        offset (129, 144)
        xzoom -.76
        yzoom .76


    group face if_all ['m_talk', 'b_gown_bed'] auto variant 'talk':
        offset (138, 61)


    group face if_all 'm_talk' if_any ['b_breakfast_gettingup', 'b_breakfast_gettingup_pregnant_belly'] auto variant 'talk':
        offset (231, 96)
        xzoom -.76
        yzoom .76


    group face if_all 'm_talk' if_any ['b_breakfast_standing', 'b_breakfast_standing_panties_down', 'b_breakfast_standing_pregnant_belly'] auto variant 'talk':
        offset (102, 12)
        xzoom -.76
        yzoom .76


    group face if_all ['m_talk', 'b_breakfast_leaning'] auto variant 'talk':
        offset (259, 170)
        xzoom -.76
        yzoom .76


    group face if_all 'm_talk' if_any ['b_bed_back_tied', 'b_bed_back_naked'] auto variant 'talk':
        offset (10, -2)


    group face if_all ['m_talk', 'b_bed_reading'] auto variant 'talk':
        offset (143, 62)


    group face if_all ['m_talk', 'b_groping_naked_squirt'] auto variant 'talk':
        offset (-11, 10)


    group face if_all ['m_talk', 'b_groping_naked_orgasm'] auto variant 'talk':
        offset (-23, 66)


    group face if_all 'm_talk' if_any ['b_bed_side', 'b_jersey_bed_side'] auto variant 'talk':
        offset (19, 127)
        xzoom -1


    group face if_all 'm_talk' if_any ['b_bed_side_laptop', 'b_jersey_bed_side_laptop'] auto variant 'talk':
        offset (-477, 133)


    group face if_all ['m_talk', 'b_bed_front_sit'] auto variant 'talk':
        offset (-118, -133)


    group face if_all ['m_talk', 'b_bed_front_laying'] auto variant 'talk':
        offset (-230, 70)


    group face if_all ['m_talk', 'b_couch_sit'] auto variant 'talk':
        offset (240, 107)
        zoom .69


    group face if_all ['m_talk','b_bed_pussy'] auto variant 'bed_pussy_talk':
        attribute f_sexy_down "jenny_face_bed_pussy_talk_f_sexy_down"

        attribute f_nipple2 "jenny_face_bed_pussy_talk_f_nipple2"

        attribute f_nipple3 "jenny_face_bed_pussy_talk_f_nipple3"



    group face if_all ['m_talk', 'b_bed_pussy1'] auto variant 'talk':
        offset (-191, 2)


    group face if_all ['m_talk', 'b_bed_pussy2'] auto variant 'talk':
        offset (-223, 9)


    group face if_all 'm_talk' if_any ['b_telescope_standing_panties', 'b_telescope_standing'] auto variant 'talk':
        offset (240, -134)
        zoom .82


    group face if_all 'm_talk' if_any ['b_bed_jersey', 'b_bed_jersey_belly', 'b_bed_jersey_boobs'] auto variant 'talk':
        offset (-381, -32)


    group face if_all 'm_talk' if_any ['b_bed_jersey_boobs_back'] auto variant 'talk':
        offset (129, -28)
        xzoom -1


    group face if_all 'm_talk' if_any ['b_jersey_bed_climb'] auto variant 'talk':
        offset (-410, 3)


    group face if_all 'm_talk' if_any ['b_jersey_bed_mount'] auto variant 'talk':
        align (.5, .5)
        offset (-419, -6)
        rotate -12.75






    group face if_all ['m_talk', 'b_cheer_side'] auto variant 'bed_back_look_talk':
        offset (170, 138)


    group face if_all 'm_talk' if_any ['b_front_couch_bored'] auto variant 'talk':
        offset (-392, -55)


    group face if_all 'm_talk' if_any ['b_shower_back', 'b_shower_back_creampie'] auto variant 'bed_back_look_talk':
        offset (-22, 137)


    group face if_all 'm_talk' if_any jenny_unique_options auto variant 'talk':
        attribute f_empty null


    group face if_all 'm_talk' if_any ['b_bed_back_look'] auto variant 'bed_back_look_talk'


    group face if_all 'm_talk' if_any ['b_door_dressed_pregnant_belly', 'b_door_open_dressed_pregnant_belly'] auto variant 'bedroom_door_talk'


    group overlay_under_arms:
        attribute o_under_arms_empty default null
        attribute o_under_arms_cheer_bed_front_sit2 "characters/jenny/layeredimage/jenny_overlay_o_cheer_bed_front_sit2.png"



    group arms if_any ['b_dressed', 'b_dressed_magic', 'b_wet', 'b_casual', 'b_towelhead', 'b_pantieless'] auto variant 'dressed':
        attribute a_idle default "jenny_arms_dressed_a_crossed[M_jenny.pregnancy.to_string]"

        attribute a_phone "jenny_arms_dressed_a_phone[M_jenny.pregnancy.to_string]"

        attribute a_baby "characters/jenny/layeredimage/jenny_arms_dressed_a_baby_[player.last_baby_gender].png"
        attribute a_magic


    group arms if_any ['b_dressed_pregnant_bump'] auto variant 'dressed':
        attribute a_idle default "jenny_arms_dressed_a_crossed_pregnant_bump"



    group arms if_any ['b_dressed_pregnant_belly'] auto variant 'dressed':
        attribute a_idle default "jenny_arms_dressed_a_crossed_pregnant_belly"

        attribute a_crossed "jenny_arms_dressed_a_crossed_pregnant_belly"

        attribute a_cry 'jenny_arms_dressed_a_pregnant_belly_cry'
        attribute a_touch 'jenny_arms_dressed_a_pregnant_touch'


    group arms if_any ['b_jersey_pregnant_belly'] auto variant 'jersey_pregnant_belly':
        attribute a_idle default "jenny_arms_jersey_pregnant_belly_a_touch"



    group arms if_any ['b_naked_pregnant_belly'] auto variant 'naked_pregnant_belly':
        attribute a_idle default 'jenny_arms_towel_a_pregnant_touch'
        attribute a_touch 'jenny_arms_towel_a_pregnant_touch'


    group arms if_any 'b_bed_jersey' auto variant 'bed_jersey':
        attribute a_idle default 'jenny_arms_bed_jersey_a_down'


    group arms if_any 'b_bed_jersey_belly' auto variant 'bed_jersey_belly':
        attribute a_idle default 'jenny_arms_bed_jersey_belly_a_lift2'
        attribute a_touch anim.TransitionAnimation(
            'jenny_arms_bed_jersey_belly_a_touch1', .6, Dissolve(.3),
            'jenny_arms_bed_jersey_belly_a_touch2', .6, Dissolve(.3))


    group arms if_any ['b_bed_jersey_boobs', 'b_bed_jersey_boobs_back'] auto variant 'bed_jersey_boobs':
        attribute a_idle default 'jenny_arms_bed_jersey_boobs_a_down'
        attribute a_squeeze anim.TransitionAnimation(
            'jenny_arms_bed_jersey_boobs_a_squeeze1', 1., Dissolve(.2),
            'jenny_arms_bed_jersey_boobs_a_squeeze2', .6, Dissolve(.2))


    group arms if_any ['b_magic_sit_stand_dressed'] auto:
        attribute a_idle default "jenny_arms_a_magic_sit_stand_hip_spoon"

        attribute a_magic_sit_stand_belly_touch "jenny_arms_a_magic_sit_stand_belly_touch"

        attribute a_magic_sit_stand_phone "jenny_arms_a_magic_sit_stand_phone"

        attribute a_magic_sit_stand_crossed "jenny_arms_a_magic_sit_stand_crossed"



    group arms if_any ['b_bed_front_sit'] auto variant 'bed_front_sit':
        attribute a_idle default "jenny_arms_bed_front_sit_a_sides"



    group arms if_any ['b_couch_sit'] auto variant 'couch':
        attribute a_idle default 'jenny_arms_couch_a_rest'
        attribute a_dick "jenny_arms_couch_a_dick"



    group arms if_any ['b_bed_panties', 'b_bed_dressed'] auto variant 'bed_dressed':
        attribute a_idle default 'jenny_arms_bed_dressed_a_down'
        attribute a_bed_dressed_hips_toy4b Image("characters/jenny/layeredimage/jenny_arms_dressed_a_hips_toy4b.png",yoffset=-50)


    group arms if_any ['b_bed_cheer'] auto variant 'bed_cheer':
        attribute a_idle default 'jenny_arms_bed_cheer_a_down'


    group arms if_any ['b_bed_back_tied'] auto variant 'bed_back_tied':
        attribute a_idle default 'jenny_arms_bed_back_tied_a_down'


    group arms if_any ['b_bed_back_sit'] auto variant 'bed_back':
        attribute a_idle default 'jenny_arms_bed_back_a_sit_hips'


    group arms if_any ['b_bed_back_look'] auto variant 'bed_back_look':
        attribute a_idle default 'jenny_arms_bed_back_look_a_up'


    group arms if_any ['b_bed_cheerup'] auto variant 'bed_cheerup':
        attribute a_idle default 'jenny_arms_bed_cheerup_a_down'


    group arms if_any ['b_tied'] auto variant 'tied':
        attribute a_idle default 'jenny_arms_tied_a_hips'


    group arms if_any ['b_breakfast_standing', 'b_breakfast_standing_panties_down', 'b_breakfast_standing_pregnant_belly'] auto variant 'breakfast_standing':
        attribute a_idle default 'jenny_arms_breakfast_standing_a_hips'
        attribute a_sides 'jenny_arms_dressed_a_sides':
            offset (102, 12)
            xzoom -.76
            yzoom .76


    group arms if_any ['b_cam_intro'] auto variant 'cam_intro':
        attribute a_idle default 'jenny_arms_cam_intro_a_cover'


    group arms if_any ['b_cheer'] auto variant 'cheer':
        attribute a_idle default 'jenny_arms_cheer_a_hips'


    group arms if_any ['b_swimsuit'] auto variant 'swimsuit':
        attribute a_idle default "jenny_arms_baju renang_a_crossed[M_jenny.pregnancy.to_string]"

        attribute a_phone "jenny_arms_baju renang_a_ponsel[M_jenny.pregnancy.to_string]"



    group arms if_any ['b_dinner_casual_side'] auto variant 'dinner_casual_side':
        attribute a_idle default 'jenny_arms_dinner_casual_side_a_side1'


    group arms if_any ['b_bed_tied'] auto variant 'bed_tied':
        attribute a_idle default 'jenny_arms_bed_tied_a_down'


    group arms if_any ['b_bed_reading'] auto variant 'bed_reading':
        attribute a_idle default 'jenny_arms_bed_reading_a_journal'


    group arms if_any ['b_bed_side_laptop', 'b_bed_side'] auto variant 'bed_side':
        attribute a_idle default 'jenny_arms_bed_side_a_laptop'
        attribute a_jerk "jenny_arms_bed_side_a_jerk"



    group arms if_any 'b_jersey_bed_side' auto variant 'jersey_bed_side':
        attribute a_idle default 'jenny_arms_jersey_bed_side_a_side'


    group arms if_any 'b_jersey_bed_side_laptop' auto variant 'jersey_bed_side_laptop':
        attribute a_idle default 'jenny_arms_jersey_bed_side_laptop_a_side'


    group arms if_any ['b_couch_standing'] auto variant 'couch_standing':
        attribute a_idle default 'jenny_arms_couch_standing_a_hips'


    group arms if_any ['b_towel'] auto variant 'towel':
        attribute a_idle default 'jenny_arms_magic_preggo_a_towel[M_jenny.pregnancy.to_string]'


    group arms if_any ['b_breakfast_dressed', 'b_breakfast_dressed_pregnant_belly', 'b_dinner_casual'] auto variant 'breakfast_dressed':
        attribute a_idle default "jenny_arms_sarapan_berpakaian_a_crossed[M_jenny.pregnancy.to_string]"

        attribute a_phone "jenny_arms_sarapan_berpakaian_a_ponsel[M_jenny.pregnancy.to_string]"

        attribute a_rub "jenny_arms_sarapan_berpakaian_a_rub"



    group arms if_any ['b_breakfast_dressed_eat_pregnant_belly'] auto variant 'breakfast_dressed_eat_pregnant_belly':
        attribute a_idle default 'jenny_arms_breakfast_dressed_eat_pregnant_belly_a_eat1'
        attribute a_eat anim.TransitionAnimation(
            'jenny_arms_breakfast_dressed_eat_pregnant_belly_a_eat1', .4, Dissolve(.2),
            'jenny_arms_breakfast_dressed_eat_pregnant_belly_a_eat2', .4, Dissolve(.2))


    group arms if_any ['b_visit_sit_naked'] auto variant 'visit_sit_naked':
        attribute a_idle default 'jenny_arms_visit_sit_naked_a_down'


    group arms if_any ['b_visit_sit'] auto variant 'visit_sit':
        attribute a_idle default 'jenny_arms_visit_sit_a_down'
        attribute a_stroke "jenny_arms_visit_sit_a_stroke"



    group arms if_any ['b_sleep_side_naked'] auto variant 'sleep_naked':
        attribute a_idle default 'jenny_arms_sleep_naked_a_side'


    group arms if_any ['b_sleep_turn_shirtup', 'b_sleep_turn', 'b_sleep_side_shirtup', 'b_sleep_side', 'b_sleep_side_grope'] auto variant 'sleep':
        attribute a_idle default 'jenny_arms_sleep_a_side'


    group arms if_any ['b_naked', 'b_shower', 'b_panties'] auto variant 'naked':
        attribute a_idle default 'jenny_arms_naked_a_hips'
        attribute a_monster_hit "jenny_arms_naked_a_monster_hit"



    group arms if_any ['b_shower_back'] auto variant 'shower_back':
        attribute a_idle default 'jenny_arms_shower_back_a_down'


    group arms if_any ['b_naked_side'] auto variant 'naked_side':
        attribute a_idle default 'jenny_arms_naked_side_a_up'


    group arms if_any ['b_naked_back_plug'] auto variant 'naked_back':
        attribute a_idle default 'jenny_arms_naked_back_a_sides'


    group arms if_any ['b_telescope'] auto variant 'telescope':
        attribute a_idle default 'jenny_arms_telescope_a_down'


    group arms if_any ['b_telescope_rub_look', 'b_telescope_rub'] auto variant 'telescope_rub':
        attribute a_idle default 'jenny_arms_telescope_rub_a_rub'


    group arms if_any ['b_gown_bed', 'b_gown_bed_sleep'] auto variant 'gown_bed':
        attribute a_idle default 'jenny_arms_naked_a_hip'
        attribute a_baby "characters/diane/layeredimage/diane_arms_gown_bed_a_baby_[M_jenny.pregnancy.baby_gender].png"
        attribute a_bed "characters/diane/layeredimage/diane_arms_gown_bed_a_side.png"


    group arms if_any ['b_front_undies', 'b_front'] auto variant 'front':
        attribute a_idle default 'jenny_arms_front_a_down'


    group arms if_any ['b_groping_touch_talk', 'b_groping_touch_look', 'b_groping_touch1', 'b_groping_touch2', 'b_groping_touch3', 'b_groping_touch', 'b_groping_suck_pre', 'b_groping_suck3', 'b_groping_suck2', 'b_groping_suck1', 'b_groping_suck' ,'b_groping'] auto variant 'groping':
        attribute a_idle default 'jenny_arms_groping_a_hips'


    group arms if_any ['b_groping_naked_touch_look', 'b_groping_naked_touch3', 'b_groping_naked_touch2', 'b_groping_naked_touch1', 'b_groping_naked_touch', 'b_groping_naked_suck_pre', 'b_groping_naked_suck3', 'b_groping_naked_suck2', 'b_groping_naked_suck1', 'b_groping_naked_suck', 'b_groping_naked_squirt', 'b_groping_naked_finger3', 'b_groping_naked_finger2', 'b_groping_naked_finger1', 'b_groping_naked_finger', 'b_groping_naked_cover', 'b_groping_naked'] auto variant 'groping_naked':
        attribute a_idle default 'jenny_arms_groping_naked_a_hips'


    group overlay if_not ['b_breakfast_dressed', 'b_breakfast_dressed_pregnant_belly', 'b_breakfast_dressed_pregnant_bump', 'b_dinner_casual', 'b_breakfast_gettingup', 'b_breakfast_gettingup_pregnant_belly', 'b_breakfast_standing', 'b_breakfast_standing_panties_down', 'b_breakfast_standing_pregnant_belly', 'b_breakfast_pulling', 'b_breakfast_pulling_pregnant_belly', 'b_cheer_dress1', 'b_dressed_panties_remove_down', 'b_dressed_pregnant_belly_panties_remove_down', 'b_dressed_pregnant_belly_run', 'b_dressed_pregnant_bump_run', 'b_dressed_run', 'b_naked_panties_remove_down'] auto:
        attribute o_empty default null
        attribute o_visit_cumshot "jenny_overlay_o_visit_cumshot"


    group overlay if_any ['b_breakfast_dressed', 'b_breakfast_dressed_pregnant_belly', 'b_breakfast_dressed_pregnant_bump', 'b_dinner_casual'] auto:
        offset (129, 144)
        xzoom -.76
        yzoom .76

    group overlay if_any ['b_breakfast_gettingup', 'b_breakfast_gettingup_pregnant_belly'] auto:
        offset (231, 96)
        xzoom -.76
        yzoom .76

    group overlay if_any ['b_breakfast_standing', 'b_breakfast_standing_panties_down', 'b_breakfast_standing_pregnant_belly'] auto:
        offset (102, 12)
        xzoom -.76
        yzoom .76

    group overlay if_any ['b_breakfast_pulling', 'b_breakfast_pulling_pregnant_belly'] auto:
        offset (-408, 13)
        zoom .76

    group overlay if_any ['b_cheer_dress1', 'b_dressed_panties_remove_down', 'b_dressed_pregnant_belly_panties_remove_down', 'b_dressed_pregnant_belly_run', 'b_dressed_pregnant_bump_run', 'b_dressed_run', 'b_naked_panties_remove_down'] auto:
        align (.5, .5)
        offset (-60, 107)
        rotate -6

image jenny_f = "characters/jenny/layeredimage/jenny_face_f_normal.png"



image jenny_arms_magic_preggo_a_towel_pregnant_belly = "characters/jenny/layeredimage/jenny_arms_towel_a_pregnant_touch.png"
image jenny_arms_magic_preggo_a_towel_pregnant_bump = "characters/jenny/layeredimage/jenny_arms_naked_a_sides.png"
image jenny_arms_magic_preggo_a_towel = "characters/jenny/layeredimage/jenny_arms_towel_a_hips.png"

image jenny_arms_breakfast_dressed_a_phone_pregnant_belly = "characters/jenny/layeredimage/jenny_arms_breakfast_dressed_a_pregnant_phone.png"
image jenny_arms_breakfast_dressed_a_phone_pregnant_bump = "characters/jenny/layeredimage/jenny_arms_breakfast_dressed_a_phone.png"
image jenny_arms_breakfast_dressed_a_phone = "characters/jenny/layeredimage/jenny_arms_breakfast_dressed_a_phone.png"

image jenny_arms_swimsuit_a_phone_pregnant_belly = "characters/jenny/layeredimage/jenny_arms_swimsuit_a_pregnant_belly_phone.png"
image jenny_arms_swimsuit_a_phone_pregnant_bump = "characters/jenny/layeredimage/jenny_arms_swimsuit_a_phone.png"
image jenny_arms_swimsuit_a_phone = "characters/jenny/layeredimage/jenny_arms_swimsuit_a_phone.png"

image jenny_arms_dressed_a_phone_pregnant_belly = "characters/jenny/layeredimage/jenny_arms_dressed_a_pregnant_belly_phone.png"
image jenny_arms_dressed_a_phone_pregnant_bump = "characters/jenny/layeredimage/jenny_arms_dressed_a_phone.png"
image jenny_arms_dressed_a_phone = "characters/jenny/layeredimage/jenny_arms_dressed_a_phone.png"

image jenny_arms_breakfast_dressed_a_crossed_pregnant_belly = "characters/jenny/layeredimage/jenny_arms_breakfast_dressed_a_pregnant_crossed.png"
image jenny_arms_breakfast_dressed_a_crossed_pregnant_bump = "characters/jenny/layeredimage/jenny_arms_breakfast_dressed_a_crossed.png"
image jenny_arms_breakfast_dressed_a_crossed = "characters/jenny/layeredimage/jenny_arms_breakfast_dressed_a_crossed.png"

image jenny_arms_swimsuit_a_crossed_pregnant_belly = "characters/jenny/layeredimage/jenny_arms_swimsuit_a_pregnant_crossed.png"
image jenny_arms_swimsuit_a_crossed_pregnant_bump = "characters/jenny/layeredimage/jenny_arms_swimsuit_a_crossed.png"
image jenny_arms_swimsuit_a_crossed = "characters/jenny/layeredimage/jenny_arms_swimsuit_a_crossed.png"

image jenny_arms_dressed_a_crossed_pregnant_belly = "characters/jenny/layeredimage/jenny_arms_dressed_a_pregnant_crossed.png"
image jenny_arms_dressed_a_crossed_pregnant_bump = "characters/jenny/layeredimage/jenny_arms_dressed_a_crossed.png"
image jenny_arms_dressed_a_crossed = "characters/jenny/layeredimage/jenny_arms_dressed_a_crossed.png"


image jenny_body_b_front_kiss:
    Transform("characters/jenny/layeredimage/jenny_body_b_front_kiss1.png")
    pause .4
    Transform("characters/jenny/layeredimage/jenny_body_b_front_kiss2.png")
    pause .4
    repeat

image jenny_body_b_shower_soaping:
    Transform("characters/jenny/layeredimage/jenny_body_b_shower_soaping1.png")
    pause .4
    Transform("characters/jenny/layeredimage/jenny_body_b_shower_soaping2.png")
    pause .4
    repeat

image jenny_body_b_groping_touch:
    Transform("characters/jenny/layeredimage/jenny_body_b_groping_touch1.png")
    pause .3
    Transform("characters/jenny/layeredimage/jenny_body_b_groping_touch2.png")
    pause .3
    Transform("characters/jenny/layeredimage/jenny_body_b_groping_touch3.png")
    pause .3
    repeat

image jenny_body_b_groping_suck:
    Transform("characters/jenny/layeredimage/jenny_body_b_groping_suck1.png")
    pause .3
    Transform("characters/jenny/layeredimage/jenny_body_b_groping_suck2.png")
    pause .3
    Transform("characters/jenny/layeredimage/jenny_body_b_groping_suck3.png")
    pause .3
    repeat

image jenny_body_b_groping_naked_touch:
    Transform("characters/jenny/layeredimage/jenny_body_b_groping_naked_touch1.png")
    pause .3
    Transform("characters/jenny/layeredimage/jenny_body_b_groping_naked_touch2.png")
    pause .3
    Transform("characters/jenny/layeredimage/jenny_body_b_groping_naked_touch3.png")
    pause .3
    repeat

image jenny_body_b_groping_naked_suck:
    Transform("characters/jenny/layeredimage/jenny_body_b_groping_naked_suck1.png")
    pause .3
    Transform("characters/jenny/layeredimage/jenny_body_b_groping_naked_suck2.png")
    pause .3
    Transform("characters/jenny/layeredimage/jenny_body_b_groping_naked_suck3.png")
    pause .3
    repeat

image jenny_body_b_groping_naked_finger:
    Transform("characters/jenny/layeredimage/jenny_body_b_groping_naked_finger1.png")
    pause .3
    Transform("characters/jenny/layeredimage/jenny_body_b_groping_naked_finger2.png")
    pause .3
    Transform("characters/jenny/layeredimage/jenny_body_b_groping_naked_finger3.png")
    pause .3
    repeat

image jenny_body_b_shower_scene_e_rub:
    Transform("characters/jenny/layeredimage/jenny_body_b_shower_scene_e1.png")
    pause .4
    Transform("characters/jenny/layeredimage/jenny_body_b_shower_scene_e2.png")
    pause .4
    repeat

image jenny_body_b_shower_scene_d_rub:
    Transform("characters/jenny/layeredimage/jenny_body_b_shower_scene_d2.png")
    pause .4
    Transform("characters/jenny/layeredimage/jenny_body_b_shower_scene_d3.png")
    pause .4
    repeat

image jenny_body_b_bed_pussy:
    Transform("characters/jenny/layeredimage/jenny_body_b_bed_pussy1.png")
    pause .4
    Transform("characters/jenny/layeredimage/jenny_body_b_bed_pussy2.png")
    pause .4
    repeat

image jenny_face_bed_pussy_f_sexy_down:
    Transform("characters/jenny/layeredimage/jenny_face_f_sexy_down.png",xpos=-191, ypos=2)
    pause .4
    Transform("characters/jenny/layeredimage/jenny_face_f_sexy_down.png",xpos=-223, ypos=9)
    pause .4
    repeat

image jenny_face_bed_pussy_talk_f_sexy_down:
    Transform("characters/jenny/layeredimage/jenny_face_talk_f_sexy_down.png",xpos=-191, ypos=2)
    pause .4
    Transform("characters/jenny/layeredimage/jenny_face_talk_f_sexy_down.png",xpos=-223, ypos=9)
    pause .4
    repeat

image jenny_face_bed_pussy_f_nipple2:
    Transform("characters/jenny/layeredimage/jenny_face_f_nipple2.png",xpos=-191, ypos=2)
    pause .4
    Transform("characters/jenny/layeredimage/jenny_face_f_nipple2.png",xpos=-223, ypos=9)
    pause .4
    repeat

image jenny_face_bed_pussy_f_nipple3:
    Transform("characters/jenny/layeredimage/jenny_face_f_nipple3.png",xpos=-191, ypos=2)
    pause .4
    Transform("characters/jenny/layeredimage/jenny_face_f_nipple3.png",xpos=-223, ypos=9)
    pause .4
    repeat


image jenny_arms_naked_a_monster_hit:
    Transform("characters/jenny/layeredimage/jenny_arms_naked_a_monster_hit1.png")
    pause .3
    Transform("characters/jenny/layeredimage/jenny_arms_naked_a_monster_hit2.png")
    pause .3
    repeat

image jenny_arms_bed_side_a_jerk:
    Transform("characters/jenny/layeredimage/jenny_arms_bed_side_a_jerk1.png")
    pause M_jenny.get("sex speed")
    Transform("characters/jenny/layeredimage/jenny_arms_bed_side_a_jerk2.png")
    pause M_jenny.get("sex speed")
    repeat

image jenny_arms_telescope_rub_a_rub:
    Transform("characters/jenny/layeredimage/jenny_arms_telescope_rub_a_rub1.png")
    pause .2
    Transform("characters/jenny/layeredimage/jenny_arms_telescope_rub_a_rub2.png")
    pause .2
    Transform("characters/jenny/layeredimage/jenny_arms_telescope_rub_a_rub3.png")
    pause .2
    Transform("characters/jenny/layeredimage/jenny_arms_telescope_rub_a_rub4.png")
    pause .2
    repeat

image jenny_arms_breakfast_dressed_a_rub:
    Transform("characters/jenny/layeredimage/jenny_arms_breakfast_dressed_a_rub1.png")
    pause .4
    Transform("characters/jenny/layeredimage/jenny_arms_breakfast_dressed_a_rub2.png")
    pause .4
    repeat

image jenny_player_couch_cum:
    Transform("characters/jenny/layeredimage/jenny_arms_couch_a_cum1.png")
    pause .2
    Transform("characters/jenny/layeredimage/jenny_arms_couch_a_cum2.png")
    pause .2


image jenny_couch_dick_rub 1 = "characters/jenny/layeredimage/jenny_arms_couch_a_dick1.png"
image jenny_couch_dick_rub 2 = "characters/jenny/layeredimage/jenny_arms_couch_a_dick2.png"
image jenny_couch_dick_rub 3 = "characters/jenny/layeredimage/jenny_arms_couch_a_dick3.png"


image jenny_electro 1 = "characters/jenny/layeredimage/jenny_body_b_cam_electro_anim1.png"
image jenny_electro 2 = "characters/jenny/layeredimage/jenny_body_b_cam_electro_anim2.png"
image jenny_electro 3 = "characters/jenny/layeredimage/jenny_body_b_cam_electro_anim3.png"
image jenny_electro 4 = "characters/jenny/layeredimage/jenny_body_b_cam_electro_anim4.png"

image jenny_vibrate 1 = "characters/jenny/layeredimage/jenny_body_b_cam_vibrate_anim1.png"
image jenny_vibrate 2 = "characters/jenny/layeredimage/jenny_body_b_cam_vibrate_anim2.png"
image jenny_vibrate 3 = "characters/jenny/layeredimage/jenny_body_b_cam_vibrate_anim3.png"
image jenny_vibrate 4 = "characters/jenny/layeredimage/jenny_body_b_cam_vibrate_anim4.png"

image jenny_monster 1 = "characters/jenny/layeredimage/jenny_body_b_cam_monster_anim1.png"
image jenny_monster 2 = "characters/jenny/layeredimage/jenny_body_b_cam_monster_anim2.png"
image jenny_monster 3 = "characters/jenny/layeredimage/jenny_body_b_cam_monster_anim3.png"
image jenny_monster 4 = "characters/jenny/layeredimage/jenny_body_b_cam_monster_anim4.png"

image jenny_body_b_magic_sit_stand_dressed = ConditionSwitch(
    "player.location == L_home_diningroom", "characters/jenny/layeredimage/jenny_body_b_breakfast_dressed[M_jenny.pregnancy.to_string].png",
    "player.location == L_home_sisbedroom", "characters/jenny/layeredimage/jenny_body_b_dressed[M_jenny.pregnancy.to_string].png",
    "True", "characters/jenny/layeredimage/jenny_body_b_swimsuit[M_jenny.pregnancy.to_string].png")

image jenny_face_talk_f_magic_sit_stand_grin = ConditionSwitch(
    "player.location == L_home_diningroom", Transform("characters/jenny/layeredimage/jenny_face_talk_f_grin.png",xzoom=-.76,yzoom=.76,xoffset=129,yoffset=144),
    "True", "characters/jenny/layeredimage/jenny_face_talk_f_grin.png")
image jenny_face_f_magic_sit_stand_grin = ConditionSwitch(
    "player.location == L_home_diningroom", Transform("characters/jenny/layeredimage/jenny_face_f_grin.png",xzoom=-.76,yzoom=.76,xoffset=129,yoffset=144),
    "True", "characters/jenny/layeredimage/jenny_face_f_grin.png")
image jenny_face_f_magic_sit_stand_laugh = ConditionSwitch(
    "player.location == L_home_diningroom", Transform("characters/jenny/layeredimage/jenny_face_f_laugh.png",xzoom=-.76,yzoom=.76,xoffset=129,yoffset=144),
    "True", "characters/jenny/layeredimage/jenny_face_f_laugh.png")
image jenny_face_f_magic_sit_stand_eyeroll = ConditionSwitch(
    "player.location == L_home_diningroom", Transform("characters/jenny/layeredimage/jenny_face_f_eyeroll.png",xzoom=-.76,yzoom=.76,xoffset=129,yoffset=144),
    "True", "characters/jenny/layeredimage/jenny_face_f_eyeroll.png")
image jenny_face_talk_f_magic_sit_stand_upset = ConditionSwitch(
    "player.location == L_home_diningroom", Transform("characters/jenny/layeredimage/jenny_face_talk_f_upset.png",xzoom=-.76,yzoom=.76,xoffset=129,yoffset=144),
    "True", "characters/jenny/layeredimage/jenny_face_talk_f_upset.png")
image jenny_face_f_magic_sit_stand_upset = ConditionSwitch(
    "player.location == L_home_diningroom", Transform("characters/jenny/layeredimage/jenny_face_f_upset.png",xzoom=-.76,yzoom=.76,xoffset=129,yoffset=144),
    "True", "characters/jenny/layeredimage/jenny_face_f_upset.png")
image jenny_face_talk_f_magic_sit_stand_angry = ConditionSwitch(
    "player.location == L_home_diningroom", Transform("characters/jenny/layeredimage/jenny_face_talk_f_angry.png",xzoom=-.76,yzoom=.76,xoffset=129,yoffset=144),
    "True", "characters/jenny/layeredimage/jenny_face_talk_f_angry.png")
image jenny_face_f_magic_sit_stand_angry = ConditionSwitch(
    "player.location == L_home_diningroom", Transform("characters/jenny/layeredimage/jenny_face_f_angry.png",xzoom=-.76,yzoom=.76,xoffset=129,yoffset=144),
    "True", "characters/jenny/layeredimage/jenny_face_f_angry.png")
image jenny_face_talk_f_magic_sit_stand_phone_upset = ConditionSwitch(
    "player.location == L_home_diningroom", Transform("characters/jenny/layeredimage/jenny_face_talk_f_upset_down.png",xzoom=-.76,yzoom=.76,xoffset=129,yoffset=144),
    "True", "characters/jenny/layeredimage/jenny_face_talk_f_gross_down.png")
image jenny_face_f_magic_sit_stand_phone_upset = ConditionSwitch(
    "player.location == L_home_diningroom", Transform("characters/jenny/layeredimage/jenny_face_f_upset_down.png",xzoom=-.76,yzoom=.76,xoffset=129,yoffset=144),
    "True", "characters/jenny/layeredimage/jenny_face_f_gross_down.png")
image jenny_face_talk_f_magic_sit_stand_gross = ConditionSwitch(
    "player.location == L_home_diningroom", Transform("characters/jenny/layeredimage/jenny_face_talk_f_gross.png",xzoom=-.76,yzoom=.76,xoffset=129,yoffset=144),
    "True", "characters/jenny/layeredimage/jenny_face_talk_f_gross.png")
image jenny_face_f_magic_sit_stand_gross = ConditionSwitch(
    "player.location == L_home_diningroom", Transform("characters/jenny/layeredimage/jenny_face_f_gross.png",xzoom=-.76,yzoom=.76,xoffset=129,yoffset=144),
    "True", "characters/jenny/layeredimage/jenny_face_f_gross.png")
image jenny_face_f_magic_sit_stand_surprised = ConditionSwitch(
    "player.location == L_home_diningroom", Transform("characters/jenny/layeredimage/jenny_face_f_surprised.png",xzoom=-.76,yzoom=.76,xoffset=129,yoffset=144),
    "True", "characters/jenny/layeredimage/jenny_face_f_surprised.png")
image jenny_face_talk_f_magic_sit_stand_sad = ConditionSwitch(
    "player.location == L_home_diningroom", Transform("characters/jenny/layeredimage/jenny_face_talk_f_sad.png",xzoom=-.76,yzoom=.76,xoffset=129,yoffset=144),
    "True", "characters/jenny/layeredimage/jenny_face_talk_f_sad.png")
image jenny_face_f_magic_sit_stand_sad = ConditionSwitch(
    "player.location == L_home_diningroom", Transform("characters/jenny/layeredimage/jenny_face_f_sad.png",xzoom=-.76,yzoom=.76,xoffset=129,yoffset=144),
    "True", "characters/jenny/layeredimage/jenny_face_f_sad.png")
image jenny_face_talk_f_magic_sit_stand_normal = ConditionSwitch(
    "player.location == L_home_diningroom", Transform("characters/jenny/layeredimage/jenny_face_talk_f_normal.png",xzoom=-.76,yzoom=.76,xoffset=129,yoffset=144),
    "True", "characters/jenny/layeredimage/jenny_face_talk_f_normal.png")
image jenny_face_f_magic_sit_stand_normal = ConditionSwitch(
    "player.location == L_home_diningroom", Transform("characters/jenny/layeredimage/jenny_face_f_normal.png",xzoom=-.76,yzoom=.76,xoffset=129,yoffset=144),
    "True", "characters/jenny/layeredimage/jenny_face_f_normal.png")
image jenny_face_talk_f_magic_sit_stand_sexy = ConditionSwitch(
    "player.location == L_home_diningroom", Transform("characters/jenny/layeredimage/jenny_face_talk_f_sexy.png",xzoom=-.76,yzoom=.76,xoffset=129,yoffset=144),
    "True", "characters/jenny/layeredimage/jenny_face_talk_f_sexy.png")
image jenny_face_f_magic_sit_stand_sexy = ConditionSwitch(
    "player.location == L_home_diningroom", Transform("characters/jenny/layeredimage/jenny_face_f_sexy.png",xzoom=-.76,yzoom=.76,xoffset=129,yoffset=144),
    "True", "characters/jenny/layeredimage/jenny_face_f_sexy.png")

image jenny_arms_a_magic_sit_stand_hip_spoon = ConditionSwitch(
    "player.location == L_home_diningroom", "characters/jenny/layeredimage/jenny_arms_breakfast_dressed_a_spoon.png",
    "player.location == L_home_sisbedroom", "characters/jenny/layeredimage/jenny_arms_dressed_a_hips.png",
    "True", "characters/jenny/layeredimage/jenny_arms_swimsuit_a_hips.png")
image jenny_arms_a_magic_sit_stand_belly_touch = ConditionSwitch(
    "player.location == L_home_diningroom", "characters/jenny/layeredimage/jenny_arms_breakfast_dressed_a_pregnant_touch.png",
    "player.location == L_home_sisbedroom", "characters/jenny/layeredimage/jenny_arms_dressed_a_pregnant_touch.png",
    "True", "characters/jenny/layeredimage/jenny_arms_swimsuit_a_pregnant_touch.png")
image jenny_arms_a_magic_sit_stand_phone = ConditionSwitch(
    "player.location == L_home_diningroom", "jenny_arms_breakfast_dressed_a_phone[M_jenny.pregnancy.to_string]",
    "player.location == L_home_sisbedroom", "jenny_arms_dressed_a_phone[M_jenny.pregnancy.to_string]",
    "True", "jenny_arms_swimsuit_a_phone[M_jenny.pregnancy.to_string]")
image jenny_arms_a_magic_sit_stand_crossed = ConditionSwitch(
    "player.location == L_home_diningroom", "jenny_arms_breakfast_dressed_a_crossed[M_jenny.pregnancy.to_string]",
    "player.location == L_home_sisbedroom", "jenny_arms_dressed_a_crossed[M_jenny.pregnancy.to_string]",
    "True", "jenny_arms_swimsuit_a_crossed[M_jenny.pregnancy.to_string]")


image jenny_hj_mc = ConditionSwitch(
    "M_jenny.get('cam show mask') == True", "characters/jenny/layeredimage/jenny_body_b_hj_mc_mask.png",
    "True", "characters/jenny/layeredimage/jenny_body_b_hj_mc.png")

image jenny_hj 1 = "characters/jenny/layeredimage/jenny_body_b_hj_anim1.png"
image jenny_hj 2 = "characters/jenny/layeredimage/jenny_body_b_hj_anim2.png"
image jenny_hj 3 = "characters/jenny/layeredimage/jenny_body_b_hj_anim3.png"
image jenny_hj 4 = "characters/jenny/layeredimage/jenny_body_b_hj_anim4.png"
image jenny_hj 5 = "characters/jenny/layeredimage/jenny_body_b_hj_anim5.png"

image jenny_hj_mc cum = ConditionSwitch(
    "M_jenny.get('cam show mask') == True", "characters/jenny/layeredimage/jenny_body_b_hj_cum_mask.png",
    "True", "characters/jenny/layeredimage/jenny_body_b_hj_cum.png")

image jenny_hj_cum:
    Transform("characters/jenny/layeredimage/jenny_body_b_hj_cum_shoot1.png")
    pause .25
    Transform("characters/jenny/layeredimage/jenny_body_b_hj_cum_shoot2.png")
    pause .25
    Transform("characters/jenny/layeredimage/jenny_body_b_hj_cum_shoot3.png")
    pause .25


image jenny_bj 1 = "characters/jenny/layeredimage/jenny_sex_bj_anim01.png"
image jenny_bj 2 = "characters/jenny/layeredimage/jenny_sex_bj_anim02.png"
image jenny_bj 3 = "characters/jenny/layeredimage/jenny_sex_bj_anim03.png"
image jenny_bj 4 = "characters/jenny/layeredimage/jenny_sex_bj_anim04.png"
image jenny_bj 5 = "characters/jenny/layeredimage/jenny_sex_bj_anim05.png"
image jenny_bj 6 = "characters/jenny/layeredimage/jenny_sex_bj_anim06.png"
image jenny_bj 7 = "characters/jenny/layeredimage/jenny_sex_bj_anim07.png"
image jenny_bj 8 = "characters/jenny/layeredimage/jenny_sex_bj_anim08.png"
image jenny_bj 9 = "characters/jenny/layeredimage/jenny_sex_bj_anim09.png"

image jenny_bj cum:
    Transform("characters/jenny/layeredimage/jenny_sex_bj_cum1.png")
    pause .4
    Transform("characters/jenny/layeredimage/jenny_sex_bj_cum2.png")
    pause .8
    Transform("characters/jenny/layeredimage/jenny_sex_bj_cum1.png")
    pause .4
    Transform("characters/jenny/layeredimage/jenny_sex_bj_cum2.png")
    pause .4

image jenny_body_b_sleep_side_grope:
    Transform("characters/jenny/layeredimage/jenny_body_b_sleep_side_grope1.png")
    pause .4
    Transform("characters/jenny/layeredimage/jenny_body_b_sleep_side_grope2.png")
    pause .4
    repeat

image jenny_body_b_sleep_side_grope_shirtup:
    Transform("characters/jenny/layeredimage/jenny_body_b_sleep_side_grope1_shirtup.png")
    pause .4
    Transform("characters/jenny/layeredimage/jenny_body_b_sleep_side_grope2_shirtup.png")
    pause .4
    repeat

image jenny_body_b_sleep_side_grope_hump_shirtup:
    Transform("characters/jenny/layeredimage/jenny_body_b_sleep_side_grope1_shirtup.png")
    pause .4
    Transform("characters/jenny/layeredimage/jenny_body_b_sleep_side_grope2_hump_shirtup.png")
    pause .4
    repeat

image jenny_arms_a_sleep_side_grope:
    'characters/jenny/layeredimage/jenny_arms_a_sleep_side_grope1.png'
    .4
    'characters/jenny/layeredimage/jenny_arms_a_sleep_side_grope2.png'
    .4
    repeat


image jenny_body_b_couch_clit:
    Transform("characters/jenny/layeredimage/jenny_body_b_couch_clit1.png")
    pause .2
    Transform("characters/jenny/layeredimage/jenny_body_b_couch_clit2.png")
    pause .2
    Transform("characters/jenny/layeredimage/jenny_body_b_couch_clit3.png")
    pause .2
    Transform("characters/jenny/layeredimage/jenny_body_b_couch_clit4.png")
    pause .2
    repeat


image jenny_couch_sex cumshot = "characters/jenny/layeredimage/jenny_sex_couch_cumshot.png"
image jenny_couch_sex pullout 1 = "characters/jenny/layeredimage/jenny_sex_couch_pullout1.png"
image jenny_couch_sex pullout 2 = "characters/jenny/layeredimage/jenny_sex_couch_pullout2.png"

image jenny_couch_sex cum 2 = "characters/jenny/layeredimage/jenny_sex_couch_cum2.png"

image jenny_couch_sex cum:
    Transform("characters/jenny/layeredimage/jenny_sex_couch_cum1.png")
    pause .4
    Transform("characters/jenny/layeredimage/jenny_sex_couch_cum2.png")
    pause .8
    Transform("characters/jenny/layeredimage/jenny_sex_couch_cum1.png")
    pause .4
    Transform("characters/jenny/layeredimage/jenny_sex_couch_cum2.png")
    pause .4
    repeat

image jenny_couch_sex 1 = "characters/jenny/layeredimage/jenny_sex_couch_anim01.png"
image jenny_couch_sex 2 = "characters/jenny/layeredimage/jenny_sex_couch_anim02.png"
image jenny_couch_sex 3 = "characters/jenny/layeredimage/jenny_sex_couch_anim03.png"
image jenny_couch_sex 4 = "characters/jenny/layeredimage/jenny_sex_couch_anim04.png"
image jenny_couch_sex 5 = "characters/jenny/layeredimage/jenny_sex_couch_anim05.png"
image jenny_couch_sex 6 = "characters/jenny/layeredimage/jenny_sex_couch_anim06.png"
image jenny_couch_sex 7 = "characters/jenny/layeredimage/jenny_sex_couch_anim07.png"
image jenny_couch_sex 8 = "characters/jenny/layeredimage/jenny_sex_couch_anim08.png"


image jenny_lick_shirt 1 = "characters/jenny/char_jenny_sex_139.png"
image jenny_lick_shirt 2 = "characters/jenny/char_jenny_sex_140.png"
image jenny_lick_shirt 3 = "characters/jenny/char_jenny_sex_141.png"
image jenny_lick_shirt 4 = "characters/jenny/char_jenny_sex_142.png"


image jenny_lick 1 = "characters/jenny/char_jenny_sex_139b.png"
image jenny_lick 2 = "characters/jenny/char_jenny_sex_140b.png"
image jenny_lick 3 = "characters/jenny/char_jenny_sex_141b.png"
image jenny_lick 4 = "characters/jenny/char_jenny_sex_142b.png"


image jenny_mc_room_sex 1 = "characters/jenny/layeredimage/jenny_sex_visit_anim_01.png"
image jenny_mc_room_sex 2 = "characters/jenny/layeredimage/jenny_sex_visit_anim_02.png"
image jenny_mc_room_sex 3 = "characters/jenny/layeredimage/jenny_sex_visit_anim_03.png"
image jenny_mc_room_sex 4 = "characters/jenny/layeredimage/jenny_sex_visit_anim_04.png"
image jenny_mc_room_sex 5 = "characters/jenny/layeredimage/jenny_sex_visit_anim_05.png"
image jenny_mc_room_sex 6 = "characters/jenny/layeredimage/jenny_sex_visit_anim_06.png"
image jenny_mc_room_sex 7 = "characters/jenny/layeredimage/jenny_sex_visit_anim_07.png"
image jenny_mc_room_sex 8 = "characters/jenny/layeredimage/jenny_sex_visit_anim_08.png"
image jenny_mc_room_sex 9 = "characters/jenny/layeredimage/jenny_sex_visit_anim_09.png"

image jenny_mc_room_sex cum 1 = "characters/jenny/layeredimage/jenny_sex_visit_cum1.png"
image jenny_mc_room_sex cum 2 = "characters/jenny/layeredimage/jenny_sex_visit_cum2.png"
image jenny_mc_room_sex cumshot = "characters/jenny/layeredimage/jenny_sex_visit_cumshot.png"
image jenny_mc_room_sex insert = "characters/jenny/layeredimage/jenny_sex_visit_insert.png"
image jenny_mc_room_sex pullout = "characters/jenny/layeredimage/jenny_sex_visit_pullout.png"

image jenny_overlay_o_visit_cumshot:
    Transform("characters/jenny/layeredimage/jenny_overlay_o_visit_cumshot1.png")
    pause .4
    Transform("characters/jenny/layeredimage/jenny_overlay_o_visit_cumshot2.png")
    pause .4


image jenny_arms_visit_sit_a_stroke:
    Transform("characters/jenny/layeredimage/jenny_arms_visit_sit_a_stroke1.png")
    pause .4
    Transform("characters/jenny/layeredimage/jenny_arms_visit_sit_a_stroke2.png")
    pause .4
    repeat


image jenny_shower_bj 1 = "characters/jenny/layeredimage/jenny_sex_shower_bj_anim01.png"
image jenny_shower_bj 2 = "characters/jenny/layeredimage/jenny_sex_shower_bj_anim02.png"
image jenny_shower_bj 3 = "characters/jenny/layeredimage/jenny_sex_shower_bj_anim03.png"
image jenny_shower_bj 4 = "characters/jenny/layeredimage/jenny_sex_shower_bj_anim04.png"
image jenny_shower_bj 5 = "characters/jenny/layeredimage/jenny_sex_shower_bj_anim05.png"
image jenny_shower_bj 6 = "characters/jenny/layeredimage/jenny_sex_shower_bj_anim06.png"
image jenny_shower_bj 7 = "characters/jenny/layeredimage/jenny_sex_shower_bj_anim07.png"

image jenny_shower_bj_deep 1 = "characters/jenny/layeredimage/jenny_sex_shower_bj_deep1.png"
image jenny_shower_bj_deep 2 = "characters/jenny/layeredimage/jenny_sex_shower_bj_deep2.png"

image jenny_shower_bj pre_talk = "characters/jenny/layeredimage/jenny_sex_shower_bj_pre_talk.png"
image jenny_shower_bj pre_look = "characters/jenny/layeredimage/jenny_sex_shower_bj_pre_look.png"
image jenny_shower_bj cum = "characters/jenny/layeredimage/jenny_sex_shower_bj_cum.png"
image jenny_shower_bj after = "characters/jenny/layeredimage/jenny_sex_shower_bj_after.png"

image jenny_shower_bj_mc = "characters/jenny/layeredimage/jenny_sex_shower_bj_mc.png"


image jenny_cheer_sex_tied_insert_mask = Composite(
    (1024,768),
    (0,0), "jenny_sex_bed_tied_insert",
    (0,0), "jenny_sex_bed_tied_insert_mask")

image jenny_cheer_sex tied insert = ConditionSwitch( 
    "M_jenny.get('cam show mask') == True", "jenny_cheer_sex_tied_insert_mask",
    "True", "jenny_sex_bed_tied_insert")

image jenny_cheer_sex_mc tied cumshot initial = "jenny_sex_bed_tied_cumshot_dick1"

image jenny_cheer_sex_mc tied cumshot:
    Transform("jenny_sex_bed_tied_cumshot_dick1")
    pause .4
    Transform("jenny_sex_bed_tied_cumshot_dick2")
    pause .4

image jenny_cheer_sex_tied_pullout_1_mask = Composite(
    (1024,768),
    (0,0), "jenny_sex_bed_tied_pullout1",
    (0,0), "jenny_sex_bed_tied_pullout1_mask")
image jenny_cheer_sex_tied_pullout_2_mask = Composite(
    (1024,768),
    (0,0), "jenny_sex_bed_tied_pullout2",
    (0,0), "jenny_sex_bed_tied_pullout2_mask")
image jenny_cheer_sex_tied_pullout_3_mask = Composite(
    (1024,768),
    (0,0), "jenny_sex_bed_tied_pullout3",
    (0,0), "jenny_sex_bed_tied_pullout3_mask")
image jenny_cheer_sex_tied_pullout_4_mask = Composite(
    (1024,768),
    (0,0), "jenny_sex_bed_tied_pullout4",
    (0,0), "jenny_sex_bed_tied_pullout4_mask")

image jenny_cheer_sex tied pullout 1 = ConditionSwitch( 
    "M_jenny.get('cam show mask') == True", "jenny_cheer_sex_tied_pullout_1_mask",
    "True", "jenny_sex_bed_tied_pullout1")
image jenny_cheer_sex tied pullout 2 = ConditionSwitch( 
    "M_jenny.get('cam show mask') == True", "jenny_cheer_sex_tied_pullout_2_mask",
    "True", "jenny_sex_bed_tied_pullout2")
image jenny_cheer_sex tied pullout 3 = ConditionSwitch( 
    "M_jenny.get('cam show mask') == True", "jenny_cheer_sex_tied_pullout_3_mask",
    "True", "jenny_sex_bed_tied_pullout3")
image jenny_cheer_sex tied pullout 4 = ConditionSwitch( 
    "M_jenny.get('cam show mask') == True", "jenny_cheer_sex_tied_pullout_4_mask",
    "True", "jenny_sex_bed_tied_pullout4")

image jenny_cheer_sex_tied_cumshot_mask = Composite(
    (1024,768),
    (0,0), "jenny_sex_bed_tied_cumshot",
    (0,0), "jenny_sex_bed_tied_cumshot_mask")

image jenny_cheer_sex tied cumshot = ConditionSwitch( 
    "M_jenny.get('cam show mask') == True", "jenny_cheer_sex_tied_cumshot_mask",
    "True", "jenny_sex_bed_tied_cumshot")

image jenny_cheer_sex_tied_cum_1_mask = Composite(
    (1024,768),
    (0,0), "jenny_sex_bed_tied_cum1",
    (0,0), "jenny_sex_bed_tied_cum1_mask")
image jenny_cheer_sex_tied_cum_2_mask = Composite(
    (1024,768),
    (0,0), "jenny_sex_bed_tied_cum2",
    (0,0), "jenny_sex_bed_tied_cum2_mask")

image jenny_cheer_sex tied cum 1 = ConditionSwitch( 
    "M_jenny.get('cam show mask') == True", "jenny_cheer_sex_tied_cum_1_mask",
    "True", "jenny_sex_bed_tied_cum1")
image jenny_cheer_sex tied cum 2 = ConditionSwitch( 
    "M_jenny.get('cam show mask') == True", "jenny_cheer_sex_tied_cum_2_mask",
    "True", "jenny_sex_bed_tied_cum2")

image jenny_cheer_sex tied cum:
    Transform("jenny_cheer_sex tied cum 1")
    pause .4
    Transform("jenny_cheer_sex tied cum 2")
    pause .4
    repeat

image jenny_cheer_sex_tied_mask 1 = "characters/jenny/layeredimage/jenny_sex_bed_tied_anim01_mask.png"
image jenny_cheer_sex_tied_mask 2 = "characters/jenny/layeredimage/jenny_sex_bed_tied_anim02_mask.png"
image jenny_cheer_sex_tied_mask 3 = "characters/jenny/layeredimage/jenny_sex_bed_tied_anim03_mask.png"
image jenny_cheer_sex_tied_mask 4 = "characters/jenny/layeredimage/jenny_sex_bed_tied_anim04_mask.png"
image jenny_cheer_sex_tied_mask 5 = "characters/jenny/layeredimage/jenny_sex_bed_tied_anim05_mask.png"
image jenny_cheer_sex_tied_mask 6 = "characters/jenny/layeredimage/jenny_sex_bed_tied_anim06_mask.png"
image jenny_cheer_sex_tied_mask 7 = "characters/jenny/layeredimage/jenny_sex_bed_tied_anim07_mask.png"
image jenny_cheer_sex_tied_mask 8 = "characters/jenny/layeredimage/jenny_sex_bed_tied_anim08_mask.png"
image jenny_cheer_sex_tied_mask 9 = "characters/jenny/layeredimage/jenny_sex_bed_tied_anim09_mask.png"
image jenny_cheer_sex_tied_mask 10 = "characters/jenny/layeredimage/jenny_sex_bed_tied_anim10_mask.png"
image jenny_cheer_sex_tied_mask 11 = "characters/jenny/layeredimage/jenny_sex_bed_tied_anim11_mask.png"
image jenny_cheer_sex_tied_mask 12 = "characters/jenny/layeredimage/jenny_sex_bed_tied_anim12_mask.png"
image jenny_cheer_sex_tied_mask 13 = "characters/jenny/layeredimage/jenny_sex_bed_tied_anim13_mask.png"
image jenny_cheer_sex_tied_mask 14 = "characters/jenny/layeredimage/jenny_sex_bed_tied_anim14_mask.png"
image jenny_cheer_sex_tied_mask 15 = "characters/jenny/layeredimage/jenny_sex_bed_tied_anim15_mask.png"
image jenny_cheer_sex_tied_mask 16 = "characters/jenny/layeredimage/jenny_sex_bed_tied_anim16_mask.png"
image jenny_cheer_sex_tied_mask 17 = "characters/jenny/layeredimage/jenny_sex_bed_tied_anim17_mask.png"
image jenny_cheer_sex_tied_mask 18 = "characters/jenny/layeredimage/jenny_sex_bed_tied_anim18_mask.png"

image jenny_cheer_sex_tied 1 = "characters/jenny/layeredimage/jenny_sex_bed_tied_anim01.png"
image jenny_cheer_sex_tied 2 = "characters/jenny/layeredimage/jenny_sex_bed_tied_anim02.png"
image jenny_cheer_sex_tied 3 = "characters/jenny/layeredimage/jenny_sex_bed_tied_anim03.png"
image jenny_cheer_sex_tied 4 = "characters/jenny/layeredimage/jenny_sex_bed_tied_anim04.png"
image jenny_cheer_sex_tied 5 = "characters/jenny/layeredimage/jenny_sex_bed_tied_anim05.png"
image jenny_cheer_sex_tied 6 = "characters/jenny/layeredimage/jenny_sex_bed_tied_anim06.png"
image jenny_cheer_sex_tied 7 = "characters/jenny/layeredimage/jenny_sex_bed_tied_anim07.png"
image jenny_cheer_sex_tied 8 = "characters/jenny/layeredimage/jenny_sex_bed_tied_anim08.png"
image jenny_cheer_sex_tied 9 = "characters/jenny/layeredimage/jenny_sex_bed_tied_anim09.png"
image jenny_cheer_sex_tied 10 = "characters/jenny/layeredimage/jenny_sex_bed_tied_anim10.png"
image jenny_cheer_sex_tied 11 = "characters/jenny/layeredimage/jenny_sex_bed_tied_anim11.png"
image jenny_cheer_sex_tied 12 = "characters/jenny/layeredimage/jenny_sex_bed_tied_anim12.png"
image jenny_cheer_sex_tied 13 = "characters/jenny/layeredimage/jenny_sex_bed_tied_anim13.png"
image jenny_cheer_sex_tied 14 = "characters/jenny/layeredimage/jenny_sex_bed_tied_anim14.png"
image jenny_cheer_sex_tied 15 = "characters/jenny/layeredimage/jenny_sex_bed_tied_anim15.png"
image jenny_cheer_sex_tied 16 = "characters/jenny/layeredimage/jenny_sex_bed_tied_anim16.png"
image jenny_cheer_sex_tied 17 = "characters/jenny/layeredimage/jenny_sex_bed_tied_anim17.png"
image jenny_cheer_sex_tied 18 = "characters/jenny/layeredimage/jenny_sex_bed_tied_anim18.png"

image jenny_cheer_sex_free_mask 1 = "characters/jenny/layeredimage/jenny_sex_bed_free_anim01_mask.png"
image jenny_cheer_sex_free_mask 2 = "characters/jenny/layeredimage/jenny_sex_bed_free_anim02_mask.png"
image jenny_cheer_sex_free_mask 3 = "characters/jenny/layeredimage/jenny_sex_bed_free_anim03_mask.png"
image jenny_cheer_sex_free_mask 4 = "characters/jenny/layeredimage/jenny_sex_bed_free_anim04_mask.png"
image jenny_cheer_sex_free_mask 5 = "characters/jenny/layeredimage/jenny_sex_bed_free_anim05_mask.png"

image jenny_cheer_sex_free 1 = "characters/jenny/layeredimage/jenny_sex_bed_free_anim01.png"
image jenny_cheer_sex_free 2 = "characters/jenny/layeredimage/jenny_sex_bed_free_anim02.png"
image jenny_cheer_sex_free 3 = "characters/jenny/layeredimage/jenny_sex_bed_free_anim03.png"
image jenny_cheer_sex_free 4 = "characters/jenny/layeredimage/jenny_sex_bed_free_anim04.png"
image jenny_cheer_sex_free 5 = "characters/jenny/layeredimage/jenny_sex_bed_free_anim05.png"

image jenny_cheer_sex_free_break_mask = Composite(
    (1024,768),
    (0,0), "jenny_sex_bed_free_break",
    (0,0), "jenny_sex_bed_free_break_mask")

image jenny_cheer_sex free break = ConditionSwitch( 
    "M_jenny.get('cam show mask') == True", "jenny_cheer_sex_free_break_mask",
    "True", "jenny_sex_bed_free_break")

image jenny_cheer_sex_free_pullout_1_mask = Composite(
    (1024,768),
    (0,0), "jenny_sex_bed_free_pullout1",
    (0,0), "jenny_sex_bed_free_pullout1_mask")
image jenny_cheer_sex_free_pullout_2_mask = Composite(
    (1024,768),
    (0,0), "jenny_sex_bed_free_pullout2",
    (0,0), "jenny_sex_bed_free_pullout2_mask")
image jenny_cheer_sex_free_pullout_3_mask = Composite(
    (1024,768),
    (0,0), "jenny_sex_bed_free_pullout3",
    (0,0), "jenny_sex_bed_free_pullout3_mask")
image jenny_cheer_sex_free_pullout_4_mask = Composite(
    (1024,768),
    (0,0), "jenny_sex_bed_free_pullout4",
    (0,0), "jenny_sex_bed_free_pullout4_mask")

image jenny_cheer_sex free pullout 1 = ConditionSwitch( 
    "M_jenny.get('cam show mask') == True", "jenny_cheer_sex_free_pullout_1_mask",
    "True", "jenny_sex_bed_free_pullout1")
image jenny_cheer_sex free pullout 2 = ConditionSwitch( 
    "M_jenny.get('cam show mask') == True", "jenny_cheer_sex_free_pullout_2_mask",
    "True", "jenny_sex_bed_free_pullout2")
image jenny_cheer_sex free pullout 3 = ConditionSwitch( 
    "M_jenny.get('cam show mask') == True", "jenny_cheer_sex_free_pullout_3_mask",
    "True", "jenny_sex_bed_free_pullout3")
image jenny_cheer_sex free pullout 4 = ConditionSwitch( 
    "M_jenny.get('cam show mask') == True", "jenny_cheer_sex_free_pullout_4_mask",
    "True", "jenny_sex_bed_free_pullout4")

image jenny_cheer_sex_free_cumshot_mask = Composite(
    (1024,768),
    (0,0), "jenny_sex_bed_free_cumshot",
    (0,0), "jenny_sex_bed_free_cumshot_mask")

image jenny_cheer_sex free cumshot = ConditionSwitch( 
    "M_jenny.get('cam show mask') == True", "jenny_cheer_sex_free_cumshot_mask",
    "True", "jenny_sex_bed_free_cumshot")

image jenny_cheer_sex_free_cum_1_mask = Composite(
    (1024,768),
    (0,0), "jenny_sex_bed_free_cum1",
    (0,0), "jenny_sex_bed_free_cum1_mask")
image jenny_cheer_sex_free_cum_2_mask = Composite(
    (1024,768),
    (0,0), "jenny_sex_bed_free_cum2",
    (0,0), "jenny_sex_bed_free_cum2_mask")

image jenny_cheer_sex free cum 1 = ConditionSwitch( 
    "M_jenny.get('cam show mask') == True", "jenny_cheer_sex_free_cum_1_mask",
    "True", "jenny_sex_bed_free_cum1")
image jenny_cheer_sex free cum 2 = ConditionSwitch( 
    "M_jenny.get('cam show mask') == True", "jenny_cheer_sex_free_cum_2_mask",
    "True", "jenny_sex_bed_free_cum2")

image jenny_cheer_sex free cum:
    Transform("jenny_cheer_sex free cum 1")
    pause .4
    Transform("jenny_cheer_sex free cum 2")
    pause .4
    repeat


image jenny_shower_sex cum:
    Transform("characters/jenny/layeredimage/jenny_sex_shower_cum1.png")
    pause .4
    Transform("characters/jenny/layeredimage/jenny_sex_shower_cum2.png")
    pause .4
    repeat

image jenny_shower_sex cum 2 = "characters/jenny/layeredimage/jenny_sex_shower_cum2.png"

image jenny_body_b_shower_butt1_with_face = Composite(
    (1024,768),
    (0,0), "characters/jenny/layeredimage/jenny_body_b_shower_butt1.png",
    (0,0), "characters/jenny/layeredimage/jenny_face_f_shower_butt1.png")

image jenny_body_b_shower_butt:
    Transform("jenny_body_b_shower_butt1_with_face")
    pause .3
    Transform("characters/jenny/layeredimage/jenny_body_b_shower_butt2.png")
    pause .3
    Transform("characters/jenny/layeredimage/jenny_body_b_shower_butt3.png")
    pause .3
    repeat

image jenny_shower_sex 1 = "characters/jenny/layeredimage/jenny_sex_shower_anim01.png"
image jenny_shower_sex 2 = "characters/jenny/layeredimage/jenny_sex_shower_anim02.png"
image jenny_shower_sex 3 = "characters/jenny/layeredimage/jenny_sex_shower_anim03.png"
image jenny_shower_sex 4 = "characters/jenny/layeredimage/jenny_sex_shower_anim04.png"
image jenny_shower_sex 5 = "characters/jenny/layeredimage/jenny_sex_shower_anim05.png"
image jenny_shower_sex 6 = "characters/jenny/layeredimage/jenny_sex_shower_anim06.png"
image jenny_shower_sex 7 = "characters/jenny/layeredimage/jenny_sex_shower_anim07.png"
image jenny_shower_sex 8 = "characters/jenny/layeredimage/jenny_sex_shower_anim08.png"




layeredimage jenny_sex_table:
    group body auto:
        attribute b_default default

    group face auto:
        attribute f_back default

image player_jenny_diningroom_sex pre = "characters/anon/anon_sex_table_pre.png"
image player_jenny_diningroom_sex after = "characters/anon/anon_sex_table_after.png"
image player_jenny_diningroom_sex cumshot = "characters/anon/anon_sex_table_cumshot1.png"

image player_jenny_diningroom_flying_cum:
    Transform("characters/anon/anon_sex_table_cumshot2.png")
    pause .4
    Transform("characters/anon/anon_sex_table_cumshot3.png")
    pause .4

image jenny_diningroom_sex insert = "characters/jenny/layeredimage/jenny_sex_table_insert.png"
image jenny_diningroom_sex pullout = "characters/jenny/layeredimage/jenny_sex_table_pullout.png"

image jenny_diningroom_sex cum:
    Transform("characters/jenny/layeredimage/jenny_sex_table_cum1.png")
    pause .4
    Transform("characters/jenny/layeredimage/jenny_sex_table_cum2.png")
    pause .4
    repeat

image jenny_diningroom_sex cum2 = "characters/jenny/layeredimage/jenny_sex_table_cum2.png"

image jenny_diningroom_sex 1 = "characters/jenny/layeredimage/jenny_sex_table_anim01.png"
image jenny_diningroom_sex 2 = "characters/jenny/layeredimage/jenny_sex_table_anim02.png"
image jenny_diningroom_sex 3 = "characters/jenny/layeredimage/jenny_sex_table_anim03.png"
image jenny_diningroom_sex 4 = "characters/jenny/layeredimage/jenny_sex_table_anim04.png"
image jenny_diningroom_sex 5 = "characters/jenny/layeredimage/jenny_sex_table_anim05.png"
image jenny_diningroom_sex 6 = "characters/jenny/layeredimage/jenny_sex_table_anim06.png"
image jenny_diningroom_sex 7 = "characters/jenny/layeredimage/jenny_sex_table_anim07.png"
image jenny_diningroom_sex 8 = "characters/jenny/layeredimage/jenny_sex_table_anim08.png"
image jenny_diningroom_sex 9 = "characters/jenny/layeredimage/jenny_sex_table_anim09.png"


image player_jenny_sleeping_sex pre = "characters/jenny/layeredimage/jenny_sex_sleep_default_dick_pre.png"
image player_jenny_sleeping_sex after = "characters/jenny/layeredimage/jenny_sex_sleep_default_dick_after.png"
image jenny_sex_sleep_blanket = "characters/jenny/layeredimage/jenny_sex_sleep_blanket.png"

image player_jenny_sleeping_sex cum:
    Transform("characters/jenny/layeredimage/jenny_sex_sleep_default_dick_cumshot1.png")
    pause .4
    Transform("characters/jenny/layeredimage/jenny_sex_sleep_default_dick_cumshot2.png")
    pause .4
    Transform("characters/jenny/layeredimage/jenny_sex_sleep_default_dick_cumshot3.png")
    pause .4

image jenny_sleeping_sex insert = "characters/jenny/layeredimage/jenny_sex_sleep_insert.png"
image jenny_sleeping_sex pullout = "characters/jenny/layeredimage/jenny_sex_sleep_pullout.png"
image jenny_sleeping_sex default = "characters/jenny/layeredimage/jenny_sex_sleep_default.png"
image jenny_sleeping_sex cum1 = "characters/jenny/layeredimage/jenny_sex_sleep_cum1.png"

image jenny_sleeping_sex_face cum = "characters/jenny/layeredimage/jenny_sex_sleep_face_cum.png"
image jenny_sleeping_sex_face normal = "characters/jenny/layeredimage/jenny_sex_sleep_face_normal.png"
image jenny_sleeping_sex_face normal_talk = "characters/jenny/layeredimage/jenny_sex_sleep_face_normal_talk.png"
image jenny_sleeping_sex_face angry_talk = "characters/jenny/layeredimage/jenny_sex_sleep_face_angry_talk.png"

image jenny_sleeping_sex cum:
    Transform("characters/jenny/layeredimage/jenny_sex_sleep_cum1.png")
    pause .4
    Transform("characters/jenny/layeredimage/jenny_sex_sleep_cum2.png")
    pause .4
    repeat

image jenny_sleeping_sex cum2 = "characters/jenny/layeredimage/jenny_sex_sleep_cum2.png"

image jenny_sleeping_sex 1 = "characters/jenny/layeredimage/jenny_sex_sleep_anim01.png"
image jenny_sleeping_sex 2 = "characters/jenny/layeredimage/jenny_sex_sleep_anim02.png"
image jenny_sleeping_sex 3 = "characters/jenny/layeredimage/jenny_sex_sleep_anim03.png"
image jenny_sleeping_sex 4 = "characters/jenny/layeredimage/jenny_sex_sleep_anim04.png"
image jenny_sleeping_sex 5 = "characters/jenny/layeredimage/jenny_sex_sleep_anim05.png"
image jenny_sleeping_sex 6 = "characters/jenny/layeredimage/jenny_sex_sleep_anim06.png"
image jenny_sleeping_sex 7 = "characters/jenny/layeredimage/jenny_sex_sleep_anim07.png"
image jenny_sleeping_sex 8 = "characters/jenny/layeredimage/jenny_sex_sleep_anim08.png"
image jenny_sleeping_sex 9 = "characters/jenny/layeredimage/jenny_sex_sleep_anim09.png"


image jenny_pool_sex_face normal_talk_down = "characters/jenny/layeredimage/jenny_sex_pool_face_normal_talk_down.png"
image jenny_pool_sex_face normal_down = "characters/jenny/layeredimage/jenny_sex_pool_face_normal_down.png"

image jenny_pool_sex pre = "characters/jenny/layeredimage/jenny_sex_pool_pre.png"
image jenny_pool_sex after = ConditionSwitch(
    "M_jenny.get('pool_clothes')", "characters/jenny/layeredimage/jenny_sex_pool_after.png",
    "True", "characters/jenny/layeredimage/jenny_sex_pool_after_naked.png")
image jenny_pool_sex pullout1 = ConditionSwitch(
    "M_jenny.get('pool_clothes')", "characters/jenny/layeredimage/jenny_sex_pool_pullout1.png",
    "True", "characters/jenny/layeredimage/jenny_sex_pool_pullout1_naked.png")

image player_jenny_pool flying_cum:
    Transform("characters/jenny/layeredimage/jenny_sex_pool_cumshot1.png")
    pause .4
    Transform("characters/jenny/layeredimage/jenny_sex_pool_cumshot2.png")
    pause .4
    Transform("characters/jenny/layeredimage/jenny_sex_pool_cumshot3.png")
    pause .4

image player_jenny_pool pullout2 = "characters/jenny/layeredimage/jenny_sex_pool_pullout2.png"
image player_jenny_pool pullout3 = "characters/jenny/layeredimage/jenny_sex_pool_pullout3.png"

image jenny_pool_sex insert = "characters/jenny/layeredimage/jenny_sex_pool_insert.png"

image jenny_pool_sex cum:
    'jenny_pool_sex cum1'
    pause .4
    'jenny_pool_sex cum2'
    pause .4
    repeat

image jenny_pool_sex cum1 = ConditionSwitch(
    "M_jenny.get('pool_clothes')", "characters/jenny/layeredimage/jenny_sex_pool_cum1.png",
    "True", "characters/jenny/layeredimage/jenny_sex_pool_cum1_naked.png")
image jenny_pool_sex cum2 = ConditionSwitch(
    "M_jenny.get('pool_clothes')", "characters/jenny/layeredimage/jenny_sex_pool_cum2.png",
    "True", "characters/jenny/layeredimage/jenny_sex_pool_cum2_naked.png")

image jenny_pool_sex 1 = "characters/jenny/layeredimage/jenny_sex_pool_anim_01.png"
image jenny_pool_sex 2 = "characters/jenny/layeredimage/jenny_sex_pool_anim_02.png"
image jenny_pool_sex 3 = "characters/jenny/layeredimage/jenny_sex_pool_anim_03.png"
image jenny_pool_sex 4 = "characters/jenny/layeredimage/jenny_sex_pool_anim_04.png"
image jenny_pool_sex 5 = "characters/jenny/layeredimage/jenny_sex_pool_anim_05.png"
image jenny_pool_sex 6 = "characters/jenny/layeredimage/jenny_sex_pool_anim_06.png"
image jenny_pool_sex 7 = "characters/jenny/layeredimage/jenny_sex_pool_anim_07.png"
image jenny_pool_sex 8 = "characters/jenny/layeredimage/jenny_sex_pool_anim_08.png"
image jenny_pool_sex 9 = "characters/jenny/layeredimage/jenny_sex_pool_anim_09.png"
image jenny_pool_sex 10 = "characters/jenny/layeredimage/jenny_sex_pool_anim_10.png"

image jenny_pool_sex_naked 1 = "characters/jenny/layeredimage/jenny_sex_pool_anim_01_naked.png"
image jenny_pool_sex_naked 2 = "characters/jenny/layeredimage/jenny_sex_pool_anim_02_naked.png"
image jenny_pool_sex_naked 3 = "characters/jenny/layeredimage/jenny_sex_pool_anim_03_naked.png"
image jenny_pool_sex_naked 4 = "characters/jenny/layeredimage/jenny_sex_pool_anim_04_naked.png"
image jenny_pool_sex_naked 5 = "characters/jenny/layeredimage/jenny_sex_pool_anim_05_naked.png"
image jenny_pool_sex_naked 6 = "characters/jenny/layeredimage/jenny_sex_pool_anim_06_naked.png"
image jenny_pool_sex_naked 7 = "characters/jenny/layeredimage/jenny_sex_pool_anim_07_naked.png"
image jenny_pool_sex_naked 8 = "characters/jenny/layeredimage/jenny_sex_pool_anim_08_naked.png"
image jenny_pool_sex_naked 9 = "characters/jenny/layeredimage/jenny_sex_pool_anim_09_naked.png"
image jenny_pool_sex_naked 10 = "characters/jenny/layeredimage/jenny_sex_pool_anim_10_naked.png"


init python hide:
    stem = 'jenny_sex_preg_anim'
    count = 7
    first = 3
    frames = tuple(i % count + 1 for i in xrange(first, first + count))
    for i in frames:
        renpy.image('{} {}'.format(stem, i),
                    'jenny_sex_preg_anim{:02}'.format(i))
    renpy.image(stem, AnimatedImage(stem, frames, M_jenny))


image jenny_sex_preg_cumshot = anim.TransitionAnimation(
    'jenny_sex_preg_cumshot01', .4, Dissolve(.4),
    'jenny_sex_preg_cumshot02', .4, Dissolve(.4),
    'jenny_sex_preg_cumshot03')


init python:
    for i in xrange(1, 15):
        renpy.image('jenny_sex_peep_closeup_anim {}'.format(i),
                    'jenny_sex_peep_closeup_anim{:02}'.format(i))

image jenny_solo_peephole_anim = AnimatedImage(
    'jenny_sex_peep_closeup_anim', (1,2,3,4,5,6,7,8,9,10,11,12,13,14), M_jenny)






image xray_jenny_diningroom_table:
    Transform("characters/xray/xray_left_back_01.png", zoom=0.75, xoffset=460, yoffset=160)
    pause 0.4
    Transform("characters/xray/xray_left_back_02.png", zoom=0.75, xoffset=460, yoffset=160)
    pause 0.4
    Transform("characters/xray/xray_left_back_03.png", zoom=0.75, xoffset=460, yoffset=160)
    pause 0.4
    Transform("characters/xray/xray_left_back_04.png", zoom=0.75, xoffset=460, yoffset=160)
    pause 0.4
    Transform("characters/xray/xray_left_back_05.png", zoom=0.75, xoffset=460, yoffset=160)
    pause 0.4
    Transform("characters/xray/xray_left_back_06.png", zoom=0.75, xoffset=460, yoffset=160)
    pause 0.4
    Transform("characters/xray/xray_left_back_07.png", zoom=0.75, xoffset=460, yoffset=160)
    pause 0.4
    Transform("characters/xray/xray_left_back_08.png", zoom=0.75, xoffset=460, yoffset=160)
    pause 0.4
    Transform("characters/xray/xray_left_back_09.png", zoom=0.75, xoffset=460, yoffset=160)
    pause 0.4
    Transform("characters/xray/xray_left_back_10.png", zoom=0.75, xoffset=460, yoffset=160)
    pause 0.4
    Transform("characters/xray/xray_left_back_11.png", zoom=0.75, xoffset=460, yoffset=160)
    pause 0.4
    Transform("characters/xray/xray_left_back_12.png", zoom=0.75, xoffset=460, yoffset=160)
    pause 0.4
    Transform("characters/xray/xray_left_back_13.png", zoom=0.75, xoffset=460, yoffset=160)
    pause 0.4
    Transform("characters/xray/xray_left_back_14.png", zoom=0.75, xoffset=460, yoffset=160)
    pause 0.4
    Transform("characters/xray/xray_left_back_15.png", zoom=0.75, xoffset=460, yoffset=160)
    pause 0.4
    Transform("characters/xray/xray_left_back_16.png", zoom=0.75, xoffset=460, yoffset=160)
    pause 0.4
    Transform("characters/xray/xray_left_back_17.png", zoom=0.75, xoffset=460, yoffset=160)
    pause 0.4
    Transform("characters/xray/xray_left_back_18.png", zoom=0.75, xoffset=460, yoffset=160)
    pause 2.0
    linear 2.5 alpha 0

image xray_jenny_pool:
    Transform("characters/xray/xray_under_01.png", xzoom=-.5, yzoom=.5, rotate=-50, xoffset=315, yoffset=230)
    pause 0.4
    Transform("characters/xray/xray_under_02.png", xzoom=-.5, yzoom=.5, rotate=-50, xoffset=315, yoffset=230)
    pause 0.4
    Transform("characters/xray/xray_under_03.png", xzoom=-.5, yzoom=.5, rotate=-50, xoffset=315, yoffset=230)
    pause 0.4
    Transform("characters/xray/xray_under_04.png", xzoom=-.5, yzoom=.5, rotate=-50, xoffset=315, yoffset=230)
    pause 0.4
    Transform("characters/xray/xray_under_05.png", xzoom=-.5, yzoom=.5, rotate=-50, xoffset=315, yoffset=230)
    pause 0.4
    Transform("characters/xray/xray_under_06.png", xzoom=-.5, yzoom=.5, rotate=-50, xoffset=315, yoffset=230)
    pause 0.4
    Transform("characters/xray/xray_under_07.png", xzoom=-.5, yzoom=.5, rotate=-50, xoffset=315, yoffset=230)
    pause 0.4
    Transform("characters/xray/xray_under_08.png", xzoom=-.5, yzoom=.5, rotate=-50, xoffset=315, yoffset=230)
    pause 0.4
    Transform("characters/xray/xray_under_09.png", xzoom=-.5, yzoom=.5, rotate=-50, xoffset=315, yoffset=230)
    pause 0.4
    Transform("characters/xray/xray_under_10.png", xzoom=-.5, yzoom=.5, rotate=-50, xoffset=315, yoffset=230)
    pause 0.4
    Transform("characters/xray/xray_under_11.png", xzoom=-.5, yzoom=.5, rotate=-50, xoffset=315, yoffset=230)
    pause 0.4
    Transform("characters/xray/xray_under_12.png", xzoom=-.5, yzoom=.5, rotate=-50, xoffset=315, yoffset=230)
    pause 0.4
    Transform("characters/xray/xray_under_13.png", xzoom=-.5, yzoom=.5, rotate=-50, xoffset=315, yoffset=230)
    pause 0.4
    Transform("characters/xray/xray_under_14.png", xzoom=-.5, yzoom=.5, rotate=-50, xoffset=315, yoffset=230)
    pause 0.4
    Transform("characters/xray/xray_under_15.png", xzoom=-.5, yzoom=.5, rotate=-50, xoffset=315, yoffset=230)
    pause 0.4
    Transform("characters/xray/xray_under_16.png", xzoom=-.5, yzoom=.5, rotate=-50, xoffset=315, yoffset=230)
    pause 0.4
    Transform("characters/xray/xray_under_17.png", xzoom=-.5, yzoom=.5, rotate=-50, xoffset=315, yoffset=230)
    pause 0.4
    Transform("characters/xray/xray_under_18.png", xzoom=-.5, yzoom=.5, rotate=-50, xoffset=315, yoffset=230)
    pause 2.0
    linear 2.5 alpha 0

image xray_jenny_jenny_bed:
    Transform("characters/xray/xray_under_01.png", xzoom=-.9, yzoom=.9, rotate=10, xoffset=100, yoffset=40)
    pause 0.4
    Transform("characters/xray/xray_under_02.png", xzoom=-.9, yzoom=.9, rotate=10, xoffset=100, yoffset=40)
    pause 0.4
    Transform("characters/xray/xray_under_03.png", xzoom=-.9, yzoom=.9, rotate=10, xoffset=100, yoffset=40)
    pause 0.4
    Transform("characters/xray/xray_under_04.png", xzoom=-.9, yzoom=.9, rotate=10, xoffset=100, yoffset=40)
    pause 0.4
    Transform("characters/xray/xray_under_05.png", xzoom=-.9, yzoom=.9, rotate=10, xoffset=100, yoffset=40)
    pause 0.4
    Transform("characters/xray/xray_under_06.png", xzoom=-.9, yzoom=.9, rotate=10, xoffset=100, yoffset=40)
    pause 0.4
    Transform("characters/xray/xray_under_07.png", xzoom=-.9, yzoom=.9, rotate=10, xoffset=100, yoffset=40)
    pause 0.4
    Transform("characters/xray/xray_under_08.png", xzoom=-.9, yzoom=.9, rotate=10, xoffset=100, yoffset=40)
    pause 0.4
    Transform("characters/xray/xray_under_09.png", xzoom=-.9, yzoom=.9, rotate=10, xoffset=100, yoffset=40)
    pause 0.4
    Transform("characters/xray/xray_under_10.png", xzoom=-.9, yzoom=.9, rotate=10, xoffset=100, yoffset=40)
    pause 0.4
    Transform("characters/xray/xray_under_11.png", xzoom=-.9, yzoom=.9, rotate=10, xoffset=100, yoffset=40)
    pause 0.4
    Transform("characters/xray/xray_under_12.png", xzoom=-.9, yzoom=.9, rotate=10, xoffset=100, yoffset=40)
    pause 0.4
    Transform("characters/xray/xray_under_13.png", xzoom=-.9, yzoom=.9, rotate=10, xoffset=100, yoffset=40)
    pause 0.4
    Transform("characters/xray/xray_under_14.png", xzoom=-.9, yzoom=.9, rotate=10, xoffset=100, yoffset=40)
    pause 0.4
    Transform("characters/xray/xray_under_15.png", xzoom=-.9, yzoom=.9, rotate=10, xoffset=100, yoffset=40)
    pause 0.4
    Transform("characters/xray/xray_under_16.png", xzoom=-.9, yzoom=.9, rotate=10, xoffset=100, yoffset=40)
    pause 0.4
    Transform("characters/xray/xray_under_17.png", xzoom=-.9, yzoom=.9, rotate=10, xoffset=100, yoffset=40)
    pause 0.4
    Transform("characters/xray/xray_under_18.png", xzoom=-.9, yzoom=.9, rotate=10, xoffset=100, yoffset=40)
    pause 2.0
    linear 2.5 alpha 0

image xray_jenny_cheer_bedroom:
    Transform("characters/xray/xray_under_01.png", zoom=.8, rotate=80, xoffset=190, yoffset=30)
    pause 0.4
    Transform("characters/xray/xray_under_02.png", zoom=.8, rotate=80, xoffset=190, yoffset=30)
    pause 0.4
    Transform("characters/xray/xray_under_03.png", zoom=.8, rotate=80, xoffset=190, yoffset=30)
    pause 0.4
    Transform("characters/xray/xray_under_04.png", zoom=.8, rotate=80, xoffset=190, yoffset=30)
    pause 0.4
    Transform("characters/xray/xray_under_05.png", zoom=.8, rotate=80, xoffset=190, yoffset=30)
    pause 0.4
    Transform("characters/xray/xray_under_06.png", zoom=.8, rotate=80, xoffset=190, yoffset=30)
    pause 0.4
    Transform("characters/xray/xray_under_07.png", zoom=.8, rotate=80, xoffset=190, yoffset=30)
    pause 0.4
    Transform("characters/xray/xray_under_08.png", zoom=.8, rotate=80, xoffset=190, yoffset=30)
    pause 0.4
    Transform("characters/xray/xray_under_09.png", zoom=.8, rotate=80, xoffset=190, yoffset=30)
    pause 0.4
    Transform("characters/xray/xray_under_10.png", zoom=.8, rotate=80, xoffset=190, yoffset=30)
    pause 0.4
    Transform("characters/xray/xray_under_11.png", zoom=.8, rotate=80, xoffset=190, yoffset=30)
    pause 0.4
    Transform("characters/xray/xray_under_12.png", zoom=.8, rotate=80, xoffset=190, yoffset=30)
    pause 0.4
    Transform("characters/xray/xray_under_13.png", zoom=.8, rotate=80, xoffset=190, yoffset=30)
    pause 0.4
    Transform("characters/xray/xray_under_14.png", zoom=.8, rotate=80, xoffset=190, yoffset=30)
    pause 0.4
    Transform("characters/xray/xray_under_15.png", zoom=.8, rotate=80, xoffset=190, yoffset=30)
    pause 0.4
    Transform("characters/xray/xray_under_16.png", zoom=.8, rotate=80, xoffset=190, yoffset=30)
    pause 0.4
    Transform("characters/xray/xray_under_17.png", zoom=.8, rotate=80, xoffset=190, yoffset=30)
    pause 0.4
    Transform("characters/xray/xray_under_18.png", zoom=.8, rotate=80, xoffset=190, yoffset=30)
    pause 2.0
    linear 2.5 alpha 0

image xray_jenny_mcbedroom:
    Transform("characters/xray/xray_top_01.png", zoom=.5 ,rotate=40, xoffset=370, yoffset=350)
    pause 0.4
    Transform("characters/xray/xray_top_02.png", zoom=.5 ,rotate=40, xoffset=370, yoffset=350)
    pause 0.4
    Transform("characters/xray/xray_top_03.png", zoom=.5 ,rotate=40, xoffset=370, yoffset=350)
    pause 0.4
    Transform("characters/xray/xray_top_04.png", zoom=.5 ,rotate=40, xoffset=370, yoffset=350)
    pause 0.4
    Transform("characters/xray/xray_top_05.png", zoom=.5 ,rotate=40, xoffset=370, yoffset=350)
    pause 0.4
    Transform("characters/xray/xray_top_06.png", zoom=.5 ,rotate=40, xoffset=370, yoffset=350)
    pause 0.4
    Transform("characters/xray/xray_top_07.png", zoom=.5 ,rotate=40, xoffset=370, yoffset=350)
    pause 0.4
    Transform("characters/xray/xray_top_08.png", zoom=.5 ,rotate=40, xoffset=370, yoffset=350)
    pause 0.4
    Transform("characters/xray/xray_top_09.png", zoom=.5 ,rotate=40, xoffset=370, yoffset=350)
    pause 0.4
    Transform("characters/xray/xray_top_10.png", zoom=.5 ,rotate=40, xoffset=370, yoffset=350)
    pause 0.4
    Transform("characters/xray/xray_top_11.png", zoom=.5 ,rotate=40, xoffset=370, yoffset=350)
    pause 0.4
    Transform("characters/xray/xray_top_12.png", zoom=.5 ,rotate=40, xoffset=370, yoffset=350)
    pause 0.4
    Transform("characters/xray/xray_top_13.png", zoom=.5 ,rotate=40, xoffset=370, yoffset=350)
    pause 0.4
    Transform("characters/xray/xray_top_14.png", zoom=.5 ,rotate=40, xoffset=370, yoffset=350)
    pause 0.4
    Transform("characters/xray/xray_top_15.png", zoom=.5 ,rotate=40, xoffset=370, yoffset=350)
    pause 0.4
    Transform("characters/xray/xray_top_16.png", zoom=.5 ,rotate=40, xoffset=370, yoffset=350)
    pause 0.4
    Transform("characters/xray/xray_top_17.png", zoom=.5 ,rotate=40, xoffset=370, yoffset=350)
    pause 0.4
    Transform("characters/xray/xray_top_18.png", zoom=.5 ,rotate=40, xoffset=370, yoffset=350)
    pause 2.0
    linear 2.5 alpha 0

image xray_jenny_shower:
    Transform("characters/xray/xray_side_01.png", xzoom=-.5, yzoom=.5 ,rotate=20, xoffset=410, yoffset=420)
    pause 0.4
    Transform("characters/xray/xray_side_02.png", xzoom=-.5, yzoom=.5 ,rotate=20, xoffset=410, yoffset=420)
    pause 0.4
    Transform("characters/xray/xray_side_03.png", xzoom=-.5, yzoom=.5 ,rotate=20, xoffset=410, yoffset=420)
    pause 0.4
    Transform("characters/xray/xray_side_04.png", xzoom=-.5, yzoom=.5 ,rotate=20, xoffset=410, yoffset=420)
    pause 0.4
    Transform("characters/xray/xray_side_05.png", xzoom=-.5, yzoom=.5 ,rotate=20, xoffset=410, yoffset=420)
    pause 0.4
    Transform("characters/xray/xray_side_06.png", xzoom=-.5, yzoom=.5 ,rotate=20, xoffset=410, yoffset=420)
    pause 0.4
    Transform("characters/xray/xray_side_07.png", xzoom=-.5, yzoom=.5 ,rotate=20, xoffset=410, yoffset=420)
    pause 0.4
    Transform("characters/xray/xray_side_08.png", xzoom=-.5, yzoom=.5 ,rotate=20, xoffset=410, yoffset=420)
    pause 0.4
    Transform("characters/xray/xray_side_09.png", xzoom=-.5, yzoom=.5 ,rotate=20, xoffset=410, yoffset=420)
    pause 0.4
    Transform("characters/xray/xray_side_10.png", xzoom=-.5, yzoom=.5 ,rotate=20, xoffset=410, yoffset=420)
    pause 0.4
    Transform("characters/xray/xray_side_11.png", xzoom=-.5, yzoom=.5 ,rotate=20, xoffset=410, yoffset=420)
    pause 0.4
    Transform("characters/xray/xray_side_12.png", xzoom=-.5, yzoom=.5 ,rotate=20, xoffset=410, yoffset=420)
    pause 0.4
    Transform("characters/xray/xray_side_13.png", xzoom=-.5, yzoom=.5 ,rotate=20, xoffset=410, yoffset=420)
    pause 0.4
    Transform("characters/xray/xray_side_14.png", xzoom=-.5, yzoom=.5 ,rotate=20, xoffset=410, yoffset=420)
    pause 0.4
    Transform("characters/xray/xray_side_15.png", xzoom=-.5, yzoom=.5 ,rotate=20, xoffset=410, yoffset=420)
    pause 0.4
    Transform("characters/xray/xray_side_16.png", xzoom=-.5, yzoom=.5 ,rotate=20, xoffset=410, yoffset=420)
    pause 0.4
    Transform("characters/xray/xray_side_17.png", xzoom=-.5, yzoom=.5 ,rotate=20, xoffset=410, yoffset=420)
    pause 0.4
    Transform("characters/xray/xray_side_18.png", xzoom=-.5, yzoom=.5 ,rotate=20, xoffset=410, yoffset=420)
    pause 2.0
    linear 2.5 alpha 0

image xray_jenny_couch:
    Transform("characters/xray/xray_side_01.png", xzoom=-.8, yzoom=.8, rotate=50, xoffset=300, yoffset=280)
    pause 0.4
    Transform("characters/xray/xray_side_02.png", xzoom=-.8, yzoom=.8, rotate=50, xoffset=300, yoffset=280)
    pause 0.4
    Transform("characters/xray/xray_side_03.png", xzoom=-.8, yzoom=.8, rotate=50, xoffset=300, yoffset=280)
    pause 0.4
    Transform("characters/xray/xray_side_04.png", xzoom=-.8, yzoom=.8, rotate=50, xoffset=300, yoffset=280)
    pause 0.4
    Transform("characters/xray/xray_side_05.png", xzoom=-.8, yzoom=.8, rotate=50, xoffset=300, yoffset=280)
    pause 0.4
    Transform("characters/xray/xray_side_06.png", xzoom=-.8, yzoom=.8, rotate=50, xoffset=300, yoffset=280)
    pause 0.4
    Transform("characters/xray/xray_side_07.png", xzoom=-.8, yzoom=.8, rotate=50, xoffset=300, yoffset=280)
    pause 0.4
    Transform("characters/xray/xray_side_08.png", xzoom=-.8, yzoom=.8, rotate=50, xoffset=300, yoffset=280)
    pause 0.4
    Transform("characters/xray/xray_side_09.png", xzoom=-.8, yzoom=.8, rotate=50, xoffset=300, yoffset=280)
    pause 0.4
    Transform("characters/xray/xray_side_10.png", xzoom=-.8, yzoom=.8, rotate=50, xoffset=300, yoffset=280)
    pause 0.4
    Transform("characters/xray/xray_side_11.png", xzoom=-.8, yzoom=.8, rotate=50, xoffset=300, yoffset=280)
    pause 0.4
    Transform("characters/xray/xray_side_12.png", xzoom=-.8, yzoom=.8, rotate=50, xoffset=300, yoffset=280)
    pause 0.4
    Transform("characters/xray/xray_side_13.png", xzoom=-.8, yzoom=.8, rotate=50, xoffset=300, yoffset=280)
    pause 0.4
    Transform("characters/xray/xray_side_14.png", xzoom=-.8, yzoom=.8, rotate=50, xoffset=300, yoffset=280)
    pause 0.4
    Transform("characters/xray/xray_side_15.png", xzoom=-.8, yzoom=.8, rotate=50, xoffset=300, yoffset=280)
    pause 0.4
    Transform("characters/xray/xray_side_16.png", xzoom=-.8, yzoom=.8, rotate=50, xoffset=300, yoffset=280)
    pause 0.4
    Transform("characters/xray/xray_side_17.png", xzoom=-.8, yzoom=.8, rotate=50, xoffset=300, yoffset=280)
    pause 0.4
    Transform("characters/xray/xray_side_18.png", xzoom=-.8, yzoom=.8, rotate=50, xoffset=300, yoffset=280)
    pause 2.0
    linear 2.5 alpha 0


image overlay_o_water:
    Transform("characters/jenny/layeredimage/jenny_overlay_o_water_01.png")
    pause 0.075
    Transform("characters/jenny/layeredimage/jenny_overlay_o_water_02.png")
    pause 0.075
    Transform("characters/jenny/layeredimage/jenny_overlay_o_water_03.png")
    pause 0.075
    Transform("characters/jenny/layeredimage/jenny_overlay_o_water_04.png")
    pause 0.075
    Transform("characters/jenny/layeredimage/jenny_overlay_o_water_05.png")
    pause 0.075
    Transform("characters/jenny/layeredimage/jenny_overlay_o_water_06.png")
    pause 0.075
    Transform("characters/jenny/layeredimage/jenny_overlay_o_water_07.png")
    pause 0.075
    Transform("characters/jenny/layeredimage/jenny_overlay_o_water_08.png")
    pause 0.075
    Transform("characters/jenny/layeredimage/jenny_overlay_o_water_09.png")
    pause 0.075
    Transform("characters/jenny/layeredimage/jenny_overlay_o_water_10.png")
    pause 0.075
    Transform("characters/jenny/layeredimage/jenny_overlay_o_water_11.png")
    pause 0.075
    Transform("characters/jenny/layeredimage/jenny_overlay_o_water_12.png")
    pause 0.075
    Transform("characters/jenny/layeredimage/jenny_overlay_o_water_13.png")
    pause 0.075
    Transform("characters/jenny/layeredimage/jenny_overlay_o_water_14.png")
    pause 0.075
    Transform("characters/jenny/layeredimage/jenny_overlay_o_water_15.png")
    pause 0.075
    Transform("characters/jenny/layeredimage/jenny_overlay_o_water_16.png")
    pause 0.075
    Transform("characters/jenny/layeredimage/jenny_overlay_o_water_17.png")
    pause 0.075
    Transform("characters/jenny/layeredimage/jenny_overlay_o_water_18.png")
    pause 0.075
    Transform("characters/jenny/layeredimage/jenny_overlay_o_water_19.png")
    pause 0.075
    Transform("characters/jenny/layeredimage/jenny_overlay_o_water_20.png")
    pause 0.075
    Transform("characters/jenny/layeredimage/jenny_overlay_o_water_21.png")
    pause 0.075
    Transform("characters/jenny/layeredimage/jenny_overlay_o_water_22.png")
    pause 0.075
    Transform("characters/jenny/layeredimage/jenny_overlay_o_water_23.png")
    pause 0.075
    Transform("characters/jenny/layeredimage/jenny_overlay_o_water_24.png")
    pause 0.075
    repeat



image jenny_body_b_dressed_tied = 'characters/jenny/layeredimage/jenny_body_b_dressed[M_jenny.pregnancy]_tied.png'
image jenny_body_b_dressed_tied_recoil = 'characters/jenny/layeredimage/jenny_body_b_dressed[M_jenny.pregnancy]_tied_recoil.png'
image jenny_body_b_dressed_tied_hair_pull = 'characters/jenny/layeredimage/jenny_body_b_dressed[M_jenny.pregnancy]_tied_hair_pull.png'
image jenny_body_b_dressed_untying = 'characters/jenny/layeredimage/jenny_body_b_dressed[M_jenny.pregnancy]_untying.png'
image jenny_body_b_dressed_run = 'characters/jenny/layeredimage/jenny_body_b_dressed[M_jenny.pregnancy]_run.png'
image jenny_body_b_dressed_hug_mc1 = 'characters/jenny/layeredimage/jenny_body_b_dressed[M_jenny.pregnancy.to_belly_string]_hug_mc1.png'
image jenny_body_b_dressed_hug_mc2 = 'characters/jenny/layeredimage/jenny_body_b_dressed[M_jenny.pregnancy.to_belly_string]_hug_mc2.png'
image jenny_body_b_dressed_hug_mc3 = 'characters/jenny/layeredimage/jenny_body_b_dressed[M_jenny.pregnancy.to_belly_string]_hug_mc3.png'
image jenny_body_b_dressed_hold_anon_arm = 'characters/jenny/layeredimage/jenny_body_b_dressed[M_jenny.pregnancy]_hold_anon_arm.png'

image jenny_body_b_dressed_tied_boob_grab:
    'characters/jenny/layeredimage/jenny_body_b_dressed[M_jenny.pregnancy]_tied_boob_grab1.png'
    pause .4
    'characters/jenny/layeredimage/jenny_body_b_dressed[M_jenny.pregnancy]_tied_boob_grab2.png'
    pause .4
    repeat

image jenny_arms_dressed_a_magic = ConditionSwitch(
    'M_jenny.pregnancy.to_belly_string', 'characters/jenny/layeredimage/jenny_arms_dressed_a_pregnant_touch.png',
    True, 'jenny_arms_dressed_a_sides')

image jenny_arms_dressed_a_slap_butt = 'characters/jenny/layeredimage/jenny_arms_dressed[M_jenny.pregnancy.to_belly_string]_a_slap_butt.png'
image jenny_arms_dressed_a_sides = 'characters/jenny/layeredimage/jenny_arms_dressed[M_jenny.pregnancy]_a_sides.png'
image jenny_arms_dressed_a_up_surprised = 'characters/jenny/layeredimage/jenny_arms_dressed[M_jenny.pregnancy.to_belly_string]_a_up_surprised.png'
image jenny_arms_dressed_a_upset = 'characters/jenny/layeredimage/jenny_arms_dressed[M_jenny.pregnancy.to_belly_string]_a_upset.png'
image jenny_arms_dressed_a_wrists_hurt = 'characters/jenny/layeredimage/jenny_arms_dressed[M_jenny.pregnancy.to_belly_string]_a_wrists_hurt.png'
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
