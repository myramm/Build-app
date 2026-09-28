init:
    $ micoe_clothing_options = ['b_dressed','b_jerk1','b_jerk2','b_jerk3','b_jerk']

init python:


    renpy.image('micoe_arms_a_empty', 'ground.png')
    renpy.image('micoe_body_b_empty', 'ground.png')
    renpy.image('micoe_face_f_empty', 'ground.png')
    renpy.image('micoe_face_talk_f_empty', 'ground.png')


    renpy.image('micoe_face_talk_f_laugh', 'micoe_face_f_laugh')
    renpy.image('micoe_face_talk_f_surprised', 'micoe_face_f_surprised')
    renpy.image('micoe_face_talk_f_wink', 'micoe_face_f_wink')
    renpy.image('micoe_face_talk_f_spit', 'micoe_face_f_spit')
    renpy.image('micoe_face_talk_f_full', 'micoe_face_f_full')
    renpy.image('micoe_face_talk_f_lip_bite', 'micoe_face_f_lip_bite')
    renpy.image('micoe_face_talk_f_look_back', 'micoe_face_f_look_back')



layeredimage micoe:

    yanchor config.screen_height
    ypos 1.
    xanchor config.screen_width
    xpos 1.


    group body auto:
        attribute b_dressed default
        attribute b_empty null
        attribute b_jerk "micoe_body_b_jerk"


    group mouth prefix 'm':
        attribute talk null

    group face:
        attribute f_normal default null







    group face if_not 'm_talk' if_any micoe_clothing_options auto











    group face if_all 'm_talk' if_any micoe_clothing_options auto variant 'talk'







    group arms if_all 'b_dressed' auto variant 'dressed':
        attribute a_idle default 'micoe_arms_dressed_a_front'






    group overlay auto:
        attribute o_empty default null

image micoe_f = "characters/micoe/micoe_face_f_normal.png"

image micoe_body_b_jerk:
    Transform("characters/micoe/micoe_body_b_jerk2.png")
    pause 0.4
    Transform("characters/micoe/micoe_body_b_jerk3.png")
    pause 0.4
    repeat



image micoe_bj cum = "characters/micoe/micoe_sex_bj_cum.png"
image micoe_bj look = "characters/micoe/micoe_sex_bj_look.png"
image micoe_bj talk = "characters/micoe/micoe_sex_bj_talk.png"
image micoe_bj mouth_full = "characters/micoe/micoe_sex_bj_mouth_full.png"

image micoe_bj 1 = "characters/micoe/micoe_sex_bj_anim01.png"
image micoe_bj 2 = "characters/micoe/micoe_sex_bj_anim02.png"
image micoe_bj 3 = "characters/micoe/micoe_sex_bj_anim03.png"
image micoe_bj 4 = "characters/micoe/micoe_sex_bj_anim04.png"
image micoe_bj 5 = "characters/micoe/micoe_sex_bj_anim05.png"
image micoe_bj 6 = "characters/micoe/micoe_sex_bj_anim06.png"
image micoe_bj 7 = "characters/micoe/micoe_sex_bj_anim07.png"
image micoe_bj 8 = "characters/micoe/micoe_sex_bj_anim08.png"
image micoe_bj 9 = "characters/micoe/micoe_sex_bj_anim09.png"
image micoe_bj 10 = "characters/micoe/micoe_sex_bj_anim10.png"
image micoe_bj 11 = "characters/micoe/micoe_sex_bj_anim11.png"
image micoe_bj 12 = "characters/micoe/micoe_sex_bj_anim12.png"
image micoe_bj 13 = "characters/micoe/micoe_sex_bj_anim13.png"
image micoe_bj 14 = "characters/micoe/micoe_sex_bj_anim14.png"
image micoe_bj 15 = "characters/micoe/micoe_sex_bj_anim15.png"
image micoe_bj 16 = "characters/micoe/micoe_sex_bj_anim16.png"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
