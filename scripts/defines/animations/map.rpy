
image car01:
    choice:
        "map/map_car_down01.png"
    choice:
        "map/map_car_down02.png"
    xpos 645
    ypos 10
    alpha 0.0
    parallel:
        linear 6.0 ypos 400
    parallel:
        linear 1.0 alpha 1.0
        pause 4.0
        linear 1.0 alpha 0.0
    pause 5.0
    repeat

image car02:
    pause 2.0
    choice:
        "map/map_car_horizontal01.png"
        ypos 455
    choice:
        "map/map_car_horizontal02.png"
        ypos 455
    choice:
        "map/map_car_horizontal03.png"
        ypos 455
    choice:
        "map/map_car_horizontal04.png"
        ypos 455
    choice:
        "map/map_car_horizontal05.png"
        ypos 455
    choice:
        "map/map_car_horizontal06.png"
        ypos 455
    choice:
        "map/map_bus01.png"
        ypos 441
    xpos 1000
    alpha 0.0
    parallel:
        linear 7.0 xpos 480
    parallel:
        linear 1.0 alpha 1.0
        pause 10
        linear 1.0 alpha 0.0
    pause 7.0
    repeat

image car03:
    pause 3.0
    choice:
        "map/map_car_up01.png"
    choice:
        "map/map_car_up02.png"
    xpos 668
    ypos 400
    alpha 0.0
    parallel:
        linear 3.0 ypos 10
    parallel:
        linear 1.0 alpha 1.0
        pause 1
        linear 1.0 alpha 0.0
    pause 8.0
    repeat

image car01_night:
    choice:
        "map/map_car_down01_night.png"
    choice:
        "map/map_car_down02_night.png"
    xpos 645
    ypos 10
    alpha 0.0
    parallel:
        linear 6.0 ypos 400
    parallel:
        linear 1.0 alpha 1.0
        pause 4.0
        linear 1.0 alpha 0.0
    pause 5.0
    repeat

image car02_night:
    pause 2.0
    choice:
        "map/map_car_horizontal01_night.png"
        ypos 455
    choice:
        "map/map_car_horizontal02_night.png"
        ypos 455
    choice:
        "map/map_car_horizontal03_night.png"
        ypos 455
    choice:
        "map/map_car_horizontal04_night.png"
        ypos 455
    choice:
        "map/map_car_horizontal05_night.png"
        ypos 455
    choice:
        "map/map_car_horizontal06_night.png"
        ypos 455
    choice:
        "map/map_bus01_night.png"
        ypos 441
    xpos 1000
    alpha 0.0
    parallel:
        linear 7.0 xpos 480
    parallel:
        linear 1.0 alpha 1.0
        pause 10
        linear 1.0 alpha 0.0
    pause 7.0
    repeat

image santa_car_night:
    pause 2.0
    choice:
        "map/map_car_horizontal07_night.png"
        ypos 455
    xpos 1000
    alpha 0.0
    parallel:
        linear 7.0 xpos 480
    parallel:
        linear 1.0 alpha 1.0
        pause 10
        linear 1.0 alpha 0.0
    pause 7.0
    repeat

image santa_car:
    pause 2.0
    choice:
        "map/map_car_horizontal07.png"
        ypos 455
    xpos 1000
    alpha 0.0
    parallel:
        linear 7.0 xpos 480
    parallel:
        linear 1.0 alpha 1.0
        pause 10
        linear 1.0 alpha 0.0
    pause 7.0
    repeat

image car03_night:
    pause 3.0
    choice:
        "map/map_car_up01_night.png"
    choice:
        "map/map_car_up02_night.png"
    xpos 668
    ypos 400
    alpha 0.0
    parallel:
        linear 3.0 ypos 10
    parallel:
        linear 1.0 alpha 1.0
        pause 1
        linear 1.0 alpha 0.0
    pause 8.0
    repeat

image cloud01:
    "map/map_clouds01.png"
    xpos -1.0
    ypos -1.0
    linear 80.0 xpos 1.0 ypos 1.0
    pause 0.1
    repeat

image smoke01:
    contains:
        'map/map_smoke01.png'
        alpha 0
        anchor (.5, .5)
        offset (117, 66)
        zoom .256
        block:
            linear 2.5 alpha 1
            linear .5 alpha .5
            repeat
    contains:
        'map/map_smoke01.png'
        alpha 0
        anchor (.5, .5)
        offset (117, 60)
        zoom .512
        .5
        block:
            linear 2.5 alpha .9
            linear .5 alpha .4
            repeat
    contains:
        'map/map_smoke01.png'
        alpha 0
        anchor (.5, .5)
        offset (111, 51)
        zoom .768
        1
        block:
            linear 2.5 alpha .8
            linear .5 alpha .3
            repeat
    contains:
        'map/map_smoke01.png'
        alpha 0
        anchor (.5, .5)
        offset (99, 42)
        zoom 1.024
        1.5
        block:
            linear 2.5 alpha .7
            linear .5 alpha .2
            repeat
    contains:
        'map/map_smoke01.png'
        alpha 0
        anchor (.5, .5)
        offset (83, 35)
        zoom 1.28
        2
        block:
            linear 2.5 alpha .6
            linear .5 alpha .1
            repeat

image sparkle01:
    choice:
        "map/map_sparkle01.png"
    choice:
        "map/map_sparkle02.png"
    choice:
        "map/map_sparkle03.png"
    parallel:
        choice:
            xpos 20
        choice:
            xpos 30
        choice:
            xpos 60
        choice:
            xpos 10
        choice:
            xpos 40
        choice:
            xpos 50
    parallel:
        choice:
            ypos 600
        choice:
            ypos 700
        choice:
            ypos 620
        choice:
            ypos 640
        choice:
            ypos 660
        choice:
            ypos 680
        choice:
            ypos 610
        choice:
            ypos 650
        choice:
            ypos 690
    alpha 0.0
    linear 0.3 alpha 1.0
    linear 0.2 alpha 0.0
    pause 3.0
    repeat

image sparkle02:
    choice:
        "map/map_sparkle01.png"
    choice:
        "map/map_sparkle02.png"
    choice:
        "map/map_sparkle03.png"
    parallel:
        choice:
            xpos 20
        choice:
            xpos 30
        choice:
            xpos 60
        choice:
            xpos 10
        choice:
            xpos 40
        choice:
            xpos 50
    parallel:
        choice:
            ypos 600
        choice:
            ypos 700
        choice:
            ypos 620
        choice:
            ypos 640
        choice:
            ypos 660
        choice:
            ypos 680
        choice:
            ypos 610
        choice:
            ypos 650
        choice:
            ypos 690
    alpha 0.0
    linear 0.3 alpha 1.0
    linear 0.2 alpha 0.0
    pause 5.0
    repeat

image sparkle03:
    choice:
        "map/map_sparkle01.png"
    choice:
        "map/map_sparkle02.png"
    choice:
        "map/map_sparkle03.png"
    parallel:
        choice:
            xpos 160
        choice:
            xpos 170
        choice:
            xpos 180
        choice:
            xpos 190
    parallel:
        choice:
            ypos 680
        choice:
            ypos 690
        choice:
            ypos 700
        choice:
            ypos 710
    alpha 0.0
    linear 0.3 alpha 1.0
    linear 0.2 alpha 0.0
    pause 4.0
    repeat
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
