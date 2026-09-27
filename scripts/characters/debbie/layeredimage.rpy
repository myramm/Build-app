init:
    $ debbie_clothing_options = ['b_robe','b_robe_open', 'b_robe_hug_mc_behind', 'b_casual', 'b_naked', 'b_empty', 'b_nightgown', 'b_nightgown_hair', 'b_robe_hug_jenny_bump', 'b_robe_hug_jenny_front', 'b_robe_hug_jenny_front_arm', 'b_robe_hug_jenny_front_anon', 'b_robe_hug_tony']

init python:


    renpy.image('debbie_arms_a_empty', 'ground.png')
    renpy.image('debbie_body_b_empty', 'ground.png')
    renpy.image('debbie_face_f_empty', 'ground.png')
    renpy.image('debbie_face_talk_f_empty', 'ground.png')


    renpy.image('debbie_face_talk_f_laugh', 'debbie_face_f_laugh')



layeredimage debbie:

    yanchor config.screen_height
    ypos 1.
    xanchor config.screen_width
    xpos 1.


    group body auto:
        attribute b_robe default
        attribute b_empty null
        attribute b_robe_kiss_mc 'debbie_body_b_robe_kiss_mc'


    group mouth prefix 'm':
        attribute talk null

    group face:
        attribute f_normal default null







    group face if_not 'm_talk' if_any debbie_clothing_options auto


    group face if_not 'm_talk' if_any ['b_robe_tied'] auto:
        offset (-551, 126)


    group face if_not 'm_talk' if_any ['b_robe_tied_recoil', 'b_robe_untying'] auto:
        offset (-605, 144)


    group face if_not 'm_talk' if_any ['b_robe_hug_jenny_sad'] auto:
        align (.5, .5)
        offset (15, 64)
        rotate -11
        rotate_pad False


    group face if_not 'm_talk' if_any ['b_front_couch_watching'] auto:
        offset (125, -122)


    group face if_not 'm_talk' if_any ['b_robe_mc_touch'] auto:
        offset (-194, 0)


    group face if_not 'm_talk' if_any ['b_bed_nightgown_getup', 'b_nightgown_bed', 'b_naked_bed', 'b_bed_nightgown_undress'] auto:
        xzoom -1
        offset (392,-18)


    group face if_not 'm_talk' if_all 'b_bed_nightgown_straight' auto:
        xzoom -1
        offset (40,1)


    group face if_not 'm_talk' if_all 'b_bed_undress2' auto:
        xzoom -1
        offset (416,7)


    group face if_not 'm_talk' if_all 'b_breakfast_sitting' auto:
        zoom .76
        offset (295,137)


    group face if_not 'm_talk' if_all 'b_breakfast_potatoes' auto:
        zoom .76
        offset (299,15)


    group face if_not 'm_talk' if_all 'b_breakfast_mug' auto:
        zoom .76
        offset (284,15)


    group face if_not 'm_talk' if_all 'b_breakfast_kiss' auto:
        zoom .76
        offset (75,128)

    group face if_not 'm_talk' if_all 'b_robe_scared_anon' auto:
        offset (61, 0)











    group face if_all 'm_talk' if_any debbie_clothing_options auto variant 'talk'


    group face if_all 'm_talk' if_any ['b_robe_tied'] auto variant 'talk':
        offset (-551, 126)


    group face if_all 'm_talk' if_any ['b_robe_tied_recoil', 'b_robe_untying'] auto variant 'talk':
        offset (-605, 144)


    group face if_all 'm_talk' if_any ['b_robe_hug_jenny_sad'] auto variant 'talk':
        align (.5, .5)
        offset (15, 64)
        rotate -11
        rotate_pad False


    group face if_all 'm_talk' if_any ['b_front_couch_watching'] auto variant 'talk':
        offset (125, -122)


    group face if_all 'm_talk' if_any ['b_robe_mc_touch'] auto variant 'talk':
        offset (-194, 0)


    group face if_all 'm_talk' if_any ['b_bed_nightgown_getup', 'b_nightgown_bed', 'b_naked_bed', 'b_bed_nightgown_undress'] auto variant 'talk':
        xzoom -1
        offset (392,-18)


    group face if_all ['m_talk', 'b_bed_nightgown_straight'] auto variant 'talk':
        xzoom -1
        offset (40,1)


    group face if_all ['m_talk', 'b_bed_undress2'] auto variant 'talk':
        xzoom -1
        offset (416,7)


    group face if_all ['m_talk', 'b_breakfast_sitting'] auto variant 'talk':
        zoom .76
        offset (295,137)


    group face if_all ['m_talk', 'b_breakfast_potatoes'] auto variant 'talk':
        zoom .76
        offset (299,15)


    group face if_all ['m_talk', 'b_breakfast_mug'] auto variant 'talk':
        zoom .76
        offset (284,15)


    group face if_all ['m_talk', 'b_breakfast_kiss'] auto variant 'talk':
        zoom .76
        offset (75,128)

    group face if_all ['m_talk', 'b_robe_scared_anon'] auto variant 'talk':
        offset (61, 0)







    group arms if_any ['b_robe','b_robe_open'] auto variant 'robe':
        attribute a_idle default 'debbie_arms_robe_a_mug'
        attribute a_baby "characters/debbie/layeredimage/debbie_arms_robe_a_baby_[player.last_baby_gender].png"


    group arms if_all 'b_robe_mc_touch' auto variant 'robe_mc_touch':
        attribute a_idle default 'debbie_arms_robe_mc_touch_a_idle'


    group arms if_all 'b_nightgown' auto variant 'nightgown':
        attribute a_idle default 'debbie_arms_nightgown_a_sides'


    group arms if_all 'b_casual' auto variant 'casual':
        attribute a_idle default 'debbie_arms_casual_a_sides'
        attribute a_baby "characters/debbie/layeredimage/debbie_arms_casual_a_baby_[player.last_baby_gender].png"


    group arms if_all 'b_breakfast_sitting' auto variant 'breakfast':
        attribute a_idle default 'debbie_arms_breakfast_a_rest'


    group arms if_any ['b_naked'] auto variant 'naked':
        attribute a_idle default 'debbie_arms_naked_a_sides'


    group overlay auto:
        attribute o_empty default null


layeredimage debbie cutscene12:
    group mouth prefix 'm':
        attribute talk null

    group face if_not 'm_talk' auto:
        attribute f_crying null
    group face if_all 'm_talk' auto variant 'talk'


layeredimage debbie cutscene22b:
    group mouth prefix 'm':
        attribute talk null

    group face if_not 'm_talk' auto
    group face if_all 'm_talk' auto variant 'talk':
        attribute f_normal default null


layeredimage debbie deb0m_post:
    always 'debbie_deb0m_post_body_b_default'

    group mouth prefix 'm':
        attribute talk null

    group face if_not 'm_talk' auto
    group face if_all 'm_talk' auto variant 'talk':
        attribute f_calm default


image debbie_f = "characters/debbie/layeredimage/debbie_face_talk_f_normal.png"

image debbie_body_b_robe_kiss_mc:
    Transform("debbie_body_b_robe_kiss_mc1")
    pause .4
    Transform("debbie_body_b_robe_kiss_mc2")
    pause .4
    repeat


init python:
    for i in xrange(1, 13):
        renpy.image('debbie_diane_anim {}'.format(i),
                    'debbie_body_b_sex_lesb_anim{:02}'.format(i))

image debbie_diane_anim = AnimatedImage('debbie_diane_anim',
                                        (1,2,3,4,5,6,7,8,9,10,11,12), M_debbie)




image debbie_body_b_robe_hug_jenny_front = 'characters/debbie/layeredimage/debbie_body_b_robe[M_jenny.pregnancy.to_belly_string]_hug_jenny_front.png'
image debbie_body_b_robe_hug_jenny_front_arm = 'characters/debbie/layeredimage/debbie_body_b_robe[M_jenny.pregnancy.to_belly_string]_hug_jenny_front_arm.png'
image debbie_body_b_robe_hug_jenny_front_anon = 'characters/debbie/layeredimage/debbie_body_b_robe[M_jenny.pregnancy.to_belly_string]_hug_jenny_front_anon.png'
image debbie_body_b_robe_hug_jenny_sad = 'characters/debbie/layeredimage/debbie_body_b_robe[M_jenny.pregnancy]_hug_jenny_sad.png'
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
