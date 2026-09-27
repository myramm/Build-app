init:
    $ josephine_clothing_options = ['b_dressed','b_magic','b_undershirt','b_topless','b_naked','b_empty','b_dressed_fondle','b_dressed_messy','b_dressed_slip','b_naked_mc_kiss_cheek']

init python:


    renpy.image('josephine_arms_a_empty', 'ground.png')
    renpy.image('josephine_body_b_empty', 'ground.png')
    renpy.image('josephine_face_f_empty', 'ground.png')
    renpy.image('josephine_face_talk_f_empty', 'ground.png')


    renpy.image('josephine_face_talk_f_laugh', 'josephine_face_f_laugh')
    renpy.image('josephine_face_talk_f_surprised_down', 'josephine_face_f_surprised_down')
    renpy.image('josephine_face_sex_bj_talk_talk_f_cum', 'josephine_face_sex_bj_talk_f_cum')
    renpy.image('josephine_face_sex_talk_f_moan', 'josephine_face_sex_f_moan')
    renpy.image('josephine_face_chair_talk_f_laugh', 'josephine_face_chair_f_laugh')



layeredimage josephine:

    yanchor config.screen_height
    ypos 1.
    xanchor config.screen_width
    xpos 1.


    group body auto:
        attribute b_dressed default
        attribute b_empty null
        attribute b_dressed_kiss "josephine_body_b_dressed_kiss"

        attribute b_naked_kiss "josephine_body_b_naked_kiss"

        attribute b_magic "josephine_body_b_[M_josie.outfit.get][M_josie.pregnancy.to_string]"   

        attribute b_sex_top null


    group mouth prefix 'm':
        attribute talk null

    group face:
        attribute f_normal default null







    group face if_not 'm_talk' if_any josephine_clothing_options auto


    group face if_not 'm_talk' if_any 'b_dressed_couch' auto:
        rotate 10
        offset (-84, -138)


    group face if_not 'm_talk' if_any ['b_naked_jerk'] auto:
        offset (-416, 16)


    group face if_not 'm_talk' if_any ['b_naked_sexy'] auto:
        offset (-4, 6)


    group face if_not 'm_talk' if_any ['b_naked_grab'] auto:
        xzoom -1
        offset (646, 0)


    group face if_not 'm_talk' if_any ['b_gown_bed'] auto:
        offset (83, 24)


    group face if_not 'm_talk' if_any ['b_sex_top'] auto:
        anchor (.5, .5)
        pos (512 - 300, 384 - 133)
        rotate -1
        rotate_pad False
        zoom 1.18






    group face if_not 'm_talk' if_any ['b_chair'] auto variant 'chair'


    group face if_not 'm_talk' if_any ['b_sex_after_top', 'b_sex_after_top_no_phone', 'b_sex_insert_top', 'b_sex_insert_top_no_phone', 'b_sex_pre_top', 'b_sex_pre_top_no_phone', 'b_sex_pullout_top', 'b_sex_pullout_top_no_phone'] auto variant 'sex'


    group face if_not 'm_talk' if_any 'b_sex_bj_talk' auto variant 'sex_bj_talk':
        attribute f_normal default 'josephine_face_sex_bj_talk_f_normal'


    group face if_any 'b_sex_bj_lick' auto:
        attribute f_normal default 'josephine_face_sex_bj_lick_f_lick_cum'







    group face if_all 'm_talk' if_any josephine_clothing_options auto variant 'talk'


    group face if_all 'm_talk' if_any 'b_dressed_couch' auto variant 'talk':
        rotate 10
        offset (-84, -138)


    group face if_all 'm_talk' if_any ['b_naked_jerk'] auto variant 'talk':
        offset (-416, 16)


    group face if_all 'm_talk' if_any ['b_naked_sexy'] auto variant 'talk':
        offset (-4, 6)


    group face if_all 'm_talk' if_any ['b_naked_grab'] auto variant 'talk': 
        xzoom -1
        offset (646, 0)


    group face if_all ['m_talk', 'b_gown_bed'] auto variant 'talk':
        offset (83, 24)


    group face if_all 'm_talk' if_any ['b_sex_top'] auto variant 'talk':
        anchor (.5, .5)
        pos (512 - 300, 384 - 133)
        rotate -1
        rotate_pad False
        zoom 1.18






    group face if_all 'm_talk' if_any ['b_chair'] auto variant 'chair_talk'


    group face if_all 'm_talk' if_any ['b_sex_after_top', 'b_sex_after_top_no_phone', 'b_sex_insert_top', 'b_sex_insert_top_no_phone', 'b_sex_pre_top', 'b_sex_pre_top_no_phone', 'b_sex_pullout_top', 'b_sex_pullout_top_no_phone'] auto variant 'sex_talk'


    group face if_all 'm_talk' if_any 'b_sex_bj_talk' auto variant 'sex_bj_talk_talk':
        attribute f_normal default 'josephine_face_sex_bj_talk_talk_f_normal'



    group arms if_any ['b_dressed','b_dressed_messy','b_dressed_slip'] auto variant 'dressed':
        attribute a_idle default 'josephine_arms_dressed_a_desk'
        attribute a_baby "josephine_arms_dressed_a_baby_[M_josie.pregnancy.baby_gender]"

        attribute a_touch 'josephine_arms_dressed_a_touch[M_josie.pregnancy.to_string]'


    group arms if_any ['b_dressed_couch'] auto variant 'dressed_couch':
        attribute a_idle default 'josephine_arms_dressed_couch_a_phone'


    group arms if_all 'b_gown_bed' auto variant 'gown_bed':
        attribute a_idle default "josephine_arms_gown_bed_a_baby_[M_josie.pregnancy.baby_gender]"



    group arms if_all 'b_magic' auto:
        attribute a_idle default 'josephine_arms_[M_josie.outfit.get]_a_touch[M_josie.pregnancy.to_string]'
        attribute a_phone 'josephine_arms_[M_josie.outfit.get]_a_phone'
        attribute a_phone_show_left 'josephine_arms_[M_josie.outfit.get]_a_phone_show_left'



    group arms if_all 'b_dressed_fondle' auto variant 'dressed_fondle':
        attribute a_idle default 'josephine_arms_dressed_fondle_a_squeeze'


    group arms if_all 'b_topless' auto variant 'topless':
        attribute a_idle default 'josephine_arms_topless_a_undress4'


    group arms if_all 'b_undershirt' auto variant 'undershirt':
        attribute a_idle default 'josephine_arms_undershirt_a_undress3'


    group arms if_all 'b_naked_jerk' auto variant 'naked_jerk':
        attribute a_idle default 'josephine_arms_naked_jerk_a_unzip1'
        attribute a_jerk 'josephine_arms_naked_jerk_a_jerk'


    group arms if_any ['b_naked'] auto variant 'naked':
        attribute a_idle default 'josephine_arms_naked_a_hips'
        attribute a_touch 'josephine_arms_naked_a_touch[M_josie.pregnancy.to_string]'


    group overlay if_not 'b_sex_bj_talk' auto:
        attribute o_empty default null

    group overlay if_not 'm_talk' if_all 'b_sex_bj_talk' auto variant 'sex_bj_talk':
        attribute o_empty default null

    group overlay if_all ['m_talk', 'b_sex_bj_talk'] auto variant 'sex_bj_talk_talk':
        attribute o_empty default null

image josephine_f = "characters/josephine/josephine_face_f_normal.png"

image josephine_arms_dressed_a_touch = "characters/josephine/josephine_arms_dressed_a_hips.png"

image josephine_arms_naked_a_touch = "characters/josephine/josephine_arms_naked_a_hips.png"

image josephine_body_b_dressed_kiss:
    Transform("josephine_body_b_dressed_kiss1")
    pause .4
    Transform("josephine_body_b_dressed_kiss2")
    pause .4
    repeat

image josephine_body_b_naked_kiss:
    Transform("josephine_body_b_dressed_kiss3")
    pause .4
    Transform("josephine_body_b_dressed_kiss4")
    pause .4
    repeat

image josephine_arms_dressed_fondle_a_squeeze:
    Transform("josephine_arms_dressed_fondle_a_squeeze1")
    pause .4
    Transform("josephine_arms_dressed_fondle_a_squeeze2")
    pause .4
    repeat

image josephine_arms_naked_jerk_a_jerk:
    Transform("josephine_arms_naked_jerk_a_jerk1")
    pause .4
    Transform("josephine_arms_naked_jerk_a_jerk2")
    pause .4
    repeat


image mc_josephine_sex pre = "josephine_sex_pre_bottom"
image mc_josephine_sex insert = "josephine_sex_insert_bottom"
image mc_josephine_sex pullout = "josephine_sex_pullout_bottom"
image mc_josephine_sex cum = "josephine_sex_cum_bottom"
image mc_josephine_sex after = "josephine_sex_after_bottom"

image josephine_sex_cum_cumshot:
    Transform("josephine_sex_cum_cumshot1")
    pause .4
    Transform("josephine_sex_cum_cumshot2")
    pause .4
    Transform("josephine_sex_cum_cumshot3")

image josephine_office_sex_mc_slow 1 = "josephine_body_b_sex_anim_slow_mc01"
image josephine_office_sex_mc_slow 2 = "josephine_body_b_sex_anim_slow_mc02"
image josephine_office_sex_mc_slow 3 = "josephine_body_b_sex_anim_slow_mc03"
image josephine_office_sex_mc_slow 4 = "josephine_body_b_sex_anim_slow_mc04"
image josephine_office_sex_mc_slow 5 = "josephine_body_b_sex_anim_slow_mc05"
image josephine_office_sex_mc_slow 6 = "josephine_body_b_sex_anim_slow_mc06"
image josephine_office_sex_mc_slow 7 = "josephine_body_b_sex_anim_slow_mc07"
image josephine_office_sex_mc_slow 8 = "josephine_body_b_sex_anim_slow_mc08"
image josephine_office_sex_mc_slow 9 = "josephine_body_b_sex_anim_slow_mc09"
image josephine_office_sex_mc_slow 10 = "josephine_body_b_sex_anim_slow_mc10"

image josephine_office_sex_josephine_slow 1 = "josephine_body_b_sex_anim_slow01"
image josephine_office_sex_josephine_slow 2 = "josephine_body_b_sex_anim_slow02"
image josephine_office_sex_josephine_slow 3 = "josephine_body_b_sex_anim_slow03"
image josephine_office_sex_josephine_slow 4 = "josephine_body_b_sex_anim_slow04"
image josephine_office_sex_josephine_slow 5 = "josephine_body_b_sex_anim_slow05"
image josephine_office_sex_josephine_slow 6 = "josephine_body_b_sex_anim_slow06"
image josephine_office_sex_josephine_slow 7 = "josephine_body_b_sex_anim_slow07"
image josephine_office_sex_josephine_slow 8 = "josephine_body_b_sex_anim_slow08"
image josephine_office_sex_josephine_slow 9 = "josephine_body_b_sex_anim_slow09"
image josephine_office_sex_josephine_slow 10 = "josephine_body_b_sex_anim_slow10"

image josephine_office_sex_mc_fast 1 = "josephine_body_b_sex_anim_fast_mc01"
image josephine_office_sex_mc_fast 2 = "josephine_body_b_sex_anim_fast_mc02"
image josephine_office_sex_mc_fast 3 = "josephine_body_b_sex_anim_fast_mc03"
image josephine_office_sex_mc_fast 4 = "josephine_body_b_sex_anim_fast_mc04"
image josephine_office_sex_mc_fast 5 = "josephine_body_b_sex_anim_fast_mc05"
image josephine_office_sex_mc_fast 6 = "josephine_body_b_sex_anim_fast_mc06"
image josephine_office_sex_mc_fast 7 = "josephine_body_b_sex_anim_fast_mc07"
image josephine_office_sex_mc_fast 8 = "josephine_body_b_sex_anim_fast_mc08"

image josephine_office_sex_josephine_fast 1 = "josephine_body_b_sex_anim_fast01"
image josephine_office_sex_josephine_fast 2 = "josephine_body_b_sex_anim_fast02"
image josephine_office_sex_josephine_fast 3 = "josephine_body_b_sex_anim_fast03"
image josephine_office_sex_josephine_fast 4 = "josephine_body_b_sex_anim_fast04"
image josephine_office_sex_josephine_fast 5 = "josephine_body_b_sex_anim_fast05"
image josephine_office_sex_josephine_fast 6 = "josephine_body_b_sex_anim_fast06"
image josephine_office_sex_josephine_fast 7 = "josephine_body_b_sex_anim_fast07"
image josephine_office_sex_josephine_fast 8 = "josephine_body_b_sex_anim_fast08"


image josephine_office_bj_mc = "josephine_sex_bj_anim_mc_overlay"

image josephine_office_bj 1 = "josephine_sex_bj_anim01"
image josephine_office_bj 2 = "josephine_sex_bj_anim02"
image josephine_office_bj 3 = "josephine_sex_bj_anim03"
image josephine_office_bj 4 = "josephine_sex_bj_anim04"
image josephine_office_bj 5 = "josephine_sex_bj_anim05"
image josephine_office_bj 6 = "josephine_sex_bj_anim06"
image josephine_office_bj 7 = "josephine_sex_bj_anim07"
image josephine_office_bj 8 = "josephine_sex_bj_anim08"
image josephine_office_bj 9 = "josephine_sex_bj_anim09"
image josephine_office_bj 10 = "josephine_sex_bj_anim10"
image josephine_office_bj 11 = "josephine_sex_bj_anim11"
image josephine_office_bj 12 = "josephine_sex_bj_anim12"

image josephine_office_bj_dick_cum:
    Transform("josephine_sex_bj_dick_cum1")
    pause .4
    Transform("josephine_sex_bj_dick_cum2")
    pause .4
    Transform("josephine_sex_bj_dick_cum3")

image josephine_face_sex_bj_lick_f_lick_cum:
    Transform("josephine_face_sex_bj_lick_f_lick_cum1")
    pause .4
    Transform("josephine_face_sex_bj_lick_f_lick_cum2")
    pause .4
    repeat


image josephine_face_sex_bj_lick_f_lick_cum1 = Composite(
    (1024,768),
    (0,0), "characters/josephine/josephine_face_sex_bj_lick_f_lick1.png",
    (0,0), "characters/josephine/josephine_overlay_sex_bj_talk_o_cum_lick1.png",
    )

image josephine_face_sex_bj_lick_f_lick_cum2 = Composite(
    (1024,768),
    (0,0), "characters/josephine/josephine_face_sex_bj_lick_f_lick2.png",
    (0,0), "characters/josephine/josephine_overlay_sex_bj_talk_o_cum_lick2.png",
    )





image xray_josephine_top:
    Transform("characters/xray/xray_front_top_01.png", xzoom=-.7, yzoom=.7, rotate=50, xoffset=100, yoffset=190)
    pause 0.4
    Transform("characters/xray/xray_front_top_02.png", xzoom=-.7, yzoom=.7, rotate=50, xoffset=100, yoffset=190)
    pause 0.4
    Transform("characters/xray/xray_front_top_03.png", xzoom=-.7, yzoom=.7, rotate=50, xoffset=100, yoffset=190)
    pause 0.4
    Transform("characters/xray/xray_front_top_04.png", xzoom=-.7, yzoom=.7, rotate=50, xoffset=100, yoffset=190)
    pause 0.4
    Transform("characters/xray/xray_front_top_05.png", xzoom=-.7, yzoom=.7, rotate=50, xoffset=100, yoffset=190)
    pause 0.4
    Transform("characters/xray/xray_front_top_06.png", xzoom=-.7, yzoom=.7, rotate=50, xoffset=100, yoffset=190)
    pause 0.4
    Transform("characters/xray/xray_front_top_07.png", xzoom=-.7, yzoom=.7, rotate=50, xoffset=100, yoffset=190)
    pause 0.4
    Transform("characters/xray/xray_front_top_08.png", xzoom=-.7, yzoom=.7, rotate=50, xoffset=100, yoffset=190)
    pause 0.4
    Transform("characters/xray/xray_front_top_09.png", xzoom=-.7, yzoom=.7, rotate=50, xoffset=100, yoffset=190)
    pause 0.4
    Transform("characters/xray/xray_front_top_10.png", xzoom=-.7, yzoom=.7, rotate=50, xoffset=100, yoffset=190)
    pause 0.4
    Transform("characters/xray/xray_front_top_11.png", xzoom=-.7, yzoom=.7, rotate=50, xoffset=100, yoffset=190)
    pause 0.4
    Transform("characters/xray/xray_front_top_12.png", xzoom=-.7, yzoom=.7, rotate=50, xoffset=100, yoffset=190)
    pause 0.4
    Transform("characters/xray/xray_front_top_13.png", xzoom=-.7, yzoom=.7, rotate=50, xoffset=100, yoffset=190)
    pause 0.4
    Transform("characters/xray/xray_front_top_14.png", xzoom=-.7, yzoom=.7, rotate=50, xoffset=100, yoffset=190)
    pause 0.4
    Transform("characters/xray/xray_front_top_15.png", xzoom=-.7, yzoom=.7, rotate=50, xoffset=100, yoffset=190)
    pause 0.4
    Transform("characters/xray/xray_front_top_16.png", xzoom=-.7, yzoom=.7, rotate=50, xoffset=100, yoffset=190)
    pause 0.4
    Transform("characters/xray/xray_front_top_17.png", xzoom=-.7, yzoom=.7, rotate=50, xoffset=100, yoffset=190)
    pause 0.4
    Transform("characters/xray/xray_front_top_18.png", xzoom=-.7, yzoom=.7, rotate=50, xoffset=100, yoffset=190)
    pause 2.0
    linear 2.5 alpha 0



init python hide:
    count = 12
    first = 1
    frames = tuple(i % count + 1 for i in xrange(first, first + count))

    map = (('josephine_sex_chair_anim', 'josie_sex_chair'),
           ('josephine_sex_top_anim', 'josie_sex_desk'))

    for src, stem in map:
        for i in frames:
            renpy.image('{} {}'.format(stem, i),
                        '{}{:02}'.format(src, i))
        
        renpy.image(stem, AnimatedImage(stem, frames, M_josie))

layeredimage josephine sex_chair:
    attribute m_talk null

    group face if_not 'm_talk' auto:
        attribute f_normal default

    group face if_all 'm_talk' auto variant 'talk'

image josephine_sex_chair_cumshot:
    'josephine_sex_chair_cumshot1'
    .4
    'josephine_sex_chair_cumshot2' with fastdissolve
    .4
    'josephine_sex_chair_cumshot3' with fastdissolve

image josephine_sex_top_slide:
    'josephine_sex_top_anim01'
    .2
    'josephine_sex_top_anim02' with fastdissolve
    .2
    'josephine_sex_top_anim03' with fastdissolve
    .2
    'josephine_sex_top_anim04' with fastdissolve
    .2
    'josephine_sex_top_anim05' with fastdissolve
    .2
    'josephine_sex_top_anim06' with fastdissolve

image josephine_sex_top_rope1:
    contains:
        'josephine_sex_top_cumshot1'
        .4
        'josephine_sex_top_cumshot2' with fastdissolve
    contains:
        'josephine_sex_top_dick1'
        .4
        'josephine_sex_top_dick2' with fastdissolve

image josephine_sex_top_rope2:
    contains:
        'josephine_sex_top_cumshot4'
        .4
        'josephine_sex_top_cumshot5' with fastdissolve
    contains:
        'josephine_sex_top_dick1'
        .4
        'josephine_sex_top_dick2' with fastdissolve

layeredimage josephine sex_top:
    attribute m_talk null

    group face if_not 'm_talk' auto:
        attribute f_normal default null
    group face if_all 'm_talk' auto variant 'talk'
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
