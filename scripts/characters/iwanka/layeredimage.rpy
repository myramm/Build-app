init:
    $ iwanka_clothing_options = ['b_dressed','b_naked_stretch','b_swimsuit','b_dressed_magic','b_club','b_maid','b_maid_scarfless','b_naked','b_magic','b_swimsuit_undress2']

init python:


    renpy.image('iwanka_arms_a_empty', 'ground.png')
    renpy.image('iwanka_body_b_empty', 'ground.png')
    renpy.image('iwanka_face_f_empty', 'ground.png')
    renpy.image('iwanka_face_talk_f_empty', 'ground.png')
    renpy.image('iwanka_face_bj_f_normal', 'ground.png')


    renpy.image('iwanka_face_talk_f_laugh', 'iwanka_face_f_laugh')
    renpy.image('iwanka_face_talk_f_yawn', 'iwanka_face_f_yawn')
    renpy.image('iwanka_face_bj_talk_f_cum', 'iwanka_face_bj_f_cum')
    renpy.image('iwanka_face_bj_talk_f_laugh', 'iwanka_face_bj_f_laugh')



layeredimage iwanka:

    yanchor config.screen_height
    ypos 1.
    xanchor config.screen_width
    xpos 1.


    group body auto:
        attribute b_dressed default
        attribute b_empty null
        attribute b_magic "iwanka_body_b_[M_iwanka.outfit.get][M_iwanka.pregnancy.to_string]"   

        attribute b_dressed_magic "iwanka_body_b_dressed[M_iwanka.pregnancy.to_string]"   

        attribute b_swim_kiss 'iwanka_body_b_swim_kiss'
        attribute b_maid_kiss 'iwanka_body_b_maid_kiss'
        attribute b_naked_kiss 'iwanka_body_b_naked_kiss'
        attribute b_dressed_kiss 'iwanka_body_b_dressed_kiss'
        attribute b_club_dance 'iwanka_body_b_club_dance'
        attribute b_club_dance_back 'iwanka_body_b_club_dance_back'
        attribute b_undress 'location_boat_evening_undress'
        attribute b_presex_yacht 'location_boat_interior_evening_bed_presex'
        attribute b_presex_iwanka_room 'location_rump_iwanka_day_bed_presex'


    group mouth prefix 'm':
        attribute talk null

    group face:
        attribute f_normal default null







    group face if_not 'm_talk' if_any iwanka_clothing_options auto


    group face if_not 'm_talk' if_any ['b_swim'] auto:
        offset (25, 166)


    group face if_not 'm_talk' if_any ['b_knees_back','b_knees_back_pull'] auto:
        offset (-67, -64)


    group face if_not 'm_talk' if_any ['b_club_pulling_mc'] auto:
        offset (-240, 0)


    group face if_not 'm_talk' if_any 'b_knees' auto:
        offset (-242, 0)


    group face if_not 'm_talk' if_any 'b_jacuzzi' auto:
        offset (0, 110)


    group face if_not 'm_talk' if_any 'b_gown_bed' auto:
        offset (94, 58)


    group face if_not 'm_talk' if_any ['b_club_dance4','b_naked_dance4'] auto:
        offset (-52, 27)


    group face if_not 'm_talk' if_any ['b_club_dance5','b_naked_dance5'] auto:
        offset (-70, 16)


    group face if_not 'm_talk' if_any ['b_club_dance6','b_naked_dance6'] auto:
        offset (-85, 38)


    group face if_not 'm_talk' if_any ['b_sidebed_left_shy','b_sidebed_left'] auto:
        offset (-286, -15)


    group face if_not 'm_talk' if_any ['b_sidebed_right_shy','b_sidebed_right'] auto:
        xzoom -1
        offset (316, -15)


    group face if_not 'm_talk' if_any ['b_onbed_cuddle_naked'] auto:
        rotate 25
        xzoom -1
        offset (295, -80)


    group face if_not 'm_talk' if_any ['b_chair_naked','b_chair_swimsuit'] auto:
        xzoom -1
        offset (-41, 118)






    group face if_not 'm_talk' if_any ['b_bj_naked', 'b_bj'] auto variant 'bj'


    group face if_not 'm_talk' if_any ['b_sex_pre_after', 'b_sex_insert_pullout'] auto variant 'sex'







    group face if_all 'm_talk' if_any iwanka_clothing_options auto variant 'talk'


    group face if_all 'm_talk' if_any ['b_swim'] auto variant 'talk':
        offset (25, 166)


    group face if_all 'm_talk' if_any ['b_knees_back','b_knees_back_pull'] auto variant 'talk':
        offset (-67, -64)


    group face if_all 'm_talk' if_any ['b_club_pulling_mc'] auto variant 'talk':
        offset (-240, 0)


    group face if_all 'm_talk' if_any 'b_knees' auto variant 'talk':
        offset (-242, 0)


    group face if_all 'm_talk' if_any 'b_jacuzzi' auto variant 'talk':
        offset (0, 110)


    group face if_all ['m_talk', 'b_gown_bed'] auto variant 'talk':
        offset (94, 58)


    group face if_all 'm_talk' if_any ['b_club_dance4','b_naked_dance4'] auto variant 'talk':
        offset (-52, 27)


    group face if_all 'm_talk' if_any ['b_club_dance5','b_naked_dance5'] auto variant 'talk':
        offset (-70, 16)


    group face if_all 'm_talk' if_any ['b_club_dance6','b_naked_dance6'] auto variant 'talk':
        offset (-85, 38)


    group face if_all 'm_talk' if_any ['b_sidebed_left_shy','b_sidebed_left'] auto variant 'talk':
        offset (-286, -15)


    group face if_all 'm_talk' if_any ['b_sidebed_right_shy','b_sidebed_right'] auto variant 'talk':
        xzoom -1
        offset (316, -15)


    group face if_all 'm_talk' if_any ['b_onbed_cuddle_naked'] auto variant 'talk':
        rotate 25
        xzoom -1
        offset (295, -80)


    group face if_all 'm_talk' if_any ['b_chair_naked','b_chair_swimsuit'] auto variant 'talk':
        xzoom -1
        offset (-41, 118)






    group face if_all 'm_talk' if_any ['b_bj_naked', 'b_bj'] auto variant 'bj_talk'


    group face if_all 'm_talk' if_any ['b_sex_pre_after', 'b_sex_insert_pullout'] auto variant 'sex_talk'


    group face if_all 'm_talk' if_any ['b_undress'] auto variant 'undress_talk'


    group face if_all 'm_talk' if_any ['b_presex_yacht','b_presex_iwanka_room'] auto variant 'presex_talk'



    group arms if_all 'b_dressed' auto variant 'dressed':
        attribute a_idle default 'iwanka_arms_dressed_a_front'
        attribute a_baby 'iwanka_arms_dressed_a_baby_[M_iwanka.pregnancy.baby_gender]'
        attribute a_melonia_baby 'iwanka_arms_dressed_a_melonia_baby_[M_melonia.pregnancy.baby_gender]'


    group arms if_all 'b_onbed_cuddle_naked' auto variant 'onbed_cuddle_naked':
        attribute a_idle default 'iwanka_arms_onbed_cuddle_naked_a_chest'


    group arms if_all 'b_swim' auto variant 'swim':
        attribute a_idle default 'iwanka_arms_swim_a_float'


    group arms if_any ['b_maid','b_maid_scarfless'] auto variant 'maid':
        attribute a_idle default 'iwanka_arms_maid_a_sides'


    group arms if_all 'b_club' auto variant 'club':
        attribute a_idle default 'iwanka_arms_club_a_hip'


    group arms if_all 'b_knees' auto variant 'knees':
        attribute a_idle default 'iwanka_arms_knees_a_down'


    group arms if_all 'b_knees_back' auto variant 'knees_back':
        attribute a_idle default 'iwanka_arms_knees_back_a_front'


    group arms if_all 'b_gown_bed' auto variant 'gown_bed':
        attribute a_idle default "iwanka_arms_gown_bed_a_baby_[M_iwanka.pregnancy.baby_gender]"



    group arms if_all 'b_magic' auto:
        attribute a_idle default 'iwanka_arms_[M_iwanka.outfit.get]_a_touch[M_iwanka.pregnancy.to_string]'
        attribute a_undress 'iwanka_arms_swimsuit_a_undress'


    group arms if_all 'b_dressed_magic' auto variant 'dressed':
        attribute a_idle default 'iwanka_arms_dressed_a_touch[M_iwanka.pregnancy.to_string]'


    group arms if_all 'b_jacuzzi' auto variant 'jacuzzi':
        attribute a_idle default 'iwanka_arms_jacuzzi_a_sides'


    group arms if_any ['b_swimsuit'] auto variant 'swimsuit':
        attribute a_idle default 'iwanka_arms_swimsuit_a_front'


    group arms if_any ['b_naked'] auto variant 'naked':
        attribute a_idle default 'iwanka_arms_naked_a_front'


    group arms if_any ['b_club_back'] auto variant 'club_back':
        attribute a_idle default 'iwanka_arms_club_back_a_fishtank'


    group arms if_any ['b_bj_naked','b_bj'] auto variant 'bj':
        attribute a_idle default 'iwanka_arms_bj_a_pre'
        attribute a_cum 'iwanka_arms_bj_a_cum'


    group arms if_any ['b_sidebed_right','b_sidebed_left'] auto variant 'sidebed':
        attribute a_idle default 'iwanka_arms_sidebed_a_down'


    group arms if_any ['b_sidebed_right_shy','b_sidebed_left_shy'] auto variant 'sidebed_shy':
        attribute a_idle default 'iwanka_arms_sidebed_shy_a_down'
        attribute a_rub 'iwanka_arms_sidebed_shy_a_rub'
        attribute a_touch 'iwanka_arms_sidebed_shy_a_touch'


    group arms if_any ['b_naked_bend'] auto variant 'naked_bend':
        attribute a_idle default 'iwanka_arms_naked_bend_a_dry'


    group arms if_any ['b_kneeling'] auto variant 'kneeling':  
        attribute a_idle default 'iwanka_arms_kneeling_a_knee'


    group arms if_any ['b_chair_swimsuit','b_chair_naked'] auto variant 'chair_naked':  
        attribute a_idle default 'iwanka_arms_chair_naked_a_sides'


    group overlay if_not ['b_bj_naked','b_bj','b_sidebed_left_shy','b_sidebed_left','b_sidebed_right_shy','b_sidebed_right','b_sex_pre_after','b_sex_insert_pullout'] auto:
        attribute o_empty default null


    group overlay if_any ['b_sidebed_left_shy','b_sidebed_left'] auto:
        offset (-286, -15)


    group overlay if_any ['b_sidebed_right_shy','b_sidebed_right'] auto:
        xzoom -1
        offset (316, -15)


    group overlay if_not 'm_talk' if_any ['b_bj_naked','b_bj'] auto variant 'bj':
        attribute o_empty default null


    group overlay if_all 'm_talk' if_any ['b_bj_naked','b_bj'] auto variant 'bj_talk':
        attribute o_empty default null


    group overlay if_any ['b_sex_pre_after']:
        attribute o_empty default null
        attribute o_pre 'iwanka_overlay_o_sex_dick_pre'
        attribute o_after 'iwanka_overlay_o_sex_dick_after'


    group overlay if_any ['b_sex_insert_pullout']:
        attribute o_empty default null
        attribute o_insert_pullout 'iwanka_overlay_o_sex_dick_insert_pullout'
        attribute o_cum 'iwanka_overlay_o_sex_dick_cum'

image iwanka_f = "characters/iwanka/iwanka_face_f_normal.png"

image iwanka_arms_dressed_a_touch = "iwanka_arms_dressed_a_front"
image iwanka_arms_naked_a_touch = "iwanka_arms_naked_a_front"
image iwanka_arms_swimsuit_a_touch = "iwanka_arms_swimsuit_a_front"

image iwanka_body_b_swim_kiss:
    Transform("iwanka_body_b_swim_kiss1")
    pause .4
    Transform("iwanka_body_b_swim_kiss2")
    pause .4
    repeat

image iwanka_body_b_dressed_kiss:
    Transform("iwanka_body_b_dressed_kiss1")
    pause .4
    Transform("iwanka_body_b_dressed_kiss2")
    pause .4
    repeat

image iwanka_body_b_maid_kiss:
    Transform("iwanka_body_b_maid_kiss1")
    pause .4
    Transform("iwanka_body_b_maid_kiss2")
    pause .4
    repeat

image iwanka_body_b_naked_kiss:
    Transform("iwanka_body_b_naked_kiss1")
    pause .4
    Transform("iwanka_body_b_naked_kiss2")
    pause .4
    repeat

image iwanka_arms_naked_bend_a_dry:
    Transform("iwanka_arms_naked_bend_a_dry1")
    pause .4
    Transform("iwanka_arms_naked_bend_a_dry2")
    pause .8
    repeat

image iwanka_arms_sidebed_shy_a_rub:
    Transform("iwanka_arms_sidebed_shy_a_rub1")
    pause .4
    Transform("iwanka_arms_sidebed_shy_a_rub2")
    pause .4
    repeat

image iwanka_arms_sidebed_shy_a_touch:
    Transform("iwanka_arms_sidebed_shy_a_touch1")
    pause .4
    Transform("iwanka_arms_sidebed_shy_a_touch2")
    pause .4
    repeat

image iwanka_club_dance 1 = "iwanka_body_b_club_dance1"
image iwanka_club_dance 2 = "iwanka_body_b_club_dance2"
image iwanka_club_dance 3 = "iwanka_body_b_club_dance3"
image iwanka_club_dance 4 = Composite(
    (1024,768),
    (0,0), "characters/iwanka/iwanka_body_b_club_dance4.png",
    (-52, 27), "characters/iwanka/iwanka_face_f_laugh.png",
    )
image iwanka_club_dance 5 = Composite(
    (1025,768),
    (0,0), "characters/iwanka/iwanka_body_b_club_dance5.png",
    (-70,16), "characters/iwanka/iwanka_face_f_laugh.png",
    )
image iwanka_club_dance 6 = Composite(
    (1026,768),
    (0,0), "characters/iwanka/iwanka_body_b_club_dance6.png",
    (-85, 38), "characters/iwanka/iwanka_face_f_laugh.png",
    )

image iwanka_body_b_club_dance = AnimatedImage('iwanka_club_dance',
    (4, 5, 6, 5), M_iwanka)
image iwanka_body_b_club_dance_back = AnimatedImage('iwanka_club_dance',
    (1, 2, 3, 2), M_iwanka)



init python:
    for o in ('dress', 'naked'):
        for i in xrange(1, 19):
            renpy.image('iwanka_sex_bj_anim_{} {}'.format(o, i),
                        'iwanka_sex_bj_anim_{}{:02}'.format(o, i))

image iwanka_blowjob_dress = AnimatedImage('iwanka_sex_bj_anim_dress',
                                           (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18),
                                           M_iwanka)
image iwanka_blowjob_naked = AnimatedImage('iwanka_sex_bj_anim_naked',
                                           (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18),
                                           M_iwanka)

image iwanka_arms_bj_a_cum:
    Transform("iwanka_arms_bj_a_cum1")
    pause .4
    Transform("iwanka_arms_bj_a_cum2")
    pause .4
    Transform("iwanka_arms_bj_a_cum3")



init python:
    for i in xrange(1, 9):
        renpy.image('iwanka_body_b_sex_anim {}'.format(i),
                    'iwanka_body_b_sex_anim{:02}'.format(i))

image iwanka_body_b_sex_anim = AnimatedImage('iwanka_body_b_sex_anim',
                                           (1,2,3,4,5,6,7,8),
                                           M_iwanka)

image iwanka_overlay_o_sex_dick_cum:
    Transform("iwanka_overlay_o_sex_dick_cum1")
    pause .4
    Transform("iwanka_overlay_o_sex_dick_cum2")
    pause .4
    Transform("iwanka_overlay_o_sex_dick_cum3")


init python hide:
    count = 11
    first = 1
    frames = tuple(i % count + 1 for i in xrange(first, first + count))

    map = (('iwanka_sex_hentai_anim', 'iwanka_sex_hentai'),
           ('iwanka_sex_hentai_anim_cum', 'iwanka_sex_hentai_cum'))

    for src, stem in map:
        for i in frames:
            renpy.image('{} {}'.format(stem, i),
                        '{}{:02}'.format(src, i))
        
        renpy.image(stem, AnimatedImage(stem, frames, M_iwanka))



image xray_iwanka_sex:
    Transform("characters/xray/xray_side_01.png", zoom=.7, rotate=-30, xoffset=375, yoffset=130)
    pause 0.4
    Transform("characters/xray/xray_side_02.png", zoom=.7, rotate=-30, xoffset=375, yoffset=130)
    pause 0.4
    Transform("characters/xray/xray_side_03.png", zoom=.7, rotate=-30, xoffset=375, yoffset=130)
    pause 0.4
    Transform("characters/xray/xray_side_04.png", zoom=.7, rotate=-30, xoffset=375, yoffset=130)
    pause 0.4
    Transform("characters/xray/xray_side_05.png", zoom=.7, rotate=-30, xoffset=375, yoffset=130)
    pause 0.4
    Transform("characters/xray/xray_side_06.png", zoom=.7, rotate=-30, xoffset=375, yoffset=130)
    pause 0.4
    Transform("characters/xray/xray_side_07.png", zoom=.7, rotate=-30, xoffset=375, yoffset=130)
    pause 0.4
    Transform("characters/xray/xray_side_08.png", zoom=.7, rotate=-30, xoffset=375, yoffset=130)
    pause 0.4
    Transform("characters/xray/xray_side_09.png", zoom=.7, rotate=-30, xoffset=375, yoffset=130)
    pause 0.4
    Transform("characters/xray/xray_side_10.png", zoom=.7, rotate=-30, xoffset=375, yoffset=130)
    pause 0.4
    Transform("characters/xray/xray_side_11.png", zoom=.7, rotate=-30, xoffset=375, yoffset=130)
    pause 0.4
    Transform("characters/xray/xray_side_12.png", zoom=.7, rotate=-30, xoffset=375, yoffset=130)
    pause 0.4
    Transform("characters/xray/xray_side_13.png", zoom=.7, rotate=-30, xoffset=375, yoffset=130)
    pause 0.4
    Transform("characters/xray/xray_side_14.png", zoom=.7, rotate=-30, xoffset=375, yoffset=130)
    pause 0.4
    Transform("characters/xray/xray_side_15.png", zoom=.7, rotate=-30, xoffset=375, yoffset=130)
    pause 0.4
    Transform("characters/xray/xray_side_16.png", zoom=.7, rotate=-30, xoffset=375, yoffset=130)
    pause 0.4
    Transform("characters/xray/xray_side_17.png", zoom=.7, rotate=-30, xoffset=375, yoffset=130)
    pause 0.4
    Transform("characters/xray/xray_side_18.png", zoom=.7, rotate=-30, xoffset=375, yoffset=130)
    pause 2.0
    linear 2.5 alpha 0


init python hide:
    count = 10
    first = 1
    frames = tuple(i % count + 1 for i in xrange(first, first + count))

    map = (('iwanka_body_b_sex_ride_anim', 'iwanka_bed_tiger'),)

    for src, stem in map:
        for i in frames:
            renpy.image('{} {}'.format(stem, i),
                        '{}{:02}'.format(src, i))
        
        renpy.image(stem, AnimatedImage(stem, frames, M_iwanka))
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
