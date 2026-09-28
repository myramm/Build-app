init:
    $ liu_clothing_options = ['b_dressed','b_naked','b_naked_disheveled','b_naked_hair','b_dressed_disheveled','b_dressed_disheveled_skirt_up','b_dressed_disheveled_after_sex','b_robe_disheveled','b_robe_hair','b_magic','b_robe_open', 'b_robe_disheveled_open', 'b_dressed_magic', 'b_robe_magic']

init python:


    renpy.image('liu_arms_a_empty', 'ground.png')
    renpy.image('liu_body_b_empty', 'ground.png')
    renpy.image('liu_face_f_empty', 'ground.png')
    renpy.image('liu_face_talk_f_empty', 'ground.png')


    renpy.image('liu_face_talk_f_laugh', 'liu_face_f_laugh')
    renpy.image('liu_face_talk_f_nervous_laugh', 'liu_face_f_nervous_laugh')
    renpy.image('liu_face_talk_f_eating', 'liu_face_f_eating')
    renpy.image('liu_face_talk_f_burp', 'liu_face_f_burp')




    renpy.image('liu_arms_dressed_a_touch', 'liu_arms_dressed_a_shy')
    renpy.image('liu_arms_robe_a_touch', 'liu_arms_robe_a_shy')

layeredimage liu:

    yanchor config.screen_height
    ypos 1.
    xanchor config.screen_width
    xpos 1.


    group body auto:
        attribute b_dressed default
        attribute b_empty null
        attribute b_floor 'location_bank_hallway_floor'
        attribute b_magic "liu_body_b_[M_liu.outfit][M_liu.pregnancy]"   
        attribute b_mcpuffin null
        attribute b_dressed_kiss "liu_body_b_dressed_kiss"
        attribute b_dressed_kiss_2 "liu_body_b_dressed_kiss_2"
        attribute b_dressed_kiss_3 "liu_body_b_dressed_kiss_3"
        attribute b_robe_kiss
        attribute b_robe_disheveled_kiss
        attribute b_bed_skirt_kiss "liu_body_b_bed_skirt_kiss"
        attribute b_bed_naked_kiss "liu_body_b_bed_naked_kiss"
        attribute b_bed_dressed_kiss "liu_body_b_bed_dressed_kiss"
        attribute b_bed_shorts_kiss "liu_body_b_bed_shorts_kiss"
        attribute b_mcpuffin null
        attribute b_dressed_magic 'liu_body_b_dressed[M_liu.pregnancy]'
        attribute b_robe_magic 'liu_body_b_robe_hair[M_liu.pregnancy]'


    group mouth prefix 'm':
        attribute talk null

    group face:
        attribute f_normal default null







    group face if_not 'm_talk' if_any liu_clothing_options auto


    group face if_not 'm_talk' if_any ['b_dressed_taken_kim'] auto:
        offset (-71,44)


    group face if_not 'm_talk' if_any ['b_dressed_getup1'] auto:
        offset (-12, 240)


    group face if_not 'm_talk' if_any ['b_dressed_disheveled_skirt_pull1','b_dressed_disheveled_skirt_pull_down_panties'] auto:
        offset (-35, 46)


    group face if_not 'm_talk' if_any ['b_dressed_desk_jump2'] auto:
        offset (16, -115)


    group face if_not 'm_talk' if_any ['b_dressed_desk_jump3'] auto:
        offset (-31, -118)


    group face if_not 'm_talk' if_any ['b_dressed_disheveled_printer','b_dressed_disheveled_printer_open'] auto:
        offset (18, -92)


    group face if_not 'm_talk' if_any ['b_dressed_disheveled_jump1'] auto:
        offset (-36, 36)


    group face if_not 'm_talk' if_any ['b_dressed_disheveled_jump2'] auto:
        offset (-8, -100)


    group face if_not 'm_talk' if_any ['b_dressed_floor'] auto:
        offset (-81, -58)


    group face if_not 'm_talk' if_any ['b_naked_caught1'] auto:
        rotate -13
        offset (-352, -338)


    group face if_not 'm_talk' if_any ['b_naked_caught2'] auto:
        rotate -13
        offset (-385, -371)


    group face if_not 'm_talk' if_any ['b_naked_caught3'] auto:
        rotate -13
        offset (-409, -388)


    group face if_not 'm_talk' if_any ['b_naked_caught4'] auto:
        rotate -13
        offset (-404, -382)


    group face if_not 'm_talk' if_any ['b_robe_tea'] auto:
        offset (80, -56)


    group face if_not 'm_talk' if_any ['b_gown_bed'] auto:
        offset (102, 30)


    group face if_not 'm_talk' if_any ['b_dressed_folder_anon_tilt'] auto:
        rotate -15
        offset (-435, -180)


    group face if_not 'm_talk' if_any ['b_dressed_folder_anon'] auto:
        offset (-318, 0)


    group face if_not 'm_talk' if_any ['b_naked_anon_arms'] auto:
        offset (-400, 10)


    group face if_not 'm_talk' if_any ['b_dressed_lean_whisper'] auto:
        offset (-79, 127)






    group face if_not 'm_talk' if_any ['b_floor'] auto variant 'floor'


    group face if_not 'm_talk' if_any 'b_mcpuffin' auto variant 'briefcase':
        attribute f_normal default null


    group face if_not 'm_talk' if_any ['b_robe_front1','b_robe_front2'] auto variant 'robe_front'


    group face if_not 'm_talk' if_any ['b_sex_bed_cuddle'] auto variant 'sex_bed'


    group face if_not 'm_talk' if_any ['b_sex_printer_base'] auto variant 'sex_printer':
        offset (-2,0)
        attribute f_normal 'liu_face_sex_printer_f_shy'


    group face if_not 'm_talk' if_any ['b_sex_printer_insert'] auto variant 'sex_printer':
        offset (22,14)
        attribute f_normal 'liu_face_sex_printer_f_shy'


    group face if_not 'm_talk' if_any 'b_mcpuffin' auto variant 'briefcase':
        attribute f_normal default null







    group face if_all 'm_talk' if_any liu_clothing_options auto variant 'talk'


    group face if_all 'm_talk' if_any ['b_dressed_taken_kim'] auto variant 'talk':
        offset (-71,44)


    group face if_all 'm_talk' if_any ['b_dressed_getup1'] auto variant 'talk':
        offset (-12, 240)


    group face if_all 'm_talk' if_any ['b_dressed_disheveled_skirt_pull1','b_dressed_disheveled_skirt_pull_down_panties'] auto variant 'talk':
        offset (-35, 46)


    group face if_all 'm_talk' if_any ['b_dressed_disheveled_printer','b_dressed_disheveled_printer_open'] auto variant 'talk':
        offset (18, -92)


    group face if_all 'm_talk' if_any ['b_dressed_disheveled_jump1'] auto variant 'talk':
        offset (-36, 36)


    group face if_all 'm_talk' if_any ['b_dressed_disheveled_jump2'] auto variant 'talk':
        offset (-8, -100)


    group face if_all 'm_talk' if_any ['b_dressed_floor'] auto variant 'talk':
        offset (-81, -58)


    group face if_all 'm_talk' if_any ['b_naked_caught1'] auto variant 'talk':
        rotate -13
        offset (-352, -338)


    group face if_all 'm_talk' if_any ['b_naked_caught2'] auto variant 'talk':
        rotate -13
        offset (-385, -371)


    group face if_all 'm_talk' if_any ['b_naked_caught3'] auto variant 'talk':
        rotate -13
        offset (-409, -388)


    group face if_all 'm_talk' if_any ['b_naked_caught4'] auto variant 'talk':
        rotate -13
        offset (-404, -382)


    group face if_all 'm_talk' if_any ['b_robe_tea'] auto variant 'talk':
        offset (80, -56)


    group face if_all 'm_talk' if_any ['b_gown_bed'] auto variant 'talk':
        offset (102, 30)


    group face if_all 'm_talk' if_any ['b_dressed_folder_anon_tilt'] auto variant 'talk':
        rotate -15
        offset (-435, -180)


    group face if_all 'm_talk' if_any ['b_dressed_folder_anon'] auto variant 'talk':
        offset (-318, 0)


    group face if_all 'm_talk' if_any ['b_naked_anon_arms'] auto variant 'talk':
        offset (-400, 10)


    group face if_all 'm_talk' if_any ['b_dressed_lean_whisper'] auto variant 'talk':
        offset (-79, 127)






    group face if_all 'm_talk' if_any ['b_floor'] auto variant 'floor_talk'


    group face if_all 'm_talk' if_any 'b_mcpuffin' auto variant 'briefcase_talk':
        attribute f_normal default 'liu_face_briefcase_talk_f_normal_down'


    group face if_all 'm_talk' if_any ['b_robe_front1','b_robe_front2'] auto variant 'robe_front_talk'


    group face if_all 'm_talk' if_any ['b_sex_bed_cuddle'] auto variant 'sex_bed_talk'


    group face if_all 'm_talk' if_any ['b_sex_printer_base'] auto variant 'sex_printer_talk':
        offset (-2,0)
        attribute f_normal 'liu_face_sex_printer_talk_f_shy'


    group face if_all 'm_talk' if_any ['b_sex_printer_insert'] auto variant 'sex_printer_talk':
        offset (22,14)
        attribute f_normal 'liu_face_sex_printer_talk_f_shy'


    group face if_all 'm_talk' if_any 'b_mcpuffin' auto variant 'briefcase_talk':
        attribute f_normal default 'liu_face_briefcase_talk_f_normal_down'



    group arms if_any ['b_dressed'] auto variant 'dressed':
        attribute a_idle default 'liu_arms_dressed_a_sides'
        attribute a_wipe_tears'liu_arms_disheveled_a_wipe_tears'

    group arms if_any ['b_dressed_magic']:
        attribute a_idle default 'liu_arms_dressed[M_liu.pregnancy]_a_touch'
        attribute a_mouth_cover 'liu_arms_dressed_a_mouth_cover'
        attribute a_typing 'liu_arms_dressed_a_typing'


    group arms if_any ['b_dressed_disheveled','b_dressed_disheveled_skirt_up','b_dressed_disheveled_after_sex'] auto variant 'disheveled':
        attribute a_idle default 'liu_arms_dressed_a_sides'
        attribute a_behind 'liu_arms_dressed_a_behind'
        attribute a_cry 'liu_arms_dressed_a_cry'
        attribute a_sides 'liu_arms_dressed_a_sides'


    group arms if_all 'b_robe_tea' auto variant 'robe_tea':
        attribute a_idle default 'liu_arms_robe_tea_a_down'

    group arms if_any ['b_robe_magic']:
        attribute a_idle default 'liu_arms_robe[M_liu.pregnancy]_a_touch'


    group arms if_all 'b_dressed_floor' auto variant 'dressed_floor':
        attribute a_idle default 'liu_arms_dressed_floor_a_down'


    group arms if_any ['b_robe_open','b_robe_disheveled','b_robe_disheveled_open','b_robe_hair'] auto variant 'robe':
        attribute a_idle default 'liu_arms_robe_a_sides'
        attribute a_baby 'liu_arms_robe_a_baby_[M_liu.pregnancy.baby_gender]'


    group arms if_all 'b_gown_bed' auto variant 'gown_bed':
        attribute a_idle default 'liu_arms_gown_bed_a_baby_[M_liu.pregnancy.baby_gender]'


    group arms if_any ['b_naked','b_naked_disheveled','b_naked_hair'] auto variant 'naked':
        attribute a_idle default 'liu_arms_naked_a_sides'


    group arms if_all 'b_magic' auto:
        attribute a_idle default 'liu_arms_[M_liu.outfit]_a_touch[M_liu.pregnancy]'


    group overlay_dick_sex_printer if_any ['b_sex_printer_base'] auto:
        attribute od_pre default 'liu_overlay_dick_sex_printer_od_pre'
        attribute od_cumshot 'liu_overlay_dick_sex_printer_od_cumshot'
        attribute od_cumshot3
        attribute od_empty null

    group overlay_dick_sex_bed if_any ['b_sex_bed_pre'] auto:
        attribute od_pre default 'liu_overlay_dick_sex_bed_od_pre'
        attribute od_cumshot 'liu_overlay_dick_sex_bed_od_cumshot'
        attribute od_cumshot3
        attribute od_insert 'liu_overlay_dick_sex_bed_od_insert'
        attribute od_empty null

    group overlay_sex_printer if_any ['b_sex_printer_base','b_sex_printer_insert'] auto:
        attribute o_empty default null

    group overlay_sex_bed if_any ['b_sex_bed_pre'] auto:
        attribute o_empty default null

    group overlay if_not ['b_robe_bend', 'b_robe_tea', 'b_dressed_disheveled_skirt_pull1', 'b_dressed_disheveled_skirt_pull_down_panties', 'b_dressed_disheveled_printer', 'b_dressed_disheveled_printer_open', 'b_dressed_disheveled_jump1', 'b_dressed_disheveled_jump2'] auto:
        attribute o_empty default null

    group overlay if_any 'b_robe_tea' auto:
        offset (80, -56)

    group overlay if_any ['b_dressed_disheveled_skirt_pull1','b_dressed_disheveled_skirt_pull_down_panties'] auto:
        offset (-35, 46)

    group overlay if_any ['b_dressed_disheveled_printer','b_dressed_disheveled_printer_open'] auto:
        offset (18, -92)

    group overlay if_any ['b_dressed_disheveled_jump1'] auto:
        offset (-36, 36)

    group overlay if_any ['b_dressed_disheveled_jump2'] auto:
        offset (-8, -100)


image liu_f = "characters/liu/liu_face_f_normal.png"

image liu_desk = "characters/liu/liu_desk.png"

image liu_body_b_dressed_kiss:
    Transform("liu_body_b_dressed_kiss1")
    pause .4
    Transform("liu_body_b_dressed_kiss2")
    pause .4
    repeat

image liu_body_b_dressed_kiss_2:
    Transform("liu_body_b_dressed_kiss3")
    pause .4
    Transform("liu_body_b_dressed_kiss4")
    pause .4
    repeat

image liu_body_b_dressed_kiss_3:
    Transform("liu_body_b_dressed_kiss5")
    pause .4
    Transform("liu_body_b_dressed_kiss6")
    pause .4
    repeat

image liu_body_b_robe_kiss:
    Transform("liu_body_b_robe_hair_kiss1")
    pause .4
    Transform("liu_body_b_robe_hair_kiss2")
    pause .4
    repeat

image liu_body_b_robe_disheveled_kiss:
    Transform("liu_body_b_robe_disheveled_kiss1")
    pause .4
    Transform("liu_body_b_robe_disheveled_kiss2")
    pause .4
    repeat

image liu_body_b_bed_skirt_kiss:
    Transform("liu_body_b_bed_skirt_kiss1")
    pause .4
    Transform("liu_body_b_bed_skirt_kiss2")
    pause .4
    repeat

image liu_body_b_bed_dressed_kiss:
    Transform("liu_body_b_bed_dressed_kiss1")
    pause .4
    Transform("liu_body_b_bed_dressed_kiss2")
    pause .4
    repeat

image liu_body_b_bed_naked_kiss:
    Transform("liu_body_b_bed_naked_kiss1")
    pause .4
    Transform("liu_body_b_bed_naked_kiss2")
    pause .4
    repeat

image liu_body_b_bed_shorts_kiss:
    Transform("liu_body_b_bed_shorts_kiss1")
    pause .4
    Transform("liu_body_b_bed_shorts_kiss2")
    pause .4
    repeat

image liu_overlay_dick_sex_printer_od_cumshot:
    Transform("liu_overlay_dick_sex_printer_od_cumshot1")
    pause .4
    Transform("liu_overlay_dick_sex_printer_od_cumshot2")
    pause .4
    Transform("liu_overlay_dick_sex_printer_od_cumshot3")

image liu_overlay_dick_sex_printer_od_cumshot3 = Composite(
    (1025,768),
    (0,0), "characters/liu/liu_overlay_dick_sex_printer_od_pre.png",
    (0,0), "characters/liu/liu_overlay_sex_printer_o_dick_cumshot3.png",
    )

image liu_overlay_dick_sex_bed_od_cumshot:
    Transform("liu_overlay_dick_sex_bed_od_cumshot1")
    pause .4
    Transform("liu_overlay_dick_sex_bed_od_cumshot2")
    pause .4
    Transform("liu_overlay_dick_sex_bed_od_cumshot3")

image liu_overlay_dick_sex_bed_od_cumshot3 = Composite(
    (1025,768),
    (0,0), "characters/liu/liu_overlay_dick_sex_bed_od_pre.png",
    (0,0), "characters/liu/liu_overlay_sex_bed_o_cumshot3.png",
    )

init python:
    for i in xrange(1, 11):
        renpy.image('liu_sex_bed_anim {}'.format(i),
                    'liu_body_b_sex_bed_anim{:02}'.format(i))

image liu_sex_bed_anim = AnimatedImage(
    'liu_sex_bed_anim', (1,2,3,4,5,6,7,8,9,10), M_liu)

init python:
    for i in xrange(1, 7):
        renpy.image('liu_sex_printer_anim {}'.format(i),
                    'liu_body_b_sex_printer_anim{:02}'.format(i))

image liu_sex_printer_anim = AnimatedImage(
    'liu_sex_printer_anim', (1,2,3,4,5,6), M_liu)

init python:
    for i in xrange(1, 12):
        renpy.image('liu_sex_printer_front_anim {}'.format(i),
                    'liu_body_b_sex_printer_front_anim{:02}'.format(i))

image liu_sex_printer_front_anim = AnimatedImage(
    'liu_sex_printer_front_anim', (1,2,3,4,5,6,7,8,9,10,11), M_liu, scale=.5)


image xray_liu_sex_bed:
    anchor (.5, .5)
    pos (206 + 250, 14 + 250)
    rotate 123
    rotate_pad False
    zoom .45
    'xray_side'

image xray_liu_sex_printer:
    anchor (.5, .5)
    pos (335 + 250, 323 + 250)
    rotate 39
    rotate_pad False
    xzoom -.725
    yzoom .725
    'xray_side'


init python hide:
    count = 10
    first = 1
    frames = tuple(i % count + 1 for i in xrange(first, first + count))

    map = (('liu_body_b_sex_bed_side_anim', 'liu_bedroom_thirst'),)

    for src, stem in map:
        for i in frames:
            renpy.image('{} {}'.format(stem, i),
                        '{}{:02}'.format(src, i))
        
        renpy.image(stem, AnimatedImage(stem, frames, M_liu))
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
