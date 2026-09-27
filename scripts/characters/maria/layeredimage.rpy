init:
    $ maria_clothing_options = ['b_dressed','b_dressed_magic','b_casual_magic','b_empty','b_naked_pregnant_belly','b_apron_pregnant_belly_wipe','b_casual','b_lingerie_boob_bounce','b_lingerie','b_naked','b_magic']

init python:


    renpy.image('maria_arms_a_empty', 'ground.png')
    renpy.image('maria_body_b_empty', 'ground.png')
    renpy.image('maria_face_f_empty', 'ground.png')
    renpy.image('maria_face_talk_f_empty', 'ground.png')


    renpy.image('maria_face_talk_f_laugh', 'maria_face_f_laugh')
    renpy.image('maria_face_lingerie_back_talk_f_laugh', 'maria_face_lingerie_back_f_laugh')




    renpy.image('maria_arms_casual_a_handkerchief_pregnant_bump', 'maria_arms_casual_a_handkerchief')
    renpy.image('maria_arms_casual_a_handkerchief_blow_pregnant_bump', 'maria_arms_casual_a_handkerchief_blow')


layeredimage maria:

    yanchor config.screen_height
    ypos 1.
    xanchor config.screen_width
    xpos 1.


    group body auto:
        attribute b_dressed default
        attribute b_empty null
        attribute b_magic "maria_body_b_[M_maria.outfit][M_maria.pregnancy]"   

        attribute b_dressed_magic "maria_body_b_dressed[M_maria.pregnancy]"   

        attribute b_casual_magic "maria_body_b_casual[M_maria.pregnancy]"   

        attribute b_dressed_pregnant_kiss "maria_body_b_dressed_pregnant_kiss"

        attribute b_lingerie_back "maria_body_b_lingerie_back"

        attribute b_naked_kiss_tony "maria_body_b_naked_kiss_tony"

        attribute b_lingerie_kiss_tony "maria_body_b_lingerie_kiss_tony"

        attribute b_magic_kiss_mc_cheek "maria_body_b_[M_maria.outfit][M_maria.pregnancy]_kiss_mc_cheek"

        attribute b_magic_fall "maria_body_b_[M_maria.outfit]_falling[M_maria.pregnancy]"

        attribute b_magic_mc_hold "maria_body_b_[M_maria.outfit][M_maria.pregnancy]_mc_hold"

        attribute b_magic_hug_boobs1 "maria_body_[M_maria.outfit]_b_hug_boobs1[M_maria.pregnancy]"

        attribute b_magic_hug_boobs2 "maria_body_[M_maria.outfit]_b_hug_boobs2[M_maria.pregnancy]"

        attribute b_casual_hug_mc "maria_body_b_casual[M_maria.pregnancy]_hug_mc"



    group mouth prefix 'm':
        attribute talk null

    group face:
        attribute f_normal default null







    group face if_not 'm_talk' if_any maria_clothing_options auto


    group face if_not 'm_talk' if_any ['b_magic_hug_boobs1','b_magic_hug_boobs2'] auto:
        offset (-84, 18)


    group face if_not 'm_talk' if_any ['b_naked_bending','b_dressed_bending'] auto:
        offset (-202, 116)


    group face if_not 'm_talk' if_any 'b_naked_shy1' auto:
        offset (-6, 8)


    group face if_not 'm_talk' if_any 'b_naked_shy2' auto:
        offset (-10, 2)


    group face if_not 'm_talk' if_any 'b_naked_pulling_mc' auto:
        xzoom -1
        offset (357, 0)


    group face if_not 'm_talk' if_all 'b_magic_mc_hold' auto:
        xzoom -1
        offset (424, 106)


    group face if_not 'm_talk' if_all 'b_gown_bed' auto:
        offset (158, 40)






    group face if_not 'm_talk' if_any ['b_sex_bj_base'] auto variant 'sex_bj_base'


    group face if_not 'm_talk' if_any ['b_sex_home_pre_after','b_sex_home_insert_pullout'] auto variant 'sex_home'


    group face if_not 'm_talk' if_any ['b_lingerie_back1','b_lingerie_back2','b_lingerie_back'] auto variant 'lingerie_back'


    group face if_not 'm_talk' if_any ['b_sex_front_open','b_sex_front_closed','b_sex_front_insert'] auto variant 'sex_front'


    group face if_not 'm_talk' if_any ['b_sex_kitchen_mc_remove_panties1','b_sex_kitchen_mc_remove_panties2','b_sex_kitchen_mc_remove_panties3','b_sex_kitchen_talk','b_sex_kitchen_talk_uncovered','b_sex_kitchen_talk_pregnant_belly'] auto variant 'sex_kitchen'


    group face if_not 'm_talk' if_any ['b_sex_side_after', 'b_sex_side_after_back', 'b_sex_side_after_hug', 'b_sex_side_after_up'] auto variant 'sex_side'


    group face if_not 'm_talk' if_any 'b_sex_3some_talk' auto variant 'sex_3some'







    group face if_all 'm_talk' if_any maria_clothing_options auto variant 'talk'


    group face if_all 'm_talk' if_any ['b_magic_hug_boobs1','b_magic_hug_boobs2'] auto variant 'talk':
        offset (-84, 18)


    group face if_all 'm_talk' if_any ['b_naked_bending','b_dressed_bending'] auto variant 'talk':
        offset (-202, 116)


    group face if_all 'm_talk' if_any 'b_naked_shy1' auto variant 'talk':
        offset (-6, 8)


    group face if_all 'm_talk' if_any 'b_naked_shy2' auto variant 'talk':
        offset (-10, 2)


    group face if_all 'm_talk' if_any 'b_naked_pulling_mc' auto variant 'talk':
        xzoom -1
        offset (357, 0)


    group face if_all ['m_talk','b_magic_mc_hold'] auto variant 'talk':
        xzoom -1
        offset (424, 106)


    group face if_all ['m_talk', 'b_gown_bed'] auto variant 'talk':
        offset (158, 40)






    group face if_all 'm_talk' if_any ['b_sex_bj_base'] auto variant 'sex_bj_base_talk'


    group face if_all 'm_talk' if_any ['b_sex_home_pre_after','b_sex_home_insert_pullout'] auto variant 'sex_home_talk'


    group face if_all 'm_talk' if_any ['b_lingerie_back1','b_lingerie_back2','b_lingerie_back'] auto variant 'lingerie_back_talk'


    group face if_all 'm_talk' if_any ['b_sex_front_open','b_sex_front_closed','b_sex_front_insert'] auto variant 'sex_front_talk'


    group face if_all 'm_talk' if_any ['b_sex_kitchen_mc_remove_panties1','b_sex_kitchen_mc_remove_panties2','b_sex_kitchen_mc_remove_panties3','b_sex_kitchen_talk_uncovered','b_sex_kitchen_talk','b_sex_kitchen_talk_pregnant_belly'] auto variant 'sex_kitchen_talk'


    group face if_all 'm_talk' if_any ['b_sex_side_after', 'b_sex_side_after_back', 'b_sex_side_after_hug', 'b_sex_side_after_up'] auto variant 'sex_side_talk'


    group face if_all 'm_talk' if_any 'b_sex_3some_talk' auto variant 'sex_3some_talk'



    group arms if_all 'b_dressed' auto variant 'dressed':
        attribute a_idle default 'maria_arms_dressed_a_hips'
        attribute a_baby "maria_arms_dressed_a_baby_[M_maria.pregnancy.baby_gender]"



    group arms if_all 'b_gown_bed' auto variant 'gown_bed':
        attribute a_idle default "maria_arms_gown_bed_a_baby_[M_maria.pregnancy.baby_gender]"



    group arms if_all 'b_naked_bending' auto variant 'naked_bending':
        attribute a_idle default 'maria_arms_naked_bending_a_remove1'
        attribute a_jerk 'maria_arms_naked_bending_a_jerk'


    group arms if_all 'b_dressed_bending' auto variant 'dressed_bending':
        attribute a_idle default 'maria_arms_dressed_bending_a_remove1'


    group arms if_all 'b_casual' auto variant 'casual':
        attribute a_idle default 'maria_arms_casual_a_hips'
        attribute a_baby "maria_arms_casual_a_baby_[M_maria.pregnancy.baby_gender]"



    group arms if_all 'b_magic' auto:
        attribute a_idle default 'maria_arms_[M_maria.outfit]_a_touch[M_maria.pregnancy]'
        attribute a_mouth 'maria_arms_[M_maria.outfit]_a_mouth[M_maria.pregnancy]'
        attribute a_crossed 'maria_arms_[M_maria.outfit]_a_crossed[M_maria.pregnancy]'
        attribute a_untie_pregnant_belly 'maria_arms_naked_a_untie_pregnant_belly'
        attribute a_cannoli_hold 'maria_arms_dressed_a_cannoli_hold'


    group arms if_all 'b_dressed_magic' auto variant 'dressed':
        attribute a_idle default 'maria_arms_dressed_a_touch[M_maria.pregnancy]'


    group arms if_all 'b_casual_magic' auto variant 'casual':
        attribute a_idle default 'maria_arms_casual_a_touch[M_maria.pregnancy]'
        attribute a_groceries 'maria_arms_dressed_a_groceries[M_maria.pregnancy]'
        attribute a_groceries_give 'maria_arms_dressed_a_groceries_give[M_maria.pregnancy]'
        attribute a_point 'maria_arms_dressed_a_point[M_maria.pregnancy]'
        attribute a_handkerchief 'maria_arms_casual_a_handkerchief[M_maria.pregnancy]'
        attribute a_handkerchief_blow 'maria_arms_casual_a_handkerchief_blow[M_maria.pregnancy]'



    group arms if_all 'b_naked_pregnant_belly' auto:
        attribute a_idle default 'maria_arms_naked_a_hold_apron_pregnant_belly'


    group arms if_any ['b_sex_home_pre_after'] auto variant 'sex_home':
        attribute a_idle default 'maria_arms_sex_home_a_back'
        attribute a_cumshot 'maria_arms_sex_home_a_cumshot'


    group arms if_any ['b_lingerie'] auto variant 'lingerie':
        attribute a_idle default 'maria_arms_lingerie_a_sides'


    group arms if_any ['b_naked'] auto variant 'naked':
        attribute a_idle default 'maria_arms_naked_a_hips'


    group overlay if_any maria_clothing_options auto:
        attribute o_empty default null

    group overlay if_all 'b_lingerie_boob_bounce' auto:
        attribute o_idle default 'maria_overlay_boob_bounce'
        attribute o_empty null

    group overlay if_any ['b_sex_kitchen_base','b_sex_kitchen_base_pregnant_belly'] auto variant 'sex_kitchen':
        attribute o_empty default null

    group overlay if_any ['b_sex_front_open','b_sex_front_insert','b_sex_front_closed'] auto variant 'sex_front':
        attribute o_empty default null

    group overlay_dick if_all 'b_sex_home_pre_after' if_not 'a_cumshot' auto variant 'sex_home':
        attribute od_idle default 'maria_overlay_dick_sex_home_od_pre'
        attribute od_empty null

    group overlay_pussy if_all 'b_sex_home_pre_after' if_not 'a_pussy_open' auto variant 'sex_home':
        attribute op_idle default 'maria_overlay_pussy_sex_home_op_pre'
        attribute op_empty null

    group overlay_cumshot if_all 'b_sex_home_pre_after' auto variant 'sex_home':
        attribute oc_empty default null

image maria_f = "characters/maria/maria_face_f_normal.png"

image maria_arms_dressed_a_touch = "characters/maria/maria_arms_dressed_a_hips.png"
image maria_arms_dressed_a_crossed_pregnant_bump = "characters/maria/maria_arms_dressed_a_crossed.png"
image maria_arms_dressed_a_mouth_pregnant_bump = "characters/maria/maria_arms_dressed_a_mouth.png"
image maria_arms_casual_a_touch = "characters/maria/maria_arms_casual_a_hips.png"

image maria_arms_apron_a_touch_pregnant_belly = "characters/maria/maria_arms_naked_a_touch_pregnant_belly.png"
image maria_arms_apron_a_touch_pregnant_bump = "characters/maria/maria_arms_naked_a_hips.png"
image maria_arms_apron_a_touch = "characters/maria/maria_arms_naked_a_hips.png"

image maria_overlay_boob_bounce:
    Transform("maria_overlay_boob_bounce1")
    pause .3
    Transform("maria_overlay_boob_bounce2")
    pause .4
    Transform("maria_overlay_boob_bounce3")

image maria_body_b_dressed_pregnant_kiss:
    Transform("maria_body_b_dressed_pregnant_kiss1")
    pause .4
    Transform("maria_body_b_dressed_pregnant_kiss2")
    pause .4
    repeat

image maria_arms_naked_bending_a_jerk:
    Transform("maria_arms_naked_bending_a_jerk1")
    pause .4
    Transform("maria_arms_naked_bending_a_jerk2")
    pause .4
    repeat

image maria_body_b_lingerie_back:
    Transform("maria_body_b_lingerie_back1")
    pause .6
    Transform("maria_body_b_lingerie_back2")
    pause .6
    repeat

image maria_body_b_naked_kiss_tony:
    Transform("maria_body_b_naked_kiss_tony1")
    pause .4
    Transform("maria_body_b_naked_kiss_tony2")
    pause .4
    repeat

image maria_body_b_lingerie_kiss_tony:
    Transform("maria_body_b_lingerie_kiss_tony1")
    pause .4
    Transform("maria_body_b_lingerie_kiss_tony2")
    pause .4
    repeat



image maria_sex_bj_anim 1 = "maria_sex_bj_anim_01"
image maria_sex_bj_anim 2 = "maria_sex_bj_anim_02"
image maria_sex_bj_anim 3 = "maria_sex_bj_anim_03"
image maria_sex_bj_anim 4 = "maria_sex_bj_anim_04"
image maria_sex_bj_anim 5 = "maria_sex_bj_anim_05"
image maria_sex_bj_anim 6 = "maria_sex_bj_anim_06"
image maria_sex_bj_anim 7 = "maria_sex_bj_anim_07"
image maria_sex_bj_anim 8 = "maria_sex_bj_anim_08"
image maria_sex_bj_anim 9 = "maria_sex_bj_anim_09"
image maria_sex_bj_anim 10 = "maria_sex_bj_anim_10"

image maria_sex_bj_dick_cum1 = Composite(
    (1024,768),
    (0,0), "characters/maria/maria_sex_bj_dick1.png",
    (0,0), "characters/maria/maria_sex_bj_cum1.png",
    )

image maria_sex_bj_dick_cum2 = Composite(
    (1024,768),
    (0,0), "characters/maria/maria_sex_bj_dick2.png",
    (0,0), "characters/maria/maria_sex_bj_cum2.png",
    )

image maria_sex_bj_dick_cum3 = Composite(
    (1024,768),
    (0,0), "characters/maria/maria_sex_bj_dick3.png",
    (0,0), "characters/maria/maria_sex_bj_cum3.png",
    )

image maria_sex_bj_cum:
    Transform("maria_sex_bj_dick_cum1")
    pause .4
    Transform("maria_sex_bj_dick_cum2")
    pause .4
    Transform("maria_sex_bj_dick_cum3")


image anon_maria_sex_front insert = "characters/maria/maria_sex_front_mc_insert.png"
image anon_maria_sex_front inside = "characters/maria/maria_sex_front_mc_inside.png"
image anon_maria_sex_front pre = "characters/maria/maria_sex_front_mc_pre.png"
image anon_maria_sex_front cumshot = "characters/maria/maria_sex_front_mc_cumshot.png"

image maria_sex_front_mc_cumshot_dick:
    Transform("maria_sex_front_mc_cumshot_dick1")
    pause .4
    Transform("maria_sex_front_mc_cumshot_dick2")

image maria_backroom_sex 1 = "maria_body_b_sex_side_anim01"
image maria_backroom_sex 2 = "maria_body_b_sex_side_anim02"
image maria_backroom_sex 3 = "maria_body_b_sex_side_anim03"
image maria_backroom_sex 4 = "maria_body_b_sex_side_anim04"
image maria_backroom_sex 5 = "maria_body_b_sex_side_anim05"
image maria_backroom_sex 6 = "maria_body_b_sex_side_anim06"
image maria_backroom_sex 7 = "maria_body_b_sex_side_anim07"
image maria_backroom_sex 8 = "maria_body_b_sex_side_anim08"
image maria_backroom_sex 9 = "maria_body_b_sex_side_anim09"
image maria_backroom_sex 10 = "maria_body_b_sex_side_anim10"


image anon_maria_sex_kitchen pre = "characters/maria/maria_sex_kitchen_mc_pre.png"
image anon_maria_sex_kitchen insert = "characters/maria/maria_sex_kitchen_mc_insert.png"
image anon_maria_sex_kitchen cumshot = "characters/maria/maria_sex_kitchen_mc_cumshot.png"

image maria_sex_kitchen_mc_cumshot_dick:
    Transform("maria_sex_kitchen_mc_cumshot_dick1")
    pause .4
    Transform("maria_sex_kitchen_mc_cumshot_dick2")
    pause .4
    Transform("maria_sex_kitchen_mc_cumshot_dick3")

image maria_kitchen_sex_preggo 1 = "maria_body_b_sex_kitchen_pregnant_belly_anim01"
image maria_kitchen_sex_preggo 2 = "maria_body_b_sex_kitchen_pregnant_belly_anim02"
image maria_kitchen_sex_preggo 3 = "maria_body_b_sex_kitchen_pregnant_belly_anim03"
image maria_kitchen_sex_preggo 4 = "maria_body_b_sex_kitchen_pregnant_belly_anim04"
image maria_kitchen_sex_preggo 5 = "maria_body_b_sex_kitchen_pregnant_belly_anim05"
image maria_kitchen_sex_preggo 6 = "maria_body_b_sex_kitchen_pregnant_belly_anim06"
image maria_kitchen_sex_preggo 7 = "maria_body_b_sex_kitchen_pregnant_belly_anim07"

image maria_kitchen_sex 1 = "maria_body_b_sex_kitchen_anim01"
image maria_kitchen_sex 2 = "maria_body_b_sex_kitchen_anim02"
image maria_kitchen_sex 3 = "maria_body_b_sex_kitchen_anim03"
image maria_kitchen_sex 4 = "maria_body_b_sex_kitchen_anim04"
image maria_kitchen_sex 5 = "maria_body_b_sex_kitchen_anim05"
image maria_kitchen_sex 6 = "maria_body_b_sex_kitchen_anim06"
image maria_kitchen_sex 7 = "maria_body_b_sex_kitchen_anim07"



image maria_arms_sex_home_a_cumshot:
    Transform("maria_arms_sex_home_a_cumshot1")
    pause .4
    Transform("maria_arms_sex_home_a_cumshot2_comp")

image maria_arms_sex_home_a_cumshot2_comp = Composite(
    (1024,768),
    (0,0), "maria_arms_sex_home_a_cumshot2",
    (0,0), "maria_overlay_cumshot_sex_home_oc_cumshot",
    )

init python hide:
    for i in xrange(1, 8):
        renpy.image('maria_body_b_sex_home_anim {}'.format(i),
                    'maria_body_b_sex_home_anim{:02}'.format(i))

image maria_body_b_sex_home_anim = AnimatedImage(
    'maria_body_b_sex_home_anim', range(1, 8), M_maria)

init python hide:
    for o in ('mono', 'poly'):
        for i in xrange(1, 8):
            renpy.image('maria_body_b_sex_anim_3some_{} {}'.format(o, i),
                        'maria_body_b_sex_anim_3some_{}{:02}'.format(o, i))

image maria_3some mono = AnimatedImage(
    'maria_body_b_sex_anim_3some_mono', range(1, 8), M_maria)
image maria_3some poly = AnimatedImage(
    'maria_body_b_sex_anim_3some_poly', range(1, 8), M_maria)

image xray_maria_sex_3some:
    anchor (.5, .5)
    pos (250 + 167, 250 + 31)
    rotate 130
    rotate_pad False
    zoom .82
    'xray_side'





image xray_maria_back:
    Transform("characters/xray/xray_left_back_01.png", xzoom=-.6, yzoom=.6, rotate=70, xoffset=150, yoffset=220)
    pause 0.4
    Transform("characters/xray/xray_left_back_02.png", xzoom=-.6, yzoom=.6, rotate=70, xoffset=150, yoffset=220)
    pause 0.4
    Transform("characters/xray/xray_left_back_03.png", xzoom=-.6, yzoom=.6, rotate=70, xoffset=150, yoffset=220)
    pause 0.4
    Transform("characters/xray/xray_left_back_04.png", xzoom=-.6, yzoom=.6, rotate=70, xoffset=150, yoffset=220)
    pause 0.4
    Transform("characters/xray/xray_left_back_05.png", xzoom=-.6, yzoom=.6, rotate=70, xoffset=150, yoffset=220)
    pause 0.4
    Transform("characters/xray/xray_left_back_06.png", xzoom=-.6, yzoom=.6, rotate=70, xoffset=150, yoffset=220)
    pause 0.4
    Transform("characters/xray/xray_left_back_07.png", xzoom=-.6, yzoom=.6, rotate=70, xoffset=150, yoffset=220)
    pause 0.4
    Transform("characters/xray/xray_left_back_08.png", xzoom=-.6, yzoom=.6, rotate=70, xoffset=150, yoffset=220)
    pause 0.4
    Transform("characters/xray/xray_left_back_09.png", xzoom=-.6, yzoom=.6, rotate=70, xoffset=150, yoffset=220)
    pause 0.4
    Transform("characters/xray/xray_left_back_10.png", xzoom=-.6, yzoom=.6, rotate=70, xoffset=150, yoffset=220)
    pause 0.4
    Transform("characters/xray/xray_left_back_11.png", xzoom=-.6, yzoom=.6, rotate=70, xoffset=150, yoffset=220)
    pause 0.4
    Transform("characters/xray/xray_left_back_12.png", xzoom=-.6, yzoom=.6, rotate=70, xoffset=150, yoffset=220)
    pause 0.4
    Transform("characters/xray/xray_left_back_13.png", xzoom=-.6, yzoom=.6, rotate=70, xoffset=150, yoffset=220)
    pause 0.4
    Transform("characters/xray/xray_left_back_14.png", xzoom=-.6, yzoom=.6, rotate=70, xoffset=150, yoffset=220)
    pause 0.4
    Transform("characters/xray/xray_left_back_15.png", xzoom=-.6, yzoom=.6, rotate=70, xoffset=150, yoffset=220)
    pause 0.4
    Transform("characters/xray/xray_left_back_16.png", xzoom=-.6, yzoom=.6, rotate=70, xoffset=150, yoffset=220)
    pause 0.4
    Transform("characters/xray/xray_left_back_17.png", xzoom=-.6, yzoom=.6, rotate=70, xoffset=150, yoffset=220)
    pause 0.4
    Transform("characters/xray/xray_left_back_18.png", xzoom=-.6, yzoom=.6, rotate=70, xoffset=150, yoffset=220)
    pause 2.0
    linear 2.5 alpha 0

image xray_maria_kitchen:
    Transform("characters/xray/xray_side_01.png", xzoom=-.65, yzoom=.65, xoffset=345, yoffset=180)
    pause 0.4
    Transform("characters/xray/xray_side_02.png", xzoom=-.65, yzoom=.65, xoffset=345, yoffset=180)
    pause 0.4
    Transform("characters/xray/xray_side_03.png", xzoom=-.65, yzoom=.65, xoffset=345, yoffset=180)
    pause 0.4
    Transform("characters/xray/xray_side_04.png", xzoom=-.65, yzoom=.65, xoffset=345, yoffset=180)
    pause 0.4
    Transform("characters/xray/xray_side_05.png", xzoom=-.65, yzoom=.65, xoffset=345, yoffset=180)
    pause 0.4
    Transform("characters/xray/xray_side_06.png", xzoom=-.65, yzoom=.65, xoffset=345, yoffset=180)
    pause 0.4
    Transform("characters/xray/xray_side_07.png", xzoom=-.65, yzoom=.65, xoffset=345, yoffset=180)
    pause 0.4
    Transform("characters/xray/xray_side_08.png", xzoom=-.65, yzoom=.65, xoffset=345, yoffset=180)
    pause 0.4
    Transform("characters/xray/xray_side_09.png", xzoom=-.65, yzoom=.65, xoffset=345, yoffset=180)
    pause 0.4
    Transform("characters/xray/xray_side_10.png", xzoom=-.65, yzoom=.65, xoffset=345, yoffset=180)
    pause 0.4
    Transform("characters/xray/xray_side_11.png", xzoom=-.65, yzoom=.65, xoffset=345, yoffset=180)
    pause 0.4
    Transform("characters/xray/xray_side_12.png", xzoom=-.65, yzoom=.65, xoffset=345, yoffset=180)
    pause 0.4
    Transform("characters/xray/xray_side_13.png", xzoom=-.65, yzoom=.65, xoffset=345, yoffset=180)
    pause 0.4
    Transform("characters/xray/xray_side_14.png", xzoom=-.65, yzoom=.65, xoffset=345, yoffset=180)
    pause 0.4
    Transform("characters/xray/xray_side_15.png", xzoom=-.65, yzoom=.65, xoffset=345, yoffset=180)
    pause 0.4
    Transform("characters/xray/xray_side_16.png", xzoom=-.65, yzoom=.65, xoffset=345, yoffset=180)
    pause 0.4
    Transform("characters/xray/xray_side_17.png", xzoom=-.65, yzoom=.65, xoffset=345, yoffset=180)
    pause 0.4
    Transform("characters/xray/xray_side_18.png", xzoom=-.65, yzoom=.65, xoffset=345, yoffset=180)
    pause 2.0
    linear 2.5 alpha 0

image xray_maria_home:
    Transform("characters/xray/xray_side_01.png", xzoom=-.7, yzoom=.7, rotate=45, xoffset=240, yoffset=160)
    pause 0.4
    Transform("characters/xray/xray_side_02.png", xzoom=-.7, yzoom=.7, rotate=45, xoffset=240, yoffset=160)
    pause 0.4
    Transform("characters/xray/xray_side_03.png", xzoom=-.7, yzoom=.7, rotate=45, xoffset=240, yoffset=160)
    pause 0.4
    Transform("characters/xray/xray_side_04.png", xzoom=-.7, yzoom=.7, rotate=45, xoffset=240, yoffset=160)
    pause 0.4
    Transform("characters/xray/xray_side_05.png", xzoom=-.7, yzoom=.7, rotate=45, xoffset=240, yoffset=160)
    pause 0.4
    Transform("characters/xray/xray_side_06.png", xzoom=-.7, yzoom=.7, rotate=45, xoffset=240, yoffset=160)
    pause 0.4
    Transform("characters/xray/xray_side_07.png", xzoom=-.7, yzoom=.7, rotate=45, xoffset=240, yoffset=160)
    pause 0.4
    Transform("characters/xray/xray_side_08.png", xzoom=-.7, yzoom=.7, rotate=45, xoffset=240, yoffset=160)
    pause 0.4
    Transform("characters/xray/xray_side_09.png", xzoom=-.7, yzoom=.7, rotate=45, xoffset=240, yoffset=160)
    pause 0.4
    Transform("characters/xray/xray_side_10.png", xzoom=-.7, yzoom=.7, rotate=45, xoffset=240, yoffset=160)
    pause 0.4
    Transform("characters/xray/xray_side_11.png", xzoom=-.7, yzoom=.7, rotate=45, xoffset=240, yoffset=160)
    pause 0.4
    Transform("characters/xray/xray_side_12.png", xzoom=-.7, yzoom=.7, rotate=45, xoffset=240, yoffset=160)
    pause 0.4
    Transform("characters/xray/xray_side_13.png", xzoom=-.7, yzoom=.7, rotate=45, xoffset=240, yoffset=160)
    pause 0.4
    Transform("characters/xray/xray_side_14.png", xzoom=-.7, yzoom=.7, rotate=45, xoffset=240, yoffset=160)
    pause 0.4
    Transform("characters/xray/xray_side_15.png", xzoom=-.7, yzoom=.7, rotate=45, xoffset=240, yoffset=160)
    pause 0.4
    Transform("characters/xray/xray_side_16.png", xzoom=-.7, yzoom=.7, rotate=45, xoffset=240, yoffset=160)
    pause 0.4
    Transform("characters/xray/xray_side_17.png", xzoom=-.7, yzoom=.7, rotate=45, xoffset=240, yoffset=160)
    pause 0.4
    Transform("characters/xray/xray_side_18.png", xzoom=-.7, yzoom=.7, rotate=45, xoffset=240, yoffset=160)
    pause 2.0
    linear 2.5 alpha 0
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
