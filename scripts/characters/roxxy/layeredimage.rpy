init:
    $ roxxy_clothing_options = ['b_dressed','b_naked','b_shorts','b_empty','b_undies']

init python:


    renpy.image('roxxy_arms_a_empty', 'ground.png')
    renpy.image('roxxy_body_b_empty', 'ground.png')
    renpy.image('roxxy_face_f_empty', 'ground.png')
    renpy.image('roxxy_face_talk_f_empty', 'ground.png')


    renpy.image('roxxy_face_talk_f_laugh', 'roxxy_face_f_laugh')


    renpy.image('roxxy_face_f_pouting_hair', 'roxxy_face_talk_f_pouting_hair')


    renpy.image('roxxy_arms_undies_a_pullup', 'roxxy_arms_shorts_a_pullup')
    renpy.image('roxxy_arms_undies_a_remove1', 'roxxy_arms_shorts_a_remove1')

layeredimage roxxy:

    yanchor config.screen_height
    ypos 1.
    xanchor config.screen_width
    xpos 1.


    group body auto:
        attribute b_dressed default
        attribute b_empty null


    group mouth prefix 'm':
        attribute talk null

    group face:
        attribute f_normal default null







    group face if_not 'm_talk' if_any roxxy_clothing_options auto


    group face if_not 'm_talk' if_all 'b_pullup1' auto:
        offset (-60, 87)


    group face if_not 'm_talk' if_all 'b_dressed_toes' auto:
        offset (-49, -10)


    group face if_not 'm_talk' if_all 'b_desk_normal' auto:
        xzoom -1
        offset (9, 44)


    group face if_not 'm_talk' if_all 'b_desk_bored' auto:
        xzoom -1
        offset (111, 127)    











    group face if_all 'm_talk' if_any roxxy_clothing_options auto variant 'talk'


    group face if_all ['m_talk', 'b_pullup1'] auto variant 'talk':
        offset (-60, 87)


    group face if_all ['m_talk', 'b_dressed_toes'] auto variant 'talk':
        offset (-49, -10)


    group face if_all ['m_talk', 'b_desk_normal'] auto variant 'talk':
        xzoom -1
        offset (9, 44)


    group face if_all ['m_talk', 'b_desk_bored'] auto variant 'talk':
        xzoom -1
        offset (111, 127)    







    group arms if_all 'b_dressed' auto variant 'dressed':
        attribute a_idle default 'roxxy_arms_dressed_a_hips'


    group arms if_all 'b_dressed_toes' auto variant 'dressed_toes':
        attribute a_idle default 'roxxy_arms_dressed_toes_a_point'


    group arms if_all 'b_shorts' auto variant 'shorts':
        attribute a_idle default 'roxxy_arms_shorts_a_pullup'


    group arms if_all 'b_undies' auto variant 'undies':
        attribute a_idle default 'roxxy_arms_undies_a_sides'


    group arms if_all 'b_desk_normal' auto variant 'desk_normal':
        attribute a_idle default 'roxxy_arms_desk_normal_a_down'






    group overlay auto:
        attribute o_empty default null


layeredimage roxxy bed:
    always 'location_trailer_bedroom_facetime'

    group body auto:
        attribute b_rub_under anim.TransitionAnimation(
            'roxxy_bed_body_b_rub_under01', .4, Dissolve(.2),
            'roxxy_bed_body_b_rub_under02', .4, Dissolve(.2))
        attribute b_rub anim.TransitionAnimation(
            'roxxy_bed_body_b_rub01', .5, Dissolve(.3),
            'roxxy_bed_body_b_rub02', .5, Dissolve(.3))

    group mouth prefix 'm':
        attribute talk null

    group face if_all 'm_talk' auto variant 'talk'
    group face if_not 'm_talk' auto

    group cum auto
    group overlay auto:
        attribute o_stain


image roxxy_f = "characters/roxxy/layeredimage/roxxy_face_f_normal.png"

image roxxy_bed_overlay_o_stain:
    'roxxy_bed_overlay_o_wet'
    alpha 0
    linear 6 alpha 1





image xray_roxxy_3some_beach:
    Transform("characters/xray/xray_top_01.png", zoom=.6, rotate=50, xoffset=310, yoffset=300)
    pause 0.4
    Transform("characters/xray/xray_top_02.png", zoom=.6, rotate=50, xoffset=310, yoffset=300)
    pause 0.4
    Transform("characters/xray/xray_top_03.png", zoom=.6, rotate=50, xoffset=310, yoffset=300)
    pause 0.4
    Transform("characters/xray/xray_top_04.png", zoom=.6, rotate=50, xoffset=310, yoffset=300)
    pause 0.4
    Transform("characters/xray/xray_top_05.png", zoom=.6, rotate=50, xoffset=310, yoffset=300)
    pause 0.4
    Transform("characters/xray/xray_top_06.png", zoom=.6, rotate=50, xoffset=310, yoffset=300)
    pause 0.4
    Transform("characters/xray/xray_top_07.png", zoom=.6, rotate=50, xoffset=310, yoffset=300)
    pause 0.4
    Transform("characters/xray/xray_top_08.png", zoom=.6, rotate=50, xoffset=310, yoffset=300)
    pause 0.4
    Transform("characters/xray/xray_top_09.png", zoom=.6, rotate=50, xoffset=310, yoffset=300)
    pause 0.4
    Transform("characters/xray/xray_top_10.png", zoom=.6, rotate=50, xoffset=310, yoffset=300)
    pause 0.4
    Transform("characters/xray/xray_top_11.png", zoom=.6, rotate=50, xoffset=310, yoffset=300)
    pause 0.4
    Transform("characters/xray/xray_top_12.png", zoom=.6, rotate=50, xoffset=310, yoffset=300)
    pause 0.4
    Transform("characters/xray/xray_top_13.png", zoom=.6, rotate=50, xoffset=310, yoffset=300)
    pause 0.4
    Transform("characters/xray/xray_top_14.png", zoom=.6, rotate=50, xoffset=310, yoffset=300)
    pause 0.4
    Transform("characters/xray/xray_top_15.png", zoom=.6, rotate=50, xoffset=310, yoffset=300)
    pause 0.4
    Transform("characters/xray/xray_top_16.png", zoom=.6, rotate=50, xoffset=310, yoffset=300)
    pause 0.4
    Transform("characters/xray/xray_top_17.png", zoom=.6, rotate=50, xoffset=310, yoffset=300)
    pause 0.4
    Transform("characters/xray/xray_top_18.png", zoom=.6, rotate=50, xoffset=310, yoffset=300)
    pause 2.0
    linear 2.5 alpha 0

image xray_roxxy_1o1_beach:
    Transform("characters/xray/xray_front_top_01.png", zoom=.7, rotate=270, xoffset=370, yoffset=30)
    pause 0.4
    Transform("characters/xray/xray_front_top_02.png", zoom=.7, rotate=270, xoffset=370, yoffset=30)
    pause 0.4
    Transform("characters/xray/xray_front_top_03.png", zoom=.7, rotate=270, xoffset=370, yoffset=30)
    pause 0.4
    Transform("characters/xray/xray_front_top_04.png", zoom=.7, rotate=270, xoffset=370, yoffset=30)
    pause 0.4
    Transform("characters/xray/xray_front_top_05.png", zoom=.7, rotate=270, xoffset=370, yoffset=30)
    pause 0.4
    Transform("characters/xray/xray_front_top_06.png", zoom=.7, rotate=270, xoffset=370, yoffset=30)
    pause 0.4
    Transform("characters/xray/xray_front_top_07.png", zoom=.7, rotate=270, xoffset=370, yoffset=30)
    pause 0.4
    Transform("characters/xray/xray_front_top_08.png", zoom=.7, rotate=270, xoffset=370, yoffset=30)
    pause 0.4
    Transform("characters/xray/xray_front_top_09.png", zoom=.7, rotate=270, xoffset=370, yoffset=30)
    pause 0.4
    Transform("characters/xray/xray_front_top_10.png", zoom=.7, rotate=270, xoffset=370, yoffset=30)
    pause 0.4
    Transform("characters/xray/xray_front_top_11.png", zoom=.7, rotate=270, xoffset=370, yoffset=30)
    pause 0.4
    Transform("characters/xray/xray_front_top_12.png", zoom=.7, rotate=270, xoffset=370, yoffset=30)
    pause 0.4
    Transform("characters/xray/xray_front_top_13.png", zoom=.7, rotate=270, xoffset=370, yoffset=30)
    pause 0.4
    Transform("characters/xray/xray_front_top_14.png", zoom=.7, rotate=270, xoffset=370, yoffset=30)
    pause 0.4
    Transform("characters/xray/xray_front_top_15.png", zoom=.7, rotate=270, xoffset=370, yoffset=30)
    pause 0.4
    Transform("characters/xray/xray_front_top_16.png", zoom=.7, rotate=270, xoffset=370, yoffset=30)
    pause 0.4
    Transform("characters/xray/xray_front_top_17.png", zoom=.7, rotate=270, xoffset=370, yoffset=30)
    pause 0.4
    Transform("characters/xray/xray_front_top_18.png", zoom=.7, rotate=270, xoffset=370, yoffset=30)
    pause 2.0
    linear 2.5 alpha 0

image xray_roxxy_locker:
    Transform("characters/xray/xray_side_01.png", xzoom=-.5, yzoom=.5, rotate=-60, xoffset=410, yoffset=330)
    pause 0.4
    Transform("characters/xray/xray_side_02.png", xzoom=-.5, yzoom=.5, rotate=-60, xoffset=410, yoffset=330)
    pause 0.4
    Transform("characters/xray/xray_side_03.png", xzoom=-.5, yzoom=.5, rotate=-60, xoffset=410, yoffset=330)
    pause 0.4
    Transform("characters/xray/xray_side_04.png", xzoom=-.5, yzoom=.5, rotate=-60, xoffset=410, yoffset=330)
    pause 0.4
    Transform("characters/xray/xray_side_05.png", xzoom=-.5, yzoom=.5, rotate=-60, xoffset=410, yoffset=330)
    pause 0.4
    Transform("characters/xray/xray_side_06.png", xzoom=-.5, yzoom=.5, rotate=-60, xoffset=410, yoffset=330)
    pause 0.4
    Transform("characters/xray/xray_side_07.png", xzoom=-.5, yzoom=.5, rotate=-60, xoffset=410, yoffset=330)
    pause 0.4
    Transform("characters/xray/xray_side_08.png", xzoom=-.5, yzoom=.5, rotate=-60, xoffset=410, yoffset=330)
    pause 0.4
    Transform("characters/xray/xray_side_09.png", xzoom=-.5, yzoom=.5, rotate=-60, xoffset=410, yoffset=330)
    pause 0.4
    Transform("characters/xray/xray_side_10.png", xzoom=-.5, yzoom=.5, rotate=-60, xoffset=410, yoffset=330)
    pause 0.4
    Transform("characters/xray/xray_side_11.png", xzoom=-.5, yzoom=.5, rotate=-60, xoffset=410, yoffset=330)
    pause 0.4
    Transform("characters/xray/xray_side_12.png", xzoom=-.5, yzoom=.5, rotate=-60, xoffset=410, yoffset=330)
    pause 0.4
    Transform("characters/xray/xray_side_13.png", xzoom=-.5, yzoom=.5, rotate=-60, xoffset=410, yoffset=330)
    pause 0.4
    Transform("characters/xray/xray_side_14.png", xzoom=-.5, yzoom=.5, rotate=-60, xoffset=410, yoffset=330)
    pause 0.4
    Transform("characters/xray/xray_side_15.png", xzoom=-.5, yzoom=.5, rotate=-60, xoffset=410, yoffset=330)
    pause 0.4
    Transform("characters/xray/xray_side_16.png", xzoom=-.5, yzoom=.5, rotate=-60, xoffset=410, yoffset=330)
    pause 0.4
    Transform("characters/xray/xray_side_17.png", xzoom=-.5, yzoom=.5, rotate=-60, xoffset=410, yoffset=330)
    pause 0.4
    Transform("characters/xray/xray_side_18.png", xzoom=-.5, yzoom=.5, rotate=-60, xoffset=410, yoffset=330)
    pause 2.0
    linear 2.5 alpha 0

image xray_roxxy_trailer_bed:
    offset (400, 350)
    zoom .5
    'xray_front_under'



init python hide:
    count = 13
    first = 9
    frames = tuple(i % count + 1 for i in xrange(first, first + count))

    map = (('roxxy_sex_boobjob_anim', 'roxxy_boobjob'),)

    for src, stem in map:
        for i in frames:
            renpy.image('{} {}'.format(stem, i),
                        '{}{:02}'.format(src, i))
        
        renpy.image(stem, AnimatedImage(stem, frames, M_roxxy))

layeredimage roxxy sex_boobjob:
    attribute m_talk null
    attribute o_cum null

    group face if_not 'm_talk':
        attribute f_idle default null
        attribute f_spit 'roxxy_sex_boobjob_face_spit'
        attribute f_lick 'roxxy_sex_boobjob_face_lick'
        attribute f_laugh 'roxxy_sex_boobjob_face_laugh'

    group face if_all 'm_talk':
        attribute f_idle 'roxxy_sex_boobjob_face_talk'

    group cum if_any 'o_cum' if_not 'm_talk':
        attribute f_idle 'roxxy_sex_boobjob_after_cum_idle'
        attribute f_lick 'roxxy_sex_boobjob_after_cum_lick'

    group cum if_any 'o_cum' if_all 'm_talk':
        attribute f_idle 'roxxy_sex_boobjob_after_cum_talk'

image roxxy_sex_boobjob_face_spit:
    contains:
        'roxxy_sex_boobjob_insert_face_spit'
    contains:
        'roxxy_sex_boobjob_insert_spit1'
        .5
        'roxxy_sex_boobjob_insert_spit2' with dissolve
        .5
        'roxxy_sex_boobjob_insert_spit3' with dissolve
        .5
        linear .8 alpha 0

image roxxy_sex_boobjob_cumshot:
    'roxxy_sex_boobjob_cumshot1'
    .4
    'roxxy_sex_boobjob_cumshot2' with fastdissolve
    .4
    'roxxy_sex_boobjob_cumshot3' with fastdissolve



init python hide:
    count = 12
    first = 1
    frames = tuple(i % count + 1 for i in xrange(first, first + count))

    map = (('roxxy_sex_bj_anim', 'roxxy_blowjob'),)

    for src, stem in map:
        for i in frames:
            renpy.image('{} {}'.format(stem, i),
                        '{}{:02}'.format(src, i))
        
        renpy.image(stem, AnimatedImage(stem, frames, M_roxxy))

layeredimage roxxy sex_bj_after:
    attribute m_talk null

    group face if_not 'm_talk':
        attribute f_tired default 'roxxy_sex_bj_after_idle'
        attribute f_happy 'roxxy_sex_bj_after_happy_idle'

    group face if_all 'm_talk':
        attribute f_tired default 'roxxy_sex_bj_after_talk'
        attribute f_happy 'roxxy_sex_bj_after_happy_talk'

image roxxy_sex_bj_cum_drip:
    'roxxy_sex_bj_cum_drip1'
    .4
    'roxxy_sex_bj_cum_drip2' with fastdissolve
    .4
    'roxxy_sex_bj_cum_drip3' with fastdissolve
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
