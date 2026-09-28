init:
    $ consuela_clothing_options = ['b_empty','b_magic','b_naked_blank','b_dressed','b_naked','b_undies','b_lift','b_hospital','b_casual','b_casual_fear','b_dressed_pregnant_bump','b_dressed_pregnant_belly','b_naked_pregnant_belly','b_naked_pregnant_bump']

init python:


    renpy.image('consuela_arms_a_empty', 'ground.png')
    renpy.image('consuela_body_b_empty', 'ground.png')
    renpy.image('consuela_face_f_empty', 'ground.png')
    renpy.image('consuela_face_talk_f_empty', 'ground.png')


    renpy.image('consuela_face_talk_f_laugh', 'consuela_face_f_laugh')
    renpy.image('consuela_face_talk_f_yell', 'consuela_face_f_yell')
    renpy.image('consuela_face_talk_f_unsure', 'consuela_face_f_unsure')
    renpy.image('consuela_face_talk_f_singing', 'consuela_face_f_singing')
    renpy.image('consuela_face_talk_f_eyeroll', 'consuela_face_f_eyeroll')
    renpy.image('consuela_face_back_talk_f_laugh', 'consuela_face_back_f_laugh')




    renpy.image('consuela_body_b_naked_bend_jerk1', Fixed('consuela_body_b_naked_bend', 'consuela_arms_naked_bend_a_jerk1'))
    renpy.image('consuela_body_b_naked_bend_jerk2', Fixed('consuela_body_b_naked_bend', 'consuela_arms_naked_bend_a_jerk2'))

layeredimage consuela:

    yanchor config.screen_height
    ypos 1.
    xanchor config.screen_width
    xpos 1.


    group body auto:
        attribute b_dressed default
        attribute b_empty null
        attribute b_bending "consuela_body_b_bending"
        attribute b_magic "consuela_body_b_[M_consuela.outfit.get][M_consuela.pregnancy.to_string]"   
        attribute b_dressed_mop "consuela_body_b_dressed_mop"   
        attribute b_floor "consuela_body_b_floor_[M_consuela.outfit.get]"   
        attribute b_floor_base "consuela_body_b_floor_base_[M_consuela.outfit.get]"   
        attribute b_floor_cum "consuela_body_b_floor_cum_[M_consuela.outfit.get]"   
        attribute b_stairs "consuela_body_b_stairs_[M_consuela.outfit.get]"   
        attribute b_stairs_cum "consuela_body_b_stairs_cum_[M_consuela.outfit.get]"   
        attribute b_casual_kiss "consuela_body_b_casual_kiss"   
        attribute b_back_shake "consuela_body_b_back_shake"   
        attribute b_bend_jerk "consuela_body_b_bend_jerk"   
        attribute b_kiss "consuela_body_b_[M_consuela.outfit.get]_kiss"   
        attribute b_counter_cum "consuela_body_b_kitchen_cum_[M_consuela.outfit.get]"   
        attribute b_counter "consuela_body_b_kitchen_[M_consuela.outfit.get]"   
        attribute b_bj_cum "consuela_body_b_bj_cum_[M_consuela.outfit.get]"   
        attribute b_bj_talking "consuela_body_b_bj_talking_[M_consuela.outfit.get]"   
        attribute b_kiss10 "consuela_body_b_kiss10_shirt_[M_consuela.outfit.get]"   
        attribute b_bend "consuela_body_b_[M_consuela.outfit.get]_bend"   


    group mouth prefix 'm':
        attribute talk null

    group face:
        attribute f_normal default null







    group face if_not 'm_talk' if_any consuela_clothing_options auto


    group face if_not 'm_talk' if_any 'b_dressed_mop' auto:
        offset (-100, 78)


    group face if_not 'm_talk' if_any ['b_bend','b_bend_jerk'] auto:
        offset (-288, 124)


    group face if_not 'm_talk' if_all 'b_gown_bed' auto:
        offset (100, -12)






    group face if_not 'm_talk' if_any ['b_bj_talking'] auto variant 'bj'


    group face if_not 'm_talk' if_any ['b_floor_naked','b_floor'] auto variant 'floor'


    group face if_not 'm_talk' if_any ['b_stairs_naked','b_stairs'] auto variant 'stairs':
        attribute f_normal 'consuela_face_f_stairs_normal_down'


    group face if_not 'm_talk' if_any ['b_counter'] auto variant 'kitchen'


    group face if_not 'm_talk' if_any ['b_back','b_back_shake'] auto variant 'back'







    group face if_all 'm_talk' if_any consuela_clothing_options auto variant 'talk'


    group face if_all 'm_talk' if_any 'b_dressed_mop' auto variant 'talk':
        offset (-100, 78)


    group face if_all 'm_talk' if_any ['b_bend','b_bend_jerk'] auto variant 'talk':
        offset (-288, 124)


    group face if_all ['m_talk', 'b_gown_bed'] auto variant 'talk':
        offset (100, -12)






    group face if_all 'm_talk' if_any ['b_bj_talking'] auto variant 'bj_talk'


    group face if_all 'm_talk' if_any ['b_floor_naked','b_floor'] auto variant 'floor_talk'


    group face if_all 'm_talk' if_any ['b_stairs_naked','b_stairs'] auto variant 'stairs_talk':
        attribute f_normal 'consuela_face_talk_f_stairs_normal_down'


    group face if_all 'm_talk' if_any ['b_counter'] auto variant 'kitchen_talk'


    group face if_all 'm_talk' if_any ['b_back','b_back_shake'] auto variant 'back_talk'



    group arms if_all 'b_dressed' auto variant 'dressed':
        attribute a_idle default 'consuela_arms_dressed_a_hips'
        attribute a_baby "consuela_arms_dressed_a_baby_[M_consuela.pregnancy.baby_gender]"


    group arms if_all 'b_naked_blank' auto variant 'naked_blank':
        attribute a_idle default 'consuela_arms_naked_blank_a_boob'


    group arms if_all 'b_gown_bed' auto variant 'gown_bed':
        attribute a_idle default "consuela_arms_gown_bed_a_baby_[M_consuela.pregnancy.baby_gender]"


    group arms if_all 'b_magic' auto:
        attribute a_idle default 'consuela_arms_[M_consuela.outfit.get]_a_touch[M_consuela.pregnancy.to_string]'
        attribute a_hips 'consuela_arms_[M_consuela.outfit.get]_a_hips'
        attribute a_boobs 'consuela_arms_a_[M_consuela.outfit.get]_bump_boobs'
        attribute a_dick_big 'consuela_arms_[M_consuela.outfit.get]_a_dick_big'
        attribute a_work1 'consuela_arms_[M_consuela.outfit.get]_a_work1'
        attribute a_work2 'consuela_arms_[M_consuela.outfit.get]_a_work2'
        attribute a_work3 'consuela_arms_[M_consuela.outfit.get]_a_work3'
        attribute a_cloth 'consuela_arms_[M_consuela.outfit.get]_a_cloth'


    group arms if_all 'b_undies' auto variant 'undies':
        attribute a_idle default 'consuela_arms_undies_a_uniform_hold'


    group arms if_all 'b_casual' auto variant 'casual':
        attribute a_idle default 'consuela_arms_casual_a_hips'


    group arms if_all 'b_hospital' auto variant 'hospital':
        attribute a_idle default 'consuela_arms_hospital_a_hips'    


    group arms if_any ['b_naked'] auto variant 'naked':
        attribute a_idle default 'consuela_arms_naked_a_hips'


    group arms if_any ['b_bend'] auto:
        attribute a_idle default 'consuela_arms_[M_consuela.outfit.get]_bend_a_idle'
        attribute a_wipe 'consuela_arms_dressed_bend_a_wipe'
        attribute a_poke 'consuela_arms_[M_consuela.outfit.get]_bend_a_poke'
        attribute a_pull1 'consuela_arms_[M_consuela.outfit.get]_bend_a_pull1'
        attribute a_pull2 'consuela_arms_[M_consuela.outfit.get]_bend_a_pull2'


    group overlay auto:
        attribute o_empty default null

image consuela_f = "characters/consuela/consuela_face_f_normal.png"

image consuela_body_b_dressed_mop:
    Transform("characters/consuela/consuela_body_b_dressed_mop1.png")
    pause .4
    Transform("characters/consuela/consuela_body_b_dressed_mop2.png")
    pause .4
    repeat

image consuela_body_b_bending:
    Transform("characters/consuela/consuela_body_b_bending1.png")
    pause .4
    Transform("characters/consuela/consuela_body_b_bending2.png")
    pause .4
    repeat

image consuela_body_b_casual_kiss:
    Transform("characters/consuela/consuela_body_b_casual_kiss1.png")
    pause .4
    Transform("characters/consuela/consuela_body_b_casual_kiss2.png")
    pause .4
    repeat

image consuela_body_b_dressed_kiss:
    Transform("characters/consuela/consuela_body_b_kiss3.png")
    pause .4
    Transform("characters/consuela/consuela_body_b_kiss4.png")
    pause .4
    repeat

image consuela_body_b_naked_kiss:
    Transform("characters/consuela/consuela_body_b_kiss6.png")
    pause .4
    Transform("characters/consuela/consuela_body_b_kiss7.png")
    pause .4
    repeat

image consuela_body_b_hospital_kiss:
    Transform("characters/consuela/consuela_body_b_kiss8.png")
    pause .4
    Transform("characters/consuela/consuela_body_b_kiss9.png")
    pause .4
    repeat

image consuela_body_b_back_shake:
    Transform("characters/consuela/consuela_body_b_back_shake1.png")
    pause .4
    Transform("characters/consuela/consuela_body_b_back_shake2.png")
    pause .4
    repeat

image consuela_arms_dressed_bend_a_wipe:
    Transform("characters/consuela/consuela_arms_dressed_bend_a_wipe1.png")
    pause .4
    Transform("characters/consuela/consuela_arms_dressed_bend_a_wipe2.png")
    pause .4
    repeat

image consuela_body_b_bend_jerk:
    Transform("consuela_body_b_[M_consuela.outfit.get]_bend_jerk1")
    pause .4
    Transform("consuela_body_b_[M_consuela.outfit.get]_bend_jerk2")
    pause .4
    repeat

image consuela_arms_naked_blank_a_boob:
    Transform("characters/consuela/consuela_arms_naked_blank_a_boob1.png")
    pause .4
    Transform("characters/consuela/consuela_arms_naked_blank_a_boob2.png")
    pause .4
    repeat




image consuela_mc_body_floor base = "consuela_mc_body_b_floor_base"
image consuela_mc_body_floor insert_pullout = "consuela_mc_body_b_floor_insert_pullout"

image consuela_mc_dick_floor pre = "consuela_mc_body_b_dick_floor_pre"
image consuela_mc_dick_floor after = "consuela_mc_body_b_dick_floor_after"
image consuela_mc_dick_floor cumshot:
    Transform("characters/consuela/consuela_mc_body_b_dick_floor_cumshot1.png")
    pause .4
    Transform("characters/consuela/consuela_mc_body_b_dick_floor_cumshot2.png")
    pause .4
    Transform("characters/consuela/consuela_mc_body_b_dick_floor_cumshot3.png")

image consuela_floor 1 = "consuela_body_b_floor_anim01"
image consuela_floor 2 = "consuela_body_b_floor_anim02"
image consuela_floor 3 = "consuela_body_b_floor_anim03"
image consuela_floor 4 = "consuela_body_b_floor_anim04"
image consuela_floor 5 = "consuela_body_b_floor_anim05"
image consuela_floor 6 = "consuela_body_b_floor_anim06"
image consuela_floor 7 = "consuela_body_b_floor_anim07"

image consuela_floor_naked 1 = "consuela_body_b_floor_anim01_naked"
image consuela_floor_naked 2 = "consuela_body_b_floor_anim02_naked"
image consuela_floor_naked 3 = "consuela_body_b_floor_anim03_naked"
image consuela_floor_naked 4 = "consuela_body_b_floor_anim04_naked"
image consuela_floor_naked 5 = "consuela_body_b_floor_anim05_naked"
image consuela_floor_naked 6 = "consuela_body_b_floor_anim06_naked"
image consuela_floor_naked 7 = "consuela_body_b_floor_anim07_naked"


image consuela_mc_body_floor insert_pullout_anal = "consuela_mc_body_b_floor_insert_pullout_anal"

image consuela_floor_anal 1 = "consuela_body_b_floor_anim01_anal"
image consuela_floor_anal 2 = "consuela_body_b_floor_anim02_anal"
image consuela_floor_anal 3 = "consuela_body_b_floor_anim03_anal"
image consuela_floor_anal 4 = "consuela_body_b_floor_anim04_anal"
image consuela_floor_anal 5 = "consuela_body_b_floor_anim05_anal"
image consuela_floor_anal 6 = "consuela_body_b_floor_anim06_anal"
image consuela_floor_anal 7 = "consuela_body_b_floor_anim07_anal"

image consuela_floor_anal_naked 1 = "consuela_body_b_floor_anim01_anal_naked"
image consuela_floor_anal_naked 2 = "consuela_body_b_floor_anim02_anal_naked"
image consuela_floor_anal_naked 3 = "consuela_body_b_floor_anim03_anal_naked"
image consuela_floor_anal_naked 4 = "consuela_body_b_floor_anim04_anal_naked"
image consuela_floor_anal_naked 5 = "consuela_body_b_floor_anim05_anal_naked"
image consuela_floor_anal_naked 6 = "consuela_body_b_floor_anim06_anal_naked"
image consuela_floor_anal_naked 7 = "consuela_body_b_floor_anim07_anal_naked"


image consuela_mc_body_stairs base = "consuela_mc_body_b_stairs_base"
image consuela_mc_body_stairs cumshot = "consuela_mc_body_b_stairs_cumshot"
image consuela_mc_body_stairs insert_pullout = "consuela_mc_body_b_stairs_insert"

image consuela_mc_dick_stairs pre = "consuela_mc_body_b_dick_stairs_pre"

image consuela_mc_dick_stairs cumshot:
    Transform("characters/consuela/consuela_mc_body_b_dick_stairs_cumshot1.png")
    pause .4
    Transform("characters/consuela/consuela_mc_body_b_dick_stairs_cumshot2.png")
    pause .4
    Transform("characters/consuela/consuela_mc_body_b_dick_stairs_cumshot3.png")

image consuela_stairs 1 = "consuela_body_b_stairs_anim01"
image consuela_stairs 2 = "consuela_body_b_stairs_anim02"
image consuela_stairs 3 = "consuela_body_b_stairs_anim03"
image consuela_stairs 4 = "consuela_body_b_stairs_anim04"
image consuela_stairs 5 = "consuela_body_b_stairs_anim05"
image consuela_stairs 6 = "consuela_body_b_stairs_anim06"
image consuela_stairs 7 = "consuela_body_b_stairs_anim07"

image consuela_stairs_naked 1 = "consuela_body_b_stairs_anim01_naked"
image consuela_stairs_naked 2 = "consuela_body_b_stairs_anim02_naked"
image consuela_stairs_naked 3 = "consuela_body_b_stairs_anim03_naked"
image consuela_stairs_naked 4 = "consuela_body_b_stairs_anim04_naked"
image consuela_stairs_naked 5 = "consuela_body_b_stairs_anim05_naked"
image consuela_stairs_naked 6 = "consuela_body_b_stairs_anim06_naked"
image consuela_stairs_naked 7 = "consuela_body_b_stairs_anim07_naked"


image consuela_mc_body_kitchen base = "consuela_mc_body_b_kitchen_base"
image consuela_mc_body_kitchen cumshot = "consuela_mc_body_b_kitchen_cumshot"
image consuela_mc_body_kitchen insert_pullout = "consuela_mc_body_b_kitchen_insert"

image consuela_mc_dick_kitchen pre = "consuela_mc_body_b_dick_kitchen_pre"
image consuela_mc_dick_kitchen after = "consuela_mc_body_b_dick_kitchen_after"
image consuela_mc_dick_kitchen cumshot:
    Transform("characters/consuela/consuela_mc_body_b_dick_kitchen_cumshot1.png")
    pause .4
    Transform("characters/consuela/consuela_mc_body_b_dick_kitchen_cumshot2.png")
    pause .4
    Transform("characters/consuela/consuela_mc_body_b_dick_kitchen_cumshot3.png")

image consuela_kitchen 1 = "consuela_body_b_kitchen_anim01"
image consuela_kitchen 2 = "consuela_body_b_kitchen_anim02"
image consuela_kitchen 3 = "consuela_body_b_kitchen_anim03"
image consuela_kitchen 4 = "consuela_body_b_kitchen_anim04"
image consuela_kitchen 5 = "consuela_body_b_kitchen_anim05"
image consuela_kitchen 6 = "consuela_body_b_kitchen_anim06"
image consuela_kitchen 7 = "consuela_body_b_kitchen_anim07"

image consuela_kitchen_naked 1 = "consuela_body_b_kitchen_anim01_naked"
image consuela_kitchen_naked 2 = "consuela_body_b_kitchen_anim02_naked"
image consuela_kitchen_naked 3 = "consuela_body_b_kitchen_anim03_naked"
image consuela_kitchen_naked 4 = "consuela_body_b_kitchen_anim04_naked"
image consuela_kitchen_naked 5 = "consuela_body_b_kitchen_anim05_naked"
image consuela_kitchen_naked 6 = "consuela_body_b_kitchen_anim06_naked"
image consuela_kitchen_naked 7 = "consuela_body_b_kitchen_anim07_naked"


image consuela_bj 1 = "consuela_body_b_bj_anim01"
image consuela_bj 2 = "consuela_body_b_bj_anim02"
image consuela_bj 3 = "consuela_body_b_bj_anim03"
image consuela_bj 4 = "consuela_body_b_bj_anim04"
image consuela_bj 5 = "consuela_body_b_bj_anim05"
image consuela_bj 6 = "consuela_body_b_bj_anim06"
image consuela_bj 7 = "consuela_body_b_bj_anim07"
image consuela_bj 8 = "consuela_body_b_bj_anim08"
image consuela_bj 9 = "consuela_body_b_bj_anim09"
image consuela_bj 10 = "consuela_body_b_bj_anim10"
image consuela_bj 11 = "consuela_body_b_bj_anim11"
image consuela_bj 12 = "consuela_body_b_bj_anim12"

image consuela_bj_naked 1 = "consuela_body_b_bj_anim01_naked"
image consuela_bj_naked 2 = "consuela_body_b_bj_anim02_naked"
image consuela_bj_naked 3 = "consuela_body_b_bj_anim03_naked"
image consuela_bj_naked 4 = "consuela_body_b_bj_anim04_naked"
image consuela_bj_naked 5 = "consuela_body_b_bj_anim05_naked"
image consuela_bj_naked 6 = "consuela_body_b_bj_anim06_naked"
image consuela_bj_naked 7 = "consuela_body_b_bj_anim07_naked"
image consuela_bj_naked 8 = "consuela_body_b_bj_anim08_naked"
image consuela_bj_naked 9 = "consuela_body_b_bj_anim09_naked"
image consuela_bj_naked 10 = "consuela_body_b_bj_anim10_naked"
image consuela_bj_naked 11 = "consuela_body_b_bj_anim11_naked"
image consuela_bj_naked 12 = "consuela_body_b_bj_anim12_naked"





image xray_consuela stairs:
    Transform("characters/xray/xray_side_01.png", xzoom=-0.7, yzoom=.7, rotate=10, xoffset=270, yoffset=50)
    pause 0.4
    Transform("characters/xray/xray_side_02.png", xzoom=-0.7, yzoom=.7, rotate=10, xoffset=270, yoffset=50)
    pause 0.4
    Transform("characters/xray/xray_side_03.png", xzoom=-0.7, yzoom=.7, rotate=10, xoffset=270, yoffset=50)
    pause 0.4
    Transform("characters/xray/xray_side_04.png", xzoom=-0.7, yzoom=.7, rotate=10, xoffset=270, yoffset=50)
    pause 0.4
    Transform("characters/xray/xray_side_05.png", xzoom=-0.7, yzoom=.7, rotate=10, xoffset=270, yoffset=50)
    pause 0.4
    Transform("characters/xray/xray_side_06.png", xzoom=-0.7, yzoom=.7, rotate=10, xoffset=270, yoffset=50)
    pause 0.4
    Transform("characters/xray/xray_side_07.png", xzoom=-0.7, yzoom=.7, rotate=10, xoffset=270, yoffset=50)
    pause 0.4
    Transform("characters/xray/xray_side_08.png", xzoom=-0.7, yzoom=.7, rotate=10, xoffset=270, yoffset=50)
    pause 0.4
    Transform("characters/xray/xray_side_09.png", xzoom=-0.7, yzoom=.7, rotate=10, xoffset=270, yoffset=50)
    pause 0.4
    Transform("characters/xray/xray_side_10.png", xzoom=-0.7, yzoom=.7, rotate=10, xoffset=270, yoffset=50)
    pause 0.4
    Transform("characters/xray/xray_side_11.png", xzoom=-0.7, yzoom=.7, rotate=10, xoffset=270, yoffset=50)
    pause 0.4
    Transform("characters/xray/xray_side_12.png", xzoom=-0.7, yzoom=.7, rotate=10, xoffset=270, yoffset=50)
    pause 0.4
    Transform("characters/xray/xray_side_13.png", xzoom=-0.7, yzoom=.7, rotate=10, xoffset=270, yoffset=50)
    pause 0.4
    Transform("characters/xray/xray_side_14.png", xzoom=-0.7, yzoom=.7, rotate=10, xoffset=270, yoffset=50)
    pause 0.4
    Transform("characters/xray/xray_side_15.png", xzoom=-0.7, yzoom=.7, rotate=10, xoffset=270, yoffset=50)
    pause 0.4
    Transform("characters/xray/xray_side_16.png", xzoom=-0.7, yzoom=.7, rotate=10, xoffset=270, yoffset=50)
    pause 0.4
    Transform("characters/xray/xray_side_17.png", xzoom=-0.7, yzoom=.7, rotate=10, xoffset=270, yoffset=50)
    pause 0.4
    Transform("characters/xray/xray_side_18.png", xzoom=-0.7, yzoom=.7, rotate=10, xoffset=270, yoffset=50)
    pause 2.0
    linear 2.5 alpha 0

image xray_consuela floor:
    Transform("characters/xray/xray_side_01.png", xzoom=-0.8, yzoom=.8, rotate=70, xoffset=210, yoffset=-40)
    pause 0.4
    Transform("characters/xray/xray_side_02.png", xzoom=-0.8, yzoom=.8, rotate=70, xoffset=210, yoffset=-40)
    pause 0.4
    Transform("characters/xray/xray_side_03.png", xzoom=-0.8, yzoom=.8, rotate=70, xoffset=210, yoffset=-40)
    pause 0.4
    Transform("characters/xray/xray_side_04.png", xzoom=-0.8, yzoom=.8, rotate=70, xoffset=210, yoffset=-40)
    pause 0.4
    Transform("characters/xray/xray_side_05.png", xzoom=-0.8, yzoom=.8, rotate=70, xoffset=210, yoffset=-40)
    pause 0.4
    Transform("characters/xray/xray_side_06.png", xzoom=-0.8, yzoom=.8, rotate=70, xoffset=210, yoffset=-40)
    pause 0.4
    Transform("characters/xray/xray_side_07.png", xzoom=-0.8, yzoom=.8, rotate=70, xoffset=210, yoffset=-40)
    pause 0.4
    Transform("characters/xray/xray_side_08.png", xzoom=-0.8, yzoom=.8, rotate=70, xoffset=210, yoffset=-40)
    pause 0.4
    Transform("characters/xray/xray_side_09.png", xzoom=-0.8, yzoom=.8, rotate=70, xoffset=210, yoffset=-40)
    pause 0.4
    Transform("characters/xray/xray_side_10.png", xzoom=-0.8, yzoom=.8, rotate=70, xoffset=210, yoffset=-40)
    pause 0.4
    Transform("characters/xray/xray_side_11.png", xzoom=-0.8, yzoom=.8, rotate=70, xoffset=210, yoffset=-40)
    pause 0.4
    Transform("characters/xray/xray_side_12.png", xzoom=-0.8, yzoom=.8, rotate=70, xoffset=210, yoffset=-40)
    pause 0.4
    Transform("characters/xray/xray_side_13.png", xzoom=-0.8, yzoom=.8, rotate=70, xoffset=210, yoffset=-40)
    pause 0.4
    Transform("characters/xray/xray_side_14.png", xzoom=-0.8, yzoom=.8, rotate=70, xoffset=210, yoffset=-40)
    pause 0.4
    Transform("characters/xray/xray_side_15.png", xzoom=-0.8, yzoom=.8, rotate=70, xoffset=210, yoffset=-40)
    pause 0.4
    Transform("characters/xray/xray_side_16.png", xzoom=-0.8, yzoom=.8, rotate=70, xoffset=210, yoffset=-40)
    pause 0.4
    Transform("characters/xray/xray_side_17.png", xzoom=-0.8, yzoom=.8, rotate=70, xoffset=210, yoffset=-40)
    pause 0.4
    Transform("characters/xray/xray_side_18.png", xzoom=-0.8, yzoom=.8, rotate=70, xoffset=210, yoffset=-40)
    pause 2.0
    linear 2.5 alpha 0

image ll = "characters/xray/xray_left_back_01.png"

image xray_consuela counter:
    Transform("characters/xray/xray_left_back_01.png", xzoom=-0.5, yzoom=.5, rotate=-20, xoffset=370, yoffset=350)
    pause 0.4
    Transform("characters/xray/xray_left_back_02.png", xzoom=-0.5, yzoom=.5, rotate=-20, xoffset=370, yoffset=350)
    pause 0.4
    Transform("characters/xray/xray_left_back_03.png", xzoom=-0.5, yzoom=.5, rotate=-20, xoffset=370, yoffset=350)
    pause 0.4
    Transform("characters/xray/xray_left_back_04.png", xzoom=-0.5, yzoom=.5, rotate=-20, xoffset=370, yoffset=350)
    pause 0.4
    Transform("characters/xray/xray_left_back_05.png", xzoom=-0.5, yzoom=.5, rotate=-20, xoffset=370, yoffset=350)
    pause 0.4
    Transform("characters/xray/xray_left_back_06.png", xzoom=-0.5, yzoom=.5, rotate=-20, xoffset=370, yoffset=350)
    pause 0.4
    Transform("characters/xray/xray_left_back_07.png", xzoom=-0.5, yzoom=.5, rotate=-20, xoffset=370, yoffset=350)
    pause 0.4
    Transform("characters/xray/xray_left_back_08.png", xzoom=-0.5, yzoom=.5, rotate=-20, xoffset=370, yoffset=350)
    pause 0.4
    Transform("characters/xray/xray_left_back_09.png", xzoom=-0.5, yzoom=.5, rotate=-20, xoffset=370, yoffset=350)
    pause 0.4
    Transform("characters/xray/xray_left_back_10.png", xzoom=-0.5, yzoom=.5, rotate=-20, xoffset=370, yoffset=350)
    pause 0.4
    Transform("characters/xray/xray_left_back_11.png", xzoom=-0.5, yzoom=.5, rotate=-20, xoffset=370, yoffset=350)
    pause 0.4
    Transform("characters/xray/xray_left_back_12.png", xzoom=-0.5, yzoom=.5, rotate=-20, xoffset=370, yoffset=350)
    pause 0.4
    Transform("characters/xray/xray_left_back_13.png", xzoom=-0.5, yzoom=.5, rotate=-20, xoffset=370, yoffset=350)
    pause 0.4
    Transform("characters/xray/xray_left_back_14.png", xzoom=-0.5, yzoom=.5, rotate=-20, xoffset=370, yoffset=350)
    pause 0.4
    Transform("characters/xray/xray_left_back_15.png", xzoom=-0.5, yzoom=.5, rotate=-20, xoffset=370, yoffset=350)
    pause 0.4
    Transform("characters/xray/xray_left_back_16.png", xzoom=-0.5, yzoom=.5, rotate=-20, xoffset=370, yoffset=350)
    pause 0.4
    Transform("characters/xray/xray_left_back_17.png", xzoom=-0.5, yzoom=.5, rotate=-20, xoffset=370, yoffset=350)
    pause 0.4
    Transform("characters/xray/xray_left_back_18.png", xzoom=-0.5, yzoom=.5, rotate=-20, xoffset=370, yoffset=350)
    pause 2.0
    linear 2.5 alpha 0
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
