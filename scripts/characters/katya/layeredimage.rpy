init:
    $ katya_clothing_options = ['b_bottom', 'b_naked_disheveled', 'b_dressed', 'b_dressed_boobs', 'b_dressed_boobs_pulled', 'b_dressed_disheveled', 'b_dressed_disheveled_boobs', 'b_dressed_disheveled_boobs_pulled']

init python:


    renpy.image('katya_arms_a_empty', 'ground.png')
    renpy.image('katya_body_b_empty', 'ground.png')
    renpy.image('katya_face_f_empty', 'ground.png')
    renpy.image('katya_face_talk_f_empty', 'ground.png')


    renpy.image('katya_face_talk_f_laugh', 'katya_face_f_laugh')




    renpy.image('katya_arms_naked_disheveled_a_front', 'katya_arms_bottom_a_front')

layeredimage katya:

    yanchor config.screen_height
    ypos 1.
    xanchor config.screen_width
    xpos 1.


    group body auto:
        attribute b_bottom default
        attribute b_empty null


    group mouth prefix 'm':
        attribute talk null

    group face:
        attribute f_normal default null







    group face if_not 'm_talk' if_any katya_clothing_options auto

    group face if_not 'm_talk' if_any 'b_dressed_sit' auto:
        offset (76, 63)

    group face if_not 'm_talk' if_any 'b_couch_disheveled1' auto:
        align (.5, .5)
        offset (339, 232)
        rotate 20.5
        rotate_pad False
        transform_anchor True
        xzoom -1

    group face if_not 'm_talk' if_any 'b_couch_disheveled2' auto:
        align (.5, .5)
        offset (301, 7)
        rotate 5.5
        rotate_pad False
        transform_anchor True
        xzoom -1

    group face if_not 'm_talk' if_any 'b_couch_disheveled3' auto:
        offset (298, -74)
        xzoom -1

    group face if_not 'm_talk' if_any 'b_dressed_disheveled_boobs_pulled_back' auto:
        xoffset -266











    group face if_all 'm_talk' if_any katya_clothing_options auto variant 'talk'

    group face if_all 'm_talk' if_any 'b_dressed_sit' auto variant 'talk':
        offset (76, 63)

    group face if_all 'm_talk' if_any 'b_couch_disheveled1' auto variant 'talk':
        align (.5, .5)
        offset (339, 232)
        rotate 20.5
        rotate_pad False
        transform_anchor True
        xzoom -1

    group face if_all 'm_talk' if_any 'b_couch_disheveled2' auto variant 'talk':
        align (.5, .5)
        offset (301, 7)
        rotate 5.5
        rotate_pad False
        transform_anchor True
        xzoom -1

    group face if_all 'm_talk' if_any 'b_couch_disheveled3' auto variant 'talk':
        offset (298, -74)
        xzoom -1

    group face if_all 'm_talk' if_any 'b_dressed_disheveled_boobs_pulled_back' auto variant 'talk':
        xoffset -266







    group arms if_all 'b_bottom' auto variant 'bottom':
        attribute a_idle default 'katya_arms_bottom_a_front'






    group arms if_all 'b_naked_disheveled' auto variant 'naked_disheveled':
        attribute a_idle default 'katya_arms_naked_disheveled_a_front'

    group arms if_any ['b_dressed', 'b_dressed_disheveled'] auto variant 'dressed':
        attribute a_idle default 'katya_arms_dressed_a_front'

    group arms if_all 'b_dressed_sit' auto variant 'dressed_sit':
        attribute a_idle default 'katya_arms_dressed_sit_a_writing'

    group arms if_any ['b_dressed_boobs', 'b_dressed_disheveled_boobs'] auto variant 'dressed_boobs':
        attribute a_idle default 'katya_arms_dressed_boobs_a_undress2'

    group arms if_any ['b_dressed_boobs_pulled', 'b_dressed_disheveled_boobs_pulled'] auto variant 'dressed_boobs_pulled':
        attribute a_idle default 'katya_arms_dressed_boobs_pulled_a_pull2'

    group arms if_any ['b_dressed_disheveled_boobs_pulled_back'] auto variant 'dressed_disheveled_boobs_pulled_back':
        attribute a_idle default 'katya_arms_dressed_boobs_pulled_back_a_hips'

    group arms if_all 'b_couch_disheveled2' auto variant 'couch_disheveled2':
        attribute a_idle default 'katya_arms_couch_disheveled2_a_wipe'


    group overlay if_not 'b_couch_disheveled3' auto:
        attribute o_empty default null

    group overlay if_any 'b_couch_disheveled3' auto:
        offset (298, -74)
        xzoom -1

image katya_f = "characters/katya/katya_face_f_normal.png"


init -1 image katya_body_b_dressed_disheveled_kiss:
    'katya_body_b_dressed_disheveled_kiss1'
    .4
    'katya_body_b_dressed_disheveled_kiss2'
    .4
    repeat

init image katya_sex_desk_side_overlay_o_cumshot:
    'katya_sex_desk_side_overlay_o_cumshot1' with fastdissolve
    .4
    'katya_sex_desk_side_overlay_o_cumshot2' with fastdissolve
    .4
    'katya_sex_desk_side_overlay_o_cumshot3' with fastdissolve


init python hide:
    count = 6
    first = 1
    frames = tuple(i % count + 1 for i in xrange(first, first + count))

    map = (('katya_sex_desk_side_body_b_anim', 'katya_sex_desk_side_body_b_anim'),
           ('katya_sex_desk_top_body_b_anim', 'katya_sex_desk_top_body_b_anim'),)

    for src, stem in map:
        for i in frames:
            renpy.image('{} {}'.format(stem, i),
                        '{}{:02}'.format(src, i))
        
        renpy.image(stem, AnimatedImage(stem, frames, M_katya))


layeredimage katya sex_desk_side:
    attribute m_talk null

    group body auto:
        attribute b_base default

    group face if_all 'b_base' if_not 'm_talk' auto
    group face if_all 'b_base' if_any 'm_talk' auto variant 'talk':
        attribute f_normal_back default

    group arms if_all 'b_base' auto:
        attribute a_pre default

    group overlay if_all 'b_base' if_any 'a_pre' auto


layeredimage katya sex_desk_top:
    attribute m_talk null

    group body auto:
        attribute b_insert default

    group face if_all 'b_insert' if_not 'm_talk' auto variant 'insert'
    group face if_all 'b_insert' if_any 'm_talk' auto variant 'insert_talk':
        attribute f_happy default
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
