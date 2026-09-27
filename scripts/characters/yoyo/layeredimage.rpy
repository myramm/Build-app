init:
    $ yoyo_clothing_options = ['b_army', 'b_dressed']

init python:


    renpy.image('yoyo_arms_a_empty', 'ground.png')
    renpy.image('yoyo_body_b_empty', 'ground.png')
    renpy.image('yoyo_face_f_empty', 'ground.png')
    renpy.image('yoyo_face_talk_f_empty', 'ground.png')


    renpy.image('yoyo_face_talk_f_laugh', 'yoyo_face_f_laugh')
    renpy.image('yoyo_face_talk_f_surprised_down', 'yoyo_face_f_surprised_down')




    renpy.image('yoyo_arms_dressed_a_fists', 'josephine_arms_dressed_a_fists')
    renpy.image('yoyo_arms_dressed_a_frustrated', 'josephine_arms_dressed_a_frustrated')
    renpy.image('yoyo_arms_dressed_a_gimme', 'josephine_arms_dressed_a_gimme')
    renpy.image('yoyo_arms_dressed_a_hips', 'josephine_arms_dressed_a_hips')
    renpy.image('yoyo_arms_dressed_a_reach', 'josephine_arms_dressed_a_reach')

layeredimage yoyo:

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







    group face if_not 'm_talk' if_any yoyo_clothing_options auto











    group face if_all 'm_talk' if_any yoyo_clothing_options auto variant 'talk'







    group arms if_any 'b_dressed' auto variant 'dressed':
        attribute a_idle default 'yoyo_arms_dressed_a_sides'


    group arms if_any 'b_army' auto variant 'army':
        attribute a_idle default 'yoyo_arms_naked_a_behind'


    group overlay auto:
        attribute o_empty default null

image yoyo_f = "characters/yoyo/yoyo_face_f_normal.png"


init image yoyo_sex_car_arms_open_a_slap:
    'yoyo_sex_car_arms_open_a_slap1'
    .6
    'yoyo_sex_car_arms_open_a_slap2' with dissolve
    .6
    'yoyo_sex_car_arms_open_a_grab' with dissolve


init python hide:
    for i in renpy.list_images():
        if i.startswith('yoyo_face_'):
            renpy.image(i.replace('yoyo_face_', 'yoyo_sex_car_face_'), i)
        
        if i.startswith('yoyo_sex_car_arms_open_'):
            renpy.image(i.replace('_open_a_', '_uniform_a_'), i)


layeredimage yoyo sex_car:
    attribute m_talk null

    group body auto:
        attribute b_uniform default

    group face if_not 'm_talk' if_any ['b_uniform', 'b_open', 'b_skirt'] auto:
        offset (-264, -260)
        zoom 1.2375
        attribute f_normal default

    group face if_all 'm_talk' if_any ['b_uniform', 'b_open', 'b_skirt'] auto variant 'talk':
        offset (-264, -260)
        zoom 1.2375

    group arms if_all 'b_skirt' auto variant 'skirt'
    group arms if_all 'b_uniform' auto variant 'uniform'
    group arms if_all 'b_open' auto variant 'open'


init python hide:
    count = 7
    first = 1
    frames = tuple(i % count + 1 for i in xrange(first, first + count))

    map = (('yoyo_sex_car_anim', 'yoyo_truck_cowgirl'),)

    for src, stem in map:
        for i in frames:
            renpy.image('{} {}'.format(stem, i),
                        '{}{:02}'.format(src, i))
        
        renpy.image(stem, AnimatedImage(stem, frames, M_yoyo))


image yoyo_sex_car_insert:
    'yoyo_sex_car_anim01'
    .2
    'yoyo_sex_car_anim02' with fastdissolve
    .2
    'yoyo_sex_car_anim03' with fastdissolve
    .2
    'yoyo_sex_car_anim04' with fastdissolve


image yoyo_sex_car_after_cumshot:
    'yoyo_sex_car_after_cumshot1'
    .4
    'yoyo_sex_car_after_cumshot2' with fastdissolve
    .4
    Fixed('yoyo_sex_car_after_dick',
          'yoyo_sex_car_after_cumshot3') with fastdissolve
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
