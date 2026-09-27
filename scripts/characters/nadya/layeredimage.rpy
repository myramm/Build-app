init:
    $ nadya_clothing_options = ['b_magic','b_traditional','b_dressed','b_naked','b_pantless','b_dressed_magic']

init python:


    renpy.image('nadya_arms_a_empty', 'ground.png')
    renpy.image('nadya_body_b_empty', 'ground.png')
    renpy.image('nadya_face_f_empty', 'ground.png')
    renpy.image('nadya_face_talk_f_empty', 'ground.png')


    renpy.image('nadya_face_talk_f_laugh', 'nadya_face_f_laugh')
    renpy.image('nadya_face_limo_talk_f_laugh', 'nadya_face_limo_f_laugh')




    renpy.image('nadya_arms_dressed_a_touch', 'nadya_arms_dressed_a_hips')
    renpy.image('nadya_arms_dressed_couch_a_touch', 'nadya_arms_dressed_couch_a_down')


layeredimage nadya:

    yanchor config.screen_height
    ypos 1.
    xanchor config.screen_width
    xpos 1.


    group body auto:
        attribute b_dressed default
        attribute b_empty null
        attribute b_magic "nadya_body_b_[M_nadya.outfit][M_nadya.pregnancy]"   

        attribute b_traditional_kiss
        attribute b_dressed_magic "nadya_tubuh_b_berdandan[M_nadya.pregnancy]"

        attribute b_dressed_couch_magic "nadya_body_b_dressed_couch[M_nadya.pregnancy]"



    group mouth prefix 'm':
        attribute talk null

    group face:
        attribute f_normal default null







    group face if_not 'm_talk' if_any nadya_clothing_options auto


    group face if_not 'm_talk' if_any ['b_sex_wall_pre', 'b_sex_wall_insert_pullout'] auto:
        align (.5, .5)
        offset (-302, -109)
        zoom 1.105


    group face if_not 'm_talk' if_any 'b_sex_wall_facial' auto:
        align (.5, .5)
        offset (-302, 223)
        zoom 1.105


    group face if_not 'm_talk' if_any 'b_sex_wall_after' auto:
        align (.5, .5)
        offset (-302, -93)
        zoom 1.105


    group face if_not 'm_talk' if_any 'b_dressed_undress2' auto:
        offset (-60,172)


    group face if_not 'm_talk' if_any ['b_gown_bed'] auto:
        offset (91, 38)


    group face if_not 'm_talk' if_any ['b_gown_bed_sleep'] auto:
        align (.5, .5)
        offset (110, -58)
        rotate 20
        rotate_pad False


    group face if_not 'm_talk' if_any ['b_dressed_couch', 'b_naked_couch', 'b_naked_couch_open', 'b_dressed_couch_undress3', 'b_dressed_couch_magic'] auto:
        offset (57, 26)


    group face if_not 'm_talk' if_any 'b_dressed_couch_relax' auto:
        offset (105, 50)


    group face if_not 'm_talk' if_any 'b_naked_couch_sit' auto:
        offset (-20, 8)

    group face if_not 'm_talk' if_any 'b_dressed_laugh' auto:
        offset (-64.5, 131)






    group face if_not 'm_talk' if_any ['b_dress_limo1','b_dress_limo2','b_dress_limo3','b_dress_limo5','b_dress_limo6','b_dress_limo7','b_dress_limo8','b_dress_limo9','b_dress_limo10','b_dress_limo11','b_dress_limo12','b_dress_limo13','b_dress_limo14','b_dress_limo15'] auto variant 'limo'


    group face if_not 'm_talk' if_any ['b_sex_bj_after'] auto:
        align (.5, .5)
        offset (-17, -155)
        rotate -3
        rotate_pad False
        zoom 1.41







    group face if_all 'm_talk' if_any nadya_clothing_options auto variant 'talk'


    group face if_all 'm_talk' if_any ['b_sex_wall_pre', 'b_sex_wall_insert_pullout'] auto variant 'talk':
        align (.5, .5)
        offset (-302, -109)
        zoom 1.105


    group face if_all 'm_talk' if_any 'b_sex_wall_facial' auto variant 'talk':
        align (.5, .5)
        offset (-302, 223)
        zoom 1.105


    group face if_all 'm_talk' if_any 'b_sex_wall_after' auto variant 'talk':
        align (.5, .5)
        offset (-302, -93)
        zoom 1.105


    group face if_all 'm_talk' if_any 'b_dressed_undress2' auto variant 'talk':
        offset (-60,172)


    group face if_all 'm_talk' if_any ['b_gown_bed'] auto variant 'talk':
        offset (91, 38)


    group face if_all 'm_talk' if_any ['b_gown_bed_sleep'] auto variant 'talk':
        align (.5, .5)
        offset (110, -58)
        rotate 20
        rotate_pad False


    group face if_all 'm_talk' if_any ['b_dressed_couch', 'b_naked_couch', 'b_naked_couch_open', 'b_dressed_couch_undress3', 'b_dressed_couch_magic'] auto variant 'talk':
        offset (57, 26)


    group face if_all 'm_talk' if_any 'b_dressed_couch_relax' auto variant 'talk':
        offset (105, 50)


    group face if_all 'm_talk' if_any 'b_naked_couch_sit' auto variant 'talk':
        offset (-20, 8)

    group face if_all 'm_talk' if_any 'b_dressed_laugh' auto variant 'talk':
        offset (-64.5, 131)






    group face if_all 'm_talk' if_any ['b_dress_limo1','b_dress_limo2','b_dress_limo3','b_dress_limo5','b_dress_limo6','b_dress_limo7','b_dress_limo8','b_dress_limo9','b_dress_limo10','b_dress_limo11','b_dress_limo12','b_dress_limo13','b_dress_limo14','b_dress_limo15'] auto variant 'limo_talk'


    group face if_all 'm_talk' if_any ['b_sex_bj_after'] auto variant 'talk':
        align (.5, .5)
        offset (-17, -155)
        rotate -3
        rotate_pad False
        zoom 1.41



    group arms if_all 'b_dressed' auto variant 'dressed':
        attribute a_idle default 'nadya_arms_dressed_a_hips'
        attribute a_baby 'nadya_arms_dressed_a_baby_[M_nadya.pregnancy.baby_gender]'


    group arms if_all 'b_dressed_magic':
        attribute a_idle default 'nadya_arms_dressed[M_nadya.pregnancy]_a_touch'
        attribute a_angry 'nadya_arms_dressed[M_nadya.pregnancy]_a_angry'
        attribute a_hips 'nadya_arms_dressed[M_nadya.pregnancy]_a_hips'
        attribute a_point 'nadya_arms_dressed_a_point'


    group arms if_all 'b_traditional' auto variant 'traditional':
        attribute a_idle default 'nadya_arms_traditional_a_hips'


    group arms if_all 'b_dressed_couch' auto variant 'dressed_couch':
        attribute a_idle default 'nadya_arms_dressed_couch_a_down'
        attribute a_baby 'nadya_arms_dressed_couch_a_baby_[M_nadya.pregnancy.baby_gender]'


    group arms if_any ['b_naked_couch', 'b_naked_couch_open'] auto variant 'naked_couch':
        attribute a_idle default 'nadya_arms_naked_couch_a_down'


    group arms if_all 'b_dressed_couch_relax' auto variant 'dressed_couch_relax':
        attribute a_idle default 'nadya_arms_dressed_couch_relax_a_down'


    group arms if_any ['b_dressed_couch_magic']:
        attribute a_idle default 'nadya_arms_dressed_couch[M_nadya.pregnancy]_a_touch'


    group arms if_all 'b_sex_bj_pre' auto variant 'sex_bj_pre':
        attribute a_idle default 'nadya_arms_sex_bj_pre_a_touch'
        attribute a_wiggle 'nadya_arms_sex_bj_pre_a_wiggle'


    group arms if_all 'b_sex_bj_after' auto variant 'sex_bj_after':
        attribute a_idle default 'nadya_arms_sex_bj_after_a_down'


    group arms if_all 'b_sex_wall_facial' auto variant 'sex_wall_facial':
        attribute a_idle default 'nadya_arms_sex_wall_facial_a_down'


    group arms if_all 'b_gown_bed' auto variant 'gown_bed':
        attribute a_idle default 'nadya_arms_gown_bed_a_baby_[M_nadya.pregnancy.baby_gender]'


    group arms if_any ['b_pantless'] auto variant 'dressed':
        attribute a_idle default 'nadya_arms_dressed_a_crossed'


    group arms if_any ['b_naked'] auto variant 'naked':
        attribute a_idle default 'nadya_arms_naked_a_hips'


    group arms if_any ['b_magic'] auto:
        attribute a_idle default 'nadya_arms_[M_nadya.outfit]_a_touch[M_nadya.pregnancy]'

    group arms if_all 'b_dressed_laugh' auto variant 'dressed_laugh'


    group overlay if_not ['b_dressed_couch', 'b_naked_couch', 'b_naked_couch_open'] auto:
        attribute o_empty default null

    group overlay if_any ['b_dressed_couch', 'b_naked_couch', 'b_naked_couch_open'] variant 'naked_couch' auto:
        attribute o_empty default null


layeredimage nadya nadya_sex_couch:
    group body auto:
        attribute b_pre default

    group mouth prefix 'm':
        attribute talk null

    group anon if_any 'b_base' auto:
        attribute a_insert default
        attribute a_cumshot

    group overlay if_all 'b_pre' auto variant 'pre'
    group overlay if_all ['b_base', 'a_insert'] auto variant 'insert'

    group face if_not 'm_talk' if_any ['b_base', 'b_pre'] auto:
        attribute f_normal default

    group face if_all 'm_talk' if_any ['b_base', 'b_pre'] auto variant 'talk':
        attribute f_laugh 'nadya_nadya_sex_couch_face_f_laugh'


layeredimage nadya cutscene30:
    group face auto:
        attribute f_normal default null


layeredimage nadya cutscene36:
    group mouth prefix 'm':
        attribute talk null

    group face if_not 'm_talk' auto
    group face if_all 'm_talk' auto variant 'talk'


image nadya_f = "characters/nadya/nadya_face_f_normal.png"

image nadya_arms_sex_bj_pre_a_wiggle:
    Transform("nadya_arms_sex_bj_pre_a_wiggle1")
    pause .4
    Transform("nadya_arms_sex_bj_pre_a_wiggle2")
    pause .4
    repeat

image nadya_body_b_traditional_kiss:
    'nadya_body_b_traditional_kiss1'
    .4
    'nadya_body_b_traditional_kiss2'
    .4
    repeat


init python:
    for i in xrange(1, 8):
        renpy.image('nadya_blowjob_anim {}'.format(i),
                    'nadya_body_b_sex_bj_anim{:02}'.format(i))

image nadya_blowjob_anim = AnimatedImage('nadya_blowjob_anim',
                                         (1,2,3,4,5,6,7), M_nadya)


init python:
    for i in xrange(1, 11):
        renpy.image('nadya_sex_couch_anim {}'.format(i),
                    'nadya_body_b_sex_couch_anim{:02}'.format(i))

image nadya_sex_couch_anim = AnimatedImage('nadya_sex_couch_anim',
                                          (1,2,3,4,5,6,7,8,9,10), M_nadya)


image nadya_nadya_sex_couch_anon_a_cumshot:
    'nadya_nadya_sex_couch_anon_a_cumshot1'
    .4
    'nadya_nadya_sex_couch_anon_a_cumshot2'
    .4
    'nadya_nadya_sex_couch_anon_a_cumshot3'


image xray_nadya_sex_couch:
    anchor (.5, .5)
    pos (331 + 250, 112 + 250)
    rotate 27
    rotate_pad False
    xzoom -.78
    yzoom .78
    'xray_side'


init python:
    for i in xrange(1, 10):
        renpy.image('nadya_sex_wall_anim {}'.format(i),
                    'nadya_body_b_sex_wall_anim{:02}'.format(i))

image nadya_sex_wall_anim = AnimatedImage('nadya_sex_wall_anim',
                                          (1,2,3,4,5,6,7,8,9), M_nadya)


image xray_nadya_sex_wall:
    anchor (.5, .5)
    pos (318 + 250, 162 + 250)
    rotate -51.5
    rotate_pad False
    xzoom -.55
    yzoom .55
    'xray_left_back'


image nadya_sex_wall_after_overlay_o_cum:
    'nadya_overlay_o_storage_sex_after_cum1'
    block:
        .5
        'nadya_overlay_o_storage_sex_after_cum2' with slowdissolve
        .8
        'nadya_overlay_o_storage_sex_after_cum3' with fastdissolve
        .2
        'nadya_overlay_o_storage_sex_after_cum2' with slowdissolve
        .8
        Fixed('nadya_overlay_o_storage_sex_after_cum1',
              Transform('nadya_overlay_o_storage_sex_after_cum3',
                        crop=(0, 384, 1024, 384), yalign=1.)) with fastdissolve
        .2
        'nadya_overlay_o_storage_sex_after_cum1' with dissolve
        repeat
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
