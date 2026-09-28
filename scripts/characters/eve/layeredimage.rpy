init:
    $ eve_clothing_options = ['b_music_tie','b_naked_pregnant_belly','b_dressed','b_empty','b_dress','b_dressed_headphones_up','b_dress_boner','b_dressed_hug_grace1','b_dressed_hug_grace2','b_dressed_hug_grace3','b_dressed_hug_grace4','b_dressed_disheveled','b_dressed_wet','b_naked','b_naked_shower','b_pajamas_pregnant_belly','b_pajamas_pregnant_bump','b_pajamas','b_dressed_hoodless','b_dressed_headphones_down','b_dressed_crossed','b_music','b_pants','b_sweatshirt_remove','b_undies','b_dressed_surprised','b_topless', 'b_towel']

init python:


    renpy.image('eve_arms_a_empty', 'ground.png')
    renpy.image('eve_body_b_empty', 'ground.png')
    renpy.image('eve_face_f_empty', 'ground.png')
    renpy.image('eve_face_talk_f_empty', 'ground.png')


    renpy.image('eve_face_talk_f_laugh', 'eve_face_f_laugh')
    renpy.image('eve_face_talk_f_sad_thinking', 'eve_face_f_sad_thinking')
    renpy.image('eve_face_talk_f_burp', 'eve_face_f_burp')
    renpy.image('eve_face_talk_f_drink', 'eve_face_f_drink')
    renpy.image('eve_face_talk_f_moo', 'eve_face_f_moo')
    renpy.image('eve_face_talk_f_eat', 'eve_face_f_eat')
    renpy.image('eve_face_undressing_talk_f_exhale', 'eve_face_undressing_f_exhale')
    renpy.image('eve_face_sex_bj_talking_talk_f_swallow_after', 'eve_face_sex_bj_talking_f_swallow_after')




    renpy.image('eve_body_b_desk_look_left', 'eve_body_b_desk') 

layeredimage eve:

    yanchor config.screen_height
    ypos 1.
    xanchor config.screen_width
    xpos 1.

    group arms if_any ['b_naked'] auto variant 'naked_underlay'


    group body auto:
        attribute b_dressed default
        attribute b_empty null
        attribute b_undressing_10 "eve_body_b_undressing_10[M_eve.biggus_dickus]"
        attribute b_undressing_11 "eve_body_b_undressing_11[M_eve.biggus_dickus]"
        attribute b_undressing_12 "eve_body_b_undressing_12[M_eve.biggus_dickus]"
        attribute b_onbed_nude "eve_body_b_onbed_nude[M_eve.biggus_dickus]"
        attribute b_onbed_kiss "eve_body_b_onbed_kiss"
        attribute b_pajamas_kiss "eve_body_b_pajamas_kiss"
        attribute b_onbed_cuddle_naked_kiss "eve_body_b_onbed_cuddle_naked_kiss"
        attribute b_dressed_kiss "eve_body_b_dressed_kiss"
        attribute b_dress_kiss "eve_body_b_dress_kiss"
        attribute b_undies_kiss "eve_body_b_undies_kiss"
        attribute b_back_insert "eve_body_b_back_insert[M_eve.biggus_dickus]"
        attribute b_back_cum "eve_body_b_back_cum"
        attribute b_front_pre "eve_body_b_front_pre[M_eve.biggus_dickus]"
        attribute b_front_insert "eve_body_b_front_insert[M_eve.biggus_dickus]"
        attribute b_front_after "eve_body_b_front_after[M_eve.biggus_dickus]"
        attribute b_undies "eve_body_b_undies[M_eve.biggus_dickus]"
        attribute b_pajamas_bed_side_kiss "eve_body_b_pajamas_bed_side_kiss"
        attribute b_naked_shower_kiss "eve_body_b_naked_shower_kiss"
        attribute b_naked_shower_pickup "eve_body_b_naked_shower_pickup[M_eve.biggus_dickus]"
        attribute b_naked_shower_pickup01 "eve_body_b_naked_shower_pickup01[M_eve.biggus_dickus]"
        attribute b_naked_shower_pickup02 "eve_body_b_naked_shower_pickup02[M_eve.biggus_dickus]"
        attribute b_towel_kiss "eve_body_b_towel_kiss"


    group mouth prefix 'm':
        attribute talk null

    group face:
        attribute f_normal default null







    group face if_not 'm_talk' if_any eve_clothing_options auto


    group face if_not 'm_talk' if_any ['b_onbed_dressed','b_onbed_topless','b_onbed_tanktop','b_onbed_tanktop_remove1','b_onbed_panties','b_onbed_nude'] auto:
        offset (-34, -34)


    group face if_not 'm_talk' if_any ['b_onbed_tanktop_remove2','b_onbed_top_remove4'] auto:
        offset (82, 35)


    group face if_not 'm_talk' if_all 'b_dressed_tired' auto:
        offset (-72, 110)


    group face if_not 'm_talk' if_all 'b_dressed_scared' auto:
        offset (-49, 28)


    group face if_not 'm_talk' if_any ['b_sidebed','b_dress_sidebed'] auto:
        offset (-105, -15)


    group face if_not 'm_talk' if_all 'b_desk' auto:
        offset (2, 70)
        xzoom -1


    group face if_not 'm_talk' if_all 'b_desk_look_left' auto:
        offset (2, 70)
        xzoom -1
        attribute f_normal "eve_face_f_normal_right"
        attribute f_worried "eve_face_f_worried_right"
        attribute f_wink "eve_face_f_wink_right"
        attribute f_sad "eve_face_f_sad_right"
        attribute f_happy "eve_face_f_happy_right"
        attribute f_nervous "eve_face_f_nervous_right"
        attribute f_confused "eve_face_f_confused_right"


    group face if_not 'm_talk' if_all 'b_gown_bed' auto:
        offset (75, 24)


    group face if_not 'm_talk' if_any 'b_pajamas_bed_side' auto:
        offset (-102, -114)

    group face if_not 'm_talk' if_any ['b_naked_shower_kiss', 'b_naked_shower_kiss01'] auto:
        xoffset -291






    group face if_not 'm_talk' if_any ['b_onbed_cuddle','b_onbed_cuddle_naked'] auto variant 'onbed_cuddle'


    group face if_not 'm_talk' if_all 'b_undressing_01' auto variant 'undressing'


    group face if_not 'm_talk' if_all 'b_undressing_08' auto variant 'undressing':
        offset (39, -64)


    group face if_not 'm_talk' if_all 'b_undressing_12' auto variant 'undressing':
        offset (29, -30)


    group face if_not 'm_talk' if_all 'b_sex_bj_talking' auto variant 'sex_bj_talking'


    group face if_not 'm_talk' if_any ['b_front_after_anal','b_front_insert_anal','b_sex_jerk_alt','b_sex_jerk','b_front_pre','b_front_after','b_front_after_alt','b_front_insert','b_front_insert_alt'] auto variant 'sex_front'


    group face if_not 'm_talk' if_any 'b_pajamas_bed_back' auto variant 'pajamas_bed_back':
        attribute f_normal 'eve_face_pajamas_bed_back_f_calm'


    group face if_not 'm_talk' if_any ['b_pajamas_sleeping01','b_pajamas_sleeping02','b_pajamas_sleeping03'] auto variant 'sleep'







    group face if_all 'm_talk' if_any eve_clothing_options auto variant 'talk'


    group face if_all 'm_talk' if_any ['b_onbed_dressed','b_onbed_topless','b_onbed_tanktop','b_onbed_tanktop_remove1','b_onbed_panties','b_onbed_nude'] auto variant 'talk':
        offset (-34, -34)


    group face if_all 'm_talk' if_any ['b_onbed_tanktop_remove2','b_onbed_top_remove4'] auto variant 'talk':
        offset (82, 35)


    group face if_all ['m_talk', 'b_dressed_tired'] auto variant 'talk':
        offset (-72, 110)


    group face if_all ['m_talk', 'b_dressed_scared'] auto variant 'talk':
        offset (-49, 28)


    group face if_all 'm_talk' if_any ['b_sidebed','b_dress_sidebed'] auto variant 'talk':
        offset (-105, -15)


    group face if_all ['m_talk', 'b_desk'] auto variant 'talk':
        offset (2, 70)
        xzoom -1


    group face if_all ['m_talk', 'b_desk_look_left'] auto variant 'talk':
        offset (2, 70)
        xzoom -1
        attribute f_normal "eve_face_talk_f_normal_right"
        attribute f_worried "eve_face_talk_f_worried_right"
        attribute f_wink "eve_face_talk_f_wink_right"
        attribute f_sad "eve_face_talk_f_sad_right"
        attribute f_happy "eve_face_talk_f_happy_right"
        attribute f_nervous "eve_face_talk_f_nervous_right"
        attribute f_confused "eve_face_talk_f_confused_right"


    group face if_all ['m_talk','b_gown_bed'] auto variant 'talk':
        offset (75, 24)


    group face if_all 'm_talk' if_any 'b_pajamas_bed_side' auto variant 'talk':
        offset (-102, -114)

    group face if_all 'm_talk' if_any ['b_naked_shower_kiss', 'b_naked_shower_kiss01'] auto variant 'talk':
        xoffset -291






    group face if_all 'm_talk' if_any ['b_onbed_cuddle','b_onbed_cuddle_naked'] auto variant 'onbed_cuddle_talk'


    group face if_all ['m_talk','b_undressing_01'] auto variant 'undressing_talk'


    group face if_all ['m_talk','b_undressing_08'] auto variant 'undressing_talk':
        offset (39, -64)


    group face if_all ['m_talk','b_undressing_12'] auto variant 'undressing_talk':
        offset (29, -30)


    group face if_all ['m_talk','b_sex_bj_talking'] auto variant 'sex_bj_talking_talk'


    group face if_all 'm_talk' if_any ['b_front_after_anal','b_front_insert_anal','b_sex_jerk_alt','b_sex_jerk','b_front_pre','b_front_after','b_front_insert'] auto variant 'sex_front_talk'


    group face if_all 'm_talk' if_any 'b_pajamas_bed_back' auto variant 'pajamas_bed_back_talk':
        attribute f_normal 'eve_face_pajamas_bed_back_talk_f_calm'


    group face if_all 'm_talk' if_any ['b_pajamas_sleeping01','b_pajamas_sleeping02','b_pajamas_sleeping03'] auto variant 'sleep_talk'


    group overlay_dick if_any ['b_naked', 'b_naked_shower'] auto:
        attribute od_empty default null

    group overlay_dick if_any ['b_naked_shower_kiss', 'b_naked_shower_kiss01'] auto:
        xoffset -291
        attribute od_dick_grow 'eve_overlay_dick_od_dick_grow'



    group arms if_any ['b_dressed','b_dressed_disheveled','b_dressed_headphones_up','b_dressed_wet','b_dressed_hoodless','b_dressed_headphones_down','b_dressed_crossed','b_music'] auto variant 'dressed':
        attribute a_idle default 'eve_arms_dressed_a_crossed'


    group arms if_any ['b_dress','b_dress_boner'] auto variant 'dress':
        attribute a_idle default 'eve_arms_dress_a_crossed'


    group arms if_all 'b_onbed_dressed' auto variant 'onbed_dressed':
        attribute a_idle default 'eve_arms_onbed_dressed_a_down'


    group arms if_all 'b_onbed_topless' auto variant 'onbed_topless':
        attribute a_idle default 'eve_arms_onbed_topless_a_down'


    group arms if_all 'b_onbed_tanktop' auto variant 'onbed_tanktop':
        attribute a_idle default 'eve_arms_onbed_tanktop_a_down'


    group arms if_all 'b_onbed_panties' auto variant 'onbed_panties':
        attribute a_idle default 'eve_arms_onbed_panties_a_down'


    group arms if_any ['b_onbed_cuddle'] auto variant 'onbed_cuddle':
        attribute a_idle default 'eve_arms_onbed_cuddle_a_chest'
        attribute a_touch 'eve_arms_onbed_cuddle_a_touch'
        attribute a_jerk 'eve_arms_onbed_cuddle_naked_a_jerk'
        attribute a_jerk1 'eve_arms_onbed_cuddle_naked_a_jerk1'
        attribute a_jerk2 'eve_arms_onbed_cuddle_naked_a_jerk2'
        attribute a_taste 'eve_arms_onbed_cuddle_naked_a_taste'


    group arms if_any ['b_onbed_cuddle_naked'] auto variant 'onbed_cuddle_naked':
        attribute a_idle default 'eve_arms_onbed_cuddle_naked_a_chest'
        attribute a_jerk 'eve_arms_onbed_cuddle_naked_a_jerk'


    group arms if_any ['b_onbed_cuddle_naked_kiss2','b_onbed_cuddle_naked_kiss1','b_onbed_cuddle_naked_kiss'] auto variant 'onbed_cuddle_naked_kiss':
        attribute a_idle default 'eve_arms_onbed_cuddle_naked_kiss_a_chest'
        attribute a_jerk 'eve_arms_onbed_cuddle_naked_kiss_a_jerk'


    group arms if_any ['b_naked', 'b_naked_shower'] auto variant 'naked':
        attribute a_idle default 'eve_arms_naked_a_crossed'
        attribute a_cover null

    group arms if_any ['b_naked_shower'] auto variant 'naked_shower':
        attribute a_scrub 'eve_arms_naked_shower_a_scrub'
        attribute a_dry_hair 'eve_arms_naked_shower_a_dry_hair'


    group arms if_all 'b_towel' auto variant 'towel':
        attribute a_idle default 'eve_arms_towel_a_sides'


    group arms if_all 'b_naked_pregnant_belly' auto variant 'naked_pregnant_belly':
        attribute a_idle default 'eve_arms_naked_pregnant_belly_a_touch'


    group arms if_all 'b_pajamas' auto variant 'pajamas':
        attribute a_idle default 'eve_arms_pajamas_a_crossed'
        attribute a_baby "eve_arms_pajamas_a_baby_[M_eve.pregnancy.baby_gender]"


    group arms if_all 'b_pajamas_pregnant_bump' auto variant 'pajamas_pregnant_bump':
        attribute a_idle default 'eve_arms_pajamas_pregnant_bump_a_touch'
        attribute a_squeeze 'eve_arms_pajamas_pregnant_bump_a_squeeze'


    group arms if_all 'b_pajamas_pregnant_belly' auto variant 'pajamas_pregnant_belly':
        attribute a_idle default 'eve_arms_pajamas_pregnant_belly_a_touch'


    group arms if_any ['b_undies'] auto variant 'undies':
        attribute a_idle default 'eve_arms_naked_a_hip'
        attribute a_hip 'eve_arms_naked_a_hip'


    group arms if_any ['b_desk','b_desk_look_left'] auto variant 'desk':
        attribute a_idle default 'eve_arms_desk_a_down'


    group arms if_all 'b_topless' auto variant 'topless':
        attribute a_idle default 'eve_arms_topless_a_crossed'


    group arms if_all 'b_pants' auto variant 'pants':
        attribute a_idle default 'eve_arms_pants_a_hip'


    group arms if_all 'b_sweatshirt_remove' auto variant 'sweatshirt_remove':
        attribute a_idle default 'eve_arms_sweatshirt_remove_a_front'


    group arms if_all 'b_gown_bed' auto variant 'gown_bed':
        attribute a_idle default "eve_arms_gown_bed_a_baby_[M_eve.pregnancy.baby_gender]"


    group arms if_all 'b_sidebed' auto variant 'sidebed':
        attribute a_idle default 'eve_arms_sidebed_a_down'
        attribute a_hair 'eve_arms_sidebed_a_hair'


    group arms if_all 'b_dress_sidebed' auto variant 'dress_sidebed':
        attribute a_idle default 'eve_arms_dress_sidebed_a_normal'


    group arms if_all 'b_sex_bj_talking' auto variant 'sex_bj_talking':
        attribute a_idle default 'eve_arms_sex_bj_talking_a_jerk'


    group arms if_any 'b_pajamas_bed_back' auto variant 'pajamas_bed_back':
        attribute a_idle default 'eve_arms_pajamas_bed_back_a_belly'
        attribute a_empty null


    group arms if_any 'b_pajamas_bed_side' auto variant 'pajamas_bed_side':
        attribute a_idle default 'eve_arms_pajamas_bed_side_a_belly'
        attribute a_empty null


    group overlay if_not 'b_onbed_cuddle' auto:
        attribute o_empty default null

    group overlay if_all 'b_onbed_cuddle' auto variant 'onbed_cuddle':
        attribute o_empty default null

    group overlay if_any ['b_onbed_cuddle_naked','b_onbed_cuddle_naked_kiss'] auto variant 'onbed_cuddle_naked':
        attribute o_empty default null
        attribute o_cum "eve_overlay_onbed_cuddle_naked_o_cum"

    group overlay if_all 'b_sex_bj_pre' auto variant 'sex_bj_pre':
        attribute o_empty default null

image eve_f = "characters/eve/eve_face_f_normal.png"
image eve_f2 = "characters/eve/eve_face_undressing_talk_f_shy.png"

image eve_overlay_dick_od_dick_grow:
    'eve_overlay_dick_od_dick01'
    .5
    'eve_overlay_dick_od_dick02' with dissolve
    .5
    'eve_overlay_dick_od_dick03' with dissolve

image eve_arms_sidebed_a_hair:
    Transform("eve_arms_sidebed_a_hair1")
    pause .6
    Transform("eve_arms_sidebed_a_hair2")
    pause .8
    repeat

image eve_arms_onbed_cuddle_a_touch:
    Transform("eve_arms_onbed_cuddle_a_touch1")
    pause .6
    Transform("eve_arms_onbed_cuddle_a_touch2")
    pause .8
    repeat

image eve_body_b_onbed_kiss:
    Transform("eve_body_b_onbed_kiss1")
    pause .6
    Transform("eve_body_b_onbed_kiss2")
    pause .8
    repeat

image eve_body_b_pajamas_kiss:
    Transform("eve_body_b_pajamas_kiss1")
    pause .6
    Transform("eve_body_b_pajamas_kiss2")
    pause .8
    repeat

image eve_body_b_onbed_cuddle_naked_kiss:
    Transform("eve_body_b_onbed_cuddle_naked_kiss1")
    pause .6
    Transform("eve_body_b_onbed_cuddle_naked_kiss2")
    pause .8
    repeat

image eve_body_b_dressed_kiss:
    Transform("eve_body_b_dressed_kiss1")
    pause .6
    Transform("eve_body_b_dressed_kiss2")
    pause .8
    repeat

image eve_body_b_undies_kiss:
    Transform("eve_body_b_undies_kiss1")
    pause .6
    Transform("eve_body_b_undies_kiss2")
    pause .8
    repeat

image eve_body_b_dress_kiss:
    Transform("eve_body_b_dress_kiss1")
    pause .6
    Transform("eve_body_b_dress_kiss2")
    pause .8
    repeat

image eve_body_b_naked_shower_kiss:
    'eve_body_b_naked_shower_kiss01'
    .4
    'eve_body_b_naked_shower_kiss02'
    .4
    repeat

image eve_arms_naked_shower_a_dry_hair:
    'eve_arms_naked_shower_a_dry_hair01'
    .4
    'eve_arms_naked_shower_a_dry_hair02'
    .4
    repeat

image eve_body_b_naked_shower_pickup01_alt = Fixed(
    'eve_body_b_naked_shower_pickup01', 'eve_overlay_o_shower_pickup_balls01')
image eve_body_b_naked_shower_pickup02_alt = Fixed(
    'eve_body_b_naked_shower_pickup02', 'eve_overlay_o_shower_pickup_balls02')

image eve_body_b_naked_shower_pickup = anim.TransitionAnimation(
    'eve_body_b_naked_shower_pickup01', .4, fastdissolve,
    'eve_body_b_naked_shower_pickup02', .4, fastdissolve)

image eve_body_b_naked_shower_pickup_alt = anim.TransitionAnimation(
    'eve_body_b_naked_shower_pickup01_alt', .4, fastdissolve,
    'eve_body_b_naked_shower_pickup02_alt', .4, fastdissolve)

image eve_arms_naked_shower_a_scrub = anim.TransitionAnimation(
    'eve_arms_naked_shower_a_scrub01', .7, dissolve,
    'eve_arms_naked_shower_a_scrub02', .7, dissolve)

image eve_body_b_towel_kiss:
    'eve_body_b_towel_kiss1'
    .4
    'eve_body_b_towel_kiss2'
    .4
    repeat

image eve_body_b_pajamas_bed_side_kiss = anim.TransitionAnimation(
    'eve_body_b_pajamas_bed_side_kiss01', .4, fastdissolve,
    'eve_body_b_pajamas_bed_side_kiss02', .4, fastdissolve)

image eve_arms_sex_bj_talking_a_jerk:
    Transform("eve_arms_sex_bj_talking_a_jerk1")
    pause .4
    Transform("eve_arms_sex_bj_talking_a_jerk2")
    pause .4
    repeat

image eve_arms_pajamas_pregnant_bump_a_squeeze:
    Transform("eve_arms_pajamas_pregnant_bump_a_squeeze1")
    pause .4
    Transform("eve_arms_pajamas_pregnant_bump_a_squeeze2")
    pause .4
    repeat

image eve_arms_onbed_cuddle_naked_kiss_a_jerk:
    Transform("eve_arms_onbed_cuddle_naked_kiss_a_jerk1")
    pause .4
    Transform("eve_arms_onbed_cuddle_naked_kiss_a_jerk2")
    pause .4
    repeat

image eve_arms_onbed_cuddle_naked_a_jerk:
    Transform("eve_arms_onbed_cuddle_naked_a_jerk1")
    pause M_eve.get("sex speed")
    Transform("eve_arms_onbed_cuddle_naked_a_jerk2")
    pause M_eve.get("sex speed")
    repeat

image eve_overlay_onbed_cuddle_naked_o_cum:
    Transform("eve_overlay_onbed_cuddle_naked_o_cum1")
    pause .4
    Transform("eve_overlay_onbed_cuddle_naked_o_cum2")
    pause .4
    Transform("eve_overlay_onbed_cuddle_naked_o_cum3")



image eve_jerk_body = "eve_sex_jerk_body"
image eve_jerk_body_alt = "eve_sex_jerk_body_alt"

image eve_jerk_body cum = "eve_sex_jerk_cum"
image eve_jerk_body_alt cum = "eve_sex_jerk_cum_alt"

image eve_sex_jerk 1 = "eve_sex_jerk_anim01"
image eve_sex_jerk 2 = "eve_sex_jerk_anim02"
image eve_sex_jerk 3 = "eve_sex_jerk_anim03"
image eve_sex_jerk 4 = "eve_sex_jerk_anim04"
image eve_sex_jerk 5 = "eve_sex_jerk_anim05"
image eve_sex_jerk 6 = "eve_sex_jerk_anim06"

image eve_sex_jerk_alt 1 = "eve_sex_jerk_anim01_alt"
image eve_sex_jerk_alt 2 = "eve_sex_jerk_anim02_alt"
image eve_sex_jerk_alt 3 = "eve_sex_jerk_anim03_alt"
image eve_sex_jerk_alt 4 = "eve_sex_jerk_anim04_alt"
image eve_sex_jerk_alt 5 = "eve_sex_jerk_anim05_alt"
image eve_sex_jerk_alt 6 = "eve_sex_jerk_anim06_alt"
image eve_sex_jerk_alt 7 = "eve_sex_jerk_anim07_alt"
image eve_sex_jerk_alt 8 = "eve_sex_jerk_anim08_alt"
image eve_sex_jerk_alt 9 = "eve_sex_jerk_anim09_alt"
image eve_sex_jerk_alt 10 = "eve_sex_jerk_anim10_alt"
image eve_sex_jerk_alt 11 = "eve_sex_jerk_anim11_alt"

image eve_sex_jerk_cumshot:
    Transform("eve_sex_jerk_cum_cumshot01")
    pause .4
    Transform("eve_sex_jerk_cum_cumshot02")
    pause .4
    Transform("eve_sex_jerk_cum_cumshot03")

image eve_sex_front_face_mc normal = "eve_sex_front_face_mc_normal"
image eve_sex_front_face_mc normal_talk = "eve_sex_front_face_mc_normal_talk"
image eve_sex_front_face_mc normal_down = "eve_sex_front_face_mc_normal_down"
image eve_sex_front_face_mc cum = "eve_sex_front_face_mc_cum"

image eve_sex_back 1 = "eve_sex_back_anim_01"
image eve_sex_back 2 = "eve_sex_back_anim_02"
image eve_sex_back 3 = "eve_sex_back_anim_03"
image eve_sex_back 4 = "eve_sex_back_anim_04"
image eve_sex_back 5 = "eve_sex_back_anim_05"
image eve_sex_back 6 = "eve_sex_back_anim_06"
image eve_sex_back 7 = "eve_sex_back_anim_07"
image eve_sex_back 8 = "eve_sex_back_anim_08"
image eve_sex_back 9 = "eve_sex_back_anim_09"

image eve_sex_back_alt 1 = "eve_sex_back_anim_01_alt"
image eve_sex_back_alt 2 = "eve_sex_back_anim_02_alt"
image eve_sex_back_alt 3 = "eve_sex_back_anim_03_alt"
image eve_sex_back_alt 4 = "eve_sex_back_anim_04_alt"
image eve_sex_back_alt 5 = "eve_sex_back_anim_05_alt"
image eve_sex_back_alt 6 = "eve_sex_back_anim_06_alt"
image eve_sex_back_alt 7 = "eve_sex_back_anim_07_alt"
image eve_sex_back_alt 8 = "eve_sex_back_anim_08_alt"
image eve_sex_back_alt 9 = "eve_sex_back_anim_09_alt"

image eve_overlay_sex_back o_pre_alt = "eve_overlay_sex_back_pre_o_alt"
image eve_overlay_sex_back o_after_alt = "eve_overlay_sex_back_after_o_alt"
image eve_overlay_sex_back o_cumshot = "eve_overlay_sex_back_cumshot_o_cumshot"
image eve_overlay_sex_back o_cumshot3 = "eve_overlay_sex_back_cumshot_o_cumshot3"
image eve_overlay_sex_back o_pullout = "eve_overlay_sex_back_insert_o_pullout[M_eve.biggus_dickus]"

image eve_body_b_back_cum:
    Transform("eve_body_b_back_cum1")
    pause .4
    Transform("eve_body_b_back_cum2")
    pause .4
    repeat

image eve_overlay_sex_back_cumshot_o_cumshot:
    Transform("eve_overlay_sex_back_cumshot_o_cumshot1")
    pause .4
    Transform("eve_overlay_sex_back_cumshot_o_cumshot2")
    pause .4
    Transform("eve_overlay_sex_back_cumshot_o_cumshot3")

image eve_sex_front 1 = "eve_sex_front_anim_01"
image eve_sex_front 2 = "eve_sex_front_anim_02"
image eve_sex_front 3 = "eve_sex_front_anim_03"
image eve_sex_front 4 = "eve_sex_front_anim_04"
image eve_sex_front 5 = "eve_sex_front_anim_05"
image eve_sex_front 6 = "eve_sex_front_anim_06"

image eve_sex_front_anal 1 = "eve_sex_front_anim_01_anal"
image eve_sex_front_anal 2 = "eve_sex_front_anim_02_anal"
image eve_sex_front_anal 3 = "eve_sex_front_anim_03_anal"
image eve_sex_front_anal 4 = "eve_sex_front_anim_04_anal"
image eve_sex_front_anal 5 = "eve_sex_front_anim_05_anal"
image eve_sex_front_anal 6 = "eve_sex_front_anim_06_anal"

image eve_sex_front_alt 1 = "eve_sex_front_anim_01_alt"
image eve_sex_front_alt 2 = "eve_sex_front_anim_02_alt"
image eve_sex_front_alt 3 = "eve_sex_front_anim_03_alt"
image eve_sex_front_alt 4 = "eve_sex_front_anim_04_alt"
image eve_sex_front_alt 5 = "eve_sex_front_anim_05_alt"
image eve_sex_front_alt 6 = "eve_sex_front_anim_06_alt"

image eve_overlay_sex_front o_creampie = "eve_overlay_sex_front_after_o_creampie[M_eve.biggus_dickus]"
image eve_overlay_sex_front o_cumshot = "eve_overlay_sex_front_after_o_cumshot"
image eve_overlay_sex_front o_cumshot3 = "eve_overlay_sex_front_after_o_cumshot3"
image eve_overlay_sex_front o_cumshot_alt = "eve_overlay_sex_front_cum_o_cumshot_alt"
image eve_overlay_sex_front o_cum_alt = "eve_overlay_sex_front_o_cum_alt"
image eve_overlay_sex_front o_cum_anal = "eve_overlay_sex_front_o_cum_anal"
image eve_overlay_sex_front o_pullout_anal = "eve_overlay_sex_front_after_o_pullout_anal"
image eve_overlay_sex_front o_pullout = "eve_overlay_sex_front_after_o_pullout[M_eve.biggus_dickus]"

image eve_overlay_sex_front_after_o_cumshot:
    Transform("eve_overlay_sex_front_after_o_cumshot1")
    pause .4
    Transform("eve_overlay_sex_front_after_o_cumshot2")
    pause .4
    Transform("eve_overlay_sex_front_after_o_cumshot3")

image eve_overlay_sex_front_cum_o_cumshot_alt:
    Transform("eve_overlay_sex_front_cum_o_cumshot1_alt")
    pause .4
    Transform("eve_overlay_sex_front_cum_o_cumshot2_alt")
    pause .4
    Transform("eve_overlay_sex_front_cum_o_cumshot3_alt")

image eve_sex_bj 1 = "eve_sex_bj_anim_01"
image eve_sex_bj 2 = "eve_sex_bj_anim_02"
image eve_sex_bj 3 = "eve_sex_bj_anim_03"
image eve_sex_bj 4 = "eve_sex_bj_anim_04"
image eve_sex_bj 5 = "eve_sex_bj_anim_05"
image eve_sex_bj 6 = "eve_sex_bj_anim_06"
image eve_sex_bj 7 = "eve_sex_bj_anim_07"
image eve_sex_bj 8 = "eve_sex_bj_anim_08"
image eve_sex_bj 9 = "eve_sex_bj_anim_09"
image eve_sex_bj 10 = "eve_sex_bj_anim_10"

image eve_sex_bj_mc_body = "eve_sex_bj_mc"

image eve_sex_bj_mc_face pre = "eve_sex_bj_face_pre"
image eve_sex_bj_mc_face after_alt = "eve_sex_bj_face_after_alt"
image eve_sex_bj_mc_face after = "eve_sex_bj_face_after"





image xray_eve_back:
    Transform("characters/xray/xray_left_back_01.png", zoom=.75, rotate=-20, xoffset=250, yoffset=30)
    pause 0.4
    Transform("characters/xray/xray_left_back_02.png", zoom=.75, rotate=-20, xoffset=250, yoffset=30)
    pause 0.4
    Transform("characters/xray/xray_left_back_03.png", zoom=.75, rotate=-20, xoffset=250, yoffset=30)
    pause 0.4
    Transform("characters/xray/xray_left_back_04.png", zoom=.75, rotate=-20, xoffset=250, yoffset=30)
    pause 0.4
    Transform("characters/xray/xray_left_back_05.png", zoom=.75, rotate=-20, xoffset=250, yoffset=30)
    pause 0.4
    Transform("characters/xray/xray_left_back_06.png", zoom=.75, rotate=-20, xoffset=250, yoffset=30)
    pause 0.4
    Transform("characters/xray/xray_left_back_07.png", zoom=.75, rotate=-20, xoffset=250, yoffset=30)
    pause 0.4
    Transform("characters/xray/xray_left_back_08.png", zoom=.75, rotate=-20, xoffset=250, yoffset=30)
    pause 0.4
    Transform("characters/xray/xray_left_back_09.png", zoom=.75, rotate=-20, xoffset=250, yoffset=30)
    pause 0.4
    Transform("characters/xray/xray_left_back_10.png", zoom=.75, rotate=-20, xoffset=250, yoffset=30)
    pause 0.4
    Transform("characters/xray/xray_left_back_11.png", zoom=.75, rotate=-20, xoffset=250, yoffset=30)
    pause 0.4
    Transform("characters/xray/xray_left_back_12.png", zoom=.75, rotate=-20, xoffset=250, yoffset=30)
    pause 0.4
    Transform("characters/xray/xray_left_back_13.png", zoom=.75, rotate=-20, xoffset=250, yoffset=30)
    pause 0.4
    Transform("characters/xray/xray_left_back_14.png", zoom=.75, rotate=-20, xoffset=250, yoffset=30)
    pause 0.4
    Transform("characters/xray/xray_left_back_15.png", zoom=.75, rotate=-20, xoffset=250, yoffset=30)
    pause 0.4
    Transform("characters/xray/xray_left_back_16.png", zoom=.75, rotate=-20, xoffset=250, yoffset=30)
    pause 0.4
    Transform("characters/xray/xray_left_back_17.png", zoom=.75, rotate=-20, xoffset=250, yoffset=30)
    pause 0.4
    Transform("characters/xray/xray_left_back_18.png", zoom=.75, rotate=-20, xoffset=250, yoffset=30)
    pause 2.0
    linear 2.5 alpha 0

image xray_eve_front:
    Transform("characters/xray/xray_under_01.png", xzoom=-0.6, yzoom=.7, rotate=-100, xoffset=190, yoffset=170)
    pause 0.4
    Transform("characters/xray/xray_under_02.png", xzoom=-0.6, yzoom=.7, rotate=-100, xoffset=190, yoffset=170)
    pause 0.4
    Transform("characters/xray/xray_under_03.png", xzoom=-0.6, yzoom=.7, rotate=-100, xoffset=190, yoffset=170)
    pause 0.4
    Transform("characters/xray/xray_under_04.png", xzoom=-0.6, yzoom=.7, rotate=-100, xoffset=190, yoffset=170)
    pause 0.4
    Transform("characters/xray/xray_under_05.png", xzoom=-0.6, yzoom=.7, rotate=-100, xoffset=190, yoffset=170)
    pause 0.4
    Transform("characters/xray/xray_under_06.png", xzoom=-0.6, yzoom=.7, rotate=-100, xoffset=190, yoffset=170)
    pause 0.4
    Transform("characters/xray/xray_under_07.png", xzoom=-0.6, yzoom=.7, rotate=-100, xoffset=190, yoffset=170)
    pause 0.4
    Transform("characters/xray/xray_under_08.png", xzoom=-0.6, yzoom=.7, rotate=-100, xoffset=190, yoffset=170)
    pause 0.4
    Transform("characters/xray/xray_under_09.png", xzoom=-0.6, yzoom=.7, rotate=-100, xoffset=190, yoffset=170)
    pause 0.4
    Transform("characters/xray/xray_under_10.png", xzoom=-0.6, yzoom=.7, rotate=-100, xoffset=190, yoffset=170)
    pause 0.4
    Transform("characters/xray/xray_under_11.png", xzoom=-0.6, yzoom=.7, rotate=-100, xoffset=190, yoffset=170)
    pause 0.4
    Transform("characters/xray/xray_under_12.png", xzoom=-0.6, yzoom=.7, rotate=-100, xoffset=190, yoffset=170)
    pause 0.4
    Transform("characters/xray/xray_under_13.png", xzoom=-0.6, yzoom=.7, rotate=-100, xoffset=190, yoffset=170)
    pause 0.4
    Transform("characters/xray/xray_under_14.png", xzoom=-0.6, yzoom=.7, rotate=-100, xoffset=190, yoffset=170)
    pause 0.4
    Transform("characters/xray/xray_under_15.png", xzoom=-0.6, yzoom=.7, rotate=-100, xoffset=190, yoffset=170)
    pause 0.4
    Transform("characters/xray/xray_under_16.png", xzoom=-0.6, yzoom=.7, rotate=-100, xoffset=190, yoffset=170)
    pause 0.4
    Transform("characters/xray/xray_under_17.png", xzoom=-0.6, yzoom=.7, rotate=-100, xoffset=190, yoffset=170)
    pause 0.4
    Transform("characters/xray/xray_under_18.png", xzoom=-0.6, yzoom=.7, rotate=-100, xoffset=190, yoffset=170)
    pause 2.0
    linear 2.5 alpha 0


layeredimage eve sex_wake cis:
    group body:
        attribute pre default 'eve_body_b_sex_wakeup_base'
        attribute insert 'eve_body_b_sex_wakeup_base'
        attribute enter 'eve_body_b_sex_wakeup_anim01'
        attribute slam 'eve_body_b_sex_wakeup_cum_base'
        attribute cum 'eve_body_b_sex_wakeup_cum_base'
        attribute pullout 'eve_body_b_sex_wakeup_base'
        attribute after 'eve_body_b_sex_wakeup_base'
        attribute cumshot 'eve_body_b_sex_wakeup_base'

    attribute m_talk null

    group face if_not 'm_talk':
        attribute horny default 'eve_face_f_sex_wakeup_horny'
        attribute embarrassed 'eve_face_f_sex_wakeup_embarrassed'
        attribute surprised 'eve_face_f_sex_wakeup_embarrassed_surprised'

    group face if_all 'm_talk':
        attribute horny 'eve_face_talk_f_sex_wakeup_horny'
        attribute embarrassed 'eve_face_talk_f_sex_wakeup_embarrassed'
        attribute surprised 'eve_face_talk_f_sex_wakeup_embarrassed_surprised'

    group face:
        attribute gasp 'eve_face_f_sex_wakeup_insert'
        attribute laugh 'eve_face_f_sex_wakeup_laugh'
        attribute lipbite 'eve_face_f_sex_wakeup_lipbite'
        attribute enter null
        attribute cum null
        attribute slam null

    group genitals:
        attribute pre 'eve_body_b_sex_wakeup_pre_girl'
        attribute insert 'eve_body_b_sex_wakeup_insert_girl'
        attribute slam 'eve_body_b_sex_wakeup_cum_girl'
        attribute cum 'eve_body_b_sex_wakeup_cum_girl'
        attribute pullout 'eve_body_b_sex_wakeup_insert_girl'
        attribute after 'eve_body_b_sex_wakeup_pre_girl'
        attribute cumshot 'eve_body_b_sex_wakeup_pre_girl'

    group anon:
        attribute pre 'eve_body_b_sex_wakeup_anon_pre'
        attribute after 'eve_body_b_sex_wakeup_anon_pre'
        attribute cumshot anim.TransitionAnimation(
            'eve_body_b_sex_wakeup_anon_cumshot01', .3, Dissolve(.3),
            'eve_body_b_sex_wakeup_anon_cumshot02', .3, Dissolve(.3),
            'eve_body_b_sex_wakeup_anon_cumshot03')

    group overlay:
        attribute pullout 'eve_body_b_sex_wakeup_pullout_girl'
        attribute inside 'eve_body_b_sex_wakeup_anon_after_girl'
        attribute outside 'eve_body_b_sex_wakeup_anon_cumshot_overlay'


layeredimage eve sex_wake cis anal:
    group body:
        attribute pre default 'eve_body_b_sex_wakeup_base'
        attribute insert 'eve_body_b_sex_wakeup_base'
        attribute enter 'eve_body_b_sex_wakeup_anim01_anal'
        attribute slam 'eve_body_b_sex_wakeup_cum_base'
        attribute cum 'eve_body_b_sex_wakeup_cum_base'
        attribute pullout 'eve_body_b_sex_wakeup_base'
        attribute after 'eve_body_b_sex_wakeup_base'
        attribute cumshot 'eve_body_b_sex_wakeup_base'

    attribute m_talk null

    group face if_not 'm_talk':
        attribute horny default 'eve_face_f_sex_wakeup_horny'
        attribute embarrassed 'eve_face_f_sex_wakeup_embarrassed'
        attribute surprised 'eve_face_f_sex_wakeup_embarrassed_surprised'

    group face if_all 'm_talk':
        attribute horny 'eve_face_talk_f_sex_wakeup_horny'
        attribute embarrassed 'eve_face_talk_f_sex_wakeup_embarrassed'
        attribute surprised 'eve_face_talk_f_sex_wakeup_embarrassed_surprised'

    group face:
        attribute gasp 'eve_face_f_sex_wakeup_insert'
        attribute laugh 'eve_face_f_sex_wakeup_laugh'
        attribute lipbite 'eve_face_f_sex_wakeup_lipbite'
        attribute enter null
        attribute cum null
        attribute slam null

    group genitals:
        attribute pre 'eve_body_b_sex_wakeup_pre_girl'
        attribute insert 'eve_body_b_sex_wakeup_insert_girl_anal'
        attribute slam 'eve_body_b_sex_wakeup_cum_girl_anal'
        attribute cum 'eve_body_b_sex_wakeup_cum_girl_anal'
        attribute pullout 'eve_body_b_sex_wakeup_insert_girl_anal'
        attribute after 'eve_body_b_sex_wakeup_pre_girl'
        attribute cumshot 'eve_body_b_sex_wakeup_pre_girl'

    group anon:
        attribute pre 'eve_body_b_sex_wakeup_anon_pre'
        attribute after 'eve_body_b_sex_wakeup_anon_pre'
        attribute cumshot anim.TransitionAnimation(
            'eve_body_b_sex_wakeup_anon_cumshot01', .3, Dissolve(.3),
            'eve_body_b_sex_wakeup_anon_cumshot02', .3, Dissolve(.3),
            'eve_body_b_sex_wakeup_anon_cumshot03')

    group overlay:
        attribute pullout 'eve_body_b_sex_wakeup_pullout_girl_anal'
        attribute inside 'eve_body_b_sex_wakeup_anon_after_girl_anal'
        attribute outside 'eve_body_b_sex_wakeup_anon_cumshot_overlay'

layeredimage eve sex_wake trans anal:
    group body:
        attribute pre default 'eve_body_b_sex_wakeup_base'
        attribute insert 'eve_body_b_sex_wakeup_base'
        attribute enter 'eve_body_b_sex_wakeup_anim01_alt'
        attribute slam 'eve_body_b_sex_wakeup_cum_base'
        attribute cum 'eve_body_b_sex_wakeup_cum_base'
        attribute pullout 'eve_body_b_sex_wakeup_base'
        attribute after 'eve_body_b_sex_wakeup_base'
        attribute cumshot 'eve_body_b_sex_wakeup_base'

    attribute m_talk null

    group face if_not 'm_talk':
        attribute horny default 'eve_face_f_sex_wakeup_horny'
        attribute embarrassed 'eve_face_f_sex_wakeup_embarrassed'
        attribute surprised 'eve_face_f_sex_wakeup_embarrassed_surprised'

    group face if_all 'm_talk':
        attribute horny 'eve_face_talk_f_sex_wakeup_horny'
        attribute embarrassed 'eve_face_talk_f_sex_wakeup_embarrassed'
        attribute surprised 'eve_face_talk_f_sex_wakeup_embarrassed_surprised'

    group face:
        attribute gasp 'eve_face_f_sex_wakeup_insert'
        attribute laugh 'eve_face_f_sex_wakeup_laugh'
        attribute lipbite 'eve_face_f_sex_wakeup_lipbite'
        attribute enter null
        attribute cum null
        attribute slam null

    group genitals:
        attribute pre 'eve_body_b_sex_wakeup_pre_trans'
        attribute insert 'eve_body_b_sex_wakeup_insert_trans'
        attribute slam 'eve_body_b_sex_wakeup_cum_trans'
        attribute cum 'eve_body_b_sex_wakeup_cum_trans'
        attribute pullout 'eve_body_b_sex_wakeup_insert_trans'
        attribute after 'eve_body_b_sex_wakeup_pre_trans'
        attribute cumshot 'eve_body_b_sex_wakeup_pre_trans'

    group cum:
        attribute pullout 'eve_body_b_sex_wakeup_cumshot_overlay'
        attribute after 'eve_body_b_sex_wakeup_cumshot_overlay'
        attribute cum 'eve_body_b_sex_wakeup_cum_trans_cumshot_overlay'
        attribute cumshot 'eve_body_b_sex_wakeup_cumshot_overlay'

    group anon:
        attribute pre 'eve_body_b_sex_wakeup_anon_pre'
        attribute after 'eve_body_b_sex_wakeup_anon_pre'
        attribute cumshot anim.TransitionAnimation(
            'eve_body_b_sex_wakeup_anon_cumshot01', .3, Dissolve(.3),
            'eve_body_b_sex_wakeup_anon_cumshot02', .3, Dissolve(.3),
            'eve_body_b_sex_wakeup_anon_cumshot03_trans')

    group overlay:
        attribute pullout 'eve_body_b_sex_wakeup_pullout_trans'
        attribute inside 'eve_body_b_sex_wakeup_anon_after_trans'
        attribute outside 'eve_body_b_sex_wakeup_anon_cumshot_overlay_trans'


init python hide:
    stem = 'eve_sex_wake_anim'
    count = 8
    first = 6
    frames = tuple(i % count + 1 for i in xrange(first, first + count))

    spec = (('cis',                    ('',)),
            ('cis anal',               ('_anal',)),
            ('trans anal',             ('_alt',)),
            ('trans anal cumshot',     ('_alt', '_cumshot')),
            ('trans anal cumshot cum', ('_alt', '_cum', '_cumshot')),
            ('trans anal cum',         ('_alt', '_cum')))

    for a, s in spec:
        for f in frames:
            src = tuple('eve_body_b_sex_wakeup_anim{:02}{}'.format(f, c) for c in s)
            src = Fixed(*src) if len(src) > 1 else src[0]
            renpy.image('{} {} {}'.format(stem, a, f), src)

    for a in ('cis', 'cis anal'):
        n = ' '.join((stem, a))
        ai = AnimatedImage(n, frames, M_eve)
        renpy.image(n, ai)

    renpy.image('eve_sex_wake_anim trans anal', AnimatedImage2(machine='eve')
        .loop('eve_sex_wake_anim trans anal {}', 8)
        .wait(-1)
        .wait(2).loop('eve_sex_wake_anim trans anal cumshot {}', 8, start=2)
        .wait(6).loop('eve_sex_wake_anim trans anal cumshot cum {}', 8)
        .wait(0)
        .wait(0).loop('eve_sex_wake_anim trans anal cum {}', 8))


init python hide:
    for o in ('cis', 'trans'):
        for i in xrange(1, 8):
            renpy.image('eve_sex_shower_anim_{} {}'.format(o, i),
                        'eve_sex_shower_anim_{}_{:02}'.format(o, i))

image eve_sex_shower_anim_trans = AnimatedImage(
    'eve_sex_shower_anim_trans', range(1, 8), M_eve)
image eve_sex_shower_anim_cis = AnimatedImage(
    'eve_sex_shower_anim_cis', range(1, 8), M_eve)

image eve_body_b_sex_shower_cum_alt:
    block:
        'eve_body_b_sex_shower_cum_alt02' with fastdissolve
        .4
        'eve_body_b_sex_shower_cum_alt03' with fastdissolve
        .4
        'eve_body_b_sex_shower_cum_alt04' with fastdissolve
        .4
        'eve_body_b_sex_shower_cum_alt05' with fastdissolve
        .4
        repeat 3
    'eve_body_b_sex_shower_cum_alt06' with fastdissolve

image eve_sex_shower_anim_water:
    'eve_sex_shower_water_fx_01'
    1 / 12.
    'eve_sex_shower_water_fx_02'
    1 / 12.
    'eve_sex_shower_water_fx_03'
    1 / 12.
    'eve_sex_shower_water_fx_04'
    1 / 12.
    'eve_sex_shower_water_fx_05'
    1 / 12.
    'eve_sex_shower_water_fx_06'
    1 / 12.
    'eve_sex_shower_water_fx_07'
    1 / 12.
    repeat

image xray_eve_sex_shower:
    anchor (.5, .5)
    pos (250 + 247, 250 + 292)
    rotate 335
    rotate_pad False
    xzoom -1
    zoom .64
    'xray_side'
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
