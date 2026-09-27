











init:
    $ diane_clothing_options = ['b_empty','b_dressed','b_topless_pregnant_belly','b_topless_blank2','b_topless_blank','b_topless','b_shirtless_pull','b_shirtless_pregnant_bump','b_shirtless_pregnant_belly','b_shirtless','b_nightgown_remove2','b_nightgown_remove1','b_nightgown_pregnant_bump','b_nightgown_pregnant_belly','b_nightgown_hug1','b_nightgown','b_naked_pregnant_bump','b_naked_pregnant_belly','b_naked','b_lingerie','b_kitchen','b_hug_deb_robe','b_hug_deb','b_gown_dress','b_gown','b_dressed_wet','b_cow_pregnant_bump','b_cow_pregnant_belly','b_cow','b_classy','b_casual_remove5','b_casual_bag_hug','b_casual']

init python:


    renpy.image('diane_arms_a_empty', 'ground.png')
    renpy.image('diane_body_b_empty', 'ground.png')
    renpy.image('diane_face_f_empty', 'ground.png')
    renpy.image('diane_face_talk_f_empty', 'ground.png')


    renpy.image('diane_face_talk_f_laugh', 'diane_face_f_laugh')
    renpy.image('diane_face_talk_f_surprised', 'diane_face_f_surprised')
    renpy.image('diane_face_talk_f_teasing_look', 'diane_face_f_teasing_look')
    renpy.image('diane_face_talk_f_reading_intrigued', 'diane_face_f_reading_intrigued')
    renpy.image('diane_face_talk_f_thinking', 'diane_face_f_thinking')
    renpy.image('diane_face_talk_f_surprised_front', 'diane_face_f_surprised_front')
    renpy.image('diane_face_talk_f_thinking_back', 'diane_face_f_thinking_back')
    renpy.image('diane_face_talk_f_scream', 'diane_face_f_scream')
    renpy.image('diane_face_talk_f_teasing', 'diane_face_f_teasing')
    renpy.image('diane_face_talk_f_lookup', 'diane_face_f_lookup')
    renpy.image('diane_face_talk_f_laugh_blush', 'diane_face_f_laugh_blush')
    renpy.image('diane_face_talk_f_tired_down', 'diane_face_f_tired_down')
    renpy.image('diane_face_talk_f_surprised_down', 'diane_face_f_surprised_down')
    renpy.image('diane_face_talk_f_lip_bite', 'diane_face_f_lip_bite')
    renpy.image('diane_face_dinner_talk_f_laugh', 'diane_face_dinner_f_laugh')
    renpy.image('diane_face_talk_f_reading_blushing', 'diane_face_f_reading_blushing')
    renpy.image('diane_face_talk_f_reading_lip_bite', 'diane_face_f_reading_lip_bite')
    renpy.image('diane_face_talk_f_cheese', 'diane_face_f_cheese')


    renpy.image('diane_face_f_shamed_look_closed', 'diane_face_talk_f_shamed_look_closed')
    renpy.image('diane_face_f_shamed_smile', 'diane_face_talk_f_shamed_smile')
    renpy.image('diane_face_f_scared_back', 'diane_face_talk_f_scared_back')
    renpy.image('diane_face_f_shamed_look', 'diane_face_talk_f_shamed_look')

layeredimage diane:

    yanchor config.screen_height
    ypos 1.
    xanchor config.screen_width
    xpos 1.


    group body auto:
        attribute b_dressed default "characters/diane/layeredimage/diane_body_b_dressed[M_diane.pregnancy.to_string].png"
        attribute b_naked "characters/diane/layeredimage/diane_body_b_[M_diane.outfit.get][M_diane.pregnancy.to_string].png"   
        attribute b_nightgown "characters/diane/layeredimage/diane_body_b_nightgown[M_diane.pregnancy.to_string].png"
        attribute b_shirtless "characters/diane/layeredimage/diane_body_b_shirtless[M_diane.pregnancy.to_string].png"
        attribute b_nightgown_sit "characters/diane/layeredimage/diane_body_b_nightgown_sit[M_diane.pregnancy.to_string].png"
        attribute b_pull_mc_naked "characters/diane/layeredimage/diane_body_b_pull_mc_[M_diane.outfit.get].png"        
        attribute b_laying_grope "diane_body_b_laying_grope"        

        attribute b_jerk "diane_body_b_jerk"

        attribute b_hay_feeding1 "characters/diane/layeredimage/diane_body_b_hay_feeding_[M_diane.outfit.get]1.png"
        attribute b_hay_feeding "diane_body_b_hay_feeding"

        attribute b_hay_feeding_shirtless "diane_body_b_hay_feeding_shirtless"

        attribute b_nightgown_sit_stroke "diane_body_b_nightgown_sit_stroke"

        attribute b_hay_rub "diane_body_b_hay_rub"

        attribute b_hay_stroke "diane_body_b_hay_stroke"

        attribute b_hay_cucumber1 "characters/diane/layeredimage/diane_body_b_hay_cucumber1_[M_diane.outfit.get].png"
        attribute b_hay_cucumber2 "characters/diane/layeredimage/diane_body_b_hay_cucumber2_[M_diane.outfit.get].png"
        attribute b_hay_sit "characters/diane/layeredimage/diane_body_b_hay_[M_diane.outfit.get].png"
        attribute b_topless "diane_body_b_topless[M_diane.pregnancy.to_string]"

        attribute b_empty null


        attribute b_kiss_shirtless Image("characters/diane/layeredimage/diane_body_b_kiss_shirtless.png",xoffset=-217)
        attribute b_kiss_casual Image("characters/diane/layeredimage/diane_body_b_kiss_casual.png",xoffset=-217)
        attribute b_kiss_mouth Image("characters/diane/layeredimage/diane_body_b_kiss_mouth.png",xoffset=-172)
        attribute b_kiss_naked "characters/diane/layeredimage/diane_body_b_kiss_[M_diane.outfit.get].png" 
        attribute b_kiss_both_naked "diane_kiss_keduanya_telanjang[M_diane.pregnancy.to_string]" 

        attribute b_lingerie_kiss Image("characters/diane/layeredimage/diane_body_b_lingerie_kiss.png",xoffset=-124)
        attribute b_hug_vero_talk Image("characters/diane/layeredimage/diane_body_b_hug_vero_talk.png",xoffset=-235)
        attribute b_dinner_hug1 Image("characters/diane/layeredimage/diane_body_b_dinner_hug1.png",xoffset=-125)
        attribute b_dinner_hug2 Image("characters/diane/layeredimage/diane_body_b_dinner_hug2.png",xoffset=-125)
        attribute b_dinner_hug3 Image("characters/diane/layeredimage/diane_body_b_dinner_hug3.png",xoffset=282)
        attribute b_dinner_hug4 Image("characters/diane/layeredimage/diane_body_b_dinner_hug4.png",xoffset=282)
        attribute b_nightgown_hug2 Image("characters/diane/layeredimage/diane_body_b_nightgown_hug2.png",xoffset=-360)
        attribute b_nightgown_hug3 Image("characters/diane/layeredimage/diane_body_b_nightgown_hug3.png",xoffset=-360)
        attribute b_nightgown_hug4 Image("characters/diane/layeredimage/diane_body_b_nightgown_hug4.png",xoffset=-360)
        attribute b_dream1 Image("characters/diane/layeredimage/diane_body_b_dream1.png",xoffset=250,yoffset=-140)
        attribute b_dream2 Image("characters/diane/layeredimage/diane_body_b_dream2.png",xoffset=250,yoffset=-140)
        attribute b_hay_behind_pre "characters/diane/layeredimage/diane_body_b_hay_behind_pre_[M_diane.outfit.get].png"
        attribute b_hay_behind "characters/diane/layeredimage/diane_body_b_hay_behind_[M_diane.outfit.get].png"
        attribute b_hay_behind_talk "characters/diane/layeredimage/diane_body_b_hay_behind_talk_[M_diane.outfit.get].png"
        attribute b_hay_insert1 "characters/diane/layeredimage/diane_body_b_hay_insert1_[M_diane.outfit.get].png"
        attribute b_laying_massage_back "diane_body_b_laying_massage_back"

        attribute b_laying_massage_naked_back "diane_body_b_laying_massage_naked_back"

        attribute b_laying_massage_butt "diane_body_b_laying_massage_butt"


        attribute b_laying_getup Image("characters/diane/layeredimage/diane_body_b_laying_getup.png",yoffset=30)
        attribute b_laying_kick Image("characters/diane/layeredimage/diane_body_b_laying_kick.png",yoffset=30)
        attribute b_laying_massage1 Image("characters/diane/layeredimage/diane_body_b_laying_massage1.png",yoffset=30)
        attribute b_laying_massage2 Image("characters/diane/layeredimage/diane_body_b_laying_massage2.png",yoffset=30)
        attribute b_laying_massage3 Image("characters/diane/layeredimage/diane_body_b_laying_massage3.png",yoffset=30)
        attribute b_laying_massage4 Image("characters/diane/layeredimage/diane_body_b_laying_massage4.png",yoffset=30)
        attribute b_laying_massage5 Image("characters/diane/layeredimage/diane_body_b_laying_massage5.png",yoffset=30)
        attribute b_laying_remove1 Image("characters/diane/layeredimage/diane_body_b_laying_remove1.png",yoffset=30)
        attribute b_laying_remove2 Image("characters/diane/layeredimage/diane_body_b_laying_remove2.png",yoffset=30)
        attribute b_laying1 Image("characters/diane/layeredimage/diane_body_b_laying1.png",yoffset=30)
        attribute b_laying2 Image("characters/diane/layeredimage/diane_body_b_laying2.png",yoffset=30)
        attribute b_laying3 Image("characters/diane/layeredimage/diane_body_b_laying3.png",yoffset=30)
        attribute b_laying4 Image("characters/diane/layeredimage/diane_body_b_laying4.png",yoffset=30)
        attribute b_laying5 Image("characters/diane/layeredimage/diane_body_b_laying5.png",yoffset=30)


    group mouth prefix 'm':
        attribute talk null

    group face:
        attribute f_normal default null







    group face if_not 'm_talk' if_any diane_clothing_options auto


    group face if_not 'm_talk' if_any ['b_front_couch_watching'] auto:
        xzoom -1
        offset (308, -97)


    group face if_not 'm_talk' if_any ['b_pole_point','b_pole'] auto:
        offset (-72, -88)


    group face if_not 'm_talk' if_any ['b_laying_grope','b_laying_grope2','b_laying_grope1','b_laying_back_shirtless','b_laying_back_naked'] auto:
        offset (-34, 184)


    group face if_not 'm_talk' if_any ['b_laying_sitting_topless','b_laying_sitting_naked'] auto:
        offset (-165, 62)


    group face if_not 'm_talk' if_any ['b_hay_dressed','b_hay_sit','b_hay_cucumber1','b_hay_cucumber2','b_hay_rub','b_hay_stroke','b_hay_naked','b_hay_undress2','b_hay_undress1','b_hay_stroke2_naked','b_hay_stroke1_naked','b_hay_stroke2_cow','b_hay_stroke1_cow','b_hay_rub2_naked','b_hay_rub1_naked','b_hay_rub2_cow','b_hay_rub1_cow','b_hay_feeding_shirtless','b_hay_feeding1','b_hay_feeding','b_hay_feeding_shirtless2','b_hay_feeding_shirtless1','b_hay_feeding_naked2','b_hay_feeding_naked1','b_hay_feeding_cow2','b_hay_feeding_cow1'] auto:
        xzoom -1
        offset (-43, -126)


    group face if_not 'm_talk' if_any ['b_jerk','b_jerk_pre','b_jerk1','b_jerk2'] auto:
        offset (-114, 192)


    group face if_not 'm_talk' if_any ['b_nightgown_sit','b_naked_sit'] auto:
        offset (-82, -40)


    group face if_not 'm_talk' if_any ['b_nightgown_undress'] auto:
        offset (36, -68)


    group face if_not 'm_talk' if_any ['b_nightgown_undress2'] auto:
        offset (118, -20)


    group face if_not 'm_talk' if_any ['b_nightgown_sit_stroke2','b_nightgown_sit_stroke1','b_nightgown_sit_stroke'] auto:
        offset (-94, -28)


    group face if_not 'm_talk' if_any ['b_couch_boob','b_couch'] auto:
        offset (85, -88)


    group face if_not 'm_talk' if_any ['b_gown_bed'] auto:
        offset (126, 72)






    group face if_not 'm_talk' if_any ['b_dinner_open','b_dinner'] auto variant 'dinner'







    group face if_all 'm_talk' if_any diane_clothing_options auto variant 'talk'


    group face if_all 'm_talk' if_any ['b_front_couch_watching'] auto variant 'talk':
        xzoom -1
        offset (308, -97)


    group face if_all 'm_talk' if_any ['b_pole_point','b_pole'] auto variant 'talk':
        offset (-72, -88)


    group face if_all 'm_talk' if_any ['b_laying_grope','b_laying_grope2','b_laying_grope1','b_laying_back_shirtless','b_laying_back_naked'] auto variant 'talk':
        offset (-34, 184)


    group face if_all 'm_talk' if_any ['b_laying_sitting_topless','b_laying_sitting_naked'] auto variant 'talk':
        offset (-165, 62)


    group face if_all 'm_talk' if_any ['b_hay_dressed','b_hay_sit','b_hay_cucumber1','b_hay_cucumber2','b_hay_rub','b_hay_stroke','b_hay_naked','b_hay_undress2','b_hay_undress1','b_hay_stroke2_naked','b_hay_stroke1_naked','b_hay_stroke2_cow','b_hay_stroke1_cow','b_hay_rub2_naked','b_hay_rub1_naked','b_hay_rub2_cow','b_hay_rub1_cow','b_hay_feeding_shirtless','b_hay_feeding1','b_hay_feeding','b_hay_feeding_shirtless2','b_hay_feeding_shirtless1','b_hay_feeding_naked2','b_hay_feeding_naked1','b_hay_feeding_cow2','b_hay_feeding_cow1'] auto variant 'talk':
        xzoom -1
        offset (-43, -126)


    group face if_all 'm_talk' if_any ['b_jerk','b_jerk_pre','b_jerk1','b_jerk2'] auto variant 'talk':
        offset (-114, 192)


    group face if_all 'm_talk' if_any ['b_nightgown_sit','b_naked_sit'] auto variant 'talk':
        offset (-82, -40)


    group face if_all 'm_talk' if_any ['b_nightgown_undress'] auto variant 'talk':
        offset (36, -68)


    group face if_all 'm_talk' if_any ['b_nightgown_undress2'] auto variant 'talk':
        offset (118, -20)


    group face if_all 'm_talk' if_any ['b_nightgown_sit_stroke2','b_nightgown_sit_stroke1','b_nightgown_sit_stroke'] auto variant 'talk':
        offset (-94, -28)


    group face if_all 'm_talk' if_any ['b_couch_boob','b_couch'] auto variant 'talk':
        offset (85, -88)


    group face if_all 'm_talk' if_any ['b_gown_bed'] auto variant 'talk':
        offset (126, 72)






    group face if_all 'm_talk' if_any ['b_dinner_open','b_dinner'] auto variant 'dinner_talk'


    group overlay auto:
        attribute o_empty default null


    group arms:
        attribute a_empty null


    group arms if_any ['b_dressed','b_dressed_wet'] auto variant 'dressed':
        attribute a_idle default "characters/diane/layeredimage/diane_arms_dressed_a_sides[M_diane.pregnancy.to_string].png"
        attribute a_cucumber_rub "diane_arms_dressed_a_cucumber_rub"



    group arms if_any ['b_naked'] auto variant 'naked':
        attribute a_idle default "diane_arms_[M_diane.outfit.get]_a_sides[M_diane.pregnancy.to_string]"

        attribute a_shovel_sides "diane_arms_[M_diane.outfit.get]_a_shovel_sides"

        attribute a_touch_belly "diane_arms_[M_diane.outfit.get]_a_touch[M_diane.pregnancy.to_string]"

        attribute a_touch_cum "characters/diane/layeredimage/diane_arms_[M_diane.outfit.get]_a_touch_cum.png"
        attribute a_lick_cum "characters/diane/layeredimage/diane_arms_[M_diane.outfit.get]_a_lick_cum.png"
        attribute a_squeeze3 "diane_arms_[M_diane.outfit.get]_a_squeeze3[M_diane.pregnancy.to_string]"

        attribute a_bottle1 "diane_arms_[M_diane.outfit.get]_a_bottle1[M_diane.pregnancy.to_string]"

        attribute a_statue_full "characters/diane/layeredimage/diane_arms_[M_diane.outfit.get]_a_statue_full.png"
        attribute a_nudge "characters/diane/layeredimage/diane_arms_[M_diane.outfit.get]_a_nudge.png"
        attribute a_shock "characters/diane/layeredimage/diane_arms_shirtless_a_shock.png"
        attribute a_check "characters/diane/layeredimage/diane_arms_cow_a_check.png"
        attribute a_milk_cups "diane_arms_[M_diane.outfit.get]_a_milk_cups[M_diane.pregnancy.to_belly_string]"

        attribute a_milk_cups_give "diane_arms_[M_diane.outfit.get]_a_milk_cups_give[M_diane.pregnancy.to_belly_string]"

        attribute a_take "diane_arms_[M_diane.outfit.get]_a_take[M_diane.pregnancy.to_belly_string]"



    group arms if_any ['b_shirtless_pull','b_shirtless'] auto variant 'shirtless':
        attribute a_idle default "diane_arms_shirtless_a_sides[M_diane.pregnancy.to_string]"

        attribute a_wave "diane_arms_shirtless_a_wave"

        attribute a_cover "diane_arms_shirtless_a_cover[M_diane.pregnancy.to_string]"

        attribute a_vase1 "diane_arms_shirtless_a_vase1[M_diane.pregnancy.to_string]"

        attribute a_vase2 "diane_arms_shirtless_a_vase2[M_diane.pregnancy.to_string]"



    group arms if_any ['b_topless'] auto variant 'topless':
        attribute a_idle default "diane_arms_naked_a_sides[M_diane.pregnancy.to_string]"

        attribute a_squeeze3 "diane_arms_[M_diane.outfit.get]_a_squeeze3[M_diane.pregnancy.to_string]"

        attribute a_bottle1 "diane_arms_[M_diane.outfit.get]_a_bottle1[M_diane.pregnancy.to_string]"



    group arms if_any ['b_topless_blank','b_topless_blank2'] auto variant 'topless_blank':
        attribute a_idle default 'diane_arms_topless_blank_a_waiting'
        attribute a_squeeze "diane_arms_topless_blank_a_squeeze"

        attribute a_pump "diane_arms_topless_a_pump"



    group arms if_any ['b_lingerie'] auto variant 'lingerie':
        attribute a_idle default 'diane_arms_lingerie_a_sides'
        attribute a_shock Image("characters/diane/layeredimage/diane_arms_shirtless_a_shock.png",yoffset=13)


    group arms if_any ['b_laying_grope','b_laying_grope2','b_laying_grope1','b_laying_back_shirtless','b_laying_back_naked'] auto variant 'laying':
        attribute a_idle default 'diane_arms_laying_a_laydown'
        attribute a_drink "characters/diane/layeredimage/diane_arms_laying_a_[drink_made]_drink.png"     
        attribute a_drink_sip "characters/diane/layeredimage/diane_arms_laying_a_[drink_made]_drink_sip.png"
        attribute a_wave "diane_arms_laying_a_wave"



    group arms if_all 'b_gown_bed' auto variant 'gown_bed':
        attribute a_idle default 'diane_arms_gown_bed_a_side'
        attribute a_baby "characters/diane/layeredimage/diane_arms_gown_bed_a_baby_[M_diane.pregnancy.baby_gender].png"


    group arms if_all 'b_gown' auto variant 'gown':
        attribute a_idle default 'diane_arms_gown_a_sides'


    group arms if_any ['b_dinner_open','b_dinner'] auto variant 'dinner':
        attribute a_idle default 'diane_arms_dinner_a_normal'
        attribute a_touch "diane_arms_dinner_a_touch"



    group arms if_all 'b_cow' auto variant 'cow':
        attribute a_idle default "diane_arms_cow_a_sides[M_diane.pregnancy.to_string]"



    group arms if_any ['b_couch','b_couch_boob'] auto variant 'couch':
        attribute a_idle default 'diane_arms_couch_a_reading'


    group arms if_all 'b_classy' auto variant 'classy':
        attribute a_idle default 'diane_arms_classy_a_sides'


    group arms if_all 'b_casual' auto variant 'casual':
        attribute a_idle default 'diane_arms_casual_a_sides'
        attribute a_baby "characters/diane/layeredimage/diane_arms_casual_a_baby_[M_diane.pregnancy.baby_gender].png"


    group arms if_all 'b_nightgown' auto variant 'nightgown':
        attribute a_idle default "diane_arms_nightgown_a_sides[M_diane.pregnancy.to_string]"

        attribute a_water "diane_arms_baju tidur_a_water[M_diane.pregnancy.to_string]"



    group arms if_any ['b_hay_feeding1','b_hay_feeding','b_hay_feeding_shirtless','b_hay_feeding_shirtless2','b_hay_feeding_shirtless1','b_hay_feeding_naked2','b_hay_feeding_naked1','b_hay_feeding_cow2','b_hay_feeding_cow1'] auto variant 'hay_feeding':
        attribute a_idle default null
        attribute a_stroke "diane_arms_hay_feeding_a_stroke"

        attribute a_shirtless_stroke "diane_arms_hay_feeding_a_shirtless_stroke"



layeredimage diane deb0m_post:
    group mouth prefix 'm':
        attribute talk null

    group face if_not 'm_talk' auto
    group face if_all 'm_talk' auto variant 'talk':
        attribute f_calm_close default


image diane_f = "characters/diane/layeredimage/diane_face_f_normal.png"


image diane_arms_naked_a_sides_pregnant_belly = "characters/diane/layeredimage/diane_arms_naked_a_sides_pregnant_belly.png"
image diane_arms_naked_a_sides_pregnant_bump = "characters/diane/layeredimage/diane_arms_naked_a_sides.png"
image diane_arms_naked_a_sides = "characters/diane/layeredimage/diane_arms_naked_a_sides.png"

image diane_arms_cow_a_sides_pregnant_belly = "characters/diane/layeredimage/diane_arms_cow_a_sides_pregnant_belly.png"
image diane_arms_cow_a_sides_pregnant_bump = "characters/diane/layeredimage/diane_arms_cow_a_sides.png"
image diane_arms_cow_a_sides = "characters/diane/layeredimage/diane_arms_cow_a_sides.png"

image diane_arms_shirtless_a_sides_pregnant_belly = "characters/diane/layeredimage/diane_arms_shirtless_a_sides_pregnant_belly.png"
image diane_arms_shirtless_a_sides_pregnant_bump = "characters/diane/layeredimage/diane_arms_shirtless_a_sides.png"
image diane_arms_shirtless_a_sides = "characters/diane/layeredimage/diane_arms_shirtless_a_sides.png"

image diane_arms_naked_a_touch_pregnant_belly = "characters/diane/layeredimage/diane_arms_naked_a_touch_pregnant_belly.png"
image diane_arms_naked_a_touch_pregnant_bump = "characters/diane/layeredimage/diane_arms_naked_a_touch_pregnant_bump.png"
image diane_arms_naked_a_touch = "characters/diane/layeredimage/diane_arms_naked_a_touch.png"

image diane_arms_cow_a_touch_pregnant_belly = "characters/diane/layeredimage/diane_arms_cow_a_touch_pregnant_belly.png"
image diane_arms_cow_a_touch_pregnant_bump = "characters/diane/layeredimage/diane_arms_cow_a_touch.png"
image diane_arms_cow_a_touch = "characters/diane/layeredimage/diane_arms_cow_a_touch.png"

image diane_arms_nightgown_a_water_pregnant_belly = "characters/diane/layeredimage/diane_arms_nightgown_a_water_pregnant_belly.png"
image diane_arms_nightgown_a_water_pregnant_bump = "characters/diane/layeredimage/diane_arms_nightgown_a_water.png"
image diane_arms_nightgown_a_water = "characters/diane/layeredimage/diane_arms_nightgown_a_water.png"

image diane_arms_dressed_a_shovel_sides = "characters/diane/layeredimage/diane_arms_dressed_a_shovel.png"
image diane_arms_shirtless_a_shovel_sides = "characters/diane/layeredimage/diane_arms_shirtless_a_sides.png"
image diane_arms_naked_a_shovel_sides = "characters/diane/layeredimage/diane_arms_naked_a_sides.png"

image diane_kiss_both_naked = "characters/diane/layeredimage/diane_body_b_kiss_both_[M_diane.outfit.get].png"
image diane_kiss_both_naked_pregnant_bump = "characters/diane/layeredimage/diane_body_b_kiss_both_[M_diane.outfit.get].png"
image diane_kiss_both_naked_pregnant_belly = "characters/diane/layeredimage/diane_body_b_kiss_both_[M_diane.outfit.get]_pregnant_belly.png"

image diane_body_b_topless = "characters/diane/layeredimage/diane_body_b_topless.png"
image diane_body_b_topless_pregnant_bump = "characters/diane/layeredimage/diane_body_b_topless.png"
image diane_body_b_topless_pregnant_belly = "characters/diane/layeredimage/diane_body_b_topless_pregnant_belly.png"

image diane_arms_naked_a_squeeze3 = "characters/diane/layeredimage/diane_arms_naked_a_squeeze3.png"
image diane_arms_naked_a_squeeze3_pregnant_bump = "characters/diane/layeredimage/diane_arms_naked_a_squeeze3.png"
image diane_arms_naked_a_squeeze3_pregnant_belly = "characters/diane/layeredimage/diane_arms_naked_a_squeeze3_pregnant_belly.png"

image diane_arms_shirtless_a_squeeze3 = "characters/diane/layeredimage/diane_arms_naked_a_squeeze3.png"
image diane_arms_shirtless_a_squeeze3_pregnant_bump = "characters/diane/layeredimage/diane_arms_naked_a_squeeze3.png"
image diane_arms_shirtless_a_squeeze3_pregnant_belly = "characters/diane/layeredimage/diane_arms_naked_a_squeeze3_pregnant_belly.png"

image diane_arms_cow_a_squeeze3 = "characters/diane/layeredimage/diane_arms_cow_a_squeeze3.png"
image diane_arms_cow_a_squeeze3_pregnant_bump = "characters/diane/layeredimage/diane_arms_cow_a_squeeze3.png"
image diane_arms_cow_a_squeeze3_pregnant_belly = "characters/diane/layeredimage/diane_arms_cow_a_squeeze3_pregnant_belly.png"

image diane_arms_shirtless_a_bottle1 = "characters/diane/layeredimage/diane_arms_shirtless_a_bottle1.png"
image diane_arms_shirtless_a_bottle1_pregnant_bump = "characters/diane/layeredimage/diane_arms_shirtless_a_bottle1.png"
image diane_arms_shirtless_a_bottle1_pregnant_belly = "characters/diane/layeredimage/diane_arms_naked_a_bottle1_pregnant_belly.png"

image diane_arms_cow_a_bottle1 = "characters/diane/layeredimage/diane_arms_cow_a_bottle1.png"
image diane_arms_cow_a_bottle1_pregnant_bump = "characters/diane/layeredimage/diane_arms_cow_a_bottle1.png"
image diane_arms_cow_a_bottle1_pregnant_belly = "characters/diane/layeredimage/diane_arms_cow_a_bottle1_pregnant_belly.png"

image diane_arms_naked_a_bottle1 = "characters/diane/layeredimage/diane_arms_naked_a_bottle1.png"
image diane_arms_naked_a_bottle1_pregnant_bump = "characters/diane/layeredimage/diane_arms_naked_a_bottle1.png"
image diane_arms_naked_a_bottle1_pregnant_belly = "characters/diane/layeredimage/diane_arms_naked_a_bottle1_pregnant_belly.png"

image diane_arms_shirtless_a_cover = "characters/diane/layeredimage/diane_arms_shirtless_a_cover.png"
image diane_arms_shirtless_a_cover_pregnant_bump = "characters/diane/layeredimage/diane_arms_shirtless_a_cover.png"
image diane_arms_shirtless_a_cover_pregnant_belly = "characters/diane/layeredimage/diane_arms_shirtless_a_cover_pregnant_belly.png"

image diane_arms_shirtless_a_vase1 = "characters/diane/layeredimage/diane_arms_shirtless_a_vase1.png"
image diane_arms_shirtless_a_vase1_pregnant_bump = "characters/diane/layeredimage/diane_arms_shirtless_a_vase1.png"
image diane_arms_shirtless_a_vase1_pregnant_belly = "characters/diane/layeredimage/diane_arms_shirtless_a_vase1_pregnant_belly.png"

image diane_arms_shirtless_a_vase2 = "characters/diane/layeredimage/diane_arms_shirtless_a_vase2.png"
image diane_arms_shirtless_a_vase2_pregnant_bump = "characters/diane/layeredimage/diane_arms_shirtless_a_vase2.png"
image diane_arms_shirtless_a_vase2_pregnant_belly = "characters/diane/layeredimage/diane_arms_shirtless_a_vase2_pregnant_belly.png"




image diane_arms_dressed_a_cucumber_rub:
    Transform("characters/diane/layeredimage/diane_arms_dressed_a_cucumber_rub1.png")
    pause .4
    Transform("characters/diane/layeredimage/diane_arms_dressed_a_cucumber_rub2.png")
    pause .4
    repeat

image diane_arms_shirtless_a_wave:
    Transform("characters/diane/layeredimage/diane_arms_shirtless_a_wave1.png")
    pause .4
    Transform("characters/diane/layeredimage/diane_arms_shirtless_a_wave2.png")
    pause .4
    repeat

image diane_arms_topless_a_pump:
    Transform("characters/diane/layeredimage/diane_arms_topless_blank_a_pump1.png")
    pause .4
    Transform("characters/diane/layeredimage/diane_arms_topless_blank_a_pump2.png")
    pause .4
    repeat

image diane_arms_laying_a_wave:
    Transform("characters/diane/layeredimage/diane_arms_laying_a_wave1.png")
    pause .4
    Transform("characters/diane/layeredimage/diane_arms_laying_a_wave2.png")
    pause .4
    repeat

image diane_body_b_laying_massage_back:
    Transform("characters/diane/layeredimage/diane_body_b_laying_massage1.png",yoffset=30)
    pause .4
    Transform("characters/diane/layeredimage/diane_body_b_laying_massage2.png",yoffset=30)
    pause .4
    repeat

image diane_body_b_laying_massage_naked_back:
    Transform("characters/diane/layeredimage/diane_body_b_laying_massage1b.png",yoffset=30)
    pause .4
    Transform("characters/diane/layeredimage/diane_body_b_laying_massage2b.png",yoffset=30)
    pause .4
    repeat

image diane_body_b_laying_massage_butt:
    Transform("characters/diane/layeredimage/diane_body_b_laying_massage3.png",yoffset=30)
    pause .3
    Transform("characters/diane/layeredimage/diane_body_b_laying_massage4.png",yoffset=30)
    pause .3
    Transform("characters/diane/layeredimage/diane_body_b_laying_massage5.png",yoffset=30)
    pause .2
    Transform("characters/diane/layeredimage/diane_body_b_laying_massage4.png",yoffset=30)
    pause .2
    repeat

image diane_body_b_laying_grope:
    Transform("characters/diane/layeredimage/diane_body_b_laying_grope1.png")
    pause .4
    Transform("characters/diane/layeredimage/diane_body_b_laying_grope2.png")
    pause .4
    repeat

image diane_body_b_jerk:
    Transform("characters/diane/layeredimage/diane_body_b_jerk1.png")
    pause .4
    Transform("characters/diane/layeredimage/diane_body_b_jerk2.png")
    pause .4
    repeat

image diane_arms_topless_blank_a_squeeze:
    Transform("characters/diane/layeredimage/diane_arms_topless_blank_a_squeeze1.png")
    pause .4
    Transform("characters/diane/layeredimage/diane_arms_topless_blank_a_squeeze2.png")
    pause .8
    repeat

image diane_body_b_hay_feeding_shirtless:
    Transform("characters/diane/layeredimage/diane_body_b_hay_feeding_shirtless1.png")
    pause .4
    Transform("characters/diane/layeredimage/diane_body_b_hay_feeding_shirtless2.png")
    pause .8
    repeat

image diane_body_b_hay_feeding:
    Transform("characters/diane/layeredimage/diane_body_b_hay_feeding_[M_diane.outfit.get]1.png")
    pause .4
    Transform("characters/diane/layeredimage/diane_body_b_hay_feeding_[M_diane.outfit.get]2.png")
    pause .8
    repeat

image diane_arms_hay_feeding_a_shirtless_stroke:
    Transform("diane_arms_hay_feeding_a_shirtless1_stroke")
    pause .4
    Transform("diane_arms_hay_feeding_a_shirtless2_stroke")
    pause .8
    repeat

image diane_arms_hay_feeding_a_stroke:
    Transform("diane_arms_hay_feeding_a_[M_diane.outfit.get]1_stroke")
    pause .4
    Transform("diane_arms_hay_feeding_a_[M_diane.outfit.get]2_stroke")
    pause .8
    repeat

image diane_arms_dinner_a_touch:
    Transform("characters/diane/layeredimage/diane_arms_dinner_a_touch1.png")
    pause .6
    Transform("characters/diane/layeredimage/diane_arms_dinner_a_touch2.png")
    pause .8
    repeat

image diane dinner_under_hand:
    Transform("characters/diane/layeredimage/diane_dinner_under_hand1.png")
    pause .6
    Transform("characters/diane/layeredimage/diane_dinner_under_hand2.png")
    pause .8
    repeat

image diane_body_b_nightgown_sit_stroke:
    Transform("characters/diane/layeredimage/diane_body_b_nightgown_sit_stroke1.png")
    pause .4
    Transform("characters/diane/layeredimage/diane_body_b_nightgown_sit_stroke2.png")
    pause .4
    repeat

image diane_body_b_hay_rub:
    Transform("characters/diane/layeredimage/diane_body_b_hay_rub1_[M_diane.outfit.get].png")
    pause .4
    Transform("characters/diane/layeredimage/diane_body_b_hay_rub2_[M_diane.outfit.get].png")
    pause .4
    repeat

image diane_body_b_hay_stroke:
    Transform("characters/diane/layeredimage/diane_body_b_hay_stroke1_[M_diane.outfit.get].png")
    pause .4
    Transform("characters/diane/layeredimage/diane_body_b_hay_stroke2_[M_diane.outfit.get].png")
    pause .4
    repeat



image diane_arms_hay_feeding_a_cow1_stroke = "characters/diane/layeredimage/diane_arms_hay_feeding_a_cow1_stroke.png"
image diane_arms_hay_feeding_a_cow2_stroke = "characters/diane/layeredimage/diane_arms_hay_feeding_a_cow2_stroke.png"
image diane_arms_hay_feeding_a_shirtless1_stroke = "characters/diane/layeredimage/diane_arms_hay_feeding_a_shirtless1_stroke.png"
image diane_arms_hay_feeding_a_shirtless2_stroke = "characters/diane/layeredimage/diane_arms_hay_feeding_a_shirtless2_stroke.png"
image diane_arms_hay_feeding_a_naked1_stroke = "characters/diane/layeredimage/diane_arms_hay_feeding_a_shirtless1_stroke.png"
image diane_arms_hay_feeding_a_naked2_stroke = "characters/diane/layeredimage/diane_arms_hay_feeding_a_shirtless2_stroke.png"

image diane_chair down = Image("characters/diane/layeredimage/diane_object_chair_down.png",yoffset=30)
image diane_chair up = Image("characters/diane/layeredimage/diane_object_chair_up.png",yoffset=30)




image diane_sex_cum = "characters/diane/layeredimage/diane_sex_back_after_cum.png"
image diane_sex_cum spread = "characters/diane/layeredimage/diane_sex_back_after_spread_cum.png"


image diane_sex_flying_cum 1 = "characters/diane/layeredimage/diane_sex_back_cumshot3.png"
image diane_sex_flying_cum 2 = "characters/diane/layeredimage/diane_sex_back_cumshot4.png"


image diane_sex_dick_cum 1 = "characters/diane/layeredimage/diane_sex_back_mc_wet.png"
image diane_sex_dick_cum 2 = "characters/diane/layeredimage/diane_sex_back_pullout2_wet.png"


image diane_sex_breed_mc cumshot 1 = "characters/diane/layeredimage/diane_sex_back_cumshot1.png"
image diane_sex_breed_mc cumshot 2 = "characters/diane/layeredimage/diane_sex_back_cumshot2.png"
image diane_sex_breed_mc = "characters/diane/layeredimage/diane_sex_back_mc.png"


image diane_sex_breed after = "characters/diane/layeredimage/diane_sex_back_after_[M_diane.outfit.get].png"
image diane_sex_breed after_spread = "characters/diane/layeredimage/diane_sex_back_after_spread_[M_diane.outfit.get].png"
image diane_sex_breed creampie = "characters/diane/layeredimage/diane_sex_back_creampie_[M_diane.outfit.get].png"
image diane_sex_breed creampie_pullout = "characters/diane/layeredimage/diane_sex_back_creampie_pullout_[M_diane.outfit.get].png"
image diane_sex_breed insert_and_pullout = "characters/diane/layeredimage/diane_sex_back_insert_and_pullout2_[M_diane.outfit.get].png"
image diane_sex_breed pre_talk = "characters/diane/layeredimage/diane_sex_back_pre_talk_[M_diane.outfit.get].png"

image diane_sex_back 1 = ConditionSwitch(
    "M_diane.outfit.get == 'naked'", "characters/diane/layeredimage/diane_sex_back_anim_01_naked.png",
    "True", "characters/diane/layeredimage/diane_sex_back_anim_01_cow.png")
image diane_sex_back 2 = ConditionSwitch(
    "M_diane.outfit.get == 'naked'", "characters/diane/layeredimage/diane_sex_back_anim_02_naked.png",
    "True", "characters/diane/layeredimage/diane_sex_back_anim_02_cow.png")
image diane_sex_back 3 = ConditionSwitch(
    "M_diane.outfit.get == 'naked'", "characters/diane/layeredimage/diane_sex_back_anim_03_naked.png",
    "True", "characters/diane/layeredimage/diane_sex_back_anim_03_cow.png")
image diane_sex_back 4 = ConditionSwitch(
    "M_diane.outfit.get == 'naked'", "characters/diane/layeredimage/diane_sex_back_anim_04_naked.png",
    "True", "characters/diane/layeredimage/diane_sex_back_anim_04_cow.png")
image diane_sex_back 5 = ConditionSwitch(
    "M_diane.outfit.get == 'naked'", "characters/diane/layeredimage/diane_sex_back_anim_05_naked.png",
    "True", "characters/diane/layeredimage/diane_sex_back_anim_05_cow.png")
image diane_sex_back 6 = ConditionSwitch(
    "M_diane.outfit.get == 'naked'", "characters/diane/layeredimage/diane_sex_back_anim_06_naked.png",
    "True", "characters/diane/layeredimage/diane_sex_back_anim_06_cow.png")
image diane_sex_back 7 = ConditionSwitch(
    "M_diane.outfit.get == 'naked'", "characters/diane/layeredimage/diane_sex_back_anim_07_naked.png",
    "True", "characters/diane/layeredimage/diane_sex_back_anim_07_cow.png")
image diane_sex_back 8 = ConditionSwitch(
    "M_diane.outfit.get == 'naked'", "characters/diane/layeredimage/diane_sex_back_anim_08_naked.png",
    "True", "characters/diane/layeredimage/diane_sex_back_anim_08_cow.png")
image diane_sex_back 9 = ConditionSwitch(
    "M_diane.outfit.get == 'naked'", "characters/diane/layeredimage/diane_sex_back_anim_09_naked.png",
    "True", "characters/diane/layeredimage/diane_sex_back_anim_09_cow.png")
image diane_sex_back 10 = ConditionSwitch(
    "M_diane.outfit.get == 'naked'", "characters/diane/layeredimage/diane_sex_back_anim_10_naked.png",
    "True", "characters/diane/layeredimage/diane_sex_back_anim_10_cow.png")

image diane_sex_front 1 = ConditionSwitch(
    "M_diane.outfit.get == 'naked'", "characters/diane/layeredimage/diane_sex_front_anim_01_naked.png",
    "True", "characters/diane/layeredimage/diane_sex_front_anim_01_cow.png")
image diane_sex_front 2 = ConditionSwitch(
    "M_diane.outfit.get == 'naked'", "characters/diane/layeredimage/diane_sex_front_anim_02_naked.png",
    "True", "characters/diane/layeredimage/diane_sex_front_anim_02_cow.png")
image diane_sex_front 3 = ConditionSwitch(
    "M_diane.outfit.get == 'naked'", "characters/diane/layeredimage/diane_sex_front_anim_03_naked.png",
    "True", "characters/diane/layeredimage/diane_sex_front_anim_03_cow.png")
image diane_sex_front 4 = ConditionSwitch(
    "M_diane.outfit.get == 'naked'", "characters/diane/layeredimage/diane_sex_front_anim_04_naked.png",
    "True", "characters/diane/layeredimage/diane_sex_front_anim_04_cow.png")
image diane_sex_front 5 = ConditionSwitch(
    "M_diane.outfit.get == 'naked'", "characters/diane/layeredimage/diane_sex_front_anim_05_naked.png",
    "True", "characters/diane/layeredimage/diane_sex_front_anim_05_cow.png")
image diane_sex_front 6 = ConditionSwitch(
    "M_diane.outfit.get == 'naked'", "characters/diane/layeredimage/diane_sex_front_anim_06_naked.png",
    "True", "characters/diane/layeredimage/diane_sex_front_anim_06_cow.png")
image diane_sex_front 7 = ConditionSwitch(
    "M_diane.outfit.get == 'naked'", "characters/diane/layeredimage/diane_sex_front_anim_07_naked.png",
    "True", "characters/diane/layeredimage/diane_sex_front_anim_07_cow.png")
image diane_sex_front 8 = ConditionSwitch(
    "M_diane.outfit.get == 'naked'", "characters/diane/layeredimage/diane_sex_front_anim_08_naked.png",
    "True", "characters/diane/layeredimage/diane_sex_front_anim_08_cow.png")
image diane_sex_front 9 = ConditionSwitch(
    "M_diane.outfit.get == 'naked'", "characters/diane/layeredimage/diane_sex_front_anim_09_naked.png",
    "True", "characters/diane/layeredimage/diane_sex_front_anim_09_cow.png")
image diane_sex_front 10 = ConditionSwitch(
    "M_diane.outfit.get == 'naked'", "characters/diane/layeredimage/diane_sex_front_anim_10_naked.png",
    "True", "characters/diane/layeredimage/diane_sex_front_anim_10_cow.png")

image xray_diane_back:
    Transform("characters/xray/xray_left_back_01.png", zoom=.8, rotate=-15, xoffset=180, yoffset=70)
    pause 0.4
    Transform("characters/xray/xray_left_back_02.png", zoom=.8, rotate=-15, xoffset=180, yoffset=70)
    pause 0.4
    Transform("characters/xray/xray_left_back_03.png", zoom=.8, rotate=-15, xoffset=180, yoffset=70)
    pause 0.4
    Transform("characters/xray/xray_left_back_04.png", zoom=.8, rotate=-15, xoffset=180, yoffset=70)
    pause 0.4
    Transform("characters/xray/xray_left_back_05.png", zoom=.8, rotate=-15, xoffset=180, yoffset=70)
    pause 0.4
    Transform("characters/xray/xray_left_back_06.png", zoom=.8, rotate=-15, xoffset=180, yoffset=70)
    pause 0.4
    Transform("characters/xray/xray_left_back_07.png", zoom=.8, rotate=-15, xoffset=180, yoffset=70)
    pause 0.4
    Transform("characters/xray/xray_left_back_08.png", zoom=.8, rotate=-15, xoffset=180, yoffset=70)
    pause 0.4
    Transform("characters/xray/xray_left_back_09.png", zoom=.8, rotate=-15, xoffset=180, yoffset=70)
    pause 0.4
    Transform("characters/xray/xray_left_back_10.png", zoom=.8, rotate=-15, xoffset=180, yoffset=70)
    pause 0.4
    Transform("characters/xray/xray_left_back_11.png", zoom=.8, rotate=-15, xoffset=180, yoffset=70)
    pause 0.4
    Transform("characters/xray/xray_left_back_12.png", zoom=.8, rotate=-15, xoffset=180, yoffset=70)
    pause 0.4
    Transform("characters/xray/xray_left_back_13.png", zoom=.8, rotate=-15, xoffset=180, yoffset=70)
    pause 0.4
    Transform("characters/xray/xray_left_back_14.png", zoom=.8, rotate=-15, xoffset=180, yoffset=70)
    pause 0.4
    Transform("characters/xray/xray_left_back_15.png", zoom=.8, rotate=-15, xoffset=180, yoffset=70)
    pause 0.4
    Transform("characters/xray/xray_left_back_16.png", zoom=.8, rotate=-15, xoffset=180, yoffset=70)
    pause 0.4
    Transform("characters/xray/xray_left_back_17.png", zoom=.8, rotate=-15, xoffset=180, yoffset=70)
    pause 0.4
    Transform("characters/xray/xray_left_back_18.png", zoom=.8, rotate=-15, xoffset=180, yoffset=70)
    pause 2.0
    linear 2.5 alpha 0



image diane_sex_boobjob cum = "characters/diane/layeredimage/diane_sex_boobjob_cum_[M_diane.outfit.get].png"

image diane_sex_boobjob_look = "characters/diane/layeredimage/diane_sex_boobjob_anim2_look_[M_diane.outfit.get].png"
image diane_sex_boobjob_look talk = "characters/diane/layeredimage/diane_sex_boobjob_anim2_look_talk_[M_diane.outfit.get].png"

image diane_sex_boobjob_cum 1 = "characters/diane/layeredimage/diane_sex_boobjob_cum_anim1.png"
image diane_sex_boobjob_cum 2 = "characters/diane/layeredimage/diane_sex_boobjob_cum_anim2.png"
image diane_sex_boobjob_cum 3 = "characters/diane/layeredimage/diane_sex_boobjob_cum_anim3.png"
image diane_sex_boobjob_cum 4 = "characters/diane/layeredimage/diane_sex_boobjob_cum_anim4.png"
image diane_sex_boobjob_cum 5 = "characters/diane/layeredimage/diane_sex_boobjob_cum_anim5.png"
image diane_sex_boobjob_cum 6 = "characters/diane/layeredimage/diane_sex_boobjob_cum_anim6.png"

image diane_sex_boobjob_cum:
    Transform("characters/diane/layeredimage/diane_sex_boobjob_cum_anim1.png")
    pause .25
    Transform("characters/diane/layeredimage/diane_sex_boobjob_cum_anim2.png")
    pause .25
    Transform("characters/diane/layeredimage/diane_sex_boobjob_cum_anim3.png")
    pause .25
    Transform("characters/diane/layeredimage/diane_sex_boobjob_cum_anim4.png")
    pause .25
    Transform("characters/diane/layeredimage/diane_sex_boobjob_cum_anim5.png")
    pause .25
    Transform("characters/diane/layeredimage/diane_sex_boobjob_cum_anim6.png")
    pause .25

image diane_sex_boobjob 1 = ConditionSwitch(
    "M_diane.outfit.get == 'naked'", "characters/diane/layeredimage/diane_sex_boobjob_anim1.png",
    "True", "characters/diane/layeredimage/diane_sex_boobjob_anim1_cow.png")
image diane_sex_boobjob 2 = ConditionSwitch(
    "M_diane.outfit.get == 'naked'", "characters/diane/layeredimage/diane_sex_boobjob_anim2.png",
    "True", "characters/diane/layeredimage/diane_sex_boobjob_anim2_cow.png")
image diane_sex_boobjob 3 = ConditionSwitch(
    "M_diane.outfit.get == 'naked'", "characters/diane/layeredimage/diane_sex_boobjob_anim3.png",
    "True", "characters/diane/layeredimage/diane_sex_boobjob_anim3_cow.png")



image diane_hay_insert 1 = ConditionSwitch(
    "M_diane.outfit.get == 'naked'", "characters/diane/layeredimage/diane_body_b_hay_insert1_naked.png",
    "True", "characters/diane/layeredimage/diane_body_b_hay_insert1_cow.png")
image diane_hay_insert 2 = ConditionSwitch(
    "M_diane.outfit.get == 'naked'", "characters/diane/layeredimage/diane_body_b_hay_insert2_naked.png",
    "True", "characters/diane/layeredimage/diane_body_b_hay_insert2_cow.png")




image diane_debbie_sex_cum 1 = ConditionSwitch(
    "M_diane.get('change partner') == False", "characters/diane/layeredimage/diane_sex_bed_cumshot_diane_01.png",
    "True", "characters/diane/layeredimage/diane_sex_bed_cumshot_debbie_01.png")
image diane_debbie_sex_cum 2 = ConditionSwitch(
    "M_diane.get('change partner') == False", "characters/diane/layeredimage/diane_sex_bed_cumshot_diane_02.png",
    "True", "characters/diane/layeredimage/diane_sex_bed_cumshot_debbie_02.png")
image diane_debbie_sex_cum 3 = ConditionSwitch(
    "M_diane.get('change partner') == False", "characters/diane/layeredimage/diane_sex_bed_cumshot_diane_03.png",
    "True", "characters/diane/layeredimage/diane_sex_bed_cumshot_debbie_03.png")
image diane_debbie_sex_cum 4 = ConditionSwitch(
    "M_diane.get('change partner') == False", "characters/diane/layeredimage/diane_sex_bed_cumshot_diane_04.png",
    "True", "characters/diane/layeredimage/diane_sex_bed_cumshot_debbie_04.png")

image diane_debbie_sex_bed_cumshot_mc:
    Transform("diane_debbie_sex_cum 1")
    pause .25
    Transform("diane_debbie_sex_cum 2")
    pause .25
    Transform("diane_debbie_sex_cum 3")
    pause .25
    Transform("diane_debbie_sex_cum 4")
    pause .25

image diane_debbie_sex_bed base = ConditionSwitch(
    "M_diane.get('change partner') == False", "characters/diane/layeredimage/diane_sex_bed_cumshot_diane_base.png",
    "True", "characters/diane/layeredimage/diane_sex_bed_cumshot_debbie_base.png")


image diane_debbie_sex_bed cumpie = ConditionSwitch(
    "M_diane.get('change partner') == False", "characters/diane/layeredimage/diane_sex_bed_cum1.png",
    "True", "characters/diane/layeredimage/diane_sex_bed_cum2.png")


image diane_debbie_sex_bed insert = ConditionSwitch(
    "M_diane.get('change partner') == False", "characters/diane/layeredimage/diane_sex_bed_insert1.png",
    "True", "characters/diane/layeredimage/diane_sex_bed_insert2.png")


image diane_debbie_sex_bed prev_insert = ConditionSwitch(
    "M_diane.get('change partner') == False", "characters/diane/layeredimage/diane_sex_bed_insert2.png",
    "True", "characters/diane/layeredimage/diane_sex_bed_insert1.png")


image diane_debbie_sex_bed diane_after_talk = "characters/diane/layeredimage/diane_sex_bed_after2.png"

image diane_debbie_sex_bed debbie_after_talk = "characters/diane/layeredimage/diane_sex_bed_after1.png"

image diane_debbie_sex_bed player_after_talk = "characters/diane/layeredimage/diane_sex_bed_after3.png"

image diane_debbie_sex_bed diane_lounge_after_talk = "characters/diane/layeredimage/diane_sex_bed_after4.png"

image diane_debbie_sex_bed debbie_lounge_after_talk = "characters/diane/layeredimage/diane_sex_bed_after5.png"

image diane_debbie_sex_bed player_lounge_after_talk = "characters/diane/layeredimage/diane_sex_bed_after6.png"



image diane_debbie_sex_bed diane_talk = "characters/diane/layeredimage/diane_sex_bed_pre2.png"

image diane_debbie_sex_bed debbie_talk = "characters/diane/layeredimage/diane_sex_bed_pre1.png"

image diane_debbie_sex_bed player_talk = "characters/diane/layeredimage/diane_sex_bed_pre3.png"

image diane_debbie_sex_bed 1 = ConditionSwitch(
    "M_diane.get('change partner') == False", "characters/diane/layeredimage/diane_sex_bed_anim_top01.png",
    "True", "characters/diane/layeredimage/diane_sex_bed_anim_bot01.png")
image diane_debbie_sex_bed 2 = ConditionSwitch(
    "M_diane.get('change partner') == False", "characters/diane/layeredimage/diane_sex_bed_anim_top02.png",
    "True", "characters/diane/layeredimage/diane_sex_bed_anim_bot02.png")
image diane_debbie_sex_bed 3 = ConditionSwitch(
    "M_diane.get('change partner') == False", "characters/diane/layeredimage/diane_sex_bed_anim_top03.png",
    "True", "characters/diane/layeredimage/diane_sex_bed_anim_bot03.png")
image diane_debbie_sex_bed 4 = ConditionSwitch(
    "M_diane.get('change partner') == False", "characters/diane/layeredimage/diane_sex_bed_anim_top04.png",
    "True", "characters/diane/layeredimage/diane_sex_bed_anim_bot04.png")
image diane_debbie_sex_bed 5 = ConditionSwitch(
    "M_diane.get('change partner') == False", "characters/diane/layeredimage/diane_sex_bed_anim_top05.png",
    "True", "characters/diane/layeredimage/diane_sex_bed_anim_bot05.png")
image diane_debbie_sex_bed 6 = ConditionSwitch(
    "M_diane.get('change partner') == False", "characters/diane/layeredimage/diane_sex_bed_anim_top06.png",
    "True", "characters/diane/layeredimage/diane_sex_bed_anim_bot06.png")
image diane_debbie_sex_bed 7 = ConditionSwitch(
    "M_diane.get('change partner') == False", "characters/diane/layeredimage/diane_sex_bed_anim_top07.png",
    "True", "characters/diane/layeredimage/diane_sex_bed_anim_bot07.png")
image diane_debbie_sex_bed 8 = ConditionSwitch(
    "M_diane.get('change partner') == False", "characters/diane/layeredimage/diane_sex_bed_anim_top08.png",
    "True", "characters/diane/layeredimage/diane_sex_bed_anim_bot08.png")
image diane_debbie_sex_bed 9 = ConditionSwitch(
    "M_diane.get('change partner') == False", "characters/diane/layeredimage/diane_sex_bed_anim_top09.png",
    "True", "characters/diane/layeredimage/diane_sex_bed_anim_bot09.png")
image diane_debbie_sex_bed 10 = ConditionSwitch(
    "M_diane.get('change partner') == False", "characters/diane/layeredimage/diane_sex_bed_anim_top10.png",
    "True", "characters/diane/layeredimage/diane_sex_bed_anim_bot10.png")

image xray_diane_debbie_sex:
    Transform("characters/xray/xray_left_back_01.png", xzoom=-0.7, yzoom=0.7, xoffset=190, yoffset=270)
    pause 0.4
    Transform("characters/xray/xray_left_back_02.png", xzoom=-0.7, yzoom=0.7, xoffset=190, yoffset=270)
    pause 0.4
    Transform("characters/xray/xray_left_back_03.png", xzoom=-0.7, yzoom=0.7, xoffset=190, yoffset=270)
    pause 0.4
    Transform("characters/xray/xray_left_back_04.png", xzoom=-0.7, yzoom=0.7, xoffset=190, yoffset=270)
    pause 0.4
    Transform("characters/xray/xray_left_back_05.png", xzoom=-0.7, yzoom=0.7, xoffset=190, yoffset=270)
    pause 0.4
    Transform("characters/xray/xray_left_back_06.png", xzoom=-0.7, yzoom=0.7, xoffset=190, yoffset=270)
    pause 0.4
    Transform("characters/xray/xray_left_back_07.png", xzoom=-0.7, yzoom=0.7, xoffset=190, yoffset=270)
    pause 0.4
    Transform("characters/xray/xray_left_back_08.png", xzoom=-0.7, yzoom=0.7, xoffset=190, yoffset=270)
    pause 0.4
    Transform("characters/xray/xray_left_back_09.png", xzoom=-0.7, yzoom=0.7, xoffset=190, yoffset=270)
    pause 0.4
    Transform("characters/xray/xray_left_back_10.png", xzoom=-0.7, yzoom=0.7, xoffset=190, yoffset=270)
    pause 0.4
    Transform("characters/xray/xray_left_back_11.png", xzoom=-0.7, yzoom=0.7, xoffset=190, yoffset=270)
    pause 0.4
    Transform("characters/xray/xray_left_back_12.png", xzoom=-0.7, yzoom=0.7, xoffset=190, yoffset=270)
    pause 0.4
    Transform("characters/xray/xray_left_back_13.png", xzoom=-0.7, yzoom=0.7, xoffset=190, yoffset=270)
    pause 0.4
    Transform("characters/xray/xray_left_back_14.png", xzoom=-0.7, yzoom=0.7, xoffset=190, yoffset=270)
    pause 0.4
    Transform("characters/xray/xray_left_back_15.png", xzoom=-0.7, yzoom=0.7, xoffset=190, yoffset=270)
    pause 0.4
    Transform("characters/xray/xray_left_back_16.png", xzoom=-0.7, yzoom=0.7, xoffset=190, yoffset=270)
    pause 0.4
    Transform("characters/xray/xray_left_back_17.png", xzoom=-0.7, yzoom=0.7, xoffset=190, yoffset=270)
    pause 0.4
    Transform("characters/xray/xray_left_back_18.png", xzoom=-0.7, yzoom=0.7, xoffset=190, yoffset=270)
    pause 2.0
    linear 2.5 alpha 0


image diane_sex_milk_pump:
    Fixed('diane_sex_milk_pump02', 'diane_sex_milk_squirt03')
    .6
    Fixed('diane_sex_milk_pump02', 'diane_sex_milk_squirt04') with Dissolve(.4)
    .6
    block:
        Fixed('diane_sex_milk_pump01', 'diane_sex_milk_squirt01', 'diane_sex_milk_squirt05') with Dissolve(.4)
        1.2
        Fixed('diane_sex_milk_pump02', 'diane_sex_milk_squirt02', 'diane_sex_milk_squirt03', 'diane_sex_milk_squirt04') with Dissolve(.4)
        1.2
        repeat

image diane_sex_milk_rub:
    Fixed('diane_sex_milk_rub02', Transform(DynamicImage('[face]'), yoffset=5)) with fastdissolve
    .6
    Fixed('diane_sex_milk_base', DynamicImage('[face]'), 'diane_sex_milk_rub01') with fastdissolve
    .6
    repeat

init python hide:
    poses = ('base', 'cum', 'insert', 'pullout', 'pump01', 'pump02',
             'pump_base', 'rub02')

    for pose in poses:
        name = 'diane_sex_milk_' + pose
        renpy.image(name, name + '_[outfit]')

init python hide:
    frames = range(1, 10)
    for o in ('cow', 'naked'):
        for i in frames:
            renpy.image('diane_sex_milk_anim_{} {}'.format(o, i),
                        'diane_sex_milk_anim_{}_{:02}'.format(o, i))
        
        stem = 'diane_sex_milk_anim_{}'.format(o)
        renpy.image(stem, AnimatedImage(stem, frames, M_diane))

image diane_sex_milk_anim = 'diane_sex_milk_anim_[outfit]'

image xray_diane_sex_milk:
    anchor (.5, .5)
    pos (250 + 256, 250 + 260)
    rotate 300
    rotate_pad False
    xzoom -1
    zoom .72
    'xray_under'
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
