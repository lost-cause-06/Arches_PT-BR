label keepgoing:
    $ persistent.musicon = False
    $ persistent.act_2 = False
    $ persistent.goingincircles = False
    $ quick_menu = False
    stop music fadeout 1
    stop ambient fadeout 1
    scene black with slow_dissolve
    play sound reverse fadein 2.0
    pause 0.5
    #B8
    scene something #with fast_dissolve
    pause 0.03
    scene hope9 #with fast_dissolve
    pause 0.03
    scene realization #with fast_dissolve
    pause 0.03
    scene kitchen8 #with fast_dissolve
    pause 0.03

    #B7
    scene the_arch2 #with fast_dissolve
    pause 0.03
    scene the_divide3 #with fast_dissolve
    pause 0.03
    scene circles #with fast_dissolve
    pause 0.03
    scene catastrophic_failure2 #with fast_dissolve
    pause 0.03
    scene headlights #with fast_dissolve
    pause 0.03
    scene camforest #with fast_dissolve
    pause 0.03
    #B6
    scene choke2 #with fast_dissolve
    pause 0.03
    scene struggle2 #with fast_dissolve
    pause 0.03
    scene victims_4 #with fast_dissolve
    pause 0.03
    scene trailer4 #with fast_dissolve
    pause 0.03
    #B5
    scene psilocybin #with fast_dissolve
    pause 0.03
    scene mirror3 #with fast_dissolve
    pause 0.03
    scene brian #with fast_dissolve
    pause 0.03
    #B4
    scene forest_shadow #with fast_dissolve
    pause 0.03
    scene panic #with fast_dissolve
    pause 0.03
    #B3
    scene fight2 #with fast_dissolve
    pause 0.03
    scene blazed #with fast_dissolve
    pause 0.03
    #B2
    scene cam_lake_1 #with fast_dissolve
    pause 0.03
    scene car_3 #with fast_dissolve
    pause 0.03
    #B1
    scene closet_3 #with fast_dissolve
    pause 0.03
    scene lake_emma_1 #with fast_dissolve
    pause 0.03
    scene no_help_2 #with fast_dissolve
    pause 0.5

    scene black
    pause 3.0
    $ persistent.removeload = True
    $ persistent.act_2 = False
    $ persistent.musicon = False
    $ persistent.shortstory1 = True
    $ persistent.shortstory2 = True
    $ persistent.goingincircles = False
    return
