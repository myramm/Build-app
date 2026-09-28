init:
    $ tina_clothing_options = ['b_dressed','b_dressed_hug_maria','b_dressed_open','b_dressed_open_boobs','b_dressed_open_boobs_drop01','b_dressed_open_boobs_drop02','b_dressed_open_boobs_drop03','b_dressed_open_boobs_drop04','b_empty','b_magic','b_naked','b_casual','b_lingerie','b_panties','b_naked_disheveled','b_naked_crossed','b_panties_grope1','b_panties_grope2','b_panties_grope','b_panties_kiss1','b_panties_kiss2','b_panties_reveal1','b_panties_reveal2','b_lingerie_showoff']

init python:


    renpy.image('tina_arms_a_empty', 'ground.png')
    renpy.image('tina_body_b_empty', 'ground.png')
    renpy.image('tina_face_f_empty', 'ground.png')
    renpy.image('tina_face_talk_f_empty', 'ground.png')


    renpy.image('tina_face_talk_f_laugh', 'tina_face_f_laugh')
    renpy.image('tina_face_talk_f_surprised_down', 'tina_face_f_surprised_down')
    renpy.image('tina_face_doorway_talk_f_laugh', 'tina_face_doorway_f_laugh')
    renpy.image('tina_face_sex_talk_f_moan', 'tina_face_sex_f_moan')



layeredimage tina:

    yanchor config.screen_height
    ypos 1.
    xanchor config.screen_width
    xpos 1.


    group body auto:
        attribute b_dressed default
        attribute b_empty null
        attribute b_panties_grope 'tina_body_b_panties_grope'
        attribute b_panties_kiss 'tina_body_b_panties_kiss'
        attribute b_dressed_open_boobs_kiss 'tina_body_b_dressed_open_boobs_kiss'
        attribute b_magic "tina_body_b_[M_tina.outfit.get][M_tina.pregnancy.to_string]"   


    group mouth prefix 'm':
        attribute talk null

    group face:
        attribute f_normal default null







    group face if_not 'm_talk' if_any tina_clothing_options auto


    group face if_not 'm_talk' if_any ['b_panties_knees'] auto:
        offset (-237,126)


    group face if_not 'm_talk' if_any ['b_gown_bed'] auto:
        offset (108, 45)


    group face if_not 'm_talk' if_any ['b_sex_inbetween'] auto:
        align (.5, .5)
        offset (-196, -183)
        rotate -3.75
        rotate_pad False






    group face if_not 'm_talk' if_any 'b_sex_talk' auto variant 'sex'


    group face if_not 'm_talk' if_any ['b_doorway'] auto variant 'doorway':
        attribute f_normal default 'tina_face_doorway_f_sexy'







    group face if_all 'm_talk' if_any tina_clothing_options auto variant 'talk'


    group face if_all 'm_talk' if_any ['b_panties_knees'] auto variant 'talk':
        offset (-237,126)


    group face if_all ['m_talk', 'b_gown_bed'] auto variant 'talk':
        offset (108, 45)


    group face if_all 'm_talk' if_any ['b_sex_inbetween'] auto variant 'talk':
        align (.5, .5)
        offset (-196, -183)
        rotate -3.75
        rotate_pad False






    group face if_all 'm_talk' if_any 'b_sex_talk' auto variant 'sex_talk'


    group face if_all 'm_talk' if_any ['b_doorway'] auto variant 'doorway_talk':
        attribute f_normal default 'tina_face_doorway_talk_f_sexy'



    group arms if_all 'b_dressed' auto variant 'dressed':
        attribute a_idle default 'tina_arms_dressed_a_hips'
        attribute a_baby "tina_arms_dressed_a_baby_[M_tina.pregnancy.baby_gender]"


    group arms if_all 'b_dressed_open' auto variant 'dressed_open':
        attribute a_idle default "tina_arms_dressed_open_a_pull"



    group arms if_all 'b_dressed_open_boobs' auto variant 'dressed_open_boobs':
        attribute a_idle default "tina_arms_dressed_open_boobs_a_hips"       


    group arms if_all 'b_gown_bed' auto variant 'gown_bed':
        attribute a_idle default "tina_arms_gown_bed_a_baby_[M_tina.pregnancy.baby_gender]"


    group arms if_all 'b_magic' auto:
        attribute a_idle default 'tina_arms_[M_tina.outfit.get]_a_touch[M_tina.pregnancy.to_string]'
        attribute a_point 'tina_arms_dressed_a_point'
        attribute a_blow_kiss 'tina_arms_dressed_a_blow_kiss'
        attribute a_pinch 'tina_arms_dressed_a_pinch'


    group arms if_any ['b_casual'] auto variant 'casual':
        attribute a_idle default 'tina_arms_casual_a_hips'
        attribute a_baby "tina_arms_casual_a_baby_[M_tina.pregnancy.baby_gender]"


    group arms if_any ['b_lingerie'] auto variant 'lingerie':
        attribute a_idle default 'tina_arms_lingerie_a_hips'
        attribute a_baby "tina_arms_lingerie_a_baby_[M_tina.pregnancy.baby_gender]"
        attribute a_squeeze "tina_arms_lingerie_a_squeeze"


    group arms if_any ['b_panties_knees'] auto variant 'panties_knees': 
        attribute a_idle default 'tina_arms_panties_knees_a_up'         
        attribute a_jerk 'tina_arms_panties_knees_a_jerk'


    group arms if_any ['b_dressed_open_back'] auto variant 'dressed_open_back':
        attribute a_idle default 'tina_arms_dressed_open_back_a_undress'


    group arms if_any ['b_naked','b_naked_disheveled','b_panties'] auto variant 'naked':
        attribute a_idle default 'tina_arms_naked_a_hips'
        attribute a_touch 'tina_arms_naked_a_touch[M_tina.pregnancy.to_string]'


    group overlay auto:
        attribute o_empty default null

image tina_f = "characters/tina/tina_face_f_normal.png"

image tina_arms_naked_a_touch = "characters/tina/tina_arms_naked_a_hips.png"
image tina_arms_dressed_a_touch = "characters/tina/tina_arms_dressed_a_hips.png"
image tina_arms_casual_a_touch = "characters/tina/tina_arms_casual_a_hips.png"

image tina_arms_panties_knees_a_jerk:
    Transform("tina_arms_panties_knees_a_jerk1")
    pause .4
    Transform("tina_arms_panties_knees_a_jerk2")
    pause .4
    repeat

image tina_arms_lingerie_a_squeeze:
    Transform("tina_arms_lingerie_a_squeeze1")
    pause .4
    Transform("tina_arms_lingerie_a_squeeze2")
    pause .4
    repeat

image tina_body_b_panties_grope:
    Transform("tina_body_b_panties_grope1")
    pause .4
    Transform("tina_body_b_panties_grope2")
    pause .4
    repeat

image tina_body_b_dressed_open_boobs_kiss:
    Transform("tina_body_b_dressed_open_boobs_kiss1")
    pause .4
    Transform("tina_body_b_dressed_open_boobs_kiss2")
    pause .4
    repeat

image tina_body_b_panties_kiss:
    Transform("tina_body_b_panties_kiss1")
    pause .4
    Transform("tina_body_b_panties_kiss2")
    pause .4
    repeat


init python hide:
    count = 6
    first = 1
    frames = tuple(i % count + 1 for i in xrange(first, first + count))

    map = (('tina_body_b_sex_anim', 'tina_lounge_cowgirl'),)

    for src, stem in map:
        for i in frames:
            renpy.image('{} {}'.format(stem, i),
                        '{}{:02}'.format(src, i))
        
        renpy.image(stem, AnimatedImage(stem, frames, M_tina))


image tina_sex_body_cumshot_dick:
    Transform("tina_sex_body_cumshot_dick1")
    pause .4
    Transform("tina_sex_body_cumshot_dick2")
    pause .4
    Transform("tina_sex_body_cumshot_dick3")



image anon_sex_office_base = "tina_body_b_sex_office_base_mc"

image anon_sex_office_dick pre = "tina_overlay_o_sex_office_dick_pre"
image anon_sex_office_dick after = "tina_overlay_o_sex_office_dick_after"
image anon_sex_office_dick cumshot:
    Transform("tina_overlay_o_sex_office_dick_cumshot1")
    pause .4
    Transform("tina_overlay_o_sex_office_dick_cumshot2")
    pause .4
    Transform("tina_overlay_o_sex_office_dick_cumshot3_comp")

image tina_overlay_o_sex_office_dick_cumshot3_comp = Composite(
    (1025,768),
    (0,0), "characters/tina/tina_overlay_o_sex_office_dick_pre.png",
    (0,0), "characters/tina/tina_overlay_o_sex_office_dick_cumshot3.png",
    )

init python:
    for i in xrange(1, 9):
        renpy.image('tina_body_b_sex_office_anim {}'.format(i),
                    'tina_body_b_sex_office_anim{:02}'.format(i))

image tina_body_b_sex_office_anim = AnimatedImage('tina_body_b_sex_office_anim',
                                           (1,2,3,4,5,6,7,8),
                                           M_tina)





image xray_tina_top:
    Transform("characters/xray/xray_side_01.png", xzoom=-.6, yzoom=.6, rotate=-120, xoffset=500, yoffset=70)
    pause 0.4
    Transform("characters/xray/xray_side_02.png", xzoom=-.6, yzoom=.6, rotate=-120, xoffset=500, yoffset=70)
    pause 0.4
    Transform("characters/xray/xray_side_03.png", xzoom=-.6, yzoom=.6, rotate=-120, xoffset=500, yoffset=70)
    pause 0.4
    Transform("characters/xray/xray_side_04.png", xzoom=-.6, yzoom=.6, rotate=-120, xoffset=500, yoffset=70)
    pause 0.4
    Transform("characters/xray/xray_side_05.png", xzoom=-.6, yzoom=.6, rotate=-120, xoffset=500, yoffset=70)
    pause 0.4
    Transform("characters/xray/xray_side_06.png", xzoom=-.6, yzoom=.6, rotate=-120, xoffset=500, yoffset=70)
    pause 0.4
    Transform("characters/xray/xray_side_07.png", xzoom=-.6, yzoom=.6, rotate=-120, xoffset=500, yoffset=70)
    pause 0.4
    Transform("characters/xray/xray_side_08.png", xzoom=-.6, yzoom=.6, rotate=-120, xoffset=500, yoffset=70)
    pause 0.4
    Transform("characters/xray/xray_side_09.png", xzoom=-.6, yzoom=.6, rotate=-120, xoffset=500, yoffset=70)
    pause 0.4
    Transform("characters/xray/xray_side_10.png", xzoom=-.6, yzoom=.6, rotate=-120, xoffset=500, yoffset=70)
    pause 0.4
    Transform("characters/xray/xray_side_11.png", xzoom=-.6, yzoom=.6, rotate=-120, xoffset=500, yoffset=70)
    pause 0.4
    Transform("characters/xray/xray_side_12.png", xzoom=-.6, yzoom=.6, rotate=-120, xoffset=500, yoffset=70)
    pause 0.4
    Transform("characters/xray/xray_side_13.png", xzoom=-.6, yzoom=.6, rotate=-120, xoffset=500, yoffset=70)
    pause 0.4
    Transform("characters/xray/xray_side_14.png", xzoom=-.6, yzoom=.6, rotate=-120, xoffset=500, yoffset=70)
    pause 0.4
    Transform("characters/xray/xray_side_15.png", xzoom=-.6, yzoom=.6, rotate=-120, xoffset=500, yoffset=70)
    pause 0.4
    Transform("characters/xray/xray_side_16.png", xzoom=-.6, yzoom=.6, rotate=-120, xoffset=500, yoffset=70)
    pause 0.4
    Transform("characters/xray/xray_side_17.png", xzoom=-.6, yzoom=.6, rotate=-120, xoffset=500, yoffset=70)
    pause 0.4
    Transform("characters/xray/xray_side_18.png", xzoom=-.6, yzoom=.6, rotate=-120, xoffset=500, yoffset=70)
    pause 2.0
    linear 2.5 alpha 0

image xray_tina_office:
    Transform("characters/xray/xray_left_back_01.png", xzoom=-.7, yzoom=.7, rotate=-10, xoffset=260, yoffset=120)
    pause 0.4
    Transform("characters/xray/xray_left_back_02.png", xzoom=-.7, yzoom=.7, rotate=-10, xoffset=260, yoffset=120)
    pause 0.4
    Transform("characters/xray/xray_left_back_03.png", xzoom=-.7, yzoom=.7, rotate=-10, xoffset=260, yoffset=120)
    pause 0.4
    Transform("characters/xray/xray_left_back_04.png", xzoom=-.7, yzoom=.7, rotate=-10, xoffset=260, yoffset=120)
    pause 0.4
    Transform("characters/xray/xray_left_back_05.png", xzoom=-.7, yzoom=.7, rotate=-10, xoffset=260, yoffset=120)
    pause 0.4
    Transform("characters/xray/xray_left_back_06.png", xzoom=-.7, yzoom=.7, rotate=-10, xoffset=260, yoffset=120)
    pause 0.4
    Transform("characters/xray/xray_left_back_07.png", xzoom=-.7, yzoom=.7, rotate=-10, xoffset=260, yoffset=120)
    pause 0.4
    Transform("characters/xray/xray_left_back_08.png", xzoom=-.7, yzoom=.7, rotate=-10, xoffset=260, yoffset=120)
    pause 0.4
    Transform("characters/xray/xray_left_back_09.png", xzoom=-.7, yzoom=.7, rotate=-10, xoffset=260, yoffset=120)
    pause 0.4
    Transform("characters/xray/xray_left_back_10.png", xzoom=-.7, yzoom=.7, rotate=-10, xoffset=260, yoffset=120)
    pause 0.4
    Transform("characters/xray/xray_left_back_11.png", xzoom=-.7, yzoom=.7, rotate=-10, xoffset=260, yoffset=120)
    pause 0.4
    Transform("characters/xray/xray_left_back_12.png", xzoom=-.7, yzoom=.7, rotate=-10, xoffset=260, yoffset=120)
    pause 0.4
    Transform("characters/xray/xray_left_back_13.png", xzoom=-.7, yzoom=.7, rotate=-10, xoffset=260, yoffset=120)
    pause 0.4
    Transform("characters/xray/xray_left_back_14.png", xzoom=-.7, yzoom=.7, rotate=-10, xoffset=260, yoffset=120)
    pause 0.4
    Transform("characters/xray/xray_left_back_15.png", xzoom=-.7, yzoom=.7, rotate=-10, xoffset=260, yoffset=120)
    pause 0.4
    Transform("characters/xray/xray_left_back_16.png", xzoom=-.7, yzoom=.7, rotate=-10, xoffset=260, yoffset=120)
    pause 0.4
    Transform("characters/xray/xray_left_back_17.png", xzoom=-.7, yzoom=.7, rotate=-10, xoffset=260, yoffset=120)
    pause 0.4
    Transform("characters/xray/xray_left_back_18.png", xzoom=-.7, yzoom=.7, rotate=-10, xoffset=260, yoffset=120)
    pause 2.0
    linear 2.5 alpha 0


init python hide:
    count = 10
    first = 1
    frames = tuple(i % count + 1 for i in xrange(first, first + count))

    map = (('tina_body_b_sex_doggy_anim', 'tina_lounge_doggy'),)

    for src, stem in map:
        for i in frames:
            renpy.image('{} {}'.format(stem, i),
                        '{}{:02}'.format(src, i))
        
        renpy.image(stem, AnimatedImage(stem, frames, M_tina))
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
