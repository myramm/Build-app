

define config.speaking_attribute = 'm_talk'

init python hide:
    def autodissolve(tag, mode, before, after):
        rv = config.say_attribute_transition
        if not renpy.get_transition():
            delta = before ^ after
            if any(a.startswith(('a_', 'b_')) for a in delta):
                rv = dissolve
            if tag == 'nadya' and 'f_normal_smoke_blow' in delta:
                return dissolve, 'master'
        return rv, config.say_attribute_transition_layer

    config.say_attribute_transition_callback = autodissolve

init:
    $ anon_clothing_options = ['b_dressed','b_hammock','b_dressed_dance1','b_jersey','b_jacket','b_shirt','b_naked','b_dressed_disheveled','b_empty','b_underwear','b_shorts','b_hug_eve_disheveled','b_hug_eve','b_pulling4']
    $ anon_unique_options = ['b_couch_sit','b_couch_sit_naked','b_front','b_front_kiss_talk','b_sleep_side','b_visit','b_visit_up1','b_visit_up2','b_side_naked_forward','b_side_naked_backward','b_side_naked']

init python:


    renpy.image('anon_arms_a_empty', 'ground.png')
    renpy.image('anon_overlay_face_of_empty', 'ground.png')
    renpy.image('anon_arms_front_a_empty', 'ground.png')
    renpy.image('anon_body_b_empty', 'ground.png')
    renpy.image('anon_body_b_empty_sleep_cuddle', 'ground.png')
    renpy.image('anon_body_b_empty_eve_onbed_cuddle', 'ground.png')
    renpy.image('anon_body_b_empty_eve_onbed_hug', 'ground.png')
    renpy.image('anon_face_couch_sit_f_empty', 'ground.png')
    renpy.image('anon_face_couch_sit_talk_f_empty','ground.png')
    renpy.image('anon_face_couch_watch_f_empty', 'ground.png')
    renpy.image('anon_face_f_empty', 'ground.png')
    renpy.image('anon_face_talk_f_empty', 'ground.png')



    renpy.image('anon_face_talk_f_laugh', 'anon_face_f_laugh')
    renpy.image('anon_face_talk_f_shock', 'anon_face_f_shock')
    renpy.image('anon_face_talk_f_grin', 'anon_face_f_grin')
    renpy.image('anon_face_talk_f_surprised_teeth_down', 'anon_face_f_surprised_teeth_down')
    renpy.image('anon_face_talk_f_shock_left', 'anon_face_f_shock_left')
    renpy.image('anon_face_talk_f_shock_low', 'anon_face_f_shock_low')
    renpy.image('anon_face_talk_f_surprised_forward','anon_face_f_surprised_forward')
    renpy.image('anon_face_talk_f_surprised_teeth', 'anon_face_f_surprised_teeth')
    renpy.image('anon_face_talk_f_front_scared_right', 'anon_face_f_front_scared_right')
    renpy.image('anon_face_talk_f_surprised_left', 'anon_face_f_surprised_left')
    renpy.image('anon_face_talk_f_surprised_teeth_left', 'anon_face_f_surprised_teeth_left')
    renpy.image('anon_face_talk_f_couch_sit_watching_straight', 'anon_face_f_couch_sit_watching_straight')
    renpy.image('anon_face_talk_f_couch_sit_watching_straight_surprised', 'anon_face_f_couch_sit_watching_straight_surprised')
    renpy.image('anon_face_talk_f_couch_sit_watching_jerking', 'anon_face_f_couch_sit_watching_jerking')
    renpy.image('anon_face_talk_f_couch_sit_down_surprised', 'anon_face_f_couch_sit_down_surprised')
    renpy.image('anon_face_talk_f_visit_sleep', 'anon_face_f_visit_sleep')
    renpy.image('anon_face_talk_f_cough', 'anon_face_f_cough')
    renpy.image('anon_face_talk_f_front_forward_laugh', 'anon_face_f_front_forward_laugh')
    renpy.image('anon_face_talk_f_disgusted_wince', 'anon_face_f_disgusted_wince')
    renpy.image('anon_face_talk_f_hurt', 'anon_face_f_hurt')
    renpy.image('anon_face_talk_f_shock_down', 'anon_face_f_shock_down')
    renpy.image('anon_face_talk_f_side_react', 'anon_face_f_side_react')
    renpy.image('anon_face_talk_f_depressed', 'anon_face_talk_f_sad_down')
    renpy.image('anon_face_talk_f_smoke', 'anon_face_f_smoke')
    renpy.image('anon_face_talk_f_choked_shock', 'anon_face_f_choked_shock')
    renpy.image('anon_face_talk_f_choked_surprised_teeth', 'anon_face_f_choked_surprised_teeth')
    renpy.image('anon_face_talk_f_choked_hurt', 'anon_face_f_choked_hurt')
    renpy.image('anon_face_tina_sex_talk_f_shock', 'anon_face_tina_sex_f_shock')
    renpy.image('anon_face_tina_sex_talk_f_react', 'anon_face_tina_sex_f_react')



    renpy.image('anon_face_f_depressed', 'anon_face_talk_f_sad_down')
    renpy.image('anon_face_f_brag_closed', 'anon_face_talk_f_brag_closed')
    renpy.image('anon_face_f_disgusted_down', 'anon_face_talk_f_disgusted_down')

    renpy.image('anon_cutscene31_face_f_shocked', 'anon_cutscene31_face_talk_f_shocked')




    renpy.image('anon_body_b_dinner_sitting_look_left', 'anon_body_b_dinner_sitting') 


    renpy.image('anon_arms_dressed_a_backpack', 'anon_arms_dressed_a_backpack')
    renpy.image('anon_arms_front_a_jenny_crotch_rub', 'anon_arms_front_a_jenny_crotch_rub')
    renpy.image('anon_arms_couch_a_boner_cum', 'anon_arms_couch_a_boner_cum')
    renpy.image('anon_arms_couch_a_boner_jerk', 'anon_arms_couch_a_boner_jerk')
    renpy.image('anon_arms_dinner_sitting_a_bowl', 'anon_arms_dinner_sitting_a_bowl')
    renpy.image('anon_arms_dressed_a_give_panties', 'anon_arms_dressed_a_give_panties')


    renpy.image('anon_overlay_o_couch_boner_cum', 'anon_overlay_o_couch_boner_cum')
    renpy.image('anon_overlay_face_of_bed_jenny_laying_undies_arms_mask_X', 'anon_overlay_face_of_bed_jenny_laying_undies_arms_mask_X')
    renpy.image('anon_overlay_face_of_bed_jenny_laying_mask_X', 'anon_overlay_face_of_bed_jenny_laying_mask_X')

layeredimage anon:

    yanchor config.screen_height
    ypos 1.
    xanchor config.screen_width
    xpos 1.


    group body auto:
        attribute b_dressed default
        attribute b_empty null
        attribute b_sit_kiss_eve "anon_body_b_sit_kiss_eve"

        attribute b_dressed_dance_shy "anon_body_b_dressed_dance_shy"

        attribute b_dressed_dance_shy_talk "anon_body_b_dressed_dance_shy_talk"

        attribute b_dressed_dance_flirt_low "anon_body_b_dressed_dance_flirt_low"

        attribute b_dressed_dance_unimpressed "anon_body_b_dressed_dance_unimpressed"

        attribute b_naked_spin_frown_down "anon_body_b_naked_spin_frown_down"

        attribute b_naked_spin_frown_down_talk "anon_body_b_naked_spin_frown_down_talk"

        attribute b_naked_spin_worried_low_talk "anon_body_b_naked_spin_worried_low_talk"

        attribute b_naked_spin_worried_low "anon_body_b_naked_spin_worried_low"

        attribute b_hammock_thrust_worried_low "anon_body_b_hammock_thrust_worried_low"

        attribute b_hammock_thrust_worried "anon_body_b_hammock_thrust_worried"

        attribute b_hammock_thrust_worried_talk "anon_body_b_hammock_thrust_worried_talk"

        attribute b_mcpuffin 'location_bank_vault_briefcase'
        attribute b_maria_sex_side_back null
        attribute b_dressed_zap


    group mouth prefix 'm':
        attribute talk null

    group face:
        attribute f_normal default null








    group face if_not 'm_talk' if_any anon_clothing_options auto


    group face if_not 'm_talk' if_any ['b_dressed_floor', 'b_dressed_floor_barefeet', 'b_dressed_floor_hug_daisy'] auto:
        offset (151,-12)


    group face if_not 'm_talk' if_any ['b_dressed_tall'] auto:
        offset (0, -124)


    group face if_not 'm_talk' if_any ['b_front_behind_couch'] auto:
        zoom .95
        offset (46,-84)


    group face if_not 'm_talk' if_any ['b_liu_dressed','b_liu_shorts','b_liu_naked','b_liu_shorts_remove_shorts','b_liu_shorts_throw_shirt'] auto:
        zoom .95
        rotate -10
        offset (89,-112)


    group face if_not 'm_talk' if_any ['b_laying_ground'] auto:
        zoom .95
        rotate -10
        offset (-159,-255)


    group face if_not 'm_talk' if_any ['b_hammock_dance_pose'] auto:
        offset (122, 95)


    group face if_not 'm_talk' if_any ['b_jacuzzi_naked'] auto:
        offset (-57, 69)


    group face if_not 'm_talk' if_any ['b_onbed_naked'] auto:
        xzoom -1
        offset (84, -17)


    group face if_not 'm_talk' if_any ['b_swim'] auto:
        offset (-35, 151)


    group face if_not 'm_talk' if_any ['b_tina_lingerie1','b_tina_lingerie2'] auto:
        offset (208, 22)


    group face if_not 'm_talk' if_any ['b_onbed_back'] auto:
        offset (-42, 0)


    group face if_not 'm_talk' if_any ['b_punch','b_flour'] auto:
        offset (73, 143)


    group face if_not 'm_talk' if_all 'b_onbed_sit' auto:
        offset (22, -29)


    group face if_not 'm_talk' if_all 'b_pulling1' auto:
        offset (266, 0)


    group face if_not 'm_talk' if_any ['b_pulling2','b_pulling5'] auto:
        offset (252, 0)


    group face if_not 'm_talk' if_all 'b_pulling3' auto:
        offset (275, 0)


    group face if_not 'm_talk' if_all 'b_empty_eve_onbed_hug' auto:
        offset (-14, 1)


    group face if_not 'm_talk' if_all 'b_empty_eve_onbed_cuddle' auto:
        offset (-50, 72)


    group face if_not 'm_talk' if_all 'b_desk' auto:
        offset (-67, 88)


    group face if_not 'm_talk' if_all 'b_telescope' auto:
        offset (-51, 145)
        zoom .82


    group face if_not 'm_talk' if_all 'b_telescope_laying_back' auto:
        offset (-99, 180)
        zoom .82


    group face if_not 'm_talk' if_all 'b_bed_jenny_sit' auto:
        offset (85, -28)
        xzoom -1


    group face if_not 'm_talk' if_all 'b_bed_jenny_sit_back' auto:
        offset (85, 60)
        xzoom -1


    group face if_not 'm_talk' if_all 'b_bed_jenny_laptop' auto:
        offset (-375, 1)
        xzoom -1


    group face if_not 'm_talk' if_all 'b_dinner_standing_cumming' auto:
        offset (92, 88)
        xzoom -.76
        yzoom .76


    group face if_not 'm_talk' if_all 'b_dinner_sitting' auto:
        offset (384, 133)
        zoom .76
        attribute f_eat anim.TransitionAnimation(
            'anon_face_f_looking_down_eating', 1., Dissolve(.4),
            'anon_face_f_looking_down_food', 2., Dissolve(.4),
            'anon_face_f_looking_down', 3., Dissolve(.4),
            anim_timebase=False)


    group face if_not 'm_talk' if_all 'b_dinner_sitting_look_left' auto:
        offset (384, 133)
        zoom .76
        attribute f_normal "anon_face_f_normal_left"

        attribute f_worried "anon_face_f_worried_left"

        attribute f_surprised "anon_face_f_surprised_left"

        attribute f_skeptical "anon_face_f_worried_left"

        attribute f_grin "anon_face_f_grin_left"

        attribute f_flirt "anon_face_f_flirt_left"

        attribute f_shock "anon_face_f_shock_left"

        attribute f_surprised_teeth "anon_face_f_surprised_teeth_left"



    group face if_not 'm_talk' if_all 'b_pool' auto:
        offset (70, 233)
        zoom .76


    group face if_not 'm_talk' if_any ['b_sit', 'b_sit_naked'] auto:
        offset (161, -13)


    group face if_not 'm_talk' if_all 'b_spook' auto:
        offset (72, 144)


    group face if_not 'm_talk' if_any ['b_dressed_car'] auto:
        offset (76, -88)
        attribute f_empty null


    group face if_not 'm_talk' if_any ['b_sit_back','b_sit_back_shirt', 'b_sit_back_remove_shorts2'] auto:
        offset (50, 30)


    group face if_not 'm_talk' if_any ['b_sit_naked_up'] auto:
        offset (166, -193)


    group face if_not 'm_talk' if_any ['b_sit_naked_check'] auto:
        offset (195, -138)


    group face if_not 'm_talk' if_any ['b_dressed_dance2'] auto:
        offset (-2, 0)


    group face if_not 'm_talk' if_any ['b_hammock_thrust1'] auto:
        offset (-11, 12)


    group face if_not 'm_talk' if_any ['b_hammock_thrust2'] auto:
        offset (9, 25)


    group face if_not 'm_talk' if_any ['b_dressed_car_getup'] auto:
        rotate 10
        offset (170, -222)


    group face if_not 'm_talk' if_any ['b_sleep_side_eve'] auto:
        offset (43, 0)


    group face if_not 'm_talk' if_any ['b_sleep_side_eve_cuddle'] auto:
        anchor (0, 0)
        offset (58, 85)
        rotate -7.4
        rotate_pad False
        transform_anchor True


    group face if_not 'm_talk' if_any 'b_visit_morning_sit' auto:
        offset (61.3, 92.3)
        xzoom -.91
        yzoom .91

    group face if_not 'm_talk' if_any 'b_maria_sex_side_back' auto:
        align (.5, .5)
        offset (287.75, 47.5)
        rotate 43
        rotate_pad False
        subpixel True
        transform_anchor True
        zoom 1.4

    group face if_not 'm_talk' if_any 'b_dressed_sitting_chair' auto:
        offset (48, 151)

    group face if_not 'm_talk' if_any 'b_bend' auto:
        offset (73, 142)






    group face if_not 'm_talk' if_any ['b_dressed_car_front'] auto variant 'dressed_car_front':
        attribute f_empty null


    group face if_not 'm_talk' if_any anon_unique_options auto:
        attribute f_empty null


    group face if_all 'b_couch_sit_watching' auto:
        attribute f_empty null


    group face if_not 'm_talk' if_all 'b_tina_sex' auto variant 'tina_sex':
        attribute f_empty null


    group face if_not 'm_talk' if_any ['b_sleep_cuddle', 'b_empty_sleep_cuddle'] auto:
        offset (112, 0)


    group face if_not 'm_talk' if_any 'b_mcpuffin' auto variant 'briefcase':
        attribute f_normal default null


    group face if_not 'm_talk' if_any 'b_visit_morning_relax' auto variant 'visit_morning_relax'







    group face if_all 'm_talk' if_any anon_clothing_options auto variant 'talk'


    group face if_all 'm_talk' if_any ['b_dressed_floor', 'b_dressed_floor_barefeet', 'b_dressed_floor_hug_daisy'] auto variant 'talk':
        offset (151,-12)


    group face if_all 'm_talk' if_any ['b_dressed_tall'] auto variant 'talk':
        offset (0, -124)


    group face if_all 'm_talk' if_any ['b_front_behind_couch'] auto variant 'talk':
        zoom .95
        offset (46,-84)


    group face if_all 'm_talk' if_any  ['b_liu_dressed','b_liu_shorts','b_liu_naked','b_liu_shorts_remove_shorts','b_liu_shorts_throw_shirt'] auto variant 'talk':
        zoom .95
        rotate -10
        offset (89,-112)


    group face if_all 'm_talk' if_any ['b_laying_ground'] auto variant 'talk':
        zoom .95
        rotate -10
        offset (-159,-255)


    group face if_all 'm_talk' if_any ['b_hammock_dance_pose'] auto variant 'talk':
        offset (122, 95)


    group face if_all 'm_talk' if_any ['b_jacuzzi_naked'] auto variant 'talk':
        offset (-57, 69)


    group face if_all 'm_talk' if_any ['b_onbed_naked'] auto variant 'talk':
        xzoom -1
        offset (84, -17)


    group face if_all 'm_talk' if_any ['b_swim'] auto variant 'talk':
        offset (-35, 151)


    group face if_all 'm_talk' if_any ['b_tina_lingerie1','b_tina_lingerie2'] auto variant 'talk':
        offset (208, 22)


    group face if_all 'm_talk' if_any ['b_onbed_back'] auto variant 'talk':
        offset (-42, 0)


    group face if_all 'm_talk' if_any ['b_punch','b_flour'] auto variant 'talk':
        offset (73, 143)


    group face if_all ['m_talk','b_onbed_sit'] auto variant 'talk':
        offset (22, -29)


    group face if_all ['m_talk','b_pulling1'] auto variant 'talk':
        offset (266, 0)


    group face if_all 'm_talk' if_any ['b_pulling2','b_pulling5'] auto variant 'talk':
        offset (252, 0)


    group face if_all ['m_talk','b_pulling3'] auto variant 'talk':
        offset (275, 0)


    group face if_all ['m_talk','b_empty_eve_onbed_hug'] auto variant 'talk':
        offset (-14, 1)


    group face if_all ['m_talk','b_empty_eve_onbed_cuddle'] auto variant 'talk':
        offset (-50, 72)


    group face if_all ['m_talk', 'b_desk'] auto variant 'talk':
        offset (-67, 88)


    group face if_all ['m_talk', 'b_telescope'] auto variant 'talk':
        offset (-51, 145)
        zoom .82


    group face if_all ['m_talk', 'b_telescope_laying_back'] auto variant 'talk':
        offset (-99, 180)
        zoom .82


    group face if_all ['m_talk', 'b_bed_jenny_sit'] auto variant 'talk':
        offset (85, -28)
        xzoom -1


    group face if_all ['m_talk', 'b_bed_jenny_sit_back'] auto variant 'talk':
        offset (85, 60)
        xzoom -1


    group face if_all 'm_talk' if_any 'b_bed_jenny_laptop' auto variant 'talk':
        offset (-375, 1)
        xzoom -1


    group face if_all ['m_talk', 'b_dinner_standing_cumming'] auto variant 'talk':
        offset (92, 88)
        xzoom -.76
        yzoom .76


    group face if_all ['m_talk', 'b_dinner_sitting'] auto variant 'talk':
        offset (384, 133)
        zoom .76


    group face if_all ['m_talk', 'b_dinner_sitting_look_left'] auto variant 'talk':
        offset (384, 133)
        zoom .76
        attribute f_normal "anon_face_talk_f_normal_left"

        attribute f_worried "anon_face_talk_f_worried_left"

        attribute f_surprised "anon_face_f_surprised_left"

        attribute f_skeptical "anon_face_talk_f_worried_left"

        attribute f_grin "anon_face_f_grin_left"

        attribute f_flirt "anon_face_talk_f_flirt_left"

        attribute f_shock "anon_face_f_shock_left"

        attribute f_surprised_teeth "anon_face_f_surprised_teeth_left"



    group face if_all ['m_talk', 'b_pool'] auto variant 'talk':
        offset (70, 233)
        zoom .76


    group face if_all 'm_talk' if_any ['b_sit', 'b_sit_naked'] auto variant 'talk':
        offset (161, -13)


    group face if_all ['m_talk', 'b_spook'] auto variant 'talk':
        offset (72, 144)


    group face if_all 'm_talk' if_any ['b_dressed_car'] auto variant 'talk':
        offset (76, -88)
        attribute f_empty null


    group face if_all 'm_talk' if_any ['b_sit_back','b_sit_back_shirt', 'b_sit_back_remove_shorts2'] auto variant 'talk':
        offset (50, 30)


    group face if_all 'm_talk' if_any ['b_sit_naked_up'] auto variant 'talk':
        offset (166, -193)


    group face if_all 'm_talk' if_any ['b_sit_naked_check'] auto variant 'talk':
        offset (195, -138)


    group face if_all 'm_talk' if_any ['b_dressed_dance2'] auto variant 'talk':
        offset (-2, 0)


    group face if_all 'm_talk' if_any ['b_hammock_thrust1'] auto variant 'talk':
        offset (-11, 12)


    group face if_all 'm_talk' if_any ['b_hammock_thrust2'] auto variant 'talk':
        offset (9, 25)


    group face if_all 'm_talk' if_any ['b_dressed_car_getup'] auto variant 'talk':
        rotate 10
        offset (170, -222)


    group face if_all 'm_talk' if_any ['b_sleep_side_eve'] auto variant 'talk':
        offset (43, 0)


    group face if_all 'm_talk' if_any ['b_sleep_side_eve_cuddle'] auto variant 'talk':
        anchor (0, 0)
        offset (58, 85)
        rotate -7.4
        rotate_pad False
        transform_anchor True


    group face if_all 'm_talk' if_any 'b_visit_morning_sit' auto variant 'talk':
        offset (61.3, 92.3)
        xzoom -.91
        yzoom .91

    group face if_all 'm_talk' if_any 'b_maria_sex_side_back' auto variant 'talk':
        align (.5, .5)
        offset (287.75, 47.5)
        rotate 43
        rotate_pad False
        subpixel True
        transform_anchor True
        zoom 1.4

    group face if_all 'm_talk' if_any 'b_dressed_sitting_chair' auto variant 'talk':
        offset (48, 151)

    group face if_all 'm_talk' if_any 'b_bend' auto variant 'talk':
        offset (73, 142)






    group face if_all 'm_talk' if_any ['b_dressed_car_front'] auto variant 'dressed_car_front_talk':
        attribute f_empty null


    group face if_all 'm_talk' if_any anon_unique_options auto variant 'talk':
        attribute f_empty null


        attribute f_right 'anon_face_talk_f_couch_sit_right'
        attribute f_down 'anon_face_talk_f_couch_sit_down'
        attribute f_down_surprised 'anon_face_f_couch_sit_down_surprised'
        attribute f_down_happy 'anon_face_f_couch_sit_down_happy'


    group face if_all ['m_talk','b_tina_sex'] auto variant 'tina_sex_talk':
        attribute f_empty null


    group face if_all 'm_talk' if_any['b_sleep_cuddle', 'b_empty_sleep_cuddle'] auto variant 'talk':
        offset (112, 0)


    group face if_all 'm_talk' if_any 'b_mcpuffin' auto variant 'briefcase_talk':
        attribute f_normal default 'anon_face_briefcase_talk_f_normal_down'


    group face if_all 'm_talk' if_any 'b_visit_morning_relax' auto variant 'visit_morning_relax_talk'


    group overlay if_any ['b_dressed_floor'] auto variant 'dressed_floor':
        attribute o_empty default null




    group arms if_any ['b_dressed','b_dressed_disheveled'] auto variant 'dressed':
        attribute a_idle default 'anon_arms_dressed_a_pocket'
        attribute a_baby "anon_arms_dressed_a_baby_[player.last_baby_gender]"

        attribute a_melonia_baby "anon_arms_dressed_a_baby_[M_melonia.pregnancy.baby_gender]"

        attribute a_cover_boner null
        attribute a_milk_cups null


    group arms if_any ['b_dressed_floor', 'b_dressed_floor_barefeet'] auto variant 'dressed_floor':
        attribute a_idle default 'anon_arms_dressed_floor_a_down'
        attribute a_pat
        attribute a_poke


    group arms if_any ['b_dressed_tall'] auto variant 'dressed_tall':
        attribute a_idle default 'anon_arms_dressed_tall_a_pocket'
        attribute a_sides 'anon_arms_dressed_tall_a_side'

    group arms if_any ['b_dressed_tall'] variant 'dressed':
        offset (0, -124)
        attribute a_behind_head
        attribute a_cheering
        attribute a_cold
        attribute a_fists
        attribute a_frustrated
        attribute a_surprised_shoulders
        attribute a_surprised_up
        attribute a_surprised_up_both
        attribute a_thinking
        attribute a_up


    group arms if_any ['b_laying_ground'] auto variant 'laying_ground':
        attribute a_idle default 'anon_arms_laying_ground_a_side'


    group arms if_any ['b_jacuzzi_naked'] auto variant 'jacuzzi_naked':
        attribute a_idle default 'anon_arms_jacuzzi_naked_a_sides'
        attribute a_massage_foot 'anon_arms_jacuzzi_naked_a_massage_foot'
        attribute a_massage_foot_calf 'anon_arms_jacuzzi_naked_a_massage_foot_calf'
        attribute a_whisper_back 'anon_arms_jacuzzi_naked_a_whisper_back'


    group arms if_any ['b_dressed_back_cleaning'] auto variant 'dressed_back_cleaning':
        attribute a_idle default 'anon_arms_dressed_back_cleaning_a_net'


    group arms if_any ['b_hammock_back_cleaning'] auto variant 'hammock_back_cleaning':
        attribute a_idle default 'anon_arms_hammock_back_cleaning_a_net'


    group arms if_any ['b_jersey'] auto variant 'jersey':
        attribute a_idle default 'anon_arms_jersey_a_pocket'


    group arms if_any ['b_dressed_car','b_dressed_car_front'] auto variant 'dressed_car':
        attribute a_idle default 'anon_arms_dressed_car_a_down'



    group arms if_any ['b_onbed_back'] auto variant 'onbed_back':
        attribute a_idle default 'anon_arms_onbed_back_a_side_bonerless'


    group arms if_any ['b_jacket'] auto variant 'jacket':
        attribute a_idle default 'anon_arms_jacket_a_pocket'


    group arms if_any ['b_shirt'] auto variant 'dressed':
        attribute a_idle default 'anon_arms_dressed_a_up'
        attribute a_flick1 'anon_arms_dressed_a_flick1'
        attribute a_flick2 'anon_arms_dressed_a_flick2'
        attribute a_crossed 'anon_arms_dressed_a_crossed'

    group arms if_any ['b_shirt'] auto variant 'shirt'


    group arms if_any ['b_onbed_sit'] auto variant 'onbed_sit':
        attribute a_idle default 'anon_arms_onbed_sit_a_down'


    group arms if_any ['b_underwear', 'b_naked', 'b_shorts','b_hammock'] auto variant 'naked':
        attribute a_idle default 'anon_arms_naked_a_sides'


    group arms if_all 'b_swim' auto variant 'swim':
        attribute a_idle default 'anon_arms_swim_a_float'


    group arms if_all 'b_desk' auto variant 'desk':
        attribute a_idle default 'anon_arms_desk_a_writing'


    group arms if_any ['b_dinner_sitting', 'b_dinner_sitting_look_left'] auto variant 'dinner_sitting':
        attribute a_idle default 'anon_arms_dinner_sitting_a_resting'
        attribute a_eat anim.TransitionAnimation(
            'anon_arms_dinner_sitting_a_eating', 1., Dissolve(.4),
            'anon_arms_dinner_sitting_a_resting', 3.8, Dissolve(.4),
            'anon_arms_dinner_sitting_a_bowl1', .6, Dissolve(.4),
            'anon_arms_dinner_sitting_a_bowl2', .6, Dissolve(.4),
            anim_timebase=False)


    group arms if_all 'b_sleep_side' auto variant 'sleep_side':
        attribute a_idle default 'anon_arms_sleep_side_a_normal'


    group arms if_any ['b_side_naked', 'b_side_naked_backward', 'b_side_naked_forward'] auto variant 'side_naked':
        attribute a_idle default 'anon_arms_side_naked_a_down'


    group arms if_all 'b_telescope_laying_back' auto variant 'telescope':
        attribute a_idle default 'anon_arms_telescope_a_side'


    group arms if_all 'b_sit' auto variant 'sit':
        attribute a_idle default 'anon_arms_sit_a_lap'


    group arms if_all 'b_sit_naked' auto variant 'sit_naked':
        attribute a_idle default 'anon_arms_sit_naked_a_lap'


    group arms if_all ['b_sit_naked_up'] auto variant 'sit_naked_up':
        attribute a_idle default 'anon_arms_sit_naked_up_a_sides'


    group arms if_any ['b_couch_sit', 'b_couch_sit_look', 'b_couch_sit_naked', 'b_couch_sit_watching'] auto variant 'couch':
        attribute a_idle default 'anon_arms_couch_a_sides'


    group arms if_all 'b_front' auto variant 'front':
        attribute a_idle default 'anon_arms_front_a_down'


    group arms if_any ['b_sit_back','b_sit_back_shirt'] auto variant 'sit_back':
        attribute a_idle default 'anon_arms_sit_back_a_down'


    group arms if_any 'b_sleep_side_eve' auto variant 'sleep_side_eve':
        attribute a_idle default 'anon_arms_sleep_side_eve_a_down'


    group arms if_any 'b_sleep_side_eve_cuddle' auto variant 'sleep_side_eve_cuddle':
        attribute a_idle default 'anon_arms_sleep_side_eve_cuddle_a_hold'


    group arms if_any 'b_visit_morning_sit' auto variant 'visit_morning_sit':
        attribute a_idle default 'anon_arms_visit_morning_sit_a_sides'

    group arms if_any 'b_dressed_sitting_chair' auto variant 'dressed_sitting_chair':
        attribute a_idle default 'anon_arms_dressed_sitting_chair_a_rest'

    group arms if_any 'b_bend' auto variant 'bend':
        attribute a_idle default 'anon_arms_bend_a_undress_khadne1'


    group overlay_dick if_not ['b_shirt', 'b_onbed_naked', 'b_sit_back_shirt', 'b_sit_back_remove_shorts2', 'b_sit_naked_remove_shirt', 'b_sit_naked', 'b_sit_naked_up', 'b_sit_naked_check'] auto:
        attribute od_empty default null
        attribute od_naked_dick_grow 'anon_overlay_dick_od_naked_dick_grow'

    group overlay_dick if_any ['b_shirt'] auto variant 'shirt':
        attribute od_dick1 default "anon_overlay_dick_shirt_od_dick1"

        attribute od_dick4_wet Fixed("anon_overlay_dick_shirt_od_dick4",
                                     "anon_overlay_dick_shirt_od_dick4_wet")
        attribute od_dick_spring "anon_overlay_dick_shirt_od_dick_spring"

        attribute od_empty null

    group overlay_dick if_any ['b_onbed_naked'] auto variant 'onbed_naked':
        attribute od_dick1 default "anon_overlay_dick_onbed_naked_od_dick1"

        attribute od_empty null

    group overlay_dick if_any ['b_sit_back_shirt', 'b_sit_back_remove_shorts2', 'b_sit_naked_remove_shirt', 'b_sit_naked'] auto variant 'sit_back_shirt':
        attribute od_dick1 default "anon_overlay_dick_sit_back_shirt_od_dick1"

        attribute od_dick_spring "anon_overlay_dick_sit_back_shirt_od_dick_spring"


    group overlay_dick if_any ['b_sit_naked_up'] auto:
        offset (117, -239)
        attribute od_dick1 default

    group overlay_dick if_any ['b_sit_naked_check'] auto:
        align (.5, .5)
        attribute od_dick1 default
        offset (107, -211)
        rotate 2

    group overlay_dick if_any 'b_dressed_sitting_chair' auto variant 'dressed_sitting_chair'


    group overlay_hands auto:
        attribute oh_empty default null


    group overlay_face if_not ['b_bed_jenny_sit', 'b_bed_jenny_sit_back', 'b_bed_jenny_laptop', 'b_dinner_sitting', 'b_dinner_sitting_look_left', 'b_sit', 'b_sit_naked', 'b_sit_back', 'b_sit_back_shirt', 'b_sit_back_remove_shorts2', 'b_sit_naked_up', 'b_sit_naked_check', 'b_dressed_car', 'b_dressed_tall', 'b_dressed_floor', 'b_dressed_floor_barefeet', 'b_liu_dressed', 'b_liu_shorts', 'b_liu_naked', 'b_liu_shorts_remove_shorts', 'b_liu_shorts_throw_shirt', 'b_onbed_back', 'b_onbed_sit'] auto:
        attribute of_empty default null

    group overlay_face if_all 'b_dressed_tall' auto:
        offset (0, -124)

    group overlay_face if_all 'b_bed_jenny_sit' auto:
        offset (84, -30)
        xzoom -1

    group overlay_face if_all 'b_bed_jenny_sit_back' auto:
        offset (85, 59)
        xzoom -1

    group overlay_face if_any 'b_bed_jenny_laptop' auto:
        offset (-375, 1)
        xzoom -1


    group overlay_face if_any ['b_dinner_sitting', 'b_dinner_sitting_look_left'] auto:
        offset (384, 133)
        zoom .76

    group overlay_face if_any ['b_sit', 'b_sit_naked'] auto:
        offset (161, -13)

    group overlay_face if_any ['b_sit_back', 'b_sit_back_shirt', 'b_sit_back_remove_shorts2'] auto:
        offset (50, 30)

    group overlay_face if_any ['b_sit_naked_up'] auto:
        offset (166, -193)

    group overlay_face if_any ['b_sit_naked_check'] auto:
        offset (195, -138)


    group overlay_face if_all 'b_dressed_car' auto:
        offset (76, -88)

    group overlay_face if_any ['b_dressed_floor', 'b_dressed_floor_barefeet'] auto:
        offset (151, -12)

    group overlay_face if_any  ['b_liu_dressed','b_liu_shorts','b_liu_naked','b_liu_shorts_remove_shorts','b_liu_shorts_throw_shirt'] auto:
        zoom .95
        rotate -10
        offset (89,-112)

    group overlay_face if_any ['b_onbed_back'] auto:
        offset (-42, 0)

    group overlay_face if_any ['b_onbed_sit'] auto:
        offset (22, -29)


    group overlay if_not ['b_shirt_undress_bottom', 'b_naked_undress_bottom', 'b_dressed_floor', 'b_dressed_falling'] auto:
        attribute o_empty default null

    group overlay if_any ['b_sit_back_shirt'] auto variant 'sit_back_shirt':
        attribute o_empty default null

    group overlay if_any ['b_shirt_undress_bottom'] auto variant 'shirt_undress_bottom':
        attribute o_empty default null

    group overlay if_any ['b_naked_undress_bottom'] auto variant 'naked_undress_bottom':
        attribute o_empty default null

    group overlay if_any ['b_dressed_falling'] auto variant 'falling':
        attribute o_empty default null

    group arms if_any ['b_dressed','b_dressed_disheveled']:
        attribute a_cover_boner 'anon_arms_dressed_a_cover_boner'
        attribute a_milk_cups 'anon_arms_dressed_a_milk_cups'


layeredimage anon liu_sex_bedroom:
    group mouth prefix 'm':
        attribute talk null

    group face if_not 'm_talk' auto:
        attribute f_normal default
    group face if_all 'm_talk' auto variant 'talk'


layeredimage anon nadya_sex_cargo:
    group body auto:
        attribute b_pre default
        attribute b_facial1
        attribute b_facial2

    group mouth prefix 'm':
        attribute talk null

    group arms if_any 'b_pre' auto:
        attribute a_pre default

    group overlay if_any 'b_pre' auto variant 'pre'
    group overlay if_any 'b_insert' auto variant 'insert'


layeredimage anon grace_massage_apt:
    at Transform(crop=(0, 0, config.screen_width, config.screen_height))

    attribute m_talk null
    attribute pause null

    group body:
        attribute back 'grace_sex_mc_down_back'
        attribute flip 'grace_sex_body_b_ontop_turn'
        attribute kiss 'grace_sex_body_b_ontop_kiss'
        attribute over 'grace_sex_mc_top'
        attribute peek 'grace_sex_mc_down_back_peek'
        attribute push 'grace_sex_body_b_ontop_arms_sad_push'
        attribute roll 'grace_sex_mc_laying' default
        attribute snog anim.TransitionAnimation(
            'grace_sex_mc_top_kiss1', .5, Dissolve(.3),
            'grace_sex_mc_top_kiss2', .5, Dissolve(.3))

    group face if_all 'm_talk' if_any 'back':
        attribute normal 'anon_face_talk_f_down_back_towel' default

    group face if_not 'm_talk' if_any 'back':
        attribute normal 'anon_face_f_down_back_towel'

    group face if_all 'm_talk' if_any 'peek':
        align (.5, .5)
        offset (13, 27)
        rotate -11.75
        zoom 1.135
        attribute confused 'anon_face_talk_f_confused'
        attribute worried 'anon_face_talk_f_worried'

    group face if_not 'm_talk' if_any 'peek':
        align (.5, .5)
        offset (13, 27)
        rotate -11.75
        zoom 1.135
        attribute confused 'anon_face_f_confused'
        attribute worried 'anon_face_f_worried'

    group far:
        attribute peek 'grace_sex_mc_down_back_peek_arm_top'

    group grace if_any ['back', 'peek']:
        attribute sad 'grace_sex_body_b_ontop_sad'

    group grace if_any ['back']:
        attribute boing 'grace_body_b_ontop'

    group grace if_any ['back'] if_all 'pause':
        attribute rub 'grace_body_b_massage_mc5'
        attribute grind 'grace_body_b_massage_mc1'

    group grace if_any ['back'] if_not 'pause':
        attribute rub anim.TransitionAnimation(
            'grace_body_b_massage_mc5', .7, Dissolve(.3),
            'grace_body_b_massage_mc6', .7, Dissolve(.3))
        attribute grind anim.TransitionAnimation(
            'grace_body_b_massage_mc1', .7, Dissolve(.3),
            'grace_body_b_massage_mc2', .7, Dissolve(.3))

    group grace_arms_sad if_all ['sad'] if_any ['back', 'peek']:
        attribute side 'grace_sex_body_b_ontop_arms_sad_side' default
        attribute wipe 'grace_sex_body_b_ontop_arms_sad_wipe'

    group grace_arms_kiss if_all ['kiss']:
        attribute grip 'grace_sex_body_b_ontop_arms_kiss' default
        attribute surprised 'grace_sex_body_b_ontop_arms_kiss_surprised'

    group near:
        attribute back 'grace_sex_mc_down_back_arm'
        attribute peek 'grace_sex_mc_down_back_peek_arm_front'

    group grace if_any ['back']:
        attribute climb 'grace_body_b_massage_climb'
        attribute pullout 'grace_body_b_massage_pullout'
        attribute pullout1 'grace_body_b_massage_pullout1'
        attribute pullout2 'grace_body_b_massage_pullout2'

    group dick if_any ['back', 'peek']:
        if_not ['boing', 'climb', 'grind', 'pause', 'rub', 'sad', 'pullout',
                'pullout1', 'pullout2']
        attribute soft 'grace_sex_mc_overlay_o_dick_soft' default
        attribute hard 'grace_sex_mc_overlay_o_dick_hard'

    group dick:
        attribute none null

    group dick if_all ['back', 'climb']:
        attribute soft 'grace_sex_mc_overlay_o_climb_dick_soft'
        attribute hard 'grace_sex_mc_overlay_o_climb_dick_hard'

    group dick if_any ['rub'] if_all 'pause':
        attribute firm 'grace_body_b_massage_mc5_dick_mid'
        attribute hard 'grace_body_b_massage_mc5_dick'

    group dick if_any ['rub'] if_not 'pause':
        attribute firm anim.TransitionAnimation(
            'grace_body_b_massage_mc5_dick_mid', .7, Dissolve(.3),
            'grace_body_b_massage_mc6_dick_mid', .7, Dissolve(.3))
        attribute hard anim.TransitionAnimation(
            'grace_body_b_massage_mc5_dick', .7, Dissolve(.3),
            'grace_body_b_massage_mc6_dick', .7, Dissolve(.3))

    group dick if_any ['grind'] if_all 'pause':
        attribute soft 'grace_body_b_massage_mc1_soft'
        attribute firm 'grace_sex_massage_mc1_mid'
        attribute hard 'grace_body_b_massage_mc1_hard'

    group dick if_any ['grind'] if_not 'pause':
        attribute soft anim.TransitionAnimation(
            'grace_body_b_massage_mc1_soft', .7, Dissolve(.3),
            'grace_body_b_massage_mc2_soft', .7, Dissolve(.3))
        attribute firm anim.TransitionAnimation(
            'grace_sex_massage_mc1_mid', .7, Dissolve(.3),
            'grace_sex_massage_mc2_mid', .7, Dissolve(.3))
        attribute hard anim.TransitionAnimation(
            'grace_body_b_massage_mc1_hard', .7, Dissolve(.3),
            'grace_body_b_massage_mc2_hard', .7, Dissolve(.3))

    group dick if_any ['boing']:
        attribute hard 'grace_sex_body_b_ontop_dick'

    group dick if_any ['pullout']:
        attribute cumshot anim.TransitionAnimation(
            'grace_sex_overlay_massage_pullout_o_cum1', .4, Dissolve(.2),
            'grace_sex_overlay_massage_pullout_o_cum2', .4, Dissolve(.2),
            'grace_sex_overlay_massage_pullout_o_cum3')


layeredimage anon grace_sex_apt:
    attribute m_talk null

    group face if_not 'm_talk' auto
    group face if_all 'm_talk' auto variant 'talk'


layeredimage anon maria_sex_side:
    group mouth prefix 'm':
        attribute talk null

    group face if_not 'm_talk' auto:
        attribute f_shy default
    group face if_all 'm_talk' auto variant 'talk'


layeredimage anon khadne_crates_lick:
    attribute m_talk null

    group face if_not 'm_talk' auto
    group face if_all 'm_talk' auto variant 'talk':
        attribute f_normal default


layeredimage anon svet_furnace_blowjob:
    attribute m_talk null

    group face if_not 'm_talk' auto
    group face if_all 'm_talk' auto variant 'talk':
        attribute f_nervous default


layeredimage anon svet_furnace_cowgirl:
    attribute m_talk null

    group face if_not 'm_talk' auto
    group face if_all 'm_talk' auto variant 'talk':
        attribute f_nervous default


layeredimage anon cutscene21:
    group mouth prefix 'm':
        attribute talk null

    group face if_not 'm_talk' auto
    group face if_all 'm_talk' auto variant 'talk'


layeredimage anon cutscene22b:
    group mouth prefix 'm':
        attribute talk null

    group face if_not 'm_talk' auto:
        attribute f_normal default null
    group face if_all 'm_talk' auto variant 'talk'


layeredimage anon cutscene31:
    group mouth prefix 'm':
        attribute talk null

    group face if_not 'm_talk' auto
    group face if_all 'm_talk' auto variant 'talk':
        attribute f_normal default null


layeredimage anon cutscene43:
    group mouth prefix 'm':
        attribute talk null

    group face if_not 'm_talk' auto:
        attribute f_normal default null
    group face if_all 'm_talk' auto variant 'talk'


image anon_f = "characters/anon/anon_face_f_normal.png"

image anon_overlay_face_of_bed_jenny_laying_mask_X = ConditionSwitch(
    "M_jenny.get('cam show mask') == True", "anon_overlay_face_of_bed_jenny_laying_mask",
    "True", "ground.png")

image anon_overlay_face_of_bed_jenny_laying_undies_arms_mask_X = ConditionSwitch(
    "M_jenny.get('cam show mask') == True", "anon_overlay_face_of_bed_jenny_laying_undies_arms_mask",
    "True", "ground.png")

image anon_arms_jacuzzi_naked_a_whisper_back:
    Transform("anon_arms_naked_a_whisper_back",xoffset=-50,yoffset=70)

image anon_arms_jacuzzi_naked_a_massage_foot:
    Transform("anon_arms_jacuzzi_naked_a_massage_foot1")
    pause .4
    Transform("anon_arms_jacuzzi_naked_a_massage_foot2")
    pause .4
    repeat

image anon_arms_jacuzzi_naked_a_massage_foot_calf:
    Transform("anon_arms_jacuzzi_naked_a_massage_foot1")
    pause .3
    Transform("anon_arms_jacuzzi_naked_a_massage_foot2")
    pause .3
    Transform("anon_arms_jacuzzi_naked_a_massage_calf")
    pause .3
    Transform("anon_arms_jacuzzi_naked_a_massage_foot2")
    pause .3
    repeat

image anon_body_b_hammock_thrust_worried_low:
    Transform("anon_body_b_hammock_thrust1_worried_low_comp")
    pause M_player.get('sex speed')
    Transform("anon_body_b_hammock_thrust2_worried_low_comp")
    pause M_player.get('sex speed')
    repeat

image anon_body_b_hammock_thrust1_worried_low_comp = Composite(
    (1025,768),
    (0,0), "characters/anon/anon_body_b_hammock_thrust1.png",
    (-11, 12), "characters/anon/anon_face_f_worried_low.png",
    )

image anon_body_b_hammock_thrust2_worried_low_comp = Composite(
    (1025,768),
    (0,0), "characters/anon/anon_body_b_hammock_thrust2.png",
    (9,25), "characters/anon/anon_face_f_worried_low.png",
    )

image anon_body_b_hammock_thrust_worried:
    Transform("anon_body_b_hammock_thrust1_worried_comp")
    pause M_player.get('sex speed')
    Transform("anon_body_b_hammock_thrust2_worried_comp")
    pause M_player.get('sex speed')
    repeat

image anon_body_b_hammock_thrust1_worried_comp = Composite(
    (1025,768),
    (0,0), "characters/anon/anon_body_b_hammock_thrust1.png",
    (-11, 12), "characters/anon/anon_face_f_worried.png",
    )

image anon_body_b_hammock_thrust2_worried_comp = Composite(
    (1025,768),
    (0,0), "characters/anon/anon_body_b_hammock_thrust2.png",
    (9,25), "characters/anon/anon_face_f_worried.png",
    )

image anon_body_b_hammock_thrust_worried_talk:
    Transform("anon_body_b_hammock_thrust1_worried_talk_comp")
    pause M_player.get('sex speed')
    Transform("anon_body_b_hammock_thrust2_worried_talk_comp")
    pause M_player.get('sex speed')
    repeat

image anon_body_b_hammock_thrust1_worried_talk_comp = Composite(
    (1025,768),
    (0,0), "characters/anon/anon_body_b_hammock_thrust1.png",
    (-11, 12), "characters/anon/anon_face_talk_f_worried.png",
    )

image anon_body_b_hammock_thrust2_worried_talk_comp = Composite(
    (1025,768),
    (0,0), "characters/anon/anon_body_b_hammock_thrust2.png",
    (9,25), "characters/anon/anon_face_talk_f_worried.png",
    )

image anon_body_b_dressed_dance_shy:
    Transform("anon_body_b_dressed_dance1_comp_shy")
    pause .3
    Transform("anon_body_b_dressed_dance2_comp_shy")
    pause .3
    repeat

image anon_body_b_dressed_dance1_comp_shy = Composite(
    (1025,768),
    (0,0), "characters/anon/anon_body_b_dressed_dance1.png",
    (0,0), "characters/anon/anon_face_f_shy.png",
    )

image anon_body_b_dressed_dance2_comp_shy = Composite(
    (1025,768),
    (0,0), "characters/anon/anon_body_b_dressed_dance2.png",
    (-2,0), "characters/anon/anon_face_f_shy.png",
    )

image anon_body_b_dressed_dance_shy_talk:
    Transform("anon_body_b_dressed_dance1_comp_shy_talk")
    pause .3
    Transform("anon_body_b_dressed_dance2_comp_shy_talk")
    pause .3
    repeat

image anon_body_b_dressed_dance1_comp_shy_talk = Composite(
    (1025,768),
    (0,0), "characters/anon/anon_body_b_dressed_dance1.png",
    (0,0), "characters/anon/anon_face_talk_f_shy.png",
    )

image anon_body_b_dressed_dance2_comp_shy_talk = Composite(
    (1025,768),
    (0,0), "characters/anon/anon_body_b_dressed_dance2.png",
    (-2,0), "characters/anon/anon_face_talk_f_shy.png",
    )

image anon_body_b_dressed_dance_flirt_low:
    Transform("anon_body_b_dressed_dance1_comp_flirt_low")
    pause .3
    Transform("anon_body_b_dressed_dance2_comp_flirt_low")
    pause .3
    repeat

image anon_body_b_dressed_dance1_comp_flirt_low = Composite(
    (1025,768),
    (0,0), "characters/anon/anon_body_b_dressed_dance1.png",
    (0,0), "characters/anon/anon_face_f_flirt_low.png",
    )

image anon_body_b_dressed_dance2_comp_flirt_low = Composite(
    (1025,768),
    (0,0), "characters/anon/anon_body_b_dressed_dance2.png",
    (-2,0), "characters/anon/anon_face_f_flirt_low.png",
    )

image anon_body_b_dressed_dance_unimpressed:
    Transform("anon_body_b_dressed_dance1_comp_unimpressed")
    pause .3
    Transform("anon_body_b_dressed_dance2_comp_unimpressed")
    pause .3
    repeat

image anon_body_b_dressed_dance1_comp_unimpressed = Composite(
    (1025,768),
    (0,0), "characters/anon/anon_body_b_dressed_dance1.png",
    (0,0), "characters/anon/anon_face_f_unimpressed.png",
    )

image anon_body_b_dressed_dance2_comp_unimpressed = Composite(
    (1025,768),
    (0,0), "characters/anon/anon_body_b_dressed_dance2.png",
    (-2,0), "characters/anon/anon_face_f_unimpressed.png",
    )

image anon_arms_front_a_jenny_crotch_rub:
    Transform("anon_arms_front_a_jenny_crotch")
    pause .3
    Transform("anon_arms_front_a_jenny_crotch2")
    pause .3
    repeat

image anon_arms_hammock_back_cleaning_a_net:
    Transform("anon_arms_hammock_back_cleaning_a_net1")
    pause .4
    Transform("anon_arms_hammock_back_cleaning_a_net2")
    pause .4
    repeat

image anon_arms_dressed_back_cleaning_a_net:
    Transform("anon_arms_dressed_back_cleaning_a_net1")
    pause .4
    Transform("anon_arms_dressed_back_cleaning_a_net2")
    pause .4
    repeat

image anon_arms_couch_a_boner_cum:
    Transform("anon_arms_couch_a_boner_cum1")
    pause .2
    Transform("anon_arms_couch_a_boner_cum2")
    pause .2

image anon_overlay_o_couch_boner_cum:
    Transform("anon_overlay_o_couch_boner_cum1")
    pause .2
    Transform("anon_overlay_o_couch_boner_cum2")
    pause .2

image anon_arms_couch_a_boner_jerk:
    Transform("anon_arms_couch_a_boner_jerk1")
    pause .3
    Transform("anon_arms_couch_a_boner_jerk2")
    pause .3
    Transform("anon_arms_couch_a_boner_jerk3")
    pause .3
    repeat

image anon_arms_dinner_sitting_a_bowl:
    Transform("anon_arms_dinner_sitting_a_bowl1")
    pause .4
    Transform("anon_arms_dinner_sitting_a_bowl2")
    pause .4
    repeat

image anon_arms_dressed_a_backpack:
    Transform("anon_arms_dressed_a_backpack1")
    pause .4
    Transform("anon_arms_dressed_a_backpack2")
    pause .4
    repeat

image anon_body_b_naked_spin_frown_down:
    Transform("anon_body_b_naked_spin_1_frown_down")
    pause .2
    Transform("anon_body_b_naked_spin_2_frown_down")
    pause .2
    Transform("anon_body_b_naked_spin_3_frown_down")
    pause .2
    repeat

image anon_arms_dressed_floor_a_pat:
    'anon_arms_dressed_floor_a_pat1' with dissolve
    .6
    'anon_arms_dressed_floor_a_pat2' with dissolve
    .6
    repeat

image anon_arms_dressed_floor_a_poke:
    'anon_arms_dressed_floor_a_poke1'
    .4
    'anon_arms_dressed_floor_a_poke2'
    .4
    repeat

image anon_body_b_naked_spin_1_frown_down = Composite(
    (1024,768),
    (0,0), "characters/anon/anon_body_b_naked_spin1.png",
    (-23, 12), "characters/anon/anon_face_f_frown_down.png",
    )

image anon_body_b_naked_spin_2_frown_down = Composite(
    (1024,768),
    (0,0), "characters/anon/anon_body_b_naked_spin2.png",
    (-6, 2), "characters/anon/anon_face_f_frown_down.png",
    )

image anon_body_b_naked_spin_3_frown_down = Composite(
    (1024,768),
    (0,0), "characters/anon/anon_body_b_naked_spin3.png",
    (16, 39), "characters/anon/anon_face_f_frown_down.png",
    )

image anon_body_b_naked_spin_frown_down_talk:
    Transform("anon_body_b_naked_spin_1_frown_down_talk")
    pause .2
    Transform("anon_body_b_naked_spin_2_frown_down_talk")
    pause .2
    Transform("anon_body_b_naked_spin_3_frown_down_talk")
    pause .2
    repeat

image anon_body_b_naked_spin_1_frown_down_talk = Composite(
    (1024,768),
    (0,0), "characters/anon/anon_body_b_naked_spin1.png",
    (-23, 12), "characters/anon/anon_face_talk_f_frown_down.png",
    )

image anon_body_b_naked_spin_2_frown_down_talk = Composite(
    (1024,768),
    (0,0), "characters/anon/anon_body_b_naked_spin2.png",
    (-6, 2), "characters/anon/anon_face_talk_f_frown_down.png",
    )

image anon_body_b_naked_spin_3_frown_down_talk = Composite(
    (1024,768),
    (0,0), "characters/anon/anon_body_b_naked_spin3.png",
    (16, 39), "characters/anon/anon_face_talk_f_frown_down.png",
    )

image anon_body_b_naked_spin_worried_low_talk:
    Transform("anon_body_b_naked_spin_1_worried_low_talk")
    pause .2
    Transform("anon_body_b_naked_spin_2_worried_low_talk")
    pause .2
    Transform("anon_body_b_naked_spin_3_worried_low_talk")
    pause .2
    repeat

image anon_body_b_naked_spin_1_worried_low_talk = Composite(
    (1024,768),
    (0,0), "characters/anon/anon_body_b_naked_spin1.png",
    (-23, 12), "characters/anon/anon_face_talk_f_worried_low.png",
    )

image anon_body_b_naked_spin_2_worried_low_talk = Composite(
    (1024,768),
    (0,0), "characters/anon/anon_body_b_naked_spin2.png",
    (-6, 2), "characters/anon/anon_face_talk_f_worried_low.png",
    )

image anon_body_b_naked_spin_3_worried_low_talk = Composite(
    (1024,768),
    (0,0), "characters/anon/anon_body_b_naked_spin3.png",
    (16, 39), "characters/anon/anon_face_talk_f_worried_low.png",
    )

image anon_body_b_naked_spin_worried_low:
    Transform("anon_body_b_naked_spin_1_worried_low")
    pause .2
    Transform("anon_body_b_naked_spin_2_worried_low")
    pause .2
    Transform("anon_body_b_naked_spin_3_worried_low")
    pause .2
    repeat

image anon_body_b_naked_spin_1_worried_low = Composite(
    (1024,768),
    (0,0), "characters/anon/anon_body_b_naked_spin1.png",
    (-23, 12), "characters/anon/anon_face_f_worried_low.png",
    )

image anon_body_b_naked_spin_2_worried_low = Composite(
    (1024,768),
    (0,0), "characters/anon/anon_body_b_naked_spin2.png",
    (-6, 2), "characters/anon/anon_face_f_worried_low.png",
    )

image anon_body_b_naked_spin_3_worried_low = Composite(
    (1024,768),
    (0,0), "characters/anon/anon_body_b_naked_spin3.png",
    (16, 39), "characters/anon/anon_face_f_worried_low.png",
    )

image anon_body_b_sit_kiss_eve:
    Transform("anon_body_b_sit_kiss_eve1")
    pause .6
    Transform("anon_body_b_sit_kiss_eve2")
    pause .8
    repeat

image anon_arms_dressed_a_give_panties = ConditionSwitch(
    "M_somrak.get('delivered_panties') == 'Debbie'", "characters/anon/anon_arms_dressed_a_panties_debbie2.png",
    "M_somrak.get('delivered_panties') == 'Jenny'", "characters/anon/anon_arms_dressed_a_panties_jenny2.png",
    "M_somrak.get('delivered_panties') == 'Roxxy'", "characters/anon/anon_arms_dressed_a_panties_roxxy2.png",
    "M_somrak.get('delivered_panties') == 'Mia'", "characters/anon/anon_arms_dressed_a_panties_mia2.png",
    "M_somrak.get('delivered_panties') == 'Eve'", "characters/anon/anon_arms_dressed_a_panties_eve2.png",
    "M_somrak.get('delivered_panties') == 'Grace'", "characters/anon/anon_arms_dressed_a_panties_grace2.png",
    "M_somrak.get('delivered_panties') == 'Odette'", "characters/anon/anon_arms_dressed_a_panties_odette2.png",
    "M_somrak.get('delivered_panties') == 'Bridget'", "characters/anon/anon_arms_dressed_a_panties_bridget2.png",
    )

image anon_overlay_dick_shirt_od_dick_spring:
    'anon_overlay_dick_shirt_od_dick3'
    .4
    'anon_overlay_dick_shirt_od_dick4' with fastdissolve

image anon_overlay_dick_sit_back_shirt_od_dick_spring:
    'anon_overlay_dick_sit_back_shirt_od_dick1'
    .5
    'anon_overlay_dick_sit_back_shirt_od_dick2' with dissolve


image anon_nadya_sex_cargo_body_b_facial1:
    'anon_nadya_sex_cargo_body_b_cumshot1'
    .5
    'anon_nadya_sex_cargo_body_b_cumshot2' with dissolve
    .5
    'anon_nadya_sex_cargo_body_b_cumshot3' with dissolve
    .5
    'anon_nadya_sex_cargo_body_b_cumshot4' with dissolve


image anon_nadya_sex_cargo_body_b_facial2:
    'anon_nadya_sex_cargo_body_b_cumshot5'
    .5
    'anon_nadya_sex_cargo_body_b_cumshot6' with dissolve
    .5
    'anon_nadya_sex_cargo_body_b_cumshot7' with dissolve


image anon_overlay_dick_od_naked_dick_grow:
    'anon_overlay_dick_od_naked_dick1'
    .5
    'anon_overlay_dick_od_naked_dick2' with dissolve
    .5
    'anon_overlay_dick_od_naked_dick3' with dissolve


image anon_body_b_dressed_zap:
    Fixed('anon_body_b_dressed_zap1', Transform('anon_overlay_o_taser_barbs_zap', xoffset=115))
    .2
    Fixed('anon_body_b_dressed_zap2', Transform('anon_overlay_o_taser_barbs', xoffset=115))
    .2
    repeat
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
