init:
    $ odette_clothing_options = ['b_vamp_normal','b_vamp_magic','b_naked_pregnant_belly','b_dressed_pregnant_belly','b_dressed_pregnant_bump','b_dressed','b_naked','b_drop1','b_drop2','b_hug_grace','b_hug_grace_both','b_wakeup','b_topless','b_hug_grace','b_panties','b_skirt','b_empty','b_skirtblank','b_pantiesblank']

init python:


    renpy.image('odette_arms_a_empty', 'ground.png')
    renpy.image('odette_body_b_empty', 'ground.png')
    renpy.image('odette_face_f_empty', 'ground.png')    
    renpy.image('odette_face_talk_f_empty', 'ground.png')


    renpy.image('odette_face_talk_f_laugh', 'odette_face_f_laugh')
    renpy.image('odette_face_bite_talk_f_laugh', 'odette_face_bite_f_laugh')
    renpy.image('odette_face_talk_f_yawn', 'odette_face_f_yawn')
    renpy.image('odette_face_talk_f_moo', 'odette_face_f_moo')
    renpy.image('odette_face_talk_f_kiss', 'odette_face_f_kiss')
    renpy.image('odette_vamp_front_face_talk_f_tongue', 'odette_vamp_front_face_f_tongue')
    renpy.image('odette_face_talk_f_drink', 'odette_face_vamp_f_drink')


    renpy.image('odette_face_f_drink', 'odette_face_vamp_f_drink')
    renpy.image('odette_face_f_exasperated', 'odette_face_talk_f_exasperated')
    renpy.image('odette_face_f_wink', 'odette_face_talk_f_wink')
    renpy.image('odette_face_f_disgusted', 'odette_face_talk_f_disgusted')
    renpy.image('odette_face_f_disgusted', 'odette_face_talk_f_disgusted')
    renpy.image('odette_face_vamp_f_teeth_look', 'odette_face_vamp_talk_f_teeth_look')


    renpy.image('odette_arms_vamp_a_touch', 'odette_arms_vamp_a_blood_cup')

layeredimage odette:

    yanchor config.screen_height
    ypos 1.
    xanchor config.screen_width
    xpos 1.


    group body auto:
        attribute b_dressed default "odette_body_b_dressed[M_odette.pregnancy.to_string]"
        attribute b_empty null
        attribute b_kiss_eve "odette_body_b_kiss_eve"
        attribute b_kiss_grace "odette_body_b_kiss_grace"
        attribute b_kiss_anon "odette_body_b_kiss_anon"
        attribute b_massage_cum "odette_body_b_massage_cum"
        attribute b_bike_cum "odette_body_b_bike_cum"
        attribute b_vamp_front "location_crypt_front"
        attribute b_vamp_front_normal "location_crypt_front"
        attribute b_vamp_normal "odette_body_b_vamp"
        attribute b_vamp_sitting_cape_normal "odette_body_b_vamp_sitting_cape"
        attribute b_vamp_sitting_normal "odette_body_b_vamp_sitting"
        attribute b_vamp_bite "location_crypt_bite01"
        attribute b_vamp_magic "odette_body_b_vamp[M_odette.pregnancy.to_string]"
        attribute b_naked_vamp "odette_body_b_naked"
        attribute b_naked_vamp_pull_anon "odette_body_b_naked_pull_anon"


    group mouth prefix 'm':
        attribute talk null

    group face:
        attribute f_normal default null







    group face if_not 'm_talk' if_any odette_clothing_options auto


    group face if_not 'm_talk' if_any 'b_naked_pull_anon' auto variant 'vamp':
        offset (-110, 0)


    group face if_not 'm_talk' if_any 'b_naked_vamp' auto variant 'vamp'
    group face if_not 'm_talk' if_any 'b_naked_vamp_pull_anon' auto variant 'vamp':
        offset (-110, 0)


    group face if_not 'm_talk' if_any 'b_vamp' auto variant 'vamp'


    group face if_not 'm_talk' if_any 'b_vamp_front' auto variant 'vamp_front':
        attribute f_normal 'odette_face_vamp_front_f_vamp_normal'


    group face if_not 'm_talk' if_any 'b_vamp_front_normal' auto variant 'vamp_front'  


    group face if_not 'm_talk' if_any ['b_vamp_sitting_normal','b_vamp_sitting_cape_normal'] auto:
        offset (14, 76)


    group face if_not 'm_talk' if_any ['b_vamp_sitting','b_vamp_sitting_cape'] auto variant 'vamp':
        offset (14, 76)


    group face if_not 'm_talk' if_any ['b_vamp_sitting_up'] auto variant 'vamp':
        offset (-203, 15)


    group face if_not 'm_talk' if_any 'b_dressed_kiss_peck' auto:
        xzoom -1
        offset (356, 0)


    group face if_not 'm_talk' if_all 'b_massage' auto:
        offset (12, -138)


    group face if_not 'm_talk' if_all 'b_massage_leaning' auto:
        offset (-118, -90)


    group face if_not 'm_talk' if_all 'b_gown_bed' auto:
        offset (121, 46)


    group face if_not 'm_talk' if_all 'b_situp' auto:
        xzoom -1
        offset (-23, -54)


    group face if_not 'm_talk' if_all 'b_ontop' auto:
        xzoom -1
        offset (109, -114)


    group face if_not 'm_talk' if_all 'b_dressed_pull_anon' auto:
        xoffset -375






    group face if_not 'm_talk' if_all 'b_bike_base' auto variant 'bike_base'


    group face if_not 'm_talk' if_any ['b_sex_vamp_base','b_sex_vamp_insert'] auto variant 'sex_vamp'


    group face if_not 'm_talk' if_any ['b_vamp_bite'] auto variant 'bite':
        attribute f_bite null







    group face if_all 'm_talk' if_any odette_clothing_options auto variant 'talk'


    group face if_all 'm_talk' if_any 'b_naked_pull_anon' auto variant 'vamp_talk':
        offset (-110, 0)


    group face if_all 'm_talk' if_any 'b_vamp_front' auto variant 'vamp_front_talk':
        attribute f_normal 'odette_face_vamp_front_talk_f_vamp_normal'


    group face if_all 'm_talk' if_any 'b_vamp_front_normal' auto variant 'vamp_front_talk'   


    group face if_all 'm_talk' if_any 'b_naked_vamp' auto variant 'vamp_talk'
    group face if_all 'm_talk' if_any 'b_naked_vamp_pull_anon' auto variant 'vamp_talk':
        offset (-110, 0)


    group face if_all 'm_talk' if_any 'b_vamp' auto variant 'vamp_talk'


    group face if_all 'm_talk' if_any ['b_vamp_sitting','b_vamp_sitting_cape'] auto variant 'vamp_talk':
        offset (14, 76)


    group face if_all 'm_talk' if_any ['b_vamp_sitting_normal','b_vamp_sitting_cape_normal'] auto variant 'talk':
        offset (14, 76)


    group face if_all 'm_talk' if_any ['b_vamp_sitting_up'] auto variant 'vamp_talk':
        offset (-203, 15)


    group face if_all 'm_talk' if_any 'b_dressed_kiss_peck' auto variant 'talk':
        xzoom -1
        offset (356, 0)


    group face if_all ['m_talk','b_massage'] auto variant 'talk':
        offset (12, -138)


    group face if_all ['m_talk','b_massage_leaning'] auto variant 'talk':
        offset (-118, -90)


    group face if_all ['m_talk','b_gown_bed'] auto variant 'talk':
        offset (121, 46)


    group face if_all ['m_talk','b_situp'] auto variant 'talk':
        xzoom -1
        offset (-23, -54)


    group face if_all ['m_talk','b_ontop'] auto variant 'talk':
        xzoom -1
        offset (109, -114)


    group face if_all 'm_talk' if_any 'b_dressed_pull_anon' auto variant 'talk':
        xoffset -375






    group face if_all ['m_talk','b_massage_laying_back'] auto variant 'massage_laying_back_talk'


    group face if_all ['m_talk','b_bike_base'] auto variant 'bike_base_talk'


    group face if_all 'm_talk' if_any ['b_sex_vamp_base','b_sex_vamp_insert'] auto variant 'sex_vamp_talk'


    group face if_all 'm_talk' if_any ['b_vamp_bite'] auto variant 'bite_talk'



    group arms if_any ['b_dressed','b_wakeup','b_dressed_pregnant_bump','b_dressed_pregnant_belly'] auto variant 'dressed':
        attribute a_idle default 'odette_arms_magic_a_idle[M_odette.pregnancy.to_string]'
        attribute a_baby "odette_arms_dressed_a_baby_[M_odette.pregnancy.baby_gender]"


    group arms if_any ['b_vamp_magic'] auto variant 'vamp':
        attribute a_idle default 'odette_arms_vamp_a_touch[M_odette.pregnancy.to_string]'


    group arms if_any ['b_vamp','b_vamp_normal'] auto variant 'vamp':
        attribute a_idle default 'odette_arms_vamp_a_blood_cup'


    group arms if_any ['b_vamp_sitting_cape','b_vamp_sitting_cape_normal'] auto variant 'vamp_sitting_cape':
        attribute a_idle default 'odette_arms_vamp_sitting_cape_a_wine'


    group arms if_any ['b_vamp_sitting','b_vamp_sitting_normal'] auto variant 'vamp_sitting':
        attribute a_idle default 'odette_arms_vamp_sitting_a_sides'


    group arms if_any ['b_naked','b_naked_vamp','b_topless','b_panties','b_skirt'] auto variant 'naked':
        attribute a_idle default 'odette_arms_naked_a_hips'

    group arms if_any ['b_panties'] auto variant 'panties'
    group arms if_any ['b_topless'] auto variant 'topless'


    group arms if_any ['b_naked_pregnant_belly'] auto variant 'naked_pregnant_belly':
        attribute a_idle default 'odette_arms_naked_pregnant_belly_a_touch'
        attribute a_squeeze 'odette_arms_naked_pregnant_belly_a_squeeze'


    group arms if_all 'b_bike_base' auto variant 'bike_base':
        attribute a_idle default 'odette_arms_bike_base_a_down'


    group arms if_all 'b_situp' auto variant 'situp':
        attribute a_idle default 'odette_arms_situp_a_down'


    group arms if_any ['b_skirtblank','b_pantiesblank'] auto variant 'skirtblank':
        attribute a_idle default 'odette_arms_skirtblank_a_boobs'


    group arms if_all 'b_massage' auto variant 'massage':
        attribute a_idle default 'odette_arms_massage_a_hips'
        attribute a_empty null


    group arms if_all 'b_gown_bed' auto variant 'gown_bed':
        attribute a_idle default "odette_arms_gown_bed_a_baby_[M_odette.pregnancy.baby_gender]"


    group overlay if_not 'b_sex_vamp_base' auto:
        attribute o_empty default null

    group overlay if_all 'b_sex_vamp_base' auto variant 'sex_vamp_base':
        attribute o_empty default null
        attribute o_cumshot 'odette_overlay_sex_vamp_base_o_cumshot'

    group dick if_all 'b_sex_vamp_insert' auto variant 'sex_vamp_insert':
        attribute d_insert default

    group overlay if_all 'b_sex_vamp_insert' auto variant 'sex_vamp_insert':
        attribute o_empty default null

image odette_f = "characters/odette/odette_face_f_normal.png"

image odette_arms_magic_a_idle = "odette_arms_dressed_a_hips"
image odette_arms_magic_a_idle_pregnant_bump = "odette_arms_naked_pregnant_bump_a_hips"
image odette_arms_magic_a_idle_pregnant_belly = "odette_arms_naked_pregnant_belly_a_touch"

image odette_arms_naked_pregnant_belly_a_squeeze:
    Transform("odette_arms_naked_pregnant_belly_a_squeeze1")
    pause .4
    Transform("odette_arms_naked_pregnant_belly_a_squeeze2")
    pause .4
    repeat

image odette_arms_skirtblank_a_boobs:
    Transform("odette_arms_skirtblank_a_boobs1")
    pause .4
    Transform("odette_arms_skirtblank_a_boobs2")
    pause .4
    repeat

image odette_body_b_kiss_anon:
    Transform("odette_body_b_kiss_anon1")
    pause .6
    Transform("odette_body_b_kiss_anon2")
    pause .8
    repeat

image odette_body_b_kiss_eve:
    Transform("odette_body_b_kiss1")
    pause .6
    Transform("odette_body_b_kiss2")
    pause .8
    repeat

image odette_body_b_kiss_grace:
    Transform("odette_body_b_kiss3")
    pause .6
    Transform("odette_body_b_kiss4")
    pause .8
    repeat

image odette_arms_massage_leaning_a_rub1_2:
    Transform("odette_arms_massage_leaning_a_rub1")
    pause .4
    Transform("odette_arms_massage_leaning_a_rub2")
    pause .4
    repeat

image odette_arms_massage_leaning_a_rub3_4:
    Transform("odette_arms_massage_leaning_a_rub3")
    pause .4
    Transform("odette_arms_massage_leaning_a_rub4")
    pause .4
    repeat



image odette_sex_bike_base_mc = "odette_sex_body_b_bike_base_mc"

image odette_sex_bike 1 = "odette_sex_bike_anim01"
image odette_sex_bike 2 = "odette_sex_bike_anim02"
image odette_sex_bike 3 = "odette_sex_bike_anim03"
image odette_sex_bike 4 = "odette_sex_bike_anim04"
image odette_sex_bike 5 = "odette_sex_bike_anim05"
image odette_sex_bike 6 = "odette_sex_bike_anim06"
image odette_sex_bike 7 = "odette_sex_bike_anim07"
image odette_sex_bike 8 = "odette_sex_bike_anim08"
image odette_sex_bike 9 = "odette_sex_bike_anim09"
image odette_sex_bike 10 = "odette_sex_bike_anim10"

image odette_body_b_bike_cum:
    Transform("odette_body_b_bike_cum1")
    pause .4
    Transform("odette_body_b_bike_cum2")
    pause .4
    repeat

image odette_creampie = "odette_arms_bike_base_mc_a_pullout"

image odette_sex_arms_bike_base_mc a_pre = "odette_arms_bike_base_mc_a_pre"
image odette_sex_arms_bike_base_mc a_insert = "odette_arms_bike_base_mc_a_insert"
image odette_sex_arms_bike_base_mc a_after = "odette_arms_bike_base_mc_a_after"

image odette_sex_arms_bike_base_mc a_cumshot:
    Transform("odette_arms_bike_base_mc_a_cumshot1")
    pause .4
    Transform("odette_arms_bike_base_mc_a_cumshot2")
    pause .4
    Transform("odette_arms_bike_base_mc_a_cumshot3")

image odette_sex_arms_bike_base_mc a_cumshot3 = "odette_arms_bike_base_mc_a_cumshot3"

image odette_sex_massage 1 = "odette_sex_anim01"
image odette_sex_massage 2 = "odette_sex_anim02"
image odette_sex_massage 3 = "odette_sex_anim03"
image odette_sex_massage 4 = "odette_sex_anim04"
image odette_sex_massage 5 = "odette_sex_anim05"
image odette_sex_massage 6 = "odette_sex_anim06"
image odette_sex_massage 7 = "odette_sex_anim07"
image odette_sex_massage 8 = "odette_sex_anim08"
image odette_sex_massage 9 = "odette_sex_anim09"
image odette_sex_massage 10 = "odette_sex_anim10"
image odette_sex_massage 11 = "odette_sex_anim11"
image odette_sex_massage 12 = "odette_sex_anim12"
image odette_sex_massage 13 = "odette_sex_anim13"
image odette_sex_massage 14 = "odette_sex_anim14"
image odette_sex_massage 15 = "odette_sex_anim15"
image odette_sex_massage 16 = "odette_sex_anim16"
image odette_sex_massage 17 = "odette_sex_anim17"
image odette_sex_massage 18 = "odette_sex_anim18"

image odette_body_b_massage_cum:
    Transform("odette_body_b_massage_cum1")
    pause .4
    Transform("odette_body_b_massage_cum2")
    pause .4
    repeat


image odette_sex_mc_overlay o_dick_soft = "odette_overlay_o_ontop_dick_soft"
image odette_sex_mc_overlay o_dick_hard = "odette_overlay_o_ontop_dick_hard"

image odette_sex_mc_overlay o_massage_pullout_cum:
    Transform("odette_overlay_o_massage_pullout_cum1")
    pause .4
    Transform("odette_overlay_o_massage_pullout_cum2")
    pause .4
    Transform("odette_overlay_o_massage_pullout_cum3")


init python:
    for i in xrange(1, 9):
        renpy.image('odette_body_b_sex_vamp_anim {}'.format(i),
                    'odette_body_b_sex_vamp_anim{:02}'.format(i))

image odette_body_b_sex_vamp_anim = AnimatedImage('odette_body_b_sex_vamp_anim',
                                           (1,2,3,4,5,6,7,8),
                                           M_odette)

image odette_overlay_sex_vamp_base_o_cumshot:
    Transform("odette_overlay_sex_vamp_base_o_cumshot01")
    pause .4
    Transform("odette_overlay_sex_vamp_base_o_cumshot02")
    pause .4
    Transform("odette_overlay_sex_vamp_base_o_cumshot03")



init python hide:
    count = 11
    first = 1
    frames = tuple(i % count + 1 for i in xrange(first, first + count))

    map = (('odette_sex_bj_anim',       'odette_blowjob'),
           ('odette_sex_bj_naked_anim', 'odette_blowjob_naked'))

    for src, stem in map:
        for i in frames:
            renpy.image('{} {}'.format(stem, i),
                        '{}{:02}'.format(src, i))
        
        renpy.image(stem, AnimatedImage(stem, frames, M_odette))



init python hide:
    count = 12
    first = 7
    frames = tuple(i % count + 1 for i in xrange(first, first + count))

    stem = 'odette_paizuri'
    for i in frames:
        renpy.image('{} {}'.format(stem, i),
                    'odette_sex_boobjob_anim{:02}'.format(i))

    renpy.image(stem, AnimatedImage(stem, frames, M_odette))


image odette_sex_boobjob_cumshot:
    .4
    'odette_sex_boobjob_cumshot01' with fastdissolve
    .4
    'odette_sex_boobjob_cumshot02' with fastdissolve
    .4
    'odette_sex_boobjob_cumshot03' with fastdissolve






image xray_odette_vamp_sex:
    Transform("characters/xray/xray_left_back_01.png", xzoom=-0.5, yzoom=0.5, xoffset=350, yoffset=350)
    pause 0.4
    Transform("characters/xray/xray_left_back_02.png", xzoom=-0.5, yzoom=0.5, xoffset=350, yoffset=350)
    pause 0.4
    Transform("characters/xray/xray_left_back_03.png", xzoom=-0.5, yzoom=0.5, xoffset=350, yoffset=350)
    pause 0.4
    Transform("characters/xray/xray_left_back_04.png", xzoom=-0.5, yzoom=0.5, xoffset=350, yoffset=350)
    pause 0.4
    Transform("characters/xray/xray_left_back_05.png", xzoom=-0.5, yzoom=0.5, xoffset=350, yoffset=350)
    pause 0.4
    Transform("characters/xray/xray_left_back_06.png", xzoom=-0.5, yzoom=0.5, xoffset=350, yoffset=350)
    pause 0.4
    Transform("characters/xray/xray_left_back_07.png", xzoom=-0.5, yzoom=0.5, xoffset=350, yoffset=350)
    pause 0.4
    Transform("characters/xray/xray_left_back_08.png", xzoom=-0.5, yzoom=0.5, xoffset=350, yoffset=350)
    pause 0.4
    Transform("characters/xray/xray_left_back_09.png", xzoom=-0.5, yzoom=0.5, xoffset=350, yoffset=350)
    pause 0.4
    Transform("characters/xray/xray_left_back_10.png", xzoom=-0.5, yzoom=0.5, xoffset=350, yoffset=350)
    pause 0.4
    Transform("characters/xray/xray_left_back_11.png", xzoom=-0.5, yzoom=0.5, xoffset=350, yoffset=350)
    pause 0.4
    Transform("characters/xray/xray_left_back_12.png", xzoom=-0.5, yzoom=0.5, xoffset=350, yoffset=350)
    pause 0.4
    Transform("characters/xray/xray_left_back_13.png", xzoom=-0.5, yzoom=0.5, xoffset=350, yoffset=350)
    pause 0.4
    Transform("characters/xray/xray_left_back_14.png", xzoom=-0.5, yzoom=0.5, xoffset=350, yoffset=350)
    pause 0.4
    Transform("characters/xray/xray_left_back_15.png", xzoom=-0.5, yzoom=0.5, xoffset=350, yoffset=350)
    pause 0.4
    Transform("characters/xray/xray_left_back_16.png", xzoom=-0.5, yzoom=0.5, xoffset=350, yoffset=350)
    pause 0.4
    Transform("characters/xray/xray_left_back_17.png", xzoom=-0.5, yzoom=0.5, xoffset=350, yoffset=350)
    pause 0.4
    Transform("characters/xray/xray_left_back_18.png", xzoom=-0.5, yzoom=0.5, xoffset=350, yoffset=350)
    pause 2.0
    linear 2.5 alpha 0

image xray_odette_massage:
    Transform("characters/xray/xray_side_01.png", xzoom=-0.6, yzoom=0.6, rotate=-120, xoffset=220, yoffset=80)
    pause 0.4
    Transform("characters/xray/xray_side_02.png", xzoom=-0.6, yzoom=0.6, rotate=-120, xoffset=220, yoffset=80)
    pause 0.4
    Transform("characters/xray/xray_side_03.png", xzoom=-0.6, yzoom=0.6, rotate=-120, xoffset=220, yoffset=80)
    pause 0.4
    Transform("characters/xray/xray_side_04.png", xzoom=-0.6, yzoom=0.6, rotate=-120, xoffset=220, yoffset=80)
    pause 0.4
    Transform("characters/xray/xray_side_05.png", xzoom=-0.6, yzoom=0.6, rotate=-120, xoffset=220, yoffset=80)
    pause 0.4
    Transform("characters/xray/xray_side_06.png", xzoom=-0.6, yzoom=0.6, rotate=-120, xoffset=220, yoffset=80)
    pause 0.4
    Transform("characters/xray/xray_side_07.png", xzoom=-0.6, yzoom=0.6, rotate=-120, xoffset=220, yoffset=80)
    pause 0.4
    Transform("characters/xray/xray_side_08.png", xzoom=-0.6, yzoom=0.6, rotate=-120, xoffset=220, yoffset=80)
    pause 0.4
    Transform("characters/xray/xray_side_09.png", xzoom=-0.6, yzoom=0.6, rotate=-120, xoffset=220, yoffset=80)
    pause 0.4
    Transform("characters/xray/xray_side_10.png", xzoom=-0.6, yzoom=0.6, rotate=-120, xoffset=220, yoffset=80)
    pause 0.4
    Transform("characters/xray/xray_side_11.png", xzoom=-0.6, yzoom=0.6, rotate=-120, xoffset=220, yoffset=80)
    pause 0.4
    Transform("characters/xray/xray_side_12.png", xzoom=-0.6, yzoom=0.6, rotate=-120, xoffset=220, yoffset=80)
    pause 0.4
    Transform("characters/xray/xray_side_13.png", xzoom=-0.6, yzoom=0.6, rotate=-120, xoffset=220, yoffset=80)
    pause 0.4
    Transform("characters/xray/xray_side_14.png", xzoom=-0.6, yzoom=0.6, rotate=-120, xoffset=220, yoffset=80)
    pause 0.4
    Transform("characters/xray/xray_side_15.png", xzoom=-0.6, yzoom=0.6, rotate=-120, xoffset=220, yoffset=80)
    pause 0.4
    Transform("characters/xray/xray_side_16.png", xzoom=-0.6, yzoom=0.6, rotate=-120, xoffset=220, yoffset=80)
    pause 0.4
    Transform("characters/xray/xray_side_17.png", xzoom=-0.6, yzoom=0.6, rotate=-120, xoffset=220, yoffset=80)
    pause 0.4
    Transform("characters/xray/xray_side_18.png", xzoom=-0.6, yzoom=0.6, rotate=-120, xoffset=220, yoffset=80)
    pause 2.0
    linear 2.5 alpha 0

image xray_odette_bike:
    Transform("characters/xray/xray_left_back_01.png", xzoom=-0.6, yzoom=0.6, xoffset=325, yoffset=275)
    pause 0.4
    Transform("characters/xray/xray_left_back_02.png", xzoom=-0.6, yzoom=0.6, xoffset=325, yoffset=275)
    pause 0.4
    Transform("characters/xray/xray_left_back_03.png", xzoom=-0.6, yzoom=0.6, xoffset=325, yoffset=275)
    pause 0.4
    Transform("characters/xray/xray_left_back_04.png", xzoom=-0.6, yzoom=0.6, xoffset=325, yoffset=275)
    pause 0.4
    Transform("characters/xray/xray_left_back_05.png", xzoom=-0.6, yzoom=0.6, xoffset=325, yoffset=275)
    pause 0.4
    Transform("characters/xray/xray_left_back_06.png", xzoom=-0.6, yzoom=0.6, xoffset=325, yoffset=275)
    pause 0.4
    Transform("characters/xray/xray_left_back_07.png", xzoom=-0.6, yzoom=0.6, xoffset=325, yoffset=275)
    pause 0.4
    Transform("characters/xray/xray_left_back_08.png", xzoom=-0.6, yzoom=0.6, xoffset=325, yoffset=275)
    pause 0.4
    Transform("characters/xray/xray_left_back_09.png", xzoom=-0.6, yzoom=0.6, xoffset=325, yoffset=275)
    pause 0.4
    Transform("characters/xray/xray_left_back_10.png", xzoom=-0.6, yzoom=0.6, xoffset=325, yoffset=275)
    pause 0.4
    Transform("characters/xray/xray_left_back_11.png", xzoom=-0.6, yzoom=0.6, xoffset=325, yoffset=275)
    pause 0.4
    Transform("characters/xray/xray_left_back_12.png", xzoom=-0.6, yzoom=0.6, xoffset=325, yoffset=275)
    pause 0.4
    Transform("characters/xray/xray_left_back_13.png", xzoom=-0.6, yzoom=0.6, xoffset=325, yoffset=275)
    pause 0.4
    Transform("characters/xray/xray_left_back_14.png", xzoom=-0.6, yzoom=0.6, xoffset=325, yoffset=275)
    pause 0.4
    Transform("characters/xray/xray_left_back_15.png", xzoom=-0.6, yzoom=0.6, xoffset=325, yoffset=275)
    pause 0.4
    Transform("characters/xray/xray_left_back_16.png", xzoom=-0.6, yzoom=0.6, xoffset=325, yoffset=275)
    pause 0.4
    Transform("characters/xray/xray_left_back_17.png", xzoom=-0.6, yzoom=0.6, xoffset=325, yoffset=275)
    pause 0.4
    Transform("characters/xray/xray_left_back_18.png", xzoom=-0.6, yzoom=0.6, xoffset=325, yoffset=275)
    pause 2.0
    linear 2.5 alpha 0



init python hide:
    count = 6
    first = 1
    frames = tuple(i % count + 1 for i in xrange(first, first + count))

    map = (('odette_sex_couch_anal_anim', 'odette_sex_couch_anal'),)

    for src, stem in map:
        for i in frames:
            renpy.image('{} {}'.format(stem, i),
                        '{}{:02}'.format(src, i))
        
        renpy.image(stem, AnimatedImage(stem, frames, M_odette))

layeredimage odette sex_couch_anal:
    attribute m_talk null

    group face if_not 'm_talk' auto:
        attribute f_normal default

    group face if_all 'm_talk' auto variant 'talk'



init python hide:
    count = 9
    first = 1
    frames = tuple(i % count + 1 for i in xrange(first, first + count))

    map = (('odette_sex_couch_back_anim', 'odette_sex_couch_back'),)

    for src, stem in map:
        for i in frames:
            renpy.image('{} {}'.format(stem, i),
                        '{}{:02}'.format(src, i))
        
        renpy.image(stem, AnimatedImage(stem, frames, M_odette))

image odette_sex_couch_back_cumshot:
    'odette_sex_couch_back_cumshot1'
    .4
    'odette_sex_couch_back_cumshot2' with fastdissolve
    .4
    'odette_sex_couch_back_cumshot3' with fastdissolve
    .4
    'odette_sex_couch_back_cumshot4' with fastdissolve

layeredimage odette sex_couch_back:
    attribute m_talk null

    group face if_not 'm_talk' auto:
        attribute f_normal default

    group face if_all 'm_talk' auto variant 'talk'


init python hide:
    count = 10
    first = 1
    frames = tuple(i % count + 1 for i in xrange(first, first + count))

    map = (('odette_body_b_sex_vamp_missionary_anim', 'odette_crypt_cowgirl'),)

    for src, stem in map:
        for i in frames:
            renpy.image('{} {}'.format(stem, i),
                        '{}{:02}'.format(src, i))
        
        renpy.image(stem, AnimatedImage(stem, frames, M_odette))


image odette_crypt_cowgirl_cum:
    'ground.png'
    'odette_body_b_sex_vamp_missionary_cum_drip01' with Dissolve(3)
    3
    'odette_body_b_sex_vamp_missionary_cum_drip02' with Dissolve(3)
    3
    'odette_body_b_sex_vamp_missionary_cum_drip03' with Dissolve(3)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
