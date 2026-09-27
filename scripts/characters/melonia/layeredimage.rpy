init:
    $ melonia_clothing_options = ['b_dressed','b_naked','b_dressed_magic','b_naked_disheveled','b_dressed_pregnant_bump','b_dressed_pregnant_belly','b_dressed_undress2','b_dressed_undress5','b_dressed_undress6','b_dressed_undress7','b_naked_push','b_swimsuit','b_swimsuit_bottom','b_swimsuit_hatless','b_swimsuit_remove2','b_swimsuit_remove3','b_swimsuit_remove4','b_undies','b_panties_blank','b_magic']

init python:


    renpy.image('melonia_arms_a_empty', 'ground.png')
    renpy.image('melonia_body_b_empty', 'ground.png')
    renpy.image('melonia_face_f_empty', 'ground.png')
    renpy.image('melonia_face_talk_f_empty', 'ground.png')


    renpy.image('melonia_face_talk_f_laugh', 'melonia_face_f_laugh')
    renpy.image('melonia_face_talk_f_smirk_lipbite_moan', 'melonia_face_f_smirk_lipbite_moan')


    renpy.image('melonia_face_f_yell', 'melonia_face_talk_f_yell')
    renpy.image('melonia_face_sex_f_moan', 'melonia_face_sex_talk_f_moan')

layeredimage melonia:

    yanchor config.screen_height
    ypos 1.
    xanchor config.screen_width
    xpos 1.


    group body auto:
        attribute b_dressed default
        attribute b_empty null
        attribute b_magic "melonia_body_b_[M_melonia.outfit.get][M_melonia.pregnancy.to_string]"   

        attribute b_dressed_magic "melonia_body_b_dressed[M_melonia.pregnancy.to_string]"   

        attribute b_naked_kiss 'melonia_body_b_naked_kiss'
        attribute b_dressed_kiss 'melonia_body_dressed_b_kiss'
        attribute b_jacuzzi_big 'location_rump_backyard_jacuzzi_melonia'
        attribute b_sex_anim_hard 'melonia_body_b_sex_anim_hard'


    group mouth prefix 'm':
        attribute talk null

    group face:
        attribute f_normal default null







    group face if_not 'm_talk' if_any melonia_clothing_options auto


    group face if_not 'm_talk' if_all 'b_naked_sexy' auto:
        offset (6, 6)


    group face if_not 'm_talk' if_all 'b_dressed_mad' auto:
        offset (-66, 8)


    group face if_not 'm_talk' if_all 'b_swimsuit_push' auto:
        offset (-14, -4)


    group face if_not 'm_talk' if_any ['b_jacuzzi','b_jacuzzi_hatless','b_jacuzzi_topless','b_jacuzzi_topless_remove2','b_jacuzzi_topless_remove3'] auto:
        offset (0, 68)


    group face if_not 'm_talk' if_any ['b_jacuzzi_topless_edge','b_jacuzzi_edge'] auto:
        offset (-62, 84)


    group face if_not 'm_talk' if_any 'b_jacuzzi_forward' auto:
        offset (-126, 70)


    group face if_not 'm_talk' if_any 'b_jacuzzi_topless_getout' auto:
        offset (-35, 31)


    group face if_not 'm_talk' if_any 'b_jacuzzi_topless_leaning' auto:
        offset (-38, 58)


    group face if_not 'm_talk' if_any 'b_onbed_naked_belly' auto:
        xzoom -1
        offset (519, 214)


    group face if_not 'm_talk' if_any 'b_onbed_naked_belly_getup' auto:
        xzoom -1
        offset (530, 180)


    group face if_not 'm_talk' if_any ['b_swimsuit_pulling_anon','b_swimsuit_hatless_pulling_anon','b_naked_pulling_anon'] auto:
        xzoom -1
        offset (431, -4)


    group face if_not 'm_talk' if_any 'b_gown_bed' auto:
        offset (98, 53)

    group face if_not 'm_talk' if_any 'b_onbed_naked_belly_turn' auto:
        align (.5, .5)
        offset (-74, 215)
        rotate .5
        rotate_pad False
        zoom 1.01






    group face if_not 'm_talk' if_any ['b_sex_pre_after', 'b_sex_insert_pullout'] auto variant 'sex'


    group face if_not 'm_talk' if_any 'b_onbed_naked_back' auto variant 'onbed_naked_back'







    group face if_all 'm_talk' if_any melonia_clothing_options auto variant 'talk'


    group face if_all 'm_talk' if_any 'b_dressed_mad' auto variant 'talk':
        offset (-66, 8)


    group face if_all ['m_talk', 'b_naked_sexy'] auto variant 'talk':
        offset (6, 6)


    group face if_all ['m_talk', 'b_swimsuit_push'] auto variant 'talk':
        offset (-14, -4)


    group face if_all 'm_talk' if_any ['b_jacuzzi','b_jacuzzi_hatless','b_jacuzzi_topless','b_jacuzzi_topless_remove2','b_jacuzzi_topless_remove3'] auto variant 'talk':
        offset (0, 68)


    group face if_all 'm_talk' if_any ['b_jacuzzi_topless_edge','b_jacuzzi_edge'] auto variant 'talk':
        offset (-62, 84)


    group face if_all 'm_talk' if_any 'b_jacuzzi_forward' auto variant 'talk':
        offset (-126, 70)


    group face if_all 'm_talk' if_any 'b_jacuzzi_topless_getout' auto variant 'talk':
        offset (-35, 31)


    group face if_all 'm_talk' if_any 'b_jacuzzi_topless_leaning' auto variant 'talk':
        offset (-38, 58)


    group face if_all 'm_talk' if_any 'b_onbed_naked_belly' auto variant 'talk':
        xzoom -1
        offset (519, 214)


    group face if_all 'm_talk' if_any 'b_onbed_naked_belly_getup' auto variant 'talk':
        xzoom -1
        offset (530, 180)


    group face if_all 'm_talk' if_any ['b_swimsuit_pulling_anon','b_swimsuit_hatless_pulling_anon','b_naked_pulling_anon'] auto variant 'talk':
        xzoom -1
        offset (431, -4)


    group face if_all ['m_talk', 'b_gown_bed'] auto variant 'talk':
        offset (98, 53)

    group face if_all 'm_talk' if_any 'b_onbed_naked_belly_turn' auto variant 'talk':
        align (.5, .5)
        offset (-74, 215)
        rotate .5
        rotate_pad False
        zoom 1.01






    group face if_all 'm_talk' if_any ['b_sex_pre_after', 'b_sex_insert_pullout'] auto variant 'sex_talk'


    group face if_all 'm_talk' if_any 'b_onbed_naked_back' auto variant 'onbed_naked_back_talk'


    group face if_all 'm_talk' if_any ['b_jacuzzi_big'] auto variant 'jacuzzi_big_talk'



    group arms if_all 'b_dressed' auto variant 'dressed':
        attribute a_idle default 'melonia_arms_dressed_a_hips'
        attribute a_baby "melonia_arms_dressed_a_baby_[M_melonia.pregnancy.baby_gender]"

        attribute a_baby_give "melonia_arms_dressed_a_baby_[M_melonia.pregnancy.baby_gender]_memberi"



    group arms if_all 'b_jacuzzi_forward' auto variant 'jacuzzi_forward':
        attribute a_idle default 'melonia_arms_jacuzzi_forward_a_down'
        attribute a_massage 'melonia_arms_jacuzzi_forward_a_massage'


    group arms if_all 'b_jacuzzi_topless_leaning' auto variant 'jacuzzi_topless_leaning':
        attribute a_idle default 'melonia_arms_jacuzzi_topless_leaning_a_down'
        attribute a_massage 'melonia_arms_jacuzzi_topless_leaning_a_massage'


    group arms if_all 'b_sex_pre_after' auto variant 'sex_pre_after':
        attribute a_idle default 'melonia_arms_sex_pre_after_a_pre'
        attribute a_after 'melonia_arms_sex_pre_after_a_after'


    group arms if_all 'b_sex_insert_pullout' auto variant 'sex_insert_pullout':
        attribute a_idle default 'melonia_arms_sex_insert_pullout_a_insert'
        attribute a_cumshot 'melonia_arms_sex_insert_pullout_a_cumshot'
        attribute a_empty null


    group arms if_all 'b_gown_bed' auto variant 'gown_bed':
        attribute a_idle default "melonia_arms_gown_bed_a_baby_[M_melonia.pregnancy.baby_gender]"

        attribute a_baby_give "melonia_arms_gown_bed_a_baby_give_[M_melonia.pregnancy.baby_gender]"



    group arms if_all 'b_magic' auto:
        attribute a_idle default 'melonia_arms_[M_melonia.outfit.get]_a_touch[M_melonia.pregnancy.to_string]'
        attribute a_undress1 'melonia_arms_dressed_a_undress1'
        attribute a_point 'melonia_arms_dressed_a_point'
        attribute a_fists 'melonia_arms_[M_melonia.outfit.get][M_melonia.pregnancy.to_string]_a_fists'


    group arms if_all 'b_dressed_magic' auto variant 'dressed':
        attribute a_idle default 'melonia_arms_dressed_a_touch[M_melonia.pregnancy.to_string]'
        attribute a_blow_kiss 'melonia_arms_dressed_a_blow_kiss'
        attribute a_thinking 'melonia_arms_dressed_a_thinking'


    group arms if_any ['b_jacuzzi','b_jacuzzi_hatless'] auto variant 'jacuzzi':
        attribute a_idle default 'melonia_arms_jacuzzi_a_sides'


    group arms if_any ['b_jacuzzi_topless'] auto variant 'jacuzzi_topless':
        attribute a_idle default 'melonia_arms_jacuzzi_topless_a_sides'
        attribute a_clap 'melonia_arms_jacuzzi_a_clap'


    group arms if_any ['b_swimsuit','b_swimsuit_hatless'] auto variant 'swimsuit':
        attribute a_idle default 'melonia_arms_swimsuit_a_hips'


    group arms if_any ['b_undies'] auto variant 'undies':
        attribute a_idle default 'melonia_arms_undies_a_hips'


    group arms if_any ['b_panties_blank'] auto variant 'panties_blank':
        attribute a_idle default 'melonia_arms_panties_blank_a_pull_bra1'


    group arms if_any ['b_naked','b_swimsuit_bottom','b_naked_disheveled'] auto variant 'naked':
        attribute a_idle default 'melonia_arms_naked_a_hips'


    group overlay if_not ['b_onbed_naked_back', 'b_onbed_naked_belly_turn'] auto:
        attribute o_empty default null

    group overlay if_any 'b_onbed_naked_back' auto variant 'onbed_naked_back'
    group overlay if_any 'b_onbed_naked_belly_turn' auto variant 'onbed_naked_belly_turn'


image melonia_f = "characters/melonia/melonia_face_f_normal.png"

image melonia_arms_dressed_a_touch = "characters/melonia/melonia_arms_dressed_a_hips.png"
image melonia_arms_naked_a_touch = "characters/melonia/melonia_arms_naked_a_hips.png"
image melonia_arms_swimsuit_a_touch = "characters/melonia/melonia_arms_swimsuit_a_hips.png"

image melonia_body_dressed_b_kiss:
    Transform("melonia_body_dressed_b_kiss1")
    pause .4
    Transform("melonia_body_dressed_b_kiss2")
    pause .4
    repeat

image melonia_body_b_naked_kiss:
    Transform("melonia_body_b_naked_kiss1")
    pause .4
    Transform("melonia_body_b_naked_kiss2")
    pause .4
    repeat

image melonia_arms_jacuzzi_forward_a_massage:
    Transform("melonia_arms_jacuzzi_forward_a_massage1")
    pause .4
    Transform("melonia_arms_jacuzzi_forward_a_massage2")
    pause .4
    repeat

image melonia_arms_jacuzzi_topless_leaning_a_massage:
    Transform("melonia_arms_jacuzzi_topless_leaning_a_massage1")
    pause .3
    Transform("melonia_arms_jacuzzi_topless_leaning_a_massage2")
    pause .3
    Transform("melonia_arms_jacuzzi_topless_leaning_a_massage3")
    pause .3
    Transform("melonia_arms_jacuzzi_topless_leaning_a_massage2")
    pause .3
    repeat



init python:
    for o in ('', '_anal'):
        for i in xrange(1, 9):
            renpy.image('melonia_body_b_sex_anim{} {}'.format(o, i),
                        'melonia_body_b_sex_anim{}{:02}'.format(o, i))

image melonia_body_b_sex_anim = AnimatedImage('melonia_body_b_sex_anim',
                                           (1,2,3,4,5,6,7,8),
                                           M_melonia)
image melonia_body_b_sex_anim_anal = AnimatedImage('melonia_body_b_sex_anim_anal',
                                           (1,2,3,4,5,6,7,8),
                                           M_melonia)

image melonia_body_b_sex_anim_hard:
    'melonia_body_b_sex_cum'
    .6
    'melonia_body_b_sex_anim06' with dissolve

image melonia_arms_sex_insert_pullout_a_cumshot:
    Transform("melonia_arms_sex_insert_pullout_a_cumshot1")
    pause .4
    Transform("melonia_arms_sex_insert_pullout_a_cumshot2")
    pause .4
    Transform("melonia_arms_sex_insert_pullout_a_cumshot3")





image xray_melonia_top:
    Transform("characters/xray/xray_front_top_01.png", xzoom=-.7, yzoom=.7, rotate=90, xoffset=190, yoffset=160)
    pause 0.4
    Transform("characters/xray/xray_front_top_02.png", xzoom=-.7, yzoom=.7, rotate=90, xoffset=190, yoffset=160)
    pause 0.4
    Transform("characters/xray/xray_front_top_03.png", xzoom=-.7, yzoom=.7, rotate=90, xoffset=190, yoffset=160)
    pause 0.4
    Transform("characters/xray/xray_front_top_04.png", xzoom=-.7, yzoom=.7, rotate=90, xoffset=190, yoffset=160)
    pause 0.4
    Transform("characters/xray/xray_front_top_05.png", xzoom=-.7, yzoom=.7, rotate=90, xoffset=190, yoffset=160)
    pause 0.4
    Transform("characters/xray/xray_front_top_06.png", xzoom=-.7, yzoom=.7, rotate=90, xoffset=190, yoffset=160)
    pause 0.4
    Transform("characters/xray/xray_front_top_07.png", xzoom=-.7, yzoom=.7, rotate=90, xoffset=190, yoffset=160)
    pause 0.4
    Transform("characters/xray/xray_front_top_08.png", xzoom=-.7, yzoom=.7, rotate=90, xoffset=190, yoffset=160)
    pause 0.4
    Transform("characters/xray/xray_front_top_09.png", xzoom=-.7, yzoom=.7, rotate=90, xoffset=190, yoffset=160)
    pause 0.4
    Transform("characters/xray/xray_front_top_10.png", xzoom=-.7, yzoom=.7, rotate=90, xoffset=190, yoffset=160)
    pause 0.4
    Transform("characters/xray/xray_front_top_11.png", xzoom=-.7, yzoom=.7, rotate=90, xoffset=190, yoffset=160)
    pause 0.4
    Transform("characters/xray/xray_front_top_12.png", xzoom=-.7, yzoom=.7, rotate=90, xoffset=190, yoffset=160)
    pause 0.4
    Transform("characters/xray/xray_front_top_13.png", xzoom=-.7, yzoom=.7, rotate=90, xoffset=190, yoffset=160)
    pause 0.4
    Transform("characters/xray/xray_front_top_14.png", xzoom=-.7, yzoom=.7, rotate=90, xoffset=190, yoffset=160)
    pause 0.4
    Transform("characters/xray/xray_front_top_15.png", xzoom=-.7, yzoom=.7, rotate=90, xoffset=190, yoffset=160)
    pause 0.4
    Transform("characters/xray/xray_front_top_16.png", xzoom=-.7, yzoom=.7, rotate=90, xoffset=190, yoffset=160)
    pause 0.4
    Transform("characters/xray/xray_front_top_17.png", xzoom=-.7, yzoom=.7, rotate=90, xoffset=190, yoffset=160)
    pause 0.4
    Transform("characters/xray/xray_front_top_18.png", xzoom=-.7, yzoom=.7, rotate=90, xoffset=190, yoffset=160)
    pause 2.0
    linear 2.5 alpha 0


init image melonia_bedroom_press_dick_d_cumshot:
    'melonia_bedroom_press_dick_d_cumshot1'
    .4
    'melonia_bedroom_press_dick_d_cumshot2' with fastdissolve


layeredimage melonia bedroom_press:
    always 'melonia_bedroom_press_body_b_base'
    attribute m_talk null

    group face if_not 'm_talk' auto
    group face if_all 'm_talk' auto variant 'talk':
        attribute f_smirk default

    group dick auto:
        attribute d_insert default


init python hide:
    count = 10
    first = 1
    frames = tuple(i % count + 1 for i in xrange(first, first + count))

    map = (('melonia_body_b_sex_bj_anim', 'melonia_bedroom_blowjob'),)

    for src, stem in map:
        for i in frames:
            renpy.image('{} {}'.format(stem, i),
                        '{}{:02}'.format(src, i))
        
        renpy.image(stem, AnimatedImage(stem, frames, M_melonia))


init python hide:
    count = 8
    first = 1
    frames = tuple(i % count + 1 for i in xrange(first, first + count))

    map = (('melonia_body_b_sex_missionary_anim', 'melonia_bedroom_press'),)

    for src, stem in map:
        for i in frames:
            renpy.image('{} {}'.format(stem, i),
                        '{}{:02}'.format(src, i))
        
        renpy.image(stem, AnimatedImage(stem, frames, M_melonia))


image melonia_bedroom_blowjob_cum:
    'melonia_body_b_sex_bj_cum_drip1'
    'melonia_body_b_sex_bj_cum_drip2' with Dissolve(3)
    3
    'melonia_body_b_sex_bj_cum_drip3' with Dissolve(3)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
