init:
    $ roz_clothing_options = ['b_dressed','b_magic']

init python:


    renpy.image('roz_arms_a_empty', 'ground.png')
    renpy.image('roz_body_b_empty', 'ground.png')
    renpy.image('roz_face_f_empty', 'ground.png')
    renpy.image('roz_face_talk_f_empty', 'ground.png')


    renpy.image('roz_face_talk_f_laugh', 'roz_face_f_laugh')
    renpy.image('roz_face_talk_f_surprised', 'roz_face_f_surprised')
    renpy.image('roz_face_talk_f_surprised_down', 'roz_face_f_surprised_down')


    renpy.image('roz_face_f_remove_teeth', 'roz_face_talk_f_remove_teeth')

layeredimage roz:

    yanchor config.screen_height
    ypos 1.
    xanchor config.screen_width
    xpos 1.


    group body auto:
        attribute b_dressed default
        attribute b_empty null
        attribute b_magic "roz_body_b_[M_roz.outfit.get][M_roz.pregnancy.to_string]"   



    group mouth prefix 'm':
        attribute talk null

    group face:
        attribute f_normal default null







    group face if_not 'm_talk' if_any roz_clothing_options auto


    group face if_not 'm_talk' if_any 'b_dressed_kneeling' auto:
        offset (-46, 145)


    group face if_not 'm_talk' if_any 'b_gown_bed' auto:
        offset (328, 58)











    group face if_all 'm_talk' if_any roz_clothing_options auto variant 'talk'


    group face if_all 'm_talk' if_any 'b_dressed_kneeling' auto variant 'talk':
        offset (-46, 145)


    group face if_all ['m_talk', 'b_gown_bed'] auto variant 'talk':
        offset (328, 58)







    group arms if_all 'b_dressed' auto variant 'dressed':
        attribute a_idle default 'roz_arms_dressed_a_hips'
        attribute a_baby "roz_arms_dressed_a_baby_[M_roz.pregnancy.baby_gender]"



    group arms if_all 'b_gown_bed' auto variant 'gown_bed':
        attribute a_idle default "roz_arms_gown_bed_a_baby_[M_roz.pregnancy.baby_gender]"



    group arms if_all 'b_magic' auto:
        attribute a_idle default 'roz_arms_[M_roz.outfit.get]_a_touch[M_roz.pregnancy.to_string]'


    group arms if_all 'b_dressed_kneeling' auto variant 'dressed_kneeling':
        attribute a_idle default 'roz_arms_dressed_kneeling_a_down'






    group overlay auto:
        attribute o_empty default null

image roz_f = "characters/roz/layeredimage/roz_face_f_normal.png"

image roz_arms_dressed_a_touch = "characters/roz/layeredimage/roz_arms_dressed_a_hips.png"



image roz_mc_body_bj = "roz_sex_mc"
image roz_mc_body_bj cum = "roz_sex_mc_cum"

image roz_mc_face_bj normal = "roz_sex_mc_face_f_normal"
image roz_mc_face_bj normal_talk = "roz_sex_mc_face_talk_f_normal"

image roz_bj 1 = "roz_sex_bj_anim_01"
image roz_bj 2 = "roz_sex_bj_anim_02"
image roz_bj 3 = "roz_sex_bj_anim_03"
image roz_bj 4 = "roz_sex_bj_anim_04"
image roz_bj 5 = "roz_sex_bj_anim_05"
image roz_bj 6 = "roz_sex_bj_anim_06"
image roz_bj 7 = "roz_sex_bj_anim_07"
image roz_bj 8 = "roz_sex_bj_anim_08"
image roz_bj 9 = "roz_sex_bj_anim_09"
image roz_bj 10 = "roz_sex_bj_anim_10"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
